# Rules for the RM Review porting wave

Work ONLY inside this worktree: `/Users/ivazhu01/projects/lika-cert-prep/.worktrees/rm` (branch `rm-review-port`).
Source material (read-only, copyrighted, never copy wording, never commit):
`/Users/ivazhu01/projects/lika-cert-prep/inbox/text/*.txt` and the 8 reports in
`knowledge/review/rm-review/*.md` (the reports list the MISSING facts per module; start there).

## Where to write

- Theory: APPEND new sections to the existing `knowledge/theory/mNN-<slug>.md` (the loader reads
  only the first theory file per module). Each new section starts with `## <Lesson name>` and a
  `**Objectives:** <code>` line, then prose paragraphs (no tables longer than ~10 rows, no images).
  Lesson names must be new and unique inside the module.
- Questions: create a NEW file `knowledge/questions/mNN-rm2-<slug>.md` (round 2; do not touch existing mNN-rm-*.md files) (do not edit existing question
  files — another branch is editing them). File starts with `# Module NN. <Title>` and a one-line
  note "Original items." Then `## <Lesson name>` headings that match the theory sections you added
  (so the "Вместе" mode pairs them), then items numbered `### Q1`, `### Q2`, … restarting at Q1 for
  each lesson heading.

## Item format (parser is strict)

```
### Q7
Stem: One or two sentences. Numbers in words or digits, no LaTeX, no formulas in the stem.
A. first option
B. second option
C. third option
D. fourth option
Answer: C
Objective: III.8
Why: Two to five sentences. State the correct fact, then why each distractor is wrong. For calculations show the arithmetic and a check.
```

- Exactly four options A–D; `Answer:` is a single letter; mix the correct letter across A/B/C/D
  roughly evenly (do not key everything A).
- For numeric answers, the correct option is a number with a unit; distractors are plausible
  wrong-method results (not zeros, not duplicates).
- Objective codes: I (physics), II (imaging/anatomy), III (planning), IV (calcs), V (brachy),
  VI (protection), VII (QA), with sub-numbers as used in the existing files of that module;
  `admin` for format/strategy items.
- English exam terminology; current standards (QUANTEC, TG-101, TG-142, TG-203, TG-43U1,
  10 CFR 20/35/71, NCRP 147/151). Do not import anything the reports flagged as a wrong key or
  outdated; if two sources disagree, write the Why to say which figure the bank uses and why.
- Original wording only. Paraphrase facts; never reuse a stem from the source files.

## Before you finish

Run from the worktree:

```
python3 -c "from study.bank import load_modules; ms=load_modules(); ids=[i.id for m in ms for i in m.items]; print(len(ids), len(set(ids)))"
python3 -m pytest -q
```

Both counts must be equal and tests must pass. Do NOT run git commands; the orchestrator commits.
Return: files touched, number of theory sections and items added per module, and anything you
deliberately skipped and why.
