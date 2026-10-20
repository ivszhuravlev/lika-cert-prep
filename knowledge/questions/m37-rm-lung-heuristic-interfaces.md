# Module 37. Corrections for Tissue Inhomogeneities and Density Overrides

Original items. Lung rule of thumb, direction of the uncorrected error, composite paths, override decisions, classical method contrasts, and interface dose.

## Lung Rules of Thumb, Composite Paths, and Interface Dose

### Q1
Stem: A 6 MV beam crosses 8.0 cm of lung before reaching a mediastinal point. Using the rule of thumb of 3.5 percent per centimeter of lung, about how much higher is the dose at that point than a homogeneous water calculation predicts?
A. 3.5 %
B. 28 %
C. 14 %
D. 80 %
Answer: B
Objective: IV.4
Why: The heuristic is thickness times the per-centimeter gain: 8.0 × 3.5 = 28 percent. Check: a TMR-ratio calculation for 8 cm of lung at density 0.25 gives a gain near 29 percent, so the heuristic lands in the right range. Stopping at 3.5 percent ignores the thickness. Fourteen percent is what the 18 MV figure of about 2 percent per centimeter would give for a shorter path and is the wrong energy. Eighty percent would need 10 percent per centimeter, which no megavoltage beam shows in lung.

### Q2
Stem: A lung plan is calculated with the heterogeneity correction turned off and the monitor units are set so the plan shows the prescription at a target beyond 9 cm of lung. What happens when those monitor units are delivered?
A. The target is underdosed, because lung scatters the beam away
B. The dose is correct, because the correction only changes the isodose display
C. The target is underdosed, because the calculated dose was too low
D. The target and the tissue beyond it are overdosed, because the plan asked for more monitor units than the real lung path needs
Answer: D
Objective: IV.4
Why: A homogeneous calculation treats lung as water, predicts too little dose beyond it, and raises the monitor units to reach the prescription. The real lung attenuates less, so the delivered dose beyond the lung is higher than planned, and the exit-side cord, heart, or contralateral lung receives more than the plan shows. The calculated number is low, but the patient's dose is high; confusing those two gives the underdose answers. The correction changes the monitor units, not only the picture. Lateral scatter loss inside a small field is a separate algorithm issue, not the path-length direction.

### Q3
Stem: A posterior beam crosses 4.0 cm of soft tissue at relative density 1.00, 2.0 cm of spongy bone at 1.1, 3.0 cm of cortical bone at 1.65, and 6.0 cm of lung at 0.25. What is the water-equivalent depth to the point?
A. 12.65 cm
B. 15.00 cm
C. 12.45 cm
D. 10.50 cm
Answer: A
Objective: IV.4
Why: Effective depth = 4.0 × 1.00 + 2.0 × 1.1 + 3.0 × 1.65 + 6.0 × 0.25 = 4.00 + 2.20 + 4.95 + 1.50 = 12.65 cm. Check: the bone layers add 2.15 cm of water over their physical thickness and the lung removes 4.50 cm, and 15.0 + 2.15 − 4.50 = 12.65 cm. The physical depth is 15.00 cm, the uncorrected value. Leaving the spongy bone at 1.0 gives 12.45 cm. Treating both bone layers as water gives 4 + 2 + 3 + 1.5 = 10.50 cm.

### Q4
Stem: The planning CT of a breast patient shows a 4 mm calcified granuloma in the lung and several small surgical clips in the tumor bed. Which of these should receive a density override before the dose calculation?
A. The calcification, overridden to water so that it does not perturb the lung dose
B. Both, overridden to the density of cortical bone
C. Neither; both are real material that will be present at treatment and are sampled correctly by the scanner
D. The clips only, overridden to air because metal saturates the detector
Answer: C
Objective: I.9
Why: An override replaces a CT number that misrepresents the material in the beam at treatment, such as transient contrast, saturated metal, or a streak artifact. A calcification is real tissue, is correctly sampled, is present at every fraction, and is small, so overriding it to water removes real attenuation. Small clips are likewise left alone; only a large metal mass that saturates the scanner is overridden, and then to the real alloy density, never to air. Neither object is cortical bone.

### Q5
Stem: Two hand corrections are compared for a point beyond a lung slab. One reads the TMR at the water-equivalent depth and uses that value directly. The other divides the TAR at the water-equivalent depth by the TAR at the physical depth, both for the field size at the point. What does the second method include that the first does not?
A. Electron transport across the lung–tissue interface
B. The change in scatter contribution with depth for the actual field size
C. The position of the lung slab relative to the calculation point
D. The three-dimensional density distribution around the point
Answer: B
Objective: IV.4
Why: The TAR-ratio method carries the field size through both TARs, so the scatter change between the two depths enters the correction factor; the effective-depth method only shifts the lookup depth and takes scatter as if the field were at that depth in water. Neither method knows where the slab sits; the Batho power-law method adds that. The three-dimensional density picture belongs to the equivalent-TAR method. No classical correction transports electrons.

### Q6
Stem: Four correction approaches are listed: equivalent-TAR, pencil beam with a path-length correction, convolution/superposition, and Monte Carlo. Which ordering runs from least to most accurate in lung?
A. Monte Carlo, convolution/superposition, pencil beam, equivalent-TAR
B. Pencil beam, equivalent-TAR, Monte Carlo, convolution/superposition
C. Convolution/superposition, pencil beam, equivalent-TAR, Monte Carlo
D. Equivalent-TAR, pencil beam, convolution/superposition, Monte Carlo
Answer: D
Objective: IV.4
Why: The classical TAR-based corrections only modify primary attenuation and scatter lookups, so they sit at the bottom. A pencil beam corrects path length along each pencil but does not re-transport lateral electrons in low density. Convolution/superposition scales its kernels with density and handles lateral disequilibrium far better. Monte Carlo transports photons and electrons through the actual densities and is the reference at interfaces. The other orderings place a classical method above a transport method.

### Q7
Stem: A 2.5 cm lung tumor surrounded by lung is planned with a 3 by 3 cm field. The planner considers 6 MV and 18 MV. Which statement about the dose at the lung–tumor boundary is correct?
A. The proximal tumor edge is underdosed by rebuild-up, and the deficit is larger at 18 MV and with the small field
B. The proximal tumor edge is overdosed because lung scatters extra electrons into the tumor
C. Energy does not matter at the boundary because both beams are megavoltage
D. The deficit is smaller at 18 MV because the beam is more penetrating
Answer: A
Objective: IV.4
Why: Where the beam passes from lung into tumor the density rises and dose must build up again, so the proximal edge receives less than a path-length method predicts. The electrons set in motion by an 18 MV beam travel farther in lung and the small field loses lateral electron equilibrium, so the underdose grows with energy and shrinks with field size. That is why lung stereotactic plans use 6 MV and no more than 10 MV. Penetration describes attenuation beyond the slab, not the interface deficit, and lung does not add electrons to the tumor edge.

### Q8
Stem: A homogeneous water calculation for a 6 MV lung field gives 250 MU to a point beyond 8.0 cm of lung. For a quick check the dosimetrist applies a 3 percent per centimeter lung gain. About how many monitor units does the corrected hand estimate require?
A. 310 MU
B. 190 MU
C. 202 MU
D. 250 MU
Answer: C
Objective: IV.4
Why: Gain = 8.0 × 3 = 24 percent, so the lung path delivers 1.24 times the water dose per monitor unit, and the corrected monitor units are 250 / 1.24 = 201.6, about 202 MU. Check: 202 × 1.24 = 250. Multiplying instead, 250 × 1.24 = 310 MU, pushes the dose further in the wrong direction. Subtracting 24 percent of the monitor units, 250 × 0.76 = 190 MU, is not the inverse of a 24 percent gain. Leaving 250 MU is the uncorrected plan that overdoses the patient.
