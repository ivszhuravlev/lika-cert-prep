import re
import unittest
from pathlib import Path
from unittest.mock import patch

from study.bank import Item, find_module, load_modules, parse_number, parse_questions, parse_theory
from study.cli import check
from study.engine import Progress, grade_number, ordered, problems, road_blocks, road_prompt
from study.telegram_bot import handle, reveal_text, russian
from study.translate import Translator


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures"


class StudyTest(unittest.TestCase):
    def test_scientific_notation(self):
        self.assertAlmostEqual(parse_number("3.7 × 10^10 Bq"), 3.7e10)
        self.assertAlmostEqual(parse_number("2.58 × 10^(−4) C/kg"), 2.58e-4)

    def test_parse_number_keeps_the_whole_literal(self):
        self.assertAlmostEqual(parse_number("1,5"), 1.5)
        self.assertNotEqual(parse_number("1,5"), 1)
        self.assertAlmostEqual(parse_number("1 500"), 1500)
        self.assertNotEqual(parse_number("1 500"), 1)
        self.assertAlmostEqual(parse_number("1.5e3"), 1500)
        self.assertNotEqual(parse_number("1.5e3"), 1.5)
        self.assertAlmostEqual(parse_number(".5"), 0.5)
        self.assertNotEqual(parse_number(".5"), 5)
        self.assertIsNone(parse_number("Co-60"))
        self.assertIsNone(parse_number("A0 / λ"))
        self.assertIsNone(parse_number("2ab/(a+b)"))

    def test_every_lesson_paragraph_is_a_chunk(self):
        body = """**What the exam expects:** Compute the gap.

**Formula**

gap = L / 2

**Given.** Field length 20 cm.

**Substitute.**

gap = 1.40 cm

**Arithmetic.** 0.80 + 0.60 = 1.40

**Sources.** Khan and Gibbons.
"""
        chunks = parse_theory("m36", "# Module\n\n## Gap Calculation Tutorial\n\n" + body)
        paragraphs = [part.strip() for part in re.split(r"\n[ \t]*\n", body.strip()) if part.strip()]
        self.assertEqual("\n\n".join(chunk.text for chunk in chunks), "\n\n".join(paragraphs))
        self.assertGreater(len(chunks), 1)
        self.assertIn("Khan", chunks[-1].text)
        given = next(index for index, chunk in enumerate(chunks) if "Given." in chunk.text)
        self.assertLess(given, len(chunks) - 1)

    def test_gap_tutorial_keeps_every_paragraph(self):
        raw = (ROOT / "knowledge/theory/m36-special-calculations.md").read_text(encoding="utf-8")
        bucket: list[str] = []
        capture = False
        for line in raw.splitlines():
            if line.startswith("## "):
                if capture:
                    break
                capture = line[3:].strip() == "Gap Calculation Tutorial"
                continue
            if capture:
                bucket.append(line)
        body = "\n".join(bucket)
        paragraphs = [part.strip() for part in re.split(r"\n[ \t]*\n", body.strip()) if part.strip()]
        module = find_module(load_modules(ROOT), "m36")
        self.assertIsNotNone(module)
        chunks = [chunk for chunk in module.chunks if chunk.lesson == "Gap Calculation Tutorial"]
        self.assertEqual("\n\n".join(chunk.text for chunk in chunks), "\n\n".join(paragraphs))
        self.assertIn("Substitute.", "\n".join(chunk.text for chunk in chunks))
        self.assertIn("Arithmetic.", "\n".join(chunk.text for chunk in chunks))

    def test_text_key_is_not_a_numeric_problem(self):
        text = """## Penumbra
### Q1
Stem: Calculate the penumbra.
A. The Co-60 source has a finite diameter, while a linac target is nearly a point
B. 1.22 cm
C. 0.50 cm
D. 2.00 cm
Answer: A
Why: Source size.
### Q2
Stem: Calculate the penumbra.
A. The Co-60 source has a finite diameter, while a linac target is nearly a point
B. 1.22 cm
C. 0.50 cm
D. 2.00 cm
Answer: B
Why: Geometry.
### Q3
Stem: Calculate the activity.
A. A0 / λ
B. 0.0693
C. 10
D. 1
Answer: A
Why: Mean life.
### Q4
Stem: Calculate the ratio.
A. Greater than 1, because scatter from the phantom adds dose
B. 1.05
C. 0.95
D. 2
Answer: A
Why: Scatter.
"""
        items = parse_questions("m07", text)
        self.assertIsNone(items[0].number)
        self.assertNotEqual(items[0].number, -60)
        self.assertAlmostEqual(items[1].number, 1.22)
        self.assertIsNone(items[2].number)
        self.assertIsNone(items[3].number)
        self.assertEqual([item.id for item in problems(items)], [items[1].id])
        penumbra = find_module(load_modules(ROOT), "m07")
        live = next(item for item in penumbra.items if item.answer_text.startswith("The Co-60 source"))
        self.assertIsNone(live.number)
        self.assertNotIn(live.id, {item.id for item in problems(penumbra.items)})
        activity = find_module(load_modules(ROOT), "m03")
        mean_life = next(item for item in activity.items if item.answer_text.strip() == "A0 / λ")
        self.assertIsNone(mean_life.number)
        square = find_module(load_modules(ROOT), "m35")
        formula = next(item for item in square.items if item.answer_text.strip() == "2ab/(a+b)")
        self.assertIsNone(formula.number)

    def test_tie_with_a_wrong_choice_is_not_accepted(self):
        item = Item(
            id="tie",
            module="m35",
            lesson="Interpolation",
            stem="Calculate the factor.",
            choices={"A": "1.40", "B": "1.41", "C": "2.00", "D": "0.50"},
            answer="A",
            objective="IV.3",
            why="The interpolated value is 1.40.",
            number=1.40,
            channel="paper",
        )
        self.assertFalse(grade_number(item, "1.405").ok)
        self.assertFalse(grade_number(item, "1.41").ok)
        self.assertTrue(grade_number(item, "1.404").ok)
        self.assertTrue(grade_number(item, "1.40").ok)

    def test_numeric_reply_echoes_the_parsed_number_in_one_message(self):
        item = Item(
            id="echo",
            module="m12",
            lesson="Units",
            stem="Calculate the exposure.",
            choices={"A": "2.0 cm", "B": "1.0 cm", "C": "3.0 cm", "D": "4.0 cm"},
            answer="A",
            objective="I.1",
            why="The value is 2.",
            number=2.0,
            channel="paper",
        )
        grade = grade_number(item, "1,5")
        self.assertFalse(grade.ok)
        self.assertAlmostEqual(grade.parsed, 1.5)
        shown = reveal_text(grade, {}, numeric=True)
        self.assertIn("Прочитано: 1.5.", shown)
        self.assertNotRegex(shown, r"Прочитано: 1(?:\.0)?\.(?!\d)")
        self.assertLessEqual(shown.count("Разбор:"), 1)

        modules = load_modules(FIXTURE)
        progress = Progress(Path("/tmp/lika-echo-progress.json"))
        if progress.path.exists():
            progress.path.unlink()
        progress = Progress(progress.path)
        state: dict = {}
        sent: list[dict] = []

        class Box:
            def send(self, chat_id, text, keyboard=None, remove_keyboard=False, placeholder=None):
                sent.append({"text": text})

        with patch("study.telegram_bot.load_modules", return_value=modules):
            handle(Box(), 1, "3", state, progress)
            sent.clear()
            handle(Box(), 1, "Задачи", state, progress)
            sent.clear()
            handle(Box(), 1, "1,5", state, progress)
        self.assertEqual(len(sent), 1)
        self.assertLessEqual(len(sent[0]["text"]), 4096)
        self.assertIn("Прочитано: 1.5.", sent[0]["text"])
        self.assertIn("Не сошлось", sent[0]["text"])

    def test_fixture_session(self):
        self.assertEqual(check(), 0)

    def test_live_radioactivity_parses(self):
        module = find_module(load_modules(ROOT), "radioactivity")
        if module is None:
            self.skipTest("theory agents have not written radioactivity yet")
        self.assertGreaterEqual(len(module.items), 20)
        numeric = [item for item in module.items if item.number is not None and item.channel == "paper"]
        self.assertTrue(numeric)
        graded = grade_number(numeric[0], str(numeric[0].number))
        self.assertTrue(graded.ok)
        prompt = road_prompt(module, Progress(Path("/tmp/lika-test-empty-progress.json")))
        questions = prompt.split("Модуль:", 1)[1]
        self.assertNotIn("HVL", questions)
        self.assertNotRegex(questions.lower(), r"monitor unit")

    def test_mastered_items_leave_the_front(self):
        module = find_module(load_modules(FIXTURE), "radioactivity")
        progress = Progress(Path("/tmp/lika-rotation.json"))
        if progress.path.exists():
            progress.path.unlink()
        progress = Progress(progress.path)
        item = module.items[-1]
        progress.record(item.id, False)
        self.assertEqual(ordered(module.items, progress)[0].id, item.id)
        for _ in range(3):
            progress.record(item.id, True)
        self.assertNotEqual(ordered(module.items, progress, ear_only=True)[0].id, item.id)

    def test_module_quiz_is_not_one_card(self):
        module = find_module(load_modules(ROOT), "m43")
        self.assertIsNotNone(module)
        self.assertGreaterEqual(len(module.items), 20)
        progress = Progress(Path("/tmp/lika-m43-order.json"))
        if progress.path.exists():
            progress.path.unlink()
        progress = Progress(progress.path)
        queue = ordered(module.items, progress)
        self.assertEqual(queue[0].id, module.items[0].id)
        self.assertNotEqual(queue[0].id, queue[1].id)
        self.assertGreater(len({item.id for item in queue}), 1)

    def test_each_road_block_is_one_telegram_message(self):
        progress = Progress(Path("/tmp/lika-road-fit.json"))
        if progress.path.exists():
            progress.path.unlink()
        progress = Progress(progress.path)
        for module in load_modules(ROOT):
            if not module.items:
                continue
            blocks = road_blocks(module, progress)
            for block in blocks:
                self.assertLessEqual(len(block), 4000)
                self.assertLessEqual(len(block), 4096)
                self.assertTrue(block.startswith("Скопируй это сообщение целиком"))


class Echo:
    def complete(self, messages, max_tokens=500):
        return messages[-1]["content"]


class Russian:
    def complete(self, messages, max_tokens=500):
        return "Радиоактивность. half-life 73.8"


class TranslationTest(unittest.TestCase):
    def test_english_echo_is_labeled_a_failure(self):
        import study.telegram_bot as bot

        path = Path("/tmp/lika-ru-echo.json")
        if path.exists():
            path.unlink()
        bot._translator = Translator(Echo(), path)
        text = "Activity is not dose."
        self.assertEqual(bot._translator(text), text)
        self.assertFalse(path.exists())
        shown = russian({"ru": True}, text)
        self.assertTrue(shown.startswith("Перевод не получился"))
        self.assertIn(text, shown)

    def test_cached_english_is_not_served_as_russian(self):
        import study.telegram_bot as bot

        path = Path("/tmp/lika-ru-bad-cache.json")
        path.write_text('{"Activity is not dose.": "Activity is not dose."}', encoding="utf-8")
        bot._translator = Translator(Echo(), path)
        shown = russian({"ru": True}, "Activity is not dose.")
        self.assertTrue(shown.startswith("Перевод не получился"))

    def test_real_russian_keeps_the_number(self):
        path = Path("/tmp/lika-ru-ok.json")
        if path.exists():
            path.unlink()
        translator = Translator(Russian(), path)
        out = translator("half-life is 73.8 days")
        self.assertIn("73.8", out)
        self.assertIn("Радиоактивность", out)
        self.assertIn("half-life", out)

    def test_changed_number_or_term_stays_english(self):
        import study.telegram_bot as bot

        path = Path("/tmp/lika-ru-changed.json")
        if path.exists():
            path.unlink()

        class Change:
            def complete(self, messages, max_tokens=500):
                return "Радиоактивность. half-life 80"

        class DropTerm:
            def complete(self, messages, max_tokens=500):
                return "Период полураспада равен 73.8 суткам"

        source = "half-life is 73.8 days"
        bot._translator = Translator(Change(), path)
        try:
            shown = russian({"ru": True}, source)
        finally:
            bot._translator = None
        self.assertTrue(shown.startswith("Перевод не получился"))
        self.assertIn("73.8", shown)
        self.assertNotIn("80", shown)
        self.assertEqual(Translator(DropTerm(), path)(source), source)


if __name__ == "__main__":
    unittest.main()
