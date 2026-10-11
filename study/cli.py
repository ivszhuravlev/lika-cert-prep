"""Local stand-in for the Telegram bot. The bank grades. A model is optional and cannot mark answers."""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.error import URLError

from study.bank import find_module, load_modules, repo_root
from study.engine import (
    Progress,
    default_progress_path,
    explain_messages,
    grade_choice,
    grade_number,
    ordered,
    problems,
    render_question,
    render_reveal,
    road_prompt,
)

OLLAMA_MODEL = "qwen2.5:3b"


def _ask(text: str) -> str:
    try:
        return input(text)
    except EOFError:
        return "стоп"


def _stopped(raw: str) -> bool:
    return raw.strip().lower() in {"стоп", "s", "stop", "хватит"}


def list_modules() -> int:
    modules = [module for module in load_modules() if module.chunks or module.items]
    if not modules:
        print("В knowledge/ ещё нет модулей.")
        return 1
    for module in modules:
        ear = sum(1 for item in module.items if item.channel == "ear")
        paper = sum(1 for item in module.items if item.channel == "paper")
        print(
            f"{module.code}  {module.title}  "
            f"уроки {len(module.lessons)}  слух {ear}  лист {paper}"
        )
    return 0


def _pick_module(name: str | None):
    modules = load_modules()
    if name:
        return find_module(modules, name)
    list_modules()
    picked = _ask("\nМодуль (номер или имя): ").strip()
    if not picked or picked.lower() in {"стоп", "q"}:
        return None
    return find_module(modules, picked)


def run_theory(module) -> None:
    if not module.chunks:
        print("Теории по этому модулю ещё нет.")
        return
    labels = {"exam": "Что спрашивают", "work": "Формула и пример", "trap": "Где срываются"}
    for chunk in module.chunks:
        print(f"\n— {chunk.lesson} · {labels.get(chunk.kind, chunk.kind)}\n")
        print(chunk.text)
        nxt = _ask("\nДальше — Enter, стоп — s: ").strip().lower()
        if _stopped(nxt):
            return


def run_problems(module, progress: Progress) -> None:
    pool = problems(ordered(module.items, progress))
    if not pool:
        print("Числовых задач с готовым ответом в этом модуле пока нет. Возьми квиз.")
        return
    for item in pool:
        print()
        print(render_question(item, progress, numeric=True))
        raw = _ask("Число: ").strip()
        if _stopped(raw):
            return
        grade = grade_number(item, raw)
        progress.record(item.id, grade.ok)
        print(render_reveal(grade, numeric=True))


def run_quiz(module, progress: Progress, *, lesson: str | None = None, limit: int | None = None) -> None:
    pool = ordered(module.items, progress)
    if lesson:
        pool = [item for item in pool if item.lesson == lesson]
    if limit:
        pool = pool[:limit]
    if not pool:
        print("Квиза по этому модулю ещё нет.")
        return
    for item in pool:
        print()
        print(render_question(item, progress, numeric=False))
        raw = _ask("Буква: ").strip()
        if _stopped(raw):
            return
        grade = grade_choice(item, raw)
        progress.record(item.id, grade.ok)
        print(render_reveal(grade, numeric=False))


def run_mixed(module, progress: Progress) -> None:
    if not module.chunks:
        run_quiz(module, progress)
        return
    by_lesson: dict[str, list] = {}
    for chunk in module.chunks:
        by_lesson.setdefault(chunk.lesson, []).append(chunk)
    for lesson, chunks in by_lesson.items():
        print(f"\n— {lesson}\n")
        print(chunks[0].text)
        run_quiz(module, progress, lesson=lesson, limit=3)
        nxt = _ask("\nДальше — Enter, стоп — s: ").strip().lower()
        if _stopped(nxt):
            return


def run_road(module, progress: Progress) -> Path | None:
    prompt = road_prompt(module, progress)
    if not prompt:
        print("В этом модуле нет слуховых вопросов.")
        return None
    path = repo_root() / "progress" / "road-prompt.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(prompt, encoding="utf-8")
    print(prompt)
    print(f"\nФайл: {path}")
    return path


def ollama_complete(messages: list[dict], *, max_tokens: int = 400) -> str:
    """Local chat completion. Same shape as the study bot's Ollama client."""
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": item.get("role", "user"),
                "content": item.get("content") or item.get("text") or "",
            }
            for item in messages
        ],
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": max_tokens},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(
            "Локальная модель не ответила. Проверь, что Ollama запущена на 127.0.0.1:11434."
        ) from exc
    text = str(body.get("message", {}).get("content", "")).strip()
    if not text:
        raise RuntimeError("Локальная модель вернула пустой ответ")
    return text


def ollama_explain(prompt: str, student: str) -> str:
    """Ask the local model to explain a graded miss. The grade itself is not its job."""
    return ollama_complete(explain_messages(prompt, student))


def voice_check() -> int:
    modules = load_modules()
    module = find_module(modules, "radioactivity")
    if module is None or not module.items:
        print("Нет модуля radioactivity, голосовую проверку пропустить нельзя.")
        return 1
    prompt = road_prompt(module, Progress(Path("/tmp/lika-voice-progress.json")))
    questions = prompt.split("Модуль:", 1)[1]
    if re.search(r"\b(MU|HVL|DVH)\b", questions):
        print("В дорожный промпт попала задача с листа.")
        return 1
    if "73.8" not in prompt and "Ir-192" not in prompt:
        print("В пачке нет узнавания Ir-192.")
        return 1
    try:
        reply = ollama_explain(prompt, "кобальт шестьдесят")
    except Exception as exc:  # network to localhost
        print(f"Ollama не ответила: {exc}")
        return 1
    if "Gy" in reply or "грей" in reply.lower():
        print("Модель добавила дозу, которой в пачке нет.")
        print(reply)
        return 1
    print(reply.strip()[:800])
    print("Голосовой разбор прошёл: оценка от банка, модель только объясняет.")
    return 0


def check() -> int:
    """Scripted session: grade, misses, road filter. No Telegram."""
    from pathlib import Path as P

    fixture = repo_root() / "tests" / "fixtures"
    modules = load_modules(fixture)
    decay = find_module(modules, "radioactivity")
    special = find_module(modules, "special")
    assert decay is not None and special is not None
    lam = next(item for item in decay.items if item.lesson == "Decay Constant")
    assert grade_number(lam, "0.0693").ok
    assert not grade_number(lam, "6.93").ok
    half = next(item for item in decay.items if "Ir-192" in item.stem)
    assert half.channel == "ear"
    assert grade_choice(half, "a").ok
    hvl = next(item for item in special.items if "HVL" in item.stem)
    assert hvl.channel == "paper"
    progress = Progress(P("/tmp/lika-study-check.json"))
    if progress.path.exists():
        progress.path.unlink()
        progress = Progress(progress.path)
    progress.record(half.id, False)
    first = ordered(decay.items, progress, ear_only=True)[0]
    assert first.id == half.id
    for _ in range(3):
        progress.record(half.id, True)
    assert ordered(decay.items, progress, ear_only=True)[0].id != half.id
    prompt = road_prompt(decay, Progress(P("/tmp/lika-empty.json")))
    questions = prompt.split("Модуль:", 1)[1]
    assert "HVL" not in questions and "Ir-192" in questions
    assert road_prompt(special, Progress(P("/tmp/lika-special-empty.json"))) == ""
    live = find_module(load_modules(), "radioactivity")
    if live:
        live_prompt = road_prompt(live, Progress(P("/tmp/lika-live-empty.json")))
        live_questions = live_prompt.split("Модуль:", 1)[1]
        assert "DVH" not in live_questions
        assert "monitor unit" not in live_questions.lower()
    print("Локальная сессия сошлась: число, буква, промах в начало, HVL не в дороге.")
    return 0


def interactive() -> int:
    print("Домашний прогон. Telegram не подключён. Ответ сверяет банк.")
    module = _pick_module(None)
    if module is None:
        return 0
    progress = Progress(default_progress_path())
    print("теория | задачи | квиз | вместе | дорога")
    mode = _ask("Режим: ").strip().lower()
    if mode in {"теория", "theory", "т"}:
        run_theory(module)
    elif mode in {"задачи", "problems", "з"}:
        run_problems(module, progress)
    elif mode in {"квиз", "quiz", "к"}:
        run_quiz(module, progress)
    elif mode in {"вместе", "mixed", "вм"}:
        run_mixed(module, progress)
    elif mode in {"дорога", "road", "д"}:
        run_road(module, progress)
    else:
        print("Не тот режим.")
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        return interactive()
    command = args[0]
    if command == "list":
        return list_modules()
    if command == "check":
        return check()
    if command == "voice-check":
        return voice_check()
    if command in {"theory", "problems", "quiz", "mixed", "road"} and len(args) > 1:
        module = _pick_module(args[1])
        if module is None:
            print("Модуль не найден.")
            return 1
        progress = Progress(default_progress_path())
        if command == "theory":
            run_theory(module)
        elif command == "problems":
            run_problems(module, progress)
        elif command == "quiz":
            run_quiz(module, progress)
        elif command == "mixed":
            run_mixed(module, progress)
        else:
            run_road(module, progress)
        return 0
    print("Команды: list | check | voice-check | theory <модуль> | problems | quiz | mixed | road")
    return 1
