# Module 38. Deformable dose accumulations

Original notes for MDCB CMD prep. Objectives IV.5 and II.5.

## Deformable Registration and Dose Accumulation

**Objectives:** IV.5, II.5

**What the exam expects:** Dose grids that belong to two different anatomies are not added voxel by voxel in the planning-CT coordinate system. A deformable image registration (DIR) has to carry each dose element to the same tissue. That registration is weak where tissue slides, and it does not conserve energy if the patient has gained or lost mass. Courses with different fraction sizes are converted to EQD2 before a biological sum. A physical sum of gray is a different question from a biological sum.

Four rules:

1. **No DIR, no accumulation.** Adding the dose cube from the planning CT to the dose cube from a later CT, index by index, deposits dose in whatever voxel now occupies that coordinate. If the tumor or the cord moved, the sum is in the wrong tissue.
2. **Sliding interfaces.** Lung against chest wall, and bowel loops against each other, slide. Most DIR algorithms apply a smooth transform and smear that slip plane. Dose near the chest wall can be assigned to lung or to chest wall incorrectly. A pretty deformed contour is not proof the dose followed the right voxels.
3. **Mass change breaks energy conservation.** Dose is energy per mass. Weight loss removes tissue. Warping the old dose onto a smaller body and adding does not conserve energy: the same energy cannot be squeezed into less mass and still mean the same gray in a simple sum. Large weight loss is a reason to replan, not only to deform.
4. **Fraction size.** A gray from a 3 Gy fraction is not biologically a gray from a 2 Gy fraction. Convert each course with the organ’s \(\alpha/\beta\), then add EQD2. Do not add EQD2 to raw physical dose.

**Formula**

\[
\mathrm{EQD2} = D \times \frac{d_f + \alpha/\beta}{2 + \alpha/\beta}
\]

- \(D\): total physical dose of that course (Gy)
- \(d_f\): dose per fraction of that course (Gy)
- \(\alpha/\beta\): the value stated for the organ (Gy)
- EQD2: the total dose in 2 Gy fractions that matches the biological effect under the linear-quadratic model

The prior course and the new course each get their own \(d_f\). A course that was already given at 2 Gy per fraction has EQD2 equal to its physical dose, for any \(\alpha/\beta\).

### Worked example

**Given.** An organ with \(\alpha/\beta = 3\) Gy received 40 Gy in 2 Gy fractions last year. The new plan contributes 30 Gy in 10 fractions of 3 Gy. The two dose grids have been deformable-registered onto one anatomy. The question is the biological sum.

**Substitute.** The old course is already in 2 Gy fractions, so its EQD2 is 40 Gy.

\[
\mathrm{EQD2}_{\text{new}} = 30 \times \frac{3+3}{2+3} = 30 \times \frac{6}{5} = 30 \times 1.2
\]

**Arithmetic.** \(30 \times 1.2 = 36\) Gy EQD2. Biological sum \(= 40 + 36 = 76\) Gy EQD2. Physical sum \(= 40 + 30 = 70\) Gy.

**Check.** \(6/5 = 1.2\), and \(30 \times 1.2 = 36\). \(76 - 70 = 6\) Gy. The entire 6 Gy gap is the new course: 30 Gy physical versus 36 Gy EQD2. The old course contributes 0 to that gap because \(d_f = 2\).

**Result means.** After a trustworthy DIR, the biological accumulation is 76 Gy EQD2, not 70 Gy. Quoting 70 Gy understates the effect for this \(\alpha/\beta\). The DIR step is still required before either number is assigned to a structure. If the second dataset is a smaller patient after weight loss, neither sum repairs the broken mass.

**Wrong turns**

- Adding 70 Gy because “a gray is a gray.” That is the physical sum, and it is the distractor when fraction sizes differ.
- Adding 36 Gy EQD2 to 40 Gy and also multiplying the old course by 1.2 again (double conversion).
- Using \(\alpha/\beta = 10\) Gy when the stem said 3. With \(\alpha/\beta = 10\), the new course would be \(30 \times (3+10)/(2+10) = 30 \times 13/12 = 32.5\) Gy EQD2, and the sum would be 72.5 Gy. The stem’s \(\alpha/\beta\) is part of the given data.
- Trusting DIR at a sliding lung–chest wall interface because the algorithm ran without an error message.
- Treating half-life or mean life as the accumulation method. Those belong to radioactive sources.

**Traps.** Ask three questions in order. Are the anatomies the same tissue via a DIR? Did the mass change? Are the fraction sizes both 2 Gy? Stop at the first “no” and do the step that question requires.

**Sources.** AAPM TG-132 for image registration, including deformable registration limits. The linear-quadratic EQD2 relation is the standard radiobiology conversion used with QUANTEC-style comparisons (module 43).
