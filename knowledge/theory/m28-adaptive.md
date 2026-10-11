# Module 28. Adaptive Radiotherapy

Adaptive radiotherapy means the plan changes because the patient’s geometry changed. A daily couch shift that puts today’s anatomy back inside yesterday’s PTV is image guidance. A new dose distribution calculated on new anatomy is adaptation.

## Adaptive Radiotherapy

**MDCB objectives:** III.7, II.5, II.6

**What the exam expects**

You can define offline adaptation and online adaptation, and you can name the geometry changes that justify a replan. You know a rigid shift cannot repair deformation, and you know an adapted contour and an adapted plan still need a human check. You do not invent a universal action level in millimeters. Confirm that threshold in the departmental adaptive protocol.

**Core facts**

The original plan is a dose calculation on the simulation anatomy, plus margins. The internal margin and the setup margin (ICRU 62) were supposed to cover random motion and random setup error. Image guidance removes a large part of the setup error every day. What remains, and what margins do not fix, is a systematic change in shape:

- Weight loss in the head and neck, so the mask no longer fits and the parotids and the cord move relative to the target
- Tumor shrinkage that leaves the original high-dose region covering unnecessary tissue, or that moves a target off a serial organ in a way you can now spare
- A postoperative seroma or a breast contour that swells or drains
- A bladder or rectum protocol that is systematically different from simulation, not just noisy day to day
- Pleural fluid, bowel gas patterns that are new and stable, or an arm position that does not match the scan
- A rectal spacer that has been absorbed, so the gap the plan relied on is gone

Offline adaptation uses images acquired at treatment, reviews them after the fraction, and builds a new plan that starts on a later day. There is time for contours, planning, a second calculation, and ordinary plan QA. The patient continues on the old plan, if it is still safe, until the new plan is ready. This is the right pace for weight loss over a week.

Online adaptation builds and delivers a new plan while the patient is on the table, in that session. Cone-beam or MR-linac images are contoured, a plan is optimized or adapted, and some form of on-table check is done before beam-on. The time pressure is the risk. Speed does not remove the need to look at the target, the cord or the rectum, the fraction dose, and the identity of the plan. Autocontouring and autoplanning are often part of the online workflow. Both still require human review (modules 29 and 30).

A replan is warranted when the geometry change makes the current dose distribution the wrong distribution: target outside the PTV in a way a shift cannot restore, an OAR now inside the high dose, or a systematic change large enough that the original margins no longer describe the patient. A 3 mm random translation with the organs otherwise matching is an image-guidance shift, not a new plan. The number that separates those two statements is a protocol number. Confirm it in the adaptive policy. Do not memorize a single millimeter cutoff as universal.

The new plan uses the same ICRU logic on the new anatomy. Someone redraws or edits the GTV and CTV. The PTV and PRV margins are reapplied under the protocol, not copied blindly if the motion or the setup method has also changed. Previous fractions have already deposited dose. If the new plan overlaps that dose in a serial organ, the adaptation is also a re-treatment problem. Account for what was delivered. The arithmetic of equivalent dose is in the radiobiology module. The decision to sum dose through a deformable registration is only as good as the registration (TG-132). A folded or sliding warp will invent a cord dose.

Online systems may offer a “warm start” from yesterday’s plan or a full re-optimization. Either way, check:

- The contour that drives the optimizer, especially small serial structures and the external contour
- The daily image quality: truncation, artifact, and, for MR-guided treatment, distortion
- The prescription for this fraction, not the original course total pasted into one day
- The independent check the departmental online procedure requires
- The record of what was actually delivered, archived so the course can be reconstructed

Triggers that should make you stop and ask about a replan, even offline: a mask that rocks, a systematic cone-beam shift at the action level every day, weight change the clinic has chosen as a threshold, visible tumor response, or a spacer or a prosthesis whose position no longer matches the plan. Confirm the threshold values in the protocol.

Adaptive planning does not relax target definition. A CTV edited to chase a noisy cone-beam every day can shrink the clinical volume for the wrong reason. The physician owns the target. The dosimetrist’s job is to show the geometric change clearly and to produce a dose that matches the decision.

**Formulas**

The rotation arithmetic from image guidance is often what shows that a rigid correction is not enough. A 15 cm target, 3° of uncorrected rotation:

3° = 0.0524 rad

Displacement at the end ≈ 15 × 0.0524 = 0.79 cm

If that 8 mm is deformation rather than a true rigid rotation (the neck flexed, the shoulders dropped), a six-degree couch correction that forces the bones to match will misplace the soft tissue. Adaptation recalculates on the new shape. A couch rotation only pretends the shape is unchanged.

Dose already delivered, conceptually: if 15 of 30 fractions were given and a new plan will finish the course, the new plan is designed for the remaining 15 fractions plus the anatomy now, and the serial-organ total includes the first 15. Write the addition in EQD2 only when the fraction size changed and the stem asks. If both plans are 2 Gy fractions, the physical doses add directly.

**Traps**

- Calling every daily shift adaptive radiotherapy.
- Running an online plan with unchecked autocontours because the patient is on the table.
- Deforming the dose from week 1 onto week 4 and believing the sum in a low-contrast neck or a sliding lung.
- Replanning a random bladder filling that the drinking protocol will not repeat tomorrow, and missing a true systematic weight loss.
- Forgetting prior dose when the new beams still cross the cord.
- Using cone-beam Hounsfield units for the new calculation without a validated density relationship. CBCT is not a planning CT.

**Sources**

- ICRU 62, internal margin versus setup margin, which is the boundary between motion you planned for and geometry you did not
- AAPM TG-132, deformable registration used to accumulate the old dose on the new anatomy
- The departmental online and offline adaptive procedures, for action levels and on-table checks. Confirm the numbers there.
