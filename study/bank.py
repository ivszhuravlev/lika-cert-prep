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
CHOICE_RE = re.compile(r"^([A-D])\.\s*(.*)$")
# A thousands group is exactly three digits. A comma with any other width is a decimal,
# so 1,5 is 1.5 and 1,500 is 1500.
_NUMBER = re.compile(
    r"""
    [+-]?
    (?:
        \d{1,3}(?:[ \u00a0\u202f]\d{3})+(?:[.,]\d+)?
        |
        \d+(?:,\d{3})+(?:\.\d+)?
        |
        \d+[.,]\d+
        |
        \d+
        |
        [.,]\d+
    )
    (?:[eE][+-]?\d+)?
    (?:\s*[xX*]\s*10\^?\(?\s*[+-]?\d+\s*\)?)?
    """,
    re.VERBOSE,
)
_WORDS = re.compile(r"[A-Za-z]{2,}")
_UNITS = {
    "bq",
    "cc",
    "cgy",
    "ci",
    "cm",
    "day",
    "days",
    "deg",
    "degree",
    "degrees",
    "dimensionless",
    "eqd2",
    "ev",
    "fx",
    "gbq",
    "gy",
    "hour",
    "hours",
    "hr",
    "hrs",
    "hvl",
    "hz",
    "kbq",
    "kev",
    "kg",
    "khz",
    "km",
    "mbq",
    "mci",
    "mev",
    "mg",
    "mhz",
    "min",
    "mins",
    "minute",
    "minutes",
    "mm",
    "mr",
    "ms",
    "msv",
    "mu",
    "mus",
    "mv",
    "nm",
    "pm",
    "rad",
    "rem",
    "sec",
    "second",
    "seconds",
    "sv",
    "tvl",
    "uci",
    "ug",
    "usv",
    "year",
    "years",
    "yr",
    "yrs",
}
_KINDS = {
    "exam": ("what the exam expects", "core facts", "skills this quiz checks"),
    "work": ("formulas", "formula", "worked example"),
    "trap": ("traps", "usual wrong turn", "wrong turns"),
}


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


def _prepare(text: str) -> str:
    return text.replace("−", "-").replace("–", "-").replace("×", "x").replace("·", "x")


def _glued(text: str, start: int, end: int) -> bool:
    """A digit inside Co-60, A0, or 2ab is part of the name, not a value."""
    if start > 0 and text[start - 1].isalpha():
        return True
    if end < len(text) and text[end].isalpha():
        return True
    if start >= 2 and text[start - 1] == "-" and text[start - 2].isalpha():
        return True
    return False


def _literals(text: str):
    cleaned = _prepare(text)
    for match in _NUMBER.finditer(cleaned):
        token = match.group(0).rstrip()
        if not token:
            continue
        end = match.start() + len(token)
        if _glued(cleaned, match.start(), end):
            continue
        yield cleaned, match.start(), end, token


def _token_value(token: str) -> float | None:
    text = token.strip()
    power = 0
    sci = re.search(r"\s*[xX*]\s*10\^?\(?\s*([+-]?\d+)\s*\)?\s*$", text)
    if sci:
        power = int(sci.group(1))
        text = text[: sci.start()].strip()
    exp = 0
    exp_match = re.search(r"[eE]([+-]?\d+)$", text)
    if exp_match:
        exp = int(exp_match.group(1))
        text = text[: exp_match.start()]
    if not text:
        return None
    sign = 1
    if text[0] in "+-":
        sign = -1 if text[0] == "-" else 1
        text = text[1:]
    text = text.replace(" ", "").replace("\u00a0", "").replace("\u202f", "")
    if not text:
        return None
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        groups = text.split(",")
        if (
            len(groups) >= 2
            and groups[0].isdigit()
            and all(len(part) == 3 and part.isdigit() for part in groups[1:])
        ):
            text = "".join(groups)
        else:
            text = groups[0] + "." + "".join(groups[1:])
    if text.startswith("."):
        text = "0" + text
    try:
        return sign * float(text) * (10**exp) * (10**power)
    except ValueError:
        return None


def parse_number(text: str) -> float | None:
    for _cleaned, _start, _end, token in _literals(text):
        value = _token_value(token)
        if value is not None:
            return value
    return None


def _is_quantity(text: str, start: int, end: int) -> bool:
    """A computed choice leads with its value. A sentence that mentions a digit does not."""
    before = _WORDS.findall(text[:start])
    after = [word for word in _WORDS.findall(text[end:]) if word.lower() not in _UNITS]
    if len(before) > 3:
        return False
    if before and len(after) > 1:
        return False
    return True


def computed_number(text: str) -> float | None:
    """The choice's computed value, or None for a sentence or a symbol such as Co-60."""
    for cleaned, start, end, token in _literals(text):
        if not _is_quantity(cleaned, start, end):
            return None
        return _token_value(token)
    return None


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


def _paragraphs(body: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n[ \t]*\n", body.strip()) if part.strip()]


def _heading_name(paragraph: str) -> str | None:
    bold = re.fullmatch(r"\*\*(.+?)\*\*", paragraph)
    if bold:
        return bold.group(1).strip()
    hashed = re.fullmatch(r"#{1,6}\s+(.+)", paragraph)
    if hashed:
        return hashed.group(1).strip()
    return None


def _kind_of(name: str, current: str) -> str:
    key = name.strip().lower().rstrip(".:").strip()
    for kind, names in _KINDS.items():
        if key in names:
            return kind
    return current


def _lesson_chunks(lesson: str, body: str) -> list[Chunk]:
    """One chunk per paragraph. A bare heading stays with the paragraph it introduces."""
    paragraphs = _paragraphs(body)
    if not paragraphs:
        return []
    chunks: list[Chunk] = []
    pending: list[str] = []
    kind = "exam"
    for paragraph in paragraphs:
        name = _heading_name(paragraph)
        if name is not None:
            kind = _kind_of(name, kind)
            pending.append(paragraph)
            continue
        chunks.append(Chunk(lesson, kind, "\n\n".join([*pending, paragraph])))
        pending = []
    if pending:
        chunks.append(Chunk(lesson, kind, "\n\n".join(pending)))
    return chunks


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
        number=computed_number(answer_text),
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
        theory_paths = sorted(theory_dir.glob(f"{code}-*.md")) if theory_dir.exists() else []
        question_paths = sorted(question_dir.glob(f"{code}-*.md")) if question_dir.exists() else []
        theory = theory_paths[0] if theory_paths else None
        sample = theory or (question_paths[0] if question_paths else None)
        slug = sample.stem.split("-", 1)[1] if sample else code
        title = slug.replace("-", " ").title()
        if theory and theory.exists():
            first = theory.read_text(encoding="utf-8").splitlines()[0]
            if first.startswith("# "):
                title = re.sub(r"^#\s*Module\s+\d+\.?\s*", "", first).strip() or title
        module = Module(code=code, slug=slug, title=title)
        if theory and theory.exists():
            module.chunks = parse_theory(code, theory.read_text(encoding="utf-8"))
        items = []
        for questions in question_paths:
            items.extend(parse_questions(code, questions.read_text(encoding="utf-8")))
        module.items = items
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
