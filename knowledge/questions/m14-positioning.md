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
