"""Turn a bank passage into Russian without changing numbers or exam terms.

The stored English text stays the source. A translation is only for reading.
"""

from __future__ import annotations

import json
from pathlib import Path

from study.bank import repo_root
from study.llm import OllamaLLM

PROMPT = (
    "Ты переводчик. Ответь только по-русски. "
    "Не копируй английский абзац. Не добавляй фактов. "
    "Числа, формулы и термины экзамена оставь как есть: half-life, DVH, GTV, CTV, PTV, "
    "MU, SSD, SAD, PDD, TMR, QUANTEC, HDR, Khan, Bentel, ALARA."
)


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
        if cached and not _same_english(key, cached):
            return cached
        parts = _pieces(key)
        translated = []
        for part in parts:
            translated.append(self._one(part))
        out = "\n\n".join(translated)
        if _same_english(key, out):
            return text
        self.cache[key] = out
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2), encoding="utf-8")
        return out

    def _one(self, part: str) -> str:
        cached = self.cache.get(part)
        if cached and not _same_english(part, cached):
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
        if _same_english(part, out):
            return part
        self.cache[part] = out
        return out


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
