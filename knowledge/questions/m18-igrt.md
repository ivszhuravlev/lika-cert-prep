# Module 18 — IGRT

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Treatment Verification

### Q1
Stem: A prostate patient has three intraprostatic fiducials. Daily imaging is a pair of orthogonal kilovoltage radiographs. The bony pelvis matches the digitally reconstructed radiographs within 1 mm, but the fiducials sit 7 mm posterior to their planned position. Which match should drive the couch shift?
A. The bony pelvis, because bone is a more stable surrogate than markers implanted in the gland
B. The fiducials, because the prostate can move relative to the pelvic bones
C. The average of the bone shift and the fiducial shift
D. Neither; orthogonal kV images cannot show fiducials, so the disagreement is an artifact
Answer: B
Objective: II.6
Why: Answer B. Rectal filling and bladder volume move the prostate relative to the pelvic skeleton, often by several millimeters, predominantly anterior-posterior. Implanted fiducials are a surrogate for the gland itself. A bone match that leaves the markers 7 mm off will treat the volume that was planned around the old prostate position. Averaging the two shifts satisfies neither anatomy. D is wrong: high-Z fiducials are exactly what a kilovoltage radiograph is good at showing. What that pair cannot show is soft tissue and a full three-dimensional rotation.

### Q2
Stem: Which imaging method can show the soft-tissue prostate, lung tumor, or bladder on the treatment couch, rather than only bone, a surface, or implanted metal?
A. A surface-guided infrared camera
B. Megavoltage portal images alone, compared with digitally reconstructed radiographs
C. Cone-beam CT acquired on the treatment unit
D. A single anterior kilovoltage radiograph
Answer: C
Objective: I.8
Why: Answer C. Cone-beam CT reconstructs a volumetric dataset from projections taken on the linac, so soft-tissue boundaries, bladder filling, and many lung tumors are visible. A surface camera (A) sees the skin only. A megavoltage portal (B) is a projection with poor soft-tissue contrast and is compared with a DRR, which is a bone and aperture check. A single kV radiograph (D) collapses the patient into one plane and does not separate soft-tissue organs in depth. Cone-beam CT still has scatter, a limited field of view, and Hounsfield numbers that are not a substitute for a planning CT.

### Q3
Stem: A department uses an online correction protocol for lung SBRT and an offline protocol for a palliative whole-brain course. What does "online" mean in this context?
A. The shift is measured and applied before the beam is delivered that day
B. Images are reviewed the next morning and a systematic offset is applied to future fractions only
C. The record-and-verify system recomputes the monitor units from the cone-beam CT
D. The patient is treated on the planning CT coordinates with no measurement
Answer: A
Objective: II.6
Why: Answer A. Online image guidance means the localization images are acquired at the machine, the shift is decided, and the couch is moved before that fraction is treated. Offline review looks at images after the fact (or before the next fraction) to correct a systematic trend; it does not fix the fraction already delivered. C attributes dose calculation to the verify system and to a cone-beam CT, which is not what online correction does. D is treatment without localization.

### Q4
Stem: A surface-guided system reports the chest wall within 1 mm of the reference surface during a breast setup. The internal mammary nodes are part of the target. What has the surface system verified?
A. The position of the skin surface relative to the cameras
B. The position of the internal mammary nodes relative to the plan
C. That the monitor units and energy match the plan
D. That respiratory motion will stay correlated with the surface for the whole beam-on time, including if the patient tenses
Answer: A
Objective: II.6
Why: Answer A. Surface guidance tracks the external contour with optical cameras. It does not image the internal mammary chain, which lies beside the sternum, deep to the skin. A good surface match is useful for setup and for breath-hold coaching, but the relationship between skin and an internal target can change if the patient changes posture or muscle tension. It also does not check energy, monitor units, or multileaf apertures. Those are record-and-verify and machine checks, not a surface image.

### Q5
Stem: For a stereotactic intracranial plan with a 1 mm PTV margin, the department's action level is 1 mm. For a palliative parallel-opposed pair with a 1 cm margin, the action level is 5 mm. A 3 mm shift is measured on both patients. Which statement is consistent with those protocols?
A. Both shifts must be corrected, because every measured offset is a miss
B. Neither shift is corrected, because 3 mm is below a universal 5 mm tolerance
C. The stereotactic shift is corrected because 3 mm exceeds its 1 mm action level; the palliative shift may be left within its 5 mm action level
D. The palliative shift is the one that must be corrected, because the field is larger
Answer: C
Objective: II.6
Why: Answer C. An action level is a clinic rule tied to the margin and the consequence of a miss, not a law of physics that is the same for every plan. A 3 mm residual is three times the entire PTV margin of the stereotactic case, so that couch is moved. The same 3 mm sits inside the 5 mm action level of a large palliative field whose margin is 1 cm. B invents a universal tolerance. D reverses the priority: large fields are more forgiving of a small shift, not less.

### Q20
Stem: Each day’s cone-beam is matched to the previous day’s cone-beam. Those two images agree within 1 mm. The planning CT is not in the match. What can that agreement hide?
A. A drift of the isocenter away from the anatomy the dose was calculated on
B. A wrong energy, which the cone-beam match measures directly
C. A reset of the prescription dose
D. Nothing; the latest cone-beam replaces the planning CT as the reference
Answer: A
Objective: II.6
Why: Answer A. The reference for a cone-beam match is the planning CT in the simulated orientation. Matching today to yesterday lets a small residual walk the isocenter off the planned anatomy. The image does not read linac energy and it does not rewrite the prescription.

### Q21
Stem: The approved shift is 0.7 cm to the patient’s left. The couch is moved 0.7 cm to the patient’s right. What is the size of the geometric error?
A. 0 cm, because both moves are on the left-right axis
B. 0.7 cm, because the magnitude matched the plan
C. 1.4 cm, the intended shift and the applied shift added in opposite directions
D. A change in CT slice thickness only
Answer: C
Objective: II.6
Why: Answer C. The correct move and the opposite move are each 0.7 cm, so the patient is 1.4 cm from the planned position. A matching number with the wrong sign is twice the intended correction. Slice thickness is a scan parameter, not this error.

### Q22
Stem: A breast plan was simulated in deep-inspiration breath hold. At treatment the surface trace is stable on the free-breathing average, and the beam is delivered at that level. What has the trace confirmed?
A. That any stable surface is the simulated breath-hold anatomy
B. The position of the free-breathing surface, which is not the inspiration level the plan used
C. The monitor units
D. That respiratory motion has stopped for the rest of the course
Answer: B
Objective: II.6
Why: Answer B. Breath-hold and gating have to reproduce the simulated inspiration level or phase. A stable trace on the free-breathing average is a different chest position from the planning scan. Surface guidance does not check monitor units, and one stable reading does not end motion for later fractions.

### Q23
Stem: Daily kilovoltage images match three prostatic fiducials to their planned coordinates. Which statement fits that match?
A. The markers are the GTV, so the gland is covered once the markers agree
B. The match has also confirmed the energy and the monitor units
C. Fiducials are invisible on kilovoltage images, so the match cannot be real
D. The match localizes the markers; the gland is inferred from them, and a marker that has migrated no longer stands for the target
Answer: D
Objective: II.6
Why: Answer D. A fiducial is a surrogate, not the GTV. If a marker migrates, a perfect match to that marker puts the isocenter on the marker and off the gland. High-Z markers are visible on kilovoltage radiographs. Energy and monitor units are record-and-verify parameters, not a result of the image match.

### Q24
Stem: Machine QA lists a 1 mm geometric tolerance for the imager. A stereotactic plan uses a 2 mm PTV margin and a departmental action level of 1 mm. How are those numbers related?
A. The imager tolerance is a test that the imaging isocenter agrees with the treatment isocenter; the action level is the clinical rule for this plan
B. The three numbers are interchangeable labels for one tolerance
C. The PTV margin is the action level, so a 2 mm residual is inside the rule
D. Passing the imager QA sets the PTV margin to zero
Answer: A
Objective: II.6
Why: Answer A. A TG-142-style geometry test asks whether the imager and the machine isocenter coincide. The action level is the clinic’s rule for how large a shift must be corrected on this plan. The PTV margin is the volume grown for residual uncertainty. Passing one of those checks does not rewrite the others.

### Q25
Stem: A nasopharynx match proposes a 2° pitch and no translation. A supraclavicular node is 20 cm inferior to the match point. Using Δ ≈ rθ with 2° = 0.0349 rad, about how far does that pitch move the node, and what can a translation-only couch do?
A. About 0.3 mm, so the pitch can be ignored on every target length
B. 20 cm, the full distance to the node
C. About 7 mm, and a couch that cannot rotate cannot apply that pitch
D. 2 mm at any distance, because 2° means 2 mm
Answer: C
Objective: II.6
Why: Answer C. 20 cm × 0.0349 = 0.70 cm, about 7 mm at the node. That is a real displacement at the end of a long field. A three-degree-of-freedom couch can apply translations only. The pitch is corrected by a couch that can rotate, within protocol, or the patient is reset. The angle in degrees is not a shift in millimeters.

### Q26
Stem: A cone-beam CT match uses the anatomy named in the protocol. Bladder filling, rectal volume, and the body contour agree with the planning CT. The rigid shift is inside the departmental action level for this site. What is the appropriate next step?
A. Complete the localization the policy allows for an in-tolerance shift, and treat, without calling the physician for this shift alone
B. Call the physician for every cone-beam shift, including a shift inside the action level
C. Treat on the tattoos and discard the image, because an in-tolerance shift means the cone-beam was optional
D. Calculate the fraction on the cone-beam CT with the planning-CT density table before treating
Answer: A
Objective: II.6
Why: Answer A. The action level is the clinic’s rule for what the treating team may finish when the anatomy still matches the plan. Inside that level, on the required surrogate, a rigid correction is localization. A nonzero shift is not automatically a physician call. Discarding the image leaves the measured offset unaddressed. A cone-beam is not the commissioned density set for a dose calculation.

### Q27
Stem: Under the same policy, the cone-beam shows a rectum full of gas, the prostate displaced relative to the pelvic nodes, and a bladder much emptier than the planning CT. One translation can still drive the bony residual inside the site’s action level. What is required?
A. Treat, because a bone residual inside the action level clears the fraction
B. Hold the beam and call the physician. A rigid shift that centers the bone does not restore the filling or put both the prostate and the nodes back on the plan
C. Average the bone shift and the prostate shift until the displayed number is inside the action level, then treat
D. Change the energy so the filling difference drops out of the match
Answer: B
Objective: II.6
Why: Answer B. The action level limits the rigid correction the team may apply when the patient still matches the plan. Gas, an empty bladder, and a prostate that has moved relative to the nodes are a different geometry from the planning CT. Forcing the bone number under the limit does not repair that. Averaging two surrogates satisfies neither. Energy does not move bowel or bladder.

### Q28
Stem: A clinic uses a no-action-level (NAL) offline protocol for a palliative course and an online cone-beam correction for stereotactic lung. What does NAL do?
A. It estimates the systematic setup error from an initial set of images and applies that correction on later fractions, leaving today’s random residual until an online shift
B. It recalculates monitor units from the cone-beam before every fraction
C. It is the name for a same-day replan on an MR-linac
D. It ignores systematic error and corrects only the random error of the current fraction before beam-on
Answer: A
Objective: II.6
Why: Answer A. NAL is offline. The mean of an initial set of setup images estimates the systematic error, and that mean is applied to subsequent fractions with no threshold. The fraction already imaged is not moved for its own random residual before beam-on. Online correction is the move before the beam. NAL does not recompute monitor units, and it is not online plan adaptation. Option D reverses which component NAL targets.

### Q29
Stem: Extended NAL (eNAL) is added because the setup is drifting over the course. What does the extension change?
A. The systematic estimate is updated from later images, and the updated correction applies to future fractions
B. eNAL turns the offline protocol into a same-session adaptive replan
C. eNAL sets the cone-beam dose to zero
D. eNAL replaces the planning CT with yesterday’s cone-beam as the match reference
Answer: A
Objective: II.6
Why: Answer A. eNAL keeps the offline correction and refreshes the estimate of the systematic error, so a trend is not frozen at the first measurement. The new correction is for later fractions. It does not reoptimize the dose on the table, it does not cancel imaging dose, and the match reference remains the planning CT.

### Q30
Stem: Daily kilovoltage cone-beam CT is required for a long fractionated course. Which statement about the imaging dose is correct?
A. Kilovoltage imaging dose is zero because the beam is not the treatment energy
B. Each cone-beam deposits dose, the daily scans accumulate, and that dose is separate from the therapeutic prescription
C. One cone-beam delivers one treatment fraction, so the prescription is reduced by the number of scans
D. Imaging dose is deposited only when the match exceeds the action level
Answer: B
Objective: II.6
Why: Answer B. A kilovoltage cone-beam is ionizing radiation. Repeating it every fraction adds dose. That dose is small next to a therapeutic fraction, and it is not the prescribed tumor dose, so it is neither ignored as zero nor subtracted from the prescription one scan at a time. The dose is deposited when the scan is acquired, independent of how large the shift is.

## IGRT Mini-Quiz

### Q1
Stem: Daily cone-beam CT for a pancreas SBRT patient can be matched on the vertebral body or on a stent and soft tissue near the tumor. The spine match is 1 mm. The stent match is 8 mm superior. Which match agrees with the target?
A. The spine, because a vertebral body is rigid and the stent can be ignored
B. The stent and the soft tissue next to the tumor; the spine is a poor surrogate when the target has moved along the spine
C. The midpoint, 4 mm superior, because both surrogates are equally valid
D. The spine for the superior-inferior direction and the stent for the lateral direction only
Answer: B
Objective: II.6
Why: Answer B. Image guidance is only as good as the surrogate. The vertebral body can be stable while the pancreas and a stent move with respiration, bowel, and day-to-day position. An 8 mm disagreement means a spine-based shift would set up the bones and miss the target the plan was drawn around. Splitting the difference (C) leaves several millimeters on the target. Using each surrogate for a different axis (D) has no anatomical basis when the same organ motion produced the shift.

### Q2
Stem: A six-degree-of-freedom couch can correct pitch, roll, and yaw as well as translations. A long cervicothoracic spine volume is matched at its center, and the software offers a 3 degree pitch. Why might that rotation be a bad correction even though the math is available?
A. Six-degree-of-freedom couches cannot rotate, so the offer is a display error
B. A rotation that centers the middle of a long target swings the superior and inferior ends off the planned cord position
C. Pitch corrections automatically recompute the multileaf pattern for the new angle
D. Yaw, pitch, and roll are the three translations, so a 3 degree pitch is a 3 mm shift
Answer: B
Objective: II.6
Why: Answer B. A rigid rotation is correct for a small, nearly spherical target if the whole volume truly rotated. Along a long spine target, the same pitch that fixes the central slice moves the ends in the opposite anterior-posterior direction. Those ends can include cord. Many clinics re-immobilize rather than apply a large rotation to a long target, or they match with an emphasis on the cord. A is wrong because a six-degree-of-freedom couch is built to rotate within mechanical limits. C is wrong because a couch rotation does not rewrite the planned apertures. D confuses degrees of rotation with millimeters of translation.

### Q3
Stem: Megavoltage cone-beam CT on a helical tomotherapy unit is used for setup. Compared with a kilovoltage cone-beam CT on a C-arm linac, what is a known imaging limitation of the megavoltage cone beam or megavoltage fan-beam CT?
A. It cannot be acquired in the treatment room
B. Soft-tissue contrast is poorer, and the imaging dose per scan is generally higher
C. It shows only the skin surface
D. It is acquired with the treatment multileaf collimator fully closed, so it does not image the patient
Answer: B
Objective: I.8
Why: Answer B. Megavoltage photons interact mainly by Compton scatter, so bone-to-soft-tissue contrast is weaker than with kilovoltage imaging, where the photoelectric effect still helps separate high-Z bone from tissue. Megavoltage CT also deposits more dose per usable image. It is still an in-room volumetric image of the patient (A and D are false) and it is not a surface camera (C). It is useful for alignment, especially when high-Z metal would wreck a kilovoltage cone-beam CT, but it is a weak tool for subtle soft-tissue targets.

### Q4
Stem: A patient is localized with cone-beam CT immediately before a 12-minute volumetric modulated arc. There is no surface tracking, no fiducial tracking, and no intrafraction imaging. Which uncertainty remains even if the pre-beam match was perfect?
A. Motion and relaxation that occur after the scan, during the arc
B. The wrong energy having been loaded in the plan, which the cone-beam CT measures directly
C. Whether the planning CT Hounsfield units were calibrated, which the cone-beam match corrects
D. The prescription dose, which is reset by the couch shift
Answer: A
Objective: II.6
Why: Answer A. A pre-treatment image is a snapshot. During a long arc the patient can relax, breathe differently, or shift inside the mask. Without another measurement during the beam, that intrafraction motion is not corrected. The cone-beam CT does not read the linac energy, does not recalibrate the planning CT density table, and does not change the prescribed dose. Those are plan, commissioning, and prescription issues.

### Q5
Stem: Orthogonal megavoltage portal images are compared with digitally reconstructed radiographs for an anterior-posterior and posterior-anterior lung plan. The carina and clavicles match. What has this check actually confirmed?
A. That the tumor, which is not visible on the portal image, is inside the aperture
B. That the bony projection and the field outline agree with the planned beam's-eye view within the limits of a two-dimensional megavoltage image
C. That the delivered dose distribution matches the planned dose distribution
D. That soft-tissue rotation out of the axial plane has been fully measured
Answer: B
Objective: II.6
Why: Answer B. A portal-to-DRR comparison checks that the beam aperture and the bony anatomy projected along that beam agree with the plan. It is a geometry check of that two-dimensional view. A lung tumor often is not visible at megavoltage energy, so a bone match does not prove the tumor is centered (A). The image is not a dose measurement (C). Two orthogonal projections still leave limited information about pitch and roll of soft tissue (D).
