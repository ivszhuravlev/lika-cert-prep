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

from study.bank import find_module, load_modules, repo_root
from study.engine import (
    Progress,
    default_progress_path,
    grade_choice,
    grade_number,
    ordered,
    problems,
    render_question,
    render_reveal,
    road_prompt,
)

LABELS = {"exam": "Что спрашивают", "work": "Формула и пример", "trap": "Где срываются"}
MODES = {
    "теория": "theory",
    "задачи": "problems",
    "квиз": "quiz",
    "вместе": "mixed",
    "в дорогу": "road",
}


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

    def send(self, chat_id: int, text: str, *, keyboard: list[str] | None = None) -> None:
        for chunk in _chunks(text):
            payload: dict = {"chat_id": chat_id, "text": chunk}
            if keyboard:
                payload["reply_markup"] = json.dumps(
                    {"keyboard": [[label] for label in keyboard], "resize_keyboard": True}
                )
            self.call("sendMessage", payload)


def _chunks(text: str, size: int = 3500) -> list[str]:
    if len(text) <= size:
        return [text or "Пусто."]
    parts = []
    rest = text
    while rest:
        parts.append(rest[:size])
        rest = rest[size:]
    return parts


class Session:
    def __init__(self, path: Path):
        self.path = path
        self.chats: dict[str, dict] = {}
        if path.exists():
            self.chats = json.loads(path.read_text(encoding="utf-8"))

    def get(self, chat_id: int) -> dict:
        return self.chats.setdefault(
            str(chat_id),
            {"module": "", "mode": "", "cursor": 0, "item_id": ""},
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.chats, ensure_ascii=False, indent=2), encoding="utf-8")


def module_list() -> str:
    lines = ["Выбери модуль номером или названием.", ""]
    for module in load_modules():
        if module.chunks or module.items:
            lines.append(f"{module.code[1:]}  {module.title}")
    return "\n".join(lines)


KEYBOARD = ["Теория", "Задачи", "Квиз", "Вместе", "В дорогу"]


def ask_next(tg: Telegram, chat_id: int, state: dict, progress: Progress) -> None:
    module = find_module(load_modules(), state["module"])
    if module is None:
        tg.send(chat_id, module_list())
        return
    mode = state["mode"]
    if mode == "theory":
        if not module.chunks:
            tg.send(chat_id, "Теории по этому модулю ещё нет.", keyboard=KEYBOARD)
            return
        index = int(state.get("cursor", 0))
        if index >= len(module.chunks):
            tg.send(chat_id, "Урок кончился. Можно выбрать другой режим.", keyboard=KEYBOARD)
            state["mode"] = ""
            return
        chunk = module.chunks[index]
        state["cursor"] = index + 1
        tg.send(
            chat_id,
            f"{chunk.lesson}\n{LABELS.get(chunk.kind, chunk.kind)}\n\n{chunk.text}\n\nДальше — «дальше».",
            keyboard=KEYBOARD + ["дальше"],
        )
        return
    if mode == "road":
        prompt = road_prompt(module, progress)
        if not prompt:
            tg.send(chat_id, "В этом модуле нет слуховых вопросов.", keyboard=KEYBOARD)
            return
        tg.send(
            chat_id,
            "Скопируй это в новый голосовой чат. Задачи на лист туда не входят.\n\n" + prompt,
            keyboard=KEYBOARD,
        )
        state["mode"] = ""
        return
    if mode == "problems":
        pool = problems(ordered(module.items, progress))
        numeric = True
    elif mode == "mixed":
        phase = state.get("phase", "theory")
        if phase != "quiz":
            if not module.chunks:
                phase = "quiz"
            else:
                index = int(state.get("cursor", 0)) % max(len(module.chunks), 1)
                chunk = module.chunks[index]
                state["cursor"] = index + 1
                state["phase"] = "quiz"
                state["left"] = 3
                state["item_id"] = ""
                tg.send(chat_id, f"{chunk.lesson}\n\n{chunk.text}", keyboard=KEYBOARD)
                ask_next(tg, chat_id, state, progress)
                return
        pool = ordered(module.items, progress)
        if state.get("lesson"):
            pool = [item for item in pool if item.lesson == state["lesson"]] or pool
        numeric = False
    else:
        pool = ordered(module.items, progress)
        numeric = False
    if not pool:
        tg.send(chat_id, "В этом режиме вопросов нет.", keyboard=KEYBOARD)
        return
    index = int(state.get("cursor", 0)) % len(pool)
    item = pool[index]
    state["cursor"] = index + 1
    state["item_id"] = item.id
    state["lesson"] = item.lesson
    hint = "Напиши число." if numeric else "Напиши букву A, B, C или D."
    tg.send(chat_id, render_question(item, progress, numeric=numeric) + "\n\n" + hint, keyboard=KEYBOARD)
    if mode == "mixed":
        state["left"] = int(state.get("left", 1)) - 1
        if state["left"] <= 0:
            state["phase"] = "theory"


def handle(tg: Telegram, chat_id: int, text: str, state: dict, progress: Progress) -> None:
    raw = text.strip()
    low = raw.lower()
    if low in {"/start", "/help", "старт"}:
        state["module"] = ""
        state["mode"] = ""
        tg.send(chat_id, module_list())
        return
    if low in MODES:
        if not state.get("module"):
            tg.send(chat_id, "Сначала модуль.\n\n" + module_list())
            return
        state["mode"] = MODES[low]
        state["cursor"] = 0
        state["item_id"] = ""
        ask_next(tg, chat_id, state, progress)
        return
    if low == "дальше" and state.get("mode") == "theory":
        ask_next(tg, chat_id, state, progress)
        return
    module = find_module(load_modules(), raw) if not state.get("item_id") or low[:1] not in "abcd" else None
    if module is not None and low not in {"a", "b", "c", "d"}:
        state["module"] = module.code
        state["mode"] = ""
        state["item_id"] = ""
        tg.send(chat_id, f"{module.title}. Теория, задачи, квиз, вместе или в дорогу.", keyboard=KEYBOARD)
        return
    item_id = state.get("item_id") or ""
    if item_id and state.get("mode") in {"quiz", "problems", "mixed"}:
        module = find_module(load_modules(), state["module"])
        item = next((piece for piece in module.items if piece.id == item_id), None) if module else None
        if item is None:
            state["item_id"] = ""
            tg.send(chat_id, module_list())
            return
        numeric = state["mode"] == "problems"
        grade = grade_number(item, raw) if numeric else grade_choice(item, raw)
        if not numeric and raw[:1].upper() not in "ABCD":
            tg.send(chat_id, "Нужна буква A, B, C или D.")
            return
        progress.record(item.id, grade.ok)
        state["item_id"] = ""
        tg.send(chat_id, render_reveal(grade, numeric=numeric))
        ask_next(tg, chat_id, state, progress)
        return
    found = find_module(load_modules(), raw)
    if found:
        state["module"] = found.code
        state["mode"] = ""
        tg.send(chat_id, f"{found.title}. Теория, задачи, квиз, вместе или в дорогу.", keyboard=KEYBOARD)
        return
    tg.send(chat_id, "Не разобрала. /start покажет модули.")


def main() -> None:
    token = load_token()
    tg = Telegram(token)
    me = tg.call("getMe")
    tg.call("deleteWebhook")
    print(f"listening as @{me.get('username')}", flush=True)
    progress = Progress(default_progress_path())
    session = Session(repo_root() / "progress" / "telegram_state.json")
    offset = 0
    while True:
        try:
            updates = tg.call("getUpdates", {"timeout": 25, "offset": offset})
        except Exception as exc:
            print(f"poll error: {exc}", flush=True)
            time.sleep(3)
            continue
        for update in updates:
            offset = int(update["offset"]) + 1
            message = update.get("message") or {}
            chat = message.get("chat") or {}
            text = message.get("text")
            if not chat or not text:
                continue
            chat_id = int(chat["id"])
            state = session.get(chat_id)
            try:
                handle(tg, chat_id, text, state, progress)
            except Exception as exc:
                tg.send(chat_id, "Сбой на этом сообщении. /start")
                print(f"handle error: {exc}", flush=True)
            session.save()


if __name__ == "__main__":
    main()
