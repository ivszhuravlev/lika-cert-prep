"""Telegram transport for the local study bank.

The bank still grades. This process only delivers messages.
The token is read from the environment or from a gitignored .env file.
"""

from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

from study.bank import find_module, load_modules, parse_number, repo_root
from study.engine import (
    Progress,
    default_progress_path,
    grade_choice,
    grade_number,
    ordered,
    problems,
    road_blocks,
)
from study.translate import Translator, _keeps_bank_tokens, _same_english

LABELS = {"exam": "Что спрашивают", "work": "Формула и пример", "trap": "Где срываются"}
MODES = {
    "теория": "theory",
    "задачи": "problems",
    "квиз": "quiz",
    "вместе": "mixed",
    "в дорогу": "road",
}
MODE_TITLE = {
    "theory": "теория",
    "problems": "задача",
    "quiz": "квиз",
    "mixed": "вместе",
    "road": "в дорогу",
}
TOPICS = {"к темам", "темы", "назад", "меню", "/themes"}
PENDING = "урок не выбран"
PH_HOME = "Выбери режим кнопкой"
PH_THEORY = "Теория: кнопка Дальше"
PH_LETTER = "Квиз: буква A B C D"
PH_MIXED = "Вместе: буква A B C D"
PH_NUMBER = "Задача: напиши число"
PH_ROAD = "В дорогу: скопируй блок"
RU_NOTE = (
    "Дальше теория, задачи, квиз и вместе по-русски. "
    "Числа и термины экзамена остаются как в банке. "
    "Букву и число проверяет банк. В дорогу копируется как в банке."
)
EN_NOTE = "Дальше теория, задачи, квиз и вместе на языке банка. Букву и число проверяет банк."
HOME = (
    "Модуль открыт. Урок начнётся после кнопки режима.\n"
    "Теория — текст урока, кнопка «Дальше».\n"
    "Задачи — в ответ число.\n"
    "Квиз — в ответ буква A, B, C или D.\n"
    "Вместе — абзац теории, потом вопросы к нему.\n"
    "В дорогу — блок для голосового чата, здесь на него не отвечают.\n"
    "«К темам» — список модулей.\n"
    "«Где я» — последний решённый квиз и задача. «Вопрос 12» открывает этот номер."
)
_CYR = str.maketrans(
    {
        "а": "A",
        "А": "A",
        "в": "B",
        "В": "B",
        "с": "C",
        "С": "C",
        "д": "D",
        "Д": "D",
        "е": "E",
        "Е": "E",
    }
)
_translator: Translator | None = None


def load_token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if token:
        return token
    env_path = repo_root() / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")


def _public_error(exc: BaseException, secret: str) -> str:
    text = str(exc)
    if secret:
        text = text.replace(secret, "…")
    return text


class Telegram:
    def __init__(self, token: str):
        self.base = f"https://api.telegram.org/bot{token}"

    def call(self, method: str, payload: dict | None = None) -> dict:
        data = urllib.parse.urlencode(payload or {}).encode()
        request = urllib.request.Request(self.base + "/" + method, data=data)
        with urllib.request.urlopen(request, timeout=70) as response:
            body = json.loads(response.read().decode())
        if not body.get("ok"):
            raise RuntimeError(body.get("description", method))
        return body["result"]

    def send(
        self,
        chat_id: int,
        text: str,
        *,
        keyboard: list | None = None,
        remove_keyboard: bool = False,
        placeholder: str | None = None,
    ) -> None:
        rows = None
        if keyboard:
            rows = keyboard if isinstance(keyboard[0], list) else [[label] for label in keyboard]
        markup = None
        if rows:
            markup = {"keyboard": rows, "resize_keyboard": True, "is_persistent": True}
            if placeholder:
                markup["input_field_placeholder"] = placeholder[:64]
        elif remove_keyboard:
            markup = {"remove_keyboard": True}
        for chunk in visible_parts(text):
            payload: dict = {"chat_id": chat_id, "text": chunk}
            if markup:
                payload["reply_markup"] = json.dumps(markup, ensure_ascii=False)
            self.call("sendMessage", payload)


def header_prefix(text: str) -> str:
    lines = text.splitlines()
    if len(lines) >= 2 and lines[0].startswith("Модуль ") and lines[1].startswith("Сейчас:"):
        return lines[0] + "\n" + lines[1] + "\n\n"
    return ""


def visible_parts(text: str, limit: int = 4096) -> list[str]:
    body = text or "Пусто."
    if len(body) <= limit:
        return [body]
    prefix = header_prefix(body)
    budget = max(limit - len(prefix), 800)
    parts: list[str] = []
    rest = body
    first = True
    while rest:
        room = limit if first else budget
        chunk = rest[:room]
        rest = rest[room:]
        if not first and prefix and not chunk.startswith("Модуль "):
            chunk = prefix + chunk
        parts.append(chunk)
        first = False
    return parts


class Session:
    def __init__(self, path: Path):
        self.path = path
        self.chats: dict[str, dict] = {}
        self.offset = 0
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("chats"), dict):
                self.chats = data["chats"]
                self.offset = int(data.get("offset") or 0)
            elif isinstance(data, dict):
                self.chats = data

    def get(self, chat_id: int) -> dict:
        return self.chats.setdefault(
            str(chat_id),
            {
                "module": "",
                "mode": "",
                "cursor": 0,
                "chunk_at": 0,
                "item_id": "",
                "phase": "",
                "lesson": "",
                "left": 0,
                "road_i": 0,
            },
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"offset": self.offset, "chats": self.chats}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def module_number(module) -> str:
    digits = module.code[1:]
    return str(int(digits)) if digits.isdigit() else module.code


def module_list() -> str:
    lines = [
        "Список модулей.",
        "Напиши номер. Откроется модуль, и внизу появятся кнопки режима.",
        "Из модуля кнопка «К темам» возвращает сюда.",
        "",
    ]
    found = False
    for module in load_modules():
        if module.chunks or module.items:
            found = True
            lines.append(f"{module_number(module)}  {module.title}")
    if not found:
        lines.append("Модулей пока нет.")
    return "\n".join(lines)


def normalize(text: str) -> str:
    low = " ".join(text.strip().lower().replace("«", "").replace("»", "").split())
    if low.startswith("/"):
        low = low.split("@", 1)[0]
    return low


def is_next(low: str) -> bool:
    return low.replace("e", "е") == "дальше"


def choice_letter(raw: str) -> str | None:
    text = raw.strip()
    low = normalize(text)
    for prefix in ("ответ", "answer"):
        if low.startswith(prefix + " ") or low == prefix:
            text = text[len(prefix) :].strip()
            break
    compact = text.translate(_CYR)
    for mark in (".", ")", ":", " "):
        compact = compact.replace(mark, "")
    if len(compact) != 1:
        return None
    letter = compact.upper()
    return letter if letter in "ABCD" else None


def keys(state: dict, action: list[str] | None = None, nav: list[str] | None = None) -> list[list[str]]:
    toggle = "English" if state.get("ru") else "По-русски"
    rows: list[list[str]] = []
    if nav:
        rows.append(nav)
    if action:
        rows.append(action)
    rows.extend(
        [
            ["Теория", "Задачи"],
            ["Квиз", "Вместе"],
            ["В дорогу", toggle],
            ["К темам"],
        ]
    )
    return rows


def clear_place(state: dict) -> None:
    state["module"] = ""
    state["mode"] = ""
    state["cursor"] = 0
    state["chunk_at"] = 0
    state["item_id"] = ""
    state["phase"] = ""
    state["lesson"] = ""
    state["left"] = 0
    state["road_i"] = 0
    state["deck"] = []
    state["deck_key"] = ""


def enter_mode(state: dict, mode: str) -> None:
    state["mode"] = mode
    state["cursor"] = 0
    state["chunk_at"] = 0
    state["item_id"] = ""
    state["phase"] = ""
    state["lesson"] = ""
    state["left"] = 0
    state["road_i"] = 0
    state["deck"] = []
    state["deck_key"] = ""


def header(state: dict, module, lesson: str) -> str:
    mode = MODE_TITLE.get(state.get("mode") or "", "меню")
    name = (lesson or "").strip() or PENDING
    return f"Модуль {module_number(module)} · {module.title}\nСейчас: {mode} · {name}"


def frame(state: dict, module, lesson: str, body: str, hint: str) -> str:
    name = (lesson or "").strip() or PENDING
    mode = MODE_TITLE.get(state.get("mode") or "", "меню")
    return f"{header(state, module, name)}\n\n{body.strip()}\n\n— {mode} · {name}. {hint}"


def brief(state: dict, module, lesson: str, line: str) -> str:
    return f"{header(state, module, lesson)}\n\n{line.strip()}"


def body_pages(head: str, body: str, limit: int = 3900) -> list[str]:
    """Split a lesson so each Telegram bubble is one complete piece."""
    text = body.strip() or "Пусто."
    room = limit - len(head) - 2
    if room < 700:
        room = 700
    if len(head) + 2 + len(text) <= limit:
        return [text]
    pages: list[str] = []
    rest = text
    while rest:
        if len(rest) <= room:
            pages.append(rest)
            break
        cut = rest.rfind("\n\n", 0, room)
        if cut < room // 3:
            cut = rest.rfind("\n", 0, room)
        if cut < room // 3:
            cut = room
        pages.append(rest[:cut].rstrip())
        rest = rest[cut:].lstrip("\n")
    return pages


def current_module(state: dict):
    code = state.get("module") or ""
    if not code:
        return None
    return find_module(load_modules(), code)


def exact_module(name: str):
    key = " ".join(name.strip().lower().split())
    if not key or key in {"a", "b", "c", "d"}:
        return None
    for module in load_modules():
        if key in {module.code.lower(), module.slug.lower(), module.title.lower()}:
            return module
        if key.isdigit() and module.code == f"m{int(key):02d}":
            return module
    return None


def waiting(state: dict) -> bool:
    return bool(state.get("item_id")) and state.get("mode") in {"quiz", "problems", "mixed"}


def item_by_id(module, item_id: str):
    if module is None or not item_id:
        return None
    return next((piece for piece in module.items if piece.id == item_id), None)


def russian(state: dict, text: str) -> str:
    if not state.get("ru"):
        return text
    global _translator
    if _translator is None:
        _translator = Translator()
    out = _translator(text)
    if _same_english(text, out) or not _keeps_bank_tokens(text, out):
        return "Перевод не получился, оставляю английский.\n\n" + text
    return out


def question_body(item, progress: Progress, state: dict, *, numeric: bool) -> str:
    lines: list[str] = []
    if progress.get(item.id).get("last") == "wrong":
        lines.extend(["Снова: прошлая попытка мимо.", ""])
    lines.append(russian(state, item.stem))
    if not numeric:
        lines.append("")
        for letter in "ABCD":
            lines.append(f"{letter}. {russian(state, item.choices[letter])}")
    return "\n".join(lines)


def _parsed_label(value: float) -> str:
    return f"{value:.10g}"


def reveal_text(grade, state: dict, *, numeric: bool, echo: bool = True) -> str:
    if grade.ok:
        head = "Верно."
    elif numeric:
        head = "Не сошлось."
    else:
        head = "Мимо."
    if numeric:
        shown = grade.expected
    else:
        letter, sep, rest = grade.expected.partition(". ")
        shown = f"{letter}. {russian(state, rest)}" if sep else grade.expected
    why = russian(state, grade.why)
    base = f"{head} В банке: {shown}\nРазбор: {why}"
    parsed = getattr(grade, "parsed", None)
    if not (numeric and echo and parsed is not None):
        return base
    echoed = f"{head} Прочитано: {_parsed_label(parsed)}.\nВ банке: {shown}\nРазбор: {why}"
    return echoed


def deliver(
    tg: Telegram,
    chat_id: int,
    text: str,
    *,
    keyboard: list | None = None,
    remove_keyboard: bool = False,
    placeholder: str | None = None,
) -> None:
    tg.send(
        chat_id,
        text,
        keyboard=keyboard,
        remove_keyboard=remove_keyboard,
        placeholder=placeholder,
    )


def show_topics(tg: Telegram, chat_id: int, state: dict, lead: str = "") -> None:
    clear_place(state)
    text = module_list() if not lead else lead.rstrip() + "\n\n" + module_list()
    deliver(tg, chat_id, text, remove_keyboard=True)


def open_module(tg: Telegram, chat_id: int, state: dict, module) -> None:
    state["module"] = module.code
    state["mode"] = ""
    state["cursor"] = 0
    state["chunk_at"] = 0
    state["item_id"] = ""
    state["phase"] = ""
    state["lesson"] = ""
    state["left"] = 0
    state["road_i"] = 0
    state["deck"] = []
    state["deck_key"] = ""
    deliver(
        tg,
        chat_id,
        frame(state, module, PENDING, HOME, "К темам — к списку"),
        keyboard=keys(state),
        placeholder=PH_HOME,
    )


def show_chunk(
    tg: Telegram,
    chat_id: int,
    state: dict,
    module,
    chunk,
    *,
    next_button: bool,
    stamp: str,
    preface: str = "",
) -> None:
    state["lesson"] = chunk.lesson
    state["item_id"] = ""
    body = russian(state, chunk.text)
    if preface:
        body = preface.strip() + "\n\n" + body
    head = header(state, module, chunk.lesson)
    pages = body_pages(head, body)
    page = int(state.get("page") or 0)
    if page < 0 or page >= len(pages):
        page = 0
    state["page"] = page
    if next_button and state.get("mode") == "mixed":
        placeholder = "Вместе: кнопка Дальше"
    elif next_button:
        placeholder = PH_THEORY
    else:
        placeholder = PH_HOME
    deliver(
        tg,
        chat_id,
        f"{head}\n\n{pages[page]}",
        keyboard=keys(state),
        placeholder=placeholder,
    )
    if len(pages) > 1:
        line = f"{stamp}, часть {page + 1} из {len(pages)}.\nКнопка «Дальше»."
    else:
        line = f"{stamp}.\nКнопка «Дальше»."
    deliver(
        tg,
        chat_id,
        brief(state, module, chunk.lesson, line),
        keyboard=keys(state, ["Дальше"] if next_button else None),
        placeholder=placeholder,
    )


def emit_item(
    tg: Telegram,
    chat_id: int,
    state: dict,
    module,
    progress: Progress,
    item,
    *,
    preface: str = "",
) -> None:
    state["item_id"] = item.id
    state["lesson"] = item.lesson
    numeric = state.get("mode") == "problems"
    if numeric:
        action = "Задача. Напиши число: оно уйдёт в проверку. Другой модуль — сначала «К темам»."
        row = None
        placeholder = PH_NUMBER
        hint = "Число или К темам"
    elif state.get("mode") == "mixed":
        action = "Вместе, сейчас вопрос. Нажми A, B, C или D. Другой модуль — сначала «К темам»."
        row = ["A", "B", "C", "D"]
        placeholder = PH_MIXED
        hint = "Буква или К темам"
    else:
        action = ""
        row = ["A", "B", "C", "D"]
        placeholder = PH_LETTER
        hint = "A–D, Предыдущий или Следующий"
    pool = question_deck(state, module, progress) if state.get("mode") in {"quiz", "problems"} else []
    total = len(pool)
    number = int(state.get("cursor", 0)) + 1 if total else 0
    label = f"Вопрос {number} из {total}" if total else ""
    bits = [preface, action, label, question_body(item, progress, state, numeric=numeric)]
    nav = ["Предыдущий", "Следующий"] if state.get("mode") in {"quiz", "problems"} else None
    deliver(
        tg,
        chat_id,
        frame(state, module, item.lesson, "\n\n".join(bit for bit in bits if bit), hint),
        keyboard=keys(state, row, nav),
        placeholder=placeholder,
    )


def reshow(tg: Telegram, chat_id: int, state: dict, progress: Progress, preface: str) -> bool:
    module = current_module(state)
    if module is None:
        return False
    mode = state.get("mode")
    item = item_by_id(module, state.get("item_id") or "")
    if item is not None and mode in {"quiz", "problems", "mixed"}:
        emit_item(tg, chat_id, state, module, progress, item, preface=preface)
        return True
    if mode == "theory" and module.chunks:
        index = int(state.get("chunk_at", 0)) - 1
        if 0 <= index < len(module.chunks):
            chunk = module.chunks[index]
            show_chunk(
                tg,
                chat_id,
                state,
                module,
                chunk,
                next_button=True,
                stamp=f"Блок {index + 1} из {len(module.chunks)}",
                preface=preface,
            )
            return True
    return False


def show_language(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    note = RU_NOTE if state.get("ru") else EN_NOTE
    if reshow(tg, chat_id, state, progress, note):
        return
    module = current_module(state)
    if module is None:
        show_topics(tg, chat_id, state, note)
        return
    row = road_row(state, module, progress) if state.get("mode") == "road" else None
    placeholder = PH_ROAD if state.get("mode") == "road" else PH_HOME
    deliver(
        tg,
        chat_id,
        frame(state, module, state.get("lesson") or PENDING, note, "К темам — к списку"),
        keyboard=keys(state, row),
        placeholder=placeholder,
    )


def question_pool(state: dict, module, progress: Progress) -> list:
    mode = state.get("mode")
    if mode == "problems":
        return problems(ordered(module.items, progress))
    items = ordered(module.items, progress)
    if mode == "mixed" and state.get("lesson"):
        return [item for item in items if item.lesson == state["lesson"]]
    return items


def question_deck(state: dict, module, progress: Progress) -> list:
    """Quiz and problems stay in one list until the mode is opened again."""
    if state.get("mode") not in {"quiz", "problems"}:
        return question_pool(state, module, progress)
    key = f"{module.code}:{state.get('mode')}"
    if state.get("deck_key") != key or not state.get("deck"):
        state["deck"] = [item.id for item in question_pool(state, module, progress)]
        state["deck_key"] = key
    found = [item_by_id(module, item_id) for item_id in state["deck"]]
    return [item for item in found if item is not None]


def step_theory(tg: Telegram, chat_id: int, state: dict, module) -> None:
    if not module.chunks:
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                PENDING,
                "Текста теории в этом модуле нет. Выбери другой режим или «К темам».",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    index = int(state.get("chunk_at", 0))
    if index >= len(module.chunks):
        lesson = state.get("lesson") or module.chunks[-1].lesson
        text = frame(
            state,
            module,
            lesson,
            "Теория модуля кончилась. Выбери другой режим или «К темам».",
            "К темам — к списку",
        )
        state["mode"] = ""
        state["item_id"] = ""
        deliver(tg, chat_id, text, keyboard=keys(state), placeholder=PH_HOME)
        return
    chunk = module.chunks[index]
    state["chunk_at"] = index + 1
    state["page"] = 0
    show_chunk(
        tg,
        chat_id,
        state,
        module,
        chunk,
        next_button=True,
        stamp=f"Блок {index + 1} из {len(module.chunks)}",
    )


def block_lesson(block: str, module) -> str:
    for line in block.splitlines():
        if line.startswith("### ") and ". " in line:
            return line.split(". ", 1)[1].strip() or PENDING
    if module.lessons:
        return module.lessons[0]
    return PENDING


def road_row(state: dict, module, progress: Progress) -> list[str] | None:
    total = len(road_blocks(module, progress))
    if int(state.get("road_i", 0)) < total:
        return ["Следующий блок"]
    return None


def step_road(tg: Telegram, chat_id: int, state: dict, module, progress: Progress) -> None:
    blocks = road_blocks(module, progress)
    if not blocks:
        text = frame(
            state,
            module,
            PENDING,
            "Слуховых вопросов в этом модуле нет. Выбери другой режим или «К темам».",
            "К темам — к списку",
        )
        state["mode"] = ""
        state["item_id"] = ""
        deliver(tg, chat_id, text, keyboard=keys(state), placeholder=PH_HOME)
        return
    index = int(state.get("road_i", 0))
    if index >= len(blocks):
        text = frame(
            state,
            module,
            state.get("lesson") or PENDING,
            "Блоки «в дорогу» кончились. «В дорогу» начнёт сначала. «К темам» — список модулей.",
            "К темам — к списку",
        )
        state["mode"] = ""
        state["item_id"] = ""
        deliver(tg, chat_id, text, keyboard=keys(state), placeholder=PH_HOME)
        return
    block = blocks[index]
    lesson = block_lesson(block, module)
    state["lesson"] = lesson
    state["item_id"] = ""
    more = index + 1 < len(blocks)
    row = ["Следующий блок"] if more else None
    paste = header(state, module, lesson) + "\n\n" + block
    if len(paste) > 4096:
        paste = block
    deliver(
        tg,
        chat_id,
        paste,
        keyboard=keys(state, row),
        placeholder=PH_ROAD,
    )
    state["road_i"] = index + 1
    if more:
        line = f"Блок {index + 1} из {len(blocks)}.\nСкопируй сообщение выше.\nКнопка «Следующий блок»."
    else:
        line = f"Блок {index + 1} из {len(blocks)}, последний.\nСкопируй сообщение выше."
    deliver(
        tg,
        chat_id,
        brief(state, module, lesson, line),
        keyboard=keys(state, row),
        placeholder=PH_ROAD,
    )


def step_mixed_paragraph(tg: Telegram, chat_id: int, state: dict, module, progress: Progress) -> bool:
    index = int(state.get("chunk_at", 0)) % len(module.chunks)
    chunk = module.chunks[index]
    state["chunk_at"] = index + 1
    state["lesson"] = chunk.lesson
    state["item_id"] = ""
    state["cursor"] = 0
    same = [item for item in ordered(module.items, progress) if item.lesson == chunk.lesson]
    total = len(module.chunks)
    shown = index + 1
    if same:
        state["phase"] = "quiz"
        state["left"] = min(3, len(same))
        state["page"] = 0
        show_chunk(
            tg,
            chat_id,
            state,
            module,
            chunk,
            next_button=True,
            stamp=f"Абзац {shown} из {total}. Дальше — вопрос",
        )
        return False
    state["phase"] = "read"
    state["page"] = 0
    show_chunk(
        tg,
        chat_id,
        state,
        module,
        chunk,
        next_button=True,
        stamp=f"Абзац {shown} из {total}. Дальше — следующий абзац",
    )
    return False


def step_question(tg: Telegram, chat_id: int, state: dict, module, progress: Progress) -> None:
    pool = question_deck(state, module, progress)
    if not pool:
        state["item_id"] = ""
        state["phase"] = ""
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                state.get("lesson") or PENDING,
                "В этом режиме вопросов нет. Выбери другой режим или «К темам».",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    index = int(state.get("cursor", 0)) % len(pool)
    item = pool[index]
    if state.get("mode") == "mixed":
        state["cursor"] = index + 1
    else:
        state["cursor"] = index
    if state.get("mode") == "mixed" and state.get("phase") == "quiz":
        left = int(state.get("left") or 0)
        if left:
            state["left"] = left - 1
            if state["left"] <= 0:
                state["phase"] = ""
    emit_item(tg, chat_id, state, module, progress, item)


def ask_next(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    module = current_module(state)
    if module is None:
        show_topics(tg, chat_id, state)
        return
    mode = state.get("mode") or ""
    if mode == "theory":
        step_theory(tg, chat_id, state, module)
        return
    if mode == "road":
        step_road(tg, chat_id, state, module, progress)
        return
    if mode == "mixed" and state.get("phase") != "quiz":
        if module.chunks:
            step_mixed_paragraph(tg, chat_id, state, module, progress)
            return
        state["phase"] = "quiz"
    step_question(tg, chat_id, state, module, progress)


def move_question(tg: Telegram, chat_id: int, state: dict, progress: Progress, delta: int) -> None:
    if state.get("mode") not in {"quiz", "problems"}:
        module = current_module(state)
        if module is None:
            show_topics(tg, chat_id, state, "Предыдущий и Следующий листают квиз и задачи.")
            return
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                state.get("lesson") or PENDING,
                "Предыдущий и Следующий листают квиз и задачи.",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    module = current_module(state)
    if module is None:
        show_topics(tg, chat_id, state)
        return
    pool = question_deck(state, module, progress)
    if not pool:
        step_question(tg, chat_id, state, module, progress)
        return
    index = (int(state.get("cursor", 0)) + delta) % len(pool)
    state["cursor"] = index
    state["item_id"] = ""
    step_question(tg, chat_id, state, module, progress)


def explain_road(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    module = current_module(state)
    if module is None:
        show_topics(tg, chat_id, state, "Сначала номер модуля.")
        return
    deliver(
        tg,
        chat_id,
        frame(
            state,
            module,
            state.get("lesson") or PENDING,
            "Это «в дорогу». Буквы здесь не ответ. Скопируй блок в голосовой чат. «К темам» — список модулей.",
            "К темам — к списку",
        ),
        keyboard=keys(state, road_row(state, module, progress)),
        placeholder=PH_ROAD,
    )


def on_next(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    if state.get("mode") == "theory":
        module = current_module(state)
        index = int(state.get("chunk_at", 0)) - 1
        if module is not None and 0 <= index < len(module.chunks):
            chunk = module.chunks[index]
            head = header(state, module, chunk.lesson)
            pages = body_pages(head, russian(state, chunk.text))
            if int(state.get("page") or 0) + 1 < len(pages):
                state["page"] = int(state.get("page") or 0) + 1
                show_chunk(
                    tg,
                    chat_id,
                    state,
                    module,
                    chunk,
                    next_button=True,
                    stamp=f"Блок {index + 1} из {len(module.chunks)}",
                )
                return
        ask_next(tg, chat_id, state, progress)
        return
    module = current_module(state)
    if waiting(state) and module is not None:
        item = item_by_id(module, state.get("item_id") or "")
        if item is not None:
            emit_item(
                tg,
                chat_id,
                state,
                module,
                progress,
                item,
                preface="«Дальше» листает теорию. Здесь нужен ответ. Это не записано.",
            )
            return
    if state.get("mode") == "mixed":
        if module is None:
            show_topics(tg, chat_id, state, "Сначала номер модуля.")
            return
        if state.get("phase") == "quiz":
            step_question(tg, chat_id, state, module, progress)
            return
        ask_next(tg, chat_id, state, progress)
        return
    if module is not None:
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                state.get("lesson") or PENDING,
                "«Дальше» листает теорию. Сейчас открой режим кнопкой.",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    show_topics(tg, chat_id, state, "«Дальше» листает теорию. Сначала номер модуля.")


def on_block(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    if state.get("mode") == "road":
        ask_next(tg, chat_id, state, progress)
        return
    module = current_module(state)
    if waiting(state) and module is not None:
        item = item_by_id(module, state.get("item_id") or "")
        if item is not None:
            emit_item(
                tg,
                chat_id,
                state,
                module,
                progress,
                item,
                preface="«Следующий блок» относится к «в дорогу». Здесь нужен ответ. Это не записано.",
            )
            return
    if module is not None:
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                state.get("lesson") or PENDING,
                "«Следующий блок» включается в режиме «В дорогу».",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    show_topics(tg, chat_id, state, "«Следующий блок» включается в режиме «В дорогу». Сначала номер модуля.")


def take_answer(tg: Telegram, chat_id: int, raw: str, state: dict, progress: Progress) -> None:
    module = current_module(state)
    item = item_by_id(module, state.get("item_id") or "")
    if module is None or item is None:
        state["item_id"] = ""
        show_topics(tg, chat_id, state, "Вопрос уже не открыт.")
        return
    numeric = state.get("mode") == "problems"
    if numeric:
        if parse_number(raw) is None and raw.strip().lower() != item.answer_text.lower():
            emit_item(
                tg,
                chat_id,
                state,
                module,
                progress,
                item,
                preface="Нужно число. Это не записано как ответ.",
            )
            return
        grade = grade_number(item, raw)
    else:
        letter = choice_letter(raw)
        if letter is None and raw.strip().lower() != item.answer_text.lower():
            emit_item(
                tg,
                chat_id,
                state,
                module,
                progress,
                item,
                preface="Нужна буква A, B, C или D. Это не записано как ответ.",
            )
            return
        grade = grade_choice(item, letter or raw)
    progress.record(item.id, grade.ok)
    done = state.get("last_done")
    if not isinstance(done, dict):
        done = {}
        state["last_done"] = done
    done[f"{state.get('module')}:{state.get('mode')}"] = {
        "id": item.id,
        "n": int(state.get("cursor", 0)) + 1,
        "lesson": item.lesson,
        "ok": grade.ok,
    }
    state["item_id"] = ""
    nav = ["Предыдущий", "Следующий"] if state.get("mode") in {"quiz", "problems"} else None
    action = ["Дальше"] if state.get("mode") == "mixed" else None
    hint = "Предыдущий или Следующий" if nav else "Дальше или К темам"
    body = "Разбор ответа.\n\n" + reveal_text(grade, state, numeric=numeric)
    text = frame(state, module, item.lesson, body, hint)
    if len(text) > 4096:
        body = "Разбор ответа.\n\n" + reveal_text(grade, state, numeric=numeric, echo=False)
        text = frame(state, module, item.lesson, body, hint)
    deliver(
        tg,
        chat_id,
        text,
        keyboard=keys(state, action, nav),
        placeholder=PH_HOME,
    )


def jump_number(low: str) -> int | None:
    parts = low.split()
    if len(parts) == 2 and parts[0] in {"вопрос", "задача"} and parts[1].isdigit():
        return int(parts[1])
    return None


def show_mark(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    module = current_module(state)
    if module is None:
        show_topics(tg, chat_id, state, "Сначала номер модуля.")
        return
    done = state.get("last_done") if isinstance(state.get("last_done"), dict) else {}
    lines = []
    for mode, title in (("quiz", "Квиз"), ("problems", "Задачи")):
        row = done.get(f"{module.code}:{mode}") or {}
        if row:
            mark = "верно" if row.get("ok") else "мимо"
            lines.append(f"{title}: последний решённый — вопрос {row.get('n')}, {row.get('lesson')}, {mark}.")
        else:
            lines.append(f"{title}: в этом модуле ещё ничего не решено.")
    if state.get("mode") in {"quiz", "problems"} and state.get("deck"):
        lines.append(f"Сейчас открыт вопрос {int(state.get('cursor', 0)) + 1} из {len(state['deck'])}.")
    lines.append("По одному — кнопки «Предыдущий» и «Следующий». На номер напиши «вопрос 12».")
    nav = ["Предыдущий", "Следующий"] if state.get("mode") in {"quiz", "problems"} else None
    deliver(
        tg,
        chat_id,
        brief(state, module, state.get("lesson") or PENDING, "\n".join(lines)),
        keyboard=keys(state, nav=nav),
        placeholder=PH_HOME,
    )


def jump_question(tg: Telegram, chat_id: int, state: dict, progress: Progress, number: int) -> None:
    module = current_module(state)
    if module is None or state.get("mode") not in {"quiz", "problems"}:
        show_mark(tg, chat_id, state, progress)
        return
    pool = question_deck(state, module, progress)
    if not pool or number < 1 or number > len(pool):
        deliver(
            tg,
            chat_id,
            brief(state, module, state.get("lesson") or PENDING, f"В этом списке вопросы 1–{len(pool)}."),
            keyboard=keys(state, nav=["Предыдущий", "Следующий"]),
            placeholder=PH_HOME,
        )
        return
    state["cursor"] = number - 1
    state["item_id"] = ""
    step_question(tg, chat_id, state, module, progress)


def lost(tg: Telegram, chat_id: int, state: dict) -> None:
    module = current_module(state)
    if module is not None:
        deliver(
            tg,
            chat_id,
            frame(
                state,
                module,
                state.get("lesson") or PENDING,
                "Не разобрала сообщение. Режим — кнопкой внизу. «К темам» — список модулей.",
                "К темам — к списку",
            ),
            keyboard=keys(state),
            placeholder=PH_HOME,
        )
        return
    show_topics(tg, chat_id, state, "Не разобрала. Напиши номер модуля.")


def handle(tg: Telegram, chat_id: int, text: str, state: dict, progress: Progress) -> None:
    raw = text.strip()
    low = normalize(text)
    if low in TOPICS:
        show_topics(tg, chat_id, state)
        return
    if low in {"по-русски", "по русски"}:
        state["ru"] = True
        show_language(tg, chat_id, state, progress)
        return
    if low == "english":
        state["ru"] = False
        show_language(tg, chat_id, state, progress)
        return
    if low in {"/start", "/help", "старт"}:
        show_topics(tg, chat_id, state)
        return
    if low in MODES:
        if not state.get("module"):
            show_topics(tg, chat_id, state, "Сначала номер модуля.")
            return
        new_mode = MODES[low]
        if (
            state.get("mode") == new_mode
            and new_mode in {"quiz", "problems"}
            and state.get("item_id")
        ):
            reshow(tg, chat_id, state, progress, "")
            return
        enter_mode(state, new_mode)
        ask_next(tg, chat_id, state, progress)
        return
    if low in {"где я", "последний"}:
        show_mark(tg, chat_id, state, progress)
        return
    number = jump_number(low)
    if number is not None:
        if state.get("mode") in {"quiz", "problems"}:
            jump_question(tg, chat_id, state, progress, number)
        else:
            module = current_module(state)
            text = "Номер открывается в квизе или задачах. Сначала эта кнопка, потом «вопрос 12»."
            if module is None:
                show_topics(tg, chat_id, state, text)
            else:
                deliver(
                    tg,
                    chat_id,
                    brief(state, module, state.get("lesson") or PENDING, text),
                    keyboard=keys(state),
                    placeholder=PH_HOME,
                )
        return
    if low in {"предыдущий", "предыдущий вопрос", "следующий", "следующий вопрос"}:
        move_question(tg, chat_id, state, progress, -1 if low.startswith("предыдущий") else 1)
        return
    if is_next(low):
        on_next(tg, chat_id, state, progress)
        return
    if low == "следующий блок":
        on_block(tg, chat_id, state, progress)
        return
    if waiting(state):
        take_answer(tg, chat_id, raw, state, progress)
        return
    found = exact_module(raw)
    if found is not None:
        open_module(tg, chat_id, state, found)
        return
    if state.get("mode") == "road":
        explain_road(tg, chat_id, state, progress)
        return
    lost(tg, chat_id, state)


def main() -> None:
    token = load_token()
    tg = Telegram(token)
    me = tg.call("getMe")
    tg.call("deleteWebhook")
    print(f"listening as @{me.get('username')}", flush=True)
    progress = Progress(default_progress_path())
    session = Session(repo_root() / "progress" / "telegram_state.json")
    offset = session.offset
    while True:
        try:
            updates = tg.call("getUpdates", {"timeout": 25, "offset": offset})
        except Exception as exc:
            print(f"poll error: {_public_error(exc, token)}", flush=True)
            time.sleep(3)
            continue
        for update in updates:
            offset = int(update["update_id"]) + 1
            session.offset = offset
            message = update.get("message") or {}
            chat = message.get("chat") or {}
            text = message.get("text")
            if not chat or not text:
                continue
            chat_id = int(chat["id"])
            state = session.get(chat_id)
            print(f"in {chat_id} {text!r}", flush=True)
            try:
                handle(tg, chat_id, text, state, progress)
            except Exception as exc:
                print(f"handle error: {_public_error(exc, token)}", flush=True)
                module = None
                try:
                    module = current_module(state)
                except Exception:
                    module = None
                if module is not None:
                    tg.send(
                        chat_id,
                        frame(
                            state,
                            module,
                            state.get("lesson") or PENDING,
                            "Сбой на этом сообщении. «К темам» или /start — к списку модулей.",
                            "К темам — к списку",
                        ),
                        keyboard=keys(state),
                    )
                else:
                    tg.send(
                        chat_id,
                        "Сбой на этом сообщении. /start откроет список модулей.",
                        remove_keyboard=True,
                    )
            session.save()


if __name__ == "__main__":
    main()
