# Module 37. Corrections for Tissue Inhomogeneities and Density Overrides

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Density Overrides

### Q1
Stem: Iodinated contrast is still in the vessels on the planning CT. The scanner mapped those voxels to a relative density above muscle. What should the dosimetrist do before calculating dose?
A. Leave the high density so the optimizer avoids vessels
B. Override the contrast to air
C. Override the contrast to soft-tissue density
D. Override the whole body to water and turn heterogeneity off
Answer: C
Objective: IV.4
Why: Contrast is a temporary high-Z fluid. If it stays in the CT-density curve, downstream dose is low because the calculation thinks the body is thicker than it will be at treatment. Override the contrast to soft-tissue density. Correct choice: Override the contrast to soft-tissue density. The iodine is not tissue. Leaving it makes the algorithm attenuate too much along those rays. Air would under-attenuate a vessel that is actually soft tissue or blood. A full water override throws away real lung and bone information. Only the contrast, and artifact if needed, should be painted back to tissue.

### Q2
Stem: A hip prosthesis creates bright streaks across the pelvis. Which override is the sensible first step?
A. Calculate on the raw streaks
B. Override the entire pelvis to air
C. Turn the dose grid to 1 cm so the streaks average out
D. Override the metal to a known metal density and the streaks to soft tissue or water
Answer: D
Objective: IV.4
Why: Metal should be set to a realistic metal density if the beam must pass through it, and the streak artifact should be reset to the surrounding tissue density. Better still, choose beam angles that avoid the prosthesis when the plan allows. Correct choice: Override the metal to a known metal density and the streaks to soft tissue or water. The streaks are artifact, not bone, and they invent false attenuation. That removes the patient. A coarse grid hides the artifact. It does not assign the right density.

### Q3
Stem: A 2 cm vessel was left at the contrast density 1.15 and the rest of this ray is water. Path: 2 cm at relative density 1.15, 10 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 12.00 cm
B. 12.30 cm
C. 11.74 cm
D. 2.30 cm
Answer: B
Objective: IV.4
Why: Substitute 2×1.15 + 10×1 = 2.30 + 10.00 = 12.30 cm, reported as 12.30 cm. The physical depth is 12.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 12.00 cm. Dividing thickness by density instead of multiplying gives 11.74 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 2.30 cm.

### Q4
Stem: Contrast plus soft tissue on one ray. Relative densities are the planning values after the CT table, before any override. Path: 3 cm at relative density 1.2, 8 cm at relative density 1, 1 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 12.00 cm
B. 11.50 cm
C. 3.60 cm
D. 12.60 cm
Answer: D
Objective: IV.4
Why: Substitute 3×1.2 + 8×1 + 1×1 = 3.60 + 8.00 + 1.00 = 12.60 cm, reported as 12.60 cm. The physical depth is 12.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 12.00 cm. Dividing thickness by density instead of multiplying gives 11.50 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 3.60 cm.

### Q5
Stem: A rectal air pocket is contoured as a density override. Why can that override be wrong by the time of treatment?
A. Air has relative density 1.0
B. Overrides are illegal in the pelvis
C. Gas moves, so the planning density may not be the treatment density
D. Air increases attenuation
Answer: C
Objective: IV.4
Why: An air override is only as good as the anatomy at treatment. Rectal gas changes between the planning CT and the fraction, so a hard air override can mis-estimate prostate and rectal dose. Correct choice: Gas moves, so the planning density may not be the treatment density. Air is near 0.001, not 1. The problem is that the pocket will not stay put. Overrides are appropriate for contrast and metal. Gas is the unstable case. Air decreases attenuation. The clinical issue is that the air may be gone, or larger, at treatment.

## Lung vs. Soft Tissue Heterogeneity Correction

### Q1
Stem: A 6 MV plan through lung is calculated as if the chest were water. What is the usual direction of the error beyond the lung?
A. The calculated dose is low
B. The calculated dose is high
C. There is no error if the equivalent square is correct
D. The error is only in the wedge factor
Answer: A
Objective: IV.4
Why: Lung attenuates less than water. A homogeneous calculation therefore underestimates dose downstream of lung. Inside a small field in lung the opposite problem also appears: loss of lateral scatter, which a simple path-length correction does not restore. Correct choice: The calculated dose is low. Water attenuates more than lung, so a water calculation removes too much dose before the point beyond the lung. Equivalent square does not insert a density. The wedge is unrelated to the missing heterogeneity.

### Q2
Stem: Which algorithm is weakest for a 4×4 cm field inside lung?
A. Monte Carlo
B. A linear Boltzmann solver
C. Pencil beam
D. Convolution/superposition
Answer: C
Objective: IV.4
Why: The pencil beam does not re-transport lateral electrons when density drops, so small fields in lung are its worst case. Correct choice: Pencil beam. Monte Carlo is a strong choice for lateral disequilibrium. A Boltzmann solver transports the interface rather than ignoring it. Superposition is imperfect in lung but stronger than a pencil beam.

### Q3
Stem: Teaching path. Soft tissue, then lung at relative density 0.25, then soft tissue. Path: 4 cm at relative density 1, 8 cm at relative density 0.25, 3 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 15.00 cm
B. 39.00 cm
C. 2.00 cm
D. 9.00 cm
Answer: D
Objective: IV.4
Why: Substitute 4×1 + 8×0.25 + 3×1 = 4.00 + 2.00 + 3.00 = 9.00 cm, reported as 9.00 cm. The physical depth is 15.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 15.00 cm. Dividing thickness by density instead of multiplying gives 39.00 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 2.00 cm.

### Q4
Stem: Teaching path through bone assigned relative density 1.4. Path: 6 cm at relative density 1, 3 cm at relative density 1.4, 4 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 13.00 cm
B. 12.14 cm
C. 4.20 cm
D. 14.20 cm
Answer: D
Objective: IV.4
Why: Substitute 6×1 + 3×1.4 + 4×1 = 6.00 + 4.20 + 4.00 = 14.20 cm, reported as 14.20 cm. The physical depth is 13.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 13.00 cm. Dividing thickness by density instead of multiplying gives 12.14 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 4.20 cm.

### Q5
Stem: Beyond a slab of bone, compared with a water calculation, a simple equivalent-path estimate does what?
A. Lowers the dose, because the water-equivalent depth is larger
B. Raises the dose the same way lung does
C. Leaves the dose unchanged if the physical depth is used
D. Applies Mayneord F
Answer: A
Objective: IV.4
Why: Relative density above 1 lengthens the water-equivalent path, lowers the TMR, and lowers the estimated dose beyond the bone. Lung does the opposite. Correct choice: Lowers the dose, because the water-equivalent depth is larger. Bone is denser than water, so it attenuates more, not less. Using the physical depth is the uncorrected calculation. The equivalent depth is longer, so TMR falls. Mayneord F is an SSD change, not a density change.

## Corrections for Tissue Inhomogeneity Mini-Quiz

### Q1
Stem: Quiz. Lung density 0.30. Path: 5 cm at relative density 1, 6 cm at relative density 0.3, 4 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 15.00 cm
B. 29.00 cm
C. 1.80 cm
D. 10.80 cm
Answer: D
Objective: IV.4
Why: Substitute 5×1 + 6×0.3 + 4×1 = 5.00 + 1.80 + 4.00 = 10.80 cm, reported as 10.80 cm. The physical depth is 15.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 15.00 cm. Dividing thickness by density instead of multiplying gives 29.00 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 1.80 cm.

### Q2
Stem: Quiz. A long lung path. Path: 2 cm at relative density 1, 10 cm at relative density 0.25, 2 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 14.00 cm
B. 44.00 cm
C. 6.50 cm
D. 2.50 cm
Answer: C
Objective: IV.4
Why: Substitute 2×1 + 10×0.25 + 2×1 = 2.00 + 2.50 + 2.00 = 6.50 cm, reported as 6.50 cm. The physical depth is 14.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 14.00 cm. Dividing thickness by density instead of multiplying gives 44.00 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 2.50 cm.

### Q3
Stem: Quiz. Bone density 1.6. Path: 7 cm at relative density 1, 2 cm at relative density 1.6, 5 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 15.20 cm
B. 14.00 cm
C. 13.25 cm
D. 3.20 cm
Answer: A
Objective: IV.4
Why: Substitute 7×1 + 2×1.6 + 5×1 = 7.00 + 3.20 + 5.00 = 15.20 cm, reported as 15.20 cm. The physical depth is 14.00 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 14.00 cm. Dividing thickness by density instead of multiplying gives 13.25 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 3.20 cm.

### Q4
Stem: Quiz. Equivalent depth is shallower than the physical depth. An equivalent-path estimate uses TMR(water-equivalent depth) = 0.8 and TMR(physical depth) = 0.68. The uncorrected point dose is 180 cGy. Correction factor = TMR(equivalent)/TMR(physical), and corrected dose = uncorrected × factor. What is the corrected dose? Scatter change is ignored in this estimate.
A. 153.0 cGy
B. 180.0 cGy
C. 192.0 cGy
D. 211.8 cGy
Answer: D
Objective: IV.4
Why: Factor = 0.8 / 0.68 = 1.1765. Corrected dose = 180 × 1.1765 = 211.76 cGy, reported as 211.8 cGy. When the equivalent depth is shallower than the physical depth (lung in the path), the factor is greater than 1: the water-only calculation was low. Inverting the TMR ratio gives 153.0 cGy and would claim the patient got less dose beyond lung. Leaving the dose uncorrected gives 180.0 cGy. Adding the TMR difference as if it were cGy gives 192.0 cGy.

### Q5
Stem: Quiz. The equivalent depth is deeper (bone). Read the ratio direction. An equivalent-path estimate uses TMR(water-equivalent depth) = 0.76 and TMR(physical depth) = 0.82. The uncorrected point dose is 200 cGy. Correction factor = TMR(equivalent)/TMR(physical), and corrected dose = uncorrected × factor. What is the corrected dose? Scatter change is ignored in this estimate.
A. 185.4 cGy
B. 215.8 cGy
C. 200.0 cGy
D. 194.0 cGy
Answer: A
Objective: IV.4
Why: Factor = 0.76 / 0.82 = 0.9268. Corrected dose = 200 × 0.9268 = 185.37 cGy, reported as 185.4 cGy. When the equivalent depth is shallower than the physical depth (lung in the path), the factor is greater than 1: the water-only calculation was low. Inverting the TMR ratio gives 215.8 cGy and would claim the patient got less dose beyond lung. Leaving the dose uncorrected gives 200.0 cGy. Adding the TMR difference as if it were cGy gives 194.0 cGy.

### Q6
Stem: Quiz. Lung path, uncorrected dose 150 cGy. An equivalent-path estimate uses TMR(water-equivalent depth) = 0.845 and TMR(physical depth) = 0.705. The uncorrected point dose is 150 cGy. Correction factor = TMR(equivalent)/TMR(physical), and corrected dose = uncorrected × factor. What is the corrected dose? Scatter change is ignored in this estimate.
A. 125.1 cGy
B. 150.0 cGy
C. 179.8 cGy
D. 164.0 cGy
Answer: C
Objective: IV.4
Why: Factor = 0.845 / 0.705 = 1.1986. Corrected dose = 150 × 1.1986 = 179.79 cGy, reported as 179.8 cGy. When the equivalent depth is shallower than the physical depth (lung in the path), the factor is greater than 1: the water-only calculation was low. Inverting the TMR ratio gives 125.1 cGy and would claim the patient got less dose beyond lung. Leaving the dose uncorrected gives 150.0 cGy. Adding the TMR difference as if it were cGy gives 164.0 cGy.

### Q7
Stem: Quiz. Interpolate TMR at the water-equivalent depth before any correction factor. A table lists TMR = 0.86 at 8 and TMR = 0.8 at 12. Linearly interpolate TMR at 9. No curve fit, just the straight fraction of the interval.
A. 0.860
B. 0.845
C. 0.830
D. 0.815
Answer: B
Objective: IV.4
Why: The point 9 is (9−8)/(12−8) = 0.2500 of the way from 8 to 12. The table changes by -0.06 over that whole step. Change on this step = 0.2500 × (-0.06) = -0.0150. TMR = 0.86 + (-0.0150) = 0.8450, reported as 0.845. Using the nearer table entry without interpolating gives 0.860. Averaging the endpoints as if the point were midway gives 0.830. Measuring the fraction from the wrong end of the interval gives 0.815.

### Q8
Stem: Quiz. Residual oral contrast, relative density 1.25, on an otherwise water-like ray. Path: 1.5 cm at relative density 1.25, 12 cm at relative density 1. Water-equivalent depth = sum of (thickness × relative electron density). What is the water-equivalent depth? This equivalent-path estimate ignores the change in lateral scatter.
A. 13.50 cm
B. 13.88 cm
C. 13.20 cm
D. 1.88 cm
Answer: B
Objective: IV.4
Why: Substitute 1.5×1.25 + 12×1 = 1.88 + 12.00 = 13.88 cm, reported as 13.88 cm. The physical depth is 13.50 cm, which would be the answer only if every segment had density 1. Beyond lung, a photon plan that ignores the low density underestimates dose, because the real attenuation is less than the water calculation. The equivalent-path method does not restore lateral electron equilibrium, so small fields in lung still need a better algorithm than this hand factor. Adding physical thicknesses only gives 13.50 cm. Dividing thickness by density instead of multiplying gives 13.20 cm. Keeping only the inhomogeneous segments and dropping unit-density tissue gives 1.88 cm.

### Q9
Stem: A lung slab is 6.0 cm thick and its mean HU is −750. For this hand calculation, relative density is one plus the quantity HU divided by 1000. What is the water-equivalent thickness of that slab, to the nearest 0.01 cm?
A. 6.00 cm
B. 4.50 cm
C. 1.50 cm
D. 10.50 cm
Answer: C
Objective: IV.4
Why: Relative density = 1 + (−750 / 1000) = 1 − 0.750 = 0.250. Water-equivalent thickness = 6.0 × 0.250 = 1.50 cm. Using the physical thickness alone gives 6.00 cm. Dropping the leading 1 and using 0.750 as the density gives 6.0 × 0.750 = 4.50 cm. Flipping the sign of the HU, 1 + (750 / 1000) = 1.750, gives 6.0 × 1.750 = 10.50 cm.

### Q10
Stem: A 6 MV ray to a point beyond lung crosses 3.0 cm of soft tissue, then 10.0 cm of lung whose mean HU is −700, then 2.0 cm of soft tissue. Soft tissue relative density is 1.00. For the lung, relative density is one plus the quantity HU divided by 1000. Dose at dmax on this ray, at the point's source distance, is 250 cGy. TMR values for this field are 0.860 at 6 cm, 0.785 at 8 cm, 0.740 at 10 cm, and 0.620 at 15 cm. What path-length dose reaches the point, to the nearest 0.1 cGy? This estimate does not restore lateral scatter.
A. 196.3 cGy
B. 155.0 cGy
C. 215.0 cGy
D. 185.0 cGy
Answer: A
Objective: IV.4
Why: Lung density = 1 + (−700 / 1000) = 1 − 0.700 = 0.300. Water-equivalent depth = 3.0 × 1.00 + 10.0 × 0.300 + 2.0 × 1.00 = 3.00 + 3.00 + 2.00 = 8.00 cm. TMR at 8 cm is 0.785. Dose = 250 × 0.785 = 196.25 cGy, reported as 196.3 cGy. The physical depth is 3 + 10 + 2 = 15 cm, and 250 × 0.620 = 155.0 cGy, which is the homogeneous-water result and is low beyond lung. Stopping at 6 cm, as if the last soft tissue were omitted or the lung contributed nothing, gives 250 × 0.860 = 215.0 cGy. Reading 10 cm instead of 8 cm gives 250 × 0.740 = 185.0 cGy.

### Q11
Stem: An isocentric beam is calibrated to 1.000 cGy/MU at dmax for this field at the isocenter, open and on axis. The ray crosses 5.0 cm of soft tissue at relative density 1.00, 4.0 cm of bone at relative density 1.65, and 3.0 cm of soft tissue at relative density 1.00. The point is to receive 180 cGy. TMR values for this field are 0.760 at 10 cm, 0.700 at 12 cm, 0.640 at 14 cm, and 0.600 at 16 cm. How many MU does the path-length estimate require, to the nearest 0.1 MU?
A. 257.1 MU
B. 286.6 MU
C. 113.0 MU
D. 236.8 MU
Answer: B
Objective: IV.4
Why: Water-equivalent depth = 5.0 × 1.00 + 4.0 × 1.65 + 3.0 × 1.00 = 5.00 + 6.60 + 3.00 = 14.60 cm. The 14.6 cm point is (14.6 − 14) / (16 − 14) = 0.60 / 2 = 0.30 of the way from 14 cm to 16 cm. TMR change = 0.30 × (0.600 − 0.640) = 0.30 × (−0.040) = −0.012. TMR = 0.640 − 0.012 = 0.628. Scatter and distance match the calibration, so MU = 180 / 0.628 = 286.62, which rounds to 286.6 MU. The physical depth is 5 + 4 + 3 = 12 cm, and 180 / 0.700 = 257.14 MU, reported as 257.1 MU. Dividing the bone thickness by 1.65 instead of multiplying, 4.0 / 1.65 = 2.424 cm, puts the equivalent depth at 5.00 + 2.424 + 3.00 = 10.424 cm; reading the 10 cm row then gives 180 / 0.760 = 236.84 MU, reported as 236.8 MU. Multiplying the dose by the TMR, 180 × 0.628 = 113.04, gives 113.0 MU.

### Q12
Stem: Missing tissue leaves a 4.0 cm air gap along a fan line. Isodose-shift factors are 0.7 for cobalt-60, 0.6 for 6 MV, and 0.5 for 18 MV. The beam is 6 MV, and the chart is shifted by that energy's factor times the gap. How many centimetres is the shift, to the nearest 0.1 cm?
A. 4.0 cm
B. 2.8 cm
C. 2.0 cm
D. 2.4 cm
Answer: D
Objective: IV.4
Why: The 6 MV factor is 0.6. Shift = 0.6 × 4.0 = 2.4 cm. Shifting by the whole gap gives 4.0 cm and ignores that scatter does not move as fast as primary attenuation. The cobalt-60 factor gives 0.7 × 4.0 = 2.8 cm. The 18 MV factor gives 0.5 × 4.0 = 2.0 cm. For missing tissue the chart moves downstream, away from the source, by this 2.4 cm; the question asks for that distance.

### Q13
Stem: The calculation point lies inside lung, not beyond it, in a 3 by 3 cm 6 MV field, and lateral electron equilibrium is lost. A water calculation at the point is 160 cGy. Measured factors at this depth in lung, listed as path-length factor then lateral factor, are 1.18 and 0.99 for 10 by 10, 1.14 and 0.93 for 5 by 5, 1.10 and 0.84 for 3 by 3, and 1.06 and 0.72 for 2 by 2. What dose should the hand calculation report, to the nearest 0.1 cGy?
A. 176.0 cGy
B. 115.2 cGy
C. 134.4 cGy
D. 160.0 cGy
Answer: C
Objective: IV.4
Why: Inside a small field in lung, electrons leave the field and are not replaced, so the lateral factor is the one that applies. For 3 by 3 cm that factor is 0.84. Dose = 160 × 0.84 = 134.4 cGy. The path-length factor 1.10 would raise the dose, 160 × 1.10 = 176.0 cGy, which is the wrong direction inside the lung. The 2 by 2 cm lateral factor gives 160 × 0.72 = 115.2 cGy. Leaving the water dose unchanged gives 160.0 cGy.

### Q14
Stem: Contrast fills 5.0 cm of bladder at relative density 1.50, then the ray crosses 6.0 cm of tissue at relative density 1.00. On the treatment day the bladder is water at relative density 1.00. The plan left the contrast in and reports 170 cGy beyond the bladder. TMR values for this field are 0.760 at 11.0 cm and 0.680 at 13.5 cm. With the contrast overridden to water, what path-length dose replaces that report, to the nearest 0.1 cGy?
A. 170.0 cGy
B. 152.1 cGy
C. 172.5 cGy
D. 190.0 cGy
Answer: D
Objective: IV.4
Why: With contrast left in, water-equivalent depth = 5.0 × 1.50 + 6.0 × 1.00 = 7.50 + 6.00 = 13.50 cm, and the TMR is 0.680. After the override to water, depth = 5.0 × 1.00 + 6.0 × 1.00 = 11.00 cm, and the TMR is 0.760. The reported 170 cGy was built on the longer path, so the overridden dose is 170 × (0.760 / 0.680). The ratio 0.760 / 0.680 = 1.11765. Then 170 × 1.11765 = 190.00 cGy, reported as 190.0 cGy. The same product is 170 × 0.760 = 129.2, and 129.2 / 0.680 = 190.0. Keeping the contrast report gives 170.0 cGy. Inverting the TMR ratio gives 170 × (0.680 / 0.760) = 152.11 cGy, reported as 152.1 cGy. Adding the 2.5 cm of extra water-equivalent path onto the report as if it were cGy gives 172.5 cGy.

### Q15
Stem: A ray crosses 4.0 cm of soft tissue at relative density 1.00, 8.0 cm of lung at relative density 0.25, and 3.0 cm of soft tissue at relative density 1.00. TMR values for this field are 0.800 at 9 cm, 0.710 at 12 cm, and 0.620 at 15 cm. By what percent does the path-length correction raise the dose above a homogeneous water calculation, to the nearest 0.1 percent?
A. 29.0 %
B. 22.5 %
C. 18.0 %
D. 129.0 %
Answer: A
Objective: IV.4
Why: Water-equivalent depth = 4.0 × 1.00 + 8.0 × 0.25 + 3.0 × 1.00 = 4.00 + 2.00 + 3.00 = 9.00 cm. Physical depth = 4 + 8 + 3 = 15 cm. TMR at 9 cm is 0.800 and TMR at 15 cm is 0.620. Ratio = 0.800 / 0.620 = 1.2903. The fractional increase is 1.2903 − 1 = 0.2903, and 0.2903 × 100 = 29.03%, reported as 29.0%. Dividing the TMR difference by the equivalent-depth TMR, (0.800 − 0.620) / 0.800 = 0.180 / 0.800 = 0.225, gives 22.5%. Calling the raw TMR difference a percent, 0.800 − 0.620 = 0.180, gives 18.0%. Turning the ratio itself into a percent, 1.2903 × 100, gives 129.0% and never subtracts the original dose.

### Q16
Stem: An equivalent-path calculation predicts 180 cGy at a point past an air cavity. The point is 1.0 cm beyond the distal edge of the cavity. A measured rebuild-up table for this beam, as a factor on that path-length dose, is 0.85 at 0.0 cm past the cavity, 0.96 at 2.0 cm past the cavity, and 1.00 at 5.0 cm past the cavity. What dose includes rebuild-up, to the nearest 0.1 cGy?
A. 153.0 cGy
B. 162.9 cGy
C. 172.8 cGy
D. 180.0 cGy
Answer: B
Objective: IV.4
Why: The point at 1.0 cm is (1.0 − 0.0) / (2.0 − 0.0) = 0.50 of the way from 0.0 cm to 2.0 cm. Factor = 0.85 + 0.50 × (0.96 − 0.85) = 0.85 + 0.50 × 0.11 = 0.85 + 0.055 = 0.905. Dose = 180 × 0.905 = 162.9 cGy. Just at the distal edge, 180 × 0.85 = 153.0 cGy. At 2.0 cm past the cavity, 180 × 0.96 = 172.8 cGy. Using the path-length dose with no rebuild-up factor gives 180.0 cGy. Near the cavity the dose is still short of the equivalent-path prediction because electron buildup has to start again.
