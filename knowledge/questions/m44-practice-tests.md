# Module 44. Practice Test

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## The Format

### Q1
Stem: How long is the CMD exam window for the sitting described in the public handbook summary used here?
A. 3 hours 50 minutes
B. 2 hours
C. 3 hours
D. 5 hours
Answer: A
Objective: III.1
Why: The public exam description used for this bank gives 3 hours 50 minutes for 155 questions, in English, based on U.S. practice. Correct choice: 3 hours 50 minutes. Two hours would be a shorter licensing exam than this one. The published time is 3 hours 50 minutes, not a flat 3 hours. Five hours is longer than the published sitting.

### Q2
Stem: How many questions are in that sitting, with a few unscored pilot items mixed in?
A. 100
B. 155
C. 140
D. 200
Answer: B
Objective: III.1
Why: The sitting is 155 questions. A few of them are unscored pilots mixed into the form, and some items are performance-based in ProKnow rather than ordinary multiple choice. Correct choice: 155. 100 understates the published length. 140 is close and still short of 155. 200 overstates the published length.

### Q3
Stem: Which domain carries the largest share of the 2023 blueprint?
A. Radiation physics, about 14%
B. Dose calculation, about 13%
C. Quality assurance, about 9%
D. Treatment planning, about 42%
Answer: D
Objective: III.1
Why: Treatment planning is about 42%. Physics is about 14%, dose calculation about 13%, protection and QA about 9% each, localization about 8%, and brachytherapy about 5%. Correct choice: Treatment planning, about 42%. Physics is 14%, a real domain and not the largest. Dose calculation is 13%. QA is 9%, tied in weight with radiation protection.

### Q4
Stem: Which statement matches the language and practice setting of the exam?
A. Any language, with SI units forbidden
B. English, based only on non-U.S. fractionation customs
C. English only, and the items assume U.S. practice
D. An oral exam in the candidate's choice of language
Answer: C
Objective: III.1
Why: The exam is given in English and is written for U.S. practice. Correct choice: English only, and the items assume U.S. practice. The exam is English. SI units are used throughout dosimetry. The handbook frames the exam as U.S. practice. This is not an oral exam.

### Q5
Stem: Besides ordinary multiple-choice items, the blueprint includes which performance tasks?
A. ProKnow plan evaluation, isodose, DVH, anatomy, beam arrangement, and contouring
B. A water-tank lab practical as the entire exam
C. An oral defense of a thesis
D. A take-home MU homework set
Answer: A
Objective: III.1
Why: A portion of the exam is performance-based: plan evaluation, isodose display, DVH, anatomy, beam arrangement, and contouring. Correct choice: ProKnow plan evaluation, isodose, DVH, anatomy, beam arrangement, and contouring. Measurement practicals are not the scored performance section described here. There is no oral thesis defense. The performance items are in the sitting, using ProKnow-style plan review.

## Practice Exam 1

### Q1
Stem: Practice exam 1. HDR source decay before a fraction. Activity at calibration was 11.5 Ci. Elapsed time is 18 days. Half-life is 73.8 days. Remaining activity = A0 × (1/2)^(t/T½). What activity remains?
A. 8.70 Ci
B. 9.71 Ci
C. 5.75 Ci
D. 10.23 Ci
Answer: B
Objective: I.7
Why: Number of half-lives = 18/73.8 = 0.2439. Fraction remaining = (1/2)^(0.2439) = 0.8445. Activity = 11.5 × 0.8445 = 9.7113 Ci, reported as 9.71 Ci. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.2439) = 0.8445. A linear model A0×(1−t/T½) gives 8.70 Ci and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 5.75 Ci. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 10.23 Ci. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q2
Stem: Practice exam 1. Magnification on a verification film. Source-to-film distance is 150 cm and source-to-object distance is 90 cm. The image of the marker measures 7.5 cm. Magnification = source-to-film / source-to-object. What is the true object size?
A. 12.50 cm
B. 7.50 cm
C. 3.00 cm
D. 4.50 cm
Answer: D
Objective: I.6
Why: Magnification = 150/90 = 1.6667. Object = image / magnification = 7.5 / 1.6667 = 4.5000 cm, reported as 4.50 cm. The same arithmetic is 7.5 × 90 / 150 = 4.5000 cm. Multiplying the image by the magnification, instead of dividing, gives 12.50 cm and makes the object larger than its image. Reporting the image size unchanged gives 7.50 cm. Using (SFD−SOD)/SFD as the magnification gives 3.00 cm.

### Q3
Stem: Practice exam 1. Narrow-beam shield, exactly two HVL. The incident dose on a shield is 400 cGy. The shield is exactly 2 HVL thick. Narrow-beam transmission is (1/2)^(number of HVL). What dose is transmitted?
A. 200.0 cGy
B. 50.0 cGy
C. 100.0 cGy
D. 54.1 cGy
Answer: C
Objective: I.10
Why: Each HVL cuts the narrow-beam intensity in half. Transmission = (1/2)^2 = 0.2500. Transmitted dose = 400 × 0.2500 = 100.00 cGy, reported as 100.0 cGy. Two HVL specifically transmit 1/4 (25%), not 1/2. Stopping at one HVL (transmission 1/2) gives 200.0 cGy. Using three HVL (transmission 1/8) regardless of the stated thickness gives 50.0 cGy. Using e^(-n) as if mu were 1 per HVL, instead of (1/2)^n gives 54.1 cGy.

### Q4
Stem: Practice exam 1. Move a cobalt measurement from 80 cm to 100 cm. The value is 240.0 cGy/min at 80 cm from the source. What is it at 100 cm if only inverse square changes?
A. 153.6 cGy/min
B. 192.0 cGy/min
C. 375.0 cGy/min
D. 3840.0 cGy/min
Answer: A
Objective: I.10
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 240.0 × (80/100)^2 = 240.0 × (0.8000)^2 = 240.0 × 0.6400 = 153.6 cGy/min. Dropping the square and multiplying by the bare ratio 80/100 gives 192.0 cGy/min. Inverting the distances, (100/80)^2, gives 375.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (20 cm) as if it were the source distance gives 3840.0 cGy/min, which is not a point on the beam axis from the source.

### Q5
Stem: Practice exam 1. A 9 MeV electron beam loses about 2 MeV per cm in water. At what depth has the mean energy fallen to 5 MeV?
A. 4.5 cm
B. 2.0 cm
C. 3.0 cm
D. 4.0 cm
Answer: B
Objective: I.3
Why: Energy lost = 9 − 5 = 4 MeV. Depth = 4 / 2 = 2.00 cm, reported as 2.0 cm. This is not the practical range, which is about E/2 = 4.5 cm, and not the 80% depth, which is about E/3 = 3.0 cm. E/2 = 4.5 cm is the practical-range rule of thumb, not the depth where the energy has fallen only to 5 MeV. E/3 = 3.0 cm is the usual 80% isodose depth, a different question. Subtracting the energies and forgetting to divide by 2 MeV/cm gives 4.0 cm.

### Q6
Stem: In soft tissue at megavoltage energy, which interaction dominates dose deposition from the photon beam?
A. Compton scatter
B. Photoelectric absorption, as in a diagnostic kV image
C. Pair production as the only MV process
D. Coherent scatter depositing the prescription dose
Answer: A
Objective: I.4
Why: At megavoltage energies in soft tissue, Compton scatter is the dominant interaction. Photoelectric effect matters at kilovoltage and in high-Z material. Correct choice: Compton scatter. Photoelectric effect dominates diagnostic contrast in bone and contrast, not MV tissue dose. Pair production grows at higher energy and is not the main process in tissue at ordinary treatment energies. Coherent scatter does not deposit the therapeutic dose.

### Q7
Stem: Practice exam 1. Isocentric MU. Calibration is 1.000 cGy/MU at dmax for a 10×10 cm field at SAD 100 cm. Isocentric setup, dose 190 cGy at isocenter. TMR at that depth and field is 0.77. Sc = 1.018, Sp = 1.006, wedge factor = 0.69, tray factor = 1, off-axis ratio = 1. MU = dose / (1.000 × TMR × Sc × Sp × wedge factor × tray factor × off-axis ratio). Do not put a PDD in this SAD formula. What MU is required, to the nearest 0.1 MU?
A. 349.2 MU
B. 240.9 MU
C. 357.6 MU
D. 103.4 MU
Answer: A
Objective: IV.3
Why: The calibration point is dmax for 10×10 at SAD 100 cm, so the 1.000 cGy/MU is already at isocenter distance and TMR carries the depth. Denominator = 1.000 × 0.77 × 1.018 × 1.006 × 0.69 × 1 × 1. Stepwise: 1 × 0.77 = 0.77; × 1.018 = 0.7839; × 1.006 = 0.7886; × 0.69 = 0.5441; × 1 = 0.5441; × 1 = 0.5441. MU = 190 / 0.5441 = 349.20, reported as 349.2 MU. Putting the PDD in this denominator would treat an SAD setup like an SSD percent-depth setup and double-count inverse square, because TMR is already the SAD depth ratio. Leaving the wedge factor out of the denominator gives 240.9 MU. Leaving Sc and Sp out gives 357.6 MU. Multiplying the dose by the factor product instead of dividing gives 103.4 MU.

### Q8
Stem: Practice exam 1. SSD change for a 6 MV PDD. PDD at 14 cm depth is 60.5% for SSD 100 cm. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 118 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 83.9 %
B. 62.5 %
C. 61.5 %
D. 58.5 %
Answer: B
Objective: IV.3
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(118+1.5)/(100+1.5)]^2 × [(100+14)/(118+14)]^2 = (1.1773)^2 × (0.8636)^2 = 1.3861 × 0.7459 = 1.0339. PDD2 = 60.5 × 1.0339 = 62.55%, which rounds to 62.5 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 83.9 %. Multiplying the two distance ratios once each, without squaring, gives 61.5 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 58.5 %.

### Q9
Stem: Practice exam 1. Abut two SSD fields at depth. Field 1 length at SSD is 26 cm with SSD 100 cm. Field 2 length at SSD is 18 cm with SSD 100 cm. The fields should abut at 9 cm depth. Skin gap = (L1/2)×(d/SSD1) + (L2/2)×(d/SSD2). What is the skin gap?
A. 1.98 cm
B. 3.96 cm
C. 1.17 cm
D. 244.44 cm
Answer: A
Objective: IV.3
Why: Each term is how far that field's edge diverges from its central axis over depth d. Field 1: (26/2) × (9/100) = 13 × 0.0900 = 1.1700 cm. Field 2: (18/2) × (9/100) = 9 × 0.0900 = 0.8100 cm. Gap = 1.1700 + 0.8100 = 1.9800 cm, reported as 1.98 cm. A gap that is too small overlaps the beams at depth (hot). A gap that is too large leaves a cold strip. Dropping the 1/2 and using the full field length gives 3.96 cm, twice the divergence of each edge. Keeping only the larger of the two contributions gives 1.17 cm and leaves the other field's divergence unmatched. Inverting d/SSD into SSD/d gives 244.44 cm, which has the wrong units behavior and is far too large to be a skin gap.

### Q10
Stem: Practice exam 1. Rectangle for a TMR lookup. Use Sterling's formula, equivalent square = 2ab/(a+b), which is the same as 4 × area / perimeter. What is the equivalent square of a 11 × 15 cm rectangular field?
A. 13.00 cm
B. 12.69 cm
C. 12.85 cm
D. 25.38 cm
Answer: B
Objective: IV.3
Why: Substitute 2 × 11 × 15 / (11+15) = 330 / 26 = 12.6923 cm, reported as 12.69 cm. The perimeter form gives the same result: 4 × 11 × 15 / [2 × (11+15)] = 660 / 52 = 12.6923 cm. The arithmetic mean (11+15)/2 = 13.00 cm is not the scatter-equivalent square. The geometric mean √(11×15) = 12.85 cm is a different average and is not Sterling's formula. Using 4ab/(a+b) forgets that the perimeter is 2(a+b), so it is twice the equivalent square and gives 25.38 cm.

### Q11
Stem: Practice exam 1. The wedge stayed in the beam. The monitor units were calculated for an open beam to deliver 210 cGy at the calculation point. A wedge with wedge factor 0.66 was actually left in the beam. What dose is delivered at that point?
A. 210.0 cGy
B. 318.2 cGy
C. 138.6 cGy
D. 71.4 cGy
Answer: C
Objective: IV.2
Why: The open-beam MU already assume wedge factor 1. With the wedge in the beam every MU is attenuated by the wedge factor, so delivered dose = intended dose × wedge factor. Substitute 210 × 0.66 = 138.60 cGy, reported as 138.6 cGy. The plan underdoses; it does not overdose. Leaving the dose at 210.0 cGy is the open-beam number and ignores the wedge that was in the beam. Dividing by the wedge factor (210/0.66 = 318.2 cGy) is what you do to the MU to restore dose, not what the patient received from the uncorrected MU. Multiplying by (1−wedge factor) treats the factor as if only the attenuated fraction remained in a subtraction sense and gives 71.4 cGy.

### Q12
Stem: Practice exam 1. Permanent implant, dose rate in cGy/h. A permanent Pd-103 implant has initial dose rate 11 cGy/h and half-life 17 days. Total dose to complete decay = dose rate × 1.443 × half-life, with the half-life converted to hours so the units match the dose rate. What is the total dose, to the nearest cGy?
A. 3110 cGy
B. 4488 cGy
C. 270 cGy
D. 6476 cGy
Answer: D
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 17 = 24.5310 days = 24.5310 × 24 = 588.7440 hours. Total dose = 11 cGy/h × 588.7440 h = 6476.2 cGy, reported as 6476 cGy. In one line: 11 × 1.443 × 17 × 24 = 6476.2. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 3110 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 4488 cGy. Forgetting to convert days to hours (omitting ×24) gives 270 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q13
Stem: Practice exam 1. Exposure rate. Activity is in mCi and Γ is given. The exposure-rate constant Γ is 4.69 R·cm²/(mCi·h). Activity is 6000 mCi. Distance is 80 cm. Exposure rate X = Γ A / d². What is X?
A. 351.75 R/h
B. 4.40 R/h
C. 0.00 R/h
D. 1.10 R/h
Answer: B
Objective: V.6
Why: Substitute 4.69 × 6000 / (80)^2 = 28140 / 6400 = 4.396875 R/h, reported as 4.40 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 351.75 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.00 R/h. Doubling the distance inside the square (a 2× distance error) gives 1.10 R/h.

### Q14
Stem: An occupational effective dose of 22 mSv has already been recorded this year. How much of the 50 mSv NCRP 116 annual limit remains?
A. 50 mSv
B. 22 mSv
C. 28 mSv
D. 72 mSv
Answer: C
Objective: VI.1
Why: Remaining = 50 − 22 = 28 mSv. The cumulative guidance of 10 mSv × age is a second check, not a replacement for the annual 50 mSv. Correct choice: 28 mSv. 50 mSv ignores the 22 mSv already recorded. 22 mSv is the dose already received, not the remainder. Adding 22 to 50 goes the wrong direction.

### Q15
Stem: NCRP 116 cumulative effective-dose guidance at age 52 is which value?
A. 52 mSv
B. 50 mSv
C. 1040 mSv
D. 520 mSv
Answer: D
Objective: VI.1
Why: 10 × 52 = 520 mSv. Correct choice: 520 mSv. That omits the factor of 10. 50 mSv is the annual cap. That doubles 10 × age.

### Q16
Stem: Practice exam 1. wR is stated. Absorbed dose is 1.5 mGy from alpha particles. The problem states wR = 20. Dose equivalent H = wR × absorbed dose. Do not apply a tissue weighting factor; that would make effective dose, which is not asked. What is H?
A. 1.5 mSv
B. 0.1 mSv
C. 30.0 mSv
D. 21.5 mSv
Answer: C
Objective: VI.1
Why: Substitute H = 20 × 1.5 mGy = 30 mSv, reported as 30.0 mSv. With wR stated, you do not replace it by 1 unless the radiation actually has wR = 1 (photons and electrons). Reporting the absorbed dose unchanged gives 1.5 mSv and drops wR. Dividing by wR gives 0.1 mSv. Adding wR to the absorbed dose gives 21.5 mSv.

### Q17
Stem: Practice exam 1. A barrier must transmit 10^−3. The required transmission is 10^−3. How many tenth-value layers is that? Each TVL multiplies transmission by 0.1.
A. 10.0 HVL
B. 3 TVL
C. 6 TVL
D. 1 TVL
Answer: B
Objective: VI.3
Why: Transmission = 10^(−3) = (0.1)^3, so the TVL count n = 3. That is 3 TVL. One TVL is about 3.32 HVL because log10(2) = 0.3010 and 1/0.3010 = 3.32, so 3 TVL is about 9.97 HVL, but the question asks for TVL. Converting to HVL (dividing the exponent by log10(2)) gives about 10.0 HVL, which is the companion count, not the TVL count. Doubling the exponent gives 6 TVL. 1 TVL would be transmission 0.1 only when one TVL is required.

### Q18
Stem: Practice exam 1. Morning linac output versus 1.000 cGy/MU. TG-142 daily tolerance is 3% and monthly is 2%. Expected output is 1 cGy/MU and the measurement is 1.028 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -2.8%
B. 2.8%
C. 2.7%
D. 102.8%
Answer: B
Objective: VII.1
Why: Substitute (1.028 − 1) / 1 × 100 = 0.028 / 1 × 100 = 2.80%, reported as 2.8%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -2.8%. Dividing the difference by the measurement instead of the expected value gives 2.7%. Reporting the ratio as a percent (100 × measured/expected) gives 102.8%, which is not the deviation.

### Q19
Stem: An IMRT QA gamma score is 93% using 3%/2 mm and a 10% threshold. How does TG-218 classify it?
A. A pass of the 95% tolerance
B. Under the 95% tolerance and over the 90% action limit
C. Under the 90% action limit
D. Unusable because 93% has no meaning
Answer: B
Objective: VII.5
Why: TG-218 universal tolerance is 95% and the action limit is 90%. 93% fails tolerance and has not reached the action limit. Correct choice: Under the 95% tolerance and over the 90% action limit. 93 is less than 95. 93 is still above 90. The two thresholds are exactly how you read 93%.

### Q20
Stem: How often is a physics chart check of a multi-fraction course customarily done?
A. Weekly
B. Only on the last day
C. Every 30 minutes during the beam
D. Once per year with TG-51
Answer: A
Objective: VII.2
Why: A weekly physics chart check reviews cumulative dose, fractions, images, and continued agreement with the approved plan. Daily machine QA is a separate TG-142 cadence. Correct choice: Weekly. Waiting until the end misses a course that drifted in week one. That is not the chart-check cadence. Annual calibration is a machine test, not the chart check.

### Q21
Stem: What is RO-ILS for?
A. Voluntary learning from radiation-oncology incidents and near misses
B. Issuing NRC fines
C. Replacing TG-51
D. Setting the QUANTEC cord number
Answer: A
Objective: VII.7
Why: RO-ILS is a voluntary incident-learning system associated with ASTRO and AAPM. The point is process learning, including near misses. Correct choice: Voluntary learning from radiation-oncology incidents and near misses. RO-ILS is not an enforcement agency. Calibration is a different activity. QUANTEC is a published dose-volume review, not an incident system.

### Q22
Stem: From the tattoos, the plan says move the patient 1.5 cm anterior and then another 0.5 cm anterior. What is the total anterior shift?
A. 1.0 cm anterior
B. 0.5 cm anterior
C. 2.0 cm anterior
D. 2.0 cm posterior
Answer: C
Objective: II.7
Why: Both shifts are anterior, so 1.5 + 0.5 = 2.0 cm anterior. Reversing anterior and posterior is a common setup error and is not what the plan asked. Correct choice: 2.0 cm anterior. 1.5 − 0.5 = 1.0 cm subtracts a shift that was supposed to be added. That keeps only the second shift. The direction was anterior both times. Reversing it is the classic shift error.

### Q23
Stem: A patient has lost weight and the external contour no longer matches the planning CT. Rigid bone registration looks acceptable. What is the cautious next step?
A. Add the DVHs numerically with no registration
B. Assume the rigid bone match proves the skin dose
C. Turn off heterogeneity so the weight loss disappears
D. Inspect the deformed anatomy before trusting a dose sum
Answer: D
Objective: II.5
Why: Weight loss breaks the assumption that the planning CT and today's CT are the same shape. A deformable map is an estimate and has to be looked at, especially at the surface and in soft tissue. Correct choice: Inspect the deformed anatomy before trusting a dose sum. Adding DVH bins does not put dose on the same tissue. Bone can match while the surface and targets have moved. Heterogeneity is not the registration.

### Q24
Stem: Conventional fractionation, full cord cross-section, Dmax 47 Gy. Which reading matches the cord correlate used here?
A. 47 Gy exceeds 50 Gy
B. The cord correlate is lung V20 ≤ 30%
C. 47 Gy is 3 Gy below the 50 Gy cord correlate
D. The parotid mean of 20 Gy is the cord limit
Answer: C
Objective: III.8
Why: The cord correlate is 50 Gy. Margin under that value = 50 − 47 = 3 Gy. 47 is not above 50. Lung V20 ≤ 30% and a parotid mean under 20 Gy are different organs.

### Q25
Stem: Combined-lung V20 is 28% on a conventional plan. Which statement fits the lung correlate used here?
A. V20 is 2 percentage points under the ≤30% row
B. V20 fails because the limit is 20%
C. The lung row is V30 ≤ 30%
D. 28% exceeds 30%
Answer: A
Objective: III.8
Why: The lung correlate is V20 ≤ 30%. Room under the row = 30 − 28 = 2 percentage points. The row is not 20%, and it is not V30. 28 is less than 30, so the plan is not over the row.

### Q26
Stem: Equal-volume parotid means are 22 Gy and 28 Gy. What is the combined mean?
A. 50 Gy
B. 25 Gy
C. 22 Gy
D. 28 Gy
Answer: B
Objective: III.8
Why: (22 + 28) / 2 = 50 / 2 = 25 Gy. The bilateral correlate is a combined mean under 25 Gy, so 25 Gy does not meet “under 25.” Neither gland is under 20 Gy, so the single-gland spare is missed too. 50 Gy is the sum, not the mean. 22 Gy is only the cooler gland. 28 Gy is only the hotter gland.

### Q27
Stem: Rectum, conventional prostate plan: V50=44%, V60=38%, V65=20%, V70=16%, V75=10%. What fails in the QUANTEC set?
A. Nothing. Every volume is under its value
B. V75, because 10% exceeds 15%
C. V60, because 38% is not under 35%
D. Only V70 has to pass
Answer: C
Objective: III.8
Why: The set is V50 < 50, V60 < 35, V65 < 25, V70 < 20, V75 < 15, read together. V60 = 38% exceeds 35% by 38 − 35 = 3 percentage points, so the set is not met. The others pass: 44 < 50, 20 < 25, 16 < 20, and 10 < 15. V75 at 10% is under 15%. One passing volume does not replace the whole set.

### Q28
Stem: Using Bentel's rule of thumb, the depth of the 80% electron isodose in cm is about E/3. For 12 MeV, what is that depth?
A. 4 cm
B. 6 cm
C. 3 cm
D. 12 cm
Answer: A
Objective: III.1
Why: Bentel's 80% depth ≈ 12 / 3 = 4 cm. Practical range ≈ 12 / 2 = 6 cm. Bentel's 90% depth ≈ 12 / 4 = 3 cm. Khan's 80% depth for the same beam is 12/2.8 ≈ 4.3 cm, not this item. Correct choice: 4 cm. 6 cm is E/2, the practical range. 3 cm is Bentel's 90% depth. 12 cm would be 1 cm per MeV, far beyond the electron range.

### Q29
Stem: Practice exam 1. Use the electron lead-shield rule of thumb, thickness in mm about equal to E/2 where E is in MeV. How much lead for a 16 MeV beam?
A. 16.0 mm
B. 5.3 mm
C. 8.0 mm
D. 32.0 mm
Answer: C
Objective: III.6
Why: Thickness ≈ 16 / 2 = 8.0 mm. Reported as 8.0 mm. Internal eye shields are a separate issue: they are limited to low electron energies because a higher-energy shield throws bremsstrahlung and backscatter into the eye. Using the energy in MeV as if it were already millimeters of lead gives 16.0 mm. E/3 is the 80% depth rule in centimeters, not the lead thickness in millimeters. That mistake gives 5.3 mm. Doubling the energy instead of halving it gives 32.0 mm.

### Q30
Stem: Practice exam 1. Retreat sum. Prior 23 × 2 Gy, new 5 × 3 Gy, α/β = 3 Gy. Prior course: 23 × 2 Gy. New course: 5 × 3 Gy. Use α/β = 3 Gy for both. What is the sum of the two EQD2 values?
A. 61.0 Gy
B. 64.0 Gy
C. 106.7 Gy
D. 18.0 Gy
Answer: B
Objective: III.3
Why: Course 1 physical = 23×2 = 46 Gy. BED1 = 46×(1+2/3) = 46×1.6667 = 76.67 Gy. EQD2_1 = 76.67/(1+2/3) = 76.67/1.6667 = 46.00 Gy. Course 2 physical = 5×3 = 15 Gy. BED2 = 15×(1+3/3) = 15×2.0000 = 30.00 Gy. EQD2_2 = 30.00/1.6667 = 18.00 Gy. Sum = 46.00 + 18.00 = 64.00 Gy, reported as 64.0 Gy. Adding physical doses only (46+15) gives 61.0 Gy. Adding BEDs and calling the sum an EQD2 gives 106.7 Gy. Reporting only the second course gives 18.0 Gy.

### Q31
Stem: Which volume includes the CTV plus a setup and internal margin?
A. GTV
B. CTV
C. The treated volume, defined as the GTV only
D. PTV
Answer: D
Objective: III.11
Why: ICRU: GTV is gross disease, CTV adds subclinical extension, and PTV adds the margin for setup and internal motion so the CTV receives the prescription. Correct choice: PTV. GTV is visible or palpable tumor, with no margin for microscopic disease and no setup margin. CTV adds microscopic disease to the GTV. It does not include setup uncertainty. The treated volume is the tissue actually receiving a stated dose. It is not the definition of the PTV.

### Q32
Stem: A breast plan has a hot streak of 112% in the lateral breast. Which technique is aimed at that hot spot?
A. Field-in-field
B. Opening the wedge heel over the hot spot
C. Increasing energy to 18 MV only to blur the hotspot without looking at it
D. Deleting the PTV
Answer: A
Objective: III.7
Why: Field-in-field adds a small segment that blocks the hot region for part of the MU so the 112% comes down without abandoning coverage. Correct choice: Field-in-field. More heel attenuation would be a different tool. The usual segment method for a localized hot spot is field-in-field. Energy changes depth dose everywhere. It is not the local hot-spot segment. Removing the target does not treat the patient.

### Q33
Stem: Compared with step-and-shoot IMRT, sliding-window delivery typically does what?
A. Turns the beam off between every static segment
B. Keeps the beam on while leaves move, and usually uses more MU
C. Uses a binary MLC and a continuously rotating gantry like helical tomotherapy
D. Eliminates the need for IMRT QA
Answer: B
Objective: III.5
Why: Step-and-shoot stops the beam between segments. Sliding window delivers while the leaves move and generally spends more MU. Helical tomotherapy is a different machine: binary leaves, continuous rotation, and a longer delivery. Correct choice: Keeps the beam on while leaves move, and usually uses more MU. That is step-and-shoot. That is tomotherapy, not a C-arm sliding window. More MU and moving leaves do not cancel QA.

### Q34
Stem: A pacemaker is in the field of a planned 18 MV beam. What is the relevant concern from TG-203 style guidance?
A. Neutrons from the high-energy beam, and the device should not be treated as ordinary tissue
B. Neutrons are produced only below 6 MV
C. The device can be overwritten to water and ignored
D. Mayneord F accounts for the pacemaker
Answer: A
Objective: III.13
Why: High-energy photons produce neutrons. Pacemakers and similar implants need the dose kept low, beams kept off the device when possible, and cardiology involved. Do not invent a single gray limit the report does not state as universal. Correct choice: Neutrons from the high-energy beam, and the device should not be treated as ordinary tissue. Photoneutrons become relevant at high energy, above about 10 MV, not at 6 MV. A density override does not remove neutron or dose risk to the generator. Mayneord F changes SSD. It does not model a device.

### Q35
Stem: Why is the PTV margin for SBRT kept tight?
A. SBRT beams have no penumbra
B. QUANTEC lung V20 does not apply to any thorax plan
C. The dose falls off quickly, so a large margin irradiates a shell of normal tissue to a high dose
D. A tight margin lets you skip IGRT
Answer: C
Objective: III.6
Why: Stereotactic dose falls off over millimeters. Expanding the PTV pushes that high-dose shell into normal tissue. The margin stays tight and the setup has to match it. Correct choice: The dose falls off quickly, so a large margin irradiates a shell of normal tissue to a high dose. There is still a penumbra. The falloff is steep, which is why the margin cannot be casual. The SBRT margin question is about falloff. Conventional QUANTEC lung rows were not built as SBRT constraints. A tight margin is the reason IGRT has to be good, not a reason to skip it.

### Q36
Stem: What do you expect at a photon-electron junction?
A. A perfectly uniform 100% match if the light fields abut
B. Both hot and cold spots
C. Only a cold spot, never a hot spot
D. The electron practical range cancels the photon penumbra
Answer: B
Objective: III.1
Why: Photon and electron penumbras bow in different directions, so a junction that looks matched on the skin can be hot and cold nearby. Correct choice: Both hot and cold spots. Light-field abutment does not match the different penumbras and bulges. The junction can be hot on one side of the match and cold on the other. Range and penumbra are different shapes. They do not cancel by hope.

### Q37
Stem: Practice exam 1. Opposed beams. Two beams are weighted 2:1 and together deliver 180 cGy at the specification point. How many cGy does the beam with weight 2 contribute?
A. 90 cGy
B. 180 cGy
C. 60 cGy
D. 120 cGy
Answer: D
Objective: III.7
Why: The weight fraction is 2/(2+1) = 0.6667. Contribution = 180 × 0.6667 = 120.00 cGy, reported as 120 cGy. Splitting the dose in half ignores the 2:1 weights and gives 90 cGy. Giving the whole dose to the heavier beam gives 180 cGy. Assigning the lighter weight to the beam that was asked about gives 60 cGy.

### Q38
Stem: A cumulative DVH shows a 2 cc volume at 70 Gy inside the PTV. What can that curve not tell you?
A. That 2 cc receives at least 70 Gy
B. The volume of the structure
C. Where in the patient those 2 cc sit
D. That a dose was computed
Answer: C
Objective: III.1
Why: A DVH collapses location. It cannot show whether the 70 Gy is in the center of the PTV or on a contouring error, and it cannot prove the dose grid was fine enough. Correct choice: Where in the patient those 2 cc sit. That is what the cumulative DVH does say. The DVH is normalized to a volume, or it states absolute cc. A DVH implies a dose distribution was sampled.

### Q39
Stem: Which format is the transfer standard for CT images and RT plan objects?
A. DICOM
B. A screenshot pasted into the EMR
C. A verbal isocenter
D. HL7 as the image-pixel standard
Answer: A
Objective: III.9
Why: DICOM is how CT slices, structures, plans, and dose move between the scanner, the TPS, and the record-and-verify system. Correct choice: DICOM. A picture is not an RT plan object. Coordinates have to travel with the data set. HL7 carries clinical messages. Images and RT objects use DICOM.

### Q40
Stem: Two electron fields abut on the skin. Where is the classic cold region from loss of equilibrium at the edges?
A. Only at dmax of a single open photon field
B. At the surface junction
C. Nowhere, if the energies match
D. Inside the lead shield only
Answer: B
Objective: III.1
Why: Adjacent electron fields lose side-scatter at the common edge, so the surface junction runs cold unless you feather or overlap them on purpose. Correct choice: At the surface junction. This is an electron-electron match, not a photon dmax question. Matching energies does not restore side-scatter at the shared edge. The cold spot is in tissue at the junction, not inside the shield.

### Answer key

| Item | Answer | Objective |
| --- | --- | --- |
| Q1 | B | I.7 |
| Q2 | D | I.6 |
| Q3 | C | I.10 |
| Q4 | A | I.10 |
| Q5 | B | I.3 |
| Q6 | A | I.4 |
| Q7 | A | IV.3 |
| Q8 | B | IV.3 |
| Q9 | A | IV.3 |
| Q10 | B | IV.3 |
| Q11 | C | IV.2 |
| Q12 | D | V.6 |
| Q13 | B | V.6 |
| Q14 | C | VI.1 |
| Q15 | D | VI.1 |
| Q16 | C | VI.1 |
| Q17 | B | VI.3 |
| Q18 | B | VII.1 |
| Q19 | B | VII.5 |
| Q20 | A | VII.2 |
| Q21 | A | VII.7 |
| Q22 | C | II.7 |
| Q23 | D | II.5 |
| Q24 | C | III.8 |
| Q25 | A | III.8 |
| Q26 | B | III.8 |
| Q27 | C | III.8 |
| Q28 | A | III.1 |
| Q29 | C | III.6 |
| Q30 | B | III.3 |
| Q31 | D | III.11 |
| Q32 | A | III.7 |
| Q33 | B | III.5 |
| Q34 | A | III.13 |
| Q35 | C | III.6 |
| Q36 | B | III.1 |
| Q37 | D | III.7 |
| Q38 | C | III.1 |
| Q39 | A | III.9 |
| Q40 | B | III.1 |

## Practice Exam 2

### Q1
Stem: Practice exam 2. Survey reading, inverse square only. The value is 36.0 mR/h at 100 cm from the source. What is it at 160 cm if only inverse square changes?
A. 22.5 mR/h
B. 92.2 mR/h
C. 100.0 mR/h
D. 14.1 mR/h
Answer: D
Objective: I.10
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 36.0 × (100/160)^2 = 36.0 × (0.6250)^2 = 36.0 × 0.3906 = 14.1 mR/h. Dropping the square and multiplying by the bare ratio 100/160 gives 22.5 mR/h. Inverting the distances, (160/100)^2, gives 92.2 mR/h and would raise the reading when the detector moves out. Using the gap between the two distances (60 cm) as if it were the source distance gives 100.0 mR/h, which is not a point on the beam axis from the source.

### Q2
Stem: Practice exam 2. Narrow-beam transmission is 0.0625. A narrow beam is transmitted at a fraction 0.0625 of the incident intensity. How many HVL is that? Transmission = (1/2)^(number of HVL).
A. 16 HVL
B. 2.0 HVL
C. 4 HVL
D. 3.3 HVL
Answer: C
Objective: I.10
Why: (1/2)^n = 0.0625. n = ln(0.0625) / ln(1/2) = 4.0000, so n = 4 HVL. Check: 2^4 = 16, and 1/16 = 0.0625. Reporting the denominator of the transmission fraction as if it were the HVL count gives 16 HVL. Taking half of the true HVL count gives 2.0 HVL. 3.3 HVL confuses one TVL (about 3.3 HVL, transmission 0.1) with this HVL count.

### Q3
Stem: Practice exam 2. Object size from a magnified image. Source-to-film distance is 120 cm and source-to-object distance is 80 cm. The image of the marker measures 4.8 cm. Magnification = source-to-film / source-to-object. What is the true object size?
A. 3.20 cm
B. 7.20 cm
C. 4.80 cm
D. 1.60 cm
Answer: A
Objective: I.6
Why: Magnification = 120/80 = 1.5000. Object = image / magnification = 4.8 / 1.5000 = 3.2000 cm, reported as 3.20 cm. The same arithmetic is 4.8 × 80 / 120 = 3.2000 cm. Multiplying the image by the magnification, instead of dividing, gives 7.20 cm and makes the object larger than its image. Reporting the image size unchanged gives 4.80 cm. Using (SFD−SOD)/SFD as the magnification gives 1.60 cm.

### Q4
Stem: Practice exam 2. Proton prescription. The prescription is 55 Gy (RBE) and the proton RBE used for planning is 1.1. What physical dose does that prescription represent?
A. 50.0 Gy
B. 60.5 Gy
C. 55.0 Gy
D. 1.1 Gy
Answer: A
Objective: I.3
Why: Physical dose = RBE dose / RBE = 55 / 1.1 = 50.00 Gy, reported as 50.0 Gy. Clinical proton therapy energies are about 150–250 MeV, and the constant RBE used in this item is 1.1. Multiplying by RBE instead of dividing gives 60.5 Gy. Leaving the prescription number unchanged gives 55.0 Gy and treats RBE as 1. Reporting the RBE itself, with Gy attached, gives 1.1 Gy.

### Q5
Stem: Ir-192 decays mainly by which process, with gamma emission from the daughter?
A. Alpha decay only, with no photons
B. Spontaneous fission
C. Beta minus
D. Electron capture with no photons at all
Answer: C
Objective: I.1
Why: Ir-192 decays by beta minus (and a fraction of electron capture) to excited states that emit the gamma rays used for HDR. It is not an alpha emitter and not a fission source. Correct choice: Beta minus. Ir-192 is not an alpha source. The clinical emissions are betas and gammas. Fission is not the therapy decay mode of Ir-192. The useful emissions include gamma rays. Pure electron capture without photons is the wrong picture.

### Q6
Stem: Why does a kilovoltage image show bone and iodinated contrast more strongly than a megavoltage portal image?
A. Photoelectric absorption rises with Z at kilovoltage energies
B. Compton scatter is absent at kilovoltage
C. Pair production is the kV contrast mechanism
D. MV images stop in lead and kV images do not
Answer: A
Objective: I.8
Why: At diagnostic energies the photoelectric effect scales steeply with atomic number, so bone and iodine stand out. At megavoltage energies Compton scatter dominates and that Z contrast fades. Correct choice: Photoelectric absorption rises with Z at kilovoltage energies. Compton still occurs. The contrast comes from the photoelectric Z dependence. Pair production needs energies above 1.022 MeV. That is not why bone is bright on a CT or a kV radiograph.

### Q7
Stem: Practice exam 2. SSD tumor dose, find the given dose. Tumor dose at depth is 176 cGy and the PDD at that depth is 68.4%. What given dose (dose at dmax) is required? Given dose = tumor dose / (PDD/100).
A. 120.4 cGy
B. 257.3 cGy
C. 2.6 cGy
D. 244.4 cGy
Answer: B
Objective: IV.3
Why: Given dose is the dmax dose that produces the requested tumor dose after falloff. Substitute 176 / (68.4/100) = 176 / 0.6840 = 257.31 cGy, reported as 257.3 cGy. Equivalently 176 × 100 / 68.4 = 257.31 cGy. Multiplying by PDD/100 instead of dividing answers the reverse question (tumor dose if 176 cGy were already the given dose) and gives 120.4 cGy. Dividing by the percent number 68.4 instead of by the fraction 0.6840 gives 2.6 cGy. Adding the PDD number to the tumor dose, as if percent were cGy, gives 244.4 cGy.

### Q8
Stem: Practice exam 2. Straight-line interpolation only. A table lists TMR = 0.902 at 4 and TMR = 0.846 at 8. Linearly interpolate TMR at 5. No curve fit, just the straight fraction of the interval.
A. 0.888
B. 0.902
C. 0.874
D. 0.860
Answer: A
Objective: IV.3
Why: The point 5 is (5−4)/(8−4) = 0.2500 of the way from 4 to 8. The table changes by -0.056 over that whole step. Change on this step = 0.2500 × (-0.056) = -0.0140. TMR = 0.902 + (-0.0140) = 0.8880, reported as 0.888. Using the nearer table entry without interpolating gives 0.902. Averaging the endpoints as if the point were midway gives 0.874. Measuring the fraction from the wrong end of the interval gives 0.860.

### Q9
Stem: Practice exam 2. Geometric penumbra. Source diameter s = 1.6 cm, SSD = 85 cm, depth d = 12 cm, source-to-diaphragm distance SDD = 42 cm. Geometric penumbra P = s × (SSD + d − SDD) / SDD. What is P?
A. 1.64 cm
B. 3.70 cm
C. 1.31 cm
D. 2.10 cm
Answer: D
Objective: IV.3
Why: The source is not a point, so the diaphragm casts a partial shadow that grows as you move away from the diaphragm. Substitute 1.6 × (85 + 12 − 42) / 42 = 1.6 × (55) / 42 = 1.6 × 1.3095 = 2.0952 cm, reported as 2.10 cm. This geometric width is not the physical penumbra. Physical penumbra is the 80% to 20% dose distance, usually quoted at dmax. Dropping the depth and using (SSD-SDD), which is the surface penumbra gives 1.64 cm. Forgetting to subtract SDD inside the parentheses gives 3.70 cm. Forgetting to multiply by the source diameter gives 1.31 cm.

### Q10
Stem: Practice exam 2. Breast couch kick. SAD is 100 cm and the jaw opening that diverges at the posterior border of a tangent is 17 cm, symmetric about the central axis. The rotation that follows that divergence is θ = arctan((jaw opening / 2) / SAD). What is θ to the nearest 0.1°?
A. 9.6°
B. 85.1°
C. 0.09°
D. 4.9°
Answer: D
Objective: IV.3
Why: Half the opening is 17/2 = 8.5 cm. The opposite-over-adjacent ratio is 8.5/100 = 0.0850. θ = arctan(0.0850) = 4.86°, which rounds to 4.9°. A half-beam jaw (opening closed to the central axis on the match side) has zero divergence at that border, so the matching angle for that border is 0°. Using the full jaw opening in the arctan, arctan(17/100), gives 9.6°. Flipping the triangle to arctan(SAD / half-opening) = arctan(100/8.5) gives 85.1°. Reporting the ratio 0.0850 as though it were already in degrees gives 0.09°.

### Q11
Stem: Practice exam 2. Timer setting. Two exposures give 66 cGy in 0.7 min and 171.6 cGy in 1.9 min. Timer error is extra effective on-time during transit, so true dose rate = (R2−R1)/(t2−t1) and timer error = R1/dose rate − t1. Set time = dose/dose rate − timer error. What timer setting delivers 176 cGy?
A. 2.00 min
B. 2.05 min
C. 1.82 min
D. 1.95 min
Answer: D
Objective: IV.3
Why: True dose rate = (171.6−66)/(1.9−0.7) = 105.6/1.2 = 88 cGy/min. Timer error = 66/88 − 0.7 = 0.7500 − 0.7 = 0.0500 min. Set time = 176/88 − 0.0500 = 2.0000 − 0.0500 = 1.9500 min, reported as 1.95 min. The positive timer error means the source delivered extra dose during motion, so the set time is shorter than dose/rate. Ignoring timer error and setting dose/rate gives 2.00 min, which overdoses by the transit contribution. Adding the timer error instead of subtracting it gives 2.05 min and overdoses further. Using R1/t1 = 66/0.7 = 94.2857 cGy/min as the dose rate folds the transit dose into the rate and then still subtracting tau gives 1.82 min.

### Q12
Stem: Practice exam 2. TG-43 point dose rate. TG-43 point: air-kerma strength Sk = 3.3 U, dose-rate constant Λ = 1.11 cGy/(h·U), geometry function ratio G/G0 = 0.82, radial dose function g(r) = 0.97, anisotropy F = 0.9. Dose rate = Sk × Λ × (G/G0) × g(r) × F. What is the dose rate?
A. 2.91 cGy/h
B. 3.30 cGy/h
C. 3.20 cGy/h
D. 2.62 cGy/h
Answer: D
Objective: V.6
Why: Substitute 3.3 × 1.11 = 3.6630. × 0.82 = 3.0037. × 0.97 = 2.9136. × 0.9 = 2.6222 cGy/h, reported as 2.62 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Dropping anisotropy gives 2.91 cGy/h. Using only Sk × Λ × F and dropping geometry and radial dose gives 3.30 cGy/h. Dropping the geometry ratio gives 3.20 cGy/h.

### Q13
Stem: Practice exam 2. HDR course, α/β = 10 Gy. A course is 4 fractions of 6.5 Gy. Use α/β = 10 Gy. EQD2 = BED / (1 + 2/(α/β)), with BED = n×d×(1 + d/(α/β)). What is the EQD2?
A. 42.9 Gy
B. 26.0 Gy
C. 35.8 Gy
D. 49.4 Gy
Answer: C
Objective: V.6
Why: Physical dose = 4 × 6.5 = 26 Gy. BED = 26 × (1 + 6.5/10) = 26 × 1.6500 = 42.90 Gy. The 2 Gy denominator factor is 1 + 2/10 = 1.2000. EQD2 = 42.90 / 1.2000 = 35.75 Gy, reported as 35.8 Gy. If the fraction size is already 2 Gy, EQD2 equals the physical dose for any α/β. Here the fraction size is 6.5 Gy, so that shortcut applies only when d = 2. Stopping at the BED and not dividing by (1+2/(α/β)) gives 42.9 Gy. Reporting only the physical dose gives 26.0 Gy. Using α/β = 3 Gy instead of 10 Gy gives 49.4 Gy.

### Q14
Stem: A member of the public is exposed to 2.5 mSv in a year. Which NCRP 116 comparison is correct?
A. 2.5 mSv exceeds 50 mSv
B. 2.5 mSv exceeds the 1 mSv public limit and is under the 50 mSv occupational limit
C. 2.5 mSv is under 1 mSv
D. The public limit is 150 mSv
Answer: B
Objective: VI.1
Why: The public continuous limit is 1 mSv in a year. The occupational annual limit is 50 mSv. 2.5 mSv fails the public limit and would not fail the occupational annual limit. Correct choice: 2.5 mSv exceeds the 1 mSv public limit and is under the 50 mSv occupational limit. 2.5 is far under 50. 2.5 is greater than 1. 150 mSv is the NCRP 116 lens limit for occupational exposure.

### Q15
Stem: A declared pregnancy has a fetal-monitor reading of 0.30 mSv this month. Compare it with 0.5 mSv.
A. 0.30 mSv exceeds 0.5 mSv
B. The monthly value is 5 mSv
C. There is no monthly value once the gestation limit exists
D. 0.30 mSv is under the 0.5 mSv monthly value
Answer: D
Objective: VI.2
Why: 0.30 is below 0.5, so this month is under the monthly embryo/fetus value. The gestation allowance is 5 mSv, which this one month has not used up. Correct choice: 0.30 mSv is under the 0.5 mSv monthly value. 0.30 is smaller than 0.50. 5 mSv is the gestation total, not the month. Both the month and the gestation are used.

### Q16
Stem: Practice exam 2. wR is stated as 2. Absorbed dose is 6 mGy from protons. The problem states wR = 2. Dose equivalent H = wR × absorbed dose. Do not apply a tissue weighting factor; that would make effective dose, which is not asked. What is H?
A. 6.0 mSv
B. 3.0 mSv
C. 8.0 mSv
D. 12.0 mSv
Answer: D
Objective: VI.1
Why: Substitute H = 2 × 6 mGy = 12 mSv, reported as 12.0 mSv. With wR stated, you do not replace it by 1 unless the radiation actually has wR = 1 (photons and electrons). Reporting the absorbed dose unchanged gives 6.0 mSv and drops wR. Dividing by wR gives 3.0 mSv. Adding wR to the absorbed dose gives 8.0 mSv.

### Q17
Stem: Practice exam 2. How many HVL is a transmission of 0.125? A narrow beam is transmitted at a fraction 0.125 of the incident intensity. How many HVL is that? Transmission = (1/2)^(number of HVL).
A. 8 HVL
B. 3 HVL
C. 1.5 HVL
D. 3.3 HVL
Answer: B
Objective: VI.3
Why: (1/2)^n = 0.125. n = ln(0.125) / ln(1/2) = 3.0000, so n = 3 HVL. Check: 2^3 = 8, and 1/8 = 0.125. Reporting the denominator of the transmission fraction as if it were the HVL count gives 8 HVL. Taking half of the true HVL count gives 1.5 HVL. 3.3 HVL confuses one TVL (about 3.3 HVL, transmission 0.1) with this HVL count.

### Q18
Stem: Practice exam 2. Output is 1.024 cGy/MU against 1.000. Daily TG-142 tolerance is 3% and monthly is 2%. Expected output is 1 cGy/MU and the measurement is 1.024 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -2.4%
B. 2.4%
C. 2.3%
D. 102.4%
Answer: B
Objective: VII.1
Why: Substitute (1.024 − 1) / 1 × 100 = 0.024 / 1 × 100 = 2.40%, reported as 2.4%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -2.4%. Dividing the difference by the measurement instead of the expected value gives 2.3%. Reporting the ratio as a percent (100 × measured/expected) gives 102.4%, which is not the deviation.

### Q19
Stem: Practice exam 2. Measured electron cutout factor versus the factor used for MU. The cutout was planned with output factor 0.99, but the measured factor for that cutout is 0.93. The MU were calculated with the planned factor for an intended 160 cGy. Delivered dose = intended × (true factor / factor used), because MU = dose/(calibration × factor × …) and a factor that is too high makes the MU too small. What dose is delivered?
A. 150.3 cGy
B. 160.0 cGy
C. 170.3 cGy
D. 150.4 cGy
Answer: A
Objective: VII.5
Why: Factor ratio = 0.93 / 0.99 = 0.9394. Delivered = 160 × 0.9394 = 150.30 cGy, reported as 150.3 cGy. The patient is underdosed when the factor used in the MU calculation is larger than the true output factor. Assuming the intended dose was delivered gives 160.0 cGy. Inverting the factor ratio gives 170.3 cGy and would claim an overdose. Subtracting the raw factor difference from 1 and multiplying gives 150.4 cGy, which is not how an output factor enters the MU equation.

### Q20
Stem: Which action stays inside AAMD scope?
A. Change the total dose without a new order
B. Document the calculation that supports the physician's prescription
C. Sign the annual TG-51 report as the physicist
D. Cancel a written directive because the dwell times look long
Answer: B
Objective: VII.6
Why: Scope covers designing and documenting the plan under the physician and the physicist. It does not include an independent prescription or a physics calibration signature. Correct choice: Document the calculation that supports the physician's prescription. That is prescribing. Calibration authority is the physicist's. The directive is not the dosimetrist's to cancel.

### Q21
Stem: You need a quantitative exposure rate beside an LDR implant. Which meter is appropriate?
A. A GM meter that is already pinned at the top of the scale
B. A diode array used for IMRT gamma
C. An ion-chamber survey meter
D. An uncalibrated TLD read next week
Answer: C
Objective: VII.3
Why: An ion-chamber survey meter measures exposure rate without the dead-time failure of a GM tube in a high field. Correct choice: An ion-chamber survey meter. A saturated GM reading is not a measurement. The array is a beam QA tool, not a bedside survey meter. You need a number now, from a calibrated rate meter.

### Q22
Stem: A lung target moves 1.5 cm with breathing and the patient can hold a reproducible breath. Which motion strategy fits?
A. Respiratory gating or a breath hold, plus imaging that matches that state
B. Ignore the motion because a 1 cm PTV margin is always enough
C. Turn off the CT scanner's external lasers
D. Switch the calculation to Mayneord F
Answer: A
Objective: II.3
Why: Motion of 1.5 cm will smear dose unless you gate, coach a breath hold, track, or deliberately open a margin that you have measured. The image used for planning has to represent the state you will treat. Correct choice: Respiratory gating or a breath hold, plus imaging that matches that state. 1.5 cm of motion is larger than a 1 cm margin. The motion has to be managed or covered on purpose. Lasers do not stop breathing. Mayneord F does not freeze anatomy.

### Q23
Stem: A CT arrives labeled feet-first and the patient was scanned head-first. What fails if you plan anyway?
A. Only the HU of water
B. Laterality and the superior-inferior direction
C. The Ir-192 half-life
D. The wedge factor alone
Answer: B
Objective: II.1
Why: Import checks include orientation. A feet-first label on a head-first scan swaps superior-inferior and can swap left-right depending on the transformation. You stop and fix the orientation before contouring. Correct choice: Laterality and the superior-inferior direction. Water's HU can be perfect while the patient is flipped. No source decay is involved. A wedge factor will not repair a flipped data set.

### Q24
Stem: Mean liver dose is 29 Gy. Which reading matches the liver correlate used here?
A. 29 Gy is under the 30–32 Gy liver band
B. 29 Gy exceeds 32 Gy
C. The liver correlate is the cord dose of 50 Gy
D. The kidney mean of 18 Gy is the liver limit
Answer: A
Objective: III.8
Why: The liver correlate is a mean under 30–32 Gy. 32 − 29 = 3 Gy under the top of that band, and 29 is also under 30. 29 does not exceed 32. The cord correlate is 50 Gy. The top of the kidney band, 18 Gy, is not the liver limit.

### Q25
Stem: Bilateral kidney mean dose is 16 Gy. Which reading matches the kidney correlate used here?
A. 16 Gy is above 18 Gy
B. 16 Gy fails because the band has no upper value of 18 Gy
C. 16 Gy lies inside the 15–18 Gy kidney band
D. Kidney V20 must be ≤ 30%, copied from lung
Answer: C
Objective: III.8
Why: The kidney correlate is a bilateral mean under 15–18 Gy. 16 is above 15 and below 18, so it sits inside the band. 18 − 16 = 2 Gy under the top. 16 is not above 18. Lung V20 ≤ 30% is not the kidney mean.

### Q26
Stem: The entire peritoneal potential space is contoured and V45 is 180 cc. Chemotherapy will be given. Which bowel comparison is correct?
A. 180 cc is under the V45 < 195 cc peritoneal correlate
B. Use V15 < 120 cc, so 180 cc fails
C. 180 cc fails 195 cc
D. There is no published cc constraint for bowel
Answer: A
Objective: III.8
Why: The peritoneal correlate is V45 < 195 cc. Room under that value = 195 − 180 = 15 cc, so 180 cc meets it. Loop contours use V15 < 120 cc instead. 180 is less than 195. The 120 cc and 195 cc numbers stay tied to how the volume was drawn.

### Q27
Stem: Individual small-bowel loops have V15 = 140 cc. By how many cc does this exceed the loop correlate?
A. 0 cc
B. 20 cc
C. 140 cc
D. 75 cc
Answer: B
Objective: III.8
Why: The loop correlate is V15 < 120 cc. Excess = 140 − 120 = 20 cc. The peritoneal correlate is V45 < 195 cc, and 195 − 140 = 55 cc would be the wrong comparison because these are loops, not the peritoneal space. 140 − 65 = 75 cc invents a limit. Quoting 140 cc reports the DVH volume, not the excess. Calling the constraint met would be 0 cc over.

### Q28
Stem: Practice exam 2. Using the rule of thumb that practical range in cm is about E/2 for E in MeV, what is the practical range of a 10 MeV electron beam?
A. 3.3 cm
B. 2.5 cm
C. 5.0 cm
D. 10.0 cm
Answer: C
Objective: III.1
Why: Practical range ≈ 10 / 2 = 5.0 cm, reported as 5.0 cm. The 80% depth is about E/3 = 3.3 cm, and the 90% depth is about E/4 = 2.5 cm. Energy loss is about 2 MeV/cm. E/3 = 3.3 cm is the 80% depth, not the practical range. E/4 = 2.5 cm is the 90% depth. Using E itself as the range in cm gives 10.0 cm, about twice the practical range.

### Q29
Stem: Internal eye shields are appropriate for which electron situation?
A. Low electron energies only, because higher energies produce bremsstrahlung in the shield
B. Any energy, including 18 MeV, if the shield is lead
C. Photon beams above 15 MV
D. Proton beams at 250 MeV
Answer: A
Objective: III.6
Why: Internal eye shields are restricted to low electron energies, on the order of 6–9 MeV. At higher electron energies the shield adds dose to the eye from bremsstrahlung and backscatter. Correct choice: Low electron energies only, because higher energies produce bremsstrahlung in the shield. A high-energy beam turns the shield into a source of bremsstrahlung and backscatter. An internal eye shield is an electron technique, not a high-energy photon technique. That is not the electron eye-shield rule.

### Q30
Stem: Practice exam 2. Tumor BED, α/β = 10 Gy, 10 fractions of 3 Gy. A course is 10 fractions of 3 Gy. Use α/β = 10 Gy. BED = n × d × (1 + d/(α/β)). What is the BED?
A. 30.0 Gy
B. 39.0 Gy
C. 130.0 Gy
D. 32.5 Gy
Answer: B
Objective: III.3
Why: Physical dose = 10 × 3 = 30 Gy. Relative effectiveness = 1 + 3/10 = 1 + 0.3000 = 1.3000. BED = 30 × 1.3000 = 39.00 Gy, reported as 39.0 Gy. EQD2 would divide this BED by (1 + 2/(α/β)) = 1.2000, giving 32.50 Gy. That is a different question. Stopping at the physical dose gives 30.0 Gy and omits the fraction-size term. Inverting the fraction-size term to 1+(α/β)/d gives 130.0 Gy. Reporting the EQD2 (32.5 Gy) answers a different quantity than BED.

### Q31
Stem: Which structure is gross disease with no automatic margin?
A. CTV
B. GTV
C. PTV
D. PRV
Answer: B
Objective: III.11
Why: GTV is what you can see or measure. CTV expands it for microscopic disease. PTV expands the CTV for geometric uncertainty. Correct choice: GTV. CTV includes subclinical spread around the GTV. PTV adds setup and motion margin around the CTV. A PRV is a margin on an organ at risk, not the gross tumor.

### Q32
Stem: Why does a planner add bolus to a 6 MV scar?
A. To lower skin dose
B. To act as a wedge
C. To harden the beam by two HVL
D. To move dmax to the skin and raise surface dose
Answer: D
Objective: III.7
Why: Bolus pulls the buildup curve toward the surface so a superficial scar is not sitting in the buildup region. For 6 MV, dmax is about 1.5 cm, and 0.5 cm of bolus moves the peak to about 1.0 cm below the skin. Correct choice: To move dmax to the skin and raise surface dose. Bolus does the opposite. It fills buildup. Bolus is not a wedge. It does not tilt the isodose the way a heel does. A centimeter of tissue-equivalent bolus is not two HVL of lead.

### Q33
Stem: Helical tomotherapy, compared with a few static step-and-shoot fields, is characterized by what?
A. Binary MLC, continuous rotation, and typically more MU and a longer delivery
B. A single open field with no modulation
C. The lowest possible MU of any IMRT style
D. No need for a dose grid
Answer: A
Objective: III.5
Why: Helical tomotherapy rotates continuously and opens binary leaves. That delivery spends more MU and more time than a short step-and-shoot plan. Sliding window on a C-arm is a third pattern: beam on, leaves moving, MU usually higher than step-and-shoot. Correct choice: Binary MLC, continuous rotation, and typically more MU and a longer delivery. TomoTherapy modulates with a binary collimator. The helical delivery is MU-heavy and time-heavy relative to a simple static plan. The dose is still sampled on a grid.

### Q34
Stem: An autoplan meets the optimizer's own objectives. What still has to happen?
A. Nothing. The script is the plan check
B. A person reviews targets, organs, and the DVH before approval
C. The CT-density table can be skipped because the script ran
D. QUANTEC is applied only if the script fails
Answer: B
Objective: III.10
Why: Autoplanning and autocontouring are starting points. Contours can be wrong, and an objective that was never entered will not be protected. A dosimetrist still reviews the plan. Correct choice: A person reviews targets, organs, and the DVH before approval. Automation does not replace review. A bad density table still biases an autoplan. Constraints are reviewed whether or not the optimizer says it converged.

### Q35
Stem: A plan is normalized so the prescription covers 95% of the PTV, and the hot spot is 108%. What did that normalization choose?
A. A homogeneous 100% to every voxel
B. Coverage of the PTV, at the cost of a hot spot above the prescription
C. The ICRU minimum equal to the maximum
D. Removal of the PTV margin
Answer: B
Objective: III.7
Why: Normalizing to a coverage goal (95% of the PTV at the prescription) lets the maximum rise. The alternative, normalizing to a lower hot spot, can uncover the PTV. The choice should be visible on the DVH. Correct choice: Coverage of the PTV, at the cost of a hot spot above the prescription. 108% means the plan is not flat at the prescription. Those are not equal here. Normalization does not delete a margin.

### Q36
Stem: On an axial slice through the prostate, where is the rectum?
A. Anterior to the prostate
B. Inside the bladder
C. Posterior to the prostate
D. Lateral to both femoral heads
Answer: C
Objective: III.4
Why: The rectum lies posterior to the prostate, and the bladder lies anterior and superior. A contour that places rectum in front of the prostate is on the wrong structure. Correct choice: Posterior to the prostate. The bladder is anterior. The rectum is posterior. They are separate structures. The femoral heads are lateral to the prostate. The rectum is midline and posterior.

### Q37
Stem: Why is a beam spoiler used for total-body irradiation with megavoltage photons?
A. To act as two HVL of lead
B. To lower skin dose below the open-beam value
C. To replace the compensators entirely with no other reason
D. To raise skin dose by adding scatter and removing buildup
Answer: D
Objective: III.6
Why: A lucite or similar spoiler sits near the patient so electron contamination and scatter bring dose up to the skin, which a bare megavoltage beam would underdose. Correct choice: To raise skin dose by adding scatter and removing buildup. A spoiler is a low-Z screen, not a lead shield of two HVL. The spoiler is there to increase superficial dose. Compensators flatten the dose along the body. The spoiler's job is the skin.

### Q38
Stem: Which optimizer setting directly limits cord dose?
A. A maximum-dose or maximum-DVH objective on the cord
B. A minimum-dose objective on the cord
C. An equivalent-square constraint
D. Turning the dose grid off
Answer: A
Objective: III.12
Why: Serial organs are protected with a maximum dose or a maximum DVH point. A minimum-dose objective does the opposite. Correct choice: A maximum-dose or maximum-DVH objective on the cord. A minimum would push dose onto the cord. Equivalent square is a hand-calc field size, not an optimizer objective. The grid is not an objective, and you cannot compute a DVH without sampling dose.

### Q39
Stem: Where does a hydrogel spacer belong if it is used for prostate radiotherapy?
A. Inside the bladder only
B. In the femur
C. Around the pacemaker
D. Between the prostate and the rectum
Answer: D
Objective: III.13
Why: The gel is injected to increase the distance between prostate and rectum so the rectum can sit farther from the high dose. It is an implanted device and has to be contoured, not ignored as artifact. Correct choice: Between the prostate and the rectum. The spacer is not a bladder implant. That is not the organ being separated. A spacer gel is a prostate-rectum device, not a cardiac device.

### Q40
Stem: Both the tangent and the supraclavicular field are half-beamed on a single isocenter. What divergence remains at that superior match line?
A. arctan(0.1) degrees, always
B. The hinge angle of a 60° wedge
C. None. The match edge is the central axis
D. One HVL of overlap
Answer: C
Objective: III.7
Why: A jaw on the central axis does not diverge. Half-beam on both sides of one isocenter removes superior-border divergence. You may still rotate the collimator for the posterior tangent border, which is a different jaw. Correct choice: None. The match edge is the central axis. That angle is for a symmetric 20 cm field at SAD 100 cm, not for a jaw parked on the central axis. The wedge hinge is a different border. HVL is not a geometric match angle.

### Answer key

| Item | Answer | Objective |
| --- | --- | --- |
| Q1 | D | I.10 |
| Q2 | C | I.10 |
| Q3 | A | I.6 |
| Q4 | A | I.3 |
| Q5 | C | I.1 |
| Q6 | A | I.8 |
| Q7 | B | IV.3 |
| Q8 | A | IV.3 |
| Q9 | D | IV.3 |
| Q10 | D | IV.3 |
| Q11 | D | IV.3 |
| Q12 | D | V.6 |
| Q13 | C | V.6 |
| Q14 | B | VI.1 |
| Q15 | D | VI.2 |
| Q16 | D | VI.1 |
| Q17 | B | VI.3 |
| Q18 | B | VII.1 |
| Q19 | A | VII.5 |
| Q20 | B | VII.6 |
| Q21 | C | VII.3 |
| Q22 | A | II.3 |
| Q23 | B | II.1 |
| Q24 | A | III.8 |
| Q25 | C | III.8 |
| Q26 | A | III.8 |
| Q27 | B | III.8 |
| Q28 | C | III.1 |
| Q29 | A | III.6 |
| Q30 | B | III.3 |
| Q31 | B | III.11 |
| Q32 | D | III.7 |
| Q33 | A | III.5 |
| Q34 | B | III.10 |
| Q35 | B | III.7 |
| Q36 | C | III.4 |
| Q37 | D | III.6 |
| Q38 | A | III.12 |
| Q39 | D | III.13 |
| Q40 | C | III.7 |
