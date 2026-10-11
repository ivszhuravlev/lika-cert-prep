# Module 32. The Accuracy and Limitations of IGRT Techniques

Module 18 named what each image can show. This module is why a passed match can still be the wrong treatment. Tolerances that depend on a protocol should be confirmed in that protocol or in the named task-group report.

## Limitations of IGRT

**MDCB objectives:** II.6, I.8, II.5

**What the exam expects**

You can explain five limits in plain language. Cone-beam CT is not a planning CT. A couch can correct a rotation and cannot correct a deformation. Surface guidance sees the surface. Prostate motion follows the rectum and the bladder. MRI geometry is distorted, especially away from the center and near air or metal. You can also say what a match region, a residual error, and a stale reference image do to the isocenter.

**Core facts**

**Cone-beam CT is not a planning CT.** A linac cone-beam is a slow, wide-cone acquisition with a limited field of view and a different scatter field from a diagnostic or simulation CT. Anatomy outside the reconstruction is truncated. Motion during the rotation blurs. Streaks from metal and from gas are worse. The Hounsfield numbers are not the density table the treatment-planning system was commissioned with. Using those numbers in the dose engine without a validated conversion calculates the wrong dose. The cone-beam exists to align the patient to the planning CT. Adaptive workflows that calculate on a cone-beam do so only after that conversion has been tested. Confirm the workflow in the departmental procedure. The imaging dose is real and is not the therapeutic dose grid.

**Rotation is not deformation.** A three-degree couch corrects translations. A six-degree couch also corrects pitch, roll, and yaw. Neither couch can apply a warp. If the neck is flexed, the shoulders have dropped, or the rectum has changed shape, part of the anatomy matches and part does not. Forcing a rigid fit on the bones then misplaces the soft tissue, or the reverse. The correct tool for a true shape change is a new plan or an adapted plan, not a larger rotation. Deformable registration can display the difference. It still cannot be delivered by the couch.

A small angle at a long lever arm is a large shift. Show the arithmetic every time a stem says the rotation is “only a few degrees.”

**Surface guidance sees the surface.** The cameras track skin or a vest of points on the skin. That signal is the right surrogate for a surface-defined target, especially breast position and deep-inspiration breath hold, and it is a useful intrafraction monitor. It does not see the prostate, a pelvic node, or a lung tumor that moves inside the chest. A perfect surface trace with the wrong internal anatomy is a passed check of the wrong organ. Surface guidance also cannot report an internal rotation that leaves the skin in place.

**Prostate motion follows rectum and bladder.** Gas or stool in the rectum pushes the prostate anteriorly. A much fuller or much emptier bladder than at simulation shifts the prostate and the seminal vesicles and changes the small-bowel position. The motion is interfraction and, to a smaller extent, intrafraction. A match to the pelvic bones can be excellent while the gland has moved several millimeters relative to the beams. Fiducials or a soft-tissue cone-beam are the checks that see the gland. The protocol says which of those is required. A surface camera does not substitute.

**MRI is distorted.** Two different effects move the pixels. Gradient nonlinearity is a property of the scanner and grows toward the edge of the field of view. Susceptibility and chemical shift are properties of the patient: air–tissue boundaries in the sinuses and the rectum, fat–water interfaces, and metal. A contour drawn on an uncorrected MRI and copied onto the CT can be in the wrong place by millimeters, more at the periphery than at the isocenter. MRI pixel values are not electron density. The dose calculation stays on a CT, or on a synthetic CT that has been validated as a density dataset. Metal makes local distortion severe enough that the slice may not be usable for a target edge. An MR-linac does not repeal this. It makes daily MRI available, and the distortion and the density questions remain.

**Other limits that decide exam questions**

- The match box decides the answer. A head-and-neck clip box that includes the jaw or the shoulder will sacrifice the target to match a moving part. Restrict the box to the stable anatomy the protocol names, then look at the rest.
- The reference is the planning CT or the DRR from it. Matching to yesterday’s cone-beam lets the isocenter walk away from the planned anatomy one day at a time.
- Two-dimensional kV pairs show bone and fiducials. They do not show a soft-tissue target that has moved off the bone. An MV portal shows the aperture in the beam’s-eye view and shows bone poorly in soft tissue. Neither is a volumetric soft-tissue match.
- Residual error remains after a good image. The PTV setup margin is the admission of that residual, plus the motion you did not gate. Image guidance can shrink the margin the protocol allows. It does not justify a zero margin.
- A six-degree correction that is computed and then only partly applied (rotation ignored because the couch cannot do it) leaves the error you calculated and chose not to remove. Re-image or reset.
- Time. A cone-beam acquired ten minutes before beam-on does not describe the bladder and the prostate at beam-on. Intrafraction motion needs a method that watches during the fraction if the protocol says the motion is large enough to matter.

**Formulas**

Rigid displacement from a small rotation:

Δ ≈ r × θ, with θ in radians.

θ (rad) = degrees × π / 180.

Example. The match is accepted at the center of a cervical spine field. The superior end of the target is 15 cm away. The residual rotation is 3°.

3 × π / 180 = 0.0524 rad

Δ = 15 × 0.0524 = 0.79 cm ≈ 8 mm

An 8 mm miss at the end of the field is larger than a typical stereotactic margin and is a real fraction of a conventional PTV. “Only 3°” is not small on a long target.

Second example. A prostate fiducial is 0.6 cm anterior to its planned position because the rectum is distended. The pelvic bones match within 0.1 cm. The bone residual does not describe the target. The target residual is 0.6 cm, and a translation of the couch by that 0.6 cm is the correction only if the whole region of interest, including the seminal vesicles and the nodes, moved together. If the nodes stayed with the bone and the gland moved, one rigid shift cannot satisfy both. That is the deformation limit in a single number from the stem.

**Traps**

- Calculating dose on cone-beam Hounsfield units.
- Applying a deformation with a couch coordinate.
- Treating surface guidance as an internal image for prostate or lung.
- Accepting a bone match as a prostate match.
- Drawing a target on a peripheral MRI slice without checking distortion against the CT.
- Walking the isocenter by matching each day to the previous day’s image.
- Setting the PTV margin to zero because “we do daily CBCT.”

**Sources**

- AAPM TG-179, QA for CT-based image guidance, including the limits of cone-beam geometry and HU
- AAPM TG-147, nonradiographic localization and surface guidance
- AAPM TG-132, rigid versus deformable registration
- ICRU 62, for the setup and internal margins that remain after imaging
- Departmental IGRT and MRI-simulation procedures, for action levels and distortion correction. Confirm the millimeters there.

## Accuracy and Limitations of IGRT Mini-Quiz

**MDCB objectives:** II.6, I.8, II.5

**Skills this quiz trains**

- Give the reasons cone-beam CT is not a planning CT: field of view, artifact, motion, and uncommissioned Hounsfield numbers.
- Convert a residual rotation into a displacement at a stated distance.
- Separate a rigid couch correction from a deformation.
- Assign surface guidance to the surface, and prostate position to rectum and bladder, seen with fiducials or soft-tissue imaging.
- Place MRI distortion at the edge of the field and near air and metal, and keep dose calculation on a CT density dataset.
- Keep the planning CT as the reference.

**Traps**

- Zero PTV margin justified by daily imaging.
- Bone match for prostate.
- Surface camera for an internal target.
- Yesterday’s cone-beam as the new plan reference.
- A 3° rotation ignored at 15 cm from the match point.
- MRI intensity treated as electron density.

**Check yourself**

A residual yaw of 2° remains after a skull match. A target point 12 cm inferior is uncorrected. How far does that point move? The same day, a prostate bone match is within 1 mm and the rectal diameter is much larger than at simulation. What has the bone match failed to prove?

Walk-through: 2° = 2 × π / 180 = 0.0349 rad. Displacement ≈ 12 × 0.0349 = 0.42 cm, about 4 mm, at that inferior point. The bone match has not proved prostate position. A distended rectum can push the gland anteriorly. Fiducials or a soft-tissue match are what show that shift. Surface guidance would not show it either.
