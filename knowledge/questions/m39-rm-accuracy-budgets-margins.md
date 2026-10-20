# Module 39. Sources of uncertainty and limitations in computer-based treatment planning

Original items. Accuracy goal, quadrature budgets, normal-distribution intervals, small-sample statistics, systematic versus random error, the margin recipe, and the TG-100 risk number.

## Accuracy Goals, Error Budgets, and Margin Statistics

### Q1
Stem: ICRU Report 24 set the classic requirement for the accuracy of dose delivered to the target volume. What is that overall tolerance?
A. plus or minus 1 %
B. plus or minus 10 %
C. plus or minus 5 %
D. plus or minus 2 %
Answer: C
Objective: IV.6
Why: ICRU 24 concluded that the dose to the target should be delivered within plus or minus 5 percent of the prescription, on the grounds that tumor-control and complication curves are steep enough for a 5 percent change to alter outcome. Plus or minus 1 or 2 percent are the tolerances for single links in the chain, such as output calibration, not the overall goal. Plus or minus 10 percent is loose enough to move cure and complication rates measurably.

### Q2
Stem: A department estimates independent uncertainties of 2.5 percent for absolute calibration, 3 percent for the planning algorithm, 3 percent for daily setup and geometry, and 2 percent for the monitor-unit calculation. What is the combined uncertainty?
A. 5.3 %
B. 10.5 %
C. 28.3 %
D. 2.6 %
Answer: A
Objective: IV.6
Why: Independent uncertainties add in quadrature. Squares: 6.25 + 9 + 9 + 4 = 28.25. Square root: 5.32, reported as 5.3 percent. Check: 5.3 squared is about 28.1. The linear sum 10.5 percent is the wrong method and roughly doubles the result. Stopping at 28.3 percent omits the square root. Dividing the linear sum by four gives 2.6 percent, an average rather than a combined uncertainty.

### Q3
Stem: The combined budget in the previous situation is slightly above the 5 percent goal. Which single change lowers the total the most?
A. Reducing the monitor-unit calculation term from 2 percent to 1 percent
B. Reducing the calibration term from 2.5 percent to 2 percent
C. Re-measuring each component so that it is quoted with one more decimal place
D. Reducing one of the 3 percent terms to 2 percent
Answer: D
Objective: IV.6
Why: In a quadrature sum the largest terms dominate because they are squared. Cutting a 3 percent term to 2 percent removes 9 − 4 = 5 from the sum of squares, taking the total from the square root of 28.25 to the square root of 23.25, about 4.8 percent. Cutting the 2 percent term to 1 percent removes only 3 and the calibration change removes only 2.25, each leaving the total near 5.1 percent. Extra decimal places change the quoting, not the uncertainty.

### Q4
Stem: A review sheet states that plus or minus three standard deviations contains 99 percent of a normally distributed set of readings. Which statement is correct?
A. The sheet is correct; 99 percent is the three-sigma interval
B. The sheet is wrong; three standard deviations contain about 99.7 percent, and 99 percent corresponds to about 2.6 standard deviations
C. The sheet is wrong; three standard deviations contain 95 percent
D. The sheet is wrong; three standard deviations contain 68 percent
Answer: B
Objective: IV.6
Why: The normal-distribution intervals are about 68 percent within one SD, 95 percent within two, and 99.7 percent within three. A 99 percent interval sits at roughly 2.6 SD. Rounding 99.7 to 99 is the trap this item tests. Ninety-five percent is the two-sigma interval and 68 percent is the one-sigma interval, not three.

### Q5
Stem: Five daily output readings differ from the baseline by +1, +2, −1, +3, and 0 percent. What is the sample standard deviation of these readings?
A. 1.0 %
B. 2.5 %
C. 1.6 %
D. 1.4 %
Answer: C
Objective: IV.6
Why: Mean = (1 + 2 − 1 + 3 + 0) / 5 = 1.0 percent. Deviations: 0, 1, −2, 2, −1; squares: 0, 1, 4, 4, 1; sum 10. Sample variance = 10 / (5 − 1) = 2.5, and the square root is 1.58, reported as 1.6 percent. Check: 1.6 squared is about 2.5. The 1.0 percent is the mean, which is a systematic offset and not the spread. The 2.5 is the variance, not its square root. Dividing by 5 instead of 4 gives the population SD of 1.4 percent, which is not the small-sample convention.

### Q6
Stem: Which of the following setup or planning errors is systematic for a given patient rather than random?
A. The physician's CTV contour includes a slice of normal tissue and misses part of the tumor
B. Day-to-day variation in rectal filling
C. Breathing amplitude that differs from one fraction to the next
D. A tattoo alignment that scatters a few millimeters each morning
Answer: A
Objective: IV.6
Why: A delineation error is baked into the plan and repeats identically at every fraction, so it shifts the entire delivered distribution: that is a systematic error. The same holds for a planning CT that caught an organ in an odd position or a wrongly placed isocenter. Rectal filling, breathing differences, and daily tattoo scatter change from fraction to fraction and blur rather than shift the distribution, which makes them random.

### Q7
Stem: For a prostate population the systematic setup standard deviation is 3 mm and the random setup standard deviation is 4 mm. Using the van Herk recipe of 2.5 times the systematic plus 0.7 times the random standard deviation, what CTV-to-PTV margin results?
A. 7.0 mm
B. 10.3 mm
C. 17.5 mm
D. 12.1 mm
Answer: B
Objective: IV.6
Why: Margin = 2.5 × 3 + 0.7 × 4 = 7.5 + 2.8 = 10.3 mm. Check: the systematic term supplies 7.5 of the 10.3 mm even though the random SD is numerically larger, which is the point of the recipe. Adding the two standard deviations gives 7.0 mm and ignores the coefficients. Multiplying their sum by 2.5 gives 17.5 mm. Swapping the coefficients, 2.5 × 4 + 0.7 × 3, gives 12.1 mm.

### Q8
Stem: Why does the population margin recipe weight the systematic standard deviation about three and a half times more heavily than the random standard deviation?
A. Systematic errors are measured in centimeters and random errors in millimeters
B. Random errors are always smaller than systematic errors
C. Random errors are removed by daily imaging while systematic errors cannot be corrected
D. A systematic error shifts the whole dose distribution off the target at every fraction, whereas a random error only blurs the edge of the distribution over the course
Answer: D
Objective: IV.6
Why: A shift that repeats identically at every fraction moves the cumulative dose off the CTV, so coverage falls quickly with each millimeter. A random error points in a different direction each day and averages into a blurred penumbra, which costs much less coverage per millimeter. Both are measured in the same units and either can be larger. Offline protocols such as NAL target precisely the systematic part, so the claim that it cannot be corrected is backwards.

### Q9
Stem: In a TG-100 failure-mode-and-effects analysis, over what range does the risk priority number run, and what value is commonly used as the trigger for adding a control?
A. 1 to 100, acting above 50
B. 3 to 30, acting above 20
C. 1 to 1,000, acting above about 125
D. 0 to 1, acting above 0.5
Answer: C
Objective: VII.7
Why: Occurrence, severity, and lack of detectability are each scored 1 to 10 and multiplied, so the risk priority number spans 1 to 1,000. TG-100's example treats a value above about 125, or a severity of 8 or more by itself, as the trigger for a new control. A range of 3 to 30 would come from adding the scores, which is the common error. The other ranges do not correspond to a product of three ten-point scales. Module 42 has the worked example.
