# Module 35 — PDD, TMR, and MU Calcs

Original items. An SSD calculation uses PDD. An SAD calculation uses TMR. Every MU stem states the calibration: 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm, unless a different point is named. Mayneord F corrects inverse square inside a PDD only.

## Interpolation Tutorial (No Formula)

### Q1
Stem: A PDD table lists 67.5% at 10.0 cm and 64.3% at 11.0 cm. What is the linearly interpolated PDD at 10.4 cm?
A. 67.5%
B. 65.9%
C. 66.22%
D. 64.3%
Answer: C
Objective: IV.3
Why: The fraction is (10.4 − 10.0) / (11.0 − 10.0) = 0.40. The table drops 67.5 − 64.3 = 3.2. Then 0.40 × 3.2 = 1.28, and 67.5 − 1.28 = 66.22%. The average 65.9% would be the midpoint at 10.5 cm, not 10.4 cm.

### Q2
Stem: PDD is 85.0% at 5.0 cm and 82.4% at 6.0 cm. What is PDD at 5.2 cm?
A. 84.48%
B. 83.7%
C. 85.0%
D. 82.4%
Answer: A
Objective: IV.3
Why: Fraction = (5.2 − 5.0) / (6.0 − 5.0) = 0.20. Drop = 85.0 − 82.4 = 2.6. Then 0.20 × 2.6 = 0.52, and 85.0 − 0.52 = 84.48%. Averaging the two rows gives 83.7%, which belongs at 5.5 cm.

### Q3
Stem: PDD is 72.0% at 8.0 cm and 67.0% at 10.0 cm. What is PDD at 8.5 cm?
A. 69.5%
B. 70.75%
C. 71.0%
D. 67.0%
Answer: B
Objective: IV.3
Why: Fraction = (8.5 − 8.0) / (10.0 − 8.0) = 0.25. Drop = 5.0. Then 0.25 × 5.0 = 1.25, and 72.0 − 1.25 = 70.75%. The midpoint 69.5% is the value at 9.0 cm. Scaling 72 by 8.5/10 is not interpolation.

### Q4
Stem: PDD is 58.0% at 12.0 cm and 55.4% at 13.0 cm. What is PDD at 12.3 cm?
A. 57.22%
B. 56.7%
C. 58.0%
D. 55.4%
Answer: A
Objective: IV.3
Why: Fraction = 0.3 / 1.0 = 0.30. Drop = 58.0 − 55.4 = 2.6. Then 0.30 × 2.6 = 0.78, and 58.0 − 0.78 = 57.22%. The average 56.7% is the 12.5 cm value.

### Q5
Stem: PDD is 76.2% at 7.0 cm and 73.8% at 8.0 cm. What is PDD at 7.5 cm?
A. 76.2%
B. 74.6%
C. 75.0%
D. 73.8%
Answer: C
Objective: IV.3
Why: 7.5 cm is midway, so the fraction is 0.50. Drop = 76.2 − 73.8 = 2.4. Then 0.50 × 2.4 = 1.2, and 76.2 − 1.2 = 75.0%. The same result is (76.2 + 73.8) / 2 = 75.0. That average is valid only because the depth is the midpoint.

### Q6
Stem: A TMR table lists 0.800 at 10 cm and 0.760 at 12 cm, same field size at the point. What is TMR at 11 cm?
A. 0.800
B. 0.780
C. 0.760
D. 0.820
Answer: B
Objective: IV.3
Why: 11 cm is midway from 10 to 12, fraction 0.50. Drop = 0.040. Then 0.50 × 0.040 = 0.020, and 0.800 − 0.020 = 0.780. Adding the drop instead of subtracting it gives 0.820.

### Q7
Stem: Collimator scatter is 1.020 for a 10 cm equivalent square and 1.050 for 15 cm. What is Sc at 12 cm by linear interpolation?
A. 1.020
B. 1.035
C. 1.032
D. 1.050
Answer: C
Objective: IV.3
Why: Fraction = (12 − 10) / (15 − 10) = 0.40. Rise = 0.030. Then 0.40 × 0.030 = 0.012, and 1.020 + 0.012 = 1.032. The midpoint 1.035 belongs at 12.5 cm.

### Q8
Stem: PDD is 80.0% at 6 cm and 75.2% at 8 cm. Someone asks for 14 cm from those two rows only. What is the right action?
A. Extrapolate and report 65.6%
B. Do not treat a long extrapolation as the same linear step; get a table row that brackets 14 cm
C. Average 80.0 and 75.2 and call it 14 cm
D. Multiply 75.2 by 14/8
Answer: B
Objective: IV.3
Why: The fraction (14 − 6) / (8 − 6) = 4, which is outside 0 to 1. PDD is not linear over that stretch. The in-range step from 6 to 8 cm drops 4.8 over 2 cm, but quoting 80 − 4 × 4.8 = 60.8, or any other far extrapolation, is not the interpolation this lesson uses. The average 77.6% is the 7 cm estimate, not 14 cm.

## PDD and TMR Calculation Tutorial

### Q1
Stem: Percent depth dose is defined as:
A. 100 × dose at depth / dose at dmax, at a fixed SSD
B. Dose at depth / dose at dmax, at a fixed source-to-point distance
C. Dose in tissue / dose in air
D. An inverse-square factor with no attenuation
Answer: A
Objective: IV.3
Why: PDD = 100 × D(d) / D(dmax) at fixed SSD, so the number is a percent and it already contains inverse square from dmax to depth. Choice B is TMR, a fraction at fixed source-to-point distance. Choice C is the idea of TAR. Inverse square alone is not a PDD.

### Q2
Stem: TMR at depth d for field size rd is:
A. A percent that includes inverse square from the skin to the isocenter
B. D(d) / D(dmax) at a fixed source-to-point distance
C. Mayneord F
D. The wedge factor
Answer: B
Objective: IV.3
Why: TMR = D(d) / D(dmax) with the point held at a fixed distance from the source. Inverse square is not inside the TMR. The field size is the field at the point. Mayneord F and the wedge factor are different multipliers.

### Q3
Stem: A PDD at 10 cm depth, SSD 100 cm, is 67.0%. dmax is 1.5 cm. Estimate the PDD at the same depth for SSD 110 cm with Mayneord F.
A. 66.1%
B. 67.0%
C. 67.9%
D. 73.7%
Answer: C
Objective: IV.3
Why: F = ((110 + 1.5) / (100 + 1.5))^2 × ((100 + 10) / (110 + 10))^2 = (111.5 / 101.5)^2 × (110 / 120)^2. 111.5 / 101.5 = 1.0985 and 1.0985^2 = 1.2067. 110 / 120 = 0.9167 and 0.9167^2 = 0.8403. F = 1.2067 × 0.8403 = 1.014. Then 67.0 × 1.014 = 67.9%. Inverting F gives about 66.1%. Dropping the squares gives about 67.5%, not 73.7%.

### Q4
Stem: The same 67.0% PDD (SSD 100 cm, depth 10 cm, dmax 1.5 cm) is moved to SSD 80 cm with Mayneord F. What PDD do you estimate?
A. 69.6%
B. 67.0%
C. 64.5%
D. 53.6%
Answer: C
Objective: IV.3
Why: F = ((80 + 1.5) / (100 + 1.5))^2 × ((100 + 10) / (80 + 10))^2 = (81.5 / 101.5)^2 × (110 / 90)^2. 81.5 / 101.5 = 0.8030 and 0.8030^2 = 0.6448. 110 / 90 = 1.2222 and 1.2222^2 = 1.4938. F = 0.6448 × 1.4938 = 0.963. Then 67.0 × 0.963 = 64.5%. A shorter SSD makes the inverse-square piece inside the PDD steeper, so the percent falls. 69.6% is 67 / 0.963, the inverted factor.

### Q5
Stem: Table PDD is 70.0% at 10 cm depth for SSD 80 cm. dmax is 0.5 cm. Mayneord F to SSD 100 cm is 1.043. What PDD do you estimate at SSD 100 cm?
A. 67.1%
B. 70.0%
C. 73.0%
D. 80.5%
Answer: C
Objective: IV.3
Why: 70.0 × 1.043 = 73.0%. Check: 73.0 / 1.043 = 70.0. Dividing the table PDD by F gives 70.0 / 1.043 = 67.1%, which applies the factor backwards. F = ((100.5)/(80.5))^2 × ((90)/(110))^2 corrects inverse square only and does not add scatter for the new SSD.

### Q6
Stem: PDD at 15 cm, SSD 100 cm, is 55.0%. dmax is 1.5 cm. Mayneord F from SSD 100 cm to SSD 120 cm is 1.040. What is the estimated PDD at SSD 120 cm?
A. 52.9%
B. 55.0%
C. 57.2%
D. 71.5%
Answer: C
Objective: IV.3
Why: PDD(120) = 55.0 × 1.040 = 57.2%. Dividing gives 55.0 / 1.040 = 52.9%, which is the wrong direction for a longer SSD. 55.0 × 1.30 = 71.5% invents a factor the stem did not give. F here is inverse square only; scatter is still the SSD 100 cm scatter.

### Q7
Stem: An SSD tumor dose is 240 cGy where PDD is 60%. What given dose at dmax is required?
A. 144 cGy
B. 300 cGy
C. 400 cGy
D. 240 cGy
Answer: C
Objective: IV.3
Why: Given dose = 240 / 0.60 = 400 cGy. Check: 400 × 0.60 = 240 cGy. Multiplying gives 144 cGy, the tumor dose if 240 cGy were already the given dose. Mayneord F is not part of this division, and a TMR is not added beside the PDD.

### Q8
Stem: On an SAD setup the dose at dmax is 400 cGy and the TMR is 0.600. What is the dose at depth?
A. 240 cGy
B. 400 cGy
C. 667 cGy
D. 160 cGy
Answer: A
Objective: IV.3
Why: 400 × 0.600 = 240 cGy. Check: 240 / 400 = 0.600. Dividing 400 / 0.600 = 667 cGy is the given-dose step and does not belong on a TMR. Mayneord F is not applied to this TMR. The 240 cGy can match an SSD tumor dose numerically; the fixed source-to-point distance does not match that SSD geometry.

## PDD and TMR Calculations

### Q1
Stem: An SSD setup prescribes 200 cGy to the tumor where PDD = 80.0%. What is the given dose at dmax?
A. 160 cGy
B. 200 cGy
C. 250 cGy
D. 280 cGy
Answer: C
Objective: IV.3
Why: Given dose = tumor dose / (PDD/100) = 200 / 0.80 = 250 cGy. Check: 250 × 0.80 = 200 cGy at the tumor. Multiplying gives 160 cGy, which is the tumor dose you would get from a given dose of 200 cGy, the reverse question.

### Q2
Stem: Given dose at dmax on an SSD setup is 250 cGy. PDD at the tumor is 72%. What tumor dose is delivered?
A. 180 cGy
B. 250 cGy
C. 347 cGy
D. 322 cGy
Answer: A
Objective: IV.3
Why: Tumor dose = 250 × 0.72 = 180 cGy. Check: 180 / 0.72 = 250 cGy given. Dividing 250 by 0.72 gives about 347 cGy, which treats 250 as the tumor dose. 250 × 1.29 is not this percent.

### Q3
Stem: On an SAD setup, dose at dmax at the isocenter distance is 250 cGy. TMR at the tumor is 0.800. What is the dose at the tumor?
A. 200 cGy
B. 250 cGy
C. 312.5 cGy
D. 180 cGy
Answer: A
Objective: IV.3
Why: D(d) = 250 × 0.800 = 200 cGy. Check: 200 / 250 = 0.800. Dividing 250 by 0.800 gives 312.5 cGy, which is the given-dose operation from a PDD problem, not this TMR multiplication. The number 200 cGy can match an SSD example and still be a different setup: TMR holds source-to-point distance fixed.

### Q4
Stem: SAD setup. Dose at depth must be 180 cGy. TMR = 0.750. What dose is required at dmax, at the same source-to-point distance?
A. 135 cGy
B. 180 cGy
C. 240 cGy
D. 255 cGy
Answer: C
Objective: IV.3
Why: D(dmax) = 180 / 0.750 = 240 cGy. Check: 240 × 0.750 = 180 cGy. Multiplying gives 135 cGy, the depth dose if 180 cGy were already the dmax dose.

### Q5
Stem: Tumor dose 160 cGy, SSD setup, PDD = 64%. What is the given dose at dmax?
A. 102 cGy
B. 160 cGy
C. 224 cGy
D. 250 cGy
Answer: D
Objective: IV.3
Why: 160 / 0.64 = 250 cGy. Check: 250 × 0.64 = 160. Leaving PDD as 64 instead of 0.64 gives 160/64 = 2.5 cGy, a unit error. 160 × 0.64 = 102.4 cGy is the reverse multiplication.

### Q6
Stem: SAD setup. Dose at dmax is 300 cGy. TMR = 0.650. What is the dose at depth?
A. 195 cGy
B. 300 cGy
C. 462 cGy
D. 235 cGy
Answer: A
Objective: IV.3
Why: 300 × 0.650 = 195 cGy. Check: 195 / 300 = 0.650. 300 / 0.650 = 461.5 cGy is the division used when 300 cGy is the tumor dose and you want dmax.

### Q7
Stem: A stem gives PDD = 80% for an SSD patient and a TMR of 0.800 for a different SAD patient. Which use is allowed?
A. Put both 0.800 factors in one MU formula
B. Use the PDD only on the SSD setup and the TMR only on the SAD setup
C. Apply Mayneord F to the TMR because the percents match
D. Call the TMR a given dose
Answer: B
Objective: IV.3
Why: The percents can be numerically equal and still belong to different geometries. PDD includes inverse square along a fixed SSD. TMR does not. One formula does not contain both. Mayneord F is not applied to TMR.

### Q8
Stem: SSD setup. Tumor dose 210 cGy. PDD = 70%. What given dose at dmax produces that tumor dose?
A. 147 cGy
B. 210 cGy
C. 280 cGy
D. 300 cGy
Answer: D
Objective: IV.3
Why: 210 / 0.70 = 300 cGy. Check: 300 × 0.70 = 210 cGy. 210 × 0.70 = 147 cGy is the tumor dose from a given dose of 210 cGy. 280 cGy uses 0.75.

## PDD and TMR Quiz

### Q1
Stem: PDD is 90.0% at 3.0 cm and 84.0% at 5.0 cm. What is the interpolated PDD at 4.0 cm?
A. 87.0%
B. 90.0%
C. 86.4%
D. 84.0%
Answer: A
Objective: IV.3
Why: 4.0 cm is midway, fraction 0.50. Drop = 6.0. Then 0.50 × 6.0 = 3.0, and 90.0 − 3.0 = 87.0%. Check: (90.0 + 84.0) / 2 = 87.0.

### Q2
Stem: PDD is 70.0% at 9.0 cm and 67.6% at 10.0 cm. What is PDD at 9.25 cm?
A. 69.4%
B. 68.8%
C. 70.0%
D. 67.6%
Answer: A
Objective: IV.3
Why: Fraction = 0.25 / 1.0 = 0.25. Drop = 2.4. Then 0.25 × 2.4 = 0.60, and 70.0 − 0.60 = 69.4%. The average 68.8% is the 9.5 cm value.

### Q3
Stem: Mayneord F from the table SSD to the treatment SSD is 1.030. Table PDD is 66.0%. What PDD do you use?
A. 64.1%
B. 66.0%
C. 68.0%
D. 67.0%
Answer: C
Objective: IV.3
Why: 66.0 × 1.030 = 67.98%, which is 68.0% to three significant figures. 66.0 / 1.030 = 64.1% inverts F. The factor corrects inverse square only, not scatter.

### Q4
Stem: Tumor dose 180 cGy, SSD, PDD = 75%. What is the given dose?
A. 135 cGy
B. 240 cGy
C. 180 cGy
D. 255 cGy
Answer: B
Objective: IV.3
Why: 180 / 0.75 = 240 cGy. Check: 240 × 0.75 = 180. Multiplying gives 135 cGy.

### Q5
Stem: SAD. Dose at dmax is 240 cGy. TMR = 0.625. What is the dose at depth?
A. 150 cGy
B. 240 cGy
C. 384 cGy
D. 180 cGy
Answer: A
Objective: IV.3
Why: 240 × 0.625 = 150 cGy. Check: 0.625 = 5/8, and 240 × 5/8 = 150. 240 / 0.625 = 384 cGy divides instead of multiplying.

### Q6
Stem: Which formula is the SSD given-dose step?
A. Tumor dose × (PDD/100)
B. Tumor dose / (PDD/100)
C. Tumor dose × TMR × PDD
D. Tumor dose × Mayneord F × TMR
Answer: B
Objective: IV.3
Why: D(dmax) = Dtumor / (PDD/100). Multiplying by PDD/100 answers the tumor dose when dmax dose is known. TMR does not enter an SSD given-dose line.

### Q7
Stem: Field size for a TMR lookup is:
A. The field on the skin, always
B. The field at the calculation point
C. The collimator setting plus 5 cm
D. The blocked percent of the jaw area
Answer: B
Objective: IV.3
Why: TMR(d, rd) uses rd at the point because the source-to-point distance is fixed. A PDD table often uses the field on the skin. Percent blocked is not a field side for the TMR row.

### Q8
Stem: SSD 100 cm PDD at 10 cm is 67%. A longer SSD, Mayneord only, does what to that PDD?
A. It lowers the PDD, because scatter increases
B. It raises the PDD slightly, because inverse-square falloff between dmax and depth is gentler
C. It converts the PDD into a TMR of 0.67
D. It leaves the PDD unchanged for any SSD
Answer: B
Objective: IV.3
Why: Both dmax and the depth point move farther from the source, so the inverse-square ratio between them moves closer to 1 and the PDD rises. The worked 100 cm to 110 cm case took 67.0% to about 67.9%. Scatter is not corrected by F, and the result is still a PDD, not a TMR.

## Equivalent Square

### Q1
Stem: An open field is 10 cm × 15 cm. What is the equivalent square side by 2ab/(a+b)?
A. 12.0 cm
B. 12.5 cm
C. 12.25 cm
D. 25 cm
Answer: A
Objective: IV.3
Why: 2 × 10 × 15 / (10 + 15) = 300 / 25 = 12.0 cm. The perimeter form agrees: area 150, perimeter 2(10+15) = 50, and 4 × 150 / 50 = 12.0 cm. The arithmetic mean is 12.5 cm. The square root of the area is about 12.25 cm. Neither replaces Sterling’s side.

### Q2
Stem: A rectangle is 5 cm × 20 cm. What equivalent square side should be used for a scatter lookup?
A. 12.5 cm
B. 10.0 cm
C. 8.0 cm
D. 25 cm
Answer: C
Objective: IV.3
Why: 2 × 5 × 20 / (5 + 20) = 200 / 25 = 8.0 cm. The mean (5+20)/2 = 12.5 cm. The square root of the area is 10.0 cm. The field is far from square, so the approximation is poorer, and the exam still wants 8.0 cm from the formula.

### Q3
Stem: Why is “25% of a 10 × 10 blocked, so the side is 7.5 cm” rejected?
A. Because 10 × 0.75 is the Clarkson SAR
B. Because block shape and position change scatter; an irregular field is a Clarkson problem, not a percent of the side
C. Because equivalent square is 4A/P only for circles
D. Because blocked fields use Mayneord F as the side length
Answer: B
Objective: IV.3
Why: Sterling’s formula is for an open rectangle. Percent blocked does not locate the block. Clarkson separates primary and scatter by sector. 10 × 0.75 = 7.5 is a scaled side, and √75 ≈ 8.7 is a scaled area; neither is the sector sum.

### Q4
Stem: Jaws are 15 cm × 15 cm and a block trims the treated opening to 8 cm × 12 cm. Which field size is used for phantom scatter?
A. 15 cm, because the jaws set every scatter factor
B. The equivalent square of the treated opening, 9.6 cm
C. 12 cm, the longer blocked side
D. 8 cm, the shorter blocked side
Answer: B
Objective: IV.3
Why: Jaws set collimator scatter Sc. The opening at the patient sets phantom scatter Sp. For the opening, 2 × 8 × 12 / (8 + 12) = 192 / 20 = 9.6 cm. Using 15 cm for Sp, or either raw side alone, reads the wrong row.

### Q5
Stem: The two forms 2ab/(a+b) and 4A/P disagree. The perimeter was taken as a+b instead of 2(a+b). For a 6 cm × 10 cm field, what wrong side appears, and what is the correct side?
A. Wrong side 15 cm; correct side 7.5 cm
B. Wrong side 7.5 cm; correct side 15 cm
C. Both forms give 8 cm
D. Wrong side 3.75 cm; correct side 7.5 cm
Answer: A
Objective: IV.3
Why: Correct: 2 × 6 × 10 / (6+10) = 120 / 16 = 7.5 cm. Area = 60. If perimeter is wrongly a+b = 16, then 4A/P = 240/16 = 15 cm, twice the correct side. Using 2(a+b) = 32 gives 240/32 = 7.5 cm, and the forms agree.

## Equivalent Square Calculation Mini-Quiz

### Q1
Stem: Find the equivalent square of a 6 cm × 10 cm open field.
A. 8.0 cm
B. 7.5 cm
C. 16 cm
D. 7.7 cm
Answer: B
Objective: IV.3
Why: 2 × 6 × 10 / (6 + 10) = 120 / 16 = 7.5 cm. Check: A = 60, P = 32, 4A/P = 240/32 = 7.5 cm. The mean is 8.0 cm. √60 ≈ 7.7 cm.

### Q2
Stem: Find the equivalent square of a 4 cm × 12 cm field.
A. 8.0 cm
B. 6.9 cm
C. 6.0 cm
D. 16 cm
Answer: C
Objective: IV.3
Why: 2 × 4 × 12 / (4 + 12) = 96 / 16 = 6.0 cm. Check: A = 48, P = 32, 4A/P = 192/32 = 6.0 cm. The mean is 8.0 cm. √48 ≈ 6.9 cm.

### Q3
Stem: Find the equivalent square of a 7 cm × 21 cm field.
A. 14.0 cm
B. 12.1 cm
C. 10.5 cm
D. 28 cm
Answer: C
Objective: IV.3
Why: 2 × 7 × 21 / (7 + 21) = 294 / 28 = 10.5 cm. Check: A = 147, P = 56, 4A/P = 588/56 = 10.5 cm. The mean is 14.0 cm. √147 ≈ 12.1 cm.

### Q4
Stem: Find the equivalent square of a 6 cm × 18 cm field.
A. 12.0 cm
B. 10.4 cm
C. 9.0 cm
D. 24 cm
Answer: C
Objective: IV.3
Why: 2 × 6 × 18 / (6 + 18) = 216 / 24 = 9.0 cm. Check: A = 108, P = 48, 4A/P = 432/48 = 9.0 cm. The mean is 12.0 cm. √108 ≈ 10.4 cm.

### Q5
Stem: Find the equivalent square of a 4 cm × 20 cm field.
A. 12.0 cm
B. 8.9 cm
C. 6.67 cm
D. 24 cm
Answer: C
Objective: IV.3
Why: 2 × 4 × 20 / (4 + 20) = 160 / 24 = 6.67 cm. Check: A = 80, P = 48, 4A/P = 320/48 = 6.67 cm. The mean is 12.0 cm. √80 ≈ 8.9 cm. The long narrow shape stretches the approximation; the formula result is still 6.67 cm.

### Q6
Stem: A 10 × 10 field has a corner block covering 20% of the area. Which side do you look up for scatter?
A. 8.0 cm, because 10 × 0.80 = 8
B. 8.9 cm, because √80 ≈ 8.9
C. Neither; integrate scatter by Clarkson sectors
D. 10 cm, because blocks never change phantom scatter
Answer: C
Objective: IV.3
Why: Percent of area does not give 2ab/(a+b). The block’s position changes the sector radii. Clarkson adds primary TAR(d, 0) to the angle-weighted SAR. An open 10 × 10 is a 10 cm square only while it stays open.

### Q7
Stem: For a PDD table that expects the field on the skin, a 12 cm × 12 cm field at isocenter (SAD 100 cm, SSD 90 cm) has what skin field, and what equivalent square is that skin field if it is still square?
A. Skin field 10.8 cm × 10.8 cm, equivalent square 10.8 cm
B. Skin field 12 cm, because SSD does not change field size
C. Skin field 13.3 cm, equivalent square 13.3 cm
D. Equivalent square 24 cm
Answer: A
Objective: IV.3
Why: Field size scales with distance from the source. Skin is at 90 cm, isocenter at 100 cm, so the skin side is 12 × (90/100) = 10.8 cm. A square’s equivalent square is itself, 10.8 cm. Using 12 cm reads the isocenter field on a skin-field table. 12 × (100/90) = 13.3 cm magnifies the wrong way.

### Q8
Stem: Rectangle 15 cm × 20 cm. Compute 2ab/(a+b).
A. 17.5 cm
B. 17.1 cm
C. 17.3 cm
D. 35 cm
Answer: B
Objective: IV.3
Why: 2 × 15 × 20 / (15 + 20) = 600 / 35 = 17.14 cm, reported as 17.1 cm. Check: A = 300, P = 70, 4A/P = 1200/70 = 17.14 cm. The mean is 17.5 cm. √300 ≈ 17.3 cm.

## Everything you need to know about MUs

### Q1
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SSD setup. SSD + dmax = 100 cm, so the inverse-square factor is 1. Sc = Sp = WF = TF = 1. PDD at the tumor is 70.0%. Tumor dose is 210 cGy. How many MU?
A. 147 MU
B. 210 MU
C. 300 MU
D. 70 MU
Answer: C
Objective: IV.3
Why: MU = 210 / (1.0 × 0.700) = 300. Check: 300 × 0.700 = 210 cGy. The given dose at dmax is 210 / 0.70 = 300 cGy, and at 1.0 cGy/MU that is also 300 MU. There is no TMR in this SSD line.

### Q2
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SAD setup. The point is at isocenter, so (SAD/SPD)^2 = 1. Sc = Sp = WF = TF = 1. TMR = 0.800. Dose = 200 cGy. How many MU?
A. 160 MU
B. 200 MU
C. 250 MU
D. 300 MU
Answer: C
Objective: IV.3
Why: MU = 200 / 0.800 = 250. Check: 250 × 0.800 = 200 cGy. A 70% PDD from a different SSD patient does not belong in this denominator. 200 × 0.800 = 160 MU puts TMR in the numerator.

### Q3
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Isocenter point, scatter and tray factors = 1, inverse square = 1. TMR = 0.750. WF = 0.600 and the wedge is in the beam. Dose = 180 cGy. How many MU?
A. 240 MU
B. 300 MU
C. 400 MU
D. 180 MU
Answer: C
Objective: IV.3
Why: MU = 180 / (0.750 × 0.600) = 180 / 0.450 = 400. Check: 400 × 0.750 × 0.600 = 180 cGy. Omitting WF gives 180 / 0.750 = 240 MU, and with the wedge still in the beam the dose is 240 × 0.450 = 108 cGy, which is 0.60 of 180 cGy.

### Q4
Stem: On an SSD MU, Sc follows which aperture, and Sp follows which aperture?
A. Both follow the blocked opening
B. Sc follows the jaws; Sp and the PDD field follow the treated opening
C. Sc follows the block; Sp follows the jaws
D. Neither factor changes with field size
Answer: B
Objective: IV.3
Why: Collimator scatter is set by the jaw opening that the head sees. Phantom scatter and the depth-dose field are set by the aperture that actually irradiates the patient, including blocks. Swapping them reads the wrong row of each table.

### Q5
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SSD = 100 cm and dmax = 1.5 cm, so dmax is 101.5 cm from the source. Sc = Sp = WF = TF = 1. PDD = 67.0%. Tumor dose = 200 cGy. The inverse-square factor (100/101.5)^2 is 0.971. How many MU?
A. 299 MU
B. 308 MU
C. 200 MU
D. 134 MU
Answer: B
Objective: IV.3
Why: ISF = (SAD / (SSD + dmax))^2 = (100/101.5)^2 = 0.971. MU = 200 / (0.670 × 0.971) = 200 / 0.650 = 308 MU. Check: 308 × 0.650 = 200 cGy. Leaving ISF out gives 200 / 0.670 = 299 MU, about 3% low. Inverting ISF uses (101.5/100)^2 and makes the MU too small.

## MU Calc Quiz

### Q1
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SSD setup with SSD + dmax = 100 cm. Sc = 1.05, Sp = 1.00, PDD = 80%, WF = TF = 1. Dose = 168 cGy. How many MU?
A. 168 MU
B. 200 MU
C. 210 MU
D. 140 MU
Answer: B
Objective: IV.3
Why: MU = 168 / (1.05 × 0.80) = 168 / 0.84 = 200. Check: 200 × 1.05 × 0.80 = 168 cGy. Dropping Sc gives 168 / 0.80 = 210 MU. Multiplying by the factors gives 168 × 0.84 = 141 MU.

### Q2
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SAD setup at isocenter. Sc = 1.00, Sp = 0.980, TMR = 0.700, WF = TF = 1. Dose = 137.2 cGy. How many MU?
A. 196 MU
B. 200 MU
C. 250 MU
D. 137 MU
Answer: B
Objective: IV.3
Why: Denominator = 0.980 × 0.700 = 0.686. MU = 137.2 / 0.686 = 200. Check: 200 × 0.686 = 137.2 cGy. Using a PDD in place of this TMR would be a different geometry. 137.2 / 0.700 = 196 MU drops Sp.

### Q3
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Isocenter, all scatter and tray factors = 1, TMR = 0.850, WF = 0.650, wedge in the beam. Dose = 180 cGy. How many MU?
A. 212 MU
B. 277 MU
C. 326 MU
D. 180 MU
Answer: C
Objective: IV.3
Why: MU = 180 / (0.850 × 0.650) = 180 / 0.5525 = 326 MU. Check: 326 × 0.5525 = 180 cGy. Omitting the wedge gives 180 / 0.850 = 212 MU, and the wedge would then deliver 212 × 0.5525 = 117 cGy, which is 0.65 × 180.

### Q4
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. The calculation point is 105 cm from the source on an SAD setup. Sc = Sp = WF = TF = 1. TMR = 0.750. Dose = 200 cGy. (100/105)^2 = 0.907. How many MU?
A. 267 MU
B. 294 MU
C. 242 MU
D. 200 MU
Answer: B
Objective: IV.3
Why: MU = 200 / (0.750 × 0.907) = 200 / 0.680 = 294 MU. Check: 294 × 0.680 = 200 cGy. Ignoring inverse square gives 200 / 0.750 = 267 MU. Inverting the distance ratio, (105/100)^2 = 1.103, gives 200 / (0.750 × 1.103) = 242 MU, which is too small because the point is farther than the calibration distance.

### Q5
Stem: Prescription 180 cGy. Calibration is 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Isocenter, TMR = 0.750, WF = 0.600 was omitted, wedge remains in the beam, other factors 1. What dose is delivered?
A. 180 cGy
B. 108 cGy
C. 240 cGy
D. 300 cGy
Answer: B
Objective: IV.3
Why: The omitted-factor MU is 180 / 0.750 = 240. Delivered dose = 240 × 0.750 × 0.600 = 108 cGy. And 108 / 180 = 0.600, the wedge factor. The correct MU is 400, and 400 × 0.450 = 180 cGy.

### Q6
Stem: Which line is an SSD monitor-unit formula?
A. Dose / (output × Sc × Sp × TMR × WF × inverse square)
B. Dose / (output × Sc × Sp × PDD/100 × WF × TF × ISF), with ISF = (SAD / (SSD + dmax))^2
C. Dose × PDD × TMR
D. Dose / (output × Mayneord F × TMR)
Answer: B
Objective: IV.3
Why: SSD uses PDD and the inverse-square move from the SAD calibration point to the actual dmax location. SAD uses TMR and (SAD/SPD)^2. The two depth quantities are not multiplied together. Mayneord F is not an extra factor on top of a TMR.

### Q7
Stem: The linac is calibrated to 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. SSD + dmax = 100 cm. Jaws equivalent square give Sc = 1.040. The blocked opening gives Sp = 0.970 and PDD = 75%. WF = TF = 1. Dose = 200 cGy. How many MU?
A. 264 MU
B. 267 MU
C. 200 MU
D. 151 MU
Answer: A
Objective: IV.3
Why: Denominator = 1.040 × 0.970 × 0.750 = 0.7566. MU = 200 / 0.757 = 264 MU. Check: 264 × 0.757 = 200 cGy. Using the jaw field for Sp, or the block for Sc, changes this product. 200 × 0.757 = 151 puts the factors in the numerator.

### Q8
Stem: A plan check finds PDD and TMR both written in the same denominator for one photon beam. What should the second checker do?
A. Average the PDD fraction and the TMR
B. Keep the depth factor that matches the setup: PDD for SSD, TMR for SAD, and delete the other
C. Multiply both and also apply Mayneord F
D. Replace both with the wedge factor
Answer: B
Objective: IV.3
Why: One beam is either fixed-SSD or fixed source-to-point distance. Using both depth factors double-counts attenuation and mixes two geometries. Mayneord F does not repair that mix. The wedge factor, if a wedge is present, is an additional denominator term, not a substitute for PDD or TMR.
