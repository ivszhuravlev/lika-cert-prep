# Module 30 — Autocontouring

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Automatic Segmentation

### Q1
Stem: An atlas-based autocontour deforms a library patient's contours onto today's CT. Today's patient is postoperative: the tumor has been resected and the cavity is full of fluid and clips. The atlas patient had an intact gross tumor. Where does this method most often fail?
A. It fails least in the surgical cavity, because deformation is most accurate across missing tissue and metal
B. It fails in anatomy the atlas does not contain: the cavity, the clips, and distorted organs next to the resection, while unmodified bone may still look reasonable
C. It fails only on the external contour, never on organs at risk
D. It cannot run unless the atlas and the patient have the same monitor units
Answer: B
Objective: III.10
Why: Answer B. Atlas methods warp a previously contoured scan onto the new scan and carry the contours along. The warp assumes the two bodies are versions of the same anatomy. A resection, a fluid cavity, and metal are not in the atlas, and deformable registration is weakest exactly at air, clips, and sliding or missing tissue. Bone far from the cavity may still match. The external contour can also be wrong, but it is not the only failure, and monitor units have nothing to do with segmentation.

### Q2
Stem: A deep-learning model draws both parotids, the cord, and the mandible on a contrast CT. It was trained on non-contrast scans. The vessels enhance brightly and the model labels a vessel as an extra lymph node region that the protocol does not treat. What is the correct use of this output?
A. Accept it; a deep-learning contour is a physician target by definition
B. Treat it as a draft: delete the false node, check laterality and every slice, and do not let a contrast-phase mistake become a target
C. Switch the CT to MRI units so the labels become valid without review
D. Keep the false node because models are not allowed to be edited
Answer: B
Objective: III.10
Why: Answer B. A model copies the patterns it was trained on. Contrast changes Hounsfield numbers in vessels and glands, so a non-contrast model can call a vessel a node or miss a boundary it used to see. Autocontours are an initial guess. Targets in particular need a physician, because the model does not know the stage or which node levels were prescribed. Editing is the normal workflow, not a violation of the model.

### Q3
Stem: The Dice coefficient between an autocontoured bladder and the corrected bladder is 0.88. The Hausdorff distance is 2.4 cm. What do those two numbers mean together?
A. Dice of 0.88 means the worst point on the surface is 0.88 cm off, so Hausdorff is redundant
B. Overlap of the volumes is fairly high, but some point on one surface is 2.4 cm from the other surface; a local miss of that size still has to be found and edited
C. Hausdorff distance of 2.4 cm means 2.4% of the voxels disagree, which is better than a Dice of 0.88
D. Both numbers are doses in gray and show the bladder is under the tolerance
Answer: B
Objective: III.10
Why: Answer B. Dice is 2 times the intersection volume divided by the sum of the volumes. A value of 0.88 means the bulk of the bladder overlaps, which is easy to achieve for a large organ even when one slice or one wall is far off. Hausdorff distance is the worst surface-to-surface gap, here 2.4 cm. That outlier will not be obvious from Dice alone and is exactly the kind of error that can sit in a high-dose region. Neither number is a dose, and neither replaces scrolling through the slices.

### Q4
Stem: An autocontour model reports a Dice score of 0.90 on the liver and 0.55 on the optic chiasm for the same patient. Which interpretation matches how these structures behave?
A. The chiasm result is more trustworthy because a low Dice score means a small structure was segmented with higher absolute accuracy
B. Small, thin structures tend to score worse and are easier to miss clinically; a bad chiasm contour can still put the high dose on the optic pathway even when the liver looks excellent
C. Dice scores can be compared as if they were the same task; 0.55 on the chiasm is equivalent to 0.55 on the liver
D. The liver score of 0.90 authorizes the chiasm contour because both came from one model
Answer: B
Objective: III.10
Why: Answer B. Dice is harsh on small structures: a one-voxel shift of a thin chiasm changes the overlap fraction dramatically, whereas the same shift on the liver barely moves Dice. The clinical risk runs the same direction. A missed chiasm, lens, or optic nerve is a serious planning error, and a reassuring liver score says nothing about it. Each structure is reviewed on its own. A low score is not evidence of higher accuracy.

### Q5
Stem: The automatic body contour includes the couch and the immobilization vacuum bag, and it excludes a bolus that was in place during the scan. The plan is a chest-wall electron calculation. What will go wrong if this body contour is used as drawn?
A. Nothing; body contours are cosmetic and are not used in dose calculation
B. The couch and bag become "patient," adding false buildup and attenuation, and the missing bolus lets the calculation treat the skin as if the bolus were absent
C. The error affects only the DVH of the cord, not the electron range
D. Including the couch raises the beam energy automatically and corrects the bolus omission
Answer: B
Objective: III.10
Why: Answer B. Dose calculation uses the external contour to decide where tissue starts and what density the beam crosses. A couch or bag inside the body contour adds material the beam may not actually cross, or it changes scatter. Leaving bolus outside the body (or unassigned) calculates a bare skin surface and the wrong electron range and skin dose. The body contour is not cosmetic, the electron result is directly affected, and contour mistakes do not change the nominal energy of the machine.

## Auto-Segmentation Mini-Quiz

### Q1
Stem: A model contours "left parotid" on the patient's right, because the CT was marked feet-first and the model assumed head-first. The shape of the gland looks smooth and the Dice score against a mirrored atlas is high. What is the status of that contour?
A. Usable; a high overlap score outweighs laterality
B. Not usable until laterality is checked against the patient orientation; a smooth wrong-sided contour is still the wrong organ
C. Usable if the planner swaps the beam names and leaves the contour on the right
D. Not a failure mode of autocontouring, because models read the DICOM patient position tag correctly in every case
Answer: B
Objective: III.10
Why: Answer B. Autocontour errors include left-right swaps when orientation tags are wrong or ignored. Overlap against a mirrored atlas can look excellent while the gland is on the wrong side of the patient. Dose constraints applied to that contour would spare the wrong parotid and ignore the real one. Beam renaming does not move the organ. Orientation has to be confirmed on the CT before any model output is trusted, because tag errors are a known import failure, not a theoretical one.

### Q2
Stem: Which statement about responsibility for autocontoured volumes is consistent with treatment-planning practice?
A. The vendor warranty replaces physician approval of the GTV and CTV
B. Organs at risk may start from a model, but a person checks them, and the physician defines or approves the target volumes before planning
C. Once Dice exceeds 0.80 for the external contour, target review is optional
D. Autocontouring is appropriate only for brachytherapy source trains, not for external-beam organs
Answer: B
Objective: III.10
Why: Answer B. Segmentation software produces a draft. The clinic still has to confirm organs at risk, because a missed slice of cord or a rectum that includes the prostate will drive the optimizer the wrong way. Gross and clinical target volumes depend on disease, not only on image edges, so they belong to the physician's approval. A warranty, a single Dice threshold, or a brachytherapy restriction does not change that division of work.

### Q3
Stem: Metal from a hip prosthesis blacks out and streaks the pelvic CT. The autocontour draws the prostate with a bite taken out of it along the worst streak, and it extends the bladder through the artifact into the prosthesis. Why is this a typical failure?
A. Models and atlases expect tissue contrast; streak and cupping artifact remove that contrast and invent false edges
B. Artifact only affects kilovoltage portal images, not the planning CT the model uses
C. A prosthesis improves autocontour accuracy by giving a high-contrast landmark inside the bladder
D. The bite out of the prostate is the PTV margin, applied automatically
Answer: A
Objective: III.10
Why: Answer A. Both atlas deformation and learned models rely on recognizable edges and intensities. A hip implant creates bright metal and dark streaks that do not correspond to organ boundaries. The model will follow those false edges. The contour has to be redrawn with the anatomy, not the streak, and the densities used for calculation need a separate override strategy. Artifact on the planning CT is the problem here, not portal imaging. A missing chunk of prostate is not a margin.

### Q4
Stem: An autocontoured cord stops two slices above the inferior edge of the PTV because the model found the canal noisy below that level and closed the contour. The DVH of this cord is within the cord limit. Why is that DVH not evidence the cord is safe?
A. It is evidence; a DVH cannot be built from a partial contour
B. The DVH only scores the cord that was drawn; the undrawn cord next to the PTV is absent from the histogram and can sit in the high dose unseen
C. Stopping short of the PTV is required by ICRU so the cord maximum is defined as zero
D. A cord contour should stop at the PTV by definition, so the missing slices are correct
Answer: B
Objective: III.10
Why: Answer B. A DVH is computed on the voxels inside the contour. If the inferior cord was never contoured, those voxels are not in the cord DVH, and the maximum can look acceptable while the real cord is in the field. This is a standard autocontour failure: the structure quietly ends. The fix is to scroll past the PTV and complete the organ, then recompute the dose-volume histogram. ICRU does not define an organ maximum by deleting the organ.

### Q5
Stem: A clinic compares two autocontour systems on 30 prostate CTs. System A has a higher mean Dice for the rectum. On three patients, system A includes the prostate in the rectum, and system B does not. Why can the mean Dice still favor system A?
A. It cannot; Dice falls to zero if the rectum touches the prostate on any slice
B. Dice averaged over many patients can hide a few severe, clinically dangerous overlaps if the rest of the cases score well
C. Mean Dice weights a single bad slice more than the volume of the other 27 patients
D. System B's correct laterality lowers its Dice by definition
Answer: B
Objective: III.10
Why: Answer B. A mean is pulled by the typical case. Three serious failures in 30 patients can leave the average looking better for the system that is smoother on the easy majority. Prostate included inside the rectum is exactly the error that makes an optimizer "spare" the rectum by cutting the target, or that hides rectal dose. Acceptance testing has to look at the worst cases and at clinical failure modes, not only at mean Dice. One bad region does not force the whole-organ Dice to zero if the rest of the volume still overlaps.
