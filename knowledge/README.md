# Lika MDCB knowledge bank

Personal study bank for the Medical Dosimetrist Certification Board (CMD) exam.
The exam is in English. Notes and questions in this bank are in English so the wording matches the test.

This is not the DoseGrid course and not an MDCB publication.
The module and lesson titles in `plan/dosegrid-public-curriculum.md` follow the curriculum list that DoseGrid shows on the public course page.
Lesson text, quizzes, and practice exams here are original notes written from the public MDCB test blueprint and from openly published references (AAPM task group reports, QUANTEC summary tables, NCRP/NRC limits stated in the public applicant materials).

Retired MDCB sample items are copyrighted by MDCB and are not copied into this repo.
Paid DoseGrid notes and quizzes are not copied into this repo.

## Layout

| Path | What it is |
| --- | --- |
| `plan/dosegrid-public-curriculum.md` | Full public lesson list, 45 modules |
| `plan/mdcb-objective-map.md` | Each MDCB 2023 objective and which modules cover it |
| `official/` | Facts taken from public MDCB pages and handbooks, with source URLs |
| `theory/` | Original teaching notes, one file per module |
| `questions/` | Original multiple-choice items, one file per module |
| `commute/` | Options for studying by voice during the drive |

## Local run

Telegram is not connected. On the Mac:

```bash
python3 -m study list
python3 -m study
python3 -m study check
python3 -m study voice-check
```

`теория` sends a lesson in chunks. `задачи` asks for a number and checks it against the stored solution. `квиз` is four choices. `вместе` is a paragraph, then three questions on that paragraph. `дорога` writes `progress/road-prompt.md`, a prompt to paste into a voice chat. That file contains only items that can be answered without a sheet. Misses are stored in `progress/lika.json` and come back first. A run of three correct answers drops that item from the frequent rotation.

## How a module file is shaped

Theory: `theory/mNN-slug.md`
Questions: `questions/mNN-slug.md`

Every lesson title from the plan has a section in both files.
Calculation lessons include a worked numeric example and numeric items.
Each question has four options, one answer, a rationale, and the MDCB objective it trains.
