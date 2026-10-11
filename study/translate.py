"""Turn a bank passage into Russian without changing numbers or exam terms.

The stored English text stays the source. A translation is only for reading.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from study.bank import repo_root
from study.llm import OllamaLLM

EXAM_TERMS = (
    "half-life",
    "DVH",
    "GTV",
    "CTV",
    "PTV",
    "MU",
    "SSD",
    "SAD",
    "PDD",
    "TMR",
    "QUANTEC",
    "HDR",
    "Khan",
    "Bentel",
    "ALARA",
)

PROMPT = (
    "Ты переводчик. Ответь только по-русски. "
    "Не копируй английский абзац. Не добавляй фактов. "
    "Числа, формулы и термины экзамена оставь как есть: "
    + ", ".join(EXAM_TERMS)
    + "."
)

_NUMBER = re.compile(r"\d+(?:\.\d+)?")


class Translator:
    def __init__(self, llm: OllamaLLM | None = None, path: Path | None = None):
        self.llm = llm or OllamaLLM()
        self.path = path or (repo_root() / "progress" / "ru_cache.json")
        self.cache: dict[str, str] = {}
        if self.path.exists():
            self.cache = json.loads(self.path.read_text(encoding="utf-8"))

    def __call__(self, text: str) -> str:
        key = text.strip()
        if not key:
            return text
        cached = self.cache.get(key)
        if cached and _usable(key, cached):
            return cached
        out = "\n\n".join(self._one(part) for part in _pieces(key))
        if not _usable(key, out):
            return text
        self.cache[key] = out
        self._save()
        return out

    def _one(self, part: str) -> str:
        cached = self.cache.get(part)
        if cached and _usable(part, cached):
            return cached
        try:
            out = self.llm.complete(
                [
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": part},
                ],
                max_tokens=500,
            )
        except RuntimeError:
            return part
        out = out.strip()
        if not _usable(part, out):
            return part
        self.cache[part] = out
        return out

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2), encoding="utf-8")


def _pieces(text: str, limit: int = 500) -> list[str]:
    blocks = [block.strip() for block in text.split("\n\n") if block.strip()]
    if not blocks:
        blocks = [text.strip()]
    pieces: list[str] = []
    current = ""
    for block in blocks:
        if len(current) + len(block) + 2 > limit and current:
            pieces.append(current)
            current = block
        else:
            current = f"{current}\n\n{block}".strip()
    if current:
        pieces.append(current)
    return pieces


def _same_english(source: str, translated: str) -> bool:
    if source.strip() == translated.strip():
        return True
    letters = [ch for ch in translated if ch.isalpha()]
    if not letters:
        return True
    cyr = sum(1 for ch in letters if "а" <= ch.lower() <= "я" or ch.lower() == "ё")
    return cyr / len(letters) < 0.4


def _keeps_bank_tokens(source: str, translated: str) -> bool:
    if _NUMBER.findall(source) != _NUMBER.findall(translated):
        return False
    src = source.lower()
    out = translated.lower()
    for term in EXAM_TERMS:
        token = term.lower()
        if token in src and token not in out:
            return False
    return True


def _usable(source: str, translated: str) -> bool:
    return not _same_english(source, translated) and _keeps_bank_tokens(source, translated)
