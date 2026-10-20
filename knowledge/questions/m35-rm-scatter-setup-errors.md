# Module 35. PDD, TMR, and MU calculations

Original items. Scatter-maximum ratio and zero-area TMR, set-up errors as delivered dose, weighted isocentric fields with a back-solved normalization, and electron range rules used inside a calculation.

## Scatter-Maximum Ratio and Zero-Area TMR

### Q1
Stem: At 10 cm depth a 10 MV beam has a tissue-maximum ratio of 0.812 for the 15 by 15 cm field at the point. The zero-area tissue-maximum ratio at that depth is 0.705. What is the scatter-maximum ratio?
A. 0.868
B. 0.188
C. 0.107
D. 1.517
Answer: C
Objective: IV.1
Why: The scatter-maximum ratio is the full-field TMR minus the zero-area (primary-only) TMR: 0.812 − 0.705 = 0.107. Check: 0.705 + 0.107 = 0.812. Dividing the two TMRs, 0.705/0.812, gives 0.868, which is the primary fraction of the dose, not the scatter term. Subtracting the TMR from 1 gives 0.188, which is the total attenuation and scatter loss between dmax and 10 cm, not the scatter contribution. Adding the two gives 1.517, which has no meaning.

### Q2
Stem: On an isocentric ray the dose at dmax is 240 cGy. At the calculation depth the tissue-maximum ratio for the treated field is 0.812 and the zero-area tissue-maximum ratio is 0.705. How much of the dose at the calculation point is phantom scatter, to the nearest 0.1 cGy?
A. 25.7 cGy
B. 169.2 cGy
C. 194.9 cGy
D. 45.1 cGy
Answer: A
Objective: IV.1
Why: Scatter dose is the dmax dose times the scatter-maximum ratio: 240 × (0.812 − 0.705) = 240 × 0.107 = 25.7 cGy. Check: primary 240 × 0.705 = 169.2 cGy, and 169.2 + 25.7 = 194.9 cGy, which equals 240 × 0.812. Reporting 169.2 cGy gives the primary dose instead. Reporting 194.9 cGy gives the total dose at the point. Using 1 − 0.812 = 0.188 as if it were the scatter ratio gives 45.1 cGy.

### Q3
Stem: A beam has an effective linear attenuation coefficient of 0.045 per centimeter in water and a dmax of 2.5 cm. What is the zero-area tissue-maximum ratio at 14 cm depth, to three decimals?
A. 0.533
B. 0.483
C. 0.894
D. 0.596
Answer: D
Objective: IV.1
Why: The primary-only TMR is the exponential attenuation over the thickness between dmax and the point, 14 − 2.5 = 11.5 cm: exponent 0.045 × 11.5 = 0.5175, and e to the minus 0.5175 is 0.596. Check: the natural log of 0.596 is −0.5175, and 0.5175/0.045 = 11.5 cm. Measuring the thickness from the surface, 0.045 × 14 = 0.63, gives 0.533. Replacing the exponential with linear attenuation, 1 − 0.5175, gives 0.483. Attenuating over dmax alone, 0.045 × 2.5, gives 0.894.

### Q4
Stem: In a convolution or superposition photon algorithm, which quantity is spread by the stored dose-deposition kernel to produce the dose distribution?
A. KERMA, the kinetic energy transferred to charged particles only
B. TERMA, the total energy released per unit mass by primary photon interactions
C. The scatter-air ratio summed over Clarkson sectors
D. The percent depth dose measured in water at the reference SSD
Answer: B
Objective: IV.1
Why: The engine first computes TERMA, the total energy released per unit mass where primary photons interact, and then convolves it with a kernel that describes how that energy spreads as scattered photons and electrons. KERMA counts only the energy handed to charged particles and omits the energy carried away by scattered photons, so it is not the quantity the kernel acts on. Clarkson sector sums are a correction-based method, not a kernel input. A measured PDD is a correction-based lookup and is not convolved with anything.

### Q5
Stem: Two photon algorithms from the same vendor are offered in a planning system. One is an analytical kernel model with lateral scatter corrections; the other solves the linear Boltzmann transport equation on the dose grid. Which pairing is correct?
A. AAA is the Boltzmann solver and Acuros XB is the analytical kernel model
B. Both are forms of Monte Carlo that differ only in the number of histories
C. Acuros XB is the analytical kernel model and AAA is a Monte Carlo code
D. AAA is the analytical kernel model and Acuros XB is the deterministic Boltzmann solver
Answer: D
Objective: IV.1
Why: AAA, the anisotropic analytical algorithm, is a convolution-type analytical model that scales kernels for lateral scatter; Acuros XB solves the linear Boltzmann transport equation deterministically through each voxel's assigned material, which is why its results sit close to Monte Carlo in lung and bone. Swapping the two names is the common trap. Neither code is Monte Carlo; Monte Carlo samples random particle histories, whereas Acuros is deterministic and AAA is analytical. Labeling AAA a Monte Carlo code and Acuros a kernel model inverts both facts.

## SSD and SAD Setup Errors as Delivered Dose

### Q1
Stem: An 18 MV unit is calibrated to deliver 1.000 cGy per MU at dmax, 3.3 cm, with the phantom surface at 100 cm from the source. For a 200 cGy isocentric fraction the MU were computed as if the unit delivered 1.000 cGy per MU with dmax placed 100 cm from the source. Considering inverse square only, what dose did the isocentric point receive, to the nearest 0.1 cGy?
A. 187.4 cGy
B. 213.4 cGy
C. 206.6 cGy
D. 200.0 cGy
Answer: B
Objective: IV.3
Why: With the surface at 100 cm, the calibration dmax is 103.3 cm from the source; moving dmax in to 100 cm raises the output by (103.3/100)² = 1.067 cGy per MU. The MU were set for 1.000 cGy per MU, so the point received 200 × 1.067 = 213.4 cGy, 6.7% high. Check: 1.033 squared is 1.0671, and 200 × 0.0671 = 13.4 cGy extra. Dividing by the factor, 200/1.067, gives 187.4 cGy and reverses the direction of the error. Using the unsquared ratio 1.033 gives 206.6 cGy. Reporting 200.0 cGy ignores the calibration geometry.

### Q2
Stem: An isocentric plan places the calculation point at 6 cm depth and prescribes 250 cGy per fraction. For four fractions the therapists set the skin, not the isocenter, at 100 cm from the source. Ignoring the small changes in field size and TMR and using inverse square only, what total dose did the point receive over those four fractions?
A. 1000 cGy
B. 943 cGy
C. 890 cGy
D. 1124 cGy
Answer: C
Objective: IV.3
Why: With the skin at 100 cm the point sits at 106 cm from the source instead of 100 cm, so each fraction delivered 250 × (100/106)² = 250 × 0.890 = 222.5 cGy, and four fractions gave 4 × 222.5 = 890 cGy. Check: (100/106)² = 0.890, an 11% underdose, and 1000 × 0.890 = 890 cGy. Reporting 1000 cGy assumes the set-up change had no effect. Using the unsquared ratio 100/106 gives 943 cGy. Inverting the distances, (106/100)², gives 1124 cGy and would mean the point moved closer to the source.

### Q3
Stem: A patient's separation is 24 cm and the prescription point is at midplane. The same midplane dose is to be delivered either isocentrically or with the skin at 100 cm from the source. Considering inverse square only, how many percent more MU does the SSD set-up need than the isocentric set-up?
A. 25.4 percent
B. 12.0 percent
C. 20.3 percent
D. 53.8 percent
Answer: A
Objective: IV.3
Why: Isocentrically the midplane point is 100 cm from the source; with the skin at 100 cm it is 100 + 12 = 112 cm away. The MU scale with the square of the distance ratio: (112/100)² = 1.254, so 25.4 percent more MU. Check: 1.12 × 1.12 = 1.2544. Using the unsquared ratio gives 12.0 percent. Inverting the ratio, 1 − (100/112)², gives a 20.3 percent reduction, which is the dose loss if the MU are not changed, not the MU increase. Using the full separation instead of the midplane depth, (124/100)², gives 53.8 percent.

### Q4
Stem: A course of 50 Gy in 20 fractions is planned through a wedged field whose wedge factor is 0.75. In four of the fractions the wedge was left out of the beam while the MU were unchanged. What total dose did the prescription point receive, to the nearest 0.1 Gy?
A. 47.5 Gy
B. 66.7 Gy
C. 52.5 Gy
D. 53.3 Gy
Answer: D
Objective: IV.3
Why: Each wedged fraction delivers 2.5 Gy; an unwedged fraction with the same MU delivers 2.5/0.75 = 3.333 Gy. Total = 16 × 2.5 + 4 × 3.333 = 40 + 13.33 = 53.3 Gy, which is 106.7% of the prescription. Check: the excess is 4 × 0.833 = 3.33 Gy above 50 Gy. Multiplying the four fractions by the wedge factor instead of dividing gives 47.5 Gy. Treating every fraction as unwedged gives 50/0.75 = 66.7 Gy. Adding 25% to the four fractions, 4 × 2.5 × 1.25, gives 52.5 Gy; the correct increase is 1/0.75, which is 33%.

## Weighted Isocentric Fields and Back-Solved Normalization

### Q1
Stem: A three-field isocentric plan is prescribed 180 cGy per fraction to the 95 percent isodose line. The anterior beam and the two lateral beams are weighted 1 to 0.5 to 0.5 at the isocenter. How much dose does each lateral beam deliver to the isocenter per fraction, to the nearest 0.1 cGy?
A. 45.0 cGy
B. 47.4 cGy
C. 42.8 cGy
D. 94.7 cGy
Answer: B
Objective: IV.3
Why: The isocenter is the 100% point, so it receives 180/0.95 = 189.5 cGy. The weights sum to 2.0, so each lateral gets 189.5 × 0.5/2 = 47.4 cGy and the anterior gets 94.7 cGy. Check: 94.7 + 47.4 + 47.4 = 189.5 cGy, and 189.5 × 0.95 = 180 cGy at the 95% line. Splitting 180 cGy directly gives 45.0 cGy and ignores the 95% prescription. Multiplying by 0.95 instead of dividing gives 42.8 cGy. The 94.7 cGy figure is the anterior beam's share.

### Q2
Stem: A five-field isocentric plan is prescribed 200 cGy per fraction to the 95 percent line. The beams carry isocenter weights of 0.30, 0.25, 0.20, 0.15, and 0.10. What dose does the beam with weight 0.15 contribute at the isocenter, to the nearest 0.1 cGy?
A. 30.0 cGy
B. 28.5 cGy
C. 31.6 cGy
D. 42.1 cGy
Answer: C
Objective: IV.3
Why: The weights sum to 1.00, and the isocenter dose is 200/0.95 = 210.5 cGy, so the 0.15 beam contributes 210.5 × 0.15 = 31.6 cGy. Check: 31.6/0.15 = 210.5 cGy, and 210.5 × 0.95 = 200 cGy at the prescription line. Multiplying 200 by 0.15 gives 30.0 cGy and skips the renormalization. Multiplying by 0.95 instead of dividing gives 28.5 cGy. Using the 0.20 weight by mistake gives 42.1 cGy.

### Q3
Stem: An electron field delivered 296 MU for a prescription of 250 cGy to the normalization isodose line. The cone factor is 1.02, the cutout factor is 0.975, the output is 1 cGy per MU at the nominal 100 cm distance, and the treatment distance was 103 cm. To which isodose line was the dose normalized, to the nearest percent?
A. 90 percent
B. 80 percent
C. 85 percent
D. 111 percent
Answer: A
Objective: IV.3
Why: Dose at dmax on the axis is MU times all factors: 296 × 1.02 × 0.975 × (100/103)² = 296 × 1.02 × 0.975 × 0.9426 = 277.5 cGy. The normalization line is 250/277.5 = 0.901, the 90 percent line. Check: 90% of 277.5 cGy is 249.7 cGy, which rounds to the 250 cGy prescribed. Applying inverse square the wrong way, (103/100)², raises the dmax dose to 312 cGy and gives the 80 percent line. Dropping inverse square gives 294 cGy and the 85 percent line. Dividing the other way, 277.5/250, gives 111 percent, which cannot be a normalization line below the maximum.

## Electron Range Rules Inside a Calculation

### Q1
Stem: A commissioning scan of an electron beam puts the depth of the 50 percent dose at 5.6 cm in water. Using the standard rule that relates mean surface energy to the half-value depth, what is the mean energy at the surface, to the nearest 0.1 MeV?
A. 11.2 MeV
B. 2.4 MeV
C. 16.8 MeV
D. 13.0 MeV
Answer: D
Objective: IV.3
Why: The mean surface energy is about 2.33 times the depth of the 50 percent dose: 2.33 × 5.6 = 13.0 MeV. Check: 13.0/2.33 = 5.58 cm. Doubling the half-value depth, 2 × 5.6, gives 11.2 MeV, which mixes up the practical-range rule with the R50 rule. Dividing by 2.33 instead of multiplying gives 2.4 MeV. Tripling the depth gives 16.8 MeV, which has no rule behind it.

### Q2
Stem: A 12 MeV electron beam is used, and a critical structure lies at 5.5 cm depth on the central axis. Using the half-value depth of about the energy divided by 2.33 and a practical range of about the energy divided by 2, which statement best describes the dose to that structure?
A. It is beyond the practical range and receives only the bremsstrahlung tail
B. It lies between the 50 percent depth and the practical range, so it receives well under half the maximum but still real electron dose
C. It is shallower than the 90 percent depth and receives nearly the full dose
D. It sits exactly at the 50 percent depth
Answer: B
Objective: IV.3
Why: The 50 percent depth is 12/2.33 = 5.2 cm and the practical range is 12/2 = 6.0 cm, so a point at 5.5 cm is in the steep falloff: deeper than the 50 percent depth, shallower than the end of the electron range. Check: Bentel's 90 percent depth is 12/4 = 3 cm, far shallower than 5.5 cm. The structure is not beyond the practical range, so it still receives electron dose, not only bremsstrahlung. It is not shallower than the 90 percent depth. It is 0.3 cm deeper than the 50 percent depth, not exactly on it.
