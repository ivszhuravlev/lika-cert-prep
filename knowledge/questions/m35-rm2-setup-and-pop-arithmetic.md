# Module 35. PDD, TMR, and MU calculations

Original items. Circle-to-square conversion, the depth-error rule of thumb, electron cut-out factors inside an MU calculation, SSD versus SAD monitor units for the same midplane point, and the dmax and midplane arithmetic of a parallel-opposed pair.

## Set-Up Conversions and Parallel-Opposed Pair Arithmetic

### Q1
Stem: A circular electron cut-out has a diameter of 12.0 cm at the treatment plane. Using the standard circle-to-square rule, what is the side of the equivalent square, to the nearest 0.1 cm?
A. 9.4 cm
B. 10.6 cm
C. 12.0 cm
D. 13.5 cm
Answer: B
Objective: IV.3
Why: The square with the same area as a circle has a side of 0.886 times the diameter: 0.886 × 12.0 = 10.63 cm, reported as 10.6 cm. Check: the circle area is 3.1416 × 6.0² = 113.1 cm² and 10.63² = 113.0 cm². Dividing the circumference by four, 2 × 3.1416 × 6.0 / 4 = 9.42 cm, gives a square with the same perimeter, which is not the equal-area rule. Using the diameter itself, 12.0 cm, ignores the conversion. Dividing by 0.886 instead of multiplying gives 13.5 cm and runs the rule backward.

### Q2
Stem: Where does the factor 0.886 in the circle-to-equivalent-square conversion come from?
A. It is the ratio of a circle's circumference to the perimeter of a square with the same width
B. It is an empirical fit to measured output factors for electron cones
C. It is the ratio of the equivalent-square formula 4A/P applied to a circle and a square of the same diameter
D. It is the square root of pi over four, so the square has the same area as the circle
Answer: D
Objective: IV.3
Why: Setting the square's area equal to the circle's area, s² = (pi/4)d², gives s = d × sqrt(pi/4) = 0.886 d. Check: 0.886² = 0.785 = pi/4. The circumference-to-perimeter ratio is pi d divided by 4d = 0.785, not 0.886, and perimeter is not the quantity the rule matches. It is a geometric identity rather than an empirical fit, although equal area is itself only an approximation for scatter. The 4A/P formula applied to a circle gives 4 × (pi/4)d² / (pi d) = d, which would say a circle equals a square of its own diameter; that is the wrong result.

### Q3
Stem: An output-factor table for a linac lists circular fields only. A planner needs the diameter of the circle that matches an 8.0 by 8.0 cm square field. Which diameter should be looked up?
A. 9.0 cm
B. 7.1 cm
C. 8.0 cm
D. 4.5 cm
Answer: A
Objective: IV.3
Why: Reversing the equal-area rule, diameter = side / 0.886 = 8.0 / 0.886 = 9.03 cm, reported as 9.0 cm. Check: 0.886 × 9.03 = 8.00 cm, and the circle area 3.1416 × 4.51² = 64.0 cm² matches 8.0² = 64 cm². Multiplying 8.0 by 0.886 gives 7.1 cm, which is the equivalent square of an 8 cm circle, the reverse question. Taking 8.0 cm treats the circle's diameter as equal to the square's side, which is an area shortfall of 21 percent. Halving to 4.5 cm is the radius of the correct circle, not its diameter.

### Q4
Stem: A 6 MV photon field is calculated at 10 cm depth, but the measured separation shows the point actually lies 1 cm deeper. Without a table, roughly how much does the dose at the point change?
A. About 10 percent lower
B. About 0.5 percent lower
C. About 2 to 3 percent lower
D. About 3 percent higher
Answer: C
Objective: IV.3
Why: Beyond dmax a 6 MV beam loses roughly 2 to 3 percent of its dose per centimeter of water (the TMR or PDD gradient), so a 1 cm depth error changes the dose by about 2 to 3 percent, downward if the point is deeper. Check: typical 6 MV 10 by 10 cm TMR values run about 0.78 at 10 cm and 0.76 at 11 cm, a 2.6 percent drop. Ten percent per centimeter is an electron-beam falloff figure, not a megavoltage photon figure. Half a percent per centimeter is far too small for any clinical photon energy. A deeper point receives less dose, not more.

### Q5
Stem: A field's monitor units were computed for 200 cGy at 10 cm depth using a 6 MV tissue-maximum ratio of 0.780. The point is actually at 11 cm, where the tissue-maximum ratio is 0.757. What dose does the point receive, to the nearest 0.1 cGy?
A. 206.1 cGy
B. 195.4 cGy
C. 194.1 cGy
D. 180.0 cGy
Answer: C
Objective: IV.3
Why: The monitor units are fixed, so the delivered dose scales with the ratio of the true to the assumed TMR: 200 × 0.757 / 0.780 = 200 × 0.9705 = 194.1 cGy. Check: 194.1 / 200 = 0.9705, a 2.9 percent loss, consistent with the 2 to 3 percent per centimeter rule. Inverting the ratio, 200 × 0.780 / 0.757, gives 206.1 cGy, a dose increase at a deeper point, which is unphysical. Subtracting the raw TMR difference as a percentage, 200 × (1 − 0.023), gives 195.4 cGy and ignores that the change is relative to 0.780, not to 1.000. Assuming 10 percent per centimeter gives 180.0 cGy.

### Q6
Stem: During electron cut-out commissioning, an ion chamber at dmax reads 21.30 nC for the open 10 by 10 cm cone and 20.46 nC with the patient's cut-out inserted, same monitor units and SSD. What is the cut-out factor, to three decimals?
A. 0.961
B. 1.041
C. 0.039
D. 0.921
Answer: A
Objective: IV.3
Why: The cut-out factor is the reading with the insert divided by the reading for the open cone it sits in: 20.46 / 21.30 = 0.9606, reported as 0.961. Check: 21.30 × 0.961 = 20.47 nC. Dividing the other way, 21.30 / 20.46, gives 1.041, a factor above one that would raise rather than lower the output. Reporting 1 − 0.961 = 0.039 gives the fractional loss, not the factor applied in the MU equation. Squaring the ratio, 0.961², gives 0.921 and double-counts the effect.

### Q7
Stem: An electron prescription is 200 cGy to the 90 percent isodose line at 100 cm SSD. The machine delivers 1.000 cGy per MU at dmax for the open reference cone, the cone factor for this cone is 1.000, and the cut-out factor measured for the insert is 0.961. How many monitor units are required, to the nearest 0.1 MU?
A. 222.2 MU
B. 213.6 MU
C. 208.1 MU
D. 231.2 MU
Answer: D
Objective: IV.3
Why: MU = prescribed dose / (output × cone factor × cut-out factor × isodose fraction) = 200 / (1.000 × 1.000 × 0.961 × 0.90) = 200 / 0.8649 = 231.2 MU. Check: 231.2 × 0.961 × 0.90 = 200.0 cGy at the 90 percent line. Dropping the cut-out factor, 200 / 0.90, gives 222.2 MU and underdoses by 4 percent. Multiplying by the cut-out factor instead of dividing, 200 × 0.961 / 0.90, gives 213.6 MU. Dividing only by the cut-out factor, 200 / 0.961, gives 208.1 MU and forgets the prescription is to the 90 percent line rather than dmax.

### Q8
Stem: A patient with a 20 cm separation is prescribed to the midplane. The treatment could be set up isocentrically at 100 cm SAD, or with the skin at 100 cm SSD so the midplane sits deeper from the source. Considering inverse square only, what is the ratio of the SSD-setup monitor units to the SAD-setup monitor units for the same midplane dose?
A. 1.10
B. 1.21
C. 0.83
D. 1.44
Answer: B
Objective: IV.3
Why: Midplane depth is 20 / 2 = 10 cm. In the SSD set-up the point sits at 100 + 10 = 110 cm from the source instead of 100 cm, so the MU ratio is ((SAD + d)/SAD)² = (110/100)² = 1.21. Check: the dose per MU at 110 cm is (100/110)² = 0.826 of that at 100 cm, and 1/0.826 = 1.21. The depth, and therefore the TMR, is the same in both set-ups, so only inverse square changes. Taking 110/100 without squaring gives 1.10. Inverting gives 0.83, which is the dose ratio, not the MU ratio. Using the full separation as the extra distance, (120/100)², gives 1.44.

### Q9
Stem: An isocentric parallel-opposed plan at 100 cm SAD calls for 150 MU per field to deliver the midplane dose through a 20 cm separation. If the same fields are instead set up with the skin at 100 cm SSD, how many monitor units per field are needed for the same midplane dose, considering inverse square only?
A. 182 MU
B. 165 MU
C. 124 MU
D. 216 MU
Answer: A
Objective: IV.3
Why: The midplane point moves from 100 cm to 110 cm from the source, so MU scale by (110/100)² = 1.21: 150 × 1.21 = 181.5 MU, reported as 182 MU. Check: 182 × (100/110)² = 182 × 0.826 = 150.4, equivalent to the original 150 MU at 100 cm. Scaling by 1.10 (not squared) gives 165 MU. Dividing by 1.21 gives 124 MU, which is the dose the point would receive if the MU were left unchanged, not the MU needed. Using (120/100)² gives 216 MU.

### Q10
Stem: Monitor units were calculated for an isocentric set-up delivering 200 cGy to a point at 10 cm depth with the isocenter at 100 cm. The therapists instead set the skin at 100 cm from the source and delivered the planned monitor units. Ignoring small changes in field size and TMR, what dose did the point receive, to the nearest 0.1 cGy?
A. 242.0 cGy
B. 181.8 cGy
C. 200.0 cGy
D. 165.3 cGy
Answer: D
Objective: IV.3
Why: With the skin at 100 cm the point lies at 110 cm from the source, so the dose falls by (100/110)² = 0.8264: 200 × 0.8264 = 165.3 cGy, a 17.4 percent underdose. Check: 165.3 × 1.21 = 200.0 cGy. Multiplying by 1.21 gives 242.0 cGy and reverses the direction of the error; moving the point farther away cannot raise the dose. Using 100/110 without squaring gives 181.8 cGy. The dose is not unchanged because the calculation geometry and the delivered geometry differ by 10 cm of distance.

### Q11
Stem: A parallel-opposed pair treats a 10 cm separation with a 15 MV beam. Each beam delivers 100 cGy at its own dmax. The PDD at the 5 cm midplane is 93 percent for each beam. What dose does the midplane receive, as a percentage of the dose a single beam gives at its dmax?
A. 193 percent
B. 186 percent
C. 200 percent
D. 107 percent
Answer: B
Objective: IV.3
Why: Each beam contributes its PDD at midplane, 93 percent of its own dmax dose, so the two beams give 93 + 93 = 186 percent of the per-beam dmax dose, which is 186 cGy here. Equivalently, the midplane receives 93 percent of the two-beam total of 200 cGy: 0.93 × 200 = 186 cGy. Adding 100 and 93 to get 193 percent is the dose at a dmax point, where one beam is at full dmax dose and the other is exiting; that is not the midplane. Two hundred percent would require no attenuation at all. Taking 100 plus the 7 percent deficit has no meaning.

### Q12
Stem: A 6 MV parallel-opposed pair treats a 16 cm separation, dmax 1.5 cm. Each beam delivers 100 cGy at its own dmax. For each beam the PDD is 78 percent at 8 cm and 60 percent at 14.5 cm. What dose does the dmax point of the anterior beam receive?
A. 156 cGy
B. 160 cGy
C. 100 cGy
D. 140 cGy
Answer: B
Objective: IV.3
Why: The anterior beam gives 100 cGy at its dmax. The posterior beam reaches that same point after traveling 16 − 1.5 = 14.5 cm, where its PDD is 60 percent, so it adds 60 cGy. Total = 100 + 60 = 160 cGy. Check: midplane receives 2 × 78 = 156 cGy, so the dmax points are 160/156 = 1.026, about 2.6 percent hotter than midplane, the expected small hot spot for a 16 cm separation at 6 MV. Reporting 156 cGy gives the midplane dose instead. Reporting 100 cGy ignores the exiting beam. Subtracting the exit contribution, 100 + (100 − 60), gives 140 cGy and treats the exit PDD as a deficit instead of a dose.

### Q13
Stem: For a parallel-opposed pair normalized at midplane, which change makes the dose at the two dmax points larger relative to the midplane dose?
A. A thinner patient treated with a higher-energy beam
B. A thinner patient treated with a lower-energy beam
C. A thicker patient treated with a lower-energy beam
D. A thicker patient treated with a higher-energy beam
Answer: C
Objective: IV.3
Why: The dmax-to-midplane ratio is (100 + exit PDD) / (2 × midplane PDD). A thicker patient lowers both PDDs but the midplane term carries the factor of two, so the ratio grows; a lower energy steepens the falloff and also lowers both PDDs, again raising the ratio. Check with the 6 MV 16 cm example: (100 + 60)/(2 × 78) = 1.026, while a 24 cm separation at 6 MV with midplane PDD about 60 and exit about 40 gives 140/120 = 1.17. Higher energy flattens the depth dose and shrinks the hot spot, so options A and D move the wrong way. A thinner patient at low energy has a smaller ratio than a thicker one, so option B is less extreme than C.

### Q14
Stem: A planner looks up output and scatter factors for a 5 by 25 cm photon field using an equivalent square of 8.3 cm. Why is this result suspect?
A. The field's long-to-short side ratio of 5 exceeds about 2, beyond which the equivalent-square approximation loses accuracy and measured elongated-field data should be used
B. The equivalent square should have been computed as the geometric mean, sqrt(5 × 25) = 11.2 cm
C. The equivalent square of a rectangle is always the shorter side, so 5 cm should have been used
D. Equivalent squares apply only to electron fields, not to photon fields
Answer: A
Objective: IV.3
Why: The 4A/P rule gives 2 × 5 × 25 / (5 + 25) = 250/30 = 8.3 cm, so the arithmetic is right, but equivalent-square tables are validated for rectangles with elongation ratios up to about 2. At a ratio of 25/5 = 5 the scatter from the long axis is not represented by an 8.3 cm square, and most departments commission measured output factors or a Clarkson-type calculation for such fields. The geometric mean is not the standard rule and overstates scatter for narrow fields. The shorter side alone understates scatter and is not the rule either. Equivalent squares are a photon scatter tool first and are also used for electron cut-outs.
