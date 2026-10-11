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

### Q6
Stem: Cord dose sampled every 2 mm is 48.0, 51.0, 54.2, 50.5, and 47.0 Gy. A 6 mm grid keeps only 48.0 Gy and 50.5 Gy. What maximum is reported, and by how much is the peak missed?
A. 50.5 Gy reported, peak missed by 3.7 Gy
B. 54.2 Gy reported, peak missed by 0 Gy
C. 48.0 Gy reported, peak missed by 6.2 Gy
D. 51.0 Gy reported, the mean of the five samples
Answer: A
Objective: IV.6
Why: The coarse grid never lands on 54.2 Gy. The higher of the two kept points is 50.5 Gy. The miss is 54.2 − 50.5 = 3.7 Gy. Reporting 54.2 assumes the fine samples were kept. 48.0 is the other kept point, and 54.2 − 48.0 = 6.2 Gy overstates the miss if the algorithm reports the maximum of the calculated points.

### Q20
Stem: Iodinated contrast is left in the bladder at the CT number. Along one ray the contrast-filled bladder is 5.0 cm thick and the density table assigns 1.25. At treatment the bladder holds urine of density 1.00. Nobody applies a water override. How much extra water-equivalent thickness did the contrast add?
A. 6.25 cm
B. 5.00 cm
C. 0.25 cm
D. 1.25 cm
Answer: D
Objective: IV.6
Why: Extra thickness = 5.0 × (1.25 − 1.00) = 1.25 cm. That fictitious path is what a water override removes. 6.25 cm is 5.0 × 1.25, the whole contrast path, not the extra above water. 5.00 cm is the true urine path. 0.25 is the density difference with the 5.0 cm thickness omitted.

### Q21
Stem: Bladder contrast is left at relative density 1.25 instead of a water override at 1.00. For a megavoltage beam that exits through that bladder, what error does the uncorrected calculation make?
A. It under-attenuates, so the reported dose beyond the bladder is too high
B. It over-attenuates, so the reported dose beyond the bladder is too low
C. It makes no error, because iodinated contrast attenuates like urine
D. It changes only the electron cutout factor; photon dose is independent of the CT number
Answer: B
Objective: IV.6
Why: Contrast is not in the patient at treatment. Leaving it at 1.25 makes the ray look thicker than urine at 1.00, so the algorithm removes too much dose and the reported dose beyond the bladder is low. The override is to water, the material that will actually be there. Photon dose uses that density. This is a systematic path-length error, not an electron cutout.

### Q22
Stem: Along a spinal cord about 6 mm across, dose sampled every 2 mm is 45.0, 52.8, and 47.5 Gy. A 4 mm calculation grid keeps the first and third samples only. What maximum does that grid report, and how much of the peak does it miss?
A. 52.8 Gy reported, missed by 0 Gy
B. 47.5 Gy reported, missed by 5.3 Gy
C. 45.0 Gy reported, missed by 7.8 Gy
D. 48.4 Gy reported, the mean of the three samples
Answer: B
Objective: IV.6
Why: The coarse samples are 45.0 and 47.5 Gy. The higher of those is 47.5 Gy. The fine-sample peak is 52.8 Gy. The miss is 52.8 − 47.5 = 5.3 Gy. Reporting 52.8 assumes the 2 mm samples were kept. Using 45.0 as the reported maximum overstates the miss as 7.8 Gy. The mean, (45.0 + 52.8 + 47.5) / 3 = 48.4 Gy, is not the maximum of the points the coarse grid calculated.

### Q23
Stem: A cord about 6 mm in diameter is calculated on a 4 mm dose grid. The DVH maximum is just under the cord limit and is printed to a tenth of a gray. Why is that a weak number to accept?
A. A 4 mm grid is finer than a 6 mm cord, so a peak between voxel centers cannot be missed
B. Grid size changes parallel organs only; a serial organ such as cord is independent of the matrix
C. The cord is only about one to two voxels across, so a narrow maximum can fall between samples while the DVH still looks precise
D. The remedy is a 1 cm grid, which places the whole cord inside a single voxel and restores the peak
Answer: C
Objective: IV.6
Why: A 6 mm cord on a 4 mm grid is about one to two voxels across. A narrow maximum can sit between voxel centers and never enter the DVH, which will still print a tidy tenth of a gray. Serial-organ maxima are calculated on a fine grid, commonly 1 to 2 mm. A 4 mm grid is coarse for that judgment. Coarsening further to 1 cm makes the miss larger. The matrix limits the cord maximum the same way it limits any small serial structure.

### Q24
Stem: Dental amalgam saturates the planning CT. Bright and dark streaks cross the oral cavity and the tongue, and the tongue is inside the target. The raw streak CT numbers are used in the dose calculation with no override. What kind of uncertainty is that?
A. None; a streak Hounsfield unit is the density of the tongue
B. Monte Carlo statistical noise, which falls if more histories are run
C. A systematic density error; the streaks are artifact, not tissue, and dose through them is not reliable until the artifact is overridden or the beams avoid the metal
D. An inverse-square error that does not depend on the CT number
Answer: C
Objective: IV.6
Why: Metal saturates the detectors. The streaks are reconstruction artifact, not the density of tongue or tumor. Leaving those CT numbers in the calculation attenuates the beam through material that is not there, in a consistent direction. That is a systematic density error. More Monte Carlo histories do not fix a wrong density. Inverse square is still present; the missing step is an override or a beam that does not cross the uncertain metal.

### Q25
Stem: Dental metal and its streaks are both on the planning CT. Which handling matches a density override for this uncertainty?
A. Override the streaks to the surrounding soft-tissue density, and set the metal itself to a known density or keep the beams from crossing it when that density is uncertain
B. Override the streaks and the tongue to the amalgam density so the artifact matches the metal
C. Override the amalgam to air, because a dark streak next to it shows the metal is a cavity
D. Leave the saturated values in place; dental metal is stored as cortical bone on the CT-density table
Answer: A
Objective: IV.6
Why: Streaks should be painted back to the tissue that will be in the beam. If a beam must cross the metal, the metal needs an assigned density for that material, not the saturated CT number. When that density is uncertain, keep the beams off the metal. Painting the tongue to amalgam density invents high-density tunnels through the target. A dark streak is artifact, not proof that the filling is air. Saturated dental metal is not a cortical-bone row on the density table.
