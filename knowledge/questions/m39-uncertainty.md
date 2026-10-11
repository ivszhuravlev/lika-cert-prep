# Module 39. Sources of uncertainty and limitations in computer-based treatment planning

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Sources of Uncertainty

### Q1
Stem: How many 2 mm dose-grid voxels fit in one 4 mm voxel?
A. 2
B. 8
C. 4
D. 16
Answer: B
Objective: IV.6
Why: Volume scales with the cube of the side. (4/2)^3 = 2^3 = 8. A 4 mm grid is eight times coarser in volume than a 2 mm grid, which is why small-structure DVHs and steep SRS gradients move when the grid changes. Correct choice: 8. 2 is the linear ratio 4/2, not the volume ratio. 4 is the area ratio (4/2)^2. 16 would be (4/2)^4, one power too many.

### Q2
Stem: A coarse grid stores 180 cGy and 100 cGy in two neighboring voxels. Linear interpolation at the midpoint reports what dose, and what is the limitation?
A. 280 cGy, the sum
B. 180 cGy, the higher neighbor, always
C. 40 cGy, the difference
D. 140 cGy, and the true peak between the samples can be missed
Answer: D
Objective: IV.6
Why: Linear interpolation gives (180 + 100) / 2 = 140 cGy. That is only what this coarse grid can see. A hotspot narrower than the grid can sit between the samples and never enter the DVH. Correct choice: 140 cGy, and the true peak between the samples can be missed. Adding the samples double-counts two different voxels. The midpoint of a linear grid estimate is the average, not the max. Even that average can miss a peak. The difference is not the interpolated dose.

### Q3
Stem: Which grid is the usual choice for a steep SRS gradient?
A. 1 cm
B. About 1 to 2 mm
C. 5 mm
D. The grid does not affect SRS because the algorithm is Monte Carlo
Answer: B
Objective: IV.6
Why: SRS and other steep gradients are usually computed on about a 1–2 mm grid so the penumbra and small-volume DVH are sampled. A 4 or 5 mm grid is a real uncertainty, not a cosmetic setting. Correct choice: About 1 to 2 mm. A 1 cm grid cannot sample a stereotactic penumbra. 5 mm is coarse for SRS and will blur the high-dose core. Monte Carlo still scores onto a grid. A coarse grid undoes the transport detail.

### Q4
Stem: Heterogeneity correction is turned off for a lung SBRT plan. How should that choice be labeled?
A. Monte Carlo statistical uncertainty
B. A dose-grid interpolation
C. An inverse-square correction
D. A systematic error, not random noise
Answer: D
Objective: IV.6
Why: Calculating lung as water biases the dose in a consistent direction. That is a systematic model error. It is different from the random uncertainty of a Monte Carlo run and different from grid sampling. Correct choice: A systematic error, not random noise. Statistical noise shrinks if you run more histories. Forgetting heterogeneity does not. The grid samples the result. It does not replace missing density. Inverse square is still present in the divergence. The missing piece is tissue density.

### Q5
Stem: Contrast is left at relative density 1.20 over a 3.0 cm vessel that should be 1.00. How much extra water-equivalent path did the contrast add on that ray?
A. 3.60 cm
B. 1.20 cm
C. 3.00 cm
D. 0.60 cm
Answer: D
Objective: IV.6
Why: Extra path = thickness × (wrong density − tissue density) = 3.0 × (1.20 − 1.00) = 3.0 × 0.20 = 0.60 cm. That extra 0.60 cm is fictitious attenuation and should be removed by overriding the contrast. Correct choice: 0.60 cm. 3.0 × 1.20 = 3.60 cm is the whole contrast path, not the extra above tissue. 1.20 is the density, not the added centimeters. 3.00 cm would be the extra only if the override density were 2.00.
