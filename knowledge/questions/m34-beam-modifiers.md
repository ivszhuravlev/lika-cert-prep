# Module 34 — Effects of beam modifying devices

Original items. When an MU is computed, the linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm, unless the stem states a different calibration. Wedge factor is dose with the wedge divided by dose open, at the same MU. Wedge angle for a symmetric pair is 90° minus half the hinge angle.

## Wedges

### Q1
Stem: A wedge factor is measured as 0.620. Which statement matches that number?
A. The wedge angle is 62°
B. At the same MU, the wedged dose is 0.620 times the open dose
C. The wedge belongs in the numerator of the MU
D. The factor is the hinge angle in radians
Answer: B
Objective: IV.2
Why: WF = dose with the wedge / dose open, same MU, same point. 0.620 is a transmission, not an angle. In the MU it sits in the denominator because each MU delivers less dose when the wedge is in the beam.

### Q2
Stem: The prescription is 200 cGy at the calibration point. The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Every other factor is 1. A physical wedge with WF = 0.600 is in the beam, and the MU was computed with no wedge factor. What dose is delivered?
A. 200 cGy
B. 333 cGy
C. 120 cGy
D. 80 cGy
Answer: C
Objective: IV.2
Why: Omitting WF sets MU = 200 / 1.0 = 200. The wedge is still in the beam, so dose = 200 × 1.0 × 0.600 = 120 cGy. That is 120/200 = 0.60 of the prescription. The correct MU would have been 200 / 0.600 = 333 MU, and 333 × 0.600 = 200 cGy. 80 cGy is the shortfall (200 − 120), not the delivered dose.

### Q3
Stem: The same calibration is used: 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Prescription 200 cGy, WF = 0.600, and every other factor is 1. The MU was computed with the wedge factor, but the wedge was never inserted. What dose is delivered?
A. 120 cGy
B. 200 cGy
C. 333 cGy
D. 600 cGy
Answer: C
Objective: IV.2
Why: MU = 200 / 0.600 = 333.3. With the wedge absent, each MU delivers the open 1.0 cGy, so dose = 333.3 × 1.0 = 333 cGy. 333/200 = 1/0.600. 120 cGy is the opposite error (wedge in, factor omitted). 600 cGy multiplies by 1/0.6 a second time.

### Q4
Stem: A wedge tilts the isodose curves. The hot side of that tilted distribution is:
A. The thick side of the wedge
B. The thin side of the wedge
C. Always the central axis, independent of the wedge
D. The side where bolus was placed
Answer: B
Objective: IV.2
Why: The wedge attenuates more on the thick side, so the isodoses tilt and the higher dose is toward the thin side. The wedge angle is that isodose tilt, not the slope of the metal. Bolus is a separate modifier and is not what defines the wedge hot side.

### Q5
Stem: Which modifier pulls dmax toward the skin and raises skin dose, without being a wedge factor?
A. A dynamic wedge
B. Bolus
C. An enhanced dynamic wedge angle
D. Mid-leaf MLC transmission used as WF
Answer: B
Objective: IV.2
Why: Bolus is tissue-equivalent thickness on the skin. It shifts dmax toward the surface and increases skin dose. A dynamic or enhanced dynamic wedge still tilts isodoses and still needs a wedge factor in the MU. Leaf transmission is a small leakage fraction, not bolus.

## Wedge Factor Calculation Tutorial

### Q1
Stem: 100 MU open delivers 98.0 cGy at a point. The same 100 MU with the wedge delivers 58.8 cGy. What is the wedge factor?
A. 1.667
B. 0.600
C. 0.588
D. 39.2
Answer: B
Objective: IV.2
Why: WF = 58.8 / 98.0 = 0.600. Check: 98.0 × 0.600 = 58.8. 1.667 is 98.0 / 58.8, which is 1/WF. 0.588 divides 58.8 by 100 MU and ignores the open reading. 39.2 is the cGy difference, not a factor.

### Q2
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. The calculation point is that calibration point. WF = 0.600 and no other modifier is in the beam. How many MU deliver 180 cGy?
A. 108 MU
B. 180 MU
C. 300 MU
D. 450 MU
Answer: C
Objective: IV.2
Why: MU = 180 / (1.0 × 0.600) = 300. Check: 300 × 0.600 = 180 cGy. 108 cGy would be the dose if 180 MU were set with the wedge still in (180 × 0.600). 180 MU omits the factor. 450 MU divides by 0.4.

### Q3
Stem: Open dose for 80 MU is 80.0 cGy. Wedged dose for 80 MU is 48.0 cGy. The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm, and the point is that calibration point. How many MU deliver 240 cGy with the wedge in the beam?
A. 144 MU
B. 240 MU
C. 400 MU
D. 667 MU
Answer: C
Objective: IV.2
Why: WF = 48.0 / 80.0 = 0.600. MU = 240 / (1.0 × 0.600) = 400. Check: 400 × 0.600 = 240 cGy. 144 is 240 × 0.600, the dose from 240 MU with the wedge left in. 667 divides by an inverted factor (240 × 1/0.36).

### Q4
Stem: At the same MU, open dose is 120 cGy and wedged dose is 90 cGy. What is WF, and what fraction of an intended dose is delivered if that factor is left out of the MU while the wedge stays in the beam?
A. WF = 0.75, and the patient receives 75% of the intended dose
B. WF = 1.33, and the patient receives 133% of the intended dose
C. WF = 0.75, and the patient receives 133% of the intended dose
D. WF = 30, because 120 − 90 = 30
Answer: A
Objective: IV.2
Why: WF = 90 / 120 = 0.75. Omitting it sets the MU as if the beam were open. The wedge still transmits 0.75, so delivered/prescribed = 0.75. 1.33 is 120/90. The 30 cGy difference is not a factor.

### Q5
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. WF = 0.500 at the calibration point and every other factor is 1. The plan asks for 150 cGy with the wedge in the beam. How many MU are required?
A. 75 MU
B. 150 MU
C. 300 MU
D. 450 MU
Answer: C
Objective: IV.2
Why: MU = 150 / 0.500 = 300. Check: 300 × 0.500 = 150 cGy. 75 MU would deliver 37.5 cGy with the wedge in. 150 MU omits WF and delivers 75 cGy. 450 MU uses a factor of 1/3.

### Q6
Stem: A wedge factor measured at 6 MV is 0.65. The same physical wedge at 18 MV has a measured factor of 0.72. A 6 MV MU calculation should use:
A. 0.65
B. 0.72
C. 0.65 × 0.72 = 0.468
D. (0.65 + 0.72) / 2 = 0.685
Answer: A
Objective: IV.2
Why: The factor belongs to the energy, field, and depth at which it was measured. The 6 MV beam uses 0.65. Averaging or multiplying the two energies invents a third beam. 0.72 is the 18 MV measurement.

### Q7
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Prescription 100 cGy at that point, WF = 0.800, wedge in the beam, all other factors 1. If the planner multiplies by WF instead of dividing, how many MU are set, and what dose is actually delivered?
A. 80 MU are set and 64 cGy is delivered
B. 125 MU are set and 100 cGy is delivered
C. 80 MU are set and 100 cGy is delivered
D. 125 MU are set and 80 cGy is delivered
Answer: A
Objective: IV.2
Why: The wrong MU is 100 × 0.800 = 80. With the wedge in the beam, dose = 80 × 0.800 = 64 cGy. The correct MU is 100 / 0.800 = 125, and 125 × 0.800 = 100 cGy. Putting WF in the numerator underdoses a second time because the wedge is still physically present.

### Q8
Stem: Two readings are taken at different MU. Open: 50 MU gives 49.0 cGy. Wedged: 100 MU gives 58.8 cGy. What is the wedge factor after both readings are scaled to the same MU?
A. 1.20
B. 0.600
C. 0.294
D. 1.667
Answer: B
Objective: IV.2
Why: Scale the open reading to 100 MU: 49.0 × (100/50) = 98.0 cGy. WF = 58.8 / 98.0 = 0.600. 1.20 is 58.8/49.0 without matching the MU. 0.294 is 58.8/200, an invented denominator. 1.667 is 98/58.8, the reciprocal of the factor.

## Wedge and Hinge Angle

### Q1
Stem: Two beams form a hinge of 120°. For a symmetric wedged pair, what wedge angle flattens the distribution?
A. 60°
B. 30°
C. 120°
D. 90°
Answer: B
Objective: IV.2
Why: Wedge angle = 90° − (hinge/2) = 90 − 60 = 30°. 60° is the hinge halved, or 180 − 120. The formula is for a symmetric pair, not a single wedge against an open field. A 60° wedge on a 120° hinge over-tilts the isodoses.

### Q2
Stem: A symmetric pair uses 45° wedges. What hinge angle matches that pair?
A. 45°
B. 90°
C. 135°
D. 22.5°
Answer: B
Objective: IV.2
Why: Hinge = 2(90 − wedge angle) = 2(90 − 45) = 90°. Check: 90 − (90/2) = 45°. 45° copies the wedge angle. 135° is 180 − 45. 22.5° halves the wedge angle.

### Q3
Stem: A symmetric pair uses 60° wedges. What hinge angle matches that pair?
A. 60°
B. 30°
C. 120°
D. 90°
Answer: A
Objective: IV.2
Why: Hinge = 2(90 − 60) = 2 × 30 = 60°. Check: wedge angle = 90 − (60/2) = 60°. 30° is half the hinge of a different pair. 120° is the hinge that calls for 30° wedges. 90° calls for 45° wedges.

### Q4
Stem: The hinge between two central axes is 100°. What wedge angle does the symmetric-pair formula give?
A. 50°
B. 40°
C. 80°
D. 100°
Answer: B
Objective: IV.2
Why: Wedge angle = 90 − (100/2) = 90 − 50 = 40°. 50° is half the hinge and skips the 90° complement. 80° is 180 − 100. The hinge itself is not the wedge angle.

### Q5
Stem: A single 30° wedge is paired with an open beam, not with a second 30° wedge. Which statement is right?
A. The hinge formula still forces the open beam to be treated as a 30° wedge
B. The relation wedge angle = 90° − hinge/2 is for a symmetric wedged pair
C. WF equals 0.30 because the wedge is 30°
D. The hinge must be 30°
Answer: B
Objective: IV.2
Why: The hinge formula assumes both wedges have the same angle. An open companion beam is a different geometry. A 30° label is the isodose tilt, not a wedge factor of 0.30. For a real 30° pair the matching hinge is 2(90 − 30) = 120°, not 30°.

## MLCs

### Q1
Stem: A region blocked by an MLC would receive 200 cGy if it were open. Mid-leaf transmission is 1.5% (0.015). What dose is transmitted through the leaf?
A. 3.0 cGy
B. 30 cGy
C. 197 cGy
D. 1.5 cGy
Answer: A
Objective: IV.2
Why: Dose = 200 × 0.015 = 3.0 cGy. Check: 200 × 0.01 = 2.0 and 200 × 0.005 = 1.0, so 2.0 + 1.0 = 3.0. 30 cGy uses 15%. 197 cGy subtracts 3 cGy from the open dose and answers the blocked primary, not the transmission. 1.5 cGy drops the 200.

### Q2
Stem: Mid-leaf transmission is 2.0% and the open dose in that region would be 180 cGy. What dose leaks through the leaf?
A. 36 cGy
B. 3.6 cGy
C. 1.8 cGy
D. 90 cGy
Answer: B
Objective: IV.2
Why: 180 × 0.020 = 3.6 cGy. 36 cGy moves the decimal (20%). 1.8 cGy uses 1%. 90 cGy is half the open dose, a partial-transmission block, not a typical mid-leaf leak.

### Q3
Stem: Interleaf leakage compared with mid-leaf transmission is generally:
A. Lower, because the tongue-and-groove is a gap
B. Higher than the mid-leaf figure
C. Exactly equal to the wedge factor
D. Zero, because leaves overlap by definition
Answer: B
Objective: IV.2
Why: The gap between leaves leaks more than the middle of a leaf. Tongue-and-groove reduces that interleaf leak and can leave a cold stripe where adjacent segments do not cover the same way. Neither number is a wedge factor, and neither is zero.

### Q4
Stem: Rounded leaf ends shift the radiation edge relative to the light field. The commissioned parameter that lines those edges up is:
A. The wedge angle
B. The dosimetric leaf gap
C. Mayneord F
D. The hinge angle
Answer: B
Objective: IV.2
Why: The leaf-gap parameter accounts for transmission through the rounded end so the light field and the radiation edge agree. A wrong gap is a systematic dose error on modulated plans. Wedge angle, Mayneord F, and hinge angle do not set the leaf end.

### Q5
Stem: A partial-transmission block is specified at 50% transmission. The open dose under that region would be 200 cGy. What dose does the block transmit?
A. 3 cGy
B. 100 cGy
C. 50 cGy
D. 150 cGy
Answer: B
Objective: IV.2
Why: 200 × 0.50 = 100 cGy. A 50% block is not an MLC mid-leaf leak of about 1–2% (that would be 200 × 0.015 = 3 cGy). 50 cGy uses the percent as if it were already the dose. 150 cGy is 200 × 0.75.

## Beam Modifying Devices Quiz

### Q1
Stem: 100 MU open gives 110 cGy. 100 MU wedged gives 66 cGy. What is WF?
A. 0.600
B. 1.667
C. 0.660
D. 44
Answer: A
Objective: IV.2
Why: WF = 66 / 110 = 0.600. Check: 110 × 0.6 = 66. 1.667 is 110/66. 0.660 divides the wedged reading by 100 MU. 44 is the cGy difference.

### Q2
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. WF = 0.700, point at calibration, all other factors 1, wedge in the beam. How many MU deliver 210 cGy?
A. 147 MU
B. 210 MU
C. 300 MU
D. 70 MU
Answer: C
Objective: IV.2
Why: MU = 210 / 0.700 = 300. Check: 300 × 0.700 = 210 cGy. 147 is 210 × 0.700, the underdose if 210 MU are delivered through the wedge. 70 MU divides by 3.

### Q3
Stem: Prescription 250 cGy. Calibration is 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. WF = 0.500 was omitted and the wedge stayed in the beam. All other factors are 1. What dose is delivered?
A. 250 cGy
B. 500 cGy
C. 125 cGy
D. 62.5 cGy
Answer: C
Objective: IV.2
Why: MU = 250 / 1 = 250. Dose = 250 × 0.500 = 125 cGy. Delivered/prescribed = 0.50, the wedge factor. 500 cGy is the overdose pattern if the factor had been included (MU = 500) and the wedge left out. 62.5 cGy applies the factor twice.

### Q4
Stem: Hinge angle 80°. Symmetric wedged pair. What wedge angle does 90° − hinge/2 give?
A. 40°
B. 50°
C. 80°
D. 10°
Answer: B
Objective: IV.2
Why: 80/2 = 40, and 90 − 40 = 50°. 40° is only the half-hinge. 10° subtracts the whole hinge from 90. Check: hinge = 2(90 − 50) = 80°.

### Q5
Stem: Hinge angle 140°. Symmetric pair. What wedge angle is required?
A. 70°
B. 40°
C. 20°
D. 50°
Answer: C
Objective: IV.2
Why: Wedge angle = 90 − (140/2) = 90 − 70 = 20°. 70° is half the hinge. 40° is 180 − 140. 50° belongs to a hinge of 80°.

### Q6
Stem: Open dose 250 cGy under a leaf. Mid-leaf transmission is 1.2% (0.012). What dose is under the leaf?
A. 30 cGy
B. 3.0 cGy
C. 2.5 cGy
D. 247 cGy
Answer: B
Objective: IV.2
Why: 250 × 0.012 = 3.0 cGy. 30 cGy uses 12%. 2.5 cGy uses 1%. 247 cGy is the open dose minus the leak, which is not the transmitted dose the question asks for.

### Q7
Stem: A compensator is in the beam to replace missing tissue on a sloping surface. It should be treated as:
A. A density override inside the patient
B. A beam modifier with its own transmission, not a wedge angle and not a density override
C. Bolus on the skin
D. A hinge of 90°
Answer: B
Objective: IV.2
Why: A compensator sits in the beam and reduces fluence according to its thickness and attenuation. It is not a CT density override, not bolus (which is on the skin and pulls dmax up), and not a wedged-pair hinge.

### Q8
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. WF = 0.600 was used, so 400 MU were set for 180 cGy at the calibration point with TMR-style depth factor 0.750 also in the denominator (180 / (0.750 × 0.600) = 400). The wedge was not inserted. All other factors are 1 and the point is at the calibration distance. What dose is delivered?
A. 180 cGy
B. 108 cGy
C. 300 cGy
D. 400 cGy
Answer: C
Objective: IV.2
Why: With the wedge out, dose = 400 × 1.0 × 0.750 × 1 = 300 cGy. Check: 400 × 0.750 × 0.600 = 180 cGy only when the wedge is in. 300/180 = 1/0.600. 108 cGy is what 240 MU would deliver if the factor were omitted and the wedge stayed in (180/0.750 = 240, then 240 × 0.750 × 0.600 = 108). 400 cGy drops the TMR as well.
