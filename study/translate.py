"""Turn a bank passage into Russian without changing numbers or exam terms.

The stored English text stays the source. A translation is only for reading.
"""

from __future__ import annotations

import json
from pathlib import Path

from study.bank import repo_root
from study.llm import OllamaLLM

PROMPT = (
    "Переведи текст на русский для подготовки к экзамену MDCB. "
    "Не меняй числа, единицы и формулы. "
    "Оставь по-английски термины экзамена: half-life, mean life, DVH, GTV, CTV, PTV, ITV, "
    "ICRU, MU, SSD, SAD, PDD, TMR, QUANTEC, HDR, LINAC, Khan, Bentel, Bragg, ALARA, OAR. "
    "Не добавляй фактов. Верни только перевод."
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
        if cached:
            return cached
        limit = min(1400, max(180, len(key) // 2))
        try:
            out = self.llm.complete(
                [
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": key},
                ],
                max_tokens=limit,
            )
        except RuntimeError:
            return text
        self.cache[key] = out
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2), encoding="utf-8")
        return out
