import unittest
from pathlib import Path

from study.bank import find_module, load_modules, parse_number
from study.cli import check
from study.engine import Progress, grade_number, ordered, road_blocks, road_prompt
from study.telegram_bot import russian
from study.translate import Translator


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures"


class StudyTest(unittest.TestCase):
    def test_scientific_notation(self):
        self.assertAlmostEqual(parse_number("3.7 × 10^10 Bq"), 3.7e10)

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


if __name__ == "__main__":
    unittest.main()
