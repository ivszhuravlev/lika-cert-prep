# Module 28 — Adaptive radiotherapy

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Adaptive Radiotherapy

### Q1
Stem: A head-and-neck patient has lost 8 kg by week 4. The mask is loose, the separation at the isocenter has dropped by 1.5 cm, and the parotids have moved medially into the high-dose region. Daily cone-beam shifts of 3 to 5 mm still leave the mask bridging over the neck. Which response matches adaptive radiotherapy rather than ordinary image guidance?
A. Continue the original plan and keep applying a rigid couch shift, because a shift recenters any changed anatomy
B. Replan on anatomy that represents the current separation and parotid position, with physician approval of the new target and organ doses
C. Increase the daily shift action level so the loose mask is no longer flagged
D. Renormalize the original monitor units upward by 8% to account for the weight loss, without a new contour set
Answer: B
Objective: III.7
Why: Answer B. A rigid shift recenters a chosen landmark. It does not rebuild a plan when the body habitus and the parotids have changed shape. Adaptive radiotherapy means a new plan (offline between fractions, or online on the couch) based on the anatomy of the day or of that week, after the physician agrees the targets and constraints are still the ones intended. Raising the action level (C) hides the problem. A percent rescaling of the old monitor units (D) does not move the parotids back out of the high dose and does not correct a mask that no longer fits.

### Q2
Stem: Which pair correctly separates offline adaptive radiotherapy from online adaptive radiotherapy?
A. Offline replanning happens between fractions from a new planning dataset; online replanning happens while the patient is immobilized on the treatment unit, before that fraction's adapted beam is delivered
B. Offline means the beam is on during the replan; online means the replan is mailed to the next department
C. They are identical; the only difference is whether the multileaf collimator is binary
D. Online adaptation avoids physician review because the cone-beam CT is the legal prescription
Answer: A
Objective: III.7
Why: Answer A. Offline adaptation uses information from treatment (weight loss, tumor shrinkage, a new CT) to build a revised plan that will be used on a later fraction. Online adaptation, as on an MR-linac or an adaptive cone-beam workflow, recontours and reoptimizes while the patient is on the table and treats the new plan in that same session. The time pressure is higher online, so contour checks and a simple independent dose check have to be fast, but they are not optional. B reverses the language. C and D remove review steps that both workflows still require: the adapted plan has to represent the physician's intent.

### Q3
Stem: A mid-course cone-beam CT is proposed as the dataset for a new photon dose calculation with no Hounsfield correction, no override, and a field of view that cuts off the shoulders. The external contour is clipped at the bore. Why is that dataset not ready for a replan?
A. Cone-beam Hounsfield units are accurate enough that a truncated body contour does not change scatter or beam path
B. Scatter, truncated anatomy, and uncorrected cone-beam Hounsfield units make the density and the body contour unreliable for dose; a corrected dataset or a new planning CT is required
C. A clipped external contour only affects electron plans, not photons
D. Missing shoulders reduce the calculation time and therefore improve accuracy
Answer: B
Objective: III.7
Why: Answer B. A treatment-planning dose engine needs a complete external contour and a density grid tied to a calibrated curve. Cone-beam CT is formed with more scatter and a different spectrum than a planning CT, so its numbers are not that calibration. A field of view that amputates the shoulders assigns whatever lies outside the reconstruction (often the bore or nothing) to the beam path and gets the missing-tissue scatter wrong. Photons and electrons both need the real contour. A proper adaptive dataset is a new planning CT, a synthetic CT, or a cone-beam CT that has been validated for dose with overrides and a completed body contour.

### Q4
Stem: An online adaptive session on an MR-linac produces a synthetic CT for dose calculation. The automated organs are edited, but the physician has not looked at the adapted target. The optimizer has already met the dose constraints on the unedited target. What is the correct status of this plan?
A. Deliverable, because a constraint report is the prescription
B. Not deliverable until the physician has confirmed the target of the day and the dose that will actually be given
C. Deliverable if the synthetic CT has 10 or more Hounsfield values
D. Not deliverable only when the original plan was three-dimensional conformal; adaptive intensity-modulated plans are exempt
Answer: B
Objective: III.7
Why: Answer B. Adaptation changes the geometry the prescription is applied to. Meeting a cost function on a target nobody has accepted is not approval. The physician owns the target and the decision to treat the adapted dose. A synthetic CT is only the density map that lets the MR session calculate dose; the count of gray levels does not authorize treatment. The same review applies to conformal and modulated adaptive plans.

### Q5
Stem: Daily rectal gas systematically pushes a prostate anteriorly by about 8 mm, and the gas volume changes shape every day. The clinic's only tool is a pre-beam rigid couch shift to fiducials, with no replanning. Which limitation remains?
A. None; a fiducial shift removes both the translation and the deformation caused by gas
B. The shift can recenter the fiducials, but the rectal wall and bladder still do not match the planned shapes, so the planned DVH is not the anatomy being treated
C. The shift recenters the bones and intentionally leaves the fiducials 8 mm off
D. Gas is invisible on cone-beam CT, so the 8 mm figure cannot be real
Answer: B
Objective: III.7
Why: Answer B. Image-guided translation puts the markers back at the planned coordinates if the markers still represent the gland. It does not deflate the rectum or restore the planned distance from prostate to rectal wall. On a day with a large gas pocket the rectal wall is stretched into a different position relative to the high dose, even when the centroid of the prostate is correct. That is the gap adaptive replanning is meant to address, and it is also why a full-to-empty rectal protocol is used in the first place. A overstates a rigid shift. C would be a bone match, which is the wrong surrogate here. D is wrong: gas is obvious on cone-beam CT.

### Q20
Stem: One workflow recontours and reoptimizes a lung plan on the MR-linac and delivers that plan before the patient gets off the couch. Another workflow sends a head-and-neck patient back to the CT simulator on Friday and starts the revised plan the next Wednesday. Which assignment is correct?
A. Both are offline, because a physician reviews both
B. The MR-linac fraction is offline and the Wednesday start is online, because only a CT simulator can be online
C. The MR-linac fraction is online adaptation; the Wednesday start is offline adaptation
D. Neither is adaptation; adaptation means a daily rigid couch shift and nothing else
Answer: C
Objective: III.7
Why: Answer C. Online adaptation creates and delivers the new plan in the same session, with the patient immobilized. Offline adaptation builds the new plan between fractions and starts it on a later day. Review is required in both, so review does not define the category. The device does not either: an MR-linac session is online because of when the new plan is treated, and a simulator rescan used next week is offline. A couch shift without a new dose distribution is image guidance.

### Q21
Stem: By week 4 a head-and-neck mask bridges a gap over the neck. Separation at isocenter is 1.5 cm smaller than at simulation, and both parotids have moved medially into the high-dose region. The couch is shifted 4 mm to center the cervical spine. Which problem remains?
A. None; a spine match restores separation and puts the parotids back where they were planned
B. The thinner body contour and the medial parotids; a rigid shift cannot rebuild a mask that no longer fits or a shape that has changed
C. Only the beam energy, which the shift changes from 6 MV to 15 MV
D. The shift is illegal above 3 mm, so the 4 mm correction should be reversed and the original isocenter treated
Answer: B
Objective: III.7
Why: Answer B. Image guidance can recenter a chosen landmark. It does not fill a 1.5 cm gap under a bridging mask, and it does not move parotids that have migrated into the high dose back to their planned positions. Those are a habitus change and a deformation. Energy is not selected by a couch coordinate. A 4 mm shift is not, by itself, a reason to undo a correct translation. The remaining problem is the shape change the translation cannot fix, which is what a replan on the current anatomy is for.

### Q22
Stem: A dosimetrist calculates a replacement photon plan on a mid-course cone-beam CT. The field of view clips the shoulders, the external contour stops at the reconstruction, and the planning-CT Hounsfield calibration is applied with no validation and no overrides. What is wrong with that dataset?
A. Nothing; cone-beam numbers share the simulator calibration, and a missing shoulder does not change scatter
B. The clip is an advantage, because a smaller field of view raises the accuracy of every Hounsfield unit
C. The dataset is acceptable when the beam is 6 MV, because megavoltage dose does not use the body contour
D. It is not a planning CT; scatter, an unvalidated density curve, and a truncated external contour make the dose unreliable
Answer: D
Objective: III.7
Why: Answer D. A planning calculation needs a complete external contour and densities tied to a calibrated curve. Cone-beam CT is formed with more scatter and a different spectrum, so its numbers are not the simulator curve unless that relationship has been validated. Tissue outside a truncated field of view is missing from the beam path and from the scatter. Photons use that contour. A smaller field of view does not repair the CT numbers.

### Q23
Stem: An online adaptive session has edited the organs at risk, and the optimizer has met every loaded constraint on the target drawn by the autocontour. The physician has not looked at that target. The patient has been on the table for 20 minutes. What is the correct status of the plan?
A. Not deliverable until the physician confirms the target of the day and the dose that will actually be given
B. Deliverable, because a met constraint report is the prescription
C. Deliverable, because time on the table replaces target review
D. Deliverable for an intensity-modulated plan; only a 3D conformal adaptive plan needs the target checked
Answer: A
Objective: III.7
Why: Answer A. Adaptation applies the prescription to a new geometry. A cost function met on a target nobody has accepted is not approval. The physician owns the target and the decision to treat the adapted dose. Elapsed time raises the pressure and does not remove the check. The same review applies to conformal and modulated adaptive plans.

### Q24
Stem: Offline adaptation is selected for head-and-neck weight loss. The new planning CT and the revised plan will not be ready for four days. The current plan still covers the target and still meets the cord limit on the images reviewed today. What is the appropriate treatment until the new plan is checked?
A. Stop all treatment, because noticing a geometry change cancels the prescription the same day
B. Continue the current plan while the offline replan is prepared, then switch when the new plan is approved
C. Treat the next four fractions on the raw cone-beam with the old monitor units and no density check
D. Call the four-day replan online adaptation, because any mid-course replan is online by definition
Answer: B
Objective: III.7
Why: Answer B. Offline adaptation is built between fractions and starts on a later day. There is time for contours, an independent calculation, and ordinary plan QA. If the current plan is still safe, the patient stays on it until the replacement is ready. Stopping without a clinical reason is not what that timeline requires. Pasting old monitor units onto an uncorrected cone-beam is not a dose calculation. A plan that starts days later is offline, not online.

### Q25
Stem: The same week, a prostate patient has one fraction with a 3 mm translation and organs that otherwise match the plan, corrected by the couch. A head-and-neck patient has a mask that bridges the neck, 1.5 cm of separation loss, and parotids medial to their planned position on repeated cone-beams. Which patient has the problem that adaptive radiotherapy is for?
A. The prostate patient, because every couch shift is a replan
B. Both, because image guidance and adaptation are the same action
C. Neither; parotids cannot move relative to a planning target volume
D. The head-and-neck patient; the shape change is systematic, and a rigid shift cannot restore the mask fit, the separation, or the parotid position
Answer: D
Objective: III.7
Why: Answer D. A small translation with organs otherwise matching is image guidance. Margins and a couch shift are what that fraction needs. The head-and-neck findings are a changed shape: immobilization that no longer represents the patient, less tissue in the beam, and organs at risk that have entered the high dose. That is a reason to replan on current anatomy. Parotids do migrate medially with weight loss. Calling every shift a replan erases the distinction.

### Q26
Stem: Fifteen of thirty fractions have already been delivered. An offline replan will treat the remaining fractions on a new CT. The new beams still enter across the spinal cord. What has to be included when the cord dose of the adapted course is judged?
A. Only the remaining fifteen fractions; dose from the first plan is discarded when the CT changes
B. A 1.5 cm couch shift in place of any cord sum
C. The cord dose already delivered plus the cord dose the new plan will add
D. The cone-beam Hounsfield units of the original simulation, reused as the density of the new patient
Answer: C
Objective: III.7
Why: Answer C. Previous fractions have already deposited dose. If the new plan still crosses a serial organ, the adaptation is also a re-treatment problem: the total includes what was given and what remains. A new CT does not erase gray already absorbed. A couch shift does not add those distributions. Cone-beam numbers from the old scan are not a density map of the patient being planned now.

### Q27
Stem: Which dataset is appropriate for the dose calculation of an adapted photon plan?
A. A new planning CT, or a cone-beam or synthetic CT whose densities and external contour have been validated for dose
B. Any cone-beam, using the simulator Hounsfield curve, including scans that cut off the shoulders
C. The original planning CT with the monitor units scaled by the percent of weight lost, and no new contours
D. A cone-beam declared to be a planning CT by relabeling it, with no density check
Answer: A
Objective: III.7
Why: Answer A. The calculation needs a complete body contour and a density grid that matches a calibrated relationship. A new planning CT satisfies that. A cone-beam or a synthetic CT can be used only after that relationship and the contour have been shown to support dose. An unvalidated, truncated cone-beam does not become a planning CT by applying the simulator curve or by changing its name. Scaling the old monitor units for weight loss does not move deformed anatomy and does not rebuild the plan.
