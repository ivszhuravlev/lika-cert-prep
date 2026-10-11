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
