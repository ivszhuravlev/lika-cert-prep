# Module 17 — Rigid image registration, deformable registration, and image fusion

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Image Registration

### Q1
Stem: A diagnostic MRI of the brain from two days ago is fused to a planning CT. The skull is intact, nothing has been resected, and both scans cover the whole head. Which registration is the appropriate first choice?
A. Deformable registration only, because CT and MRI intensities can never be aligned rigidly
B. Rigid registration with three translations and three rotations, then a bone check around the target
C. Skip registration and calculate dose on the MRI, because MRI shows the tumor better
D. Deformable registration applied only inside air cavities
Answer: B
Objective: II.5
Why: Answer B. An intact skull does not change shape between these two scans, so a rigid transform is the right model. Rigid registration has six degrees of freedom: left-right, anterior-posterior, and superior-inferior translation, plus pitch, roll, and yaw. The planner then checks landmarks in bone near the target, not only at the skin. A is wrong because multimodality images are routinely registered rigidly; the similarity metric changes (mutual information is typical for CT-MRI), not the rigidity of the skull. C is wrong because MRI voxel values are not Hounsfield units and cannot be turned into electron density for dose calculation. D restricts the warp to the region where a smooth deformable model is least trustworthy.

### Q2
Stem: Yesterday's planning CT was taken with a full bladder. Today's cone-beam CT shows the bladder at about half that volume, and the prostate has moved. The therapist asks for one couch shift that will make every soft-tissue voxel line up with the plan. What can a rigid registration do here?
A. Restore the planning bladder volume by rotating the couch
B. Apply one translation and one rotation set so that distances between pelvic bones are preserved, which will not undo the bladder deformation
C. Warp the planning CT bladder down to today's volume while keeping the registration classified as rigid
D. Change today's bladder HU so the volumes match and call that a registration
Answer: B
Objective: II.5
Why: Answer B. A rigid transform cannot stretch or shrink tissue. It can only slide and rotate the whole image, so the distance between two bony points stays the same. That single shift may center the prostate or the bones, but it cannot make a half-full bladder take the shape it had on the planning CT. A couch rotation is still rigid. C describes a deformable vector field, which is a different model and is not produced by a couch shift. D is a density edit, not a geometric registration.

### Q3
Stem: A deformable registration between a planning CT and a mid-treatment CT reports a Jacobian determinant of −0.4 in a cluster of voxels along the rectal wall. How should that region of the displacement field be treated?
A. As a valid compression, because any Jacobian below 1 means the registration succeeded
B. As a non-physical fold; do not use that vector field to accumulate dose or to copy contours through the fold
C. As proof that the rectum received 40% less dose than planned
D. As a rigid six-degree-of-freedom result, since the Jacobian is only displayed for rigid fuses
Answer: B
Objective: II.5
Why: Answer B. The Jacobian determinant describes how a tiny volume changes under the displacement field. A value of 1 means the volume is unchanged, a value between 0 and 1 means contraction, and a value greater than 1 means expansion. A negative value means the field has folded tissue through itself, which anatomy cannot do. Contours and dose pushed through a fold are not usable until the registration is redone and the fold is gone. A is wrong because "below 1" includes both ordinary contraction and this non-physical result. C confuses a geometric Jacobian with a dose ratio. D is wrong because a single rigid transform does not produce a voxel-by-voxel Jacobian map.

### Q4
Stem: After a CT-MRI fusion for a base-of-skull target, a bony landmark next to the target is still 4 mm apart on the two scans. The PTV margin written in the protocol is 3 mm. What is the correct next step?
A. Draw the target on the MRI anyway; the 3 mm PTV was designed to absorb a known 4 mm fusion miss
B. Correct or repeat the registration until the local landmark agreement is acceptable, then contour
C. Expand the MRI tumor by 4 mm, call the expansion a GTV, and leave the fusion as it is
D. Turn off the CT and plan on the MRI geometry so the 4 mm gap disappears
Answer: B
Objective: II.5
Why: Answer B. A 4 mm landmark mismatch is a known systematic error in the secondary image. Tissue drawn on the MRI will land 4 mm away from the correct CT voxels, and dose is computed on the CT. A PTV margin is a generic allowance for residual setup and delineation uncertainty. It is not a license to leave a measured 4 mm fusion error in place, and 4 mm is already larger than this protocol's entire 3 mm margin. C renames a registration error as tumor. D removes the density dataset the dose engine needs.

### Q5
Stem: Two planning CTs of the same patient, both with similar gray-scale intensities, are being registered. Which similarity measure matches that same-modality problem, and which measure is the usual choice when the second scan is an MRI?
A. Sum of squared intensity differences for the CT-CT pair; mutual information for the CT-MRI pair
B. Mutual information for the CT-CT pair; sum of squared differences for the CT-MRI pair
C. Hounsfield-unit subtraction for both, after converting MRI signal to HU by multiplying by 1000
D. Surface paint only; intensity-based registration is not used in treatment planning
Answer: A
Objective: II.5
Why: Answer A. When both images represent the same physical quantity, as two CTs do, voxels that correspond should have similar intensities, so a sum-of-squared-differences (or a similar mono-modality) metric is appropriate. MRI signal is not HU and is not linear with it, so corresponding tissues do not share a number. Mutual information scores how well one image's intensities predict the other's without assuming they are equal, which is why it is the standard CT-MRI metric. C invents a conversion that does not exist. D is wrong because intensity-based rigid and deformable registration is routine; surfaces are only one of the tools.

### Q20
Stem: A CT-MRI skull fusion looks acceptable on the blended display. A bony landmark next to the target is still 4 mm apart, and the PTV margin is 3 mm. What does that landmark result mean for drawing the target on the MRI?
A. Draw it; a blend that looks smooth means the 4 mm gap is only a display artifact
B. Do not draw it yet; 4 mm at the landmark next to the target is a systematic fusion error and is already larger than the 3 mm PTV
C. Draw it; the 3 mm PTV was assigned to absorb a measured 4 mm fusion miss
D. Discard the CT and calculate dose on the MRI so the 4 mm gap is no longer in the dataset
Answer: B
Objective: II.5
Why: Answer B. A color wash can look smooth and still hide a few millimeters. The landmark beside the target is the check that matters. Tissue drawn on the MRI will land 4 mm from the CT voxels, and 4 mm is larger than this entire PTV margin. The margin is not a budget for a known fusion miss. Dose is calculated on the CT, so dropping the CT removes the density dataset.

### Q21
Stem: A rigid registration applies a 3° rotation and no translation about a point in the neck. A cord point lies 15 cm from that center. Using Δ = rθ with θ = 0.0524 rad, about how far does that point move?
A. About 8 mm
B. 3 mm, because a 3° rotation is a 3 mm shift at any distance
C. 15 mm, which is the distance to the center
D. 0.05 mm, which is the angle in radians read as millimeters
Answer: A
Objective: II.5
Why: Answer A. Δ = 15 cm × 0.0524 = 0.786 cm, about 8 mm. A rotation that is small at the match point is a large miss at the end of a long target. Degrees are not millimeters, and the radian value is the angle, not the displacement.

### Q22
Stem: Two bony landmarks are 5.0 cm apart on the planning CT and 6.2 cm apart on the MRI. Which transform can make both distances true at once?
A. A rigid registration inside a larger clip box
B. A six-degree-of-freedom rigid registration, because six parameters include stretch
C. A translation-only registration
D. None that is rigid; one rigid transform preserves distance, so the 1.2 cm disagreement is distortion, deformation, or a misidentified point
Answer: D
Objective: II.5
Why: Answer D. Rigid registration keeps distances inside the image the same. 5.0 cm on one scan cannot land on 6.2 cm on the other. Adding rotations does not add stretch, and a larger clip box does not change that. Find the bad point or the distortion before anyone contours through the pair.

### Q23
Stem: A surface registration of a diagnostic scan to the planning CT matches the skin. The target is a node several centimeters deep to that skin. What did the registration actually align?
A. The node, because skin and a deep node are one rigid body at every site
B. The Hounsfield numbers of the node
C. The skin surface that entered the cost function; the node was not a landmark in that match
D. The monitor units of the plan
Answer: C
Objective: II.5
Why: Answer C. Surface registration solves the extracted surface. A close skin match says nothing reliable about a node deep to it. The transform does not edit CT numbers and it does not set monitor units.

### Q24
Stem: After a rigid bone match at the center of the head, an MRI contour near the edge of the field of view is copied onto the planning CT. The target sits next to sinus air. What still has to be checked?
A. The target edge against the CT, because geometric distortion grows toward the periphery and near air, and dose is calculated on the CT
B. Nothing; gradient nonlinearity is zero across a clinical MRI
C. Nothing; MRI signal multiplied by 1000 is electron density
D. Only a warp inside the air cavity, which removes distortion by definition
Answer: A
Objective: II.5
Why: Answer A. Gradient nonlinearity increases away from the center, and susceptibility shifts boundaries at air, bone, and metal. A good central bone match does not certify the edge of the field. The MRI contour is usable after that edge has been checked on the CT. MRI values are not a density table.

### Q25
Stem: Fusion software solves only the three translations for a long cervicothoracic target. The center of the target is centered on the planning CT. What can remain wrong?
A. Nothing; three translations already include pitch, roll, and yaw
B. Nothing; centering one point centers the ends of a long target
C. The Hounsfield scale of the CT
D. A residual rotation that swings the superior and inferior ends while the center stays put
Answer: D
Objective: II.5
Why: Answer D. Three translations are left-right, superior-inferior, and anterior-posterior. Pitch, roll, and yaw are the other three degrees of freedom. A solution that centers the middle of a long target can leave a rotation that moves the ends. That residual is geometric. It is not a change in CT number.

## Image Registration Mini-Quiz

### Q1
Stem: A PET/CT for a lung tumor was acquired last week during quiet breathing. The planning CT is a breath-hold scan. A rigid registration locked to the clavicles and vertebral bodies looks excellent, but the PET avid mass sits 1.5 cm medial to the mass on the planning CT. What does the bone match prove?
A. The tumor is correctly localized, because a good bone match validates every voxel in the chest
B. The bones agree; the tumor may have moved with respiration or posture, so the PET avid volume must not be copied across this transform without a soft-tissue check
C. Deformable registration is unnecessary in the chest because the lungs are rigid
D. The 1.5 cm gap is the PET voxel size and can be ignored
Answer: B
Objective: II.5
Why: Answer B. Rigid agreement of stable bones only says the skeletal coordinate systems coincide. A lung tumor is not fixed to the clavicle. Breathing phase, arm position, and mediastinal shift can move it by more than a centimeter while the bones still match. The metabolic volume should be checked against the tumor on the planning CT, or the scans should be repeated in compatible respiratory states, before that PET signal is used as a target. A overstates what a region of interest match can guarantee. C is the opposite of chest mechanics: the lung-chest wall interface slides, which is a known place deformable models fail. D is far larger than a localization tolerance and is not a voxel-size effect.

### Q2
Stem: A deformable algorithm propagates the spinal cord from the planning CT onto a replanning CT. The Dice coefficient of the propagated cord against a new manual cord is 0.92. What else has to be true before that propagated cord is used for planning?
A. Nothing; a Dice coefficient above 0.90 means every slice is safe
B. The cord is reviewed on every slice, because Dice is an overlap summary and can stay high while one slice is missed or shifted into the canal
C. Dice replaces the need to check the Jacobian of the vector field
D. The propagated cord may be used for dose calculation directly, since a structure set contains electron density
Answer: B
Objective: II.5
Why: Answer B. Dice equals twice the overlap volume divided by the sum of the two volumes. It is one number for the whole organ. A cord can have a high Dice score and still be wrong on a single axial slice, and that slice may be the one next to the high-dose region. Slice-by-slice review, and a check that the vector field has not folded, still has to be done. C is wrong because a fold (negative Jacobian) is a separate failure from overlap of the final surfaces. D is wrong because contours do not carry HU; dose is calculated on the CT densities.

### Q3
Stem: Which statement correctly separates image registration from image fusion?
A. Registration is the transform that maps one dataset onto the other; fusion is the display of the two datasets after that transform is applied
B. Fusion is the transform; registration is only the color wash used on the screen
C. They are two names for the dose grid resampling step
D. Fusion changes HU inside the CT so the MRI can be used for monitor-unit calculation
Answer: A
Objective: II.5
Why: Answer A. Registration solves for a rigid transform or a displacement vector field. Fusion is what the planner looks at: the CT gray scale with the MRI or PET laid on top using that transform. A pretty color wash does not create the transform, and neither step rewrites CT numbers into MRI signal or the reverse. Dose resampling onto a common grid is a later, separate operation and is not what "fusion" means.

### Q4
Stem: A head-and-neck planning CT is being registered to a diagnostic CT on which the shoulders were pulled much lower by a different immobilization position. The target is in the oropharynx. Which rigid-registration region is the most defensible?
A. A clip box that includes the shoulders and the skull equally, so the average error is shared
B. A clip box on the skull base and upper cervical spine near the target, accepting that the shoulders will not match
C. A clip box on the humeral heads only, because those bones are the largest
D. No clip box; the scanner table is a better landmark than the cervical spine
Answer: B
Objective: II.5
Why: Answer B. A single rigid transform cannot satisfy two regions that have moved relative to each other. The oropharynx moves with the skull and upper neck, not with the humeral heads. Matching the bones next to the target keeps the error where it matters. Averaging in the shoulders (A) pulls the target off in order to improve anatomy that will not be used for this target. C optimizes the wrong landmark. D registers furniture, not the patient.

### Q5
Stem: A physicist wants to add the dose from the original plan to the dose from an adaptive plan after 15 fractions of weight loss. Both plans have a DVH. Which method is a deformable dose accumulation, and which is not?
A. Adding the two cumulative DVH curves point by point is deformable accumulation, because both DVHs came from CT scans
B. Mapping one dose grid onto the other anatomy with a reviewed displacement vector field is the accumulation step; adding the DVHs is not, because a DVH has thrown away spatial location
C. Subtracting the mean doses and calling the difference the accumulated dose
D. Copying the original isodose lines onto the new CT without a transform, because isodose lines are already in percent
Answer: B
Objective: IV.5
Why: Answer B. Dose accumulation has to move dose voxels from one geometry onto a common geometry. That requires the displacement field (and a decision about which anatomy is the reference), followed by a sum of dose in that shared frame. A DVH has already collapsed each structure to "how much volume got how much dose." Two DVHs do not record where the high-dose voxels sat, so they cannot be added to represent tissue that has warped. The result of a proper accumulation is still an estimate: it inherits every error in the vector field, especially at sliding surfaces and air. C and D discard geometry entirely.
