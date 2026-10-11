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

## Scan length, field of view, and the setup origin

### Q20
Stem: A planning CT is reconstructed with a field of view that cuts off both lateral skin surfaces. The scan length still covers the superior and inferior borders of the target. What is wrong with the data set?
A. Nothing is wrong, because scan length and field of view are one setting
B. The missing lateral tissue is absent from the external contour, so a beam that crosses that side is calculated through air
C. The field of view reassigns water inside the patient from 0 HU to −1000 HU
D. Cutting off the lateral skin shortens only the superior-inferior scan and leaves the axial contour intact
Answer: B
Objective: II.4
Why: Field of view is the in-plane reconstruction diameter. Tissue outside it is absent, and the planning system treats the gap as air, so SSD, depth, and scatter move. Scan length is the superior-inferior coverage, and that coverage was adequate here. Water stays 0 HU where it was actually scanned. The clipped skin is an axial-contour error.

### Q21
Stem: A pelvic planning CT includes the prostate and stops at mid-bladder. Small bowel superior to the bladder is outside the data set. The axial field of view includes the skin. Which requirement failed?
A. Scan length: anatomy and beam paths superior to the last slice are missing from the calculation
B. Field of view: the skin was reconstructed, so the axial contour is the failed part
C. Slice thickness, because a short scan means a thick slice
D. Couch indexing, which creates the missing superior slices
Answer: A
Objective: II.4
Why: Scan length is how far the slices run superior and inferior. A bladder constraint, and any beam that exits through the top of the bladder, needs those slices. The skin is inside the field of view, so this is not a lateral clip. Slice thickness is the spacing of the slices that exist. An index notch does not restore missing anatomy.

### Q22
Stem: A 1 cm lung nodule is to be planned for stereotactic treatment. The only CT uses 5 mm slices through the nodule. What problem does that slice thickness create?
A. None; slice thickness affects only the window of the digitally reconstructed radiograph
B. Partial-volume averaging: each slice mixes nodule and lung, so the edge used for the target can be misplaced by a large fraction of the nodule
C. The nodule is forced to a Hounsfield number of exactly 0
D. 5 mm slices remove respiratory motion from the data set
Answer: B
Objective: II.4
Why: A thick slice assigns one value to a voxel that contains both tumor and lung. On a 1 cm nodule, a 5 mm slice is half the target, so the contoured edge is an average rather than the boundary. Stereotactic targets are scanned with slices that are small relative to the nodule and the margin. Slice thickness does not set water to 0 HU, and it does not freeze breathing. The window is a display choice.

### Q23
Stem: A 4D CT for a lung simulation is acquired with an external surrogate, and the trace is saved. The phases are never sorted. The tumor is contoured on one unsorted slice. What did that acquisition fail to provide?
A. Bins from which the range of the target can be combined into an ITV
B. A replacement for the external skin contour
C. Proof that slice thickness can be ignored
D. A measurement of carbon-fiber couch attenuation
Answer: A
Objective: II.4
Why: The surrogate exists so the acquisition can be sorted into phase or amplitude bins. The ITV is the union of the CTV positions in the bins that were scanned. One unsorted slice has no measured excursion. Skin contour, slice thickness, and couch attenuation are separate simulation checks. The maximum-intensity projection can help draw a lung tumor’s envelope later; it is not a substitute for having the bins, and it is not the dose grid.

### Q24
Stem: The 4D CT scan length is tight to the tumor at end-exhale. At end-inhale the tumor lies partly outside the reconstructed slices. The surrogate trace is regular. What ITV can this data set support?
A. A complete ITV, because a regular trace fills in the missing slices
B. An ITV that is short at the inhale extreme, because the clipped phase never entered the union
C. An ITV equal to the setup margin of the PTV
D. A complete ITV, because scan length applies only to a 3D CT
Answer: B
Objective: II.4
Why: The ITV includes only anatomy that was scanned. If the inhale position is cut off, that extreme is missing from the union and the internal margin is short in that direction. A clean surrogate trace does not invent the missing slices. The setup margin is the later PTV step. A 4D CT has a scan length, and that length has to cover the excursion.

### Q25
Stem: The planning CT was acquired on a curved diagnostic couch. Treatment will be on a flat carbon-fiber linac couch. A posterior beam is calculated with no couch in the contour. Which description fits?
A. The curved top changes the posterior contour relative to the flat treatment couch, and the posterior beam is missing the attenuation of the top it will cross
B. A curved couch is required for every linac plan, and carbon fiber is defined as air
C. Couch shape is a billing entry only; a posterior beam never crosses the top
D. The flat treatment top removes the need for reference marks
Answer: A
Objective: II.4
Why: Radiotherapy simulation uses a flat top so the spine and the posterior surface match the treatment couch. A curved diagnostic table is a different geometry. A posterior beam also traverses the carbon-fiber top. AAPM TG-176 addresses that attenuation. Leaving the top out calculates those rays through air. Carbon fiber is not air, and the couch does not replace tattoos.

### Q26
Stem: The DICOM origin, the tattooed reference marks, and the treatment isocenter are three different points. The shifts sent to the treatment machine are the vector between which two?
A. From the reference marks to the treatment isocenter
B. From the DICOM origin to the corner of the image, independent of the tattoos
C. From the isocenter back to the DICOM origin, with the marks discarded
D. A zero vector, because the origin, the marks, and the isocenter are defined as one point
Answer: A
Objective: II.7
Why: The therapists can find the reference marks. The isocenter is the planned point. The shift is that difference, in a stated orientation. The DICOM origin is a coordinate zero in the header. Moving it on import does not move the tattoos, and it is not automatically the isocenter. The three points coincide only when the isocenter was left on the marks and that same point is the origin.

### Q27
Stem: Head-first supine. +X is patient left, +Y is posterior, and +Z is superior. The reference BB is on the lasers. The planned isocenter is 2.0 cm to the patient’s left of the BB, so ΔX = +2.0 cm, with ΔY = 0 and ΔZ = 0. Which patient translation brings the isocenter onto the lasers?
A. 2.0 cm toward the patient’s left
B. 2.0 cm toward the patient’s right
C. 2.0 cm anterior
D. 2.0 cm superior
Answer: B
Objective: II.7
Why: ΔX = +2.0 cm means the isocenter is to the patient’s left of the mark. With the mark already on the lasers, the patient is translated by −Δ. −ΔX is 2.0 cm toward the patient’s right, which carries the left-sided isocenter onto the lasers. A further move to the patient’s left carries that point farther off the lasers. Anterior and superior are Y and Z, and both of those deltas are zero.

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
