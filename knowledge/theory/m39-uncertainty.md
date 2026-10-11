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
