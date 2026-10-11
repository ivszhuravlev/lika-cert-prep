"""Read theory notes and original questions from knowledge/."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

PAPER_RE = re.compile(
    r"monitor unit|\bMUs?\b|half-value|half value layer|\bHVL\b|\bDVH\b|"
    r"skin gap|field gap|gap calculation|geometric penumbra|wedge factor|"
    r"mayneord|equivalent square|percent depth|\bPDD\b|\bTMR\b|"
    r"timer error|timer setting|interpolation",
    re.IGNORECASE,
)
COMPUTE_RE = re.compile(
    r"\b(calculate|compute|how many|what is λ|what is lambda|find the)\b",
    re.IGNORECASE,
)
RECALL_RE = re.compile(
    r"half-life is|half life is|best described|is called|units of|equals\b|"
    r"which of the following|mode of decay|decays by",
    re.IGNORECASE,
)
SECTION_RE = re.compile(r"^\*\*(.+?)\*\*\s*$", re.MULTILINE)
CHOICE_RE = re.compile(r"^([A-D])\.\s*(.*)$")
SCI_RE = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*[x×*]\s*10\^?\s*(-?\d+)",
    re.IGNORECASE,
)
NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")


@dataclass
class Chunk:
    lesson: str
    kind: str
    text: str


@dataclass
class Item:
    id: str
    module: str
    lesson: str
    stem: str
    choices: dict[str, str]
    answer: str
    objective: str
    why: str
    number: float | None
    channel: str  # ear | paper

    @property
    def answer_text(self) -> str:
        return self.choices.get(self.answer, "")


@dataclass
class Module:
    code: str
    slug: str
    title: str
    chunks: list[Chunk] = field(default_factory=list)
    items: list[Item] = field(default_factory=list)

    @property
    def lessons(self) -> list[str]:
        seen: list[str] = []
        for chunk in self.chunks:
            if chunk.lesson not in seen:
                seen.append(chunk.lesson)
        for item in self.items:
            if item.lesson not in seen:
                seen.append(item.lesson)
        return seen


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_number(text: str) -> float | None:
    cleaned = (
        text.replace("−", "-")
        .replace("–", "-")
        .replace("×", "x")
        .replace("·", "x")
    )
    sci = SCI_RE.search(cleaned)
    if sci:
        return float(sci.group(1)) * (10 ** int(sci.group(2)))
    match = NUM_RE.search(cleaned)
    if not match:
        return None
    return float(match.group(0))


def channel_for(lesson: str, stem: str) -> str:
    blob = f"{lesson}\n{stem}"
    if PAPER_RE.search(blob):
        return "paper"
    if COMPUTE_RE.search(blob):
        return "paper"
    if re.search(r"\bwhat is\b", blob, re.IGNORECASE) and re.search(r"\d", stem):
        if not RECALL_RE.search(stem):
            return "paper"
    return "ear"


def _lesson_chunks(lesson: str, body: str) -> list[Chunk]:
    matches = list(SECTION_RE.finditer(body))
    if not matches:
        text = body.strip()
        return [Chunk(lesson, "exam", text)] if text else []
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append((match.group(1).strip().lower(), body[start:end].strip()))
    groups = {
        "exam": ("what the exam expects", "core facts", "skills this quiz checks"),
        "work": ("formulas", "formula", "worked example"),
        "trap": ("traps", "usual wrong turn"),
    }
    built: list[Chunk] = []
    for kind, names in groups.items():
        parts = [text for name, text in sections if name in names and text]
        if parts:
            built.append(Chunk(lesson, kind, "\n\n".join(parts)))
    if built:
        return built
    text = body.strip()
    return [Chunk(lesson, "exam", text)] if text else []


def parse_theory(code: str, text: str) -> list[Chunk]:
    lines = text.splitlines()
    chunks: list[Chunk] = []
    lesson = ""
    bucket: list[str] = []

    def flush() -> None:
        if lesson:
            chunks.extend(_lesson_chunks(lesson, "\n".join(bucket)))

    for line in lines:
        if line.startswith("## "):
            flush()
            lesson = line[3:].strip()
            bucket = []
        elif lesson:
            bucket.append(line)
    flush()
    return chunks


def parse_questions(code: str, text: str) -> list[Item]:
    lesson = ""
    items: list[Item] = []
    block: list[str] = []

    def flush() -> None:
        if block:
            item = _parse_item(code, lesson, block)
            if item:
                items.append(item)

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            lesson = line[3:].strip()
            block = []
        elif line.startswith("### Q"):
            flush()
            block = [line]
        elif block:
            block.append(line)
    flush()
    return items


def _parse_item(code: str, lesson: str, block: list[str]) -> Item | None:
    header = block[0]
    qid = header.replace("### ", "").strip()
    stem_lines: list[str] = []
    choices: dict[str, str] = {}
    answer = ""
    objective = ""
    why_lines: list[str] = []
    mode = "stem"
    for raw in block[1:]:
        line = raw.rstrip()
        if line.startswith("Stem:"):
            mode = "stem"
            stem_lines.append(line.split(":", 1)[1].strip())
            continue
        choice = CHOICE_RE.match(line)
        if choice and mode in {"stem", "choice"}:
            mode = "choice"
            choices[choice.group(1)] = choice.group(2).strip()
            continue
        if line.startswith("Answer:"):
            mode = "meta"
            answer = line.split(":", 1)[1].strip().upper()[:1]
            continue
        if line.startswith("Objective:"):
            objective = line.split(":", 1)[1].strip()
            continue
        if line.startswith("Why:"):
            mode = "why"
            why_lines.append(line.split(":", 1)[1].strip())
            continue
        if mode == "stem" and line.strip():
            stem_lines.append(line.strip())
        elif mode == "why":
            why_lines.append(line.strip())
    if not stem_lines or set(choices) != {"A", "B", "C", "D"} or answer not in choices:
        return None
    stem = " ".join(stem_lines)
    answer_text = choices[answer]
    return Item(
        id=f"{code}::{lesson}::{qid}",
        module=code,
        lesson=lesson,
        stem=stem,
        choices=choices,
        answer=answer,
        objective=objective,
        why=" ".join(why_lines).strip(),
        number=parse_number(answer_text),
        channel=channel_for(lesson, stem),
    )


def load_modules(root: Path | None = None) -> list[Module]:
    root = root or repo_root()
    theory_dir = root / "knowledge" / "theory"
    question_dir = root / "knowledge" / "questions"
    codes = set()
    for folder in (theory_dir, question_dir):
        if not folder.exists():
            continue
        for path in folder.glob("m*.md"):
            codes.add(path.name.split("-", 1)[0])
    modules: list[Module] = []
    for code in sorted(codes):
        theory = next(theory_dir.glob(f"{code}-*.md"), None) if theory_dir.exists() else None
        questions = next(question_dir.glob(f"{code}-*.md"), None) if question_dir.exists() else None
        sample = theory or questions
        slug = sample.stem.split("-", 1)[1] if sample else code
        title = slug.replace("-", " ").title()
        if theory and theory.exists():
            first = theory.read_text(encoding="utf-8").splitlines()[0]
            if first.startswith("# "):
                title = re.sub(r"^#\s*Module\s+\d+\.?\s*", "", first).strip() or title
        module = Module(code=code, slug=slug, title=title)
        if theory and theory.exists():
            module.chunks = parse_theory(code, theory.read_text(encoding="utf-8"))
        if questions and questions.exists():
            module.items = parse_questions(code, questions.read_text(encoding="utf-8"))
        modules.append(module)
    return modules


def find_module(modules: list[Module], name: str) -> Module | None:
    key = name.strip().lower()
    for module in modules:
        if key in {module.code.lower(), module.slug.lower(), module.title.lower()}:
            return module
        if key.isdigit() and module.code == f"m{int(key):02d}":
            return module
    for module in modules:
        if key in module.slug.lower() or key in module.title.lower():
            return module
    return None
