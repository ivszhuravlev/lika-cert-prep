"""Session rules: the bank grades, misses come back, the road pack stays ear-only."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from study.bank import Item, Module, parse_number, repo_root


@dataclass
class Grade:
    ok: bool
    expected: str
    why: str
    number: float | None


class Progress:
    def __init__(self, path: Path):
        self.path = path
        self.items: dict[str, dict] = {}
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            self.items = data.get("items", {})

    def get(self, item_id: str) -> dict:
        return self.items.get(item_id, {"wrong": 0, "streak": 0, "last": ""})

    def record(self, item_id: str, ok: bool) -> None:
        state = self.get(item_id)
        if ok:
            state["streak"] = int(state.get("streak", 0)) + 1
            state["last"] = "ok"
        else:
            state["wrong"] = int(state.get("wrong", 0)) + 1
            state["streak"] = 0
            state["last"] = "wrong"
        self.items[item_id] = state
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"items": self.items}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def rank(item: Item, progress: Progress) -> tuple:
    state = progress.get(item.id)
    streak = int(state.get("streak", 0))
    wrong = int(state.get("wrong", 0))
    last = state.get("last", "")
    if last == "wrong":
        bucket = 0
    elif streak >= 3:
        bucket = 2
    else:
        bucket = 1
    return (bucket, -wrong, item.id)


def ordered(items: list[Item], progress: Progress, *, ear_only: bool = False) -> list[Item]:
    pool = [item for item in items if item.channel == "ear"] if ear_only else list(items)
    return sorted(pool, key=lambda item: rank(item, progress))


def problems(items: list[Item]) -> list[Item]:
    return [item for item in items if item.channel == "paper" and item.number is not None]


def close_enough(got: float, want: float) -> bool:
    if want == 0:
        return abs(got) < 1e-6
    return abs(got - want) / abs(want) <= 0.02 or abs(got - want) <= 0.01


def grade_choice(item: Item, raw: str) -> Grade:
    text = raw.strip().upper()
    letter = text[:1]
    ok = letter == item.answer or raw.strip().lower() == item.answer_text.lower()
    return Grade(ok, f"{item.answer}. {item.answer_text}", item.why, item.number)


def grade_number(item: Item, raw: str) -> Grade:
    if item.number is None:
        return Grade(False, item.answer_text, item.why, None)
    got = parse_number(raw)
    ok = got is not None and close_enough(got, item.number)
    if not ok and raw.strip().lower() == item.answer_text.lower():
        ok = True
    return Grade(ok, item.answer_text, item.why, item.number)


def road_prompt(module: Module, progress: Progress, per_block: int = 8) -> str:
    """Prompt Lika pastes into a voice chat. Answers are in the prompt; the model waits to say them."""
    items = [item for item in ordered(module.items, progress, ear_only=True) if rank(item, progress)[0] < 2]
    if len(items) < 4:
        items = ordered(module.items, progress, ear_only=True)
    items = items[: per_block * 3]
    if not items:
        return ""
    blocks = [items[index : index + per_block] for index in range(0, len(items), per_block)]
    lines = [
        "Ты ведёшь голосовую тренировку к экзамену MDCB CMD. Говори по-русски. "
        "Термины экзамена оставляй по-английски: half-life, Compton, photoelectric, GTV, CTV, PTV, ICRU, HDR.",
        "Правила:",
        "- Один вопрос за раз. Прочитай ствол и варианты A–D. Замолчи и жди ответ.",
        "- Не называй верный вариант, пока она не ответит.",
        "- После ответа скажи букву и разбор из поля Why этого вопроса. Не добавляй чисел, доз и лимитов, которых нет в этом промпте.",
        "- Если она просит объяснить термин ещё раз, используй только Why и ствол из пачки.",
        "- Блок длится 20–25 минут. После блока спроси, повторить блок, взять следующий или остановиться.",
        "- Задачи на MU, gap, HVL и DVH в эту пачку не входят. Если она просит такую задачу, скажи, что это домашний лист, и вернись к пачке.",
        f"Модуль: {module.title}.",
        "",
    ]
    for block_index, block in enumerate(blocks, start=1):
        lines.append(f"## Блок {block_index}")
        for number, item in enumerate(block, start=1):
            lines.append(f"### {number}. {item.lesson}")
            lines.append(item.stem)
            for letter in "ABCD":
                lines.append(f"{letter}. {item.choices[letter]}")
            lines.append(f"Верно: {item.answer}. {item.answer_text}")
            lines.append(f"Why: {item.why}")
            lines.append("")
    lines.append("Начни с блока 1, вопрос 1.")
    return "\n".join(lines)


def default_progress_path() -> Path:
    return repo_root() / "progress" / "lika.json"
