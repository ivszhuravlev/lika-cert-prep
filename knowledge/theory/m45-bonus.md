# Module 45. Bonus content

Original notes for MDCB CMD prep. Trial phases and binary conversion are bonus-module skills. The mixed calculation uses only formulas already justified in modules 33–42. Nothing here is a retired exam item.

## Only if you have extra time

**Objectives:** study order across domains I–VII. This lesson is not its own blueprint row.

**What the exam expects:** Nothing in this lesson is a hidden high-weight domain. Use leftover time on misses that actually move the score.

Domain III, treatment planning, is 42% of the exam. Domain I is 14%, dose calculation 13%, protection and QA 9% each, localization 8%, brachytherapy 5%. A last week goes to the weakest of those weighted domains first. Inside dose calculation, the items that are either all right or all wrong are the ones with a formula and a trap: PDD mixed with TMR, wedge factor omitted while the wedge is in the beam, half-life used where mean life belongs, Mayneord described as a scatter correction, Khan’s electron rule used on a stem that said Bentel.

A practical order when the calendar is short:

1. One timed mixed set from module 44, graded on the setup (formula, substitution, check), not on recognition of the answer.
2. The memory rows that cannot be derived at the desk: NCRP 116 limits, QUANTEC conventional estimates, physical densities, TG-142 cadence, point A, the nuclide half-lives.
3. One redo of any miss from step 1, in the theory file, the same day.

New commercial videos and a second pass through material you already calculate cleanly are the low-yield choice. The arithmetic in modules 33–36 is the high-yield choice if those items are still slow.

### Worked example

**Given.** The form has 155 items. Dose calculation is 13% of the blueprint.

**Arithmetic.** \(155 \times 0.13 = 20.15\), about 20 items. Missing half of those setups is 10 items. \(10/155 = 0.0645\), which is 6.5% of the form.

**Check.** \(155 \times 0.13 = 20.15\). \(10/155 = 0.064516\).

**Result means.** Ten calculation misses are several percent of the whole exam. A last hour spent making Mayneord, MU, gap, and wedge setups automatic is aimed at that 6.5%. A last hour spent re-reading a topic you already score cleanly does not move the same number of items.

**Traps.** Treating every domain as equal. Brachytherapy is about 8 items; treatment planning is about 65.

**Sources.** Domain weights in the 2023 MDCB test specifications, as listed in module 44.

## Bonus Calculations

**Objectives:** IV.3, IV.1, IV.2

**What the exam expects:** Chain equivalent square, interpolation, and an SAD MU without mixing in a PDD. On a separate electron item, use the author’s rule the stem names.

### Worked example: equivalent square, interpolation, wedge, SAD MU

**Given.**

- Field 15 cm × 6 cm at isocenter
- Calibration: 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm
- Calculation point at isocenter, so source-to-point distance = 100 cm
- Depth 10 cm
- Open TMR table: 0.790 at equivalent square 8.0 cm, 0.770 at 9.0 cm
- \(S_c = 1.000\), \(S_p = 1.000\), tray factor = 1
- Wedge factor 0.600, and the wedge will be in the beam
- Dose 200 cGy

**Formulas.**

\[
\text{side} = \frac{2ab}{a+b}
\qquad
\mathrm{TMR} = y_1 + \frac{x-x_1}{x_2-x_1}(y_2-y_1)
\]

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times S_c \times S_p \times \mathrm{TMR} \times \mathrm{WF} \times (\mathrm{SAD}/\mathrm{SPD})^2}
\]

No PDD in this SAD formula. Symbols are the ones defined in module 35. \(\mathrm{SAD}/\mathrm{SPD} = 1\).

**Substitute, equivalent square.** \(2 \times 15 \times 6 / (15+6) = 180/21 = 8.571\) cm.

**Substitute, interpolation.** Fraction \(= (8.571-8.000)/(9-8) = 0.571\).

\[
\mathrm{TMR} = 0.790 + 0.571(0.770-0.790) = 0.790 - 0.01142 = 0.77858
\]

**Substitute, MU.**

\[
\mathrm{MU} = \frac{200}{1.0 \times 0.77858 \times 0.600} = \frac{200}{0.46715} = 428.1
\]

**Arithmetic check.** \(180/21 = 8.571\). \(0.571 \times 0.020 = 0.01142\). \(0.77858 \times 0.600 = 0.467148\). \(428.1 \times 0.46715 \approx 200.0\) ( \(428.1 \times 0.467 = 199.92\), and \(428.1 \times 0.00015 \approx 0.06\), sum 199.98 ).

**Result means.** Set **428 MU**. The wedge is in the denominator because it is in the beam. TMR 0.779 (three digits) is the interpolated depth factor for an 8.57 cm equivalent square, not for a 15 cm jaw and not for a 6 cm jaw.

**Wrong turns that build the usual distractors**

- Equivalent square replaced by the average \((15+6)/2 = 10.5\) cm, which reads the wrong TMR row.
- Interpolation skipped, TMR left at 0.790. Then \(\mathrm{MU} = 200/(0.790\times0.600) = 422.0\), a few MU low on the set value and a different dose if 428 were still used.
- Wedge omitted from the MU while the wedge stays in the beam. \(\mathrm{MU} = 200/0.77858 = 256.9\), and the delivered dose is \(256.9 \times 0.77858 \times 0.600 = 120\) cGy. Delivered/prescribed \(= 0.60\). That is the module 34 underdose.
- PDD copied into this SAD formula because a percent depth dose happened to be printed on the same scrap page.
- Half-life or mean life. This beam is not a decaying source.
- Khan versus Bentel. Those names belong to the electron energy rule below, not to a photon TMR.

### Worked example: Khan versus Bentel electron energy

**Given.** The distal target depth is 4.0 cm. The stem asks for a single electron energy using a named rule of thumb. Lead shielding for that energy is about \(E/2\) mm. Electrons lose about 2 MeV per cm of water. Practical range is about \(E/2\) cm.

These are the usual course rules. The stem decides which author applies. They are not interchangeable, and they are not a measured cutout factor (module 42).

**Khan-style rule used in these items:** cover with the 90% isodose, and that depth is about \(E/4\) cm.

\[
E/4 = 4.0 \quad \Rightarrow \quad E = 16 \text{ MeV}
\]

**Bentel-style rule used in these items:** cover with the 80% isodose, and that depth is about \(E/3\) cm.

\[
E/3 = 4.0 \quad \Rightarrow \quad E = 12 \text{ MeV}
\]

**Check for 12 MeV, the Bentel choice.** Practical range \(E/2 = 6.0\) cm. Energy loss \(12\,\mathrm{MeV} / 2\,\mathrm{MeV\,cm^{-1}} = 6.0\) cm. The two range pictures agree. Lead \(= 12/2 = 6\) mm.

**Check for 16 MeV, the Khan choice.** Range \(E/2 = 8.0\) cm. Lead \(= 8\) mm. Using Bentel’s 12 MeV on a Khan stem under-covers a 90% requirement: \(12/4 = 3.0\) cm, short of the 4.0 cm target.

**Result means.** The two famous wrong answers are each other’s right answers. Write the author’s name and the percent (90 or 80) before you divide. Then measure the cutout factor at the energy you picked. The rule of thumb does not give MU.

**Sources.** Khan and Gibbons, electron rules of thumb (about 2 MeV/cm, practical range about \(E/2\), 90% depth often taken as about \(E/4\), lead about \(E/2\) mm). Bentel, *Radiation Therapy Planning*, for the 80% coverage rule (depth about \(E/3\)) that items contrast with Khan. Confirm the edition you were taught if a local handout swaps the percents; on the exam, the stem’s author and percent win.

## Phases of Clinical Trials

**What the exam expects:** Name the phase from the job the study is doing. The phase is not the p-value and not the number of gray.

| Phase | Job |
| --- | --- |
| I | Safety and dose finding. Small sequential cohorts. The dose rises until toxicity defines the maximum tolerated dose. |
| II | Does it show activity? A single-arm or early efficacy signal, with toxicity still watched. Not yet the definitive comparison. |
| III | Randomized comparison against the standard of care. This is the phase that changes practice if it is positive. |
| IV | After approval or after the treatment is already in use. Long-term effects, rare effects, effectiveness outside the original trial. |

### Worked example

**Given.** Three study descriptions.

- A: 20 patients, escalating dose until toxicity limits the next step.
- B: several hundred patients, randomly assigned to the new regimen or to the current standard.
- C: a registry of rare late effects after the regimen is already in routine use.

**Result.** A is phase I. B is phase III. C is phase IV. A phase II study would have sat between A and B: a larger look at response without the definitive randomization.

**Check.** Escalation of dose is the phase I signature. Randomization against standard of care is the phase III signature. Post-marketing surveillance is phase IV. None of these is decided by whether the endpoint was overall survival; phase III often uses survival, and a randomized phase II can also exist. When the stem says “randomized against standard of care,” choose phase III.

**Wrong turns.** Calling every randomized study phase IV. Calling a dose-escalation study phase III because the doses are high. Using trial phase to pick a QUANTEC number.

**Sources.** Standard ICH / FDA phase definitions as taught in clinical-research introductions. This bonus topic is not one of the seven weighted CMD domains.

## Binary Number/Decimal Conversion

**What the exam expects:** Convert a modest integer both directions, and convert a short binary fraction. Show the place values so the check is the addition.

Place values left of the point: 32, 16, 8, 4, 2, 1 for six bits. Right of the point: \(1/2\), \(1/4\), \(1/8\), \(1/16\).

### Worked example: 45 decimal to binary

**Given.** 45.

**Method.** Divide by 2 and keep remainders. Read remainders from last to first.

\[
\begin{align*}
45 &= 22 \times 2 + 1 \\
22 &= 11 \times 2 + 0 \\
11 &= 5 \times 2 + 1 \\
5 &= 2 \times 2 + 1 \\
2 &= 1 \times 2 + 0 \\
1 &= 0 \times 2 + 1
\end{align*}
\]

**Arithmetic.** Remainders upward: 1, 0, 1, 1, 0, 1. Binary **101101**.

**Check.** \(32 + 8 + 4 + 1 = 45\). The 16-place and the 2-place are zero: \(101101\) has zeros in those positions.

### Worked example: 1101 binary to decimal

**Given.** 1101.

**Arithmetic.** \(1\times8 + 1\times4 + 0\times2 + 1\times1 = 13\).

**Check.** \(8+4+1 = 13\). Thirteen divided by 2 gives remainders 1, 0, 1, 1 upward, which is 1101.

### Worked example: 0.625 decimal to binary

**Given.** 0.625.

**Method.** Multiply the fractional part by 2. The integer part of each product is the next bit.

\[
0.625 \times 2 = 1.250 \rightarrow 1
\qquad
0.250 \times 2 = 0.500 \rightarrow 0
\qquad
0.500 \times 2 = 1.000 \rightarrow 1
\]

**Result.** Binary **0.101**.

**Check.** \(1/2 + 0/4 + 1/8 = 0.500 + 0.125 = 0.625\).

**Wrong turns.** Reading remainders top to bottom, which turns 45 into 101011 (that is \(32+8+2+1 = 43\)). Dropping a leading 1. Treating 0.101 as “one hundred one thousandths” in decimal instead of halves and eighths.

**Meaning.** 45 is 101101, 1101 is 13, and 0.625 is 0.101. The addition of place values is the check every time.

**Sources.** Ordinary place-value conversion. This is a bonus-module skill, not a dose formula.

## Radiation Therapy Concepts Quiz

**Skills this quiz checks**

- Phase I dose finding, phase II activity, phase III randomized comparison to standard care, phase IV after the treatment is in use.
- Binary place values in both directions, including a fraction such as 0.625 = 0.101, with the addition check.
- A mixed SAD MU: equivalent square, then interpolation, then TMR in the denominator, wedge in the denominator, calibration stated, PDD kept out.
- The wedge-omitted underdose on that same chain (delivered/prescribed = WF).
- Electron energy from the author named in the stem: Khan 90% about \(E/3.2\) and 80% about \(E/2.8\); Bentel 90% about \(E/4\) and 80% about \(E/3\); plus about 2 MeV/cm, range about \(E/2\) cm, and lead about \(E/2\) mm.
- One memory pass across the course: NCRP 116 limits, two HVLs transmit 25%, point A is 2 cm by 2 cm, Monte Carlo at interfaces, pencil beam weak in lung, dosimetrist does not prescribe, RO-ILS is voluntary.

A short mixed review, if you do nothing else in this module: write Mayneord’s two squared brackets and say “inverse square only”; write the SSD MU with PDD and the SAD MU with TMR on separate lines; write permanent-implant dose as initial dose rate × 1.443 × half-life; write \(H = \sum w_R D\) and the NCRP lens as 150 mSv when the stem says NCRP.
