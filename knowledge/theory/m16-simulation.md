# Module 16. Treatment Simulations, TPS Localization of a Patient

Original notes for MDCB objectives II.4 and II.7.

## Where do shifts come from?

**MDCB:** II.7, II.2, II.1

**What the exam expects**

You compute the isocenter as a coordinate difference from a reference mark, in patient directions, and you know the couch move that puts that point on the lasers is the opposite translation. You do not confuse DICOM +y with anterior.

**Core facts**

A simulation places radiopaque marks or tattoos where lasers and a stable skin surface meet. That reference point is a coordinate origin you can find again. The planner then chooses a treatment isocenter on the CT, usually inside the target or at a geometric point that makes opposed beams practical. The shift is the vector from the reference mark to that isocenter.

For a head-first supine DICOM patient coordinate system the positive axes are: x toward the patient’s left, y toward the patient’s posterior, z toward the patient’s head. Anterior is negative y. Patient right is negative x. Inferior is negative z. Confirm the orientation tag. Feet-first and prone change which way the couch axes point relative to the patient.

If the mark is currently on the machine isocenter (lasers), the couch has to move the patient so the planned point travels to the lasers. The patient translation is the opposite of the vector drawn from the mark to the planned isocenter. Writing the shift in patient language (“isocenter is 2 cm to the patient’s right of the tattoo”) and writing it in couch language (“move the couch so the patient goes left”) without saying which one you mean is how the wrong point gets treated.

Shifts are in centimeters or millimeters as the clinic’s sheet requires. A factor-of-ten error is a localization error, not a rounding error. Shifts are documented superior/inferior, anterior/posterior, and left/right in patient terms, and the couch directions are whatever that clinic’s convention derives from them.

The isocenter is not required to sit on the tattoo. Zero shift is a special case. A stem that gives tattoo coordinates and isocenter coordinates is asking for a subtraction, then a sentence that names the patient direction.

Re-simulation or a new mark set creates a new origin. Old shifts do not carry to a new tattoo.

**Formulas**

In a consistent coordinate system:

Δx = x_iso − x_ref

Δy = y_iso − y_ref

Δz = z_iso − z_ref

Head-first supine DICOM, if +x is patient left, +y is posterior, +z is superior:

- Δx > 0: isocenter is to the patient’s left of the mark
- Δy < 0: isocenter is anterior to the mark
- Δz > 0: isocenter is superior to the mark

With the mark set to the lasers, the patient is translated by −Δ to bring the isocenter to the lasers.

**Worked example**

Given: head-first supine. DICOM axes as above. Reference BB at (0.0, 0.0, 0.0) cm. Planned isocenter at x = −2.0 cm, y = −4.0 cm, z = +6.0 cm. The BB is aligned to the lasers at the start of setup. State the isocenter relative to the BB in patient language, and state the patient translation that brings the isocenter onto the lasers.

Formula: Δ = isocenter − reference. Patient language follows the sign of Δ. Couch/patient translation with the mark on the lasers is −Δ.

Substitution: Δx = −2.0 − 0 = −2.0 cm. Δy = −4.0 cm. Δz = +6.0 cm.

Arithmetic is the subtraction. Interpretation:

- Δx = −2.0 cm means the isocenter is 2.0 cm to the patient’s right of the BB (+x is left).
- Δy = −4.0 cm means the isocenter is 4.0 cm anterior to the BB (+y is posterior).
- Δz = +6.0 cm means the isocenter is 6.0 cm superior to the BB.

With the BB on the lasers, translate the patient 2.0 cm toward the patient’s left, 4.0 cm down (posterior, toward the table, so the more anterior point comes down to the laser), and 6.0 cm inferior.

Check: after that translation the point that was at (−2, −4, +6) relative to the BB is at the lasers, and the BB is 2 cm to the patient’s right of isocenter, 4 cm posterior to isocenter, and 6 cm inferior to isocenter.

Meaning: the plan says the treated point is right, anterior, and superior to the tattoo. The couch move from a tattoo-on-lasers start is left, down, and inferior. Those are opposite descriptions of one shift. Both are correct if you say which object is moving and which is fixed.

Usual wrong turn: reading +y as anterior and reporting the isocenter 4 cm posterior, which treats a point 8 cm away from the one that was planned. Or instructing “shift the patient 2 cm right” because the isocenter is on the right, which moves the planned point farther from the lasers. Or quoting the shifts in millimeters on a sheet that was computed in centimeters (2 cm written as 2 mm).

**Traps**

Anterior/posterior sign. Couch direction copied from the patient vector with the mark already on the lasers. A new tattoo with the old shift. Head-first coordinates used on a feet-first scan. Zero shift assumed because tattoos exist.

**Sources**

DICOM patient coordinate system as used in planning systems. AAPM TG-66 for simulation marks and lasers. Public blueprint II.7 and II.2. Khan and Gibbons for setup geometry.

## Localization of OAR and Target Volumes

**MDCB:** II.7, II.4, III.11

**What the exam expects**

You define GTV, CTV, ITV, PTV, OAR, and PRV the way ICRU defines them, and you know which margin is motion and which is setup. You know what a simulation must show before those contours are believable: full windows, markers, and complete organs. Contouring the wrong structure, or half of an organ that has a paired constraint, makes the DVH a different patient.

**Core facts**

ICRU 50, 62, and 83 names used on this exam:

GTV. Gross tumor volume. Disease you can see, feel, or demonstrate on imaging. If there is no gross disease after surgery, there may be no GTV. There is still a CTV.

CTV. Clinical target volume. The GTV plus the surrounding tissue that may hold microscopic disease, or the elective region itself when there is no GTV. The CTV is an anatomic and biologic volume. It does not include setup error. It does not breathe, in the sense that motion is not part of its definition. You add motion in the next step.

ITV. Internal target volume, ICRU 62. The CTV plus an internal margin for physiologic motion: respiration, bladder, rectum, swallowing. The ITV is not a second CTV. Module 15: do not expand it again by the same motion.

PTV. Planning target volume. The CTV, or the ITV if you built one, plus a setup margin for geometric uncertainty, systematic and random. The PTV is a geometric volume used to select beam apertures and to evaluate coverage. It can contain air, bone, or bolus. It is not “the tumor.” A constraint written on the PTV is a coverage constraint. A constraint written on the CTV is a different statement, used in some ICRU 83 evaluations, and you must not substitute one for the other unless the protocol says so.

OAR. Organ at risk. Normal tissue whose dose you will evaluate. Contour the organ the constraint refers to. “Both lungs” means both lungs, usually minus the GTV if the protocol subtracts it. “Spinal cord” means the cord, not a short segment under one field, unless the protocol defines a partial cord. A half-contoured kidney produces a DVH that looks artificially good or artificially bad depending on which half you kept.

PRV. Planning organ-at-risk volume. The OAR plus a margin, the normal-tissue analogue of the PTV. Serial organs with a catastrophic max dose, cord and brainstem in particular, are often evaluated on a PRV so a setup error does not put the real cord over the limit. A PRV is not a target. You do not prescribe dose to it.

Treated volume. The volume enclosed by an isodose surface that the prescription considers adequate, often the 95% isodose. It is a result of the plan, not a contour you draw before planning.

Irradiated volume. The volume that receives a dose significant for normal-tissue tolerance. Also a result, larger than the treated volume.

Remaining volume at risk. ICRU 83: the imaged body minus the CTVs and the specifically contoured OARs. It exists so unspecified tissue is not invisible to the optimizer.

Simulation conditions for these contours, objective II.4:

- Preparation matches the protocol (filling, contrast, markers, immobilization).
- The data set is complete: no missing slices, skin included, scan long enough for entrances, exits, and OAR constraints.
- Full windows. Review soft tissue, lung, and bone as needed, and a window wide enough that the skin surface is visible. A single default window clips either the skin or the lung target.
- Wires and BBs are identified so a scar wire is not a GTV and a BB is not a bone island.
- Fusion, if MRI or PET is used to draw the GTV, is registered to this CT. The contour lives on the planning CT. A contour drawn on an unregistered MRI is in MRI space.

Serial versus parallel is how you read the OAR once it is localized. Cord and brainstem fail at a small hot spot (serial). Lung, liver, and kidney fail by volume irradiated (parallel). Localizing only the hottest slice of a parallel organ, or only the center of a serial organ, does not support the constraint.

**Traps**

PTV defined as visible tumor. ITV omitted and motion placed inside the CTV definition, then added again as setup. PRV prescribed to, or a target expanded and called a PRV. One lung contoured for a both-lungs constraint. Treated volume confused with PTV; the treated volume is an isodose shell, the PTV is the planning margin. Skin clipped by the window so the external contour, the PTV flash, and the OAR doses are all slightly wrong.

**Sources**

ICRU Reports 50, 62, and 83. AAPM TG-66. Public blueprint II.4, II.7, and III.11.

## Scan length, field of view, and the setup origin

**MDCB:** II.4, II.7

**What the exam expects**

You can say what a simulation data set has to contain before the shifts and the contours are believable: scan length, field of view, slice thickness, a flat indexed couch, a 4D CT that covers the excursion, and a clear separation of DICOM origin, reference marks, and isocenter. Respiratory strategy (gate, hold, compress, track) is module 15. With the marks on the lasers, the couch-move sign is the opposite of the isocenter-minus-mark vector in the shift section above. This section is the acquisition that makes those later steps true.

**Core facts**

Scan length is the superior-inferior extent of the reconstructed slices. It has to include the target, the motion excursion, every beam entrance and exit, and the organs whose constraints will be scored. A pelvis scan that stops mid-bladder cannot support a bladder constraint. A 4D CT that stops on the end-exhale tumor clips the inhale extreme, and the ITV built from those slices is short in that direction.

Field of view is the in-plane reconstruction diameter. It has to include the whole external contour, including an arm that a beam crosses, and the couch top when a beam traverses the top. Tissue outside the field of view is missing. The planning system treats the gap as air, so SSD, depth, and scatter move. Scan length and field of view are different settings. A complete superior-inferior range with the lateral skin cut off is still a clipped contour.

Slice thickness. A thick slice averages the target edge with the tissue around it. On a small nodule that average is a large fraction of the target, so the contoured edge can sit in the wrong place. Stereotactic lung and brain scans use slices that are small relative to the target and the margin. The clinic’s protocol names the thickness for the site. A thick slice does not remove motion, and it does not set the Hounsfield number of water.

4D CT, as a simulation. An external or internal surrogate sorts the acquisition into phase or amplitude bins. The ITV is the union of the CTV positions over the bins that were actually scanned (ICRU 62). For a solid tumor in lung, the maximum-intensity projection can help draw that envelope; the phases still have to be checked. The dose grid is the average CT or a selected phase, not the maximum-intensity projection. A single unsorted slice has no measured excursion. A duplicated diaphragm is a failed sort, and that artifact is not the ITV. Module 15 is where the choice among gating, breath hold, compression, and tracking is made.

Couch top. Radiotherapy simulation uses a flat top matched to the treatment couch, with the immobilization indexed to it. A curved diagnostic table changes the posterior contour and the spine relative to a flat linac top. Posterior and posterior-oblique beams pass through the carbon-fiber top and through indexed devices. That attenuation belongs in the calculation (AAPM TG-176). A beam calculated with the top omitted is a beam calculated through air.

Origin and reference marks. Three points stay distinct. The DICOM origin is a coordinate zero in the image header. The reference marks, tattoos or BBs where the lasers met a stable skin surface, are the external point that can be found again. The treatment isocenter is the point the planner chose. Shifts are the vector from the reference marks to the isocenter. They are zero only when those two points are the same point. Resetting the DICOM origin does not move the tattoos. A new tattoo set is a new reference, and the old shifts do not apply.

With the marks already on the lasers, the patient translation that brings the isocenter to the lasers is the opposite of that vector. Head-first supine DICOM signs are in the shift section: +x patient left, +y posterior, +z superior. Name which object moves.

**Traps**

Field of view confused with scan length. A 4D CT ITV drawn from a scan that clips the inhale extreme. Dose calculated on the maximum-intensity projection. A curved diagnostic couch used as if it were the flat treatment top. Posterior beams calculated with the couch omitted. The DICOM origin treated as the isocenter. The isocenter-minus-mark vector copied onto the couch when the marks are already on the lasers.

**Sources**

ICRU Reports 50, 62, and 83. AAPM TG-66 for simulation lasers, geometry, and the flat indexed couch. AAPM TG-176 for couch-top and immobilization attenuation. AAPM TG-76 for respiratory motion, applied in module 15. Public blueprint II.4 and II.7.

## Localization Mini-Quiz

This quiz checks GTV, CTV, ITV, PTV, OAR, and PRV; a shift as isocenter minus reference with DICOM signs; and the simulation requirements of full windows, complete organs, and identified markers. Further items separate scan length from field of view, ask what a thick slice does to a small target, and ask which patient translation applies when the reference mark is already on the lasers. The traps are calling the PTV the gross tumor, adding motion on top of an ITV, reading +y as anterior, reversing the couch move when the tattoo starts on the lasers, contouring one side of a paired organ for a bilateral constraint, and treating the DICOM origin as the isocenter.
