# Module 33. External beam dose calculation and algorithms

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Dose Calculation and Algorithms

### Q1
Stem: A 3 cm lung slit sits in a 4×4 cm 6 MV field. Which dose algorithm is the weakest choice for the dose on the far side of that interface?
A. Monte Carlo
B. Pencil beam
C. Linear Boltzmann solver (Acuros XB)
D. Convolution/superposition
Answer: B
Objective: IV.1
Why: Lateral electron equilibrium fails in a small field that crosses lung. A pencil beam spreads dose with a kernel that does not re-transport that lateral scatter, so the interface dose is the least trustworthy of these four. Convolution/superposition is better because the kernel is scaled by local density. Monte Carlo and a linear Boltzmann solver (Acuros XB) follow the transport through the interface. Correct choice: Pencil beam. Monte Carlo transports photons and electrons through the interface and is one of the stronger choices, not the weakest. A linear Boltzmann transport solver handles interface transport directly and is not the weak choice here. Convolution/superposition density-scales a kernel and is imperfect, but it is still stronger than a pencil beam at this interface.

### Q2
Stem: What does a Clarkson integration separate when the field shape is irregular?
A. Mayneord F and wedge factor
B. CT number and mass density
C. Primary dose and scatter
D. Hinge angle and wedge angle
Answer: C
Objective: IV.1
Why: Clarkson averages scatter-air ratios over sectors and adds that scatter to the zero-area primary term. The method exists because an irregular block does not have the same scatter as a rectangle of the same area. Correct choice: Primary dose and scatter. Mayneord F is only an inverse-square PDD correction, and a wedge factor is a beam modifier, not what Clarkson splits. The CT-density table is a commissioning input, not the Clarkson split. Hinge and wedge angles describe how two wedged beams tilt isodose lines.

### Q3
Stem: A Mayneord F factor is applied to move a PDD from SSD 100 cm to SSD 110 cm. Which effect is inside F?
A. Inverse square only
B. A new phantom-scatter factor
C. A heterogeneity correction
D. Collimator backscatter
Answer: A
Objective: IV.1
Why: F = [(SSD2+dmax)/(SSD1+dmax)]^2 × [(SSD1+depth)/(SSD2+depth)]^2. Both pieces are distances from the source, so F is inverse square only. Correct choice: Inverse square only. F does not recompute scatter. Scatter is assumed unchanged, which is why a large SSD change makes F approximate. Nothing in F refers to density or CT number. Collimator scatter is an Sc problem, not Mayneord F.

### Q4
Stem: A blocked portal is converted to an equivalent square by multiplying the open-field equivalent square by the square root of the unblocked area fraction. What is wrong with that step?
A. The step forgot inverse square
B. Clarkson ignores scatter, so the scaling is required
C. Percent blocked area is not a full scatter correction
D. Mayneord F already applied the block
Answer: C
Objective: IV.1
Why: Scatter at a point depends on where the open phantom sits around that point. Two blocks with the same area can shadow very different amounts of scatter. Scaling by the square root of the open fraction only resizes area. Correct choice: Percent blocked area is not a full scatter correction. Inverse square is not what this area scaling claims to estimate. Clarkson is the method that keeps scatter; the area scaling is the shortcut that loses it. Mayneord F changes SSD, not block shape.

### Q5
Stem: Which description matches the algorithm class?
A. Both methods are stored TAR lookups
B. Superposition density-scales a kernel; Monte Carlo follows histories
C. Pencil beam is a form of Monte Carlo
D. Monte Carlo cannot report dose in lung
Answer: B
Objective: IV.1
Why: Superposition takes incident energy fluence and spreads it with a kernel that is stretched or scaled by local density. Monte Carlo samples particle histories and scores dose. Neither one is a TAR table. Correct choice: Superposition density-scales a kernel; Monte Carlo follows histories. TAR lookups are correction-based tables, not superposition or Monte Carlo. A pencil beam is a kernel convolution, not a history-by-history transport. Monte Carlo is used in lung precisely because it can transport the disequilibrium.

### Q6
Stem: A 6 MV field is 8.0 cm wide on the skin. The SSD is 100 cm. How wide is the field at 15 cm depth, to the nearest 0.1 cm?
A. 1.2 cm
B. 9.2 cm
C. 8.0 cm
D. 7.0 cm
Answer: B
Objective: IV.1
Why: Field width grows with distance from the source. The skin is 100 cm from the source and the point at 15 cm depth is 115 cm from the source. Width at depth = 8.0 × (115/100) = 8.0 × 1.15 = 9.20 cm, reported as 9.2 cm. Turning the distance ratio upside down gives 8.0 × (100/115) = 6.96 cm, which rounds to 7.0 cm. Leaving the skin width unchanged gives 8.0 cm. Multiplying by the depth alone, 8.0 × (15/100), gives 1.2 cm.

### Q7
Stem: The collimator readout is the field size at 100 cm from the source. The SSD is 100 cm. The field at 12 cm depth must be 18.0 cm wide. What readout, to the nearest 0.1 cm, produces that width?
A. 20.5 cm
B. 18.0 cm
C. 16.1 cm
D. 20.2 cm
Answer: C
Objective: IV.1
Why: The point at 12 cm depth is 112 cm from the source, and the collimator scale is at 100 cm. Readout = 18.0 × (100/112) = 1800/112 = 16.071 cm, which rounds to 16.1 cm. Reversing the distances gives 18.0 × (112/100) = 20.16 cm, reported as 20.2 cm. Copying the deep width onto the readout gives 18.0 cm. Measuring back from the surface toward the source, 18.0 × (100/88), gives 20.45 cm, reported as 20.5 cm.

### Q8
Stem: An isocentric field is 14.0 cm wide at SAD 100 cm. The patient SSD is 80 cm. How wide is the light field on the skin, to the nearest 0.1 cm?
A. 17.5 cm
B. 14.0 cm
C. 12.6 cm
D. 11.2 cm
Answer: D
Objective: IV.1
Why: The skin is closer to the source than the isocenter, so the light field is smaller there. Width on the skin = 14.0 × (80/100) = 11.20 cm, reported as 11.2 cm. Inverting the distances gives 14.0 × (100/80) = 17.5 cm. Leaving the isocenter width unchanged gives 14.0 cm. Using a point 10 cm deep instead of the skin, 14.0 × (90/100), gives 12.6 cm.

### Q9
Stem: At the depth of interest the zero-area TAR is 0.450 and the free-space dose at the point is 120 cGy. Scatter-air ratios at that depth are 0.110 at radius 4 cm, 0.180 at radius 8 cm, and 0.230 at radius 12 cm. The portal is three sectors: 90 degrees out to 8 cm, 180 degrees out to 4 cm, and 90 degrees out to 12 cm. What is the tissue dose at the point, to the nearest 0.1 cGy?
A. 116.4 cGy
B. 72.9 cGy
C. 54.0 cGy
D. 81.6 cGy
Answer: B
Objective: IV.1
Why: Each sector is weighted by its share of 360 degrees. The 90-degree sector at 8 cm contributes (90/360) × 0.180 = 0.25 × 0.180 = 0.0450. The 180-degree sector at 4 cm contributes (180/360) × 0.110 = 0.50 × 0.110 = 0.0550. The 90-degree sector at 12 cm contributes (90/360) × 0.230 = 0.25 × 0.230 = 0.0575. Field SAR = 0.0450 + 0.0550 + 0.0575 = 0.1575. TAR = 0.450 + 0.1575 = 0.6075. Tissue dose = 0.6075 × 120 = 72.90 cGy, reported as 72.9 cGy. Adding the three SARs to the zero-area TAR without angle weights gives (0.450 + 0.180 + 0.110 + 0.230) × 120 = 0.970 × 120 = 116.4 cGy. Primary only, 0.450 × 120, gives 54.0 cGy. Using the largest SAR for the whole field, (0.450 + 0.230) × 120, gives 81.6 cGy.

### Q10
Stem: Dose along a spinal cord, sampled every 2 mm, reads 44.0, 46.5, 49.8, 47.2, and 45.0 Gy. A 6 mm dose grid keeps only the first and the fourth of those samples. How many gray does that coarse maximum miss, to the nearest 0.1 Gy?
A. 5.8 Gy
B. 2.6 Gy
C. 49.8 Gy
D. 3.2 Gy
Answer: B
Objective: IV.1
Why: The samples in order are 44.0, 46.5, 49.8, 47.2, and 45.0 Gy. The true maximum is 49.8 Gy. The coarse grid keeps 44.0 Gy and 47.2 Gy, so its maximum is 47.2 Gy. Missed peak = 49.8 − 47.2 = 2.6 Gy. Subtracting the first sample from the coarse maximum gives 47.2 − 44.0 = 3.2 Gy. Subtracting the first sample from the true peak gives 49.8 − 44.0 = 5.8 Gy. Reporting the true peak itself gives 49.8 Gy, which is the dose, not the amount the grid missed.

### Q11
Stem: An open field is 8.0 cm by 20.0 cm on the skin. The SSD is 100 cm. What is the equivalent square of that field at 10 cm depth, to the nearest 0.1 cm?
A. 15.4 cm
B. 13.9 cm
C. 12.6 cm
D. 11.4 cm
Answer: C
Objective: IV.1
Why: Both sides scale with distance from the source. At 10 cm depth the source distance is 110 cm, so each side is multiplied by 110/100 = 1.10. The sides at depth are 8.0 × 1.10 = 8.8 cm and 20.0 × 1.10 = 22.0 cm. Equivalent square = 2 × 8.8 × 22.0 / (8.8 + 22.0) = 387.2 / 30.8 = 12.571 cm, which rounds to 12.6 cm. The same square on the skin, before divergence, is 2 × 8.0 × 20.0 / (8.0 + 20.0) = 320 / 28 = 11.429 cm, reported as 11.4 cm. The arithmetic mean of the diverged sides, (8.8 + 22.0) / 2, is 15.4 cm. The square root of the diverged area, the square root of 8.8 × 22.0 = 193.6, is 13.91 cm, reported as 13.9 cm.

### Q12
Stem: The calculation point is 112 cm from the source. Along this ray the skin is 97 cm from the source. Dose at dmax at this same source distance is 200 cGy. TMR values for this field are 0.810 at 9 cm, 0.740 at 12 cm, and 0.680 at 15 cm. A flat phantom would have put the skin at 100 cm from the source. What is the dose at the point, to the nearest 0.1 cGy?
A. 162.0 cGy
B. 294.1 cGy
C. 148.0 cGy
D. 136.0 cGy
Answer: D
Objective: IV.1
Why: Depth is the distance from the real skin to the point: 112 − 97 = 15 cm. The skin is 3 cm closer to the source than the flat-phantom surface at 100 cm, so the point sits under extra tissue. Dose = 200 × 0.680 = 136.0 cGy. The flat-phantom depth would have been 112 − 100 = 12 cm, and 200 × 0.740 = 148.0 cGy. Moving the gap the wrong way, as if the skin were 3 cm farther out at 103 cm, gives depth 9 cm and 200 × 0.810 = 162.0 cGy. Dividing by the TMR, 200 / 0.680 = 294.12 cGy, reported as 294.1 cGy, turns a depth dose back into a dmax dose.

### Q13
Stem: A corner block leaves two sectors at the depth of interest. The zero-area TAR is 0.400. The TAR at radius 5 cm is 0.580, and the TAR at radius 11 cm is 0.760. One sector is 270 degrees out to 5 cm. The other is 90 degrees out to 11 cm. The free-space dose at the point is 160 cGy. What is the tissue dose, to the nearest 0.1 cGy?
A. 100.0 cGy
B. 92.8 cGy
C. 36.0 cGy
D. 121.6 cGy
Answer: A
Objective: IV.1
Why: Scatter-air ratio is TAR minus the zero-area TAR. SAR at 5 cm = 0.580 − 0.400 = 0.180. SAR at 11 cm = 0.760 − 0.400 = 0.360. The 270-degree sector is 270/360 = 0.75 of the circle, so it contributes 0.75 × 0.180 = 0.135. The 90-degree sector is 90/360 = 0.25 of the circle, so it contributes 0.25 × 0.360 = 0.090. Field SAR = 0.135 + 0.090 = 0.225. TAR = 0.400 + 0.225 = 0.625. Tissue dose = 0.625 × 160 = 100.0 cGy. Using the 5 cm TAR for the whole portal gives 0.580 × 160 = 92.8 cGy. Using the 11 cm TAR for the whole portal gives 0.760 × 160 = 121.6 cGy. Scatter alone, 0.225 × 160, gives 36.0 cGy.

## External beam Dose Calculation and Algorithms Quiz

### Q1
Stem: An irregular 6 MV portal is split into four Clarkson sectors. Clarkson sectors have SARs 0.12, 0.18, 0.1, 0.16. Average them; do not sum them. Free-space dose at the point is 100 cGy. Scatter dose = (average SAR) × free-space dose. Primary dose in the phantom at the point is 80 cGy (already the zero-area contribution). Total dose = primary + scatter. What is the total dose?
A. 98.0 cGy
B. 94.0 cGy
C. 14.0 cGy
D. 136.0 cGy
Answer: B
Objective: IV.1
Why: Average SAR = (0.12 + 0.18 + 0.1 + 0.16) / 4 = 0.56 / 4 = 0.1400. Scatter = 0.1400 × 100 = 14.00 cGy. Total = 80 + 14.00 = 94.00 cGy, reported as 94.0 cGy. Clarkson separates primary and scatter. A percent-blocked-area shortcut would not produce these sector SARs. Using the largest sector SAR instead of the average gives 98.0 cGy. Reporting only the scatter and dropping the primary gives 14.0 cGy. Summing the SARs instead of averaging them gives 136.0 cGy.

### Q2
Stem: A mantle-style blocked field is averaged over five Clarkson sectors. Clarkson sectors have SARs 0.2, 0.08, 0.14, 0.22, 0.11. Average them; do not sum them. Free-space dose at the point is 90 cGy. Scatter dose = (average SAR) × free-space dose. Primary dose in the phantom at the point is 65 cGy (already the zero-area contribution). Total dose = primary + scatter. What is the total dose?
A. 84.8 cGy
B. 13.5 cGy
C. 132.5 cGy
D. 78.5 cGy
Answer: D
Objective: IV.1
Why: Average SAR = (0.2 + 0.08 + 0.14 + 0.22 + 0.11) / 5 = 0.75 / 5 = 0.1500. Scatter = 0.1500 × 90 = 13.50 cGy. Total = 65 + 13.50 = 78.50 cGy, reported as 78.5 cGy. Clarkson separates primary and scatter. A percent-blocked-area shortcut would not produce these sector SARs. Using the largest sector SAR instead of the average gives 84.8 cGy. Reporting only the scatter and dropping the primary gives 13.5 cGy. Summing the SARs instead of averaging them gives 132.5 cGy.

### Q3
Stem: Convert a 6 MV TMR to PDD at the calibration SSD. TMR at depth 10 cm is 0.78 for the field size at that depth. SSD is 100 cm and dmax is 1.5 cm. Ignore the phantom-scatter ratio (treat Sp(rd)/Sp(r) as 1). PDD = 100 × TMR × [(SSD+dmax)/(SSD+depth)]^2. What is the PDD?
A. 66.4 %
B. 78.0 %
C. 91.6 %
D. 72.0 %
Answer: A
Objective: IV.1
Why: Inverse-square piece = [(100+1.5)/(100+10)]^2 = (101.5/110)^2 = (0.9227)^2 = 0.8514. PDD = 100 × 0.78 × 0.8514 = 66.41%, reported as 66.4 %. Mayneord's F is this same inverse-square ratio applied when SSD changes; it is not a scatter correction. Here scatter was set to 1 on purpose. Dropping the inverse-square piece and reporting 100×TMR gives 78.0 %. Inverting the distance ratio (putting depth in the numerator) gives 91.6 %, which can exceed 100% and is a sign the distances were flipped. Using the distance ratio only once, without squaring, gives 72.0 %.

### Q4
Stem: Convert a 10 MV TMR to PDD. dmax is 2.5 cm for this beam. TMR at depth 15 cm is 0.64 for the field size at that depth. SSD is 100 cm and dmax is 2.5 cm. Ignore the phantom-scatter ratio (treat Sp(rd)/Sp(r) as 1). PDD = 100 × TMR × [(SSD+dmax)/(SSD+depth)]^2. What is the PDD?
A. 64.0 %
B. 50.8 %
C. 80.6 %
D. 57.0 %
Answer: B
Objective: IV.1
Why: Inverse-square piece = [(100+2.5)/(100+15)]^2 = (102.5/115)^2 = (0.8913)^2 = 0.7944. PDD = 100 × 0.64 × 0.7944 = 50.84%, reported as 50.8 %. Mayneord's F is this same inverse-square ratio applied when SSD changes; it is not a scatter correction. Here scatter was set to 1 on purpose. Dropping the inverse-square piece and reporting 100×TMR gives 64.0 %. Inverting the distance ratio (putting depth in the numerator) gives 80.6 %, which can exceed 100% and is a sign the distances were flipped. Using the distance ratio only once, without squaring, gives 57.0 %.

### Q5
Stem: A 6 MV PDD was measured at the standard SSD and the setup will be extended. PDD at 12 cm depth is 63.5% for SSD 100 cm. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 115 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 83.7 %
B. 64.3 %
C. 65.1 %
D. 62.0 %
Answer: C
Objective: IV.1
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(115+1.5)/(100+1.5)]^2 × [(100+12)/(115+12)]^2 = (1.1478)^2 × (0.8819)^2 = 1.3174 × 0.7777 = 1.0246. PDD2 = 63.5 × 1.0246 = 65.06%, which rounds to 65.1 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 83.7 %. Multiplying the two distance ratios once each, without squaring, gives 64.3 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 62.0 %.

### Q6
Stem: During an extended-distance setup the chamber stays at dmax and only the source distance changes. The value is 180.0 cGy/min at 100 cm from the source. What is it at 160 cm if only inverse square changes?
A. 112.5 cGy/min
B. 70.3 cGy/min
C. 460.8 cGy/min
D. 500.0 cGy/min
Answer: B
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 180.0 × (100/160)^2 = 180.0 × (0.6250)^2 = 180.0 × 0.3906 = 70.3 cGy/min. Dropping the square and multiplying by the bare ratio 100/160 gives 112.5 cGy/min. Inverting the distances, (160/100)^2, gives 460.8 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (60 cm) as if it were the source distance gives 500.0 cGy/min, which is not a point on the beam axis from the source.

### Q7
Stem: Which change improves interface dose in a small lung field the most?
A. Switch from pencil beam to Monte Carlo
B. Increase the dose grid from 2 mm to 5 mm
C. Apply Mayneord F
D. Replace the equivalent square with the arithmetic mean of the jaws
Answer: A
Objective: IV.1
Why: The error is the transport model. Moving from a pencil beam to Monte Carlo changes how electrons leaving the lung interface are tracked. A coarser grid, a Mayneord factor, or an arithmetic-mean field size does not do that. Correct choice: Switch from pencil beam to Monte Carlo. A coarser grid adds sampling error. It does not fix a pencil-beam kernel. Mayneord F only rescales PDD for SSD. It does not move lateral scatter in lung. The average of the jaw settings is not even Sterling's equivalent square, and it does not restore electron equilibrium.

### Q8
Stem: A convolution algorithm and a Monte Carlo algorithm disagree by 8% beyond a large air cavity in a 3×3 cm field. Which interpretation fits the methods?
A. Trust Monte Carlo more at that cavity
B. Trust the convolution result because it has no statistical noise
C. Average them and call the average commissioned
D. The disagreement is only inverse square
Answer: A
Objective: IV.1
Why: A small field over a large cavity loses side-scatter. Monte Carlo (or a Boltzmann solver) carries that loss. Convolution/superposition is better than a pencil beam but can still miss the cavity. Absence of noise does not make the convolution dose the reference. Correct choice: Trust Monte Carlo more at that cavity. Low noise is not the same as a correct transport model. Convolution can be precisely wrong at a cavity. An average hides a known transport failure. It is not a commissioning method. Inverse square is in both calculations. The 8% gap in a small field over air is lateral disequilibrium.

## Inverse Square Tutorial

### Q1
Stem: A 6 MV output check is repeated farther from the source. The value is 200.0 cGy/min at 100 cm from the source. What is it at 150 cm if only inverse square changes?
A. 133.3 cGy/min
B. 450.0 cGy/min
C. 800.0 cGy/min
D. 88.9 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 200.0 × (100/150)^2 = 200.0 × (0.6667)^2 = 200.0 × 0.4444 = 88.9 cGy/min. Dropping the square and multiplying by the bare ratio 100/150 gives 133.3 cGy/min. Inverting the distances, (150/100)^2, gives 450.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (50 cm) as if it were the source distance gives 800.0 cGy/min, which is not a point on the beam axis from the source.

### Q2
Stem: A cobalt dose-rate constancy rig is moved from 80 cm to 100 cm. The value is 160.0 cGy/min at 80 cm from the source. What is it at 100 cm if only inverse square changes?
A. 128.0 cGy/min
B. 250.0 cGy/min
C. 102.4 cGy/min
D. 2560.0 cGy/min
Answer: C
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 160.0 × (80/100)^2 = 160.0 × (0.8000)^2 = 160.0 × 0.6400 = 102.4 cGy/min. Dropping the square and multiplying by the bare ratio 80/100 gives 128.0 cGy/min. Inverting the distances, (100/80)^2, gives 250.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (20 cm) as if it were the source distance gives 2560.0 cGy/min, which is not a point on the beam axis from the source.

### Q3
Stem: A survey meter is moved from 1 m to 2 m from a patient under treatment. Readings are in mR/h, and the number is used here as a relative intensity. The value is 48.0 mR/h at 100 cm from the source. What is it at 200 cm if only inverse square changes?
A. 24.0 mR/h
B. 12.0 mR/h
C. 192.0 mR/h
D. 48.0 mR/h
Answer: B
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 48.0 × (100/200)^2 = 48.0 × (0.5000)^2 = 48.0 × 0.2500 = 12.0 mR/h. Dropping the square and multiplying by the bare ratio 100/200 gives 24.0 mR/h. Inverting the distances, (200/100)^2, gives 192.0 mR/h and would raise the reading when the detector moves out. Using the gap between the two distances (100 cm) as if it were the source distance gives 48.0 mR/h, which is not a point on the beam axis from the source.

### Q4
Stem: An orthovoltage applicator is compared at two source distances. The value is 300.0 cGy/min at 60 cm from the source. What is it at 100 cm if only inverse square changes?
A. 108.0 cGy/min
B. 180.0 cGy/min
C. 833.3 cGy/min
D. 675.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 300.0 × (60/100)^2 = 300.0 × (0.6000)^2 = 300.0 × 0.3600 = 108.0 cGy/min. Dropping the square and multiplying by the bare ratio 60/100 gives 180.0 cGy/min. Inverting the distances, (100/60)^2, gives 833.3 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (40 cm) as if it were the source distance gives 675.0 cGy/min, which is not a point on the beam axis from the source.

### Q5
Stem: The same beam is measured closer to the source. The value is 120.0 cGy/min at 100 cm from the source. What is it at 80 cm if only inverse square changes?
A. 187.5 cGy/min
B. 150.0 cGy/min
C. 76.8 cGy/min
D. 3000.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 120.0 × (100/80)^2 = 120.0 × (1.2500)^2 = 120.0 × 1.5625 = 187.5 cGy/min. Dropping the square and multiplying by the bare ratio 100/80 gives 150.0 cGy/min. Inverting the distances, (80/100)^2, gives 76.8 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (20 cm) as if it were the source distance gives 3000.0 cGy/min, which is not a point on the beam axis from the source.

### Q6
Stem: A brachytherapy-safe survey practice problem uses inverse square only, with the reading treated as a relative rate. The value is 80.0 cGy/min at 50 cm from the source. What is it at 100 cm if only inverse square changes?
A. 20.0 cGy/min
B. 40.0 cGy/min
C. 320.0 cGy/min
D. 80.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 80.0 × (50/100)^2 = 80.0 × (0.5000)^2 = 80.0 × 0.2500 = 20.0 cGy/min. Dropping the square and multiplying by the bare ratio 50/100 gives 40.0 cGy/min. Inverting the distances, (100/50)^2, gives 320.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (50 cm) as if it were the source distance gives 80.0 cGy/min, which is not a point on the beam axis from the source.

### Q7
Stem: An extended SSD electron-cone clearance check is photon inverse-square practice at two distances. The value is 250.0 cGy/min at 100 cm from the source. What is it at 125 cm if only inverse square changes?
A. 200.0 cGy/min
B. 390.6 cGy/min
C. 4000.0 cGy/min
D. 160.0 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 250.0 × (100/125)^2 = 250.0 × (0.8000)^2 = 250.0 × 0.6400 = 160.0 cGy/min. Dropping the square and multiplying by the bare ratio 100/125 gives 200.0 cGy/min. Inverting the distances, (125/100)^2, gives 390.6 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (25 cm) as if it were the source distance gives 4000.0 cGy/min, which is not a point on the beam axis from the source.

### Q8
Stem: A total-body setup compares dose rate at 90 cm and 120 cm. The value is 180.0 cGy/min at 90 cm from the source. What is it at 120 cm if only inverse square changes?
A. 101.3 cGy/min
B. 135.0 cGy/min
C. 320.0 cGy/min
D. 1620.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 180.0 × (90/120)^2 = 180.0 × (0.7500)^2 = 180.0 × 0.5625 = 101.3 cGy/min. Dropping the square and multiplying by the bare ratio 90/120 gives 135.0 cGy/min. Inverting the distances, (120/90)^2, gives 320.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (30 cm) as if it were the source distance gives 1620.0 cGy/min, which is not a point on the beam axis from the source.

## Inverse Square Calculations

### Q1
Stem: A single open field is timed at 80 cm SSD and then moved to 100 cm. A timer setting of 1.50 min delivers the prescription at 80 cm from the source. What timer setting delivers that same dose at 100 cm, changing only inverse square and keeping dose rate × time constant in the usual way?
A. 1.88 min
B. 0.96 min
C. 2.93 min
D. 2.34 min
Answer: D
Objective: IV.1
Why: Dose rate falls with the square of distance, so time must rise with (d2/d1)^2 to keep the same dose. Substitute 1.50 × (100/80)^2 = 1.50 × (1.2500)^2 = 1.50 × 1.5625 = 2.34 min. Using the unsquared ratio (100/80) gives 1.88 min. Inverting the square, as if a larger distance needed less time, gives 0.96 min. Cubing the distance ratio instead of squaring it gives 2.93 min.

### Q2
Stem: An extended-distance treatment keeps the same dose and changes only distance. A timer setting of 2.00 min delivers the prescription at 100 cm from the source. What timer setting delivers that same dose at 130 cm, changing only inverse square and keeping dose rate × time constant in the usual way?
A. 2.60 min
B. 1.18 min
C. 3.38 min
D. 4.39 min
Answer: C
Objective: IV.1
Why: Dose rate falls with the square of distance, so time must rise with (d2/d1)^2 to keep the same dose. Substitute 2.00 × (130/100)^2 = 2.00 × (1.3000)^2 = 2.00 × 1.6900 = 3.38 min. Using the unsquared ratio (130/100) gives 2.60 min. Inverting the square, as if a larger distance needed less time, gives 1.18 min. Cubing the distance ratio instead of squaring it gives 4.39 min.

### Q3
Stem: The setup is moved closer to the source and the timer must shorten. A timer setting of 3.20 min delivers the prescription at 100 cm from the source. What timer setting delivers that same dose at 80 cm, changing only inverse square and keeping dose rate × time constant in the usual way?
A. 2.56 min
B. 2.05 min
C. 5.00 min
D. 1.64 min
Answer: B
Objective: IV.1
Why: Dose rate falls with the square of distance, so time must rise with (d2/d1)^2 to keep the same dose. Substitute 3.20 × (80/100)^2 = 3.20 × (0.8000)^2 = 3.20 × 0.6400 = 2.05 min. Using the unsquared ratio (80/100) gives 2.56 min. Inverting the square, as if a larger distance needed less time, gives 5.00 min. Cubing the distance ratio instead of squaring it gives 1.64 min.

### Q4
Stem: A near-source measurement is repeated at twice the distance. The value is 500.0 cGy/min at 40 cm from the source. What is it at 80 cm if only inverse square changes?
A. 125.0 cGy/min
B. 250.0 cGy/min
C. 2000.0 cGy/min
D. 500.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 500.0 × (40/80)^2 = 500.0 × (0.5000)^2 = 500.0 × 0.2500 = 125.0 cGy/min. Dropping the square and multiplying by the bare ratio 40/80 gives 250.0 cGy/min. Inverting the distances, (80/40)^2, gives 2000.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (40 cm) as if it were the source distance gives 500.0 cGy/min, which is not a point on the beam axis from the source.

### Q5
Stem: A low dose-rate constancy reading is taken at a greater distance. The value is 2.40 cGy/min at 100 cm from the source. What is it at 150 cm if only inverse square changes?
A. 1.60 cGy/min
B. 5.40 cGy/min
C. 9.60 cGy/min
D. 1.07 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 2.40 × (100/150)^2 = 2.40 × (0.6667)^2 = 2.40 × 0.4444 = 1.07 cGy/min. Dropping the square and multiplying by the bare ratio 100/150 gives 1.60 cGy/min. Inverting the distances, (150/100)^2, gives 5.40 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (50 cm) as if it were the source distance gives 9.60 cGy/min, which is not a point on the beam axis from the source.

### Q6
Stem: Doubling the distance from 70 cm is the whole change. The value is 210.0 cGy/min at 70 cm from the source. What is it at 140 cm if only inverse square changes?
A. 105.0 cGy/min
B. 52.5 cGy/min
C. 840.0 cGy/min
D. 210.0 cGy/min
Answer: B
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 210.0 × (70/140)^2 = 210.0 × (0.5000)^2 = 210.0 × 0.2500 = 52.5 cGy/min. Dropping the square and multiplying by the bare ratio 70/140 gives 105.0 cGy/min. Inverting the distances, (140/70)^2, gives 840.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (70 cm) as if it were the source distance gives 210.0 cGy/min, which is not a point on the beam axis from the source.

### Q7
Stem: A weekend output spot-check uses two convenient distances. The value is 360.0 cGy/min at 100 cm from the source. What is it at 180 cm if only inverse square changes?
A. 200.0 cGy/min
B. 1166.4 cGy/min
C. 562.5 cGy/min
D. 111.1 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 360.0 × (100/180)^2 = 360.0 × (0.5556)^2 = 360.0 × 0.3086 = 111.1 cGy/min. Dropping the square and multiplying by the bare ratio 100/180 gives 200.0 cGy/min. Inverting the distances, (180/100)^2, gives 1166.4 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (80 cm) as if it were the source distance gives 562.5 cGy/min, which is not a point on the beam axis from the source.

### Q8
Stem: The chamber is brought from 110 cm back to 100 cm. The value is 145.0 cGy/min at 110 cm from the source. What is it at 100 cm if only inverse square changes?
A. 159.5 cGy/min
B. 119.8 cGy/min
C. 17545.0 cGy/min
D. 175.5 cGy/min
Answer: D
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 145.0 × (110/100)^2 = 145.0 × (1.1000)^2 = 145.0 × 1.2100 = 175.5 cGy/min. Dropping the square and multiplying by the bare ratio 110/100 gives 159.5 cGy/min. Inverting the distances, (100/110)^2, gives 119.8 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (10 cm) as if it were the source distance gives 17545.0 cGy/min, which is not a point on the beam axis from the source.

## Inverse Square Quiz (Beginner)

### Q1
Stem: Beginner drill, open beam, dmax readings only. The value is 100.0 cGy/min at 100 cm from the source. What is it at 200 cm if only inverse square changes?
A. 50.0 cGy/min
B. 400.0 cGy/min
C. 25.0 cGy/min
D. 100.0 cGy/min
Answer: C
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 100.0 × (100/200)^2 = 100.0 × (0.5000)^2 = 100.0 × 0.2500 = 25.0 cGy/min. Dropping the square and multiplying by the bare ratio 100/200 gives 50.0 cGy/min. Inverting the distances, (200/100)^2, gives 400.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (100 cm) as if it were the source distance gives 100.0 cGy/min, which is not a point on the beam axis from the source.

### Q2
Stem: Beginner drill, cobalt-style distances 80 and 160 cm. The value is 125.0 cGy/min at 80 cm from the source. What is it at 160 cm if only inverse square changes?
A. 31.3 cGy/min
B. 62.5 cGy/min
C. 500.0 cGy/min
D. 125.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 125.0 × (80/160)^2 = 125.0 × (0.5000)^2 = 125.0 × 0.2500 = 31.3 cGy/min. Dropping the square and multiplying by the bare ratio 80/160 gives 62.5 cGy/min. Inverting the distances, (160/80)^2, gives 500.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (80 cm) as if it were the source distance gives 125.0 cGy/min, which is not a point on the beam axis from the source.

### Q3
Stem: Beginner drill, moving the point closer. The value is 64.0 cGy/min at 100 cm from the source. What is it at 80 cm if only inverse square changes?
A. 100.0 cGy/min
B. 80.0 cGy/min
C. 41.0 cGy/min
D. 1600.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 64.0 × (100/80)^2 = 64.0 × (1.2500)^2 = 64.0 × 1.5625 = 100.0 cGy/min. Dropping the square and multiplying by the bare ratio 100/80 gives 80.0 cGy/min. Inverting the distances, (80/100)^2, gives 41.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (20 cm) as if it were the source distance gives 1600.0 cGy/min, which is not a point on the beam axis from the source.

### Q4
Stem: Beginner drill, a fourfold distance change. The value is 20.0 cGy/min at 50 cm from the source. What is it at 100 cm if only inverse square changes?
A. 10.0 cGy/min
B. 5.0 cGy/min
C. 80.0 cGy/min
D. 20.0 cGy/min
Answer: B
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 20.0 × (50/100)^2 = 20.0 × (0.5000)^2 = 20.0 × 0.2500 = 5.0 cGy/min. Dropping the square and multiplying by the bare ratio 50/100 gives 10.0 cGy/min. Inverting the distances, (100/50)^2, gives 80.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (50 cm) as if it were the source distance gives 20.0 cGy/min, which is not a point on the beam axis from the source.

### Q5
Stem: Beginner drill, a small step out from isocenter. The value is 90.0 cGy/min at 100 cm from the source. What is it at 110 cm if only inverse square changes?
A. 74.4 cGy/min
B. 81.8 cGy/min
C. 108.9 cGy/min
D. 9000.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 90.0 × (100/110)^2 = 90.0 × (0.9091)^2 = 90.0 × 0.8264 = 74.4 cGy/min. Dropping the square and multiplying by the bare ratio 100/110 gives 81.8 cGy/min. Inverting the distances, (110/100)^2, gives 108.9 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (10 cm) as if it were the source distance gives 9000.0 cGy/min, which is not a point on the beam axis from the source.

### Q6
Stem: Beginner drill, exactly double the distance. The value is 300.0 cGy/min at 75 cm from the source. What is it at 150 cm if only inverse square changes?
A. 75.0 cGy/min
B. 150.0 cGy/min
C. 1200.0 cGy/min
D. 300.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 300.0 × (75/150)^2 = 300.0 × (0.5000)^2 = 300.0 × 0.2500 = 75.0 cGy/min. Dropping the square and multiplying by the bare ratio 75/150 gives 150.0 cGy/min. Inverting the distances, (150/75)^2, gives 1200.0 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (75 cm) as if it were the source distance gives 300.0 cGy/min, which is not a point on the beam axis from the source.

### Q7
Stem: Beginner drill, moving from 100 cm to 40 cm. The value is 45.0 cGy/min at 100 cm from the source. What is it at 40 cm if only inverse square changes?
A. 281.3 cGy/min
B. 112.5 cGy/min
C. 7.2 cGy/min
D. 125.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 45.0 × (100/40)^2 = 45.0 × (2.5000)^2 = 45.0 × 6.2500 = 281.3 cGy/min. Dropping the square and multiplying by the bare ratio 100/40 gives 112.5 cGy/min. Inverting the distances, (40/100)^2, gives 7.2 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (60 cm) as if it were the source distance gives 125.0 cGy/min, which is not a point on the beam axis from the source.

### Q8
Stem: Beginner drill, from an extended distance back toward 100 cm. The value is 80.0 cGy/min at 120 cm from the source. What is it at 100 cm if only inverse square changes?
A. 115.2 cGy/min
B. 96.0 cGy/min
C. 55.6 cGy/min
D. 2880.0 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 80.0 × (120/100)^2 = 80.0 × (1.2000)^2 = 80.0 × 1.4400 = 115.2 cGy/min. Dropping the square and multiplying by the bare ratio 120/100 gives 96.0 cGy/min. Inverting the distances, (100/120)^2, gives 55.6 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (20 cm) as if it were the source distance gives 2880.0 cGy/min, which is not a point on the beam axis from the source.

## Inverse Square Quiz (Advanced)

### Q1
Stem: Advanced set. 6 MV, dmax 1.5 cm, original SSD 100 cm. PDD at 10 cm depth is 67% for SSD 100 cm. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 120 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 96.0 %
B. 67.9 %
C. 65.3 %
D. 68.7 %
Answer: D
Objective: IV.1
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(120+1.5)/(100+1.5)]^2 × [(100+10)/(120+10)]^2 = (1.1970)^2 × (0.8462)^2 = 1.4329 × 0.7160 = 1.0259. PDD2 = 67 × 1.0259 = 68.74%, which rounds to 68.7 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 96.0 %. Multiplying the two distance ratios once each, without squaring, gives 67.9 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 65.3 %.

### Q2
Stem: Advanced set. Cobalt-60 dmax 0.5 cm, from 80 cm SSD to 100 cm SSD. PDD at 10 cm depth is 58% for SSD 80 cm. dmax is 0.5 cm. Estimate the PDD at the same depth for SSD 100 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 90.4 %
B. 60.5 %
C. 59.2 %
D. 55.6 %
Answer: B
Objective: IV.1
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(100+0.5)/(80+0.5)]^2 × [(80+10)/(100+10)]^2 = (1.2484)^2 × (0.8182)^2 = 1.5586 × 0.6694 = 1.0434. PDD2 = 58 × 1.0434 = 60.52%, which rounds to 60.5 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 90.4 %. Multiplying the two distance ratios once each, without squaring, gives 59.2 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 55.6 %.

### Q3
Stem: Advanced set. 10 MV, dmax 2.5 cm, a large SSD change where F is only a rough inverse-square estimate. PDD at 20 cm depth is 46.5% for SSD 100 cm. dmax is 2.5 cm. Estimate the PDD at the same depth for SSD 140 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 89.9 %
B. 48.5 %
C. 50.6 %
D. 42.8 %
Answer: C
Objective: IV.1
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(140+2.5)/(100+2.5)]^2 × [(100+20)/(140+20)]^2 = (1.3902)^2 × (0.7500)^2 = 1.9328 × 0.5625 = 1.0872. PDD2 = 46.5 × 1.0872 = 50.55%, which rounds to 50.6 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 89.9 %. Multiplying the two distance ratios once each, without squaring, gives 48.5 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 42.8 %.

### Q4
Stem: Advanced set. The new SSD is shorter than 100 cm, so read the ratio direction carefully. PDD at 8 cm depth is 76.4% for SSD 100 cm. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 90 cm with the Mayneord F factor. Report PDD to the nearest 0.1%.
A. 62.1 %
B. 75.4 %
C. 75.9 %
D. 77.4 %
Answer: B
Objective: IV.1
Why: Mayneord F is an inverse-square correction only. Scatter is assumed unchanged. F = [(SSD2+dm)/(SSD1+dm)]^2 × [(SSD1+d)/(SSD2+d)]^2 = [(90+1.5)/(100+1.5)]^2 × [(100+8)/(90+8)]^2 = (0.9015)^2 × (1.1020)^2 = 0.8127 × 1.2145 = 0.9870. PDD2 = 76.4 × 0.9870 = 75.40%, which rounds to 75.4 %. Keeping only the dmax ratio and dropping [(SSD1+d)/(SSD2+d)]^2 gives 62.1 %. Multiplying the two distance ratios once each, without squaring, gives 75.9 %. Swapping SSD1 and SSD2 reverses the extended-distance correction and gives 77.4 %.

### Q5
Stem: Advanced drill. Same dose, longer distance, timer only. A timer setting of 1.25 min delivers the prescription at 100 cm from the source. What timer setting delivers that same dose at 150 cm, changing only inverse square and keeping dose rate × time constant in the usual way?
A. 2.81 min
B. 1.88 min
C. 0.56 min
D. 4.22 min
Answer: A
Objective: IV.1
Why: Dose rate falls with the square of distance, so time must rise with (d2/d1)^2 to keep the same dose. Substitute 1.25 × (150/100)^2 = 1.25 × (1.5000)^2 = 1.25 × 2.2500 = 2.81 min. Using the unsquared ratio (150/100) gives 1.88 min. Inverting the square, as if a larger distance needed less time, gives 0.56 min. Cubing the distance ratio instead of squaring it gives 4.22 min.

### Q6
Stem: Advanced drill. Moving in from 90 cm to 60 cm. A timer setting of 2.40 min delivers the prescription at 90 cm from the source. What timer setting delivers that same dose at 60 cm, changing only inverse square and keeping dose rate × time constant in the usual way?
A. 1.60 min
B. 1.07 min
C. 5.40 min
D. 0.71 min
Answer: B
Objective: IV.1
Why: Dose rate falls with the square of distance, so time must rise with (d2/d1)^2 to keep the same dose. Substitute 2.40 × (60/90)^2 = 2.40 × (0.6667)^2 = 2.40 × 0.4444 = 1.07 min. Using the unsquared ratio (60/90) gives 1.60 min. Inverting the square, as if a larger distance needed less time, gives 5.40 min. Cubing the distance ratio instead of squaring it gives 0.71 min.

### Q7
Stem: Advanced survey-style inverse square. No tissue attenuation is included. The value is 18.0 mR/h at 100 cm from the source. What is it at 40 cm if only inverse square changes?
A. 45.0 mR/h
B. 2.9 mR/h
C. 112.5 mR/h
D. 50.0 mR/h
Answer: C
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 18.0 × (100/40)^2 = 18.0 × (2.5000)^2 = 18.0 × 6.2500 = 112.5 mR/h. Dropping the square and multiplying by the bare ratio 100/40 gives 45.0 mR/h. Inverting the distances, (40/100)^2, gives 2.9 mR/h and would raise the reading when the detector moves out. Using the gap between the two distances (60 cm) as if it were the source distance gives 50.0 mR/h, which is not a point on the beam axis from the source.

### Q8
Stem: Advanced long-distance inverse square from 100 cm to 250 cm. The value is 5.00 cGy/min at 100 cm from the source. What is it at 250 cm if only inverse square changes?
A. 0.80 cGy/min
B. 2.00 cGy/min
C. 31.25 cGy/min
D. 2.22 cGy/min
Answer: A
Objective: IV.1
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 5.00 × (100/250)^2 = 5.00 × (0.4000)^2 = 5.00 × 0.1600 = 0.80 cGy/min. Dropping the square and multiplying by the bare ratio 100/250 gives 2.00 cGy/min. Inverting the distances, (250/100)^2, gives 31.25 cGy/min and would raise the reading when the detector moves out. Using the gap between the two distances (150 cm) as if it were the source distance gives 2.22 cGy/min, which is not a point on the beam axis from the source.
