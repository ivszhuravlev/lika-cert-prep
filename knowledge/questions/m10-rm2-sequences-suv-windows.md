# Module 10. Imaging Modalities

Original items. MRI in pregnancy, spin echo versus gradient echo versus inversion recovery, the three parts of mpMRI, SUV and voxel arithmetic, lung window settings, and the TG-66 spatial tolerance.

## Pulse Sequences, SUV Arithmetic, Voxels and Display Windows

### Q1
Stem: A pregnant patient needs a non-urgent MRI to help define a planning volume. The conventional approach is to:
A. Proceed at any gestational age with gadolinium, because MRI is non-ionizing
B. Defer elective MRI until after the first trimester and avoid gadolinium contrast throughout pregnancy
C. Substitute a non-contrast CT, because CT dose to the fetus is negligible
D. Refuse MRI in all trimesters because of radiofrequency heating
Answer: B
Objective: II.4
Why: No fetal harm from clinical-strength MRI has been shown, but the accepted convention is to avoid elective studies during organogenesis in the first trimester and to withhold gadolinium, which crosses the placenta and persists in amniotic fluid. Medically necessary MRI is not refused at any stage. CT delivers ionizing dose to the fetus and is not a safer substitute. Radiofrequency heating is managed by SAR limits and is not a reason for blanket refusal.

### Q2
Stem: Which sequence family uses a 180-degree refocusing pulse, which makes it relatively insensitive to susceptibility artifacts near metal and air?
A. Spin echo
B. Gradient echo
C. Echo-planar diffusion imaging
D. Dynamic contrast-enhanced imaging
Answer: A
Objective: II.4
Why: The 180-degree pulse in spin echo rephases spins dephased by static field inhomogeneity, so the signal decays with T2 rather than T2* and susceptibility effects are largely cancelled. Gradient echo refocuses with a gradient reversal, decays with T2*, and is the sequence most degraded near prostheses. Echo-planar diffusion imaging is a gradient-echo-type readout and is highly susceptibility sensitive. DCE imaging is a fast gradient-echo T1 series.

### Q3
Stem: In an inversion recovery sequence the inversion time is set to about 150 ms. The effect is to:
A. Null free water, as in FLAIR
B. Shorten the scan by acquiring multiple echoes per excitation
C. Produce proton-density contrast by removing both T1 and T2 effects
D. Null fat, as in STIR, making marrow edema and bone metastases conspicuous
Answer: D
Objective: II.4
Why: Inversion recovery nulls whichever tissue has zero longitudinal magnetization at the excitation; fat recovers quickly, so a short inversion time near 150 ms suppresses it (STIR). Free water needs a long inversion time of about 2,000 to 2,500 ms to be nulled (FLAIR). Proton-density contrast comes from long TR and short TE in a spin echo. Multiple echoes per excitation is the fast or turbo spin echo trick, not an inversion effect.

### Q4
Stem: Multiparametric prostate MRI combines which three components?
A. T1-weighted, CT fusion, and transrectal ultrasound
B. T2-weighted, diffusion-weighted with ADC map, and dynamic contrast-enhanced imaging
C. STIR, FLAIR, and MR spectroscopy
D. T2-weighted, PET-CT, and gradient echo
Answer: B
Objective: II.4
Why: mpMRI as used for PI-RADS scoring is T2-weighted imaging for zonal anatomy and the capsule, DWI with an ADC map for cellularity, and DCE T1 imaging for early enhancement; together they define the dominant lesion and show extracapsular and seminal vesicle extension. CT, ultrasound and PET are separate modalities and not part of the MRI protocol. STIR, FLAIR and spectroscopy are not the standard three.

### Q5
Stem: A patient weighing 74 kg receives 370 MBq of FDG. At scan time a lesion measures 40 kBq per mL. Ignoring decay, the lesion SUV is:
A. 0.125
B. 2.5
C. 8
D. 29.6
Answer: C
Objective: II.4
Why: SUV = tissue concentration ÷ (injected activity ÷ body mass) = 40 kBq per mL ÷ (370,000 kBq ÷ 74,000 g) = 40 ÷ 5 = 8. Check: 5 kBq per g × 8 = 40 kBq per mL. 0.125 inverts the ratio. 2.5 is the common threshold value, not this calculation. 29.6 multiplies 40 by 0.74 as though the mass were in the numerator.

### Q6
Stem: A CT data set has 2 mm by 2 mm pixels and a 5 mm slice thickness. The voxel volume is:
A. 10 mm³
B. 20 mm³
C. 9 mm³
D. 40 mm³
Answer: B
Objective: II.1
Why: Voxel volume = pixel area × slice thickness = 2 × 2 × 5 = 20 mm³. Check: 4 mm² × 5 mm = 20 mm³. 10 mm³ multiplies one pixel dimension by the slice without squaring. 9 mm³ adds the three dimensions. 40 mm³ doubles the correct result, as if the slice thickness were 10 mm.

### Q7
Stem: A thoracic CT is displayed at window level −500 HU and window width 1,500 HU. Which statement is correct?
A. The display runs from about −1,250 to +250 HU and is a lung window that shows parenchyma and vessels
B. The display runs from −500 to +1,000 HU and is a bone window
C. The display runs from −2,000 to +1,000 HU and is a soft-tissue window
D. The level sets the span of gray values and the width sets the mid-gray value
Answer: A
Objective: II.1
Why: The display spans level ± half the width, so −500 − 750 = −1,250 to −500 + 750 = +250 HU, which places aerated lung from −950 to −600 HU in the useful gray range; this is the standard lung window. A bone window sits near level +400 to +500. A soft-tissue window is about level 40 with a width near 400. Option D swaps the definitions of level and width.
