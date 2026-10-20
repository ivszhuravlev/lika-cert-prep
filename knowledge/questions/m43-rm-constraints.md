# Module 43. Memory Lane

Original items. Constraint rows added after the RM review: cord PRV, pharyngeal constrictors, kidney volume bins, mandible, conventional brachial plexus, femoral heads, lens and eye, breast tangent lung and heart, and the QUANTEC stereotactic cord line.

## Constraint rows added from review

### Q1
Stem: A conventional head-and-neck IMRT plan reports cord Dmax 44 Gy and cord PRV (cord plus 5 mm) Dmax 51.5 Gy. The protocol writes its 50 Gy limit on the PRV. What is the verdict?
A. Passes, because the cord contour itself is under 50 Gy
B. Fails, because the PRV maximum is 1.5 Gy over the 50 Gy limit
C. Passes, because PRV limits apply only to stereotactic plans
D. Cannot be judged, because QUANTEC has no PRV row and the PRV value is ignored
Answer: B
Objective: III.8
Why: When a protocol writes the limit on the PRV, the PRV maximum is the number that is scored: 51.5 − 50 = 1.5 Gy over, so the plan fails. The cord contour being 44 Gy is reassuring but does not satisfy a limit that was written on the 5 mm expansion. PRV margins are a conventional-fractionation planning habit from RTOG head-and-neck protocols, not a stereotactic-only idea. QUANTEC's 50 Gy row is written for the cord contour, which is exactly why the protocol adds its own PRV line; a missing QUANTEC row does not cancel the protocol's.

### Q2
Stem: A head-and-neck plan reports larynx mean 42 Gy, larynx Dmax 64 Gy, and pharyngeal constrictor mean 53 Gy. Against the QUANTEC rows, which structure fails?
A. The larynx, on the mean below 44 Gy edema row
B. The larynx, on the Dmax below 66 Gy row
C. Neither, because the constrictors are not a QUANTEC structure
D. The pharyngeal constrictors, on the mean below 50 Gy row
Answer: D
Objective: III.8
Why: QUANTEC gives the pharyngeal constrictors their own row, mean below 50 Gy for dysphagia and aspiration, and 53 Gy is 3 Gy over it. The larynx passes both of its rows here: 42 is under the 44 Gy edema mean and 64 is under the 66 Gy vocal-dysfunction maximum. A plan can clear every larynx row and still fail the constrictors, which is why the constrictor row must be read separately. Calling the constrictors "not QUANTEC" is the error the review flagged; the larynx-and-pharynx paper lists both.

### Q3
Stem: An abdominal plan reports bilateral kidney mean 14 Gy, V12 50%, V20 35%, V23 25%, V28 15%. Judged against the full QUANTEC kidney set, what is the result?
A. Fails on V20 only, which is 3 percentage points over 32%
B. Passes every row, because the mean is under 15 Gy
C. Fails on V20 and V23
D. Fails on the mean, because 14 Gy is above the 12 Gy figure
Answer: A
Objective: III.8
Why: The QUANTEC kidney set is mean below 15–18 Gy, V12 below 55%, V20 below 32%, V23 below 30%, V28 below 20%. Mean 14 passes, V12 50 passes, V20 35 fails (35 − 32 = 3 points over), V23 25 passes, V28 15 passes. One failing bin fails the set, so the mean passing does not rescue the plan. There is no 12 Gy mean row; 12 Gy is the dose level of the V12 bin, not a mean limit.

### Q4
Stem: A plan reports bilateral kidney mean 13 Gy, V20 30%, V23 31%, V28 18%. Which single QUANTEC bin fails?
A. V20
B. V23
C. V28
D. The mean
Answer: B
Objective: III.8
Why: V23 is 31% against a limit of below 30%, 1 point over, so it fails. V20 at 30% is under 32%, V28 at 18% is under 20%, and the mean of 13 Gy is under the 15–18 Gy row. Each bin has its own dose level and its own percent; reading V23 against the V20 figure of 32% would wrongly pass it. The set fails on this one bin even though the other three pass.

### Q5
Stem: A head-and-neck plan reports mandible Dmax 72 Gy to 0.03 cubic centimeters and 0.4 cubic centimeters of mandible above 70 Gy. Using the mandible row in this bank, which statement is correct?
A. Meets the goal, because less than 1 cubic centimeter is above 70 Gy
B. Fails outright, because any mandible volume above 70 Gy is a violation
C. Misses the Dmax 70 Gy goal but is inside the 1 cubic centimeter variation allowance
D. Cannot be judged without the V60 bin
Answer: C
Objective: III.8
Why: The row has two parts: the planning goal is Dmax below 70 Gy, and the protocol variation line is that no 1 cubic centimeter exceeds 70 Gy. Dmax 72 Gy misses the goal by 2 Gy; 0.4 cubic centimeters above 70 Gy is under the 1 cubic centimeter line, so the plan is a recorded variation rather than a pass or a hard failure. Option A collapses the goal into the variation line. Option B is the opposite error, ignoring the volume allowance that RTOG protocols write in. A V60 figure belongs to a different department-template row and is not needed here.

### Q6
Stem: A 3D conformal lung plan, 60 Gy in 30 fractions, reports brachial plexus Dmax 64 Gy. Against the conventional-fractionation plexus row this bank uses, what is the verdict?
A. Fails, because the TG-101 five-fraction point maximum is 30.5 Gy
B. Fails, because all nerves share the cord limit of 50 Gy
C. Passes, because the brachial plexus has no conventional limit
D. Passes, because 64 Gy is at or below the 66 Gy RTOG row
Answer: D
Objective: III.8
Why: The conventional plexus row is Dmax at or below 66 Gy from RTOG head-and-neck and lung protocols, and 64 is 2 Gy under it. The TG-101 cells (17.5, 24, 30.5 Gy point maximum for 1, 3, 5 fractions) are stereotactic and cannot be applied to a 30-fraction plan. The plexus is not scored on the cord's 50 Gy. A stem that instead names the Emami TD5/5 figure of 60 Gy would score 64 Gy as over, which is why the Why names the source; with no source named, this bank uses 66 Gy.

### Q7
Stem: A prostate IMRT plan to 78 Gy reports right femoral head V50 7% and left femoral head V50 3%; both have Dmax 54 Gy. The stem applies the V50 below 5% row. What is the result?
A. The right femoral head fails and the left passes
B. Both pass, because V50 under 10% is the RTOG figure
C. Both fail, because Dmax is above 50 Gy
D. Both pass, because femoral heads are judged by mean dose
Answer: A
Objective: III.8
Why: With the V50 below 5% row applied, right 7% is 2 points over and fails, left 3% is under and passes. The RTOG prostate protocols print V50 below 10%, which would pass both, but the stem said which figure to use and the stem wins. Dmax below 50 Gy is the stricter alternative that some templates write instead of V50; it was not the row applied here, so 54 Gy does not fail the plan by itself. Femoral heads are not a mean-dose structure on any common template.

### Q8
Stem: A brain IMRT plan reports right lens Dmax 8.5 Gy and left lens Dmax 4 Gy. The protocol writes lens Dmax below 7 Gy. What is the verdict?
A. Both pass, because the Emami figure is 10 Gy
B. Both fail, because the cataract threshold is about 2 Gy
C. The right lens fails and the left passes
D. The left lens fails and the right passes
Answer: C
Objective: III.8
Why: The protocol figure is 7 Gy: right 8.5 is 1.5 Gy over and fails, left 4 is under and passes. Emami's 10 Gy TD5/5 is one end of the published 7–10 Gy range, but the protocol chose 7 and the printed figure governs. The 1–2 Gy opacity threshold is a radiation-protection teaching number, not a planning constraint; scoring a 4 Gy lens as a failure against it would make most skull-base plans unplannable. Lens is not a QUANTEC row, so there is no QUANTEC number to appeal to.

### Q9
Stem: A sinonasal IMRT plan reports ipsilateral retina Dmax 47 Gy and ipsilateral globe Dmax 49 Gy. The protocol writes retina below 45 Gy and globe below 50 Gy. Which statement is correct?
A. Both rows pass, because QUANTEC gives no eye constraint
B. Both rows fail, because the eye is a single serial organ
C. The globe row fails by 1 Gy and the retina row passes
D. The retina row fails by 2 Gy and the globe row passes
Answer: D
Objective: III.8
Why: Retina 47 against below 45 is 2 Gy over, a failure; globe 49 against below 50 is 1 Gy under, a pass. The retina and globe are separate rows with separate figures, taken from the Emami retina TD5/5 of 45 Gy and RTOG head-and-neck templates of 45–50 Gy. The absence of a QUANTEC eye row does not erase a protocol row that the plan was asked to meet. Reading the globe figure onto the retina would wrongly pass the plan.

### Q10
Stem: A left whole-breast tangent plan, 50 Gy in 25 fractions, reports ipsilateral lung V20 22% and bilateral lung V20 11%. Against the breast template row, what is the verdict?
A. Passes, because bilateral V20 of 11% is far under 30%
B. Fails, because ipsilateral V20 of 22% is over the 15–20% tangent row
C. Passes, because 22% is under the 30% QUANTEC lung row
D. Fails, because no lung at all may receive 20 Gy from tangents
Answer: B
Objective: III.8
Why: Tangents treat one lung, so the breast template scores the ipsilateral lung: V20 below 15–20% (RTOG 1005 writes at or below 15%), and 22% is over either end of that range. The bilateral 30% row is the thoracic-radiotherapy pneumonitis row and is the wrong row for a tangent plan; a bilateral V20 of 11% is low only because the uninvolved lung dilutes the percent. Some lung in the tangent field is unavoidable, so a zero-tolerance reading is not a real constraint.

### Q11
Stem: A left-breast plan reports heart V25 of 6% and mean heart dose 5.8 Gy. The template applies both the QUANTEC V25 below 10% row and the breast row of mean heart dose below 4–5 Gy. What is the result?
A. Fails on the mean only
B. Passes both rows
C. Fails on V25 only
D. Fails on both rows
Answer: A
Objective: III.8
Why: V25 6% is under 10%, a pass on the QUANTEC cardiac-mortality row. Mean 5.8 Gy is over the 4–5 Gy breast row at either end (5.8 − 5 = 0.8 Gy over the looser figure), a failure. The two rows are different endpoints and are scored independently; a passing V25 does not clear a failing mean. The mean-dose row rests on the Darby relation of about 7% more major coronary events per gray of mean heart dose, which is why breast protocols write it as a separate line.

### Q12
Stem: A single-fraction spine SRS plan reports a cord maximum of 13.5 Gy. How does that read against the QUANTEC stereotactic cord line and the TG-101 single-fraction point maximum?
A. Passes both
B. Fails both
C. Over the QUANTEC 13 Gy line, under the TG-101 14 Gy point maximum
D. Under the QUANTEC line, over the TG-101 point maximum
Answer: C
Objective: III.8
Why: QUANTEC's cord paper places less than 1% myelopathy at 13 Gy in one fraction, and 13.5 is 0.5 Gy over it. TG-101 Table III gives a one-fraction point maximum (0.035 cubic centimeters) of 14 Gy, and 13.5 is 0.5 Gy under it. The two documents print different numbers for the same organ, so the verdict depends on which the stem names; this stem asked for both. Neither pass-both nor fail-both fits a value that sits between 13 and 14.

### Q13
Stem: A three-fraction spine SBRT plan reports a cord maximum of 19 Gy. Against the QUANTEC three-fraction cord line and the TG-101 three-fraction point maximum, what is the verdict?
A. Passes both
B. Fails the QUANTEC line only
C. Fails the TG-101 point maximum only
D. Fails both, because 19 Gy in three fractions exceeds 50 Gy in 2 Gy equivalents
Answer: A
Objective: III.8
Why: QUANTEC's three-fraction cord line is 20 Gy, and 19 is 1 Gy under. The TG-101 three-fraction cord point maximum is 21.9 Gy, and 19 is 2.9 Gy under. Both pass. Converting 19 Gy in three fractions to a 2 Gy equivalent with an alpha-beta of 2 gives about 40 Gy, which is also under 50 Gy, so the last option's arithmetic claim is wrong as well as being the wrong comparison for a stereotactic plan.

### Q14
Stem: A head-and-neck plan reports cord PRV Dmax 49 Gy, bilateral parotid mean 24 Gy, mandible Dmax 69 Gy, and pharyngeal constrictor mean 51 Gy. Which structure is limiting?
A. Cord PRV
B. Parotids
C. Mandible
D. Pharyngeal constrictors
Answer: D
Objective: III.8
Why: Compare each value with its row: PRV 49 against 50 passes, parotid bilateral mean 24 against 25 passes, mandible 69 against 70 passes, constrictor mean 51 against 50 fails by 1 Gy. The constrictors are the only failing row, so they are the limiting structure. The other three are all within 1 Gy of their figures, which is tight, but tight is not failing. Note that the fix for the constrictors must not push the PRV or the mandible over their own figures.

### Q15
Stem: An upper-abdominal plan reports bilateral kidney mean 12 Gy and V28 24%. The planner reports the kidneys as passing because the mean is under 15 Gy. Is that correct?
A. Yes, because the mean is the only QUANTEC kidney row
B. No, because V28 of 24% is over the 20% bin and one failing bin fails the set
C. Yes, because V28 is a stereotactic cell and does not apply at 2 Gy per fraction
D. No, because a mean of 12 Gy is over the V12 figure
Answer: B
Objective: III.8
Why: The QUANTEC kidney set includes V28 below 20%; 24% is 4 points over, so the set fails regardless of the mean. The mean row (15–18 Gy) is one member of a five-row set, not the whole constraint. V28 is a conventional-fractionation QUANTEC bin, not a TG-101 cell. V12 below 55% is a volume bin at 12 Gy and is not compared with the mean dose.

### Q16
Stem: Of the rows added to this module after the review, which one is a QUANTEC row rather than an RTOG-protocol or department-template figure?
A. Mandible Dmax below 70 Gy
B. Femoral head V50 below 5%
C. Bilateral kidney V28 below 20%
D. Lens Dmax below 7 Gy
Answer: C
Objective: III.8
Why: The kidney volume bins V20 below 32%, V23 below 30%, and V28 below 20% come from the QUANTEC kidney paper; the summary lesson had carried only the mean and V12. Mandible 70 Gy is an RTOG head-and-neck protocol line, femoral head V50 below 5% is a department-template tightening of the RTOG 10% figure, and the lens row is Emami and template practice with no QUANTEC chapter. Knowing the source matters because a stem that says "according to QUANTEC" cannot be answered with an RTOG template number.
