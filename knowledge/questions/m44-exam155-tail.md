# Module 44. Practice Test

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Timed Exam Calculation Safety and QA

### Q1
Stem: A point on a photon beam reads 320 cGy at 70 cm from the source. Only inverse square changes. What is the dose at 100 cm from the source?
A. 224.0 cGy
B. 156.8 cGy
C. 653.1 cGy
D. 96.0 cGy
Answer: B
Objective: IV
Why: Inverse square lowers the dose when the point moves farther from the source. Dose at the new distance = 320 × (70/100)^2 = 320 × 0.49 = 156.8 cGy. Check: 156.8 × (100/70)^2 = 320 cGy. Dropping the square and multiplying by 70/100 gives 224.0 cGy. Inverting the distances, (100/70)^2, gives 653.1 cGy and would raise the dose as the point moves out. Using the 30 cm gap as a fraction of 100 cm gives 96.0 cGy, which is not a distance from the source.

### Q2
Stem: SSD setup. The depth of maximum dose is 100 cm from the source, the same distance used for calibration. Calibration is 1.0 cGy/MU. The beam is open and every scatter factor is 1. The tumor dose is 150 cGy. The percent depth dose at the tumor is 75%. How many monitor units are required?
A. 112.5 MU
B. 2.0 MU
C. 225.0 MU
D. 200.0 MU
Answer: D
Objective: IV
Why: With dmax at the calibration distance, the inverse-square factor is 1, so MU = dose / (PDD/100) = 150 / 0.75 = 200.0 MU. Check: 200 × 0.75 = 150 cGy. Multiplying the dose by 0.75 answers the opposite question and gives 112.5 MU. Dividing by the percent number 75, instead of by 0.75, gives 2.0 MU. Adding 75 to 150 treats the percent as cGy and gives 225.0 MU.

### Q3
Stem: Isocentric setup. The calculation point is at isocenter, scatter and tray factors are 1, and the inverse-square factor from the calibration distance is 1. Calibration is 1.0 cGy/MU at dmax. A wedge of factor 0.500 is in the beam. TMR at the point is 0.800. The dose is 160 cGy. How many monitor units are required?
A. 400.0 MU
B. 200.0 MU
C. 100.0 MU
D. 123.1 MU
Answer: A
Objective: IV
Why: For an SAD calculation the depth quantity is TMR, and the wedge factor sits in the denominator. MU = 160 / (0.800 × 0.500) = 160 / 0.400 = 400.0 MU. Check: 400 × 0.800 × 0.500 = 160 cGy. Leaving the wedge out of the division gives 160 / 0.800 = 200.0 MU, and the wedge would then underdose the point. Putting the wedge factor in the numerator gives 160 × 0.500 / 0.800 = 100.0 MU. Adding the factors instead of multiplying them gives 160 / (0.800 + 0.500) = 123.1 MU.

### Q4
Stem: A rectangular photon field is 7 cm by 21 cm. What is the equivalent square used for a TMR or percent-depth-dose lookup?
A. 14.00 cm
B. 12.12 cm
C. 10.50 cm
D. 21.00 cm
Answer: C
Objective: IV
Why: Sterling’s equivalent square is 2ab/(a+b) = 2 × 7 × 21 / (7+21) = 294 / 28 = 10.50 cm. The perimeter form 4 × area / perimeter gives the same 10.50 cm. The arithmetic mean (7+21)/2 = 14.00 cm is not the scatter-equivalent square. The geometric mean, the square root of 7 × 21, is 12.12 cm and is a different average. Using 4ab/(a+b) doubles the equivalent square and gives 21.00 cm.

### Q5
Stem: Two photon fields are matched so the geometric edges meet at 10 cm depth. The field lengths on the skin, along the match, are 20 cm and 10 cm. Both source-to-skin distances are 100 cm. What skin gap separates the light fields?
A. 3.00 cm
B. 1.50 cm
C. 1.00 cm
D. 0.75 cm
Answer: B
Objective: IV
Why: Each light-field edge drifts sideways by half the skin length times depth over SSD. Gap = (20/2) × (10/100) + (10/2) × (10/100) = 1.00 + 0.50 = 1.50 cm. Check: 1.00 + 0.50 = 1.50. Using the full field lengths instead of the half-lengths gives 2.00 + 1.00 = 3.00 cm. Keeping only the first field gives 1.00 cm. Using a match depth of 5 cm instead of 10 cm gives 0.75 cm. The gap is the 50% geometric edge. It does not erase penumbra.

### Q6
Stem: A percent depth dose at 20 cm depth is 48% when the SSD is 100 cm. The depth of maximum dose is 1.5 cm. Estimate the percent depth dose at the same depth when the SSD is 160 cm, changing only the inverse-square piece of the percent depth dose.
A. 48.0%
B. 50.9%
C. 54.0%
D. 76.8%
Answer: C
Objective: IV
Why: Mayneord’s factor is [(SSD2+dmax)/(SSD1+dmax) × (SSD1+depth)/(SSD2+depth)]^2. Substitute [(160+1.5)/(100+1.5) × (100+20)/(160+20)]^2 = (161.5/101.5 × 120/180)^2 = (1.59113 × 0.66667)^2 = 1.06076^2 = 1.12520. New PDD = 48 × 1.12520 = 54.01%, reported as 54.0%. Leaving the PDD at 48.0% ignores the SSD change. Using the distance ratio once, without squaring, gives 50.9%. Scaling the PDD by 160/100 gives 76.8% and is not Mayneord’s factor. This factor does not correct scatter.

### Q7
Stem: An open beam delivers 250 cGy at the calculation point. The same point reads 175 cGy with the physical wedge in the beam. What is the wedge factor?
A. 0.700
B. 1.429
C. 0.875
D. 0.300
Answer: A
Objective: IV
Why: The wedge factor is the wedged reading divided by the open reading. 175 / 250 = 0.700. Check: 250 × 0.700 = 175 cGy. Inverting the ratio gives 250 / 175 = 1.429, which would be a factor greater than 1 for an attenuating wedge. Dividing the wedged reading by 200 instead of 250 gives 0.875. The fraction removed, (250 − 175) / 250 = 0.300, is the complement of the transmission factor, not the factor that belongs in the monitor-unit denominator.

### Q8
Stem: The dose on the central axis is 180 cGy. The off-axis ratio at the point of interest is 0.85. What is the dose at that off-axis point?
A. 180.0 cGy
B. 211.8 cGy
C. 130.1 cGy
D. 153.0 cGy
Answer: D
Objective: IV
Why: Off-axis dose = central-axis dose × off-axis ratio = 180 × 0.85 = 153.0 cGy. Check: 153.0 / 0.85 = 180. Reporting the central-axis dose unchanged gives 180.0 cGy. Dividing by the ratio answers the reverse question and gives 211.8 cGy. Squaring the ratio before multiplying gives 180 × 0.7225 = 130.1 cGy. Inverse square is a different correction and is not inside this ratio.

### Q9
Stem: At the depth of interest the zero-area tissue-air ratio is 0.380. The irregular field is one 120-degree sector with scatter-air ratio 0.150 and one 240-degree sector with scatter-air ratio 0.240. What is the tissue-air ratio of the whole field?
A. 0.770
B. 0.380
C. 0.590
D. 0.530
Answer: C
Objective: IV
Why: Clarkson weights each sector by its fraction of the circle, then adds the weighted scatter to the zero-area tissue-air ratio. The 120-degree sector is 120/360 = 1/3 of the circle, and the 240-degree sector is 2/3. Scatter = (1/3) × 0.150 + (2/3) × 0.240 = 0.050 + 0.160 = 0.210. Tissue-air ratio = 0.380 + 0.210 = 0.590. Check: 0.050 + 0.160 + 0.380 = 0.590. Adding both scatter-air ratios at full weight gives 0.770. Stopping at the zero-area value leaves the scatter out and gives 0.380. Adding only the smaller sector at full weight gives 0.530.

### Q10
Stem: A cobalt dose rate is 90.0 cGy/min at 120 cm from the source. Only inverse square changes. What is the dose rate at 80 cm from the source?
A. 202.5 cGy/min
B. 135.0 cGy/min
C. 40.0 cGy/min
D. 90.0 cGy/min
Answer: A
Objective: IV
Why: The point is moving closer, so the dose rate rises. Dose rate = 90.0 × (120/80)^2 = 90.0 × 2.25 = 202.5 cGy/min. Check: 202.5 × (80/120)^2 = 90.0 cGy/min. Dropping the square and multiplying by 120/80 gives 135.0 cGy/min. Using (80/120)^2 applies the farther-point factor and gives 40.0 cGy/min. Leaving the reading at 90.0 cGy/min ignores the distance change.

### Q11
Stem: SSD setup. SSD is 90 cm and the depth of maximum dose is 1.5 cm. Calibration is 1.0 cGy/MU at dmax for a 10 by 10 cm field at 100 cm SAD. Scatter, wedge, and tray factors are 1. The percent depth dose at the tumor is 80%. The tumor dose is 200 cGy. How many monitor units are required?
A. 250.0 MU
B. 209.3 MU
C. 298.6 MU
D. 160.0 MU
Answer: B
Objective: IV
Why: Dmax is closer than the calibration distance, so the inverse-square factor is (100 / (90+1.5))^2 = (100/91.5)^2 = 1.19442. MU = 200 / (0.80 × 1.19442) = 200 / 0.95554 = 209.3 MU. Check: 209.3 × 0.95554 = 200 cGy. Omitting that factor gives 200 / 0.80 = 250.0 MU, which is too many monitor units for a closer dmax. Inverting the distance ratio gives (91.5/100)^2 = 0.83723 and MU = 200 / (0.80 × 0.83723) = 298.6 MU. Multiplying the dose by 0.80 gives 160.0 MU and answers the opposite question.

### Q12
Stem: A ray to the calculation point crosses 4.0 cm of soft tissue at density 1.00, then 5.0 cm of lung at density 0.25, then 3.0 cm of soft tissue at density 1.00. What is the water-equivalent depth of that ray?
A. 12.0 cm
B. 7.00 cm
C. 9.50 cm
D. 8.25 cm
Answer: D
Objective: IV
Why: Water-equivalent depth adds physical thickness times density. 4.0 × 1.00 + 5.0 × 0.25 + 3.0 × 1.00 = 4.0 + 1.25 + 3.0 = 8.25 cm. Check: 4.0 + 3.0 + 1.25 = 8.25. The physical path 4 + 5 + 3 = 12.0 cm ignores density. Treating the lung as air, density 0, gives 7.00 cm. Using lung density 0.50 instead of the stated 0.25 gives 9.50 cm. This path length is not lateral scatter. A pencil beam can apply a path-length correction and still fail in lung.

### Q13
Stem: Two photon fields are matched so the geometric edges meet at 6 cm depth. Each field is 16 cm long on the skin along the match. One SSD is 100 cm and the other SSD is 120 cm. What skin gap separates the light fields?
A. 0.88 cm
B. 0.96 cm
C. 1.76 cm
D. 0.48 cm
Answer: A
Objective: IV
Why: Gap = (16/2) × (6/100) + (16/2) × (6/120) = 8 × 0.060 + 8 × 0.050 = 0.48 + 0.40 = 0.88 cm. Check: 0.48 + 0.40 = 0.88. Using 100 cm for both SSDs replaces the second term with another 0.48 cm and gives 0.96 cm. Using the full 16 cm lengths instead of the half-lengths gives 0.96 + 0.80 = 1.76 cm. Keeping only the 100 cm field gives 0.48 cm. A larger gap than 0.88 cm is cold at 6 cm. A smaller gap is hot there.

### Q14
Stem: TMR at 15 cm depth is 0.700 for the field size at that depth. SSD is 100 cm and dmax is 1.5 cm. Take the phantom-scatter ratio as 1. What percent depth dose corresponds to that TMR?
A. 70.0%
B. 61.8%
C. 54.5%
D. 89.9%
Answer: C
Objective: IV
Why: Percent depth dose = 100 × TMR × [(SSD+dmax)/(SSD+depth)]^2 when the phantom-scatter ratio is 1. The inverse-square piece is (101.5/115)^2 = 0.88261^2 = 0.77900. PDD = 100 × 0.700 × 0.77900 = 54.53%, reported as 54.5%. Check: 0.700 × 0.77900 = 0.5453. Reporting 100 × TMR gives 70.0% and drops inverse square. Using the distance ratio once, without squaring, gives 61.8%. Inverting the distances and squaring gives 89.9%, which can climb well above the TMR and is a sign the ratio was flipped.

### Q15
Stem: The given dose at dmax is 180 cGy. The surface dose is 25% of the dmax dose. What is the entrance dose?
A. 45.0 cGy
B. 180.0 cGy
C. 25.0 cGy
D. 72.0 cGy
Answer: A
Objective: IV
Why: Entrance dose is the stated surface percent of the given dose. 0.25 × 180 = 45.0 cGy. Check: 45.0 / 180 = 0.25. The given dose itself, 180.0 cGy, is the dmax dose, and the surface sits below dmax. Writing the percent number as cGy gives 25.0 cGy. Using 40% of the given dose gives 72.0 cGy, which is a different percent than the surface percent in the stem. Exit dose would use the percent depth dose at the exit depth, and that estimate still assumes tissue beyond the exit point.

### Q16
Stem: The jaws are set to 15 by 15 cm. A block trims the treated opening to 6 by 6 cm. Which quantities are looked up from the blocked opening?
A. Collimator scatter only
B. Phantom scatter and the tissue-maximum ratio
C. Collimator scatter together with the wedge factor
D. The calibration output, retaken for every block
Answer: B
Objective: IV
Why: Collimator scatter follows the jaws, because the head scatter is set by the collimator opening. Phantom scatter and TMR follow the field that actually irradiates the patient, here the 6 by 6 cm opening. The wedge factor is a measured transmission of the wedge, not a lookup on the blocked field. Calibration output stays at its stated condition. It is not remeasured for each block. Using the jaw field for TMR looks up too much scatter for the tissue that is actually treated.

### Q17
Stem: A lung plan needs the dose near the chest wall, where scatter from the neighboring soft tissue moves sideways. Which algorithm is the weak choice for that lateral scatter?
A. Monte Carlo with enough histories and the correct material
B. Convolution-superposition with a kernel that stretches in low density
C. Pencil beam
D. A grid-based Boltzmann solver with the correct material
Answer: C
Objective: IV
Why: A pencil beam applies heterogeneity mainly along each pencil and moves little energy sideways, so it is weak in lung near a soft-tissue boundary. Convolution-superposition stretches the scatter kernel when density falls, so lateral disequilibrium is handled more faithfully. A grid-based Boltzmann solver transports photons and electrons through the assigned material. Monte Carlo follows the interactions and is the strongest of these at an interface when the histories and the material are adequate. Calling a pencil-beam plan heterogeneity-corrected does not supply the missing lateral scatter.

### Q18
Stem: A serial organ is judged on a narrow maximum. The dose grid samples that region every 5 mm. What can that sampling do to the reported maximum?
A. Step over the peak and report a maximum lower than the true peak
B. Raise the dose that was actually delivered to the organ
C. Remove the need to correct for lung density
D. Turn a pencil-beam calculation into a Monte Carlo result
Answer: A
Objective: IV
Why: Dose is stored on the grid. A 5 mm step can miss a narrow peak and keep a lower neighboring sample as the reported maximum. The DVH then inherits that miss. The grid does not change the dose deposited in the patient. It does not correct lung density, and it does not replace the algorithm. A serial-organ maximum needs a fine grid, commonly on the order of 1 to 2 mm, before the reported maximum can be trusted.

### Q19
Stem: A new CT shows a smaller external contour after weight loss. The dose from the old plan is added onto the new CT with a rigid registration only. Which conclusion fits that sum?
A. The rigid sum is already a tissue-to-tissue accumulation
B. The old dose must be decayed before it is added, using a brachytherapy half-life
C. Overriding the external contour to water replaces the need to map tissue to tissue
D. The rigid copy can place the old dose on the wrong tissue once the contour has changed
Answer: D
Objective: IV
Why: Deformable accumulation maps a point in the old anatomy to the corresponding tissue on the new CT. After the external contour changes, a rigid copy can leave dose in air or on the wrong structure. Weight loss is not radioactive decay, so a source half-life does not adjust the old external-beam dose. A density override fixes a bad CT number. It does not move previously delivered dose onto the new anatomy. The rigid image match can still be useful for setup. It is not, by itself, the dose sum.

### Q20
Stem: The calculation point is at isocenter. The planner divides the prescribed dose by a percent depth dose taken from an SSD table. Which depth quantity belongs in this isocentric calculation?
A. That percent depth dose
B. The tissue-maximum ratio at the isocenter depth and field size
C. A Mayneord factor stacked on that percent depth dose
D. The surface-dose percent in place of any depth factor
Answer: B
Objective: IV
Why: An SAD calculation uses TMR (or TPR) at the point. With the point at isocenter the inverse-square term from the calibration distance is 1, and TMR carries the depth. A percent depth dose already includes inverse square for an SSD geometry and does not belong in this SAD line. Mayneord’s factor adjusts a percent depth dose from one SSD to another. It does not convert that PDD into the SAD depth factor. The surface percent estimates entrance dose. It is not the depth factor at isocenter.

### Q21
Stem: In the air-kerma strength unit used for brachytherapy sources, 1 U equals which value?
A. 1 µGy m²/h
B. 10 µGy m²/h
C. 0.01 µGy m²/h
D. 100 µGy m²/h
Answer: A
Objective: V
Why: Air-kerma strength is specified in U, and 1 U = 1 µGy m²/h. The factors 10, 0.01, and 100 move the power of ten. They are not the definition of U. U is not a second name for activity in millicuries, and it is not by itself the absorbed dose in gray at 1 cm.

### Q22
Stem: An I-125 eye plaque is prescribed to which dose at the apex?
A. 145 Gy
B. 85 Gy
C. 125 Gy
D. 170 Gy
Answer: B
Objective: V
Why: The I-125 plaque prescription used here is 85 Gy to the apex. 145 Gy is the I-125 prostate monotherapy prescription. 125 Gy is the Pd-103 monotherapy prescription. 170 Gy is twice the apex dose and is not the plaque prescription. The apex point is the plaque prescription point in this item, not a prostate volume.

### Q23
Stem: Permanent I-125 seeds used as prostate monotherapy are prescribed to which total dose?
A. 85 Gy
B. 125 Gy
C. 170 Gy
D. 145 Gy
Answer: D
Objective: V
Why: I-125 monotherapy is 145 Gy. 85 Gy is the I-125 eye-plaque dose to the apex, not the prostate monotherapy dose. 125 Gy is the Pd-103 monotherapy dose. 170 Gy is not the I-125 monotherapy prescription. The two I-125 prescriptions stay apart: 145 Gy for prostate monotherapy, 85 Gy to the apex of an eye plaque.

### Q24
Stem: Permanent Pd-103 seeds used as prostate monotherapy are prescribed to which total dose?
A. 145 Gy
B. 85 Gy
C. 125 Gy
D. 62.5 Gy
Answer: C
Objective: V
Why: Pd-103 monotherapy is 125 Gy. 145 Gy is I-125 monotherapy. 85 Gy is the I-125 plaque dose to the apex. Half of 125 Gy is 62.5 Gy, and that half is not the Pd-103 prescription. Pd-103 and I-125 monotherapy are different totals.

### Q25
Stem: A brachytherapy patient may be released when the total effective dose equivalent to any other individual is not likely to exceed which value?
A. 5 mSv
B. 50 mSv
C. 1 mSv
D. 0.02 mSv
Answer: A
Objective: V
Why: The patient-release criterion used here is 5 mSv to any other individual. 50 mSv is the adult occupational TEDE limit, not the release criterion. 1 mSv is the annual public limit. 0.02 mSv is the public limit in any one hour from external sources in an unrestricted area. Release compares the likely dose to another person with 5 mSv.

### Q26
Stem: Which value is the mean photon energy used here for an Ir-192 HDR source?
A. about 38 keV
B. about 190 keV
C. about 380 keV
D. about 760 keV
Answer: C
Objective: V
Why: The Ir-192 mean photon energy used here is about 380 keV. About 190 keV is half of that mean. About 760 keV is twice that mean. About 38 keV is a tenth of that mean. None of those scaled values replaces about 380 keV for Ir-192.

### Q27
Stem: Which pairing agrees with the prescriptions used here?
A. An I-125 eye plaque is prescribed to 145 Gy at the apex
B. I-125 monotherapy is prescribed to 85 Gy
C. Pd-103 monotherapy is prescribed to 125 Gy
D. An I-125 eye plaque is prescribed to 125 Gy at the apex
Answer: C
Objective: V
Why: Pd-103 monotherapy is 125 Gy. An I-125 eye plaque is 85 Gy to the apex, so 145 Gy and 125 Gy are the wrong apex totals. I-125 monotherapy is 145 Gy, so 85 Gy is the plaque number placed on the wrong technique. The three totals stay attached to their own techniques: plaque 85 Gy at the apex, I-125 monotherapy 145 Gy, Pd-103 monotherapy 125 Gy.

### Q28
Stem: Which statement defines the quantity specified by U?
A. U is the source activity in millicuries
B. U is air-kerma strength, and 1 U is 1 µGy m²/h
C. U is absorbed dose in water, in gray, at 1 cm
D. U is the public dose in one hour, 0.02 mSv
Answer: B
Objective: V
Why: U specifies air-kerma strength. The equality used here is 1 U = 1 µGy m²/h. Activity in millicuries is a different label and is not the definition of U. Absorbed dose at 1 cm still needs the TG-43 factors. It is not what the symbol U already is. The public hourly limit, 0.02 mSv, is a protection limit, not a source-strength unit.

### Q29
Stem: The adult occupational total effective dose equivalent limit is which value?
A. 5 mSv in a year
B. 1 mSv in a year
C. 0.02 mSv in any one hour
D. 50 mSv in a year
Answer: D
Objective: VI
Why: The adult occupational TEDE limit used here is 50 mSv in a year. 5 mSv is the adult badge trigger, 10 percent of 50 mSv, and it is not the TEDE ceiling. 1 mSv is the annual public limit. 0.02 mSv is the public limit in any one hour. A reading under 50 mSv can still fail ALARA. The ceiling and the badge trigger are different sentences.

### Q30
Stem: The annual dose limit for a member of the public is which value?
A. 1 mSv
B. 50 mSv
C. 5 mSv
D. 0.02 mSv
Answer: A
Objective: VI
Why: A member of the public is limited to 1 mSv in a year. 50 mSv is the adult occupational TEDE limit. 5 mSv is the adult monitoring threshold, not the public annual limit. 0.02 mSv is the public limit in any one hour, not the annual total. The year and the hour are separate tests.

### Q31
Stem: From external sources in an unrestricted area, the public dose limit in any one hour is which value?
A. 1 mSv
B. 0.02 mSv
C. 0.20 mSv
D. 50 mSv
Answer: B
Objective: VI
Why: The public hourly limit used here is 0.02 mSv in any one hour. 1 mSv is the annual public limit, not the limit for one hour. 0.20 mSv is ten times the hourly limit. 50 mSv is the adult occupational TEDE limit for a year. An hour that reaches 0.02 mSv has used the whole hourly allowance even when the year’s sum is still under 1 mSv.

### Q32
Stem: An adult is monitored with a badge when the likely annual total effective dose equivalent exceeds which value?
A. 50 mSv
B. 1 mSv
C. 5 mSv
D. 0.02 mSv
Answer: C
Objective: VI
Why: The adult badge trigger used here is 5 mSv in a year. That is 10 percent of the 50 mSv TEDE limit: 0.10 × 50 = 5. Waiting until the badge already reads 50 mSv misses the prospective trigger. 1 mSv is the annual public limit, not the adult badge threshold. 0.02 mSv is the public limit in one hour. The 5 mSv figure decides whether to badge an adult. It is not a second name for the 50 mSv ceiling.

### Q33
Stem: The public annual limit is 1 mSv and the public limit in any one hour is 0.02 mSv. A person receives 1 mSv in a single hour. How many times the hourly limit is that hour?
A. 50 times
B. 5 times
C. 2 times
D. 500 times
Answer: A
Objective: VI
Why: Divide the hour by the hourly limit: 1 / 0.02 = 50. That hour is 50 times 0.02 mSv, and it also equals the entire annual public limit of 1 mSv. Check: 50 × 0.02 = 1.00 mSv. Using the 5 mSv badge trigger in the numerator, 5 / 1, gives 5 times and answers a different ratio. Halving the result gives 2 times. Moving the hourly limit’s decimal to 0.002 gives 500 times.

### Q34
Stem: The adult badge trigger is 5 mSv. The adult TEDE limit is 50 mSv. The trigger is what percent of that limit?
A. 1%
B. 5%
C. 20%
D. 10%
Answer: D
Objective: VI
Why: Percent = 5 / 50 × 100 = 10%. Check: 0.10 × 50 = 5 mSv. 1% of 50 mSv would be 0.5 mSv, not the 5 mSv trigger. 5% of 50 mSv would be 2.5 mSv. 20% of 50 mSv would be 10 mSv. The monitoring sentence is the 10% sentence, which is 5 mSv, and the occupational ceiling remains 50 mSv.

### Q35
Stem: For a secondary barrier, head leakage at 1 m is what fraction of the useful beam?
A. 1% of the useful beam
B. 0.1% of the useful beam
C. 10% of the useful beam
D. 0.01% of the useful beam
Answer: B
Objective: VI
Why: Head leakage at 1 m is 0.1% of the useful beam, a fraction of 0.001. As a percent, 1% is ten times that leakage, and 10% is one hundred times it. 0.01% is a tenth of the leakage fraction used here. Leakage is present whenever the beam is on, so its use factor is 1. Patient scatter is a separate term and is not created by changing 0.1% to another percent.

### Q36
Stem: The useful beam delivers 1 mSv at 1 m from the source. What head-leakage dose at that same 1 m distance goes with a secondary barrier?
A. 0.010 mSv
B. 0.100 mSv
C. 0.001 mSv
D. 0.0001 mSv
Answer: C
Objective: VI
Why: Leakage at 1 m is 0.1% of the useful beam, which is the fraction 0.001. Leakage dose = 1 × 0.001 = 0.001 mSv. Check: 0.001 / 1 = 0.001 = 0.1%. Using 1% gives 0.010 mSv. Using 10% gives 0.100 mSv. Using 0.01% gives 0.0001 mSv. This 0.001 mSv is the leakage term at 1 m. It is not the public hourly limit, and it is not the shielded dose behind the barrier.

### Q37
Stem: No tenth-value layer is printed on the problem. For ordinary concrete, the teaching TVL at 6 MV is about which thickness?
A. about 35 cm
B. about 45 cm
C. about 70 cm
D. about 3.5 cm
Answer: A
Objective: VI
Why: When the stem gives no TVL, ordinary concrete at 6 MV is about 35 cm per tenth-value layer. About 45 cm is the teaching TVL at 18 MV. About 70 cm is two layers at 6 MV, not one. About 3.5 cm moves the decimal. Use a TVL printed in the problem when one is given. The 35 cm figure is the fallback for 6 MV.

### Q38
Stem: No tenth-value layer is printed on the problem. For ordinary concrete, the teaching TVL at 18 MV is about which thickness?
A. about 35 cm
B. about 90 cm
C. about 4.5 cm
D. about 45 cm
Answer: D
Objective: VI
Why: When the stem gives no TVL, ordinary concrete at 18 MV is about 45 cm per tenth-value layer. About 35 cm is the 6 MV teaching value. About 90 cm is two layers at 18 MV. About 4.5 cm moves the decimal. A 6 MV wall designed with 45 cm, or an 18 MV wall designed with 35 cm, uses the other energy’s TVL.

### Q39
Stem: The problem prints no tenth-value layer. The beam is 6 MV, and the concrete must provide 3 tenth-value layers. What thickness of ordinary concrete does that energy call for?
A. about 70 cm
B. about 105 cm
C. about 90 cm
D. about 135 cm
Answer: B
Objective: VI
Why: The 6 MV teaching TVL is about 35 cm. Three layers are 3 × 35 = 105 cm. Check: 105 / 35 = 3. Two layers at 6 MV are 2 × 35 = 70 cm. Two layers at the 18 MV value are 2 × 45 = 90 cm. Three layers at 45 cm are 135 cm, which applies the 18 MV TVL to a 6 MV beam. Thickness is the layer count times the TVL for that energy.

### Q40
Stem: The problem prints no tenth-value layer. The beam is 18 MV, and the concrete must provide 2 tenth-value layers. What thickness of ordinary concrete does that energy call for?
A. about 70 cm
B. about 45 cm
C. about 90 cm
D. about 35 cm
Answer: C
Objective: VI
Why: The 18 MV teaching TVL is about 45 cm. Two layers are 2 × 45 = 90 cm. Check: 90 / 45 = 2. Two layers at the 6 MV value are 2 × 35 = 70 cm. One 18 MV layer is about 45 cm, and one 6 MV layer is about 35 cm. Stopping at a single TVL leaves the second factor of ten unshielded.

### Q41
Stem: Which statement is the pair of public dose limits used here?
A. The public limits are 1 mSv in a year and 0.02 mSv in any one hour
B. The public limits are 50 mSv in a year and 0.02 mSv in any one hour
C. The public limits are 1 mSv in a year and 1 mSv in any one hour
D. The public limits are 5 mSv in a year and 0.02 mSv in any one hour
Answer: A
Objective: VI
Why: The public pair used here is 1 mSv in a year and 0.02 mSv in any one hour. 50 mSv is the adult occupational TEDE limit. Putting 1 mSv in a single hour replaces the hourly cap with the annual cap. 5 mSv is the adult badge trigger, not the public annual limit. Both public tests have to be named. Passing the year does not waive the hour, and passing one hour does not waive the year.

### Q42
Stem: A wall is never struck by the useful beam. It is shielded for head leakage. Which description matches that wall?
A. A primary barrier sized to the full useful-beam workload aimed at that wall
B. A secondary barrier, with head leakage at 1 m equal to 0.1% of the useful beam
C. A primary barrier whose leakage specification is 10% of the useful beam at 1 m
D. A wall that needs neither a leakage term nor a use factor
Answer: B
Objective: VI
Why: A secondary barrier is the wall the useful beam does not strike. Head leakage at 1 m is 0.1% of the useful beam, and the leakage use factor is 1 because leakage exists whenever the beam is on. A primary barrier is the wall that intercepts the useful beam, so the full useful-beam workload and that wall’s use factor belong there. 10% is not the leakage fraction. Dropping the leakage term leaves the secondary wall unshielded for radiation that is present every time the beam is on. Patient scatter, if the problem includes it, is an additional term.

### Q43
Stem: On the TG-142 schedule used here, daily x-ray output constancy is about which tolerance?
A. 1%
B. 3%
C. 2%
D. 5%
Answer: B
Objective: VII
Why: Daily output constancy is about 3%. Monthly output constancy is about 2%, and the annual absolute calibration is about 1%. 5% is looser than the daily window used here. A morning reading inside 3% can still sit outside the monthly 2% window, so the same percent is compared with the check that was actually performed.

### Q44
Stem: On the TG-142 schedule used here, monthly x-ray output constancy is about which tolerance?
A. 1%
B. 3%
C. 2%
D. 4%
Answer: C
Objective: VII
Why: Monthly output constancy is about 2%. About 3% is the daily constancy tolerance. About 1% is the annual absolute calibration. About 4% is wider than the monthly window. The monthly check is tighter than the morning check and looser than the annual calibration.

### Q45
Stem: On the TG-142 schedule used here, annual x-ray output calibration is about which tolerance?
A. 1%
B. 3%
C. 2%
D. 0.5%
Answer: A
Objective: VII
Why: The annual absolute output calibration is about 1%. About 3% is daily constancy and about 2% is monthly constancy. About 0.5% is tighter than the annual tolerance used here. The annual check is the absolute calibration. Daily and monthly checks are constancy against that baseline.

### Q46
Stem: The optical distance indicator tolerance used with TG-142 here is which value?
A. 1 mm
B. 5 mm
C. 20 mm
D. 2 mm
Answer: D
Objective: VII
Why: The ODI tolerance used here is 2 mm. 1 mm is the SRS laser tolerance and the Winston-Lutz result used here, not the ODI tolerance. 5 mm is wider than 2 mm. 20 mm is 2 cm, which confuses the unit and would accept an optical distance that is far outside 2 mm. An ODI error is compared with 2 mm before the distance is used to set the patient up.

### Q47
Stem: For a non-SRS treatment unit, the laser tolerance used with TG-142 here is which value?
A. 1 mm
B. 2 mm
C. 5 mm
D. 20 mm
Answer: B
Objective: VII
Why: Non-SRS lasers are held to 2 mm in this set. 1 mm is the SRS laser tolerance. 5 mm and 20 mm are wider than the non-SRS laser tolerance. The ODI tolerance is also 2 mm, but it is a separate check from the lasers. An SRS unit does not stay on this 2 mm laser line.

### Q48
Stem: For SRS, the laser tolerance used with TG-142 here is which value?
A. 1 mm
B. 2 mm
C. 0.5 mm
D. 5 mm
Answer: A
Objective: VII
Why: SRS lasers are held to 1 mm in this set. 2 mm is the non-SRS laser tolerance and the ODI tolerance. 0.5 mm is tighter than the SRS laser tolerance used here. 5 mm is wider than both laser lines. The SRS laser check and the Winston-Lutz check both use 1 mm, and they are still different tests.

### Q49
Stem: A Winston-Lutz check of the radiation isocenter, as used here, should fall at which result?
A. at or under 2 mm
B. at or under 5 mm
C. at or under 1 mm
D. at or under 0.5 mm
Answer: C
Objective: VII
Why: The Winston-Lutz result used here is at or under 1 mm. At or under 2 mm matches the ODI and the non-SRS lasers, not this isocenter test. At or under 5 mm is wider than 1 mm. At or under 0.5 mm is tighter than the criterion used here. A Winston-Lutz result of 1.5 mm would fail the 1 mm line even though 1.5 mm is under the 2 mm ODI tolerance.

### Q50
Stem: On the total-dose test used here, a medical event is a delivered dose that differs from the prescribed total by about which amount?
A. 5% of the total dose
B. 10% of the total dose
C. 50% of the total dose
D. 20% of the total dose
Answer: D
Objective: VII
Why: The total-dose medical-event test used here is about 20% of the prescribed total. About 50% is the single-fraction test, not the total-dose test. About 5% and about 10% are tighter than the total-dose line used here. A 20% miss of the whole course and a 50% miss of one fraction are different comparisons. The report clocks are the same once either test is met: verbal in about 24 hours and written in about 15 days.

### Q51
Stem: On the single-fraction test used here, a medical event is a delivered fraction that differs from the prescribed fraction by about which amount?
A. 50% of that fraction
B. 20% of that fraction
C. 10% of that fraction
D. 100% of that fraction
Answer: A
Objective: VII
Why: The single-fraction medical-event test used here is about 50% of the prescribed fraction. About 20% is the total-dose test. About 10% is tighter than the fraction test used here. About 100% of the fraction is a larger miss than the 50% line. One fraction can trip the 50% test even when the course total is still inside 20%, and the course total can trip the 20% test even when no single fraction reached 50%.

### Q52
Stem: After a medical event is discovered, the verbal report to the regulator is due in about which interval?
A. 1 hour
B. 24 hours
C. 12 hours
D. 48 hours
Answer: B
Objective: VII
Why: The verbal report used here is due in about 24 hours. About 1 hour and about 12 hours are sooner than that verbal interval. About 48 hours is later than the verbal interval used here. The written report is a second clock, about 15 days, and it does not replace the verbal report. A voluntary incident-learning submission does not replace either regulatory clock.

### Q53
Stem: After a medical event is discovered, the written report is due in about which interval?
A. 1 day
B. 7 days
C. 30 days
D. 15 days
Answer: D
Objective: VII
Why: The written report used here is due in about 15 days. About 1 day is closer to the verbal clock than to the written clock. About 7 days and about 30 days are not the written interval used here. The verbal report, about 24 hours, still has to be made. Filing the written report on day 15 does not erase a verbal report that was already due.

### Q54
Stem: Morning output constancy. The baseline is 1.000 cGy/MU and the measurement is 1.034 cGy/MU. What is the percent deviation from baseline?
A. 3.4%
B. 1.034%
C. 34%
D. 0.34%
Answer: A
Objective: VII
Why: Percent deviation = (measured − baseline) / baseline × 100 = (1.034 − 1.000) / 1.000 × 100 = 3.4%. Check: 1.000 × 1.034 = 1.034. Reporting the measurement itself as a percent gives 1.034%. Moving the decimal of 0.034 one place to the right gives 34%. Moving it one place to the left gives 0.34%. Against the tolerances used here, 3.4% is outside the daily window of about 3%, outside the monthly window of about 2%, and outside the annual window of about 1%.

### Q55
Stem: The mechanical distance is 100.0 cm. The optical distance indicator reads 98.2 cm. What is the absolute ODI error in millimeters?
A. 1.8 mm
B. 18 mm
C. 2 mm
D. 180 mm
Answer: B
Objective: VII
Why: The difference is 100.0 − 98.2 = 1.8 cm. In millimeters, 1.8 × 10 = 18 mm. Check: 18 mm = 1.8 cm. Keeping the 1.8 and calling it millimeters gives 1.8 mm. The 2 mm figure is the ODI tolerance, not this error. Multiplying 1.8 cm by 100 instead of by 10 gives 180 mm. The error of 18 mm is outside the 2 mm ODI tolerance, so the optical distance fails even though the arithmetic starts from a 1.8 cm gap.

### Q56
Stem: The delivered total dose differs from the prescribed total by about 20%. The miss is discovered today. Which report timing matches the medical-event clocks used here?
A. No regulatory report, because about 20% applies only to a single fraction
B. A verbal report in about 15 days and a written report in about 24 hours
C. A verbal report in about 24 hours and a written report in about 15 days
D. A written report in about 24 hours, with no verbal report
Answer: C
Objective: VII
Why: About 20% of the prescribed total meets the total-dose test used here, so the event is reportable. The verbal report is due in about 24 hours and the written report is due in about 15 days. About 50% is the single-fraction test. It is not the only way to meet the definition, and a 20% total miss is not excused by that fraction test. Swapping the clocks, or dropping the verbal report, leaves the wrong action on the wrong timer. A voluntary learning report can still be filed. It does not take the place of these two regulatory clocks.
