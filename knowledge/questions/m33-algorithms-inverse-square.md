# Module 33 — External beam dose calculation and algorithms

Original items. Source distances are from the source to the point. Depth is named separately and is added to SSD before inverse square. Clarkson weights use the fraction of a full circle.

## Dose Calculation and Algorithms

### Q1
Stem: An irregular mantle is planned by splitting the tissue-air ratio into a zero-area term and a scatter-air term, then adding them. Which method is that?
A. A pencil-beam kernel with no lateral transport
B. Clarkson sector integration
C. A grid-based Boltzmann solver
D. Mayneord F applied to a TMR
Answer: B
Objective: IV.1
Why: Clarkson writes TAR(d, r) = TAR(d, 0) + SAR(d, r). The zero-area TAR is primary. The SAR is scatter, summed over sectors as SAR times the fraction of the circle. A pencil beam does not make that split. A Boltzmann solver transports particles. Mayneord F adjusts a PDD between two SSDs and is not a scatter integration.

### Q2
Stem: Which algorithm is the weak choice in lung because heterogeneity is applied mostly along each ray and lateral scatter is poor?
A. Monte Carlo with adequate histories
B. Collapsed-cone superposition
C. Pencil beam
D. A grid-based Boltzmann solver with the correct material
Answer: C
Objective: IV.1
Why: A pencil beam can stretch the path length and still fail to move energy sideways into or out of lung. Superposition and collapsed cone scale a scatter kernel. Monte Carlo and a Boltzmann solver transport radiation through the interface. Path-length correction alone does not make a pencil beam adequate in lung.

### Q3
Stem: At a metal–tissue interface, which method handles buildup and backscatter best when the material is assigned correctly and the histories are adequate?
A. Monte Carlo
B. A correction-based hand calculation that only scales equivalent depth
C. Percent of the field area that is blocked
D. An open-beam PDD with no heterogeneity term
Answer: A
Objective: IV.1
Why: Monte Carlo follows interactions, so interface buildup and backscatter from metal are in the histories. Equivalent depth is a path-length correction. Percent blocked is not a scatter calculation. An open-water PDD never sees the metal.

### Q4
Stem: At the depth of interest, TAR(d, 0) = 0.420. The field is two 180° sectors. One has SAR = 0.160 and the other has SAR = 0.240. What is the field TAR?
A. 0.200
B. 0.400
C. 0.620
D. 0.820
Answer: C
Objective: IV.1
Why: Each 180° sector is half a circle, so the weight is 0.5. SAR_field = 0.5(0.160) + 0.5(0.240) = 0.080 + 0.120 = 0.200. TAR = 0.420 + 0.200 = 0.620. 0.200 is scatter alone. 0.400 drops the primary to 0.200 and adds scatter. 0.820 adds the unweighted SARs (0.160 + 0.240) to 0.420.

### Q5
Stem: Dose along a cord, sampled every 2 mm, reads 46.0, 49.5, 53.8, 50.1, and 46.4 Gy. A 6 mm grid keeps only the first and fourth samples. By how many gray does that grid under-report the peak?
A. 3.7 Gy
B. 4.3 Gy
C. 7.8 Gy
D. 0 Gy, because a DVH maximum is independent of grid size
Answer: A
Objective: IV.6
Why: The fine-sample peak is 53.8 Gy. The coarse grid reports max(46.0, 50.1) = 50.1 Gy. The miss is 53.8 − 50.1 = 3.7 Gy. 4.3 Gy is 53.8 − 49.5, a neighboring fine sample that the coarse grid also skipped. 7.8 Gy subtracts 46.0 from 53.8. A DVH built on the coarse grid inherits 50.1 Gy and cannot prove the peak was resolved.

## External beam Dose Calculation and Algorithms Quiz

### Q1
Stem: Four 90° sectors have SAR values 0.100, 0.180, 0.220, and 0.140. What is the field SAR?
A. 0.640
B. 0.160
C. 0.320
D. 0.090
Answer: B
Objective: IV.1
Why: Each 90° sector is 90/360 = 0.25 of the circle. The SAR sum is 0.100 + 0.180 + 0.220 + 0.140 = 0.640. Field SAR = 0.25 × 0.640 = 0.160. 0.640 forgets the angular weight. 0.320 uses a weight of 0.5 as if each sector were a half-field. 0.090 is 0.640/7.1, not a sector fraction.

### Q2
Stem: TAR(d, 0) = 0.500. Three 120° sectors have SAR = 0.210, 0.270, and 0.150. What is the field TAR?
A. 0.210
B. 0.630
C. 0.710
D. 1.130
Answer: C
Objective: IV.1
Why: Each 120° sector is 120/360 = 1/3 of the circle. SAR_field = (0.210 + 0.270 + 0.150) / 3 = 0.630 / 3 = 0.210. TAR = 0.500 + 0.210 = 0.710. 0.210 is scatter alone. 0.630 adds the unweighted SAR sum to nothing and drops primary. 1.130 adds the unweighted sum 0.630 to the primary 0.500.

### Q3
Stem: A serial-organ maximum on a 2 mm sample is 51.6 Gy. A 5 mm grid’s nearest samples are 48.4 Gy and 49.9 Gy. What maximum does the coarse grid report, and what peak did it miss?
A. It reports 51.6 Gy and misses nothing
B. It reports 49.9 Gy and misses 1.7 Gy
C. It reports 48.4 Gy and misses 3.2 Gy
D. It reports 49.2 Gy, the average of 48.4 and 49.9
Answer: B
Objective: IV.6
Why: The grid stores the samples it hits. The higher stored sample is 49.9 Gy, not the average and not the unseen 51.6 Gy. Missed peak = 51.6 − 49.9 = 1.7 Gy. 51.6 − 48.4 = 3.2 Gy uses the lower neighbor. Averaging the two coarse samples gives (48.4 + 49.9) / 2 = 49.15 Gy, which is not how a maximum is taken.

### Q4
Stem: A blocked field covers 70% of a 10 × 10 cm² open field. Which statement is the scatter calculation the board is testing?
A. The equivalent square is 7 cm because 0.70 × 10 = 7
B. Scatter must be integrated by sector (Clarkson); percent blocked is not that integral
C. The field is a 7 × 7 cm² square for both Sc and Sp
D. PDD falls by 30% because 30% of the area is blocked
Answer: B
Objective: IV.1
Why: Clarkson weights each sector’s SAR by its angle over 2π. Area percent ignores where the block sits and how much scatter each radius contributes. 0.70 × 10 = 7 changes a side length, not a scatter integral. Jaws and the blocked opening also set different factors (Sc versus Sp). A 30% area block does not subtract 30 percentage points from PDD.

### Q5
Stem: Zero-area TAR at the depth is 0.360. A full circle has SAR = 0.250. A block removes a 90° sector whose SAR at that radius would have been 0.250, and the remaining radii are unchanged. What is the blocked-field TAR?
A. 0.360
B. 0.548
C. 0.610
D. 0.673
Answer: B
Objective: IV.1
Why: The removed sector is 90/360 = 0.25 of the circle, so the scatter removed is 0.25 × 0.250 = 0.0625. Remaining SAR = 0.250 − 0.0625 = 0.1875. TAR = 0.360 + 0.1875 = 0.5475, which is 0.548 Gy-free TAR units to three decimals. 0.610 is primary plus the full SAR (0.360 + 0.250). 0.673 adds the removed piece instead of subtracting it (0.610 + 0.0625). 0.360 drops all scatter.

### Q6
Stem: A planner describes the model as “energy released in the patient is spread with a kernel that stretches when density falls.” Which family is that?
A. Pencil beam
B. Convolution/superposition
C. Timer error on a cobalt unit
D. Sterling’s equivalent square
Answer: B
Objective: IV.1
Why: Convolution and superposition, including collapsed cone, transport scatter with a kernel and stretch that kernel in low density. A pencil beam does not move that scatter sideways. Timer error and equivalent square are not dose engines.

### Q7
Stem: Along a 2 mm cord sample the doses are 47.2, 50.0, 55.0, 51.4, and 48.0 Gy. A grid that keeps only 47.2 and 51.4 reports which maximum?
A. 55.0 Gy
B. 51.4 Gy
C. 50.4 Gy
D. 47.2 Gy
Answer: B
Objective: IV.6
Why: The reported maximum is the larger stored sample, 51.4 Gy. The true peak 55.0 Gy sits between those samples. The miss is 55.0 − 51.4 = 3.6 Gy. 50.4 Gy is the average of 47.2 and 55.0 and is not a grid sample. 47.2 Gy is the lower stored sample.

### Q8
Stem: AAA, a pencil beam, and Monte Carlo are all available. The beam crosses lung next to mediastinum, and the question is interface dose. Rank them from strongest to weakest for that interface.
A. Pencil beam, AAA, Monte Carlo
B. Monte Carlo, AAA, pencil beam
C. AAA, pencil beam, Monte Carlo
D. All three are equivalent once the CT number is in the file
Answer: B
Objective: IV.1
Why: Monte Carlo transports particles through the lung–tissue boundary. AAA has lateral kernels and is stronger than a pure pencil beam, but it is still an analytical model at a hard interface. A pencil beam’s lateral scatter is the weak step. A correct CT number does not make those three engines the same.

## Inverse Square Tutorial

### Q1
Stem: A beam delivers 300 cGy/min at 100 cm from the source. Inverse square only, what is the dose rate at 200 cm?
A. 150 cGy/min
B. 75 cGy/min
C. 1200 cGy/min
D. 600 cGy/min
Answer: B
Objective: I.10
Why: I2 = 300 × (100/200)^2 = 300 × (0.5)^2 = 300 × 0.25 = 75 cGy/min. 150 cGy/min uses the ratio once and does not square it. 1200 cGy/min inverts the distances and squares (300 × 4). 600 cGy/min inverts the ratio without squaring.

### Q2
Stem: The dose rate is 120 cGy/min at 80 cm from the source. Inverse square only, what is the dose rate at 40 cm?
A. 60 cGy/min
B. 240 cGy/min
C. 480 cGy/min
D. 30 cGy/min
Answer: C
Objective: I.10
Why: I2 = 120 × (80/40)^2 = 120 × 2^2 = 120 × 4 = 480 cGy/min. 240 cGy/min forgets the square. 60 cGy/min halves the rate because the distance was halved, which is the wrong direction. 30 cGy/min applies (40/80)^2.

### Q3
Stem: 250 cGy is delivered at 100 cm from the source. The same beam-on time is used at 125 cm. Inverse square only, what dose is delivered?
A. 160 cGy
B. 200 cGy
C. 312.5 cGy
D. 390.6 cGy
Answer: A
Objective: I.10
Why: Dose tracks dose rate at fixed time. D2 = 250 × (100/125)^2 = 250 × 0.8^2 = 250 × 0.64 = 160 cGy. 200 cGy is 250 × 0.8, unsquared. 312.5 cGy is 250 × (125/100)^2, the nearer point. 390.6 cGy is 250 / 0.64.

### Q4
Stem: Dose rate at 100 cm from the source is 500 cGy/min. Inverse square only, what is the rate at 50 cm?
A. 250 cGy/min
B. 1000 cGy/min
C. 125 cGy/min
D. 2000 cGy/min
Answer: D
Objective: I.10
Why: I2 = 500 × (100/50)^2 = 500 × 4 = 2000 cGy/min. 1000 cGy/min uses the unsquared ratio of 2. 250 cGy/min and 125 cGy/min move the point farther, not closer.

### Q5
Stem: A point 200 cm from the source reads 64 cGy/min. Inverse square only, what is the rate at 100 cm?
A. 32 cGy/min
B. 128 cGy/min
C. 16 cGy/min
D. 256 cGy/min
Answer: D
Objective: I.10
Why: I2 = 64 × (200/100)^2 = 64 × 4 = 256 cGy/min. Check: 256 × (100/200)^2 = 256 × 0.25 = 64. 128 cGy/min drops the square. 32 cGy/min and 16 cGy/min apply the farther-point factor.

### Q6
Stem: Dose rate is 180 cGy/min at 90 cm from the source. Inverse square only, what is the rate at 60 cm?
A. 120 cGy/min
B. 270 cGy/min
C. 405 cGy/min
D. 80 cGy/min
Answer: C
Objective: I.10
Why: I2 = 180 × (90/60)^2 = 180 × (1.5)^2 = 180 × 2.25 = 405 cGy/min. 270 cGy/min is 180 × 1.5, unsquared. 120 cGy/min is 180 × (60/90). 80 cGy/min is 180 × (60/90)^2, which is the rate if the known point and the unknown point are swapped.

### Q7
Stem: The rate is 1000 cGy/min at 100 cm from the source. Inverse square only, what is the rate at 250 cm?
A. 400 cGy/min
B. 160 cGy/min
C. 250 cGy/min
D. 6250 cGy/min
Answer: B
Objective: I.10
Why: I2 = 1000 × (100/250)^2 = 1000 × (0.4)^2 = 1000 × 0.16 = 160 cGy/min. 400 cGy/min is 1000 × 0.4, unsquared. 250 cGy/min divides by 4. 6250 cGy/min inverts the distance ratio (1000 / 0.16).

### Q8
Stem: The same beam-on time delivers 80 cGy at 40 cm from the source. At what distance is the dose 20 cGy? Inverse square only.
A. 20 cm
B. 80 cm
C. 160 cm
D. 10 cm
Answer: B
Objective: I.10
Why: 80/20 = 4 = (d2/40)^2, so d2/40 = 2 and d2 = 80 cm. Check: 80 × (40/80)^2 = 80 × 0.25 = 20. 20 cm would raise the dose by a factor of 4, to 320 cGy. 160 cm is another factor of 4 farther (5 cGy). 10 cm is a quarter of 40 cm, not double.

## Inverse Square Calculations

### Q1
Stem: Dose rate at 100 cm from the source is 243 cGy/min. A calculation point has SSD = 80 cm and depth = 10 cm. Inverse square only, what is the dose rate at that point?
A. 300 cGy/min
B. 380 cGy/min
C. 243 cGy/min
D. 197 cGy/min
Answer: A
Objective: IV.1
Why: Source distance is SSD + depth = 80 + 10 = 90 cm, not 80 cm and not the depth alone. I2 = 243 × (100/90)^2 = 243 × (10/9)^2 = 243 × 100/81. 243/81 = 3, so I2 = 300 cGy/min. Check: 300 × (90/100)^2 = 300 × 0.81 = 243. Using SSD alone gives 243 × (100/80)^2 = 380 cGy/min, a skin point. 197 cGy/min is 243 × (90/100)^2, the ratio inverted.

### Q2
Stem: Dose rate is 200 cGy/min at 80 cm from the source. What is the rate at the skin for SSD = 100 cm if depth is zero? Inverse square only.
A. 250 cGy/min
B. 128 cGy/min
C. 160 cGy/min
D. 312.5 cGy/min
Answer: B
Objective: IV.1
Why: The skin point is 100 cm from the source. I2 = 200 × (80/100)^2 = 200 × 0.64 = 128 cGy/min. 160 cGy/min is 200 × 0.8, unsquared. 250 cGy/min is 200 × (100/80). 312.5 cGy/min is 200 × (100/80)^2, which moves the point closer.

### Q3
Stem: 150 cGy is given at 100 cm from the source. The same time is used at a point 80 cm from the source. Inverse square only, what dose is given?
A. 120 cGy
B. 187.5 cGy
C. 96 cGy
D. 234.4 cGy
Answer: D
Objective: IV.1
Why: D2 = 150 × (100/80)^2 = 150 × 1.5625 = 234.375 cGy, which is 234.4 cGy to one decimal. 187.5 cGy is 150 × 1.25, a linear guess. 120 cGy is 150 × 0.8. 96 cGy is 150 × 0.64, the farther-point factor.

### Q4
Stem: Dose rate at isocenter, 100 cm from the source, is 288 cGy/min. The point has SSD = 100 cm and depth = 20 cm. Inverse square only, what is the rate at the point?
A. 288 cGy/min
B. 240 cGy/min
C. 200 cGy/min
D. 415 cGy/min
Answer: C
Objective: IV.1
Why: Source distance is 100 + 20 = 120 cm. I2 = 288 × (100/120)^2 = 288 × (5/6)^2 = 288 × 25/36. 288/36 = 8, and 8 × 25 = 200 cGy/min. 240 cGy/min is 288 × (100/120), unsquared. 415 cGy/min is about 288 × (120/100)^2. Leaving the depth off the distance keeps 288 cGy/min, which is the skin, not the point at 20 cm.

### Q5
Stem: A reading is 360 cGy/min at an unknown source distance and 90 cGy/min at 200 cm from the source. Inverse square only, what is the unknown distance?
A. 50 cm
B. 100 cm
C. 400 cm
D. 800 cm
Answer: B
Objective: IV.1
Why: 360/90 = 4 = (200/d)^2, so 200/d = 2 and d = 100 cm. Check: 360 × (100/200)^2 = 90. 50 cm would be another factor of 4 higher (1440 cGy/min). 400 cm applies the square root on the wrong side. 800 cm forgets the square root entirely (200 × 4).

### Q6
Stem: Dose rate at 100 cm from the source is 144 cGy/min. SSD = 100 cm and depth = 20 cm. Inverse square only, what is the rate at depth?
A. 100 cGy/min
B. 120 cGy/min
C. 144 cGy/min
D. 207 cGy/min
Answer: A
Objective: IV.1
Why: d2 = 100 + 20 = 120 cm. I2 = 144 × (100/120)^2 = 144 × 25/36 = 100 cGy/min. 120 cGy/min is 144 × (100/120). 207 cGy/min is 144 × (120/100)^2. 144 cGy/min is the rate at the skin, where the source distance is still 100 cm.

### Q7
Stem: 100 cGy is delivered at 100 cm from the source in a fixed time. The same time is used at 80 cm. Inverse square only, what dose is delivered?
A. 80 cGy
B. 125 cGy
C. 64 cGy
D. 156.25 cGy
Answer: D
Objective: IV.1
Why: D2 = 100 × (100/80)^2 = 100 × 1.5625 = 156.25 cGy. Check: 156.25 × (80/100)^2 = 156.25 × 0.64 = 100. 125 cGy is 100 × 1.25. 80 cGy and 64 cGy move the point out, not in.

### Q8
Stem: A stem says the only change is source-to-point distance, from 100 cm to 80 cm, and asks for the dose-rate factor. Which factor is that?
A. Mayneord F, because every distance change is a PDD correction
B. (100/80)^2 = 1.5625
C. 80/100 = 0.80
D. A TMR looked up at 80 cm depth
Answer: B
Objective: IV.1
Why: Inverse square alone multiplies the rate by (d1/d2)^2 = (100/80)^2 = 1.5625. Mayneord F changes a PDD from one SSD to another and does not replace this dose-rate ratio. 0.80 is the unsquared distance ratio, and it points the wrong way. TMR is a tissue ratio at fixed source distance, not a distance correction, and 80 cm is not a depth in this stem.

## Inverse Square Quiz (Beginner)

### Q1
Stem: Dose rate is 600 cGy/min at 100 cm from the source. Inverse square only, what is the rate at 150 cm?
A. 400 cGy/min
B. 266.7 cGy/min
C. 900 cGy/min
D. 1350 cGy/min
Answer: B
Objective: I.10
Why: I2 = 600 × (100/150)^2 = 600 × (2/3)^2 = 600 × 4/9 = 2400/9 = 266.7 cGy/min. 400 cGy/min is 600 × 2/3, unsquared. 900 cGy/min is 600 × 1.5. 1350 cGy/min is 600 × (150/100)^2.

### Q2
Stem: The rate is 48 cGy/min at 160 cm from the source. Inverse square only, what is the rate at 80 cm?
A. 24 cGy/min
B. 96 cGy/min
C. 12 cGy/min
D. 192 cGy/min
Answer: D
Objective: I.10
Why: I2 = 48 × (160/80)^2 = 48 × 4 = 192 cGy/min. 96 cGy/min drops the square. 24 cGy/min and 12 cGy/min treat the closer point as if it were farther.

### Q3
Stem: Dose rate is 225 cGy/min at 75 cm from the source. Inverse square only, what is the rate at 150 cm?
A. 112.5 cGy/min
B. 450 cGy/min
C. 56.25 cGy/min
D. 900 cGy/min
Answer: C
Objective: I.10
Why: I2 = 225 × (75/150)^2 = 225 × (0.5)^2 = 225 × 0.25 = 56.25 cGy/min. 112.5 cGy/min is 225 × 0.5. 450 cGy/min doubles the rate. 900 cGy/min is 225 × 4, the closer-point factor.

### Q4
Stem: 100 cGy is delivered at 50 cm from the source. The same time is used at 100 cm. Inverse square only, what dose is delivered?
A. 50 cGy
B. 25 cGy
C. 200 cGy
D. 400 cGy
Answer: B
Objective: I.10
Why: D2 = 100 × (50/100)^2 = 100 × 0.25 = 25 cGy. 50 cGy forgets the square. 200 cGy and 400 cGy invert the distance ratio.

### Q5
Stem: The rate is 320 cGy/min at 100 cm from the source. Inverse square only, what is the rate at 80 cm?
A. 256 cGy/min
B. 400 cGy/min
C. 500 cGy/min
D. 205 cGy/min
Answer: C
Objective: I.10
Why: I2 = 320 × (100/80)^2 = 320 × 1.5625 = 500 cGy/min. Check: 500 × 0.64 = 320. 400 cGy/min is 320 × 1.25, unsquared. 256 cGy/min is 320 × 0.8. 205 cGy/min is 320 × 0.64, the factor for moving out to 125 cm, not in to 80 cm.

### Q6
Stem: Dose rate is 144 cGy/min at 60 cm from the source. Inverse square only, what is the rate at 90 cm?
A. 96 cGy/min
B. 64 cGy/min
C. 216 cGy/min
D. 324 cGy/min
Answer: B
Objective: I.10
Why: I2 = 144 × (60/90)^2 = 144 × (2/3)^2 = 144 × 4/9 = 64 cGy/min. 96 cGy/min is 144 × 2/3. 216 cGy/min is 144 × 1.5. 324 cGy/min is 144 × (90/60)^2.

### Q7
Stem: Moving a point from 100 cm to 200 cm from the source, inverse square only, multiplies dose rate by:
A. 1/2
B. 1/4
C. 2
D. 4
Answer: B
Objective: I.10
Why: (100/200)^2 = 1/4. The unsquared ratio is 1/2. The factors 2 and 4 are the multipliers for moving from 200 cm in to 100 cm.

### Q8
Stem: A calculation keeps the unit cGy/min and changes only the source distance from 100 cm to 50 cm. The rate was 40 cGy/min. What is the new rate?
A. 10 cGy/min
B. 20 cGy/min
C. 80 cGy/min
D. 160 cGy/min
Answer: D
Objective: I.10
Why: 40 × (100/50)^2 = 40 × 4 = 160 cGy/min. The unit stays cGy/min. 80 cGy/min is 40 × 2. 20 cGy/min and 10 cGy/min apply the factor for a farther point.

## Inverse Square Quiz (Advanced)

### Q1
Stem: Dose rate at 100 cm from the source is 220 cGy/min. The point has SSD = 85 cm and depth = 15 cm. Inverse square only, what is the rate?
A. 305 cGy/min
B. 220 cGy/min
C. 187 cGy/min
D. 159 cGy/min
Answer: B
Objective: IV.1
Why: Source distance = 85 + 15 = 100 cm, the same distance as the known rate, so the inverse-square factor is (100/100)^2 = 1 and the rate stays 220 cGy/min. 305 cGy/min is 220 × (100/85)^2, which is the skin. 187 cGy/min uses depth 15 cm as the whole distance in a rough ratio. 159 cGy/min is 220 × (85/100)^2.

### Q2
Stem: Dose rate at 100 cm from the source is 144 cGy/min. SSD = 110 cm and depth = 10 cm. Inverse square only, what is the rate at the point?
A. 144 cGy/min
B. 120 cGy/min
C. 100 cGy/min
D. 207 cGy/min
Answer: C
Objective: IV.1
Why: d2 = 110 + 10 = 120 cm. I2 = 144 × (100/120)^2 = 144 × 25/36 = 100 cGy/min. 120 cGy/min drops the square. 207 cGy/min is 144 × (120/100)^2. 144 cGy/min would be correct only if the point were 100 cm from the source.

### Q3
Stem: Dose rate is 400 cGy/min at 100 cm from the source and 25 cGy/min at an unknown distance. Inverse square only, what is that distance?
A. 200 cm
B. 400 cm
C. 1600 cm
D. 50 cm
Answer: B
Objective: IV.1
Why: 400/25 = 16 = (d/100)^2, so d/100 = 4 and d = 400 cm. Check: 400 × (100/400)^2 = 400 × 1/16 = 25. 200 cm gives a factor of 4, so 100 cGy/min, not 25. 1600 cm multiplies by 16 without the square root. 50 cm is closer and would read 1600 cGy/min.

### Q4
Stem: Dose rate at 100 cm from the source is 100 cGy/min. SSD = 60 cm and depth = 20 cm. Inverse square only, what is the rate at depth?
A. 100 cGy/min
B. 278 cGy/min
C. 156.25 cGy/min
D. 64 cGy/min
Answer: C
Objective: IV.1
Why: d2 = 60 + 20 = 80 cm. I2 = 100 × (100/80)^2 = 156.25 cGy/min. 278 cGy/min is 100 × (100/60)^2, the skin at SSD 60 cm. 64 cGy/min is 100 × (80/100)^2, the ratio inverted. 100 cGy/min ignores the shorter source distance.

### Q5
Stem: A pure dose-rate question changes only the distance from the source. A classmate multiplies by Mayneord F. What is wrong with that step?
A. Nothing; Mayneord F is the inverse-square dose-rate formula
B. Mayneord F adjusts a percent depth dose between two SSDs and does not replace I2 = I1 (d1/d2)^2
C. Mayneord F is a scatter correction and should be used instead of any distance term
D. Mayneord F converts a TMR into a PDD
Answer: B
Objective: IV.1
Why: Mayneord F is ((SSD2 + dm)/(SSD1 + dm))^2 × ((SSD1 + d)/(SSD2 + d))^2, applied to a PDD. It corrects inverse square inside that percent. It is not the dose rate at a new source distance, it does not correct scatter, and it is not applied to TMR.

### Q6
Stem: You compute 200 cGy/min at 120 cm from a known 288 cGy/min at 100 cm. Which reverse check confirms it?
A. 200 × (120/100) = 240, close enough to 288
B. 200 × (120/100)^2 = 288
C. 200 × (100/120)^2 = 288
D. 288 − 120 = 168, so the rate should have been 168
Answer: B
Objective: IV.1
Why: I1 = I2 × (d2/d1)^2 = 200 × (120/100)^2 = 200 × 1.44 = 288 cGy/min. The unsquared check gives 240, which does not recover 288. Multiplying by (100/120)^2 makes the number smaller (138.9). Subtracting the distances is not inverse square.

### Q7
Stem: Dose rate at 100 cm from the source is 162 cGy/min. SSD = 90 cm and depth = 10 cm. Inverse square only, what is the rate at the point?
A. 162 cGy/min
B. 200 cGy/min
C. 131 cGy/min
D. 180 cGy/min
Answer: A
Objective: IV.1
Why: Source distance = 90 + 10 = 100 cm, so the factor is 1 and the rate remains 162 cGy/min. Using the SSD alone gives 162 × (100/90)^2 = 162 × 100/81 = 200 cGy/min, which is the skin. 131 cGy/min is 162 × (90/100)^2. 180 cGy/min is 162 × (100/90), unsquared.

### Q8
Stem: 80 cGy is delivered at 200 cm from the source. The same time is used at 100 cm. Inverse square only, what dose is delivered?
A. 40 cGy
B. 160 cGy
C. 20 cGy
D. 320 cGy
Answer: D
Objective: IV.1
Why: D2 = 80 × (200/100)^2 = 80 × 4 = 320 cGy. Check: 320 × (100/200)^2 = 80. 160 cGy drops the square. 40 cGy and 20 cGy apply the factor for moving farther away.
