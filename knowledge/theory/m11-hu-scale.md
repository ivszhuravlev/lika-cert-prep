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
