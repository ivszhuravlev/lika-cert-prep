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
