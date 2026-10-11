import unittest
from pathlib import Path

from study.bank import find_module, load_modules, parse_number
from study.cli import check
from study.engine import Progress, grade_number, ordered, road_prompt


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


if __name__ == "__main__":
    unittest.main()
