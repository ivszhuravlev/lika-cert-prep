# Module 16 — Treatment Simulations, TPS Localization of a Patient

Original items on shifts, volume definition, and what a simulation data set has to contain.

## Where do shifts come from?

### Q1
Stem: Tattoos are placed on a stable reference at simulation. The physician later places the isocenter on the target. The shifts are:
A. The three-axis difference between the reference marks and the treatment isocenter
B. Always zero, because the isocenter must sit on the tattoos
C. The PDD at the isocenter
D. The daily change in the source half-life
Answer: A
Objective: II.7
Why: The reference is an external, reproducible origin. The isocenter is a planning decision. The difference, with a stated sign convention and patient orientation, is what the therapists move. Zero shifts occur only when the isocenter is left on the marks. PDD and half-life are not shifts.

### Q2
Stem: For this head-first supine plan, +X is patient left, +Y is posterior, and +Z is superior. The reference marks are at the origin. The isocenter is 1.5 cm to the patient right, 2.0 cm anterior, and 3.0 cm superior to the marks. The shifts from the marks to the isocenter are:
A. X = −1.5 cm, Y = −2.0 cm, Z = +3.0 cm
B. X = +1.5 cm, Y = +2.0 cm, Z = +3.0 cm
C. X = −1.5 cm, Y = −2.0 cm, Z = −3.0 cm
D. X = +1.5 cm, Y = −2.0 cm, Z = −3.0 cm
Answer: A
Objective: II.7
Why: Patient right is the opposite of +X, so X = −1.5 cm. Anterior is the opposite of +Y (posterior), so Y = −2.0 cm. Superior is +Z, so Z = +3.0 cm. Option B uses the words as if they were already the positive axes. Option C also flips Z. Option D flips both X and Z relative to the correct signs.

### Q3
Stem: The isocenter is placed exactly on the reference BBs and no additional offset is introduced. The shifts sent to the treatment machine should be:
A. Zero in all three axes
B. 1 cm in each axis, as a default
C. The field size
D. The SSD
Answer: A
Objective: II.7
Why: If the treatment isocenter and the marks are the same point, there is nothing to move. A default 1 cm shift, the field size, or the SSD would move or mislabel a setup that was intentionally centered on the marks.

### Q4
Stem: A plan reports a 4 cm superior shift, but the isocenter was never moved off the tattoos. The inconsistency means:
A. The shift sheet and the isocenter placement disagree, and one of them is wrong
B. A 4 cm shift is required whenever tattoos exist
C. Superior shifts are always 4 cm for head-first supine patients
D. The shift is the magnification
Answer: A
Objective: II.7
Why: Shifts are the measured offset. If the isocenter is on the marks, a nonzero shift contradicts the plan. There is no universal 4 cm superior shift and shifts are not a magnification factor.

### Q5
Stem: The same numeric shifts are copied from a head-first supine plan onto a feet-first supine treatment without reversing the superior-inferior direction. The isocenter will be:
A. Displaced toward the wrong end of the patient
B. Correct, because supine shifts are independent of head-foot orientation
C. Correct if the energy is changed to FFF
D. Improved by the mean-life factor 1.44
Answer: A
Objective: II.7
Why: Feet-first reverses which way “superior” points relative to the couch and the imager if the shift convention is not rewritten. Copying the head-first signs sends the isocenter the wrong way along the patient. Energy and the mean-life factor do not repair a direction error.

## Localization of OAR and Target Volumes

### Q1
Stem: Gross tumor seen on the planning images is the:
A. GTV
B. CTV
C. PTV
D. PRV
Answer: A
Objective: III.11
Why: The GTV is palpable or visible disease. The CTV adds the microscopic extent that is not seen. The PTV is a geometric margin for setup and related uncertainty. The PRV is a margin on an organ at risk, not on the tumor.

### Q2
Stem: Microscopic disease around a visible tumor is included by expanding the GTV to a:
A. CTV
B. PTV, with no CTV in between
C. PRV
D. Skin flash only
Answer: A
Objective: III.11
Why: ICRU puts subclinical spread in the CTV. The PTV is not a substitute for that clinical judgment. A PRV protects an organ. Skin flash is a field-edge technique, not the definition of microscopic extent.

### Q3
Stem: A lung CTV moves 8 mm with respiration and the setup margin is 5 mm. A volume that already contains the respiratory motion, before the setup margin is added, is the:
A. ITV
B. GTV
C. PRV of the cord
D. Treated volume
Answer: A
Objective: III.11
Why: The ITV is the CTV plus the internal margin. The PTV then adds the setup margin. The GTV has neither margin. A cord PRV is an organ-at-risk expansion. The treated volume is the tissue that actually receives a dose considered therapeutic, which is a result of the plan, not the motion contour.

### Q4
Stem: A planning organ-at-risk volume (PRV) is:
A. The OAR expanded by a margin so that setup uncertainty is less likely to put the organ into the high dose
B. Another name for the PTV
C. The GTV of a benign organ
D. The 50% isodose line
Answer: A
Objective: III.11
Why: A PRV is the OAR plus a margin, used when a small setup error would move a serial organ such as the cord into the beam. It is not the target PTV, not a GTV, and not an isodose.

### Q5
Stem: A whole-lung mean-dose constraint is being evaluated. The lungs should be contoured:
A. As the whole lungs specified by the protocol, not only the slices inside the beam aperture
B. Only on the slices where the beam is on, because mean dose ignores the unirradiated volume
C. As the PTV plus 5 cm
D. Only where the HU is exactly 0
Answer: A
Objective: II.7
Why: Mean dose and volume-dose metrics such as V20 depend on the denominator. Leaving out the unirradiated lung makes the mean and the percent volume look worse or simply wrong relative to the protocol. The lungs are not the PTV, and lung HU is far below 0.

### Q6
Stem: The PTV is expanded, and then a second PTV margin is added “to be safe.” The second expansion:
A. Double-counts geometric uncertainty and can push dose into organs that the original margin already accounted for
B. Is required by ICRU for every site
C. Converts the PTV into a GTV
D. Removes the need for image guidance
Answer: A
Objective: III.11
Why: The PTV margin is already the geometric allowance. Expanding it again is a new clinical decision, not a hidden ICRU requirement, and it often raises organ dose. It does not turn the volume back into a GTV and it does not replace IGRT.

## Localization Mini-Quiz

### Q1
Stem: A simulation scan for a non-coplanar brain plan clips the vertex. The failure is:
A. An incomplete data set. Beams that enter through the vertex have no external contour or tissue in the calculation.
B. Acceptable, because non-coplanar beams do not need an entrance path
C. Acceptable if the clips are assigned HU of +1000
D. A wedge-angle error
Answer: A
Objective: II.4
Why: Full treatment windows mean the scan covers every beam entrance and the organs the plan must score. Missing vertex tissue is calculated as air. Painting it as bone is not a reconstruction. Wedge angle is unrelated.

### Q2
Stem: Body-contour clipping, a 5 mm slice on a small stereotactic target, and a bladder protocol that does not match treatment are all:
A. Simulation-parameter problems that should be fixed before planning
B. Optimizer settings
C. Brachytherapy survey items
D. Corrected by multiplying the shifts by 1.44
Answer: A
Objective: II.4
Why: Prep, complete anatomy, appropriate slice thickness, and a reproducible physiologic state are simulation requirements on the localization blueprint. They are not solved in the optimizer, by a source survey, or by the mean-life factor.

### Q3
Stem: DRRs are generated from the planning CT at the beam angles. They are used to:
A. Compare the planned aperture and anatomy with portal or kV images at treatment
B. Replace the axial CT for the dose calculation
C. Set the Hounsfield value of water to −1000
D. Measure the source half-life
Answer: A
Objective: II.7
Why: A DRR is a projection of the CT along the beam, so the field shape and bony anatomy can be checked against the treatment image. Dose is still calculated on the axial density grid. Water is 0 HU. A DRR does not measure activity.

### Q4
Stem: In a head-first supine coordinate system where +X is patient left, a shift of X = +2.0 cm from the marks moves the isocenter:
A. 2.0 cm toward the patient’s left
B. 2.0 cm toward the patient’s right
C. 2.0 cm anterior
D. 2.0 cm superior
Answer: A
Objective: II.7
Why: The stem defines +X as patient left, so a positive X shift is to the patient’s left. Patient right would be −2.0 cm. Anterior and superior are the other two axes and are not implied by an X shift.

### Q5
Stem: A reference mark is on the patient’s right. The isocenter is 1.0 cm to the patient’s left of that mark. Using +X = patient left, the X shift from the mark to the isocenter is:
A. +1.0 cm
B. −1.0 cm
C. +1.0 cm only if the patient is prone
D. 0 cm, because left and right cancel
Answer: A
Objective: II.7
Why: From the mark, the isocenter is toward +X by 1.0 cm, so the shift is +1.0 cm. −1.0 cm would move farther to the patient’s right. The sign is defined by the stated axis, not by an unstated prone flip, and the two directions do not cancel.

### Q6
Stem: Localization inside the planning system includes placing the isocenter, creating the shifts, and checking laterality. Which additional simulation defect still makes that localization unusable?
A. The external contour is cut off, so every beam path through the missing tissue is wrong
B. The isocenter coordinates have been written down
C. A DRR was created
D. The patient orientation was confirmed against the header and the photo
Answer: A
Objective: II.4
Why: An isocenter and a shift sheet assume a true body surface. A clipped contour assigns air to tissue and the SSD and the depth dose move. Writing the coordinates, building a DRR, and confirming orientation are the successful parts of localization, not the defect.
