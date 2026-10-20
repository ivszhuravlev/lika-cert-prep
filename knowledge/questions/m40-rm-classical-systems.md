# Module 40. Brachytherapy

Original items. Written for the RM Review porting wave: classical implant systems, radium equivalence, line-source tables, and decay arithmetic for temporary and permanent implants.

## Classical Implant Systems, Radium Equivalence, and Line Sources

### Q1
Stem: A single-plane Manchester implant covers an area of 16 square centimeters. Under the Paterson-Parker distribution rules, how is the activity divided between the periphery and the center of the plane?
A. Half at the periphery and half in the center
B. Two thirds at the periphery and one third in the center
C. One third at the periphery and two thirds in the center
D. All of it at the periphery, with no central needles
Answer: B
Objective: V.2
Why: Below 25 cm² the Manchester rule puts two thirds of the activity in the peripheral needles and one third in the center, which flattens the dose to within about ±10% at 0.5 cm from the plane. Half and half applies between 25 and 100 cm². One third at the periphery applies above 100 cm². An empty center is not a Manchester pattern; the central needles carry less activity, not none.

### Q2
Stem: A Manchester cylindrical volume implant divides its total activity into eight parts. Which distribution follows the Paterson-Parker volume rule?
A. Belt 2, core 4, each end 1
B. Belt 6, core 2, no end sources
C. Belt 4, core 2, each end 1
D. Belt 3, core 3, each end 1
Answer: C
Objective: V.2
Why: The cylinder rule is four eighths in the belt, two eighths in the core, and one eighth at each end, with at least eight belt needles and four core needles. Option A reverses belt and core and would create a hot center. Option B is the sphere rule (shell 6, core 2). Option D is not a Paterson-Parker split. Each uncrossed end of a volume implant also removes 7.5% of the effective volume before the table is read.

### Q3
Stem: A single-plane Manchester implant measures 6 cm by 5 cm. One end of the plane cannot be crossed with a needle. What effective area is used to read the Paterson-Parker table?
A. 27 cm²
B. 30 cm²
C. 24 cm²
D. 27.75 cm²
Answer: A
Objective: V.6
Why: The physical area is 6 × 5 = 30 cm². Each uncrossed end of a planar implant reduces the effective area by 10%, so 30 × 0.90 = 27 cm². Check: 27 / 0.9 = 30. Option B ignores the penalty. Option C applies 20%, which would be right only if both ends were uncrossed. Option D applies the 7.5% penalty that belongs to volume implants.

### Q4
Stem: A Manchester planar implant is prescribed to deliver a stated dose of 6000 cGy. Which statement describes the dose actually found in the treatment plane 0.5 cm from the sources?
A. The dose is uniform to within ±2% across the plane, and 6000 cGy is the mean
B. The dose varies by about ±10%, and 6000 cGy is the maximum in the plane
C. The dose is uniform to within ±10%, and 6000 cGy is delivered at the periphery only
D. The dose varies by about ±10%, and the minimum in the plane is about 10% below 6000 cGy
Answer: D
Objective: V.2
Why: The Manchester system aims for a dose uniform to within about ±10% over the plane, and the stated dose is defined as 10% above the minimum dose in the plane, so the minimum is near 5400 cGy. Option A promises a uniformity no classical implant achieves. Option B describes the Quimby convention, where the planar stated dose is the central maximum. Option C misreads the periphery-weighted loading as a periphery-only prescription.

### Q5
Stem: In the central plane of a Paris-system Ir-192 implant, the local minimum dose rates between adjacent wires are 70, 74, and 66 cGy/h. What dose rate lies on the reference isodose that the Paris system prescribes to?
A. 70.0 cGy/h
B. 82.4 cGy/h
C. 59.5 cGy/h
D. 56.1 cGy/h
Answer: C
Objective: V.6
Why: The basal dose rate is the arithmetic mean of the local minima: (70 + 74 + 66) / 3 = 210 / 3 = 70 cGy/h. The reference isodose is 85% of the basal dose: 0.85 × 70 = 59.5 cGy/h. Check: 59.5 / 0.85 = 70. Option A prescribes to the basal dose itself. Option B divides by 0.85 instead of multiplying. Option D applies 85% to the lowest single minimum rather than the mean. The Paris system requires straight, parallel, equidistant lines of equal length and uniform linear activity, spaced about 8 to 15 mm, with midpoints in one central plane and no crossing needles, and the lines run about 30 to 40% beyond the target length to make up for the uncrossed ends.

### Q6
Stem: An interstitial implant is loaded with equal-strength sources at uniform spacing, as in the Quimby system. Compared with a Manchester implant of the same area, what dose pattern results and where is the planar dose stated?
A. A uniform dose across the plane, stated at the minimum
B. A non-uniform dose that is hottest at the center, stated at the maximum in the plane
C. A non-uniform dose that is hottest at the periphery, stated at the center
D. A uniform dose across the plane, stated at 85% of the central dose
Answer: B
Objective: V.2
Why: Uniform activity gives a non-uniform dose because the central region receives contributions from every source; the center is hottest, and Quimby stated the planar dose at that maximum (volume implants are stated at the minimum). Option A describes the Manchester goal, which needs periphery-weighted loading. Option C puts the hot spot in the wrong place. Option D mixes the Paris 85% rule into a uniform-dose claim. For the same minimum peripheral dose a Quimby implant needs more total milligram-hours than a Manchester implant, and the Memorial system extended Quimby to a 1 cm seed lattice with nomograms, the ancestor of prostate seed nomograms.

### Q7
Stem: An Ir-192 source is labeled 50 mCi. The exposure rate constant of Ir-192 is 4.69 R cm² per mCi per hour and that of radium is 8.25 R cm² per mg per hour. What is the strength of the source in milligram-radium-equivalent?
A. 88.0 mg-Ra-eq
B. 28.4 mg-Ra-eq
C. 234.5 mg-Ra-eq
D. 50.0 mg-Ra-eq
Answer: B
Objective: V.6
Why: mg-Ra-eq = activity × Γ of the nuclide / Γ of radium = 50 × 4.69 / 8.25 = 234.5 / 8.25 = 28.4 mg-Ra-eq. Check: 28.4 × 8.25 = 234.3, which matches 50 × 4.69 within rounding, and a millicurie of iridium must be worth less than a milligram of radium because its gamma constant is smaller. Option A inverts the ratio (50 × 8.25 / 4.69). Option C stops after the multiplication. Option D assumes one millicurie equals one milligram, which is true only for radium itself. In air-kerma strength the source is 28.4 × 7.227 = 205 U, since one mg-Ra-eq is 8.25 × 0.876 cGy cm² per hour.

### Q8
Stem: A written directive calls for 20 mg-Ra-eq of Cs-137 in an LDR applicator. Cs-137 has an exposure rate constant of 3.26 R cm² per mCi per hour. How many millicuries must be loaded?
A. 7.9 mCi
B. 65.2 mCi
C. 165 mCi
D. 50.6 mCi
Answer: D
Objective: V.6
Why: mCi = mg-Ra-eq × 8.25 / Γ of Cs-137 = 20 × 8.25 / 3.26 = 165 / 3.26 = 50.6 mCi. Check: 50.6 × 3.26 / 8.25 = 165 / 8.25 = 20.0 mg-Ra-eq. Option A applies the forward ratio (20 × 3.26 / 8.25) and would load one sixth of the ordered strength. Option B multiplies by the cesium constant alone. Option C stops before dividing by 3.26.

### Q9
Stem: A Cs-137 intracavitary tube has an overall capsule length of 20 mm and contains 14 mm of active material. Which length is entered in a line-source dose table or Sievert integral, and which decides whether the tube fits a given applicator slot?
A. The 14 mm active length for the dose table; the 20 mm physical length for the applicator fit
B. The 20 mm physical length for the dose table; the 14 mm active length for the applicator fit
C. The 14 mm active length for both
D. The 20 mm physical length for both
Answer: A
Objective: V.1
Why: Dose tables and the Sievert integral describe the distribution of radioactive material, so they use the active length; the inactive end caps and eyelet add to the physical length, which is what must fit the applicator and what sets the distance from the tip to the source center. Options B and D would compute dose as if the end caps were radioactive. Option C would let a 20 mm tube be planned into a 15 mm slot. The same distinction explains why the first HDR dwell position sits a few millimeters short of the catheter tip.

### Q10
Stem: A planner estimates the dose rate 1 cm from the center of a 3 cm active-length Cs-137 tube by treating the tube as a point source. What does the Sievert integral account for that this estimate ignores?
A. The radial dose function and the anisotropy function of the TG-43 formalism
B. The decay of the source during the treatment
C. The scatter contribution of the patient's tissue outside the implant
D. The finite active length and the oblique filtration of each element's photons through the capsule wall
Answer: D
Objective: V.6
Why: The Sievert integral sums point-element contributions along the active length, each attenuated by the capsule thickness divided by the cosine of the angle to that element, so it captures both the length and the oblique filtration. Option A names TG-43 factors, which replace the Sievert approach rather than extend the point-source formula. Option B is a separate decay correction. Option C is tissue scatter, handled by g(r) in TG-43, not by the Sievert integral. At 1 cm from a 3 cm source the point approximation overstates the fall-off; beyond about two active lengths it is within a few percent of the integral.

### Q11
Stem: Two identical 15 mg-Ra-eq Cs-137 tubes lie end to end on one axis with their centers 3.0 cm apart. Point P is 2.0 cm from the axis, directly opposite the center of the first tube. The along-and-away table for this tube, in cGy/h per mg-Ra-eq, reads 1.60 at along 0 and away 2.0 cm, and 0.55 at along 3.0 and away 2.0 cm. What is the dose rate at P?
A. 48.0 cGy/h
B. 24.0 cGy/h
C. 32.3 cGy/h
D. 16.1 cGy/h
Answer: C
Objective: V.6
Why: Each tube needs its own along-and-away pair. First tube: 15 × 1.60 = 24.0 cGy/h. Second tube, whose center is 3.0 cm along the axis from the foot of P: 15 × 0.55 = 8.25 cGy/h. Total 24.0 + 8.25 = 32.25, about 32.3 cGy/h. Check: a point-source estimate for the second tube is 15 × 7.227 / (3.0² + 2.0²) = 108.4 / 13 = 8.3 cGy/h, close to the table value. Option A reads the first tube's cell for both sources. Option B forgets the second tube. Option D averages the two table entries instead of adding the contributions.

### Q12
Stem: An interstitial implant is reported in ICRU 58 terms. The minimum target dose is 51 Gy and the mean central dose is 60 Gy. What is the dose homogeneity index?
A. 0.85
B. 1.18
C. 0.90
D. 1.50
Answer: A
Objective: V.2
Why: ICRU 58 defines the dose homogeneity index as the minimum target dose divided by the mean central dose: 51 / 60 = 0.85, the value a Paris implant produces because its reference isodose is 85% of the basal (mean central) dose. Check: 0.85 × 60 = 51. Option B is the inverse ratio. Option C is the threshold of the low-dose volume (less than 90% of the prescribed dose). Option D is the threshold of the high-dose volume (150% of the mean central dose). The mean central dose is the mean of the local minimum doses between sources in the central plane, and ICRU 58 takes the PTV equal to the CTV for interstitial work because the sources move with the tissue.

## Decay Arithmetic for Permanent Implants and Afterloaders

### Q1
Stem: A permanent Pd-103 prostate implant starts at an initial dose rate of 20 cGy/h. The half-life is 17.0 days. The patient undergoes prostatectomy and the seeds are removed 17 days after the implant. What dose has the gland received?
A. 117.7 Gy
B. 58.9 Gy
C. 81.6 Gy
D. 29.4 Gy
Answer: B
Objective: V.6
Why: Mean life = 1.443 × 17.0 = 24.5 days = 588.7 h. Total dose to complete decay = 20 × 588.7 = 11775 cGy = 117.7 Gy. Removal at one half-life delivers 1 − e^(−17/24.5) = 1 − e^(−0.693) = 0.50 of that total: 117.7 × 0.50 = 58.9 Gy. Check: after exactly one half-life, half of the integral dose has been delivered by definition. Option A is the complete-decay dose. Option C assumes a constant 20 cGy/h for 408 h (8160 cGy) and ignores decay. Option D is one quarter, the fraction that would remain after two half-lives.

### Q2
Stem: An I-125 implant has an initial dose rate of 8.0 cGy/h and a half-life of 59.4 days. It is removed after 30 days. What dose has been delivered?
A. 48.6 Gy
B. 57.6 Gy
C. 164.6 Gy
D. 82.3 Gy
Answer: A
Objective: V.6
Why: Mean life = 1.443 × 59.4 = 85.7 d = 2057 h; the complete-decay dose is 8.0 × 2057 = 16456 cGy = 164.6 Gy. Fraction delivered = 1 − e^(−30/85.7) = 1 − e^(−0.350) = 1 − 0.705 = 0.295. Dose = 164.6 × 0.295 = 48.6 Gy. Check: the no-decay dose is 8.0 × 24 × 30 = 5760 cGy = 57.6 Gy, and 30 days of I-125 decay should trim roughly 15%, giving about 49 Gy. Option B ignores decay. Option C is the dose to complete decay. Option D is half the total, which would need a full half-life (59.4 days), not 30.

### Q3
Stem: A temporary Ir-192 interstitial implant must deliver 30 Gy. The initial dose rate on the prescription isodose is 60 cGy/h and the half-life is 73.8 days. Accounting for decay during the implant, when should the sources be removed?
A. 50.0 h
B. 49.5 h
C. 101 h
D. 50.5 h
Answer: D
Objective: V.6
Why: Mean life = 1.443 × 73.8 = 106.5 d = 2556 h; the complete-decay dose would be 60 × 2556 = 153360 cGy. Ratio of prescribed to complete-decay dose = 3000 / 153360 = 0.01956. Removal time = −2556 × ln(1 − 0.01956) = 2556 × 0.01975 = 50.5 h. Check: without decay 3000 / 60 = 50.0 h; Ir-192 loses about 1% per day, so over two days the average dose rate is about 1% low and the time should be about 1% longer, which 50.5 h is. Option A ignores decay and underdoses by about 0.3 Gy. Option B shortens the time, the wrong direction for a weakening source. Option C doubles the time and would deliver nearly 60 Gy.

### Q4
Stem: Fraction one of an HDR vaginal cylinder course ran a total dwell time of 240 s. Fraction two uses the same plan and the same Ir-192 source 14 days later. The half-life is 73.8 days. What total dwell time does the afterloader need?
A. 274 s
B. 210 s
C. 240 s
D. 346 s
Answer: A
Objective: V.6
Why: Dose rate times time is constant for the same geometry, so the new time is the old time multiplied by e^(λΔt) with λΔt = 0.693 × 14 / 73.8 = 0.1315 and e^0.1315 = 1.140. Time = 240 × 1.140 = 274 s. Check: Ir-192 loses about 1% per day, so 14 days adds about 14%, and 240 × 1.14 = 274. Option B divides by the factor and would underdose the weaker source. Option C ignores decay. Option D multiplies by 1.443, the mean-life factor, which has no place in an HDR rescaling. For a Cs-137 source the same two-week gap would change the time by only about 0.09%, which is why Cs-137 times are rarely rescaled.

### Q5
Stem: A batch of seeds is assayed at 12.0 mCi. Twenty days later the same batch reads 5.31 mCi. What is the half-life of the nuclide?
A. 59.4 days
B. 24.5 days
C. 17.0 days
D. 39.1 days
Answer: C
Objective: V.6
Why: Half-life = 0.693 × Δt / ln(A1/A2) = 0.693 × 20 / ln(12.0/5.31) = 13.86 / ln(2.260) = 13.86 / 0.815 = 17.0 days, which identifies Pd-103. Check: 12.0 × e^(−0.693 × 20/17) = 12.0 × 0.4425 = 5.31 mCi. Option A is I-125, which would have decayed only to 9.5 mCi in 20 days. Option B omits the 0.693 and is the mean life, not the half-life. Option D uses a base-10 logarithm (log 2.260 = 0.354) in place of the natural log.

### Q6
Stem: A clinic has an 8.0 mCi I-125 seed with a half-life of 59.4 days and a 16.0 mCi Pd-103 seed with a half-life of 17.0 days in the same safe. After how many days will the two seeds have equal activity?
A. 17.0 days
B. 23.8 days
C. 59.4 days
D. 11.9 days
Answer: B
Objective: V.6
Why: The decay constants are 0.693/59.4 = 0.01167 per day for I-125 and 0.693/17.0 = 0.04077 per day for Pd-103. The activities are equal when t = ln(16/8) / (0.04077 − 0.01167) = 0.693 / 0.02910 = 23.8 days. Check: at 23.8 days the I-125 seed is 8 × e^(−0.278) = 6.06 mCi and the Pd-103 seed is 16 × e^(−0.970) = 6.06 mCi. Option A is one Pd-103 half-life, when the palladium is 8.0 mCi but the iodine has already fallen to 6.6 mCi, so they are not yet equal. Option C is the I-125 half-life. Option D is half the correct time. After the crossing the I-125 seed is the stronger one, which is why a shorter-lived nuclide must start hotter to deliver the same total dose.

### Q7
Stem: A permanent implant is prescribed to complete decay. What percentage of that total dose has been delivered after two half-lives?
A. 50%
B. 86%
C. 25%
D. 75%
Answer: D
Objective: V.6
Why: The delivered fraction is 1 − e^(−t/mean life) with mean life = 1.443 × half-life; at two half-lives the exponent is −2 × 0.693 = −1.386 and e^(−1.386) = 0.25, so 1 − 0.25 = 0.75, or 75%. Check: after each half-life the remaining dose halves, so 50% remains after one and 25% after two. Option A is the fraction after one half-life. Option C is the fraction still to be delivered, not the fraction delivered. Option B is what you get by putting the half-life instead of the mean life in the exponent (1 − e^(−2) = 86%), the usual wrong turn. Ninety percent of the total is reached after 2.303 mean lives, which is 3.32 half-lives.
