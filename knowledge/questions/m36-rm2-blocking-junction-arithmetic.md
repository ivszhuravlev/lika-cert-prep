# Module 36. Special calculations

Original items. Cord-block timing from a tolerance dose, sector areas inside a Clarkson integration, junction-shift arithmetic, the percent-blocked effective square, orthogonal image pairs, and calculation points near a block edge.

## Cord-Block Timing, Sector Areas, and Junction Shifts

### Q1
Stem: A head and neck course delivers 1.8 Gy per fraction, and the spinal cord sits on the 100 percent isodose line. The planning limit for the cord is 45 Gy. After how many fractions must the posterior fields come off the cord?
A. 22 fractions
B. 28 fractions
C. 25 fractions
D. 30 fractions
Answer: C
Objective: IV.3
Why: The cord receives the full 1.8 Gy each fraction, so the number of fractions allowed is 45 / 1.8 = 25. Check: 25 × 1.8 = 45.0 Gy, exactly at the limit, so the off-cord fields start at fraction 26. This bank uses the 45 Gy figure stated in the problem; QUANTEC lists about 50 Gy for a 0.2 percent myelopathy risk, so always use the limit the question gives. Dividing by 2.0 Gy gives 22 fractions and 28 fractions results from 50 / 1.8, which applies a different tolerance. Thirty fractions would deliver 54 Gy to the cord.

### Q2
Stem: Same course, 1.8 Gy per fraction with a 45 Gy cord limit, but the plan shows the cord on the 105 percent isodose line. How many full fractions can be delivered before the cord must be blocked?
A. 23 fractions
B. 25 fractions
C. 26 fractions
D. 24 fractions
Answer: A
Objective: IV.3
Why: The cord dose per fraction is 1.8 × 1.05 = 1.89 Gy, so 45 / 1.89 = 23.8 fractions. The fraction count must stay at or below the limit, so round down to 23 fractions. Check: 23 × 1.89 = 43.5 Gy, under 45 Gy, while 24 × 1.89 = 45.4 Gy would exceed it. Ignoring the hot spot gives 25 fractions and overdoses the cord by about 2 Gy. Applying the 105 percent to the tolerance instead of to the fraction dose, 45 × 1.05 / 1.8, gives 26 fractions and moves the error the wrong way. Rounding 23.8 up to 24 crosses the limit.

### Q3
Stem: A 30-fraction course at 1.8 Gy per fraction keeps the cord at 100 percent until the cord limit of 45 Gy is reached, then switches to off-cord fields with an electron strip over the cord. How many fractions are delivered with the cord blocked?
A. 25 fractions
B. 5 fractions
C. 9 fractions
D. 7 fractions
Answer: B
Objective: IV.3
Why: Fractions allowed on the cord are 45 / 1.8 = 25, so the remaining 30 − 25 = 5 fractions are delivered off-cord. Check: 25 on-cord fractions give 45 Gy to the cord and the 5 off-cord fractions deliver 5 × 1.8 = 9 Gy to the target with the cord shielded, for a total of 54 Gy. Twenty-five is the number of on-cord fractions, not off-cord. Nine is the dose in Gy delivered off-cord, not a fraction count. Seven results from using 2.0 Gy per fraction, 45 / 2 = 22.5 rounded to 23, then 30 − 23.

### Q4
Stem: In a Clarkson sector integration a 10 degree sector has a radius of 8.0 cm from the calculation point to the field edge. What is the area of that sector, to two decimals?
A. 20.11 square centimeters
B. 1.40 square centimeters
C. 22.34 square centimeters
D. 5.59 square centimeters
Answer: D
Objective: IV.3
Why: A sector is the fraction theta/360 of the full circle: (10/360) × 3.1416 × 8.0² = 0.02778 × 201.06 = 5.585 square centimeters, reported as 5.59. Check: 36 such sectors make 36 × 5.585 = 201.1 square centimeters, the whole circle. Taking 10 percent of the circle instead of 10/360 gives 20.11. Computing the arc length, (10/360) × 2 × 3.1416 × 8.0 = 1.40 cm, is a length, not an area. Using 16 cm as if the radius were the diameter gives 22.34.

### Q5
Stem: In a Clarkson calculation for an irregular field, how is the scatter contribution of a single sector of angle theta formed?
A. The scatter-air ratio for a circular field of the sector's radius, multiplied by theta/360
B. The scatter-air ratio for a square field whose side equals the sector's radius, multiplied by theta/360
C. The sector area divided by the full field area, multiplied by the open-field scatter-air ratio
D. The scatter-air ratio for a circular field of the sector's diameter, divided by the number of sectors
Answer: A
Objective: IV.3
Why: Each sector is treated as a slice of a circular field whose radius is the distance from the point to the field edge along that ray; its scatter is the circular-field scatter-air ratio for that radius weighted by the sector's share of 360 degrees. Summing all sectors gives the average scatter-air ratio for the irregular field; with 36 sectors of 10 degrees the weight is 1/36. Square-field tables are not used directly because the integration is over circular geometry. Area ratios do not appear in the method; the radius determines the scatter, as in Q4 where the sector area is only a check on the geometry. Using the diameter looks up a circle four times too large in area.

### Q6
Stem: A craniospinal course of 30 fractions feathers the cranial-spinal junction over three equally weighted positions, each 1 cm superior to the last. How many fractions are delivered at each junction position, and how far is the final position from the first?
A. 15 fractions, 3 cm
B. 10 fractions, 3 cm
C. 15 fractions, 2 cm
D. 10 fractions, 2 cm
Answer: D
Objective: IV.3
Why: Three equally weighted positions divide the 30 fractions as 30 / 3 = 10 fractions each. Three positions require two shifts, so the final junction is 2 × 1 = 2 cm from the first. Check: 10 + 10 + 10 = 30 fractions and the junction occupies 0, 1, and 2 cm. Fifteen fractions each would be only two positions. Three centimeters counts three shifts, but moving from position one to position three takes two moves, a common off-by-one error.

### Q7
Stem: The spine field of a craniospinal plan is 36 cm long, and the collimator opens to a maximum of 40 cm. The junction will be moved superiorly, lengthening the spine field, in three equally spaced positions starting from the current one. What is the largest shift per step that stays within the collimator limit?
A. 4 cm
B. 1.3 cm
C. 2 cm
D. 1 cm
Answer: C
Objective: IV.3
Why: The spine field can grow by 40 − 36 = 4 cm. Three positions mean two shifts, so each step can be at most 4 / 2 = 2 cm. Check: 36, 38, and 40 cm are all at or below the 40 cm limit. A 4 cm step is the total available growth, not the per-step value, and the second shift would require 44 cm. Dividing by three positions, 4 / 3 = 1.3 cm, miscounts the shifts. One centimeter fits but is not the largest step possible.

### Q8
Stem: A spine field is 37 cm long and the collimator limit is 40 cm. The junction is shifted 1.5 cm superiorly at each move, lengthening the spine field each time. How many shifts fit before the limit is exceeded?
A. 3 shifts
B. 2 shifts
C. 1 shift
D. 4 shifts
Answer: B
Objective: IV.3
Why: Available growth is 40 − 37 = 3 cm, and 3 / 1.5 = 2 shifts fit exactly. Check: 37 → 38.5 → 40 cm, both within the limit, while a third shift would need 41.5 cm. Three shifts assumes the spine field could reach 41.5 cm. One shift is overly conservative and leaves 1.5 cm of allowed growth unused. Four shifts would be 6 cm of growth, twice what is available.

### Q9
Stem: A 10 by 10 cm photon field has 30 percent of its area covered by blocks. For the scatter and depth-dose lookup, what effective square field side should be used, to the nearest 0.1 cm?
A. 7.0 cm
B. 5.5 cm
C. 8.4 cm
D. 3.0 cm
Answer: C
Objective: IV.3
Why: The unblocked area is 0.70 × 100 = 70 square centimeters, and the square of that area has a side of 10 × sqrt(0.70) = 10 × 0.837 = 8.4 cm. Check: 8.37² = 70.0 square centimeters. This is a phantom-scatter approximation only; the collimator scatter factor still uses the open jaw setting, and a Clarkson integration is the more exact route when the blocked shape is irregular. Multiplying the side by 0.70 gives 7.0 cm and shrinks the area to 49 percent, not 70 percent. Using the blocked fraction, 10 × sqrt(0.30), gives 5.5 cm, the square equal to the blocked area. Three centimeters is 30 percent of the side and has no meaning.

### Q10
Stem: Which pair of gantry angles produces a truly orthogonal image pair for isocenter verification?
A. 0 degrees and 180 degrees
B. 85 degrees and 355 degrees
C. 45 degrees and 90 degrees
D. 30 degrees and 150 degrees
Answer: B
Objective: IV.3
Why: Orthogonal images are 90 degrees apart. From 85 to 355 degrees is 270 degrees one way, which is 360 − 270 = 90 degrees the other way, so the pair is orthogonal even though neither angle is a cardinal one. Check: 85 + 90 = 175 and 355 − 90 = 265; 355 is the same as −5, and −5 to 85 is 90 degrees. Zero and 180 degrees are opposed, giving the same projection reversed, and provide no information along the beam axis. Forty-five and 90 degrees are 45 degrees apart. Thirty and 150 degrees are 120 degrees apart.

### Q11
Stem: A hand calculation point is placed 3 mm inside the edge of a cerrobend block, where the planning system shows isodose lines spaced about 10 percent per 2 mm. Why is this a poor choice for a monitor unit check?
A. Block transmission must be added to the dose at this point, which hand calculations cannot do
B. The point lies outside the field, so the equivalent square cannot be defined
C. The gradient has no effect on the calculation; the point is acceptable if it is within the beam aperture
D. In a steep gradient a millimeter of positional uncertainty changes the dose by several percent, so the calculated and planned doses will disagree for reasons unrelated to the monitor units
Answer: D
Objective: IV.3
Why: At 10 percent per 2 mm a 1 mm uncertainty in where the point actually sits changes the local dose by about 5 percent, which is larger than the typical 2 to 3 percent agreement expected of an independent check. The recommended practice, consistent with TG-114, is to choose a point in a low-gradient region, several millimeters to a centimeter or more inside the open field, where the dose is well represented by the central-axis or off-axis factors. Block transmission applies under the block, not just inside its edge, and is in any case a small correction, not the reason for the disagreement. The point is inside the aperture, so an equivalent square can be defined; the trouble is the gradient, not the geometry. The gradient is exactly what makes the point unreliable.
