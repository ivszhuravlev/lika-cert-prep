# Module 11. HU Unit Conversion to CT Density Table (TPS)

Original notes for MDCB objective I.9.

## HU Scale

**MDCB:** I.9, IV.4

**What the exam expects**

You compute a Hounsfield number from a ratio of linear attenuation coefficients, recall air and water, and explain why the planning system uses a calibration curve rather than HU/1000 as electron density. You know when to override contrast, metal, and a motion-blurred ITV.

**Core facts**

The Hounsfield unit compares the linear attenuation coefficient of the voxel, at the scanner kV, with water:

HU = 1000 (μ − μ_water) / μ_water

Water is defined as 0. Air, μ about 0, is −1000. Those two anchors are exact statements of the definition. A storage scale on a 12-bit scanner often runs from about −1024 to +3071. The floor of −1024 is a digital limit. The HU of air is −1000. Do not pick −1024 as the physical answer for air.

Approximate clinical ranges, not definition anchors: fat around −50 to −100, muscle around +40 to +60, inflated lung several hundred units negative (a voxel at −700 is common in a numeric stem), dense bone +1000 and higher, metal high enough to clip the scale. Confirm a tissue table in Khan if the stem wants a specific fat or muscle value. The values you must be able to produce without a table are air −1000 and water 0.

Rearrangement: μ / μ_water = 1 + HU/1000. A voxel at HU = 0 has the attenuation of water. A voxel at HU = +1000 has twice the attenuation of water. A voxel at HU = −500 has half. That ratio is a kV linear-attenuation ratio. It is not automatically the relative electron density the dose engine needs.

At CT energies the photoelectric effect still inflates the attenuation of bone and of iodinated contrast. At megavoltage treatment energies Compton scatter dominates in tissue, so dose follows electron density, which tracks physical density more closely than it tracks a kV attenuation coefficient. The planning system therefore uses a measured CT-to-density curve, typically bilinear: one slope from air through lung to water, and a different slope from water through bone. A single formula HU/1000 applied to cortical bone will mis-assign density.

Stoichiometric calibration fills in materials the phantom did not contain. The curve you commissioned is for the kV you commissioned. Scanning at a different kV changes bone and contrast HU.

Overrides the exam expects you to consider:

- Iodinated contrast in vessels or bladder. The HU is high because of iodine, not because the electron density is that of bone. Override to tissue or water density for the photon calculation, or the plan attenuates through a vessel that is not actually dense at 6 MV.
- Metal and the streaks around it. A streak of +2000 HU through soft tissue is an artifact. Override the artifact path. A hip prosthesis needs an assigned density, not the clipped CT number.
- Lung ITV on an average CT. Motion blends tumor and lung, so the average HU inside the ITV is too low. The ITV is contoured from the MIP or from the phases, then assigned a soft-tissue density on the data set used for dose. The MIP itself is the wrong data set for dose, because it paints tumor attenuation along the entire path of the motion.

A clipped body contour (truncation or a tight window) assigns air to tissue that was actually present. That removes scatter and can change a monitor unit. The external contour has to include the skin.

**Formulas**

HU = 1000 (μ − μ_water) / μ_water

μ / μ_water = 1 + HU/1000

- μ: linear attenuation coefficient of the voxel at the CT beam energy
- μ_water: the same coefficient for water
- HU: Hounsfield unit

Air: HU = −1000. Water: HU = 0.

**Worked example**

Given: a voxel has μ = 0.30 μ_water. A second voxel is water. A third has μ = 1.05 μ_water. Find all three HU values. Then interpret a lung voxel stored as HU = −700.

Formula: HU = 1000 (μ/μ_water − 1)

Substitution:

First: HU = 1000 (0.30 − 1) = 1000 × (−0.70) = −700

Second: HU = 1000 (1 − 1) = 0

Third: HU = 1000 (1.05 − 1) = 50

From the stored number −700: μ/μ_water = 1 + (−700)/1000 = 0.30.

Meaning: the −700 voxel attenuates a CT photon 30% as much as water. That is a reasonable lung value to hand to an equivalent-depth estimate (5 cm of this lung counts as 1.5 cm of water). It is still an approximation to electron density. Bone does not get this one-line treatment; bone goes through the high-density limb of the calibration curve. The water voxel is 0 even though its absolute μ is not zero. The +50 voxel is slightly above water, in the muscle range.

Usual wrong turn: HU = 1000 × (μ/μ_water), with no subtraction. Water becomes 1000 and air becomes 0. Those are the wrong anchors, and they are a common pair of distractors. Another miss: using −700 as a density of 700, or as a relative density of −0.7. Relative attenuation is 0.30, which is 1 + HU/1000, and density is not negative.

**Traps**

Air answered as 0 or as −1024. Water answered as 1000 or as 1. Contrast left at its raw HU for a 6 MV calculation. One linear HU-to-density line forced through bone. Dose calculated on the MIP because the ITV was drawn there. A kV change ignored for a bone override.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.9. AAPM TG-66 for CT simulation practice.

## HU Units Mini-Quiz

This quiz checks the formula, the anchors (air −1000, water 0), the rearrangement μ/μ_water = 1 + HU/1000, and the reasons for overriding contrast, metal artifact, and a motion-averaged ITV. The traps are water = 1000, air = 0, air = −1024 as a physical HU, HU used as electron density in bone, and a MIP used as the dose-calculation CT.

## HU Artifacts, Bit Depth and Modality Volume Bias

**Objectives:** I.9

**What the exam expects**

You recognise the artifacts that shift Hounsfield numbers without any change in the patient, you know which scanner component or physics effect each one comes from, and you can state the stored HU range, the common tissue anchors, and the systematic size difference between a prostate drawn on CT and one drawn on MRI or ultrasound.

**Core facts**

Beam hardening is the rise in mean energy of a polychromatic x-ray beam as its soft photons are removed. Rays through the thick center of a large patient or a dense skull emerge harder and are attenuated less per centimeter than the reconstruction assumes, so the center is reconstructed with falsely low HU. The result is cupping: a radial HU profile that dips in the middle of a uniform phantom. Between two dense objects, such as the petrous bones or two hip prostheses, the same physics produces dark bands and streaks. Scanners reduce it with a bowtie filter, added filtration and a software correction calibrated for water; it is the main reason a uniform water phantom is checked daily (the TG-66 tolerance is 0 ± 5 HU at the center and uniformity within a few HU across the field) and the reason a density curve commissioned at one kV should not be used at another. In the planning system, a cupped HU map assigns slightly low density to the center of a large pelvis; the dose error is small for photons but the HU shift is real.

A ring artifact is a circle or set of concentric circles centered on the axis of rotation. It is a detector problem, not a patient problem: in third-generation geometry one detector element reads consistently high or low on every projection, and back-projection paints that error as a ring. The fix is detector recalibration (an air calibration) or service, not a different reconstruction kernel. A ring that passes through a target changes the HU along it and can bias an autocontour or a density override. Fourth-generation scanners with a stationary detector ring did not show rings, which is the exam's contrast between the two designs.

Noise appears as random HU scatter and is set by photon statistics: it falls as the square root of mAs and rises as slices get thinner or the kernel gets sharper. Photon starvation through the shoulders or a hip prosthesis produces directional streaks because a few projections carry almost no signal; iterative reconstruction suppresses this better than filtered back-projection, which is one reason it lowers the usable dose. Partial-volume averaging and motion are patient-side causes of HU error covered earlier. Metal streaks are the extreme case: saturation, beam hardening and scatter together, repaired by a metal-artifact-reduction algorithm and, for dose, by an override.

Tissue anchors beyond air and water, as single values a stem may quote: fat about −100, water 0, cerebrospinal fluid near 0 to +15, muscle and most solid organs +40 to +60, clotted blood +55 to +75, thyroid about +80 because of its iodine content, trabecular bone a few hundred, cortical bone +1,000 and above, and metal at the scale ceiling. The commonly stored range is −1,024 to +3,071 HU, the 4,096 levels of a 12-bit word; an extended scale to about +30,000 exists on some scanners for metal. These are 12 bits of attenuation displayed through an 8-bit window of 256 grays, which is why a window and level are always applied.

CT overestimates the prostate volume by roughly 30 percent relative to MRI, and by a similar margin relative to transrectal ultrasound, because the capsule, the apex, the neurovascular bundles and the seminal vesicles are not separable from the gland on CT and observers draw generously. The CT prostate is therefore larger and more variable between observers; MRI-defined contours are smaller, and a CT-only target carries a systematic error that a margin cannot repair. The exam uses this fact in two places: as the reason T2 MRI is fused for prostate and brain targets (the CT shows bone and the planning density; the MRI shows the gland, the apex, the tumor and the edema), and as a caution that a volume quoted from CT is not interchangeable with one quoted from ultrasound in a brachytherapy seed order. The fusion is rigid for the brain and for the prostate when the bladder and rectum are matched, and the dose calculation stays on the CT.

**Formulas**

Noise is proportional to 1 over the square root of mAs: quadrupling mAs halves the noise.

Number of gray levels = 2 to the power of the bit depth: 8 bits = 256, 9 bits = 512, 12 bits = 4,096.

**Worked example**

Given: a prostate measures 45 cm³ on the planning CT. The published CT-to-MRI overestimate is about 30 percent. Estimate the MRI volume, and the noise change if the scan mAs were doubled.

MRI volume ≈ 45 / 1.30 = 34.6 cm³, about 35 cm³. A 45 cm³ CT gland is a 35 cm³ MRI gland, not a 45 cm³ gland with a 30 percent margin.

Noise: doubling the mAs multiplies the noise by 1 over the square root of 2, which is 0.71, a 29 percent reduction; halving the noise needs four times the mAs.

Meaning: the CT volume is biased, not just noisy, so averaging more CT observers does not recover the MRI value; and dose buys noise reduction only as a square root.

Usual wrong turn: subtracting 30 percent of the CT value (31.5 cm³), which treats the overestimate as a fraction of the CT volume instead of the MRI volume; the two answers differ by about 3 cm³ and both appear as options. Assuming noise halves when dose doubles.

**Traps**

Cupping blamed on the detector and rings blamed on the patient. Beam hardening described as making the center of the image too bright. Ring artifact repaired by a smoother kernel. Thyroid given a muscle HU. A 12-bit scale read as 1,024 levels. A prostate drawn on CT treated as the same volume as one drawn on MRI or TRUS.

**Sources**

Bushberg, *The Essential Physics of Medical Imaging*, CT artifacts chapter. AAPM TG-66 (CT simulator QA tolerances). Khan and Gibbons, *The Physics of Radiation Therapy*. Roach et al. and Rasch et al. on CT versus MRI prostate volume. Public blueprint I.9.
