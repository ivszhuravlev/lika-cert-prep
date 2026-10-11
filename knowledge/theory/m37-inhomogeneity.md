# Module 37. Corrections for tissue inhomogeneities and density overrides

Original notes for MDCB CMD prep. Objectives IV.4 and I.9. The CT number of a voxel is only as useful as the density the planning system assigns to it.

Physical densities to recall, in g/cm³:

| Material | Physical density |
| --- | --- |
| Air | about 0.001 |
| Lung | about 0.25–0.30 |
| Water | 1.00 |
| Muscle | about 1.04 |
| Bone | about 1.85 |

These are the memory values. A planning system may store relative electron density rather than physical density. For these tissues the two are close. Metal and contrast are where the table stops being tissue.

## Density Overrides

**Objectives:** IV.4, I.9

**What the exam expects:** Contrast is not tissue. A density override replaces a bad CT number with the density of the material that will actually be in the beam on the treatment day. The usual contours are contrast in the bladder or vessels, a hip prosthesis, and dental metal, plus the streak artifact next to metal.

The HU-to-density table turns Hounsfield units into density. Water is the reference (HU near 0, density 1). Air is near HU −1000. Bone is high and positive. Iodinated contrast and metal sit far above soft tissue. Metal often saturates the scanner, and the streaks are artifact, not bone. If those voxels stay on the raw table, the algorithm attenuates a beam through a material that will not be there (contrast) or through a wrong density (saturated metal and its streaks).

Override rules used on these items:

- Contrast in bladder, bowel, or vessels: override to water or to the soft-tissue density of the fluid that remains after the contrast is gone. Contrast is not tissue.
- Hip prosthesis: override the metal to the alloy density from the operative note, inside a contour drawn on the metal itself. Override the streak artifacts back to the surrounding tissue (muscle, fat, or bone marrow), not to metal.
- Dental metal: same saturation and streak problem. Override, or keep beams from traversing the metal when the override is uncertain. Oral contrast and amalgam are not teeth and not tumor.

There is no single density that fits every hip alloy. Titanium is much less dense than cobalt-chrome or steel. Use the implant note. Do not invent one “prosthesis density” for every patient.

**Formula (water-equivalent thickness of a slab)**

\[
d_{\text{w}} = d \times \rho
\qquad
\Delta d = d(\rho_{\text{assigned}} - \rho_{\text{true}})
\]

- \(d\): physical thickness of the slab (cm)
- \(\rho\): physical density relative to water
- \(d_{\text{w}}\): water-equivalent thickness (cm)
- \(\Delta d\): extra water-equivalent thickness when the assigned density is wrong (cm)

This is a path-length picture. It is what a correction-based or pencil-beam longitudinal correction does. It is not lateral scatter.

### Worked example

**Given.** A contrast-filled bladder is 4.0 cm thick along a beam. The CT table assigns density 1.30. Urine on the treatment day is water, density 1.00.

**Substitute.**

\[
\Delta d = 4.0(1.30 - 1.00) = 4.0 \times 0.30 = 1.2 \text{ cm}
\]

**Check.** Water-equivalent path if the contrast is left in: \(4.0 \times 1.30 = 5.2\) cm. True path: \(4.0 \times 1.00 = 4.0\) cm. Difference: \(5.2 - 4.0 = 1.2\) cm.

**Result means.** The uncorrected plan thinks the beam crosses 1.2 cm of extra water. It over-attenuates and underestimates dose beyond the bladder. Override that contour to 1.00 g/cm³. Leaving HU 1.30 in the calculation treats contrast as if it were tissue.

**Wrong turns**

- Overriding contrast to bone (1.85) because the HU is “bright.”
- Overriding the whole streak from a hip to the metal density, which digs false bone-density tunnels through muscle.
- Using one universal prosthesis density.
- Deleting the override after the contrast scan and calculating on a non-contrast scan that was never registered. The override belongs on the dataset that is used for the dose.

**Traps.** Ask what will be in the patient during treatment, not what was in the patient during the scan.

**Sources.** AAPM guidance on CT-to-density tables and metal artifact (the HU lesson in the physics domain, objective I.9). Khan and Gibbons, inhomogeneity corrections, for the water-equivalent path.

## Lung vs. Soft Tissue Heterogeneity Correction

**Objectives:** IV.4, IV.1

**What the exam expects:** Effective depth is the first correction and it is only a path-length correction. Pencil beam fails in lung because lateral scatter is weak. Convolution/superposition is better because the kernel can stretch in low density. Monte Carlo is best at interfaces. Density numbers above are the ones to use when a stem gives “lung” without a number.

**Formula**

\[
d_{\text{eff}} = \sum_i d_i \rho_i
\]

- \(d_i\): physical thickness of layer \(i\) (cm)
- \(\rho_i\): density of that layer relative to water
- \(d_{\text{eff}}\): water-equivalent depth used in a TAR or TMR ratio method

### Worked example

**Given.** A ray to the calculation point crosses 3.0 cm of soft tissue (\(\rho = 1.00\)), then 8.0 cm of lung (\(\rho = 0.30\)), then 2.0 cm of soft tissue (\(\rho = 1.00\)).

**Substitute.**

\[
d_{\text{eff}} = 3.0(1.00) + 8.0(0.30) + 2.0(1.00) = 3.0 + 2.4 + 2.0
\]

**Arithmetic.** \(8.0 \times 0.30 = 2.4\). \(3.0 + 2.4 + 2.0 = 7.4\) cm. Physical depth \(= 3+8+2 = 13.0\) cm.

**Check.** \(13.0 - 7.4 = 5.6\) cm of “missing” water. The lung alone contributes that: \(8.0 - 2.4 = 5.6\).

**Result means.** A hand calculation that looks up TMR at 13 cm over-attenuates the beam. The water-equivalent depth is 7.4 cm, so the point gets more dose than a homogeneous water calculation predicts. That statement is only the path-length piece.

What the algorithm then does with lateral scatter:

- A pencil beam applies a correction like this along each pencil and does not move enough dose sideways. In lung it fails, especially near the mediastinum and the chest wall, where scatter from surrounding soft tissue matters.
- Convolution/superposition (and collapsed cone) scales the scatter kernel with density, so lateral disequilibrium in lung is handled better.
- A grid-based Boltzmann solver (Acuros) transports photons and electrons on the grid and needs the override densities to be the real materials.
- Monte Carlo handles the interface dose best, provided the histories are adequate and the lung density is the overridden value, not a contrast or artifact value.

**Wrong turns**

- Calling a pencil-beam plan “heterogeneity corrected” and therefore adequate in lung. The path length can be corrected while the lateral scatter is still wrong.
- Using physical depth in the TMR table when the question asks for radiologic (effective) depth.
- Using 1.0 for lung, or using air (0.001) for lung. Lung on this recall list is 0.25–0.30.
- Assuming Monte Carlo repairs a wrong density override. It transports whatever material you assigned.

**Traps.** Separate three decisions the stem may be mixing: the effective depth, the algorithm family, and whether an override is required. A right algorithm with contrast left at density 1.30 is still the wrong dose.

**Sources.** Khan and Gibbons, tissue inhomogeneity (equivalent path length, power-law and TAR-ratio methods as the historical corrections). AAPM TG-105 for Monte Carlo. Module 33 for the algorithm ranking.

## Corrections for Tissue Inhomogeneity Mini-Quiz

**Skills this quiz checks**

- Recall air about 0.001, lung about 0.25–0.30, water 1, muscle about 1.04, bone about 1.85.
- Compute water-equivalent depth as the sum of thickness times density, and the extra path from a wrong contrast density.
- Override contrast to fluid or water, metal to the real alloy, and streaks to surrounding tissue.
- Rank lung performance: pencil beam fails, superposition is better, Monte Carlo is best at the interface.
- Keep a path-length correction from being described as full lateral transport.
