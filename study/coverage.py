"""Check the bank against the public DoseGrid lesson list and the MDCB objectives."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from study.bank import load_modules, repo_root

LESSON_LINE = re.compile(r"^- (.+)$")
MODULE_LINE = re.compile(r"^## (\d+)\. ")
OBJECTIVE_LINE = re.compile(r"\b([IVX]+)\.(\d+)\b")


def curriculum_lessons(root: Path | None = None) -> dict[str, list[str]]:
    root = root or repo_root()
    text = (root / "knowledge" / "plan" / "dosegrid-public-curriculum.md").read_text(encoding="utf-8")
    current = ""
    found: dict[str, list[str]] = {}
    for line in text.splitlines():
        module = MODULE_LINE.match(line)
        if module:
            current = f"m{int(module.group(1)):02d}"
            found[current] = []
            continue
        lesson = LESSON_LINE.match(line)
        if lesson and current:
            found[current].append(lesson.group(1).strip())
    return found


def objective_ids(root: Path | None = None) -> list[str]:
    root = root or repo_root()
    text = (root / "knowledge" / "plan" / "mdcb-objective-map.md").read_text(encoding="utf-8")
    seen: list[str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        match = re.match(r"\|\s*([IVX]+\.\d+)\s*\|", line)
        if match and match.group(1) not in seen:
            seen.append(match.group(1))
    return seen


def report(root: Path | None = None) -> dict:
    root = root or repo_root()
    modules = {module.code: module for module in load_modules(root)}
    lessons = curriculum_lessons(root)
    missing_files: list[str] = []
    missing_lessons: list[str] = []
    thin: list[str] = []
    by_objective: dict[str, int] = defaultdict(int)
    items = 0
    for code, titles in lessons.items():
        module = modules.get(code)
        if module is None or not module.items:
            missing_files.append(code)
            for title in titles:
                missing_lessons.append(f"{code} {title}")
            continue
        have = {title.strip(): 0 for title in titles}
        for item in module.items:
            items += 1
            key = item.lesson.strip()
            if key in have:
                have[key] += 1
            for match in OBJECTIVE_LINE.finditer(item.objective):
                by_objective[f"{match.group(1)}.{match.group(2)}"] += 1
        for title, count in have.items():
            if count == 0:
                missing_lessons.append(f"{code} {title}")
            elif count < 5:
                thin.append(f"{code} {title} ({count})")
    uncovered = [item for item in objective_ids(root) if by_objective[item] == 0]
    return {
        "items": items,
        "modules_with_questions": sum(1 for module in modules.values() if module.items),
        "missing_files": missing_files,
        "missing_lessons": missing_lessons,
        "thin": thin,
        "uncovered_objectives": uncovered,
        "objective_counts": dict(by_objective),
    }


def format_report(data: dict) -> str:
    lines = [
        f"questions {data['items']}",
        f"modules with questions {data['modules_with_questions']}/45",
        f"lessons with no questions {len(data['missing_lessons'])}",
        f"lessons under 5 questions {len(data['thin'])}",
        f"MDCB objectives with no item {len(data['uncovered_objectives'])}",
    ]
    if data["missing_files"]:
        lines.append("missing files: " + ", ".join(data["missing_files"]))
    if data["missing_lessons"]:
        lines.append("missing lessons:")
        lines.extend(f"  {row}" for row in data["missing_lessons"])
    if data["uncovered_objectives"]:
        lines.append("uncovered: " + ", ".join(data["uncovered_objectives"]))
    if data["thin"]:
        lines.append("thin:")
        lines.extend(f"  {row}" for row in data["thin"][:40])
    return "\n".join(lines)


def main() -> int:
    data = report()
    print(format_report(data))
    if data["missing_files"] or data["missing_lessons"] or data["uncovered_objectives"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
