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

## Lung Rules of Thumb, Composite Paths, and Interface Dose

**Objectives:** IV.4, I.9

**What the exam expects**

You can sanity-check a lung correction with a percent-per-centimeter heuristic before you trust the TMR-ratio arithmetic. You can state the direction of the error when the heterogeneity correction is left off in a lung plan, in terms of what the patient receives. You can build an effective depth through a three-material path that includes soft bone and hard bone. You know which CT findings need an override and which do not. You can contrast the effective-depth method with the TAR-ratio and power-law methods, and you can say what happens at the lung–tumor boundary when the field is small and the energy is high.

**Core facts**

The lung heuristic. For a 6 MV beam, every centimeter of lung the ray crosses instead of soft tissue raises the dose beyond the lung by roughly 3 to 3.5 percent, because the lung at density 0.25–0.30 removes only a quarter to a third of the photons that a centimeter of water would remove. At 18 MV the beam is more penetrating and the per-centimeter gain is smaller, about 2 percent. The number is a sanity check, not a calculation: a plan that shows a 30 percent correction for 3 cm of lung, or a 2 percent correction for 10 cm of lung, has something wrong with its densities. Lung is the site where turning the heterogeneity correction on changes the monitor units most; pelvis and brain plans move by a percent or two, a lung plan by ten to thirty.

Direction of the error when the correction is off. A homogeneous calculation treats the lung as water, so it predicts too little dose beyond the lung and asks for more monitor units to reach the prescription. Those monitor units are delivered into a chest that attenuates less than water. The patient is overdosed beyond the lung, and the mediastinum, cord, or contralateral lung on the exit side gets more than the plan shows. The exam phrasing to keep straight is that the calculated dose is low and the delivered dose is high. A key that says the patient is underdosed when the correction is off has confused the plan's number with the patient's dose. The one place the direction reverses is inside a small field within the lung itself, where lateral electron loss lowers the dose at the field edge; that is an algorithm problem, not the path-length direction.

Composite paths with soft bone. Density values for a hand calculation are lung 0.25, soft tissue 1.00, soft (spongy) bone about 1.1, and hard (cortical) bone about 1.65 relative electron density. A ray through a vertebral body or a pelvis often crosses both bone types. Effective depth is still the sum of thickness times density; bone lengthens the water-equivalent path and lung shortens it, and they can partly cancel on one ray. Soft bone at 1.1 is close enough to water that leaving it at 1.0 changes a 2 cm slab by only 0.2 cm; hard bone at 1.65 changes a 3 cm slab by almost 2 cm, so it is the layer to get right.

What needs an override. Contrast, saturated metal, and metal streak artifacts are overridden because the CT number does not describe the material that will be in the beam at treatment. A calcification does not need an override. It is real tissue, it will be present on every treatment day, and the scanner has sampled it correctly; it is also usually small. Overriding calcifications to water removes real attenuation. The same logic applies to dense surgical clips only when they are small enough to be ignored; a large clip cluster is treated like other metal.

Effective depth versus TAR ratio. The effective-depth (equivalent path length) method looks up the TMR or TAR at the water-equivalent depth and uses that value directly. It corrects primary attenuation only; the scatter contribution is taken as if the field were in water at the shifted depth, and it ignores where the inhomogeneity sits. The isodose-shift method is the graphical version. The TAR-ratio method takes TAR at the effective depth divided by TAR at the physical depth, both for the same field size at the point, so the change in scatter with depth and field size enters the factor; it still ignores the position of the slab relative to the point. The Batho power-law method raises TARs to powers of the densities and does account for position: a lung slab far from the point changes the dose less than a slab just above it. The equivalent-TAR method (ETAR) scales the scatter field size by a weighted average density of the volume around the point, which is the first method that uses the three-dimensional density distribution. None of these transports electrons, so the usual accuracy ranking is equivalent-TAR and power-law below pencil beam, pencil beam below convolution/superposition, and Monte Carlo best.

Interface and rebuild-up. Where a beam leaves lung and enters a tumor or the chest wall, the density rises and the dose has to build up again, because the electrons set in motion in lung travel farther and fewer of them deposit energy per centimeter. The tumor's proximal edge is therefore under the dose a path-length method predicts, and the lung just beyond the distal edge of the tumor is also perturbed. The effect grows with photon energy, since higher-energy electrons travel farther, and it grows as the field shrinks, since a small field in low-density lung loses lateral electron equilibrium. This is why lung stereotactic plans use 6 MV, and no more than 10 MV, and why a pencil beam overstates the periphery dose of a small lung lesion. A convolution/superposition or Monte Carlo calculation shows the interface deficit; a path-length correction cannot.

**Formulas**

Heuristic percent gain beyond lung ≈ (lung thickness in cm) × (3 to 3.5 percent per cm) for 6 MV, about 2 percent per cm for 18 MV.

Corrected MU for a hand check ≈ homogeneous MU / (1 + fractional gain).

Effective depth = Σ (thickness × relative density), with lung 0.25, soft bone 1.1, hard bone 1.65.

**Worked example (heuristic as a check)**

Given: a 6 MV ray crosses 8.0 cm of lung on the way to a mediastinal point. The heuristic at 3 to 3.5 percent per cm predicts 8.0 × 3 = 24 percent to 8.0 × 3.5 = 28 percent more dose than a water calculation. The TMR-ratio method in the earlier lesson, with lung at 0.25 and the same 8 cm, gave 0.800 / 0.620 = 1.29, a 29 percent gain. The two agree within the heuristic's range, so the density table and the TMR lookup pass the sanity check. Had the homogeneous plan called for 250 MU, the corrected hand estimate is 250 / 1.26 = 198 MU for a 26 percent midpoint gain; multiplying instead, 250 × 1.26 = 315 MU, would raise the dose in the wrong direction.

**Worked example (composite path)**

Given: a posterior beam to a para-aortic node crosses 4.0 cm of soft tissue, 2.0 cm of spongy bone at 1.1, 3.0 cm of cortical bone at 1.65, and 6.0 cm of lung at 0.25. Effective depth = 4.0 × 1.00 + 2.0 × 1.1 + 3.0 × 1.65 + 6.0 × 0.25 = 4.00 + 2.20 + 4.95 + 1.50 = 12.65 cm. Physical depth = 4 + 2 + 3 + 6 = 15.0 cm. Check: bone added 2.20 + 4.95 − 5.00 = 2.15 cm of water, lung removed 6.00 − 1.50 = 4.50 cm, net 15.0 − 4.50 + 2.15 = 12.65 cm. The lung wins on this ray and the point gets more dose than a water calculation shows.

**Traps**

- Reading "heterogeneity correction off in lung" as a patient underdose. The plan's number is low; the patient's dose is high.
- Applying the 6 MV percent-per-centimeter figure to an 18 MV beam.
- Overriding a calcification or a small clip to water.
- Describing the effective-depth method as if it included the scatter change that the TAR-ratio method includes, or as if either method knew where the slab was. Only the power-law and ETAR methods do.
- Choosing 15 or 18 MV for a small lung lesion to "penetrate better." The higher energy makes the interface underdose worse.

**Sources**

- Khan and Gibbons, tissue inhomogeneity corrections: effective depth, TAR ratio, power law, ETAR, and the interface discussion.
- AAPM TG-65, tissue inhomogeneity corrections for megavoltage photon beams, for the method ranking and the lung energy recommendation.
- AAPM TG-101 for the energy choice in lung stereotactic treatments.

## Bone Corrections by Energy

**Objectives:** IV.4, I.9

**What the exam expects**

You can state how much a slab of cortical bone lowers the dose beyond it per centimeter at megavoltage energies, how that changes with beam energy, and why the correction uses electron density rather than physical density. You can run the bone number next to the lung rule from the previous lesson, including on one ray that crosses both. You can say what happens to the dose inside the bone itself at megavoltage and at orthovoltage energies.

**Core facts**

Bone numbers. Cortical bone has a physical density of about 1.8 to 1.85 g per cc, and the bank's recall table uses 1.85. Its electron density relative to water is lower, about 1.65, because bone has fewer electrons per gram than water (less hydrogen). At megavoltage energies Compton scattering dominates, and Compton attenuation scales with electron density, so the correction uses 1.65. Each centimeter of cortical bone adds 1.65 − 1.00 = 0.65 cm of water-equivalent path. Spongy bone at about 1.1 adds only 0.1 cm per cm and is nearly water.

Magnitude by energy. With the bank's 6 MV heuristic of about 3.5 percent per centimeter of water-equivalent path, one centimeter of cortical bone lowers the dose beyond it by about 0.65 × 3.5 ≈ 2.3 percent. At 18 MV, where the per-centimeter figure is about 2 percent, the bone reduction is about 1.3 percent per cm. At Co-60 and low megavoltage energies, where the beam attenuates about 4.5 to 5 percent per cm of water, the reduction is about 3 percent per cm of bone. The direction to keep: the more penetrating the beam, the smaller the per-centimeter bone correction. In all cases the bone effect at megavoltage is "a few percent per centimeter", which is smaller than the lung effect per centimeter (3 to 3.5 percent at 6 MV) because lung departs from water by 0.7 to 0.75 in density while bone departs by only 0.65, and in the opposite direction.

Electron density versus physical density. If a hand calculation uses the physical density ratio (1.85) in place of the electron density ratio (1.65) for a 2 cm slab, it adds 1.7 cm of water instead of 1.3 cm, an excess of 0.4 cm, which at 3.5 percent per cm is a 1.4 percent overcorrection. Planning systems convert CT number to relative electron density (or to mass density with an elemental composition) precisely so that the Compton correction comes out right; the electron-density ratio method is the standard megavoltage correction. At orthovoltage energies the photoelectric effect in calcium makes the attenuation depend on atomic number, and neither density ratio describes it.

Bone and lung on one ray. Effective depth is additive, so a ray that crosses 2 cm of cortical bone (adds 1.3 cm) and 4 cm of lung at 0.25 (removes 3.0 cm) is net 1.7 cm shorter in water-equivalent terms than its physical length. At 3.5 percent per cm the point beyond both receives about 6 percent more than a water calculation shows; the lung wins. Reversing the sign of either term, or forgetting the bone, gives the wrong answer in a predictable way.

Dose inside the bone. At megavoltage energies the absorbed dose within bone mineral is slightly lower than in soft tissue at the same depth, about 0.96 of the water value, because Compton dose per gram follows electrons per gram and bone has fewer. The soft tissue inside bone (marrow, Haversian canals) receives a few percent more than it would in homogeneous soft tissue because electrons set in motion in the surrounding mineral deposit dose there. At orthovoltage energies, photoelectric absorption in high-Z calcium makes the dose to bone several times the soft-tissue dose; that is the historical reason superficial and orthovoltage treatments were limited near bone and why megavoltage removed the problem.

**Formulas**

Extra water-equivalent path from bone = thickness × (relative electron density − 1).

Percent dose change beyond bone ≈ −(extra path in cm) × (percent per cm for the energy).

Worked: 3.0 cm of cortical bone at relative electron density 1.65, 6 MV, 3.5 percent per cm. Extra path = 3.0 × (1.65 − 1.00) = 3.0 × 0.65 = 1.95 cm. Dose change ≈ −1.95 × 3.5 = −6.8, about −7 percent. Check: the water-equivalent depth of the slab is 3.0 × 1.65 = 4.95 cm, which is 1.95 cm more than its physical 3.0 cm. The wrong-method results are −10.5 percent (3.0 × 3.5, treating bone as if every centimeter were an extra centimeter of water), −17 percent (3.0 × 1.65 × 3.5, using the full water-equivalent thickness instead of the excess), and +7 percent (sign reversed, treating bone like lung).

**Traps**

- Using 1.85 (physical density) in a Compton correction when the stem gives or implies electron density; use 1.65.
- Multiplying the bone thickness by the percent-per-centimeter figure without first subtracting 1 from the density ratio.
- Treating bone like lung and raising the dose beyond it.
- Applying the 6 MV percent-per-centimeter figure to Co-60 or to 18 MV. Lower energy, bigger correction.
- Saying dose inside bone is higher at megavoltage because bone is denser. It is slightly lower; the large bone dose is an orthovoltage effect.

**Sources**

- Khan and Gibbons, tissue inhomogeneity corrections and dose to bone, for the electron-density method and the bone and soft-tissue-in-bone discussion
- AAPM TG-65, tissue inhomogeneity corrections for megavoltage photon beams
- ICRU 44 tissue compositions, for the electron density of cortical bone
