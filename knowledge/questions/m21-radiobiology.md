# Module 21 — Radiobiology

Original items. α/β values are the teaching numbers named in the stem. Surviving-fraction coefficients are a teaching pair, not a measured tumor.

## Cell Survival Curve

### Q1
Stem: Low-LET survival is written S = exp(−αD − βD²), with a shoulder at low dose. What does the shoulder represent?
A. Accumulation and repair of sublethal damage
B. A Bragg peak at the end of a proton range
C. Survival falling to zero in a step at one half-life
D. Absence of repair at every dose
Answer: A
Objective: III.3
Why: The shoulder is sublethal damage. If the dose is split and time is allowed for repair, more cells survive than if the same total is given at once, because the βD² term does not cross the gap between fractions. A Bragg peak is a proton depth-dose shape. Radioactive half-life is not the shape of this curve.

### Q2
Stem: In the linear-quadratic model, α/β in gray is the dose at which:
A. The linear contribution αD and the quadratic contribution βD² are equal
B. Surviving fraction is always 50%
C. The photon oxygen enhancement ratio equals 1
D. Tumor repopulation has exactly doubled the cell number
Answer: A
Objective: III.3
Why: Set αD = βD² and the dose that solves it is D = α/β. A large α/β means the linear term dominates and fractionation changes the effect less. A small α/β means dose per fraction matters more. α/β is not a surviving fraction, not an oxygen enhancement ratio, and not a repopulation time.

### Q3
Stem: No α/β is printed. You must still name the teaching values for late cord injury, generic tumor control, and prostate. Which set matches?
A. Cord ≈ 10 Gy, generic tumor ≈ 3 Gy, prostate ≈ 10 Gy
B. Cord ≈ 3 Gy, generic tumor ≈ 10 Gy, prostate often ≈ 1.5 Gy
C. All three equal 2 Gy
D. All three equal 1.1, the clinical proton RBE
Answer: B
Objective: III.3
Why: Late-responding tissue is taught at about 3 Gy. Early-responding tissue and most tumors are taught at about 10 Gy. Prostate is the usual low exception, often near 1.5 Gy. If a stem prints a value, use that value. Swapping 3 and 10 applies the late number to a tumor question or the tumor number to a cord question. 1.1 is a proton RBE, not an α/β.

### Q4
Stem: α = 0.20 Gy^−1 and β = 0.02 Gy^−2. What is αD + βD² for one fraction of 6 Gy?
A. 0.78
B. 1.20
C. 1.56
D. 1.92
Answer: D
Objective: III.3
Why: αD = 0.20 × 6 = 1.20. D² = 36, so βD² = 0.02 × 36 = 0.72. The sum is 1.20 + 0.72 = 1.92. One fraction of 3 Gy is 0.20 × 3 + 0.02 × 9 = 0.60 + 0.18 = 0.78. Two such fractions with full repair add to 0.78 + 0.78 = 1.56. Dropping βD² leaves only 1.20.

### Q5
Stem: With α = 0.20 Gy^−1 and β = 0.02 Gy^−2, compare a single 6 Gy fraction with two 3 Gy fractions separated by full repair. Which leaves more survivors?
A. The single 6 Gy, because its exponent 1.92 is larger
B. The two 3 Gy fractions, because the summed exponent 1.56 is smaller than 1.92
C. They match, because both deliver 6 Gy
D. The single 6 Gy, because βD² is smaller when the fraction is larger
Answer: B
Objective: III.3
Why: One 3 Gy fraction has αD + βD² = 0.20 × 3 + 0.02 × 9 = 0.78. Two fractions with full repair sum to 1.56. One 6 Gy fraction is 0.20 × 6 + 0.02 × 36 = 1.20 + 0.72 = 1.92. Surviving fraction is exp(−exponent), so the smaller exponent, 1.56, leaves more survivors. The quadratic piece is 0.72 for 6 Gy at once and only 0.18 for each 3 Gy fraction. Equal total dose does not equal equal kill.

### Q6
Stem: On a cell-survival plot, D0 is:
A. The prescription dose for the course
B. The dose that reduces survival to 37% (1/e) along the straight logarithmic portion
C. The clinical proton RBE of 1.1
D. The prostate α/β, about 1.5 Gy
Answer: B
Objective: III.3
Why: D0 is the slope dose on the exponential portion of the curve. One D0 along that line leaves 1/e, about 37%, of those cells. Dq measures shoulder width, and n is the extrapolation number where the straight portion would meet the survival axis at zero dose. D0 is not a prescription. Clinical protons are low LET with a generic RBE of 1.1. Prostate α/β is a fractionation parameter, not D0.

## Cell Cycle

### Q1
Stem: Which phase statement matches the usual teaching?
A. Mitosis is the most sensitive phase, and late S is the most resistant
B. Late S is the most sensitive phase, and mitosis is the most resistant
C. G0 is the most sensitive phase because those cells are out of cycle
D. The cycle order is M, S, G2, G1, and there is no G0
Answer: A
Objective: III.3
Why: The cycle is G1, S, G2, and M. G0 cells have left the cycle until they are recruited. Mitosis, together with late G2, is the most sensitive portion. Late S is the most resistant. Early G1 is relatively sensitive, while a long G1 holds many cells in a more resistant state. Calling late S the sensitive phase swaps the pair the exam asks for.

### Q2
Stem: A twice-daily schedule leaves about 6 hours between fractions. Which R is that interval aimed at, as a teaching assumption?
A. Repopulation across a gap of weeks
B. Repair of sublethal damage
C. Reoxygenation alone, with repair excluded
D. A required break so the tumor can grow before the next fraction
Answer: B
Objective: III.3
Why: Repair of sublethal damage is the shoulder on the survival curve. About 6 hours is the common teaching interval for substantial repair when a twice-daily course is planned. The interval a protocol actually requires is the one written in that protocol. Repopulation is division of survivors during a longer gap. Reoxygenation is a separate R. An unplanned break favors the tumor.

### Q3
Stem: Two head-and-neck schedules have the same EQD2. One is completed in 6 weeks. The other has an unplanned 2-week interruption. What does the plain EQD2 comparison leave out?
A. Nothing; equal EQD2 already includes overall time
B. Repopulation during the gap
C. A benefit, because an unplanned break improves head-and-neck control
D. A change of α/β from 10 Gy to 3 Gy caused by the calendar
Answer: B
Objective: III.3
Why: The basic formula EQD2 = D (d + α/β) / (2 + α/β) assumes full repair between fractions and does not subtract repopulation. Head and neck cancer is the classic site where a gap hurts, especially after the first weeks. Equal EQD2 with different overall times is not the same biological treatment. The calendar does not rewrite α/β.

### Q4
Stem: As LET rises from photons toward high-LET particles, before the overkill region, what happens to the oxygen enhancement ratio and the shoulder?
A. The oxygen enhancement ratio rises toward 3 and the shoulder widens
B. The oxygen enhancement ratio falls toward 1 and the shoulder shrinks
C. Both stay fixed, because LET is only a name for exposure
D. Every particle takes the photon oxygen enhancement ratio of about 3 and the proton RBE of 1.1 at the same time
Answer: B
Objective: III.3
Why: For photons the oxygen enhancement ratio is about 2.5 to 3: hypoxia requires that many times more dose for the same effect. As LET rises, RBE rises, the shoulder shrinks, and the oxygen enhancement ratio falls toward 1 because the damage depends less on oxygen. Past a peak in LET, RBE falls again from overkill. Clinical protons remain low LET. Their generic RBE of 1.1 is not the photon oxygen enhancement ratio and it is not a neutron RBE.

### Q5
Stem: How do redistribution and reoxygenation affect a fractionated tumor course?
A. Survivors move from resistant phases into sensitive phases, and hypoxic survivors can become better oxygenated as the tumor shrinks
B. Fractionation stops repair in the tumor and leaves repair intact only on paper
C. They remove any need to choose an α/β
D. They are two names for the hinge angle of a wedged pair
Answer: A
Objective: III.3
Why: Redistribution, also called reassortment, lets cells that survived in a resistant phase such as late S move into a sensitive phase before the next fraction. Reoxygenation lets hypoxic cells that survived become better oxygenated as the tumor shrinks and blood flow reaches them. Repair is the separate R that operates in the gap. None of the four Rs is a wedge angle, and none of them replaces α/β in the BED formula.

### Q6
Stem: Which scoring rule matches the organ?
A. Lung is scored only by a maximum dose to a point, and cord is scored only by mean dose
B. Cord and brainstem are scored at the high-dose end; lung and liver are scored by mean dose or by volume
C. One numeric limit from memory fits every organ and every fractionation
D. Parotid is serial and spinal cord is parallel
Answer: B
Objective: III.3
Why: A serial organ loses function when a small segment is destroyed, so the high-dose end dominates for cord, brainstem, and optic pathway. A parallel organ loses function in proportion to the subunit killed, so mean dose and volume dominate for lung, liver, kidney, and parotid. The number you apply is still the one in the named source. Swapping the ends of the DVH answers a different question from the one the organ asks.

### Q7
Stem: A prenatal consult asks when radiation-related cognitive injury is most likely. Which gestational window is the high-risk teaching interval?
A. About 8-15 weeks
B. Weeks 0-7
C. After 25 weeks
D. Every week equally, from conception through term
Answer: A
Objective: III.3
Why: The gestational window of highest risk for radiation-related cognitive injury is about 8-15 weeks. Weeks 0-7 come before that window. The period after 25 weeks comes after it. Equal risk in every week would make the dates irrelevant, and this teaching does not do that.

## BEDs

### Q1
Stem: A course is 45 Gy in 15 fractions. For late effects, α/β = 3 Gy. What is the EQD2?
A. 45 Gy
B. 54 Gy
C. 48.8 Gy
D. 90 Gy
Answer: B
Objective: III.3
Why: d = 45/15 = 3 Gy. EQD2 = 45 × (3 + 3) / (2 + 3) = 45 × 6/5 = 54 Gy. Reporting 45 Gy treats every physical gray as if it were already a 2 Gy fraction. With α/β = 10, EQD2 = 45 × (3 + 10) / 12 = 45 × 13/12 = 48.75 Gy, about 48.8 Gy, which is the generic tumor result. The late BED is 45 × (1 + 3/3) = 45 × 2 = 90 Gy, and that BED is not the EQD2.

### Q2
Stem: The same 45 Gy in 15 fractions is scored for a generic tumor with α/β = 10 Gy. What is the BED?
A. 58.5 Gy
B. 90 Gy
C. 48.8 Gy
D. 45 Gy
Answer: A
Objective: III.3
Why: d = 3 Gy. BED = 45 × (1 + 3/10) = 45 × 1.3 = 58.5 Gy. The bridge check is EQD2 = 58.5 / (1 + 2/10) = 58.5 / 1.2 = 48.75 Gy, which matches 45 × (3 + 10) / 12 = 48.75 Gy. Ninety gray is the late BED at α/β = 3, from 45 × (1 + 1) = 90. 48.8 Gy is that tumor EQD2 rounded, not the BED. Forty-five gray is the physical dose.

### Q3
Stem: A course is 24 Gy in 3 fractions. For a generic tumor, α/β = 10 Gy. What is the EQD2?
A. 24 Gy
B. 43.2 Gy
C. 52.8 Gy
D. 36 Gy
Answer: D
Objective: III.3
Why: d = 24/3 = 8 Gy. EQD2 = 24 × (8 + 10) / (2 + 10) = 24 × 18/12 = 36 Gy. BED at this α/β is 24 × (1 + 8/10) = 24 × 1.8 = 43.2 Gy, and 43.2 / 1.2 = 36 Gy, the same EQD2. Late α/β = 3 gives EQD2 = 24 × (8 + 3) / 5 = 24 × 11/5 = 52.8 Gy. Twenty-four gray is the physical dose.

### Q4
Stem: For 24 Gy in 3 fractions, compare late tissue at α/β = 3 Gy with a generic tumor at α/β = 10 Gy. Which statement is correct?
A. Late EQD2 is 52.8 Gy, which is higher than the tumor EQD2 of 36 Gy
B. Late EQD2 is 36 Gy and tumor EQD2 is 52.8 Gy
C. Both EQD2 values equal 24 Gy
D. Late EQD2 is 88 Gy
Answer: A
Objective: III.3
Why: d = 8 Gy. Late EQD2 = 24 × (8 + 3) / (2 + 3) = 24 × 11/5 = 52.8 Gy. Tumor EQD2 = 24 × (8 + 10) / 12 = 24 × 18/12 = 36 Gy. The larger fraction raises the late EQD2 more than the generic-tumor EQD2. The late BED is 24 × (1 + 8/3) = 24 × 11/3 = 88 Gy. That 88 Gy is a BED, not the late EQD2. Dividing 88 by (1 + 2/3) = 5/3 gives 88 × 3/5 = 52.8 Gy again.

### Q5
Stem: A prostate course is 36.25 Gy in 5 fractions. The stem sets α/β = 1.5 Gy. What is the EQD2?
A. 90.6 Gy
B. 52.1 Gy
C. 36.3 Gy
D. 211.5 Gy
Answer: A
Objective: III.3
Why: d = 36.25/5 = 7.25 Gy. EQD2 = 36.25 × (7.25 + 1.5) / (2 + 1.5) = 36.25 × 8.75 / 3.5. Because 8.75/3.5 = 2.5, EQD2 = 36.25 × 2.5 = 90.625 Gy, which is 90.6 Gy. Using α/β = 10 instead gives 36.25 × (7.25 + 10) / 12 = 36.25 × 17.25 / 12 = 36.25 × 1.4375 = 52.1 Gy. 36.3 Gy is the physical dose rounded. BED at α/β = 1.5 is 36.25 × (1 + 7.25/1.5) = 36.25 × (35/6) = 211.5 Gy, and 211.5 / (1 + 2/1.5) = 211.5 / (7/3) = 211.5 × 3/7 = 90.6 Gy.

### Q6
Stem: Whole breast is prescribed 42.5 Gy in 16 fractions. For late effects, α/β = 3 Gy. What is the EQD2?
A. 42.5 Gy
B. 44.8 Gy
C. 48.1 Gy
D. 80.1 Gy
Answer: C
Objective: III.3
Why: d = 42.5/16 = 2.656 Gy. EQD2 = 42.5 × (2.656 + 3) / (2 + 3) = 42.5 × 5.656 / 5 = 240.38 / 5 = 48.08 Gy, which is 48.1 Gy. With α/β = 10, EQD2 = 42.5 × (2.656 + 10) / 12 = 42.5 × 12.656 / 12 = 537.88 / 12 = 44.8 Gy. Forty-two and a half gray is the physical dose. The late BED is 42.5 × (1 + 2.656/3) = 42.5 × 1.885 = 80.1 Gy. Dividing that BED by (1 + 2/3) = 5/3 returns 80.1 × 3/5 = 48.1 Gy.

### Q7
Stem: External beam is 50.4 Gy in 28 fractions. An illustrative HDR course is 6 Gy × 5. Both are converted at α/β = 10 Gy and then added. What is the sum EQD2?
A. 89.6 Gy
B. 80.4 Gy
C. 102.4 Gy
D. 49.6 Gy
Answer: A
Objective: III.3
Why: External-beam d = 50.4/28 = 1.8 Gy. EQD2 = 50.4 × (1.8 + 10) / 12 = 50.4 × 11.8 / 12 = 49.56 Gy. HDR physical dose is 6 × 5 = 30 Gy. EQD2 = 30 × (6 + 10) / 12 = 30 × 16/12 = 40 Gy. Sum at α/β = 10: 49.56 + 40 = 89.56 Gy, or 89.6 Gy. Adding the physical doses gives 50.4 + 30 = 80.4 Gy. At α/β = 3 the external-beam EQD2 is 50.4 × (1.8 + 3) / 5 = 50.4 × 4.8 / 5 = 48.38 Gy and the HDR EQD2 is 30 × (6 + 3) / 5 = 30 × 9/5 = 54 Gy, summing to 102.4 Gy. That late sum is a different α/β and is not the tumor total. 49.6 Gy is the external-beam piece alone.

### Q8
Stem: A course is 30 Gy in 5 fractions. For late effects, α/β = 3 Gy. What is the EQD2?
A. 30 Gy
B. 40 Gy
C. 54 Gy
D. 90 Gy
Answer: C
Objective: III.3
Why: d = 30/5 = 6 Gy. EQD2 = 30 × (6 + 3) / (2 + 3) = 30 × 9/5 = 54 Gy. BED = 30 × (1 + 6/3) = 30 × 3 = 90 Gy, and 90 / (1 + 2/3) = 90 × 3/5 = 54 Gy. With α/β = 10, EQD2 = 30 × (6 + 10) / 12 = 30 × 16/12 = 40 Gy and BED = 30 × (1 + 6/10) = 30 × 1.6 = 48 Gy. Forty gray is that tumor EQD2. Thirty gray is the physical dose. Ninety gray is the late BED.

## Radiobiology Quiz

### Q1
Stem: A note calls late S the most radiosensitive phase of the cell cycle. What is the correction?
A. Late S is the most resistant phase; mitosis, with late G2, is the most sensitive
B. Late S is sensitive, and G0 is more sensitive still
C. Phase does not matter; survival is flat through the cycle
D. The only sensitive point is the middle of a long G1
Answer: A
Objective: III.3
Why: Mitosis is the most sensitive phase, and late G2 is sensitive with it. Late S is the most resistant. G0 cells are out of cycle, not the peak of sensitivity. G1 length varies: early G1 is relatively sensitive, and a long G1 is more resistant. The order to remember is G1, S, G2, M.

### Q2
Stem: What are the four Rs of fractionation?
A. Repair, repopulation, redistribution, and reoxygenation
B. Range, RBE, registration, and re-scan
C. Reflection, refraction, rotation, and replay
D. Repair and repopulation only, plus the 80% and 20% penumbra
Answer: A
Objective: III.3
Why: Repair fixes sublethal damage between fractions. Repopulation is division of survivors, which a treatment gap allows. Redistribution moves survivors from resistant phases toward sensitive phases. Reoxygenation improves oxygenation of hypoxic cells that survived. An interval of hours is about repair. A gap of weeks is about repopulation. Range and image registration are not these four Rs.

### Q3
Stem: A schedule is 20 Gy in 5 fractions. Late tissue has α/β = 3 Gy. What is the EQD2?
A. 20 Gy
B. 23.3 Gy
C. 28 Gy
D. 46.7 Gy
Answer: C
Objective: III.3
Why: d = 20/5 = 4 Gy. EQD2 = 20 × (4 + 3) / (2 + 3) = 20 × 7/5 = 28 Gy. At α/β = 10, EQD2 = 20 × (4 + 10) / 12 = 20 × 14/12 = 23.3 Gy. The late BED is 20 × (1 + 4/3) = 20 × 7/3 = 46.7 Gy, and 46.7 × 3/5 = 28 Gy. Twenty gray is the physical dose.

### Q4
Stem: A single fraction of 8 Gy is converted with α/β = 10 Gy. What is the EQD2?
A. 17.6 Gy
B. 12 Gy
C. 8 Gy
D. 14.4 Gy
Answer: B
Objective: III.3
Why: EQD2 = 8 × (8 + 10) / (2 + 10) = 8 × 18/12 = 12 Gy. Late α/β = 3 gives 8 × (8 + 3) / 5 = 8 × 11/5 = 17.6 Gy. The physical dose is 8 Gy. BED at α/β = 10 is 8 × (1 + 8/10) = 8 × 1.8 = 14.4 Gy, and 14.4 / 1.2 = 12 Gy. The stem asked for EQD2 at α/β = 10, which is 12 Gy.

### Q5
Stem: A course is 60 Gy in 30 fractions. What is the EQD2 at α/β = 3 Gy and at α/β = 10 Gy?
A. 100 Gy and 72 Gy
B. 60 Gy and 60 Gy
C. 72 Gy and 65 Gy
D. 36 Gy and 32.5 Gy
Answer: B
Objective: III.3
Why: d = 60/30 = 2 Gy. EQD2 = 60 × (2 + α/β) / (2 + α/β) = 60 Gy at every α/β, including 3 Gy and 10 Gy. Late BED = 60 × (1 + 2/3) = 60 × 5/3 = 100 Gy, which is not the EQD2. Thirty gray in 10 fractions, a different course, has late EQD2 = 30 × 6/5 = 36 Gy and tumor EQD2 = 30 × 13/12 = 32.5 Gy.

### Q6
Stem: For 45 Gy in 15 fractions the late BED at α/β = 3 Gy is 90 Gy, and the tumor BED at α/β = 10 Gy is 58.5 Gy. What is the sum 90 + 58.5?
A. A valid combined BED of 148.5 Gy
B. Not a usable BED; the two numbers were computed at different α/β values
C. The EQD2 of both tissues
D. The physical dose to set on the machine
Answer: B
Objective: III.3
Why: BED at α/β = 3 is 45 × (1 + 3/3) = 45 × 2 = 90 Gy. BED at α/β = 10 is 45 × (1 + 3/10) = 45 × 1.3 = 58.5 Gy. Adding 90 + 58.5 = 148.5 mixes two α/β values and does not produce a biological dose. EQD2 values may be added only when they share one α/β. Neither BED is the physical dose of 45 Gy, and neither is the EQD2 (54 Gy late, 48.75 Gy at α/β = 10).

### Q7
Stem: For 54 Gy in 3 fractions and late α/β = 3 Gy, the EQD2 is 226.8 Gy. How should that result be used?
A. As proof the cord received 226.8 Gy in 2 Gy fractions, so a conventional cord limit applies directly
B. As the linear-quadratic result, while the stereotactic plan is judged by the stereotactic constraint source and the protocol
C. As the physical isocenter dose to deliver on the next fraction
D. As the tumor EQD2 at α/β = 10, which equals the same 226.8 Gy
Answer: B
Objective: III.3
Why: d = 54/3 = 18 Gy. Late EQD2 = 54 × (18 + 3) / (2 + 3) = 54 × 21/5 = 226.8 Gy. Late BED = 54 × (1 + 18/3) = 54 × 7 = 378 Gy. At α/β = 10, EQD2 = 54 × (18 + 10) / 12 = 54 × 28/12 = 126 Gy, not 226.8 Gy. The quadratic model is being used far above the fraction size it was built on. Stereotactic organ limits belong to the stereotactic source and the protocol. 226.8 Gy is not the physical dose.

### Q8
Stem: Which set of radiobiology labels is consistent?
A. Clinical protons are high LET with RBE about 3, and the photon oxygen enhancement ratio is about 1
B. Clinical protons are low LET with generic RBE 1.1; the photon oxygen enhancement ratio is about 2.5 to 3; high-LET oxygen enhancement ratio is closer to 1
C. RBE, oxygen enhancement ratio, and LET are three names for α/β
D. Neutrons and photons are both assigned RBE 1.1
Answer: B
Objective: III.3
Why: The generic clinical proton RBE used for prescribing is 1.1, and those protons are low LET. RBE is reference dose divided by test dose for the same effect. Photon oxygen enhancement ratio is about 2.5 to 3. High-LET radiation has an oxygen enhancement ratio closer to 1 and little shoulder. The factor 1.1 is not a neutron RBE and it is not an α/β.
