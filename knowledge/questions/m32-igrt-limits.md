# Module 32 — Accuracy and limitations of IGRT

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Limitations of IGRT

### Q1
Stem: Cone-beam CT, fiducial shifts, and surface guidance are all available. Which task can none of them do?
A. Reduce the size of the setup error that remains after a couch correction
B. Prove that the delivered three-dimensional dose equals the planned dose
C. Show that the patient is grossly in the wrong place before the beam goes on
D. Detect a large weight change that makes the mask loose
Answer: B
Objective: II.6
Why: Answer B. Image guidance measures position (and, for volumetric imaging, some of the anatomy of the day). It does not measure the dose distribution. Agreement of a cone-beam CT with the plan does not confirm monitor units, leaf sequence, energy, wedge, bolus, or the calculation algorithm. Transit dosimetry and a phantom measurement are different tests. Imaging can still catch a wrong shift, a loose mask, or a large anatomic change, and a corrected setup does leave a smaller residual error than an uncorrected one. Those are localization results, not a dose proof.

### Q2
Stem: A perfect pre-treatment cone-beam match is obtained for a 15-minute liver SBRT fraction. There is no implanted marker tracking and no repeat image during the beam. The patient takes a deep breath and settles 6 mm after the scan. What can that cone-beam CT not do?
A. It cannot correct motion that happens after the image is acquired
B. It cannot be registered rigidly to the planning CT
C. It cannot show the vertebral body
D. It cannot be stored in the record-and-verify system
Answer: A
Objective: II.6
Why: Answer A. A pretreatment image is already out of date once the patient moves. Without intrafraction imaging or tracking, the 6 mm settle is invisible and uncorrected, and for SBRT it can be a large fraction of the margin. The cone-beam CT itself was perfectly usable for a rigid match, it shows bone, and it can be archived. The limitation is temporal: localization at time zero does not govern time zero plus ten minutes.

### Q3
Stem: A clinic tightens a prostate PTV margin from 8 mm to 3 mm because daily fiducial imaging is now available. Which statement about the remaining margin is correct?
A. The margin can be zero, because daily imaging removes random and systematic error completely
B. A margin remains, because residual couch error, fiducial migration, intrafraction motion, and contour uncertainty are not zero
C. The margin should increase when imaging is added, because imaging introduces deformation the PTV must cover
D. Fiducial imaging replaces the CTV, so only a GTV is contoured
Answer: B
Objective: II.6
Why: Answer B. Daily correction removes a large part of the systematic setup error and much of the day-to-day random shift, which is why margins can shrink. It does not make the residual zero. The couch does not execute a shift with infinite accuracy, the markers can migrate, the gland can move after the image, and the physician's contour is not perfect. Van Herk-type recipes exist because those residuals still need a margin. Imaging does not create a reason to enlarge the margin by default, and it does not change the definition of CTV.

### Q4
Stem: Kilovoltage orthogonal images are proposed as the only image guidance for a palliative spine field and as the only image guidance for a soft-tissue sarcoma that is not visible on radiographs and has no markers. For which patient do those images fail to show the target?
A. Both, because orthogonal kV images cannot show bone
B. The spine patient, because vertebral bodies are invisible at kilovoltage energy
C. The sarcoma patient, because a pair of radiographs shows bone and markers, not an unmarked soft-tissue mass
D. Neither, because two projections reconstruct a soft-tissue cone-beam CT
Answer: C
Objective: II.6
Why: Answer C. Orthogonal kilovoltage films are good at bone and at high-Z markers. A vertebral body match is a reasonable surrogate for a bone target such as a spine met, within the limits of two-dimensional imaging. An unmarked soft-tissue sarcoma does not appear on those films, so matching the nearest bone can miss the mass. Two radiographs are not a cone-beam CT and do not reconstruct the soft-tissue volume.

### Q5
Stem: Surface guidance confirms the breast surface during deep-inspiration breath hold. The physician wants to know whether the internal mammary nodes and the heart are in the planned position. What can the surface system not do?
A. It cannot gate or interrupt the beam based on the skin surface
B. It cannot see internal anatomy, so a correct surface does not prove the node or the heart is at the planned depth and position
C. It cannot be used for breath-hold coaching
D. It cannot record a shift in the anterior direction
Answer: B
Objective: II.6
Why: Answer B. The cameras see the surface they were calibrated to. Correlation between that surface and an internal structure is an assumption, and it breaks if the patient achieves the same chest height with a different internal pose. Surface guidance can coach a breath hold, can beam-hold when the surface leaves tolerance, and can report an anterior shift. None of that is an image of the internal mammary chain or of the heart.

### Q20
Stem: The planning CT is head-first supine. The cone-beam is feet-first. Registration reports 0 mm on bone. What is the correct use of that match?
A. Treat; a 0 mm bone result means head-first and feet-first are the same setup
B. Treat after changing only the left-right sign of a zero shift
C. Do not treat on that match; a feet-first cone-beam is not the head-first plan, and 0 mm on bone does not make the orientations the same
D. Treat if the monitor units match, because orientation is outside image guidance
Answer: C
Objective: II.6
Why: Answer C. Head-first supine and feet-first are opposite directions on the couch and in the image frame. A reported 0 mm can be a bone overlay of the wrong orientation. It does not show that the patient is in the planned position. The beam stays off until a cone-beam is acquired in the planned orientation and matched again. Monitor units do not repair the direction of the patient.

### Q21
Stem: A target is contoured on an MRI slice at the edge of the field, beside a sinus, and copied to the planning CT. The bone match at the center of the head is 1 mm. Which limit does that match leave in place?
A. None; distortion is largest at the isocenter and zero at the edge
B. None; a 1 mm bone match certifies every peripheral pixel
C. None; the MRI pixel values are the electron-density grid
D. Geometric distortion from the gradients and from the air-tissue interface, which can move the target edge by millimeters
Answer: D
Objective: II.6
Why: Answer D. Gradient nonlinearity grows toward the edge of the field, and susceptibility shifts boundaries at air and metal. The central bone match does not measure that local error. MRI values are not density. The edge has to be checked on the CT before the contour is used for planning.

### Q22
Stem: A tonsil cone-beam is matched with one clip box that weights the skull base and the dropped shoulders equally. The shoulders sit lower than they did at simulation. Where does that rigid match put the error?
A. On the tonsil, because the shoulders pull the single transform off the target
B. Nowhere; the skull and the shoulders cannot move relative to each other
C. Only on the humeral heads, while the tonsil stays fixed by definition
D. Into a deformable shift that the couch can deliver
Answer: A
Objective: II.6
Why: Answer A. One rigid correction cannot satisfy two regions that have moved apart. Sharing the match with the dropped shoulders moves the tonsil off the plan in order to improve anatomy that is not the target. The clip box belongs on the stable bones next to the tonsil. The couch still applies a rigid shift, not a warp.

### Q23
Stem: A six-degree match calls for 3° of roll. The couch can only translate, so the roll is not applied and the translations are. What remains?
A. No rotational error, because an ignored rotation is deleted from the patient
B. The roll that was calculated and not delivered
C. A new planning CT written by the couch move
D. An energy change of 3 MV
Answer: B
Objective: II.6
Why: Answer B. A rotation you measure and then do not apply is still in the setup, and it grows with distance from the match point. Translations do not cancel it. The couch does not create a new planning CT and it does not change the energy. Re-image after a reset, or apply the rotation only on a couch and a protocol that allow it.

### Q24
Stem: Rectal gas has moved the prostate 0.6 cm anterior to the plan. The pelvic nodes have stayed with the bone, and the bone residual is 0.1 cm. One couch translation is used to center the prostate. What does that single shift leave unresolved?
A. The ability to move the prostate by 0.6 cm
B. Recording the translation in the shift log
C. The fact that the correction is rigid
D. The nodes, which did not move with the prostate, so one translation cannot restore both
Answer: D
Objective: II.6
Why: Answer D. The gland and the nodes are no longer one rigid object. Centering the prostate leaves the nodes about 0.6 cm off the bone-based plan, and a bone match leaves the prostate off. The couch can apply the translation, and the log can store it. It cannot undo the deformation between prostate and nodes.

### Q25
Stem: During a prostate fraction the surface-guidance cameras report the skin within 1 mm. A cone-beam from the same session shows a distended rectum and a shifted gland. What has the surface system failed to show?
A. The anterior position of the skin it is tracking
B. A beam-hold when that skin leaves the tolerance
C. The internal move of the prostate relative to the surface
D. An anterior coordinate for the skin
Answer: C
Objective: II.6
Why: Answer C. The cameras see the surface they were aimed at. Rectal filling can displace the prostate while the skin trace still passes. Surface guidance can still report that skin position and can hold the beam when the surface leaves tolerance. It does not image the gland.

### Q26
Stem: According to AAPM TG-142, monthly coincidence of the imaging and treatment isocenters is ≤2 mm on a non-stereotactic machine and ≤1 mm for SRS/SBRT. A palliative site and a prostate site each have their own clinical action levels in the departmental policy. How are the TG-142 numbers used?
A. As the clinical action level for every site, because 2 mm is the patient-shift limit
B. As the machine test that the imager and the treatment isocenter agree. The clinical action level remains the site policy
C. As the PTV margin, so every PTV is expanded by 2 mm
D. As clearance to set the prostate margin to zero when the monthly test has passed
Answer: B
Objective: II.6
Why: Answer B. TG-142’s imaging coincidence tolerance is a QA result for the machine: the image and the beam share an isocenter within 2 mm, or within 1 mm for stereotactic use. The action level that tells the team when a patient shift is inside their authority, and when to call a physician, is written for the site and the margin. Passing the monthly test does not write those clinical numbers and does not erase the PTV.

### Q27
Stem: An offline NAL correction, taken from the first set of images, is now in the setup note. Today’s pretreatment image is not used to move the couch. That day’s setup still contains a random residual different from the NAL mean. What does NAL leave in place?
A. No residual; applying the systematic estimate removes random error before beam-on
B. Today’s random residual. NAL applies the estimated systematic correction on later fractions and leaves the online shift for a pretreatment image
C. The systematic error only, because NAL is defined to leave systematic error untouched
D. A new dose distribution calculated from the mean shift
Answer: B
Objective: II.6
Why: Answer B. NAL produces a correction for the systematic component and applies it to future fractions, with no action threshold. The random component changes from day to day. Without an online image and a couch move before this beam, that random piece remains. NAL is aimed at the systematic error, and it does not reoptimize the plan.

### Q28
Stem: One planner ignores daily cone-beam dose because the beam is kilovoltage. Another subtracts one therapeutic fraction for every cone-beam. Which description fits the two arguments?
A. Both match a dose that is real, much smaller than a treatment fraction, and kept out of the prescription unless a validated method adds it
B. The first undercounts a dose that is not zero. The second treats a localization exposure as if it were a treatment fraction
C. Both are required by TG-142, which sets cone-beam dose equal to the prescription
D. Cone-beam dose is deposited only in a phantom, so neither argument describes the patient
Answer: B
Objective: II.6
Why: Answer B. Each kilovoltage cone-beam contributes patient dose, so calling that dose zero is the wrong direction. The contribution is not a megavoltage treatment fraction, so subtracting prescription dose one-for-one is the other wrong direction. TG-142 does not set imaging dose equal to the prescription. The scan dose is delivered to the patient.

### Q29
Stem: An MR-linac protocol includes an adaptive trigger. One fraction shows a rigid translation and organ shapes that still match the plan. Another shows rectal gas that has deformed the target relative to the rectal wall, and one couch translation cannot restore both. Which decision matches the trigger?
A. Both fractions get a full online replan, because every MR-linac image is an adaptive trigger
B. The rigid translation stays a localization correction. The deformation is the finding that triggers physician review and, when the workflow applies, adaptation
C. Neither fraction is imaged, because an MR-linac shows only the skin surface
D. The deformed fraction is treated by matching to yesterday’s image
Answer: B
Objective: II.6
Why: Answer B. The adaptive trigger is the protocol’s concept for when a rigid shift is no longer the right tool. A pure translation with stable anatomy is image guidance. A shape change that one couch move cannot undo is the situation the trigger is written for, and it includes a physician decision. An MR-linac image is not automatically a replan. The point of that image is soft tissue. Yesterday’s image is the wrong reference. Module 28 is the check of an adapted plan.

### Q30
Stem: A bone match is inside the site’s action level. The protocol required a soft-tissue match, and the soft-tissue target is outside that same action level. What limit of “in tolerance” is this?
A. The action level applies to the surrogate the protocol named. An in-tolerance bone result leaves a soft-tissue miss in place
B. Bone and soft tissue share one residual, so the bone number is the target number
C. An action level is only the TG-142 machine test, so the soft-tissue discrepancy is discarded
D. A soft-tissue miss is removed by setting the PTV margin to zero
Answer: A
Objective: II.6
Why: Answer A. Tolerance means something only for the match the protocol asked for. A bone residual inside the limit can sit beside a target residual outside it when the target moves relative to bone. The action level is not the TG-142 isocenter test. Setting the PTV margin to zero does not remove the miss that is already on the image.

## Accuracy and Limitations of IGRT Mini-Quiz

### Q1
Stem: A cone-beam CT Hounsfield number in the liver reads 40 HU different from the planning CT in the same region, and the field of view cuts off the lateral body wall. A planner copies the cone-beam CT into the planning system and calculates monitor units with the photon density table from the simulator CT. What limitation is being ignored?
A. Cone-beam numbers are the same quantity as planning-CT numbers and can use the same calibration curve without validation
B. Scatter, spectrum, and truncation make cone-beam Hounsfield units a poor density source unless a validated correction or override is applied; the missing body wall is missing attenuation
C. The difference of 40 HU is exactly 40 Gy and already equals the prescription
D. Truncation only removes image noise, so the monitor units become more accurate
Answer: B
Objective: II.6
Why: Answer B. Image guidance CT is built to show position, not to feed a commissioned density table. Extra scatter and a different beam spectrum shift the numbers, and a truncated contour omits tissue the treatment beam may cross. Using those voxels with the simulator's Hounsfield-to-density curve assigns the wrong attenuation and the wrong scatter. A 40 HU discrepancy is a density error, not a dose of 40 Gy. This is one of the things cone-beam imaging cannot do: it cannot, by itself, replace the planning CT for dose calculation.

### Q2
Stem: Daily imaging has been perfect for 20 fractions. On fraction 21 the record-and-verify system has the wrong energy loaded, and a wedge that was removed from the plan is still in the treatment field. The cone-beam match to bone is 0 mm. Which errors does that match leave untouched?
A. The energy and the wedge, because image guidance does not check beam parameters or accessories
B. The 0 mm shift, because a perfect match means the energy was verified
C. Only the patient's name, which is encoded in the cone-beam pixel values
D. The wedge, but not the energy, because kilovoltage imaging measures photon energy in the treatment head
Answer: A
Objective: II.6
Why: Answer A. A localization image answers "where is the patient?" It does not answer "what will come out of the head?" Energy, monitor units, wedge, bolus, electron cone, and multileaf pattern are the job of the record-and-verify system, the timeout, and machine interlocks. A flawless bone match with a wrong accessory is still a wrong treatment. The cone-beam pixels do not store the linac energy.

### Q3
Stem: A head-and-neck CTV includes microscopic mucosal disease that was never visible on CT or on cone-beam CT. Daily cone-beam CT matches the cervical spine within 1 mm. What does that match not establish?
A. That the spine is in the planned position within about a millimeter
B. That the microscopic CTV is covered, because image guidance cannot display disease that has no imaging contrast
C. That a gross, visible lymph node is present on the cone-beam CT
D. That the mask is grossly misaligned by a centimeter
Answer: B
Objective: II.6
Why: Answer B. The CTV is defined to include subclinical disease. By definition much of it has no edge on CT or cone-beam CT. Matching the spine shows the bones are aligned; it does not draw the microscopic volume and it does not prove the physician's CTV is still the right shape after weight loss. A visible node can often be seen, and a centimeter-scale mask error would not produce a 1 mm spine match. The limitation is specifically about disease that imaging cannot show.

### Q4
Stem: Rectal gas on a prostate cone-beam CT displaces the gland and stretches the rectal wall. The fiducials are shifted back to the planned coordinates with a single couch translation. Which part of the discrepancy can that translation not remove?
A. The centroid shift of the fiducials
B. The deformed shape of the rectum and the changed distance from prostate to rectal wall
C. A 2 mm left-right translation of the whole patient
D. The recorded translation values in the shift log
Answer: B
Objective: II.6
Why: Answer B. A couch correction is a rigid transform of the whole patient. Once the fiducials are back at their planned coordinates, the translation component of the setup is done. The gas bubble still deforms the rectum. That shape change is not a couch degree of freedom, so the planned rectal DVH is no longer the organ on the couch. This is the central limit of image-guided shifts: they do not perform deformable adaptation. Left-right translation and the shift log are things the couch and the software do handle.

### Q5
Stem: A lung SBRT tumor is visible on cone-beam CT and has moved 1 cm relative to the carina since the planning CT. The bony chest matches within 2 mm. A protocol says to match the tumor. Which limitation of "match the bones" is this case demonstrating?
A. Bone match cannot localize a soft-tissue target that moves independently of the bones
B. Cone-beam CT cannot show a lung tumor under any circumstances
C. A 1 cm tumor shift is below the resolution of kilovoltage imaging
D. Matching the tumor would violate the rule that image guidance may only use the spinal canal
Answer: A
Objective: II.6
Why: Answer A. The carina, the vertebrae, and a peripheral lung tumor are not one rigid object. A bone match can look excellent and leave the tumor a centimeter off, which for SBRT is outside a typical internal margin if the planning CT already froze a breathing phase. The cone-beam CT is what makes the independent motion visible; many lung tumors can be matched directly. The limitation being illustrated is the surrogate, not a failure of the image to exist.
