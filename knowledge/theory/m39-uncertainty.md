# Module 39. Sources of uncertainty and limitations in computer-based treatment planning

Original notes for MDCB CMD prep. Objective IV.6. The dose grid is the limitation this module is named for. The algorithm, the density table, and the image are the others.

## Sources of Uncertainty

**Objectives:** IV.6, IV.1, IV.4

**What the exam expects:** A coarse dose-grid matrix misses a narrow maximum in a serial organ. A DVH built from that grid inherits the miss and still cannot show where the hot spot is or whether the contour is right. Name the other limits without inventing a tolerance the stem did not give.

The reported dose is the dose on the calculation grid, not a continuous measurement. The planning system stores a value at each voxel. If the true peak sits between coarse voxel centers, the reported maximum is the neighboring sample, and it is lower than the peak. Serial organs are judged on a small volume or a point maximum (cord, optic nerve, brainstem). A 4–5 mm grid is a real risk there. Stereotactic and serial-organ maxima are calculated on a fine grid, commonly 1–2 mm.

A DVH cannot prove:

- which slice holds the maximum
- that the contour matches the anatomy
- that the grid was fine enough to see a narrow peak
- that the algorithm handled an interface

### Worked example: grid sampling

**Given.** Along the cord, dose at 2 mm spacing is 48.0, 51.0, 54.2, 50.5, and 47.0 Gy. A 6 mm grid keeps the samples at the first and fourth positions only: 48.0 Gy and 50.5 Gy.

**Arithmetic.** True maximum = 54.2 Gy. Grid maximum = 50.5 Gy. Difference \(= 54.2 - 50.5 = 3.7\) Gy.

**Check.** \(50.5 + 3.7 = 54.2\). The 54.2 Gy sample is 4 mm from the 48.0 Gy sample and 2 mm from the 50.5 Gy sample, so a grid whose centers are 6 mm apart never lands on it.

**Result means.** The plan report says the cord maximum is 50.5 Gy. The peak on the fine samples is 54.2 Gy. A constraint written at 50 Gy or at 54 Gy can change its pass/fail result when the only change is the matrix. Recalculate serial-organ maxima on a finer grid before you defend the number. The DVH of the coarse grid will show 50.5 Gy and will look precise.

**Other limits, each one sentence.** The numeric example above is the grid. These are the companions an item may name instead:

- Algorithm: a pencil beam’s weak lateral scatter in lung (module 33 and module 37). Monte Carlo still needs enough histories or the result is noisy.
- Density: contrast, metal, and artifact on the HU table (module 37).
- Body contour cut off, or a couch and immobilization device missing from the CT, so the beam traverses material the calculation never saw.
- Calculation point placed on a steep gradient, where a 2 mm shift changes the dose more than the algorithm tolerance.
- Small fields, where charged-particle equilibrium fails and output factors must be measured.
- Motion and interplay between leaves and a moving target, which a static dose grid does not show.
- Image registration error, rigid or deformable (module 38), so the dose is scored on the wrong anatomy.
- Isocenter localization and external-contour stylus error, which shift every beam together.

**Wrong turns**

- Quoting a DVH maximum to three significant figures from a 5 mm grid and treating the tenths of a gray as real.
- Blaming only the algorithm when the grid, not the kernel, dropped a 3.7 Gy peak.
- Adding a second plan’s dose grid without DIR and calling the sum an uncertainty of a few percent. That error can be an entire organ.
- Using PDD instead of TMR, or a wedge factor, to explain a grid artifact. Those are calculation-factor mistakes from modules 34 and 35, not matrix mistakes.

**Traps.** When a serial-organ maximum looks conveniently low, ask for the grid size before you ask for a new beam arrangement.

**Sources.** AAPM TG-101 discusses grid size for stereotactic plans in the context of small serial-organ volumes. Khan and Gibbons cover the classical calculation uncertainties (contour, inhomogeneity, scatter). TG-132 for registration as a separate uncertainty from the dose engine.

## Accuracy Goals, Error Budgets, and Margin Statistics

**Objectives:** IV.6

**What the exam expects**

You can quote the overall accuracy goal for delivered dose and say where it comes from. You can combine independent uncertainties in quadrature and recognize that a linear sum overstates the total. You know what fraction of a normal distribution lies within one, two, and three standard deviations, and you do not fall for the "three standard deviations is 99 percent" trap. You can compute a mean and a sample standard deviation from a handful of readings. You can separate systematic from random error, say how each enters a PTV margin, and reproduce the van Herk recipe. You can place the TG-100 risk priority number on its scale.

**Core facts**

The overall goal. ICRU Report 24 (1976) set the classic target: the dose delivered to the target volume should be within plus or minus 5 percent of the prescribed dose. The reasoning is the steepness of tumor-control and normal-tissue-complication curves, where a 5 percent dose change can move outcome by several percent. Later analyses have argued for tighter figures (around 3 percent as one standard deviation), but the number the exam expects, and the one this bank uses, is plus or minus 5 percent overall.

Combining uncertainties. Independent uncertainties do not add linearly; they add in quadrature, as the square root of the sum of squares. A budget of 2.5 percent for absolute calibration, 3 percent for the planning-system algorithm, 3 percent for daily setup and patient geometry, and 2 percent for the monitor-unit calculation combines as the square root of 6.25 + 9 + 9 + 4 = 28.25, which is about 5.3 percent. The linear sum, 10.5 percent, is the wrong method and is roughly double. The quadrature total is dominated by the largest terms; halving the 2 percent term barely moves the result, while cutting a 3 percent term to 2 percent drops the total to about 4.8 percent. A budget that lands just above 5 percent is why every link of the chain is held to a tolerance of 1 to 3 percent: no single step is allowed to spend the whole budget.

Standard deviation intervals. For a normal distribution, plus or minus one standard deviation holds about 68 percent of values, plus or minus two holds about 95 percent, and plus or minus three holds about 99.7 percent. The 99 percent interval is plus or minus about 2.6 standard deviations, not three. A source that says "three standard deviations covers 99 percent" has rounded the wrong way; the bank uses 99.7 percent. The 95 percent figure is the one that appears in margin recipes and in the usual tolerance language of "two sigma."

Mean and standard deviation from a small set. The mean is the sum divided by the count. The sample standard deviation squares each deviation from the mean, sums the squares, divides by one less than the count, and takes the square root. Dividing by the full count gives the population standard deviation, which is smaller; for a handful of QA readings the sample form is the convention.

Systematic and random error. A systematic error is the same at every fraction: a contour drawn around the wrong anatomy, a planning CT that caught the organ in an unusual position, a misplaced isocenter mark, a calibration offset. It shifts the whole delivered dose distribution relative to the target. A random error changes from fraction to fraction: daily setup scatter, bladder and rectal filling, breathing differences. Over a course it blurs the dose distribution rather than shifting it. Because a shift moves every fraction the same way, a millimeter of systematic error costs far more coverage than a millimeter of random error. Offline protocols such as NAL estimate and remove the systematic part; online daily imaging reduces both.

The van Herk margin. The population recipe for a CTV-to-PTV margin that gives 90 percent of patients at least 95 percent of the prescription over the whole CTV is 2.5 times the systematic standard deviation plus 0.7 times the random standard deviation, written 2.5Σ + 0.7σ. The 0.7 factor is an approximation that already includes the penumbra blurring; the full form is 2.5Σ + 1.64 × (σ' − σp), where σ' combines the random error with the penumbra width σp, about 3.2 mm. The systematic and random components are each combined in quadrature from their own sources before the recipe is applied.

TG-100 risk priority number. In a failure-mode-and-effects analysis each failure mode is scored one to ten for occurrence, severity, and lack of detectability, and the risk priority number is their product, so the scale runs from 1 to 1,000. TG-100's example uses a risk priority number above about 125, or a severity score of 8 or more, as the trigger for a new control. Module 42 has the worked example and the fault-tree context; this module only places the number among the uncertainty tools.

**Formulas**

Total uncertainty = square root of (u1 squared + u2 squared + u3 squared + ...).

Mean = sum of readings / n. Sample SD = square root of [sum of (reading − mean) squared / (n − 1)].

PTV margin ≈ 2.5 × Σ + 0.7 × σ, with Σ the systematic SD and σ the random SD across the population.

Risk priority number = occurrence × severity × detectability, each 1–10, range 1–1,000, act above about 125.

**Worked example (quadrature budget)**

Given: calibration 2.5 percent, algorithm 3 percent, setup and geometry 3 percent, monitor-unit calculation 2 percent. Squares: 6.25, 9, 9, 4. Sum: 28.25. Square root: 5.32 percent, reported as 5.3 percent. Check: 5.3 squared is 28.1, close to 28.25. The total exceeds the 5 percent goal by a little, and the two 3 percent terms are where it is spent. The linear sum of 10.5 percent is the wrong method.

**Worked example (small data set)**

Given: five daily output readings differ from the baseline by +1, +2, −1, +3, and 0 percent. Mean = (1 + 2 − 1 + 3 + 0) / 5 = 5 / 5 = 1.0 percent. Deviations from the mean: 0, 1, −2, 2, −1. Squares: 0, 1, 4, 4, 1. Sum: 10. Sample variance = 10 / 4 = 2.5. Sample SD = square root of 2.5 = 1.58, about 1.6 percent. Check: dividing by 5 instead gives the population SD of 1.41 percent, which is the smaller number and not the convention here. The mean of 1.0 percent is a systematic offset; the 1.6 percent is the random scatter around it.

**Worked example (margin)**

Given: for a prostate population the systematic setup SD is 3 mm and the random SD is 4 mm. Margin = 2.5 × 3 + 0.7 × 4 = 7.5 + 2.8 = 10.3 mm. Check: the systematic term is 7.5 of the 10.3 mm even though the random SD is the larger number, which is the point of the recipe. Swapping the coefficients, 2.5 × 4 + 0.7 × 3 = 12.1 mm, is the common error. Adding the SDs, 7 mm, or multiplying their sum by 2.5, 17.5 mm, are not the recipe.

**Traps**

- Adding uncertainties linearly, or forgetting the square root after summing the squares.
- Quoting 99 percent for plus or minus three standard deviations. It is 99.7 percent; 99 percent is about 2.6 SD.
- Dividing by n instead of n − 1 for a small sample, or reporting the variance as the standard deviation.
- Treating a contouring error as random because it differs between patients. For one patient it is the same every fraction, which is systematic.
- Writing the margin recipe as 2.5σ + 0.7Σ, or using it when daily online correction has already removed most of the systematic error without re-estimating Σ.
- Adding the three TG-100 scores, or placing the trigger at 1,000.

**Sources**

- ICRU Report 24, for the plus or minus 5 percent accuracy requirement.
- van Herk et al., the probability of correct target dosage, for the 2.5Σ + 0.7σ recipe.
- AAPM TG-100, for the risk priority number scale and the action trigger; module 42 for the worked FMEA.
- Khan and Gibbons, for the quadrature combination of independent uncertainties in the dosimetry chain.
