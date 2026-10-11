# Module 45. Bonus Content

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Only if you have extra time

### Q1
Stem: Which study choice is the best use of a last review hour?
A. Work missed calculation types, then a short mixed set
B. Reread only the topics you already ace
C. Memorize a new cord tolerance you invented
D. Skip MU setups because the TPS will do them
Answer: A
Objective: IV.3
Why: The highest-yield last hour is the calculation you miss: inverse square, Mayneord, equivalent square, MU with the calibration written in the stem, gap, HVL, and the brachytherapy mean-life dose. Correct choice: Work missed calculation types, then a short mixed set. Time goes to the weak calculation, not to another pass over a strength. Do not invent dose limits. Use the published QUANTEC numbers you can defend. Hand MU, with the calibration stated, is still a tested skill.

### Q2
Stem: A formula sheet is only useful if you can do what with it?
A. Search it for a QUANTEC number that was never published
B. Skip units
C. Apply PDD inside an SAD MU because both words contain 'dose'
D. Substitute the stem's numbers and reject the common wrong operation
Answer: D
Objective: IV.3
Why: The sheet does not know whether the setup is SSD or SAD, whether the wedge was in the beam, or whether the half-life was converted to hours. Substitution and units are the skill. Correct choice: Substitute the stem's numbers and reject the common wrong operation. If a cell is not one you can defend, do not invent it. Unit errors, especially hours versus days in a permanent implant, are a standard miss. SAD with a dmax calibration uses TMR.

### Q3
Stem: Which pair is a real mix-up to drill on purpose?
A. Half-life factor 0.693 versus mean-life factor 1.443
B. Water density 1.00 versus water density 1.00
C. A half-beam angle of 0° versus a half-beam angle of 0°
D. DICOM versus DICOM
Answer: A
Objective: V.6
Why: Permanent-implant total dose uses mean life, 1.443 × half-life, not 0.693 × half-life. 0.693 is ln(2), which belongs in the decay constant. Drilling that swap prevents a factor-of-two class error. Correct choice: Half-life factor 0.693 versus mean-life factor 1.443. That is not a mix-up. Same number. Not a contrast.

### Q4
Stem: Before trusting a retreated cord EQD2, what do you check?
A. That physical doses were added with no fraction-size term
B. That both courses used the α/β you were told to use, and that fraction size was converted
C. That Mayneord F replaced α/β
D. That a conventional cord correlate of 50 Gy can be ignored once any EQD2 is written down
Answer: B
Objective: III.3
Why: EQD2 depends on the α/β stated in the problem and on every fraction size. A 2 Gy course converts to itself. A hypofractionated course does not. The cord correlate used here is 50 Gy, and it is not replaced by Mayneord F. Adding raw gray hides a change in fraction size.

### Q5
Stem: Which habit catches a wedge-factor omission?
A. Assume a wedge factor of 1 for every physical wedge
B. Put the wedge factor in the numerator
C. Replace the wedge factor with the hinge angle in degrees
D. Compare the MU with and without the wedge factor before you approve the plan
Answer: D
Objective: IV.2
Why: If the wedge is in the beam and the factor never entered the MU, the patient receives intended dose × wedge factor. The check is to recompute the MU with the factor and see the difference. Correct choice: Compare the MU with and without the wedge factor before you approve the plan. Physical and dynamic wedges both reduce cGy per MU. The factor belongs in the denominator of the MU. The hinge angle is geometry, not a transmission.

## Bonus Calculations

### Q1
Stem: Bonus. Another Mayneord pair, not the earlier SSD sets. PDD at 18 cm depth is 51.2% for SSD 100 cm. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 125 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 79.5 %
B. 52.7 %
C. 54.2 %
D. 48.4 %
Answer: C
Objective: IV.3
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(125+1.5)/(100+1.5)]^2 × [(100+18)/(125+18)]^2 = (1.2463)^2 × (0.8252)^2 = 1.5533 × 0.6809 = 1.0576. PDD2 = 51.2 × 1.0576 = 54.15%, which rounds to 54.2 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 79.5 %. Multiplying the two distance ratios once each, without squaring, gives 52.7 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 48.4 %.

### Q2
Stem: Bonus. New field lengths and SSDs. Field 1 length at SSD is 36 cm with SSD 100 cm. Field 2 length at SSD is 12 cm with SSD 90 cm. The fields should abut at 6 cm depth. Skin gap = (L1/2)×(d/SSD1) + (L2/2)×(d/SSD2). What is the skin gap?
A. 2.96 cm
B. 1.08 cm
C. 1.48 cm
D. 390.00 cm
Answer: C
Objective: IV.3
Why: Each term is how far that field's edge diverges from its central axis over depth d. Field 1: (36/2) × (6/100) = 18 × 0.0600 = 1.0800 cm. Field 2: (12/2) × (6/90) = 6 × 0.0667 = 0.4000 cm. Gap = 1.0800 + 0.4000 = 1.4800 cm, reported as 1.48 cm. A gap that is too small overlaps the beams at depth (hot). A gap that is too large leaves a cold strip. Dropping the 1/2 and using the full field length gives 2.96 cm, twice the divergence of each edge. Keeping only the larger of the two contributions gives 1.08 cm and leaves the other field's divergence unmatched. Inverting d/SSD into SSD/d gives 390.00 cm, which has the wrong units behavior and is far too large to be a skin gap.

### Q3
Stem: Bonus isocentric field. Calibration is 1.000 cGy/MU at dmax for a 10×10 cm field at SAD 100 cm. Isocentric setup, dose 210 cGy at isocenter. TMR at that depth and field is 0.765. Sc = 1.025, Sp = 1.018, wedge factor = 0.74, tray factor = 0.96, off-axis ratio = 1.02. MU = dose / (1.000 × TMR × Sc × Sp × wedge factor × tray factor × off-axis ratio). Do not put a PDD in this SAD formula. What MU is required, to the nearest 0.1 MU?
A. 268.7 MU
B. 378.8 MU
C. 121.5 MU
D. 363.1 MU
Answer: D
Objective: IV.3
Why: The calibration point is dmax for 10×10 at SAD 100 cm, so the 1.000 cGy/MU is already at isocenter distance and TMR carries the depth. Denominator = 1.000 × 0.765 × 1.025 × 1.018 × 0.74 × 0.96 × 1.02. Stepwise: 1 × 0.765 = 0.765; × 1.025 = 0.7841; × 1.018 = 0.7982; × 0.74 = 0.5907; × 0.96 = 0.5671; × 1.02 = 0.5784. MU = 210 / 0.5784 = 363.06, reported as 363.1 MU. Putting the PDD in this denominator would treat an SAD setup like an SSD percent-depth setup and double-count inverse square, because TMR is already the SAD depth ratio. Leaving the wedge factor out of the denominator gives 268.7 MU. Leaving Sc and Sp out gives 378.8 MU. Multiplying the dose by the factor product instead of dividing gives 121.5 MU.

### Q4
Stem: Bonus. New penumbra geometry. Source diameter s = 1.8 cm, SSD = 100 cm, depth d = 8 cm, source-to-diaphragm distance SDD = 55 cm. Geometric penumbra P = s × (SSD + d − SDD) / SDD. What is P?
A. 1.73 cm
B. 1.47 cm
C. 3.53 cm
D. 0.96 cm
Answer: A
Objective: IV.3
Why: The source is not a point, so the diaphragm casts a partial shadow that grows as you move away from the diaphragm. Substitute 1.8 × (100 + 8 − 55) / 55 = 1.8 × (53) / 55 = 1.8 × 0.9636 = 1.7345 cm, reported as 1.73 cm. This geometric width is not the physical penumbra. Physical penumbra is the 80% to 20% dose distance, usually quoted at dmax. Dropping the depth and using (SSD-SDD), which is the surface penumbra gives 1.47 cm. Forgetting to subtract SDD inside the parentheses gives 3.53 cm. Forgetting to multiply by the source diameter gives 0.96 cm.

### Q5
Stem: Bonus. New timer pair. Two exposures give 50.25 cGy in 0.6 min and 140.25 cGy in 1.8 min. Timer error is extra effective on-time during transit, so true dose rate = (R2−R1)/(t2−t1) and timer error = R1/dose rate − t1. Set time = dose/dose rate − timer error. What timer setting delivers 150 cGy?
A. 2.00 min
B. 2.07 min
C. 1.72 min
D. 1.93 min
Answer: D
Objective: IV.3
Why: True dose rate = (140.25−50.25)/(1.8−0.6) = 90/1.2 = 75 cGy/min. Timer error = 50.25/75 − 0.6 = 0.6700 − 0.6 = 0.0700 min. Set time = 150/75 − 0.0700 = 2.0000 − 0.0700 = 1.9300 min, reported as 1.93 min. The positive timer error means the source delivered extra dose during motion, so the set time is shorter than dose/rate. Ignoring timer error and setting dose/rate gives 2.00 min, which overdoses by the transit contribution. Adding the timer error instead of subtracting it gives 2.07 min and overdoses further. Using R1/t1 = 50.25/0.6 = 83.7500 cGy/min as the dose rate folds the transit dose into the rate and then still subtracting tau gives 1.72 min.

### Q6
Stem: Bonus. New initial dose rate. A permanent I-125 implant has initial dose rate 9 cGy/h and half-life 59.4 days. Total dose to complete decay = dose rate × 1.443 × half-life, with the half-life converted to hours so the units match the dose rate. What is the total dose, to the nearest cGy?
A. 8891 cGy
B. 12830 cGy
C. 771 cGy
D. 18514 cGy
Answer: D
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 59.4 = 85.7142 days = 85.7142 × 24 = 2057.1408 hours. Total dose = 9 cGy/h × 2057.1408 h = 18514.3 cGy, reported as 18514 cGy. In one line: 9 × 1.443 × 59.4 × 24 = 18514.3. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 8891 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 12830 cGy. Forgetting to convert days to hours (omitting ×24) gives 771 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q7
Stem: Bonus. Cord retreat estimate with the stated α/β = 2 Gy. Prior course is 20 × 2 Gy. New course is 3 × 3 Gy. Prior course: 20 × 2 Gy. New course: 3 × 3 Gy. Use α/β = 2 Gy for both. What is the sum of the two EQD2 values?
A. 49.0 Gy
B. 102.5 Gy
C. 51.3 Gy
D. 11.3 Gy
Answer: C
Objective: III.3
Why: Course 1 physical = 20×2 = 40 Gy. BED1 = 40×(1+2/2) = 40×2.0000 = 80.00 Gy. EQD2_1 = 80.00/(1+2/2) = 80.00/2.0000 = 40.00 Gy. Course 2 physical = 3×3 = 9 Gy. BED2 = 9×(1+3/2) = 9×2.5000 = 22.50 Gy. EQD2_2 = 22.50/2.0000 = 11.25 Gy. Sum = 40.00 + 11.25 = 51.25 Gy, reported as 51.3 Gy. Adding physical doses only (40+9) gives 49.0 Gy. Adding BEDs and calling the sum an EQD2 gives 102.5 Gy. Reporting only the second course gives 11.3 Gy.

### Q8
Stem: Bonus. New activity and distance. Γ is given. The exposure-rate constant Γ is 4.69 R·cm²/(mCi·h). Activity is 1500 mCi. Distance is 40 cm. Exposure rate X = Γ A / d². What is X?
A. 175.88 R/h
B. 0.00 R/h
C. 1.10 R/h
D. 4.40 R/h
Answer: D
Objective: V.6
Why: Substitute 4.69 × 1500 / (40)^2 = 7035 / 1600 = 4.396875 R/h, reported as 4.40 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 175.88 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.00 R/h. Doubling the distance inside the square (a 2× distance error) gives 1.10 R/h.

## Phases of Clinical Trials

### Q1
Stem: A first-in-human study escalates dose to find toxicity. Which phase is that?
A. Phase III
B. Phase IV
C. Phase II
D. Phase I
Answer: D
Objective: III.2
Why: Phase I finds a safe dose and describes toxicity. Phase II looks for efficacy in a disease. Phase III randomizes against a standard. Phase IV watches the treatment after it is in routine use. Correct choice: Phase I. Phase III is a randomized comparison with a standard treatment. Phase IV is post-marketing observation. Phase II looks for a signal of activity after a dose has been chosen.

### Q2
Stem: A randomized trial compares a new fractionation with standard fractionation and is powered for overall survival. Which phase is that?
A. Phase I
B. Phase III
C. Phase II
D. Phase IV
Answer: B
Objective: III.2
Why: The definitive randomized comparison is phase III. Correct choice: Phase III. Phase I is dose finding, not a survival randomization against a standard. Phase II is typically a smaller activity study, not the definitive randomized comparison. Phase IV is after approval or adoption, not the pivotal comparison.

### Q3
Stem: A single-arm study in 40 patients looks for response rate after the phase I dose was chosen. Which phase is that?
A. Phase I
B. Phase III
C. Phase IV
D. Phase II
Answer: D
Objective: III.2
Why: Looking for a response signal at a defined dose is phase II. Correct choice: Phase II. The dose was already chosen. This study is looking for activity. There is no randomized control arm in the stem. The regimen is not being followed as post-market surveillance here.

### Q4
Stem: After a regimen is in wide use, a registry watches rare late toxicity. Which phase is that?
A. Phase I
B. Phase II
C. Phase III
D. Phase IV
Answer: D
Objective: III.2
Why: Post-marketing or post-adoption surveillance is phase IV. Correct choice: Phase IV. Phase I is pre-adoption dose finding. Phase II is not a post-market registry. Phase III would be a controlled comparison, not a surveillance registry.

### Q5
Stem: Which sequence is the usual order?
A. Phase III, then I, then IV, then II
B. Phase IV, then III, then II, then I
C. Phase I, then II, then III, then IV
D. Phase II, then I, then IV, then III
Answer: C
Objective: III.2
Why: The usual development order is safety (I), activity (II), randomized comparison (III), then surveillance (IV). Correct choice: Phase I, then II, then III, then IV. Dose finding does not follow the definitive randomized trial. That reverses the development path. Safety dose finding comes before the efficacy signal.

## Binary Number/Decimal Conversion

### Q1
Stem: Place-value drill. Convert the binary number 1101 to decimal. The rightmost bit is 1, then 2, 4, 8, and so on.
A. 11
B. 5
C. 13
D. 14
Answer: C
Objective: III.9
Why: Powers from the right: 8, 4, 2, 1 assigned to bits 1101. Add the places that are 1: 1 + 4 + 8 = 13. The decimal value is 13. Reading the bits from the wrong end gives 11. Dropping the highest bit gives 5. Adding one to the value, as in an off-by-one place count gives 14.

### Q2
Stem: Place-value drill. Convert the binary number 100101 to decimal. The rightmost bit is 1, then 2, 4, 8, and so on.
A. 41
B. 5
C. 37
D. 38
Answer: C
Objective: III.9
Why: Powers from the right: 32, 16, 8, 4, 2, 1 assigned to bits 100101. Add the places that are 1: 1 + 4 + 32 = 37. The decimal value is 37. Reading the bits from the wrong end gives 41. Dropping the highest bit gives 5. Adding one to the value, as in an off-by-one place count gives 38.

### Q3
Stem: Encode a decimal field size index. Write the positive integer 45 in binary (no leading zeros).
A. 101101
B. 101100
C. 110101
D. 101110
Answer: A
Objective: III.9
Why: Find the largest power of 2 not above 45. Subtract powers that fit: 32 + 8 + 4 + 1 = 45. Those places are 1 and the skipped powers are 0, so the bits are 101101. Encoding 44 instead of 45 gives 101100. Shifting the value by a couple of counts gives 110101. Encoding 46 gives 101110.

### Q4
Stem: Encode 18. Write the positive integer 18 in binary (no leading zeros).
A. 01001
B. 10001
C. 10010
D. 10100
Answer: C
Objective: III.9
Why: Find the largest power of 2 not above 18. Subtract powers that fit: 16 + 2 = 18. Those places are 1 and the skipped powers are 0, so the bits are 10010. Reversing the bits gives 01001. Encoding 17 instead of 18 gives 10001. Shifting the value by a couple of counts gives 10100.

### Q5
Stem: A full byte. Convert the binary number 11111111 to decimal. The rightmost bit is 1, then 2, 4, 8, and so on.
A. 127
B. 255
C. 256
D. 254
Answer: B
Objective: III.9
Why: Powers from the right: 128, 64, 32, 16, 8, 4, 2, 1 assigned to bits 11111111. Add the places that are 1: 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 = 255. The decimal value is 255. Dropping the highest bit gives 127. Adding one to the value, as in an off-by-one place count gives 256. Subtracting one from the decoded value gives 254.

## Radiation Therapy Concepts Quiz

### Q1
Stem: Concepts quiz. Binary review. Convert the binary number 10110 to decimal. The rightmost bit is 1, then 2, 4, 8, and so on.
A. 13
B. 22
C. 6
D. 23
Answer: B
Objective: III.9
Why: Powers from the right: 16, 8, 4, 2, 1 assigned to bits 10110. Add the places that are 1: 2 + 4 + 16 = 22. The decimal value is 22. Reading the bits from the wrong end gives 13. Dropping the highest bit gives 6. Adding one to the value, as in an off-by-one place count gives 23.

### Q2
Stem: Concepts quiz. Write the positive integer 13 in binary (no leading zeros).
A. 1011
B. 1100
C. 1101
D. 1111
Answer: C
Objective: III.9
Why: Find the largest power of 2 not above 13. Subtract powers that fit: 8 + 4 + 1 = 13. Those places are 1 and the skipped powers are 0, so the bits are 1101. Reversing the bits gives 1011. Encoding 12 instead of 13 gives 1100. Shifting the value by a couple of counts gives 1111.

### Q3
Stem: Concepts quiz. 15 fractions of 3 Gy, α/β = 10 Gy. Report EQD2. A course is 15 fractions of 3 Gy. Use α/β = 10 Gy. EQD2 = BED / (1 + 2/(α/β)), with BED = n×d×(1 + d/(α/β)). What is the EQD2?
A. 48.8 Gy
B. 58.5 Gy
C. 45.0 Gy
D. 54.0 Gy
Answer: A
Objective: III.3
Why: Physical dose = 15 × 3 = 45 Gy. BED = 45 × (1 + 3/10) = 45 × 1.3000 = 58.50 Gy. The 2 Gy denominator factor is 1 + 2/10 = 1.2000. EQD2 = 58.50 / 1.2000 = 48.75 Gy, reported as 48.8 Gy. If the fraction size is already 2 Gy, EQD2 equals the physical dose for any α/β. Here the fraction size is 3 Gy, so that shortcut applies only when d = 2. Stopping at the BED and not dividing by (1+2/(α/β)) gives 58.5 Gy. Reporting only the physical dose gives 45.0 Gy. Using α/β = 3 Gy instead of 10 Gy gives 54.0 Gy.

### Q4
Stem: Concepts quiz. Inverse square only. The value is 64.0 cGy/min at 100 cm from the source. What is it at 200 cm if only inverse square changes?
A. 32.0 cGy/min
B. 256.0 cGy/min
C. 64.0 cGy/min
D. 16.0 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 64.0 × (100/200)^2 = 64.0 × (0.5000)^2 = 64.0 × 0.2500 = 16.0 cGy/min. Dropping the square and multiplying by the bare ratio 100/200 gives 32.0 cGy/min. Inverting the distances, (200/100)^2, gives 256.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (100 cm) as if it were the source distance gives 64.0 cGy/min, which is not a point on the beam axis from the source.

### Q5
Stem: Concepts quiz. Stated wR. Absorbed dose is 5 mGy from alpha particles. The problem states wR = 20. Dose equivalent H = wR × absorbed dose. Do not apply a tissue weighting factor; that would make effective dose, which is not asked. What is H?
A. 100.0 mSv
B. 5.0 mSv
C. 0.3 mSv
D. 25.0 mSv
Answer: A
Objective: VI.1
Why: Substitute H = 20 × 5 mGy = 100 mSv, reported as 100.0 mSv. With wR stated, you do not replace it by 1 unless the radiation actually has wR = 1 (photons and electrons). Reporting the absorbed dose unchanged gives 5.0 mSv and drops wR. Dividing by wR gives 0.3 mSv. Adding wR to the absorbed dose gives 25.0 mSv.

### Q6
Stem: Concepts quiz. Water-equivalent path. Path: 3 cm at relative density 1, 4 cm at relative density 0.25, 3 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 10.00 cm
B. 7.00 cm
C. 22.00 cm
D. 1.00 cm
Answer: B
Objective: IV.4
Why: Substitute 3×1 + 4×0.25 + 3×1 = 3.00 + 1.00 + 3.00 = 7.00 cm, reported as 7.00 cm. The physical depth is 10.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 10.00 cm. Dividing thickness by density instead of multiplying gives 22.00 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 1.00 cm.

### Q7
Stem: Which phase randomizes a new treatment against the standard of care?
A. Phase I
B. Phase II
C. Phase IV
D. Phase III
Answer: D
Objective: III.2
Why: Randomized comparison to standard care is phase III. Correct choice: Phase III. Phase I is toxicity and dose. Phase II is an activity signal. Phase IV is surveillance after adoption.

### Q8
Stem: A small photon field crosses a lung interface. Which algorithm is the weakest of these choices?
A. Pencil beam
B. Monte Carlo
C. Linear Boltzmann solver
D. Convolution/superposition
Answer: A
Objective: IV.1
Why: Pencil beam is the weak interface algorithm. Correct choice: Pencil beam. Monte Carlo is a strong choice here. A Boltzmann solver transports the interface. Superposition beats a pencil beam at this interface, even though it is not perfect.
