"""Messenger-free rehearsal of the chat loop.

The same functions print the messages a bot would send. Telegram is not called.
Each run uses its own progress file.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.request import Request, urlopen

from study.bank import Item, find_module, load_modules
from study.engine import Progress, grade_choice
from study.judge import CrossEncoderJudge
from study.llm import OllamaLLM

SECRET = "ФРАЗА-ДЛИННОГО-ЧАТА-НЕ-ДЛЯ-ЛЕНТЫ"
JUDGE_QUESTION = (
    "Is this source useful for a person studying the MDCB medical dosimetrist "
    "certification exam, dose calculation, or radiation oncology planning?"
)


@dataclass
class Log:
    channel: list[str] = field(default_factory=list)
    session: list[str] = field(default_factory=list)

    def bot_channel(self, text: str) -> None:
        self.channel.append(f"БОТ\n{text}")

    def human_channel(self, text: str) -> None:
        self.channel.append(f"ЛИКА\n{text}")

    def bot_session(self, text: str) -> None:
        self.session.append(f"БОТ\n{text}")

    def human_session(self, text: str) -> None:
        self.session.append(f"ЛИКА\n{text}")


def card_text(item: Item) -> str:
    lines = [
        f"Карточка · {item.module}",
        item.lesson,
        "",
        item.stem,
        "",
    ]
    for letter in "ABCD":
        lines.append(f"{letter}. {item.choices[letter]}")
    lines.extend(["", "Напиши букву. Ответа и конспекта в этом сообщении нет."])
    text = "\n".join(lines)
    if item.why and item.why in text:
        raise RuntimeError("карточка показала конспект")
    return text


def reveal_text(item: Item) -> str:
    return "\n".join(
        [
            f"Конспект после оценки · {item.lesson}",
            "",
            f"{item.answer}. {item.answer_text}",
            "",
            item.why,
        ]
    )


def session_invite() -> str:
    return "\n".join(
        [
            "Отдельная сессия",
            "Это не карточка канала. Переписка остаётся здесь.",
            "Команда была бы: открыть второй чат.",
        ]
    )


def one_question(reply: str) -> str:
    """Keep a single question if the model writes more than one."""
    text = reply.strip()
    if text.count("?") > 1:
        text = text.split("?")[0].strip() + "?"
    return text


def run_cards(progress_path: Path) -> Log:
    log = Log()
    progress = Progress(progress_path)
    module = find_module(load_modules(), "radioactivity")
    if module is None:
        raise RuntimeError("нет модуля radioactivity")
    item = next(piece for piece in module.items if piece.channel == "ear")
    card = card_text(item)
    log.bot_channel(card)
    log.human_channel("B")
    grade = grade_choice(item, "B")
    progress.record(item.id, grade.ok)
    if item.why in card:
        raise RuntimeError("конспект попал в карточку до оценки")
    log.bot_channel(reveal_text(item))
    log.bot_session(session_invite())
    log.human_session(SECRET)
    log.bot_session("Приняла. Это остаётся в этой сессии.")
    feed = "\n".join(log.channel)
    if SECRET in feed:
        raise RuntimeError("фраза длинного чата попала в ленту")
    if item.why not in log.channel[-1]:
        raise RuntimeError("после оценки конспект не пришёл")
    return log


def run_dialogue(progress_path: Path, llm: OllamaLLM | None = None) -> tuple[Log, str]:
    log = Log()
    module = find_module(load_modules(), "radioactivity")
    item = next(
        piece
        for piece in module.items
        if piece.channel == "ear" and "HDR remote-afterloader" in piece.stem
    )
    log.bot_session(session_invite())
    log.human_session("Напомни half-life Ir-192 и спроси меня один раз.")
    model = llm or OllamaLLM()
    reply = model.complete(
        [
            {
                "role": "system",
                "content": (
                    "Ты ведёшь один голосовой вопрос к экзамену MDCB. "
                    "Говори по-русски, термин Ir-192 оставь по-английски. "
                    "Задай ровно один вопрос и поставь один знак вопроса. "
                    "Не называй число 73.8 и не называй ответ, пока человек не ответил. "
                    "Не придумывай дозу в Gy. Тема: half-life источника HDR."
                ),
            },
            {"role": "user", "content": log.session[-1].split("\n", 1)[1]},
        ],
        max_tokens=120,
    )
    question = one_question(reply)
    if question.count("?") != 1:
        raise RuntimeError(f"модель задала не один вопрос: {question}")
    log.bot_session(question)
    log.human_session("73.8 days")
    grade_line = "Коротко: это совпало с банком, Ir-192, 73.8 days."
    log.bot_session(grade_line)
    return log, question


def visible_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "lika-cert-prep-sim"})
    with urlopen(request, timeout=30) as response:
        raw = response.read().decode("utf-8", errors="replace")
    raw = raw.replace("&nbsp;", " ")
    raw = re.sub(r"(?is)<script.*?>.*?</script>", " ", raw)
    raw = re.sub(r"(?is)<style.*?>.*?</style>", " ", raw)
    return " ".join(re.sub(r"<[^>]+>", " ", raw).split())


def fetch_relevant() -> str:
    text = visible_text("https://www.mdcb.org/certification-exam-information/exam-development")
    mark = text.lower().find("treatment planning in radiation oncology")
    if mark < 0:
        raise RuntimeError("на живой странице MDCB нет абзаца про учебники")
    return text[max(0, mark - 180) : mark + 700]


def fetch_junk() -> str:
    return visible_text("https://go.dev/doc/install")[:1500]


def run_materials(judge: CrossEncoderJudge | None = None) -> dict[str, float]:
    model = judge or CrossEncoderJudge()
    relevant = fetch_relevant()
    junk = fetch_junk()
    scores = {
        "mdcb": model.yes_probability(JUDGE_QUESTION, relevant),
        "golang": model.yes_probability(JUDGE_QUESTION, junk),
    }
    # This local cross-encoder puts a real dosimetry paragraph near 0.2
    # and an unrelated install page near 0. A 0.5 cutoff would reject both.
    if not (scores["mdcb"] >= 0.15 and scores["golang"] <= 0.05 and scores["mdcb"] > scores["golang"] * 50):
        raise RuntimeError(f"судья не отделил материал: {scores}")
    return scores


def write_log(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    import sys

    command = (argv or sys.argv[1:])[0]
    out = Path("tests/messenger_sim/runs")
    if command == "cards":
        log = run_cards(Path("/tmp/lika-sim-cards.json"))
        write_log(out / "cards.md", "Короткие карточки", "\n\n".join(log.channel + ["--- сессия ---"] + log.session))
        print((out / "cards.md").read_text(encoding="utf-8"))
        return 0
    if command == "dialogue":
        log, question = run_dialogue(Path("/tmp/lika-sim-dialogue.json"))
        write_log(out / "dialogue.md", "Длинный диалог", "\n\n".join(log.session) + f"\n\nВопросов в ответе модели: {question.count('?')}")
        print((out / "dialogue.md").read_text(encoding="utf-8"))
        return 0
    if command == "materials":
        scores = run_materials()
        card = channel_message_from_source(scores["mdcb"])
        body = card + f"\n\nСудья MDCB: {scores['mdcb']:.3f}\nСудья Go: {scores['golang']:.3f}\n"
        write_log(out / "materials.md", "Материалы", body)
        print(body)
        return 0
    print("cards | dialogue | materials")
    return 1


def channel_message_from_source(score: float) -> str:
    return "\n".join(
        [
            "Карточка · материал",
            "MDCB exam references",
            "",
            f"Судья: да, {score:.2f}. Это живая страница про то, из чего пишут вопросы экзамена.",
            "https://www.mdcb.org/certification-exam-information/exam-development",
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
