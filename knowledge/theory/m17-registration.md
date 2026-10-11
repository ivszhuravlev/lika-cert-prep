# Module 17. Rigid Image Registration, Deformable Registration, and Image Fusion

Curriculum title: Rigid Image Registration, Deformable Registration, Imaged Fusion.

Registration is how a second image set earns the right to move a contour, a couch, or a dose display. The exam asks which transform you used, what that transform can change, and how you would know the fusion is wrong.

## Image Registration

**MDCB objectives:** II.5

**What the exam expects**

You can separate a rigid registration from a deformable one and name the six degrees of freedom. You can say why CT-to-MRI and CT-to-PET need a similarity measure that does not require the pixel values to match. You can describe how a dosimetrist checks a fusion before drawing a target or accepting a shift. A blended color wash is a display. The display is only as true as the transform under it.

**Core facts**

A rigid registration applies one translation and one rotation to the whole image. Distances and angles inside that image stay the same. The six degrees of freedom are left–right, superior–inferior, and anterior–posterior translation, plus pitch, roll, and yaw. Some couches and some fusion tools solve only the three translations. A three-degree solution can center one point and still leave a rotation that moves the ends of a long target.

Rigid registration fits anatomy that behaves like one solid object between the two scans: skull to skull, vertebral body to vertebral body, a framed stereotactic study, a same-day brain CT and brain MRI. It is also the only transform a treatment couch can perform.

A deformable registration gives a displacement to many control points and interpolates a warp everywhere else. Boundaries can slide, shrink, and bend. That is the tool for propagating an atlas contour, comparing a planning CT with a CT after weight loss, or accumulating dose on changed anatomy. The warp can also fold tissue or stretch a uniform organ in a way the patient never did. A smooth overlay does not prove the vectors inside a homogeneous structure are right.

Fusion is the overlay you look at: color wash, split screen, checkerboard, or a spyglass. Fusion does not create the registration. It shows the registration you already computed.

Same-modality registration (CT to CT, or CBCT to planning CT) can compare voxel values directly. Cross-modality registration cannot assume cortical bone is bright on both images. Cortical bone is bright on CT and dark on MRI. PET intensity is uptake, not density. Mutual information is the usual cross-modality measure: it asks whether knowing the value on one image reduces the uncertainty of the value on the other. It does not need the intensities to be equal.

Landmark registration solves the transform from paired points. It is only as good as those pairs. Surface registration matches skin or another extracted surface and ignores everything deep to that surface.

The region inside the cost function decides the answer. A head-and-neck fusion optimized on the clivus can look right at the skull base and be wrong at the shoulders if the chin tuck changed. Restrict the clip box to the anatomy you are treating, then look outside that box so the residual error is visible.

A dedicated PET/CT is a same-setup pair, and the bladder, bowel, and arms can still differ between the CT and the PET acquisition. Uptake is not a margin. The GTV comes from the images plus the clinical findings. A bright PET voxel does not receive an automatic expansion of your own invention.

MRI brings geometric distortion into the fusion. Gradient nonlinearity grows toward the edge of the field of view. Air, bone, and metal shift local boundaries. Dose is calculated on the CT. An MRI contour is usable after the anatomy you are treating has been checked against that CT.

**Formulas**

A rigid transform in three dimensions has 6 parameters. A point 15 cm from the rotation center, rotated 3 degrees and not translated, moves approximately

Δ = rθ, with θ in radians.

3° = 3 × π / 180 = 0.0524 rad.

Δ = 15 × 0.0524 = 0.79 cm.

That is about 8 mm. A rotation that looks small on a skull match is a large miss at the end of a spine or neck volume. The same arithmetic shows up again when an IGRT rotation is waved through.

Overlap of two contours is often scored with the Dice coefficient:

Dice = 2 |A ∩ B| / (|A| + |B|).

If the physician contour is 12 cm³, the propagated contour is 12 cm³, and the overlap is 9 cm³,

Dice = 2 × 9 / (12 + 12) = 18 / 24 = 0.75.

The score says the volumes overlap. It does not say the missed quarter is safely away from the cord. On a deformable registration, also look for folding. A negative Jacobian in a voxel means the warp turned that bit of tissue inside out. A fold through the target or a serial organ is a failed registration.

Two fiducials 5.0 cm apart on both scans are compatible with a rigid fit. The same two points at 5.0 cm on the CT and 6.2 cm on the MRI are not. No single rigid transform can preserve both distances. The 1.2 cm disagreement is deformation, distortion, or a mis-identified point. Identify which one before anyone draws.

**Traps**

- A color wash hides a few millimeters. Check the structure you will contour with a split window or a checkerboard.
- A bone match and a soft-tissue match answer different questions. Prostate, liver, and many lung tumors move relative to bone.
- A deformable registration can copy a contour onto today’s CT. A couch cannot deliver that warp. The couch correction is rigid.
- Dose added through a deformable registration inherits the warp. An accumulated DVH can look precise in a sliding lung or in bowel that gained and lost gas and still be wrong. Registration QA expectations are in AAPM TG-132; confirm the departmental checks in that framework.
- Two images on one screen can still be tied to different origins. A shared display is not a shared frame of reference.

**Sources**

- AAPM TG-132, image registration and fusion in radiotherapy
- ICRU 62 and ICRU 83, for the volumes drawn after the images are registered
- DICOM spatial registration, for how a rigid transform is stored (object types are in the DICOM module)

## Image Registration Mini-Quiz

**MDCB objectives:** II.5

**Skills this quiz trains**

- Count the six rigid degrees of freedom and say which ones a translation-only couch leaves uncorrected.
- Choose rigid registration for skull-to-skull work and deformable registration for atlas propagation or a neck that has changed shape.
- Identify mutual information as the cross-modality similarity measure.
- Reject a fusion that matches the skull base and misses the shoulders when the target is in the low neck.
- Treat a fiducial spacing that disagrees between scans as evidence against a rigid model.
- State what Dice and a color wash leave unproved: location of the miss, and whether the warp is physically possible.

**Traps**

- Calling every overlay a deformable fusion.
- Treating PET brightness as a GTV.
- Turning a deformation grid into a couch shift.
- Ignoring MRI distortion at the edge of the field or next to sinus air.
- Optimizing on the whole image when only one region was reproducible at simulation.

**Check yourself**

A clip box locked to the mandible produces a clean overlay of the oral cavity. The target is a level IV node, and the shoulders sat lower on the MRI than on the CT. Which anatomy has to be inspected before the node is drawn, and which transform should you expect to need if the neck shape truly differs?

Walk-through: Inspect the overlay at the node, not at the mandible. A rigid fit cannot satisfy a different shoulder position and a different mandibular position at the same time. If the neck shape changed, the appropriate model is deformable, and the result still has to be checked on the slices that contain the node. A couch will later apply only a rigid correction.
