# Module 36. Special calculations

Original items. Extended-distance and asymmetric geometry, the orthovoltage timer chain, attenuation from a mass attenuation coefficient and from two readings, mixed-radiation dose equivalent, line versus point sources, CSI angles with the spine junction, and the density and temperature tables used inside calculations.

## Extended-Distance and Asymmetric Field Geometry

### Q1
Stem: A hemibody field must be 150 cm long at the patient, who is treated at 400 cm from the source. The collimator readout is defined at 100 cm from the source. What collimator setting is required?
A. 600 cm
B. 150 cm
C. 37.5 cm
D. 30.0 cm
Answer: C
Objective: IV.3
Why: A collimator reading is the field length at 100 cm, so the required length at 400 cm must be scaled back by 100/400: 150 × 100/400 = 37.5 cm. Check: 37.5 cm at 100 cm projects to 37.5 × 4 = 150 cm at 400 cm, and the setting is within the 40 cm jaw limit. Multiplying by the distance ratio instead of dividing gives 600 cm. Copying the patient length onto the readout gives 150 cm. Using 500 cm as the treatment distance gives 30.0 cm.

### Q2
Stem: A total-body patient is 180 cm long and is treated at 400 cm from the source. The straight collimator setting that would be required exceeds the 40 cm jaw limit, so the collimator is rotated 45 degrees and the diagonal of a square field is used to span the patient. What square field side is needed, to the nearest 0.1 cm?
A. 31.8 cm
B. 45.0 cm
C. 63.6 cm
D. 22.5 cm
Answer: A
Objective: IV.3
Why: The length to span at 100 cm is 180 × 100/400 = 45.0 cm, which is more than 40 cm. The diagonal of a square is the side times the square root of 2, so the side is 45.0/1.414 = 31.8 cm. Check: 31.8 × 1.414 = 45.0 cm at 100 cm, projecting to 180 cm at 400 cm. The 45.0 cm value is the straight setting, which does not fit the jaws. Multiplying by the square root of 2 gives 63.6 cm, which is even further outside the limit. Halving 45 cm gives 22.5 cm, whose diagonal spans only 127 cm at the patient.

### Q3
Stem: An asymmetric field has jaw X1 at 8 cm, X2 at 4 cm, Y1 at 3 cm, and Y2 at 11 cm, each measured from the central axis. How far from the central axis is the center of the open field, to the nearest 0.1 cm?
A. 6.0 cm
B. 2.0 cm
C. 8.9 cm
D. 4.5 cm
Answer: D
Objective: IV.3
Why: The center is offset by half the difference of each jaw pair: (8 − 4)/2 = 2 cm in X and (11 − 3)/2 = 4 cm in Y. The radius is the hypotenuse, the square root of 2² + 4² = 20, which is 4.47 cm, reported as 4.5 cm. Check: 4.47 squared is 20. Adding the two offsets gives 6.0 cm, which is not a straight-line distance. Using only the X offset gives 2.0 cm. Using the full jaw differences, the square root of 4² + 8², gives 8.9 cm.

### Q4
Stem: Two posterior fields are to meet at 8 cm depth. Field 1 is 24 cm long on the skin with the skin at 100 cm from the source. Field 2 has a collimator reading of 14 cm and is set with the skin at 125 cm from the source. What skin gap is required, to the nearest 0.01 cm?
A. 1.66 cm
B. 1.52 cm
C. 1.41 cm
D. 3.04 cm
Answer: B
Objective: IV.3
Why: The collimator reading is the length at 100 cm, so the field 2 skin length at 125 cm is 14 × 125/100 = 17.5 cm. Gap = half of 24 times 8/100 plus half of 17.5 times 8/125 = 0.96 + 0.56 = 1.52 cm. Check: the second term also equals half the 14 cm reading times 8/100 = 0.56 cm, because the projection factor and the SSD cancel. Using 14 cm as if it were the skin length at 125 cm gives 0.96 + 0.45 = 1.41 cm. Using the 17.5 cm skin length but an SSD of 100 cm for field 2 gives 0.96 + 0.70 = 1.66 cm. Using full lengths instead of half lengths gives 3.04 cm.

## Orthovoltage Timer Chain

### Q1
Stem: An orthovoltage unit is calibrated to 120 roentgen per minute in air at 50 cm. A lesion is treated at 55 cm source-to-skin distance with a prescription of 300 cGy at 3 cm depth. The roentgen-to-cGy factor is 0.94, the backscatter factor is 1.20, and the percent depth dose at 3 cm is 70 percent. Ignoring timer error, what treatment time is required, to the nearest 0.01 minute?
A. 3.17 min
B. 3.83 min
C. 4.60 min
D. 5.52 min
Answer: B
Objective: IV.3
Why: Move the exposure rate to 55 cm with inverse square, 120 × (50/55)² = 99.17 R/min; convert to cGy, 99.17 × 0.94 = 93.22; add backscatter, 93.22 × 1.20 = 111.87 cGy/min at the surface; apply PDD, 111.87 × 0.70 = 78.31 cGy/min at 3 cm. Time = 300/78.31 = 3.83 min. Check: 78.31 × 3.83 = 300 cGy. Skipping inverse square gives 300/(120 × 0.94 × 1.20 × 0.70) = 3.17 min. Leaving out the backscatter factor gives 4.60 min and a 20% overdose. Dividing by the backscatter factor gives 5.52 min.

### Q2
Stem: An orthovoltage prescription is 300 cGy at 3 cm depth, where the percent depth dose is 70 percent and the backscatter factor is 1.20. What dose does the skin surface receive during that treatment, to the nearest 0.1 cGy?
A. 360.0 cGy
B. 300.0 cGy
C. 357.1 cGy
D. 428.6 cGy
Answer: D
Objective: IV.3
Why: For orthovoltage the surface is dmax, so the surface dose is the depth dose divided by the PDD fraction: 300/0.70 = 428.6 cGy. Check: 428.6 × 0.70 = 300 cGy. The backscatter factor is already inside the surface dose rate used to compute the time and is not applied again here. Multiplying 300 by 1.20 gives 360.0 cGy, which applies backscatter to a depth dose. Reporting 300.0 cGy assumes skin sparing, which orthovoltage does not have. Dividing by both 0.70 and 1.20 gives 357.1 cGy and removes backscatter that the surface actually receives.

## Attenuation From Mass Attenuation Coefficient and Two Intensities

### Q1
Stem: A lead sheet is 0.2 cm thick. At the beam energy in question the mass attenuation coefficient of lead is 0.60 square centimeters per gram and its density is 11.35 grams per cubic centimeter. Under narrow-beam conditions, what percentage of the beam is transmitted, to the nearest 0.1 percent?
A. 25.6 percent
B. 74.4 percent
C. 88.7 percent
D. 0.1 percent
Answer: A
Objective: I.10
Why: The linear attenuation coefficient is the mass coefficient times the density, 0.60 × 11.35 = 6.81 per centimeter. The exponent is 6.81 × 0.2 = 1.362, and e to the minus 1.362 is 0.256, so 25.6 percent is transmitted. Check: the HVL is 0.693/6.81 = 0.102 cm, the sheet is 1.97 HVL, and one half to the power 1.97 is 0.256. The 74.4 percent figure is the attenuated fraction, not the transmitted one. Forgetting the density, e to the minus 0.60 × 0.2, gives 88.7 percent. Forgetting the thickness, e to the minus 6.81, gives 0.1 percent.

### Q2
Stem: A survey reading of 250 mR per hour falls to 40 mR per hour after 1.5 cm of a shielding material is inserted. What is the half-value layer of that material, to the nearest 0.001 cm?
A. 0.240 cm
B. 0.847 cm
C. 0.567 cm
D. 0.750 cm
Answer: C
Objective: I.10
Why: The natural log of the intensity ratio, ln(250/40) = ln 6.25 = 1.833, equals the linear coefficient times the thickness, so the coefficient is 1.833/1.5 = 1.222 per centimeter and the HVL is 0.693/1.222 = 0.567 cm. Check: 1.5 cm is 2.64 HVL, and one half to the power 2.64 is 0.160, which is 40/250. Dividing the thickness by the ratio 6.25 gives 0.240 cm and treats attenuation as linear. Multiplying 0.693 by the coefficient instead of dividing gives 0.847 cm. Halving the thickness gives 0.750 cm, which assumes the reading fell by exactly half.

### Q3
Stem: A shield material has a half-value layer of 6 mm for the beam in question. What thickness reduces the transmitted intensity to 5 percent of the incident value, to the nearest 0.1 mm?
A. 18.0 mm
B. 25.9 mm
C. 30.0 mm
D. 19.9 mm
Answer: B
Objective: VI.3
Why: Five percent transmission is a reduction by a factor of 20, which is log base 2 of 20 = 4.32 half-value layers, so the thickness is 4.32 × 6 = 25.9 mm. Check: one half to the power 4.32 is 0.050. Three HVL, 18.0 mm, transmits 12.5 percent. Five HVL, 30.0 mm, transmits about 3.1 percent and comes from reading "5 percent" as "5 layers." One tenth-value layer, 3.32 HVL or 19.9 mm, transmits 10 percent, not 5 percent.

## Mixed-Radiation Dose Equivalent

### Q1
Stem: A survey outside a high-energy treatment vault attributes an absorbed dose of 0.20 cGy to photons, 0.03 cGy to fast neutrons, and 0.01 cGy to alpha-emitting contamination. The survey assigns a radiation weighting factor of 1 to the photons and 20 to both the neutrons and the alpha particles. What is the total equivalent dose?
A. 2.4 mSv
B. 48 mSv
C. 10 mSv
D. 8 mSv
Answer: C
Objective: VI.3
Why: Weight each absorbed dose by its own factor and add: 0.20 × 1 + 0.03 × 20 + 0.01 × 20 = 0.20 + 0.60 + 0.20 = 1.00 cSv, which is 10 mSv. Check: the neutron term alone is 0.60 cSv, three times the photon term despite a smaller absorbed dose. Adding the absorbed doses without weights gives 0.24 cGy, or 2.4 mSv, which is not an equivalent dose. Applying the factor of 20 to every component gives 4.8 cSv or 48 mSv. Dropping the alpha term gives 0.80 cSv or 8 mSv.

## Line Source Versus Point Source

### Q1
Stem: A 10 cm long linear brachytherapy source gives a reading of 120 mR per hour at 0.5 cm from its midpoint. Estimate the reading at 2 cm from the midpoint, using the rule appropriate for points much closer than the source length.
A. 7.5 mR/h
B. 60 mR/h
C. 480 mR/h
D. 30 mR/h
Answer: D
Objective: IV.3
Why: Close to a long line source the exposure falls as one over the distance, not one over the distance squared, so 120 × (0.5/2) = 30 mR/h. Check: both distances are far smaller than the 10 cm length, so the near-field rule applies, and inverse square would only take over beyond roughly twice the length, about 20 cm. Using inverse square gives 120 × (0.5/2)² = 7.5 mR/h, a factor of four too low. Halving the reading gives 60 mR/h, which corresponds to doubling the distance, not quadrupling it. Inverting the ratio gives 480 mR/h.

### Q2
Stem: A linear source has an active length of 4 cm. Beyond roughly what distance from its center can its exposure rate be estimated with the point-source inverse-square law?
A. 8 cm
B. 4 cm
C. 2 cm
D. 16 cm
Answer: A
Objective: IV.3
Why: The usual teaching rule is that a line source behaves as a point source beyond about twice its active length, so for a 4 cm source the crossover is near 8 cm. Check: at 8 cm the ends of the source are only about 3 percent farther away than the center, so their contributions are nearly those of a point. At the full length, 4 cm, the end-to-center distance difference is still about 12 percent and inverse square overstates the fall-off. At half the length, 2 cm, the near-field one-over-distance behavior still dominates. Four times the length, 16 cm, is safely in the point-source region but is not the rule-of-thumb boundary.

## CSI Angles and the Spine Junction

### Q1
Stem: A craniospinal plan uses a posterior spine field 36 cm long at isocenter and lateral brain fields 20 cm long at isocenter, all at 100 cm source-to-axis distance. What collimator rotation is applied to the lateral brain fields so their inferior edges match the diverging superior edge of the spine field, to the nearest 0.1 degree?
A. 5.7 degrees
B. 10.2 degrees
C. 19.8 degrees
D. 79.8 degrees
Answer: B
Objective: IV.3
Why: The collimator of the brain fields follows the spine field's divergence, so the angle is the arctangent of half the spine length over the SAD: arctan(18/100) = 10.2 degrees. Check: tan 10.2 degrees = 0.180. Using half the brain field length, arctan(10/100) = 5.7 degrees, is the couch kick for the brain fields, not the collimator angle. Using the full spine length, arctan(36/100), gives 19.8 degrees. Flipping the triangle, arctan(100/18), gives 79.8 degrees.

### Q2
Stem: A tall patient's spine requires two posterior fields that must be gapped on the skin. At what depth should the geometric edges of the two spine fields be calculated to meet?
A. At the skin surface, so no gap is needed
B. At the posterior surface of the spinal cord
C. At the anterior surface of the spinal cord, so any overlap lies anterior to the cord in the vertebral body
D. At the patient midplane, as for any opposed pair
Answer: C
Objective: IV.3
Why: The gap is calculated so the field edges meet at the anterior aspect of the spinal cord; beyond the match depth the fields overlap, and placing that overlap anterior to the cord keeps the hot triangle in the vertebral body while the cord sits in the matched or slightly cold zone. Matching on the skin leaves the edges overlapping at every depth, including the cord. Matching at the posterior cord surface puts the cord itself inside the overlap. A spine pair is two adjacent fields in the same direction, not an opposed pair, so midplane is not the relevant depth.

## Density Table and Fahrenheit Temperature Correction

### Q1
Stem: A treatment plan lists these relative densities for its override table: lung 0.30, fat 0.95, muscle 1.05, and cortical bone 1.10. Which assignment is wrong?
A. Lung 0.30
B. Fat 0.95
C. Muscle 1.05
D. Cortical bone 1.10
Answer: D
Objective: IV.3
Why: Cortical bone has a relative density of about 1.65 to 1.85; a value near 1.1 describes trabecular or soft bone. Check: 2 cm of cortical bone is about 3.7 cm water-equivalent at 1.85, but only 2.2 cm at the mistaken 1.10, so the effective depth behind it would be understated. Lung at 0.25 to 0.33 is correct, and 0.30 is a typical planning value. Fat at 0.92 to 0.95 is correct. Muscle at about 1.05 is correct.

### Q2
Stem: An open ion chamber is read at 72 degrees Fahrenheit and 752 mmHg. The reference conditions are 22 degrees Celsius and 760 mmHg. What temperature-pressure correction factor multiplies the reading, to three decimals?
A. 1.011
B. 1.182
C. 0.990
D. 1.001
Answer: A
Objective: I.10
Why: Convert first: (72 − 32) × 5/9 = 22.2 degrees Celsius. The factor is (273.2 + 22.2)/(273.2 + 22.0) × 760/752 = 1.0007 × 1.0106 = 1.011. Check: the room is at reference temperature within 0.2 degrees, so the correction is almost entirely the 1.1 percent pressure term for 8 mmHg below reference. Using 72 directly as Celsius gives 345.2/295.2 × 1.0106 = 1.182. Inverting the pressure ratio gives 1.0007 × 0.9895 = 0.990. Dropping the pressure term leaves 1.001.
