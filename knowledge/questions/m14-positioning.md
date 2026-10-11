# Module 14 — Patient Positioning

Original items on reproducible setup and the errors that follow a wrong position.

## Patient Positioning

### Q1
Stem: The position used for the planning CT should be the position used for treatment because:
A. Internal anatomy and the external contour are part of the dose calculation and have to be reproduced
B. Lasers can move a patient from prone to supine without a new plan
C. A diagnostic curved couch is equivalent to a flat treatment couch
D. Position affects only the billing code
Answer: A
Objective: II.2
Why: SSD, depth, organ location, and beam path all come from the simulated position. Lasers do not convert a prone scan into a supine patient. A curved couch changes the spine and the contour relative to a flat-top linac.

### Q2
Stem: Arms are placed above the head for a thorax plan primarily so that:
A. The arms are out of the oblique and lateral beam paths
B. The lung density becomes 1.0
C. Respiratory motion stops
D. The scan can be feet-first without a note
Answer: A
Objective: II.2
Why: An arm in a lateral or tangent beam adds an unplanned attenuator and a setup that is hard to repeat. Arm position does not set lung density, does not stop breathing, and does not change head-foot orientation.

### Q3
Stem: A prone breast board is chosen instead of supine for a large pendulous breast in order to:
A. Let the breast fall away from the chest wall and change the heart and lung geometry relative to supine
B. Eliminate the need for tattoos
C. Remove all setup uncertainty
D. Convert the photons to electrons
Answer: A
Objective: II.2
Why: Prone positioning can pull the breast away from the chest wall and reduce the volume of heart or lung in the tangents for selected patients. It does not remove the need for a reproducible mark, it does not zero the setup error, and it does not change the particle type.

### Q4
Stem: Knee and ankle supports for a supine pelvis are used to:
A. Make the pelvic tilt and the leg position the same at every fraction
B. Increase the magnification of the DRR
C. Shorten the half-life of the beam
D. Replace the immobilization mask
Answer: A
Objective: II.2
Why: A comfortable, indexed leg position keeps the pelvis from rotating day to day. It is not a DRR magnification tool, not a beam property, and not a substitute for the device that actually fixes the part being treated.

### Q5
Stem: Indexing an immobilization device to the couch means:
A. The device locks to the same couch notch each day so the patient-to-isocenter geometry can be repeated
B. The device may be placed on any notch because the lasers will absorb the difference
C. Indexing replaces the CT scan
D. The notch number changes the Hounsfield scale
Answer: A
Objective: II.2
Why: A different notch shifts the patient relative to the isocenter by a fixed and easily missed distance. Lasers only report where the patient is; they do not undo a wrong index. Indexing is not a scan and it does not change HU.

### Q20
Stem: A prostate plan was scanned with a full bladder, as the setup note requires. On treatment the bladder is nearly empty and the tattoos still meet the lasers. What has changed inside the patient?
A. Nothing that the beams see, because the external marks still match
B. Small bowel can drop into the high-dose region, and the prostate is no longer in the planned place
C. The bladder wall is reassigned the Hounsfield number of cortical bone
D. The beam must be changed from 6 MV to 18 MV to cover the empty bladder
Answer: B
Objective: II.2
Why: Bladder filling is part of the position. An empty bladder lets bowel fall toward the target and moves the prostate relative to the beams that were planned on a full bladder. Lasers on the tattoos do not restore that internal anatomy. The CT numbers and the energy are unchanged.

### Q21
Stem: A belly board was used so that, prone, small bowel would fall out of a posterior pelvic field. The same board is used with the patient supine. What is the setup now?
A. The position the belly board is built for
B. The same bowel geometry, with only the photograph changed
C. A change of the beam from photons to electrons
D. The wrong surface against the opening: bowel is no longer dropped out of the posterior beam, and the beams enter the opposite side from the plan
Answer: D
Objective: II.2
Why: A belly board is a prone device. The opening lets bowel fall anteriorly, away from a posterior field. Supine puts that opening on the couch side and treats the opposite external surface from the simulated plan. The modality does not change.

### Q22
Stem: A lower-extremity plan is simulated feet-first supine because the gantry cannot clear the head. The scan is later opened with the department’s usual head-first orientation. What can that mismatch do?
A. Reverse superior-inferior, and left-right with it, relative to the patient, while the limb contour still looks familiar
B. Leave the geometry unchanged, because feet-first and head-first are the same DICOM orientation
C. Change only the slice thickness
D. Get corrected by the knee-rest notch, which replaces the orientation
Answer: A
Objective: II.2
Why: Feet-first is a different patient orientation from head-first. Planning one as the other swaps the long axis and can swap laterality. The contour of a limb can still look plausible. An immobilization notch does not rewrite the orientation.

### Q23
Stem: A perineal setup leaves a deep skin fold closed over the target. Compared with the same skin laid flat, the dose inside the fold is:
A. Lower, because the fold replaces a compensator
B. The same, because skin dose is fixed by energy alone
C. Higher, because skin against skin is self-bolus and removes the air the buildup region needs
D. Zero until a physical wedge is added
Answer: C
Objective: II.2
Why: A closed fold puts tissue against tissue. Megavoltage skin sparing assumes air beyond the surface. The fold raises the dose on that skin the way bolus does. Opening the fold is a dose decision. A wedge does not create or remove that contact.

### Q24
Stem: The plan uses 0.5 cm of bolus in contact with a chest-wall scar. At treatment the bolus tents over the scar and leaves an air gap. What does the calculation no longer describe?
A. Only the billing code for the bolus
B. The surface dose and the depth of maximum dose in the patient, because the bolus is no longer the entrance surface that was planned
C. A wedge angle equal to the air-gap thickness
D. The decay of the photon beam
Answer: B
Objective: II.2
Why: Bolus changes dose when it touches the skin and fills buildup. An air gap puts the scar back toward the skin-sparing region, and the contour correction in the plan is for contact that is not there. The same monitor units do not restore that contact. Air is not a wedge, and a photon beam has no half-life.

### Q25
Stem: A head-and-neck mask is made with the arms at the sides and the shoulders pulled down. A thorax plan on a wing board puts the arms above the head. Why does each site keep its own arm position?
A. Every site needs the arms above the head so the mask can be left off
B. Shoulder height has no effect on a lateral neck beam
C. Arm position selects 6 MV or 15 MV
D. Arms down keep the shoulders out of the neck fields, and arms up keep the arms out of tangential and lateral chest beams
Answer: D
Objective: II.2
Why: A raised shoulder sits in a lateral or anterior neck beam. An arm left on the chest or at the side sits in a tangent or a lateral thorax beam. The position is chosen so the beam path matches the plan. Energy does not follow the arm board.

### Q26
Stem: A head-and-neck plan uses a thermoplastic mask on a headrest, with the shoulders pulled down and the arms at the sides. A lung plan uses a wing board. What does each device hold?
A. The mask holds chin flexion, head rotation, and shoulder height for the neck beams; the wing board holds the arms above the head, out of the chest beams
B. Both devices are prone belly boards
C. The mask stops respiration, and the wing board selects the photon energy
D. The wing board is molded to the face, and the mask indexes only the knees
Answer: A
Objective: II.2
Why: A thermoplastic mask is molded to the face and, for head and neck, often includes the shoulders, so the chin and the shoulder height match the scan. Shoulders pulled down stay out of the lateral neck beams. A wing board is an indexed arm support for thorax, breast, and lung, so the arms stay up and out of tangents and laterals. A belly board is a prone pelvic device. Neither device chooses beam energy or stops breathing.

### Q27
Stem: A vacuum bag was molded and indexed at simulation for a supine thorax. At treatment the bag has lost vacuum and the beads have shifted. The tattoos can still be brought to the lasers. What is the setup now?
A. The simulated cradle, because the tattoos reach the lasers
B. A different support under the body, so the contour in the bag is no longer the contour that was scanned
C. An electron plan, because loss of vacuum changes the particle
D. Unchanged geometry, because a vacuum bag is only a photograph
Answer: B
Objective: II.2
Why: The bag holds a custom cradle only while it holds vacuum. Once the beads move, the support under the trunk is a different shape from the planning CT, even if the skin marks can be forced to the lasers. The modality stays photons. The bag is immobilization, and any beam that crosses it sees that shape.

### Q28
Stem: Which pairing matches the device to the site it is built for?
A. Thermoplastic mask for brain or head and neck; wing board for arms-up breast or lung; belly board for a prone pelvis; vacuum bag for a custom indexed body cradle
B. Belly board for an arms-up supine breast; wing board under a prone abdomen; mask as a knee rest only
C. Vacuum bag as a substitute for the bladder instruction; belly board as a headrest
D. Wing board as the face mask; thermoplastic mask as the couch-top density model
Answer: A
Objective: II.2
Why: The mask immobilizes the head and neck. The wing board holds the arms up for chest and breast. The belly board is prone, with an opening so abdominal contents can fall anteriorly. A vacuum bag is a molded, indexed cradle for the trunk or a limb. Swapping the devices puts the opening, the arms, or the head in the wrong place relative to the plan.

### Q29
Stem: An intact pendulous left breast was planned prone so the breast falls through the board opening, away from the chest wall. Day 1 is set up supine on a breast board, and the prone shifts are applied. What has changed?
A. The photograph only; heart, lung, and breast contour remain the prone anatomy
B. The external contour and the heart and lung geometry are now the supine anatomy, and the plan was calculated on the prone anatomy
C. Nothing geometric; prone and supine breast boards share one external contour
D. The prone opening still drops the breast while the patient lies supine
Answer: B
Objective: II.2
Why: Prone breast positioning uses the board opening to change where the breast, heart, and lung sit relative to the tangents. Supine on a breast board is a different external contour and a different organ geometry. The prone shifts were computed on the prone surface. A supine patient does not hang through that opening.

### Q30
Stem: A postmastectomy chest wall is the target. A prone breast board is available. Why is supine on a breast board, with the arm up, the usual position for that chest wall?
A. The prone opening is built so an intact breast can fall away from the wall; the chest-wall target is the wall, and it is planned supine
B. Every postmastectomy plan is prone, because the wall is heavier than an intact breast
C. Supine positioning removes the need for a reference mark
D. A wing board changes the chest-wall photons into electrons
Answer: A
Objective: II.2
Why: The prone breast board works by letting an intact breast drop through an opening, which moves that breast off the chest wall. After mastectomy the target is the chest wall, so that opening does not place the target. Supine, arm up, is the usual reproducible position for chest-wall fields. Marks are still required. The arm support does not change the particle.

### Q31
Stem: A prostate arc plan is simulated supine with a knee sponge for daily soft-tissue imaging. A rectal plan is simulated prone on a belly board so small bowel falls out of a posterior field. Which statement matches those two positions?
A. Either plan can be treated in the other position once the tattoos are rewritten
B. The prostate course stays supine, the position that was scanned and that daily imaging will match; the rectal course stays prone, because the belly-board opening is what drops the bowel
C. The belly board is the supine prostate device, and the knee sponge is used only when the patient is prone
D. Prone and supine pelves produce the same bowel and bladder geometry
Answer: B
Objective: II.2
Why: Supine prostate setup with a knee support is chosen for reproducibility and for cone-beam matching. The belly board is a prone device: the opening lets small bowel fall anteriorly, away from a posterior rectal field. Each plan’s contour, organs, and beams belong to the position that was scanned. New tattoos do not convert one external surface into the other.

### Q32
Stem: A prostate protocol scans and treats with a comfortably full bladder and an empty rectum. The tattoos are on the lasers, the bladder is empty, and the rectum is full of gas. What should happen before the beam is turned on?
A. Treat, because the external marks satisfy the plan
B. Hold the fraction. The filling is part of the position: an empty bladder lets bowel fall toward the high dose, and rectal gas pushes the prostate off the planned place
C. Empty the bladder further and proceed, because rectal gas lies outside the target by definition
D. Change to electrons so filling no longer affects the beams
Answer: B
Objective: II.2
Why: The full bladder displaces small bowel and puts the prostate in the geometry that was planned. Gas or stool in the rectum pushes the gland, usually anteriorly. Lasers on the tattoos do not restore either organ. The fraction waits until the preparation matches the protocol or a physician decides otherwise. Electrons do not replace that anatomy.

### Q33
Stem: A rectal target was simulated with the preparation written in that chart, including a full bladder to move small bowel. The prostate instruction “empty rectum, then treat once the tattoos match” is applied without the rectal note. What is the mistake?
A. Prostate and rectum share one filling rule, so the prostate instruction is the rectal plan
B. The rectum is the target on this plan, and the chart’s preparation is the preparation; an empty-rectum rule copied from prostate is a different internal anatomy
C. Bladder filling is an instruction for head-and-neck masks only
D. A full bladder is used to choose 6 MV versus 15 MV
Answer: B
Objective: II.2
Why: Prostate protocols often want an empty rectum so gas does not displace the gland, and a full bladder so bowel stays superior. On a rectal plan the rectum is the target, and the bowel instruction is the one in the note. A full bladder is a common part of that note. Copying the other site’s preparation treats a patient the dose was not calculated on. Photon energy does not follow bladder volume.

## Patient Positioning Mini-Quiz

### Q1
Stem: A plan was simulated head-first supine. On treatment the patient is set up head-first prone and the supine shifts are applied anyway. The likely geometric error is:
A. Anterior and posterior are exchanged relative to the plan, so the isocenter moves to the wrong side of the body
B. No error, because prone and supine share the same anterior direction
C. Only the slice thickness changes
D. The beam energy changes from 6 MV to 18 MV
Answer: A
Objective: II.2
Why: Prone swaps the anterior-posterior relationship to the couch and to a supine shift sheet. Applying the supine shifts sends the isocenter the wrong way through the patient. Energy and slice thickness are unchanged.

### Q2
Stem: A head-and-neck patient is scanned with the chin extended, but treatment begins with the chin flexed. The cord and the oral cavity move relative to the isocenter because:
A. Neck flexion changes the vertebral and mandibular geometry inside the mask region
B. Chin position affects only the photograph
C. Flexion changes HU of the cord from 0 to −1000
D. The mask makes flexion impossible to notice
Answer: A
Objective: II.2
Why: The cervical spine straightens or curves with the chin, and the mandible and oral cavity move with it. A plan optimized on one flexion does not describe the other. This is anatomy, not a change in HU, and a mask that was made on the wrong flexion will still look “on” if nobody checks the chin.

### Q3
Stem: Tattoos are placed at the simulation reference, not necessarily at the final isocenter. Their role is to:
A. Give a stable external starting point from which the planned shifts are made
B. Mark the GTV on the skin so that no shifts are ever required
C. Replace imaging
D. Set the window level of the CT
Answer: A
Objective: II.2
Why: The reference marks are a reproducible external origin. The treatment isocenter is often shifted from that origin after the plan is done. Tattoos do not draw the GTV, they do not replace IGRT, and they do not set the CT window.

### Q4
Stem: A left-right setup error of 2 cm is introduced after a correct plan. Which statement is correct?
A. The target and the organs move together relative to the beam, and a 2 cm shift is large compared with a typical PTV margin
B. The dose distribution stays correct because the beams move with the patient automatically
C. A 2 cm error is smaller than every PTV margin used in clinic
D. Only the MU change; the geometry does not
Answer: A
Objective: II.2
Why: If the patient is translated and the beams stay on the original isocenter, the high dose misses the target by about that translation. Many PTV margins are well under 2 cm, especially for stereotactic and head-and-neck plans. The linac does not follow the patient unless imaging or a shift corrects it. MU are not the primary failure.

### Q5
Stem: Setup photos and a written description of devices belong in the chart because:
A. The treating team has to reproduce the simulated position, including arms, bolus, and indexing, not only the shifts
B. Photos replace the dose calculation
C. A photo sets the decay constant
D. Devices do not affect the beam if the tattoos are correct
Answer: A
Objective: II.2
Why: Shifts assume the same body habitus relative to the marks. A missing bolus, a different arm position, or a different knee rest changes depth and anatomy even when the tattoos are aligned. Photos do not calculate dose and they do not change λ.
