# Module 43. Memory lane

Original notes for MDCB CMD prep. Objective III.8: OAR constraints from QUANTEC, TG-101, and related summaries. These are 2010-era planning estimates for conventional fractionation unless a row is explicitly stereotactic. They are not personal prescriptions. A physician’s constraint in the chart overrides a memory number for that patient. On an exam item, the number in the stem is the one to apply, and these are the numbers to use when the stem says QUANTEC or TG-101 and prints no other figure.

Confirm every TG-101 cell in Table III of the AAPM report before clinical use. This file gives the serial spinal cord row candidates are drilled on, and it does not invent optic, brainstem, or brachial-plexus TG-101 cells.

## QUANTEC

**Objectives:** III.8

**What the exam expects:** Apply a QUANTEC summary estimate to a stated DVH point, conventional fractionation. Know that a rectum-style constraint is a set: one passing bin does not rescue a failing bin. Know the serial-cord TG-101 pattern well enough to recognize it, and look up every other SBRT organ in Table III rather than reconstruct it.

The estimates below are the 2010 QUANTEC summary (International Journal of Radiation Oncology, Biology, Physics), conventional fractionation, for the endpoint named. They are not prescriptions.

| Organ | Summary estimate | Endpoint the summary is about |
| --- | --- | --- |
| Spinal cord | Dmax 50 Gy | about 0.2% myelopathy |
| Brainstem | whole organ < 54 Gy | necrosis / neuropathy |
| Optic nerves and chiasm | < 55 Gy | optic neuropathy |
| Parotid | mean < 25 Gy to both glands, or spare one gland to mean < 20 Gy | long-term salivary function |
| Lung | V20 ≤ 30% and mean lung dose 20 Gy | about 20% symptomatic pneumonitis |
| Heart, pericardium | mean < 26 Gy | pericarditis |
| Rectum | the set V50 < 50%, V60 < 35%, V65 < 25%, V70 < 20%, V75 < 15% | late rectal toxicity; use the set together |
| Kidney | mean < 15–18 Gy | renal function, bilateral consideration |
| Liver | mean < 30–32 Gy | radiation liver injury, excluding HCC and Child-Pugh liver disease |
| Small bowel | V15 < 120 cm³ for individual loops, or V45 < 195 cm³ for the peritoneal space | late toxicity |

Lung is a pair: V20 and mean dose. Quoting only the mean misses a failing V20. Rectum is a five-point set. Small bowel has two definitions; the stem must say loops or peritoneal space. Liver’s 30–32 Gy mean is not the number for a hepatocellular carcinoma or a Child-Pugh abnormal liver; those cases use a different, more restrictive approach that this memory row does not cover.

**TG-101 serial spinal cord**, volume limit and point maximum. Confirm these cells in TG-101 Table III before using them clinically. The figures candidates are expected to recognize:

| Fractions | About 0.35 cm³ | Point maximum |
| --- | --- | --- |
| 1 | 10 Gy | 14 Gy |
| 3 | 18 Gy | 21.9 Gy |
| 5 | 23 Gy | 30 Gy |

Optic pathway, brainstem, and brachial plexus stereotactic limits: confirm in TG-101 Table III. Those cells are not reproduced here.

SBRT cord limits and the QUANTEC 50 Gy cord limit answer different fractionations. Do not compare a 14 Gy single-fraction point maximum with the 50 Gy conventional Dmax as if they were the same constraint.

### Worked example

**Given.** Conventional fractionation prostate plan. The rectum DVH reads V50 = 48%, V60 = 36%, V65 = 22%, V70 = 18%, V75 = 12%. Judge it against the QUANTEC rectum set above. These are summary estimates, not a prescription written for this patient.

**Arithmetic, one bin at a time.**

- V50: \(48 < 50\), inside the estimate
- V60: \(36 < 35\) is false; 36 is 1 percentage point over 35
- V65: \(22 < 25\), inside
- V70: \(18 < 20\), inside
- V75: \(12 < 15\), inside

**Check.** \(36 - 35 = 1\). The other four inequalities hold. One failure is enough for the set.

**Result means.** The plan does not meet the QUANTEC rectum set, because V60 is 36% against an estimate of less than 35%. A note that says “four of five passed” still describes a set that failed. The next planning step is to reduce the volume at 60 Gy, then re-read every bin. This comparison does not change the physician’s prescription.

**Wrong turns**

- Passing the plan on V70 alone.
- Applying the conventional 50 Gy cord limit to a 3-fraction SBRT cord dose of 18 Gy and calling it a QUANTEC pass. Different fractionation, different table.
- Using the liver 30–32 Gy mean for an HCC case the row explicitly excludes.
- Treating a parotid mean of 24 Gy to both glands as a failure against the “spare one gland to 20 Gy” branch. The bilateral mean under 25 Gy is the branch that applies when both glands are irradiated. The spare-one-gland branch is the alternative.
- Inventing a TG-101 optic or plexus number that is not in front of you.

**Traps.** Write the fractionation (conventional versus 1, 3, or 5 fractions) on the first line. Then use either the QUANTEC table or the TG-101 cord row, not a blend.

**Sources.** QUANTEC, IJROBP 2010, the organ papers and the summary tables. AAPM TG-101 Table III for stereotactic serial-organ doses. Marks et al. is the QUANTEC overview paper if you need the citation trail back to a single organ chapter.

## QUANTEC Mini-Quiz

**Skills this quiz checks**

- Apply one QUANTEC estimate to a stated DVH point, and apply the rectum numbers as a set.
- Keep lung as V20 ≤ 30% and mean dose 20 Gy together.
- Keep the liver mean off HCC and Child-Pugh cases.
- Separate conventional cord Dmax 50 Gy (about 0.2% myelopathy) from the TG-101 1-, 3-, and 5-fraction cord row.
- Refuse to invent TG-101 cells for organs you would otherwise have to look up in Table III.
- State that these are 2010 summary estimates, not a prescription.

## Physical Density of Materials

**Objectives:** IV.4, I.9, III.8

**What the exam expects:** The same density list as module 37, ready to use in a water-equivalent-thickness product. Contrast and metal are not on this tissue list.

| Material | Physical density (g/cm³) |
| --- | --- |
| Air | about 0.001 |
| Lung | about 0.25–0.30 |
| Water | 1.00 |
| Muscle | about 1.04 |
| Bone | about 1.85 |

### Worked example

**Given.** A beam crosses 5.0 cm of bone. Use density 1.85. The surrounding calculation had been water (density 1.00) through that same 5.0 cm.

**Formula.** \(d_w = d \times \rho\). Extra water-equivalent thickness \(= d(\rho - 1)\).

**Substitute.** \(d_w = 5.0 \times 1.85 = 9.25\) cm. Extra \(= 5.0 \times 0.85 = 4.25\) cm.

**Check.** \(9.25 - 5.00 = 4.25\). \(5 \times 1.85 = 9.25\).

**Result means.** The bone slab is 9.25 cm of water equivalent, 4.25 cm more than the homogeneous water path. A hand calculation that leaves the 5 cm as water under-attenuates. Air through the same 5.0 cm physical gap is \(5.0 \times 0.001 = 0.005\) cm of water equivalent, which is why an air cavity barely attenuates and why it must not be assigned lung density (0.25–0.30) or bone.

**Wrong turns**

- Bone at 1.04 (that is muscle) or lung at 1.00.
- Air at 0.25 (that is the low end of lung).
- A hip prosthesis assigned “bone” at 1.85. Metal is an override to the alloy, not a bone row (module 37).
- Relative electron density and physical density swapped for metal. They diverge for high-Z materials; the tissue list above is the recall list for air, lung, water, muscle, and bone.

**Traps.** If the stem says “lung” and gives no number, use about 0.25–0.30 and show which end you picked. If the stem gives 0.26, use 0.26.

**Sources.** Standard physical-density tables used with CT-to-density commissioning (module 37). QUANTEC is not a density reference; it shares this module only because both are memory items.
