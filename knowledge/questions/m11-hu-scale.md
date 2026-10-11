# Module 11 — HU Unit Conversion to CT Density Table (TPS)

Original items. HU = 1000 × (μ − μwater) / μwater, with water at 0 and air at −1000.

## HU Scale

### Q1
Stem: A voxel has a linear attenuation coefficient 1.05 times that of water. Its Hounsfield number is:
A. 50
B. 1.05
C. 1050
D. 5
Answer: A
Objective: I.9
Why: HU = 1000 × (1.05 − 1) / 1 = 1000 × 0.05 = 50. 1.05 reports the ratio and never scales it. 1050 adds the 1000 to the ratio instead of multiplying the difference. 5 forgets a factor of ten on the 0.05.

### Q2
Stem: Air is assigned a Hounsfield number of approximately:
A. −1000
B. 0
C. +1000
D. +1000 × μwater
Answer: A
Objective: I.9
Why: For μ ≈ 0, HU = 1000 × (0 − μwater) / μwater = −1000. Zero is water. +1000 is the sign error that swaps air with the old nominal value for dense bone, or that computes (μwater − 0) instead of (0 − μwater).

### Q3
Stem: A region has μ = 0.20 × μwater. The HU is:
A. −800
B. +800
C. −200
D. +200
Answer: A
Objective: I.9
Why: HU = 1000 × (0.20 − 1) = 1000 × (−0.80) = −800. +800 flips the sign. −200 and +200 treat the 0.20 ratio as if the formula were 1000 × μ/μwater without subtracting water, or 1000 × (1 − 0.80) with the wrong remainder.

### Q4
Stem: Cortical bone with μ = 2.0 × μwater has HU:
A. +1000
B. +2
C. −1000
D. 0
Answer: A
Objective: I.9
Why: HU = 1000 × (2.0 − 1) = +1000. Real cortical bone is often higher than +1000, and this stem is the factor-of-two case. +2 drops the 1000. −1000 is air. 0 is water.

### Q5
Stem: Typical planning-CT values place water, fat, and aerated lung in which order from highest HU to lowest?
A. Water near 0, fat near −80 to −100, lung near −700 to −800
B. Lung near +1000, water near 0, fat near −1000
C. Fat near +1000, water near −1000, lung near 0
D. All three are 0 because the scanner is calibrated
Answer: A
Objective: I.9
Why: Water is the zero of the scale. Fat is slightly below water. Aerated lung is far below water and well above the −1000 of pure air. Lung is not the brightest of the three, and calibration does not force every tissue to 0.

### Q6
Stem: The planning system does not use the raw HU as a depth. It uses a CT-density table that converts HU to:
A. Relative electron density or physical density
B. Activity in mCi
C. Monitor units directly
D. SUV
Answer: A
Objective: I.9
Why: Megavoltage dose depends on electron density (Compton) and, for some algorithms and for protons, on composition. The commissioned curve turns HU into that density. It does not output activity, MU, or SUV.

## HU Units Mini-Quiz

### Q1
Stem: Iodinated contrast is in the bladder on the planning CT and will not be in the bladder at treatment. If the high HU is left unchanged, a megavoltage calculation will:
A. Treat the contrast like high-density tissue and attenuate the beam too much
B. Treat the contrast like air and under-attenuate the beam
C. Ignore HU by design, so contrast never matters
D. Convert the contrast into a proton Bragg peak
Answer: A
Objective: I.9
Why: Iodine raises the kV attenuation a great deal, so the HU looks like bone or higher. At MV energies that iodine is not a large extra attenuator. Leaving the high density in the plan over-attenuates photon beams through the bladder. The usual override is water or soft-tissue density, not air.

### Q2
Stem: A scanner is recalibrated and the same phantom insert now reads 40 HU higher across soft tissue. The safe action before the next patient calculation is:
A. Rebuild or verify the CT-density curve for that scanner. Do not keep using another scanner’s curve.
B. Divide every MU by 40.
C. Ignore it, because HU is only a display window.
D. Add 40 to the prescription dose in gray.
Answer: A
Objective: I.9
Why: The dose engine trusts the HU-to-density table that was measured for that scanner and technique. A systematic HU shift assigns the wrong density. It is not corrected by dividing MU by 40 or by adding 40 Gy, and windowing is not the stored pixel value.

### Q3
Stem: A titanium hip saturates the CT scale and causes streaks. A density override through the metal and through the spoiled soft tissue is used so that:
A. The calculation does not treat streak artifacts as real bone or real air
B. The metal can be assigned a density of zero, which is always correct for MV beams
C. The HU of titanium becomes −1000 by definition
D. Contrast and metal can share one override of air
Answer: A
Objective: I.9
Why: Artifact HU values are not the patient. Metal itself is dense and should not be painted as air or as water. Nearby tissue that the streaks painted as air or bone needs a tissue override. Iodine contrast and titanium are different materials and do not share one air override.

### Q4
Stem: A lung voxel reads −750 HU. A homogeneous-water calculation assigns that voxel a relative density of 1.0. Relative to a heterogeneity-corrected plan, the water calculation:
A. Over-attenuates the lung and underestimates dose downstream of the lung
B. Under-attenuates the lung and overestimates downstream dose
C. Is exact, because MV beams do not see density
D. Changes the HU from −750 to 0 in the DICOM file
Answer: A
Objective: I.9
Why: −750 HU is a low density (on the order of 0.25 relative to water, depending on the curve). Forcing it to 1.0 removes too many photons in the calculation, so the predicted dose beyond the lung is too low. The DICOM HU are not rewritten by the choice of algorithm. MV beams do respond to electron density.

### Q5
Stem: A proton plan needs relative stopping power, not only the photon electron-density curve. Using the photon CT-density table unchanged for protons is:
A. A calibration error, because stopping power and electron density are related but are not the same commissioned curve
B. Exact, because HU was invented for protons
C. Acceptable if the HU of water is set to 1000
D. Required, because protons do not lose energy in tissue
Answer: A
Objective: I.9
Why: Photon algorithms need electron density (and composition for the more advanced ones). Protons need relative stopping power. Both curves start from HU, but they are commissioned separately. Water is 0 HU, not 1000, and protons do lose energy, which is the Bragg peak.

### Q30
Stem: Air, with μ taken as 0, water, and a material with μ = 1.80 μwater have Hounsfield numbers:
A. 0, +1000, and −1000
B. −1000, 0, and +800
C. −1024, +1, and +1800
D. +1000, 0, and −800
Answer: B
Objective: I.9
Why: Answer B. HU = 1000 × (μ/μwater − 1). Air gives 1000 × (0 − 1) = −1000. Water gives 0. The third voxel gives 1000 × (1.80 − 1) = +800. −1024 is a storage floor, not the definition of air. +1800 is 1000 × 1.80 with water not subtracted. The sign pattern that puts +1000 on air swaps air with the factor-of-two bone case.

### Q31
Stem: A voxel is stored as −250 HU. Its kV linear-attenuation ratio to water, μ/μwater, is:
A. −0.250
B. 1.250
C. 0.750
D. 250
Answer: C
Objective: I.9
Why: Answer C. μ/μwater = 1 + HU/1000 = 1 + (−250)/1000 = 0.750. Air, at −1000 HU, has ratio 0. Water, at 0 HU, has ratio 1. A factor-of-two bone case, μ = 2 μwater, is +1000 HU and ratio 2. This voxel is none of those anchors. 1.250 is the ratio for +250 HU. −0.250 is HU/1000 with the water term omitted. 250 drops the formula.

### Q32
Stem: Cortical bone reads +1400 HU. Which statement is right for a megavoltage photon calculation?
A. Use 2.40 as the electron density, because 1 + 1400/1000 is the commissioned density of bone
B. Use 1400 as the mass density in g/cm³
C. Use 0, because bone and water share the water anchor
D. The kV attenuation ratio is 1 + 1400/1000 = 2.40, but the electron density has to come from the high-density limb of the CT-density curve. Photoelectric absorption still inflates bone at CT energy
Answer: D
Objective: I.9
Why: Answer D. 1 + 1400/1000 = 2.40 is the kV linear-attenuation ratio to water, whose HU is 0. Air is −1000. That 2.40 is not automatically the relative electron density. Compton scatter dominates at treatment energy, so bone goes through the commissioned curve rather than through HU/1000. Using 1400 g/cm³ reads the Hounsfield number as a density, and 0 is the water anchor.

### Q33
Stem: A voxel has μ = 0.40 μwater. Its Hounsfield number, set beside air, water, and dense bone, is:
A. +600, on the same side of the scale as cortical bone
B. −600, between air at −1000 and water at 0, and far from bone near +1000 and above
C. −1000, because every reading below water is defined as air
D. 0, because the scanner stores every tissue as water
Answer: B
Objective: I.9
Why: Answer B. HU = 1000 × (0.40 − 1) = 1000 × (−0.60) = −600. The attenuation ratio is 0.40, which is 1 + (−600)/1000. Air is −1000, water is 0, and μ = 2 μwater is +1000. −600 is a low-density lung-range value. +600 flips the sign and moves the voxel onto the bone side of water.

### Q34
Stem: List air, water, and a material with μ = 2.20 μwater, in that order:
A. 0, −1000, and +2200
B. −1024, +1000, and +2.20
C. −1000, 0, and +1200
D. +1200, 0, and −1000
Answer: C
Objective: I.9
Why: Answer C. Air is −1000 and water is 0 by definition. HU = 1000 × (2.20 − 1) = +1200, which is the dense-bone side of the scale. +2200 is 1000 × 2.20 with water not subtracted. −1024 is a digital floor sometimes stored near air, not the physical HU of air. +2.20 drops the factor of 1000. +1000 in that list is what water becomes if the formula never subtracts 1, not this μ = 2.20 voxel.

### Q35
Stem: A 2.50 cm streak through soft tissue is stored as −1000 HU. For the hand estimate, take air as relative density 0 and soft tissue as relative density 1.0. If the streak is left as air instead of overridden to soft tissue, the water-equivalent thickness of that streak is:
A. 2.50 cm either way, because −1000 HU is cortical bone
B. 2.50 cm either way, because −1000 HU is water
C. 5.00 cm when the air value is kept, because a negative HU doubles the path
D. 0 cm while it is treated as air, versus 2.50 cm after an override to density 1.0. Keeping the air value under-attenuates, so dose beyond the streak is overestimated
Answer: D
Objective: I.9
Why: Answer D. −1000 HU is air. Water is 0 HU. Dense bone is far above water, near +1000 and higher. Equivalent path is thickness × relative density, so 2.50 × 0 = 0 cm and 2.50 × 1.0 = 2.50 cm. The photon calculation that keeps the air value removes attenuation the tissue would have produced, and the predicted dose downstream is too high. 5.00 cm doubles the thickness. Calling −1000 HU water or bone uses the wrong anchor.
