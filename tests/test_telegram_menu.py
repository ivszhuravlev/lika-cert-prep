import re
import unittest
from pathlib import Path
from unittest.mock import patch

from study.bank import load_modules
from study.engine import Progress, ordered, problems, road_blocks
from study.telegram_bot import frame, handle, visible_parts


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures"
CYR = {"A": "А", "B": "В", "C": "С", "D": "Д"}


class Box:
    def __init__(self):
        self.sent = []

    def send(self, chat_id, text, keyboard=None, remove_keyboard=False, placeholder=None):
        self.sent.append(
            {
                "text": text,
                "keyboard": keyboard,
                "remove": remove_keyboard,
                "placeholder": placeholder,
            }
        )


def header_of(text: str) -> tuple[str, str, str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[2] != "":
        raise AssertionError(text)
    number, title = lines[0].split(" · ", 1)
    mode, lesson = lines[1].split(" · ", 1)
    if not number.startswith("Модуль ") or not mode.startswith("Сейчас: "):
        raise AssertionError(text)
    return number.removeprefix("Модуль "), title, mode.removeprefix("Сейчас: "), lesson


class MenuTest(unittest.TestCase):
    def setUp(self):
        import study.telegram_bot as bot

        self.bot = bot
        self.modules = load_modules(FIXTURE)
        self.patch = patch("study.telegram_bot.load_modules", return_value=self.modules)
        self.patch.start()
        path = Path("/tmp/lika-menu-progress.json")
        if path.exists():
            path.unlink()
        self.progress = Progress(path)
        self.state: dict = {}
        self.box = Box()
        self.previous = bot._translator
        self.translated: list[str] = []

        def fake(text: str) -> str:
            self.translated.append(text)
            return ("абвгде " * 200) + text

        bot._translator = fake

    def tearDown(self):
        self.bot._translator = self.previous
        self.patch.stop()

    def say(self, text: str) -> list[dict]:
        handle(self.box, 1, text, self.state, self.progress)
        sent = self.box.sent
        self.box.sent = []
        return sent

    def module(self, number: str):
        from study.bank import find_module

        return find_module(self.modules, number)

    def test_start_and_module_number(self):
        sent = self.say("/start@LikaBot")
        self.assertTrue(sent[-1]["remove"])
        self.assertIsNone(sent[-1]["keyboard"])
        self.assertTrue(sent[-1]["text"].startswith("Список модулей."))
        self.assertIn("3  Radioactivity", sent[-1]["text"])
        self.assertEqual(self.state["module"], "")

        sent = self.say("a")
        self.assertEqual(self.state["module"], "")
        sent = self.say("radio")
        self.assertEqual(self.state["module"], "")

        sent = self.say("03")
        number, title, mode, lesson = header_of(sent[-1]["text"])
        self.assertEqual((number, title, mode, lesson), ("3", "Radioactivity", "меню", "урок не выбран"))
        self.assertIn(["К темам"], sent[-1]["keyboard"])
        self.assertEqual(sent[-1]["placeholder"], "Выбери режим кнопкой")
        self.assertIn("К темам", sent[-1]["text"])
        self.assertEqual(self.state["module"], "m03")

        sent = self.say("radioactivity")
        self.assertEqual(header_of(sent[-1]["text"])[0], "3")

    def test_theory_next_and_end(self):
        self.say("3")
        sent = self.say("Теория")
        self.assertEqual(len(sent), 2)
        body, note = sent
        number, _, mode, lesson = header_of(body["text"])
        self.assertEqual((number, mode, lesson), ("3", "теория", "Decay Constant"))
        self.assertIn("0.693", body["text"])
        self.assertIn("Ir-192", body["text"])
        self.assertIn("## Common Radioisotopes", body["text"])
        self.assertLessEqual(len(body["text"]), 4096)
        self.assertEqual(visible_parts(body["text"]), [body["text"]])
        self.assertIn("Блок 1 из 1", note["text"])
        self.assertIn("Скопируй сообщение выше целиком.", note["text"])
        self.assertLess(len(note["text"]), 500)
        self.assertIn(["Дальше"], note["keyboard"])
        self.assertIn(["К темам"], note["keyboard"])
        sent = self.say("Дальше")
        self.assertTrue(any("кончилась" in piece["text"] for piece in sent))
        self.assertNotIn(["Дальше"], sent[-1]["keyboard"])
        self.assertEqual(self.state["mode"], "")
        self.assertEqual(self.state["module"], "m03")

    def test_theory_splits_only_at_the_telegram_limit(self):
        from study.bank import Chunk, Module
        from study.telegram_bot import TELEGRAM_LIMIT, theory_body, theory_packs

        piece = "Compute the gap from the given field length. " * 30
        self.assertGreater(len(piece), 500)
        self.assertLess(len(piece), 2000)
        chunks = [Chunk("Gap", "exam", f"P{i:02d} {piece}") for i in range(8)]
        later = [Chunk("Decay", "exam", f"Q{i:02d} {piece}") for i in range(4)]
        module = Module("m03", "radioactivity", "Radioactivity", chunks=[*chunks, *later])
        state = {"mode": "theory"}
        packs = theory_packs(state, module)
        self.assertGreater(len(packs), 1)
        self.assertLess(len(packs), len(module.chunks))
        self.assertEqual(
            [chunk.text for pack in packs for chunk in pack],
            [chunk.text for chunk in module.chunks],
        )
        for index, pack in enumerate(packs):
            head = self.bot.header(state, module, pack[0].lesson)
            body = theory_body(state, pack)
            self.assertLessEqual(len(head) + 2 + len(body), TELEGRAM_LIMIT)
            if index + 1 < len(packs):
                nxt = packs[index + 1][0]
                longer = theory_body(state, [*pack, nxt])
                self.assertGreater(len(head) + 2 + len(longer), TELEGRAM_LIMIT)

        with patch("study.telegram_bot.load_modules", return_value=[module]):
            self.state = {}
            self.say("3")
            sent = self.say("Теория")
            messages = [sent[0]["text"]]
            for _ in range(20):
                sent = self.say("Дальше")
                if any("кончилась" in part["text"] for part in sent):
                    break
                messages.append(sent[0]["text"])
            else:
                self.fail("theory did not end")
        self.assertEqual(len(messages), len(packs))
        joined = "\n".join(messages)
        for text in messages:
            self.assertLessEqual(len(text), TELEGRAM_LIMIT)
            self.assertEqual(visible_parts(text), [text])
        self.assertIn("## Gap", messages[0])
        self.assertLess(joined.find("## Gap"), joined.find("## Decay"))
        for marker in [f"P{i:02d}" for i in range(8)] + [f"Q{i:02d}" for i in range(4)]:
            self.assertIn(marker, joined)

    def test_problem_number_is_not_a_module_change(self):
        module = self.module("3")
        item = problems(ordered(module.items, self.progress))[0]
        self.say("3")
        sent = self.say("Задачи")
        _, _, mode, lesson = header_of(sent[-1]["text"])
        self.assertEqual(mode, "задача")
        self.assertEqual(lesson, item.lesson)
        self.assertIn(item.stem, sent[-1]["text"])
        self.assertEqual(sent[-1]["placeholder"], "Задача: напиши число")
        self.assertFalse(any(line.startswith("A. ") for line in sent[-1]["text"].splitlines()))
        self.assertIn(["К темам"], sent[-1]["keyboard"])

        sent = self.say("36")
        self.assertEqual(self.state["module"], "m03")
        self.assertEqual(self.state["mode"], "problems")
        self.assertEqual(self.progress.get(item.id)["last"], "wrong")
        self.assertTrue(all(header_of(piece["text"])[0] == "3" for piece in sent))
        self.assertIn("Не сошлось", sent[0]["text"])
        self.assertNotIn("Special Calculations", "\n".join(piece["text"] for piece in sent))

        self.progress = Progress(Path("/tmp/lika-menu-progress-ok.json"))
        if self.progress.path.exists():
            self.progress.path.unlink()
        self.progress = Progress(self.progress.path)
        self.state = {}
        self.say("3")
        self.say("Задачи")
        sent = self.say(str(item.number))
        self.assertEqual(self.progress.get(item.id)["last"], "ok")
        self.assertIn("Верно.", sent[0]["text"])
        self.assertIn(str(item.number), sent[0]["text"])

    def test_quiz_letter_cyrillic_and_topics_mid_question(self):
        module = self.module("3")
        item = ordered(module.items, self.progress)[0]
        self.say("3")
        sent = self.say("Квиз")
        _, _, mode, lesson = header_of(sent[-1]["text"])
        self.assertEqual((mode, lesson), ("квиз", item.lesson))
        self.assertIn(item.stem, sent[-1]["text"])
        self.assertIn(["A", "B", "C", "D"], sent[-1]["keyboard"])
        self.assertIn(["К темам"], sent[-1]["keyboard"])
        self.assertEqual(sent[-1]["placeholder"], "Квиз: буква A B C D")
        item_id = self.state["item_id"]
        cursor = self.state["cursor"]

        sent = self.say("3")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["item_id"], item_id)
        self.assertEqual(self.state["module"], "m03")
        self.assertIn("не записано", sent[-1]["text"])
        self.assertIn(["К темам"], sent[-1]["keyboard"])

        sent = self.say("Дальше")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["cursor"], cursor)
        self.assertIn("не записано", sent[-1]["text"])

        sent = self.say("К темам")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["module"], "")
        self.assertEqual(self.state["item_id"], "")
        self.assertTrue(sent[-1]["remove"])
        self.assertTrue(sent[-1]["text"].startswith("Список модулей."))

        self.say("3")
        self.say("Квиз")
        sent = self.say(CYR[item.answer])
        self.assertEqual(self.progress.get(item.id)["last"], "ok")
        self.assertIn("Верно.", sent[0]["text"])
        self.assertTrue(all(header_of(piece["text"])[2] == "квиз" for piece in sent))
        self.assertEqual(len(sent), 1)

        sent = self.say("Следующий")
        self.assertNotEqual(self.state["item_id"], item.id)
        self.assertIn("Вопрос 2 из", sent[-1]["text"])
        self.assertIn(["Предыдущий", "Следующий"], sent[-1]["keyboard"])
        sent = self.say("Предыдущий")
        self.assertEqual(self.state["item_id"], item.id)
        self.assertIn("Вопрос 1 из", sent[-1]["text"])
        sent = self.say("где я")
        self.assertIn("последний решённый — вопрос 1", sent[-1]["text"])
        self.assertLess(len(sent[-1]["keyboard"]), 8)
        sent = self.say("вопрос 2")
        self.assertIn("Вопрос 2 из", sent[-1]["text"])
        self.assertNotEqual(self.state["item_id"], item.id)

    def test_mode_switch_and_start_do_not_grade(self):
        self.say("3")
        self.say("Квиз")
        sent = self.say("Теория")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["mode"], "theory")
        self.assertEqual(header_of(sent[-1]["text"])[2], "теория")
        self.assertIn(["К темам"], sent[-1]["keyboard"])

        self.state = {}
        self.progress = Progress(Path("/tmp/lika-menu-progress-start.json"))
        if self.progress.path.exists():
            self.progress.path.unlink()
        self.progress = Progress(self.progress.path)
        self.say("3")
        self.say("Квиз")
        sent = self.say("/start")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["module"], "")
        self.assertEqual(self.state["item_id"], "")
        self.assertTrue(sent[-1]["remove"])

    def test_mixed_stays_on_the_paragraph_lesson(self):
        module = self.module("3")
        self.say("3")
        sent = self.say("Вместе")
        self.assertEqual(len(sent), 2)
        _, _, mode, lesson = header_of(sent[0]["text"])
        self.assertEqual(mode, "вместе")
        self.assertEqual(lesson, module.chunks[0].lesson)
        self.assertIn("Абзац 1 из", sent[1]["text"])
        self.assertLess(len(sent[1]["text"]), 500)
        self.assertIn(["Дальше"], sent[1]["keyboard"])
        stems = [item.stem for item in module.items if item.lesson == lesson]
        self.assertFalse(any(stem in sent[1]["text"] for stem in stems))
        sent = self.say("Дальше")
        self.assertTrue(any(stem in sent[0]["text"] for stem in stems))
        self.assertIn(["A", "B", "C", "D"], sent[0]["keyboard"])
        self.assertIn(["К темам"], sent[0]["keyboard"])

    def test_road_header_and_letter_is_not_an_answer(self):
        module = self.module("3")
        blocks = road_blocks(module, self.progress)
        self.assertTrue(blocks)
        self.say("3")
        sent = self.say("В дорогу")
        paste, note = sent[0], sent[1]
        number, _, mode, lesson = header_of(paste["text"])
        self.assertEqual((number, mode), ("3", "в дорогу"))
        self.assertLess(paste["text"].find("Сейчас:"), paste["text"].find("Скопируй"))
        self.assertIn(f"### 1. {lesson}", paste["text"])
        self.assertEqual(header_of(note["text"])[2], "в дорогу")
        self.assertIn("Блок 1 из", note["text"])
        self.assertLess(len(note["text"]), 500)
        self.assertIn(["К темам"], paste["keyboard"])
        self.assertIn(["К темам"], note["keyboard"])
        self.assertEqual((["Следующий блок"] in note["keyboard"]), len(blocks) > 1)
        self.assertEqual(visible_parts(paste["text"]), [paste["text"]])

        before = dict(self.progress.items)
        sent = self.say("A")
        self.assertEqual(self.progress.items, before)
        self.assertEqual(self.state["mode"], "road")
        self.assertEqual(self.state["module"], "m03")
        self.assertIn("не ответ", sent[-1]["text"])

        sent = self.say("Следующий блок")
        self.assertEqual(self.progress.items, before)
        self.assertTrue(sent[-1]["text"].startswith("Модуль 3 · "))

    def test_russian_toggle_does_not_grade(self):
        module = self.module("3")
        item = ordered(module.items, self.progress)[0]
        self.say("3")
        self.say("Квиз")
        self.translated.clear()
        item_id = self.state["item_id"]
        cursor = self.state["cursor"]
        sent = self.say("По-русски")
        self.assertEqual(self.progress.items, {})
        self.assertEqual(self.state["item_id"], item_id)
        self.assertEqual(self.state["cursor"], cursor)
        self.assertIn(item.stem, sent[-1]["text"])
        self.assertIn("абвгде", sent[-1]["text"])
        blobs = [item.stem, *item.choices.values()]
        for blob in blobs:
            for number in re.findall(r"\d+(?:\.\d+)?", blob):
                self.assertIn(number, sent[-1]["text"])
        self.assertTrue(self.translated)
        self.assertTrue(any("English" in row for row in sent[-1]["keyboard"]))
        self.assertIn(["К темам"], sent[-1]["keyboard"])
        _, _, mode, lesson = header_of(sent[-1]["text"])
        self.assertEqual((mode, lesson), ("квиз", item.lesson))

        sent = self.say("English")
        self.assertEqual(self.progress.items, {})
        self.assertNotIn("абвгде", sent[-1]["text"])
        self.assertTrue(any("По-русски" in row for row in sent[-1]["keyboard"]))

        self.say("По-русски")
        sent = self.say(item.answer)
        self.assertEqual(self.progress.get(item.id)["last"], "ok")
        self.assertIn("Верно.", sent[0]["text"])

    def test_empty_theory_and_road_keep_the_header(self):
        module = self.module("36")
        self.say("36")
        sent = self.say("Теория")
        number, title, mode, lesson = header_of(sent[-1]["text"])
        self.assertEqual((number, title, mode, lesson), ("36", module.title, "теория", "урок не выбран"))
        self.assertIn("нет", sent[-1]["text"])
        self.assertIn(["К темам"], sent[-1]["keyboard"])

        sent = self.say("В дорогу")
        number, _, mode, _ = header_of(sent[-1]["text"])
        self.assertEqual((number, mode), ("36", "в дорогу"))
        self.assertIn("Слуховых", sent[-1]["text"])
        self.assertIn(["К темам"], sent[-1]["keyboard"])

    def test_long_message_repeats_the_header(self):
        module = self.module("3")
        state = {"mode": "quiz"}
        text = frame(state, module, "Decay Constant", "слово " * 2000, "Буква или К темам")
        parts = visible_parts(text, limit=700)
        self.assertGreater(len(parts), 1)
        for part in parts:
            self.assertTrue(part.startswith("Модуль 3 · Radioactivity\nСейчас: квиз · Decay Constant"))


if __name__ == "__main__":
    unittest.main()
