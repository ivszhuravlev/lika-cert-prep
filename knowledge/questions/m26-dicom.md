# Module 26 — DICOM data transfer

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## DICOM

### Q1
Stem: A planning CT, the contours, the beam geometry, and the three-dimensional dose grid are exported to the record-and-verify system. Which DICOM object carries which information?
A. The CT image object carries beams and dose; the RT Plan carries only the contours
B. CT Image carries the voxels and Hounsfield units, RT Structure Set carries the contours, RT Plan carries beams and monitor units, and RT Dose carries the dose grid
C. RT Dose carries the contours, and RT Image carries the monitor units
D. A single RT Beams object carries CT, contours, dose, and scheduling, because DICOM uses one object type for radiotherapy
Answer: B
Objective: III.9
Why: Answer B. DICOM separates these jobs. The CT (or MR, or PET) image object stores the pixel matrix, pixel spacing, and rescale values that turn stored pixels into Hounsfield units. The RT Structure Set stores ROI contours and references the images they were drawn on. The RT Plan stores prescription, fractionation, beams, energy, monitor units, jaws, multileaf shapes, and accessories. The RT Dose stores the dose grid, dose units, and how that dose was summed. A digitally reconstructed radiograph or a portal image is an RT Image, not the dose and not the monitor units. Mixing these objects up is a common transfer error: contours without the plan, or a plan without the dose the physician approved.

### Q2
Stem: An RT Structure Set arrives in the planning system and the contours appear shifted several centimeters off the CT, even though the ROI names are correct. The CT series was re-exported this morning and received new SOP Instance UIDs. The structure set still points at yesterday's Frame of Reference. What is the likely reason the contours do not sit on the anatomy?
A. ROI names override the coordinate frame, so the shift is only a display color
B. The structure set is tied to a frame of reference and to the image instances it was contoured on; a new export that does not share that frame will not line up
C. DICOM contours are stored in percent of prescription, not in millimeters, so a new CT changes their scale
D. A Frame of Reference UID mismatch only affects RT Dose, never structures
Answer: B
Objective: II.1
Why: Answer B. Contours are coordinates in a defined frame, not a picture glued to a file name. The RT Structure Set references the Frame of Reference UID and the SOP instances of the slices it belongs to. If the CT is re-sent under a new frame, or the patient position tag differs, those coordinates land in the wrong place in the new dataset. The planner should not "nudge" contours by eye and calculate. The correct fix is to re-associate or re-export a consistent set. Names do not carry geometry, contours are spatial coordinates, and the frame of reference matters for structures as much as for dose.

### Q3
Stem: In the DICOM patient coordinate system, which direction is +X, which is +Y, and which is +Z?
A. +X toward the patient's right, +Y toward the anterior surface, +Z toward the feet
B. +X toward the patient's left, +Y toward the posterior surface, +Z toward the head
C. +X toward the gantry, +Y toward the patient's right, +Z up from the couch, for every patient orientation
D. +X is superior, +Y is the patient's left, +Z is anterior
Answer: B
Objective: II.1
Why: Answer B. The DICOM patient axis system is right-handed: +X increases to the patient's left, +Y increases toward the posterior, and +Z increases toward the head. A shift exported in those coordinates has to be interpreted with that sign convention. Vendor couch displays and the IEC accelerator system use different axes, so a positive DICOM X is not automatically "table left" on every console. The orientation tag (head-first supine versus feet-first supine) further changes how the patient lies in the room. Treating a feet-first patient with a head-first coordinate assumption irradiates the wrong end of the volume. C describes a machine system, not the patient system, and it is not independent of orientation.

### Q4
Stem: The physician approves a dose on the planning system. The record-and-verify system receives an RT Plan and the CT, but the RT Dose object fails to send. What does the receiving system not have?
A. The beam names and the monitor units, which live only in RT Dose
B. The three-dimensional dose grid, so a dose display or a DVH on the receiving system cannot be rebuilt from the objects that arrived
C. The Hounsfield units, which live only in RT Dose
D. The contour names, which live only in RT Dose
Answer: B
Objective: III.9
Why: Answer B. RT Dose is the dose matrix: grid origin, pixel spacing, dose units, and the dose values. Without it, the receiving system may still have the beams and monitor units inside the RT Plan, the anatomy in the CT, and, if it was sent, the contours in the RT Structure Set. It does not have the dose distribution the physician looked at. Monitor units are not a substitute for the grid, because the same monitor units on a different algorithm or a different grid origin are a different dose. Hounsfield units are in the image object. Contour names are in the structure set.

### Q5
Stem: A physicist is deciding how to move a plan from the treatment-planning system to the oncology information system. Which statement describes what DICOM is for?
A. DICOM is the calculation algorithm that converts Hounsfield units to dose
B. DICOM is the standard that packages images and radiotherapy objects so another system can read them; it does not decide whether the plan is clinically safe
C. DICOM replaces independent monitor-unit calculation
D. DICOM is the HL7 interface that schedules chemotherapy, and it does not carry images
Answer: B
Objective: III.9
Why: Answer B. DICOM (including the radiotherapy objects) is an exchange format. It lets the simulator, the planning system, and the record-and-verify system share CT, structures, plans, dose, and images without a private tape format. A successful transfer means the objects were readable and the identifiers matched. It does not mean the prescription is right, the hot spot is acceptable, or the monitor units were checked. Those reviews stay with the people and the independent calculation. HL7 moves clinical messages such as demographics and orders; it is not the radiotherapy image standard.

## DICOM Data Transfer Mini Quiz

### Q1
Stem: Which object is the usual place to find a digitally reconstructed radiograph generated by the planning system?
A. RT Image
B. RT Dose
C. RT Structure Set
D. The CT image series, as an extra row of Hounsfield units
Answer: A
Objective: III.9
Why: Answer A. An RT Image is a two-dimensional radiotherapy image. Digitally reconstructed radiographs and portal images are stored as RT Images, with geometry that ties them back to the beam in the RT Plan. RT Dose is the three-dimensional dose grid. The RT Structure Set is contours. The CT series is the axial (or helical) planning images, not the beam's-eye projection derived from them.

### Q2
Stem: A proton plan is exported. The photon RT Plan object is empty and a separate ion-plan object is present, along with an RT Dose. Why might the record-and-verify system show no beams if it only imports photon RT Plans?
A. Proton beams are stored in the CT image pixels
B. Ion beams live in the RT Ion Plan (ion beams) object; a receiver that only understands photon RT Plan will see an empty photon plan and drop the proton beams
C. RT Dose contains the spot positions and can rebuild the beams without the ion plan
D. DICOM forbids transfer of proton plans, so the empty object means the plan was not calculated
Answer: B
Objective: III.9
Why: Answer B. Photon beams and ion beams are different DICOM objects. Spot positions, energies, and ion beam modifiers are in the RT Ion Plan, not in the photon RT Plan and not in the voxel values of the CT. The dose grid shows the result of the calculation, not the control system needed to deliver spots. A department that treats protons has to confirm the receiving system actually imports the ion object. An empty photon plan is then expected, not evidence that the proton plan failed to calculate.

### Q3
Stem: The dose grid origin is 5 cm different from the CT origin, and the dose voxels are 4 mm while the CT voxels are 1 mm. The DVH shows the PTV barely covered. What should be checked before the coverage is believed?
A. Nothing; dose and CT are required to share an origin and a voxel size, so a difference of 5 cm cannot occur in a valid file
B. Whether the RT Dose grid actually covers the PTV and is referenced to the same frame; a cropped or shifted dose grid produces a bad DVH from missing dose, not from the beams
C. Only the contour color, because origin is not stored in DICOM
D. The half-life of the beam, because grid origin drifts with source decay
Answer: B
Objective: II.1
Why: Answer B. DICOM explicitly allows the dose grid to have its own origin, spacing, and size. That is useful, but a grid that was cropped to a region of interest, or referenced to the wrong frame, will look like a cold PTV when the dose was simply never scored there. The review is to overlay the dose on the CT in the planning system that created it and confirm the grid encloses the target before the DVH is used to reject the plan. Origins are stored. They do not drift with radioactive decay on a linac plan.

### Q4
Stem: Two CT series for the same patient are in the imported study. One is head-first supine. The other is feet-first supine, from a scan that was repeated after the patient was turned around. The RT Plan was calculated on the head-first series. The therapist loads the feet-first series for image guidance matching by accident. What class of error is this?
A. A patient-orientation error; the anatomy is mirrored or flipped relative to the plan coordinates and the match is not to the planned geometry
B. A harmless duplicate, because head-first and feet-first share the same DICOM +Z direction in the room
C. An energy error, because patient position changes the nominal megavoltage
D. A contour-naming error only; the coordinates are unaffected
Answer: A
Objective: II.1
Why: Answer A. Head-first supine and feet-first supine are different patient positions. The DICOM patient axes are defined relative to the patient, but the way those axes point in the treatment room changes when the patient is turned. Matching or treating the wrong series can reverse the superior-inferior direction of the plan relative to the gantry. The fix is to confirm the series description, the patient-position tag, and a known anatomic landmark before delivery. Energy does not change with orientation, and this is not a naming-only problem.

### Q5
Stem: A planner anonymizes a case for a conference by deleting the patient name only. The DICOM files still contain the medical record number, the date of birth, and the institution in other tags. What has gone wrong?
A. Nothing; the patient name is the only identifier DICOM defines
B. De-identification failed; DICOM places identifiers in many tags, and a real anonymization profile has to clear or replace all of them
C. Dates of birth are required for dose calculation, so they must remain for the plan to open
D. The medical record number is stored only in HL7, never in a DICOM header
Answer: B
Objective: III.9
Why: Answer B. The Patient Name attribute is only one identifier. Medical record number, birth date, accession number, device serial numbers, and even burned-in pixels on a radiograph can identify a person. DICOM has a de-identification profile that lists what to remove, keep, or replace. Clearing the name and exporting the rest is not anonymization. Dose calculation does not need the date of birth in the header. Identifiers are present in DICOM headers; they are not exclusive to HL7.

### Q20
Stem: The receiving system shows beams and monitor units and an empty contour list. The CT series and the RT Plan imported. Which object is missing, or is pointing at another series?
A. RT Dose, because contours are stored only in the dose grid
B. RT Image, because a digitally reconstructed radiograph is the contour object
C. The RT Structure Set
D. The CT Image, because an empty contour list means the voxels never arrived
Answer: C
Objective: III.9
Why: Answer C. Contours live in the RT Structure Set, which references the CT series they were drawn on. Beams and monitor units can arrive in the RT Plan without that object. RT Dose is the three-dimensional dose grid. An RT Image is a projection, a digitally reconstructed radiograph or a portal. A CT that is present does not create the contours.

### Q21
Stem: An imported dose grid sits 2.5 cm superior to the planning CT origin along the patient axis. Pixel spacing along that axis is 1.0 mm. How many pixels is the shift, and what is the fix?
A. 25 pixels; restore the shared frame and recheck a point dose, and do not move the patient until the wash covers the tattoos
B. 2.5 pixels, and accept the histogram because the import message said complete
C. 250 pixels, from treating the 1.0 mm spacing as if it were 1.0 cm
D. 0 pixels, because a file that opens forces the dose origin onto the CT origin
Answer: A
Objective: II.1
Why: Answer A. 2.5 cm / 0.1 cm = 25 pixels. A completed transfer is not a checked frame. A dose grid translated along the patient scores the wrong anatomy. A couch shift that makes the pictures look aligned treats the wrong coordinates.

### Q22
Stem: A planning CT and an MRI are exported together. The spatial-registration object that held the rigid transform between their frames of reference is not in the transfer. Both series open. What can still be wrong?
A. The CT voxels are deleted when the registration object is dropped
B. MRI signal is converted to Hounsfield units by the missing object, so fusion is no longer needed
C. Only an RT Image can be displaced; an MRI stays locked to the CT origin
D. The MRI can sit on the wrong origin relative to the CT even though both series imported
Answer: D
Objective: II.1
Why: Answer D. That object stores the transform between two frames of reference. Without it, each series can open in its own frame and the MRI can be drawn in the wrong place on the CT. A successful import does not prove the frames match. MRI values are not Hounsfield units.

### Q23
Stem: A cone-beam series is stored as a CT-class image and sent to the planning system. Which statement matches what that object is?
A. It is the commissioned planning CT, because the image class says CT
B. It can be stored in the CT class and is still not the commissioned planning dataset used for dose
C. It is an RT Dose object, so the pixel values are gray
D. Its numbers are the simulator density table by definition
Answer: B
Objective: III.9
Why: Answer B. A cone-beam or a megavoltage CT may be stored as a CT-class image. The class does not make it the simulator scan the planning calculation was commissioned on. Scatter and an unvalidated density relationship remain. The dose grid is a different object.

### Q24
Stem: A teaching-file export keeps the pixels and removes the Frame of Reference UID and the SOP Instance UIDs. The case still opens. What can that strip do?
A. Nothing; those identifiers are display labels and do not connect objects
B. It turns the RT Plan into an RT Image
C. It is required before a point dose can be compared
D. It can unlink the dose, the contours, and the CT, so the objects may open displaced or unattached
Answer: D
Objective: III.9
Why: Answer D. The Frame of Reference UID is the coordinate contract, and SOP Instance UIDs are what the structure set and the dose point at. Clearing them is a different failure from clearing the patient name. Repair the identifiers. Do not nudge the anatomy until it looks right and then calculate.

### Q25
Stem: The import window says the transfer is complete. Which review is still required before anyone plans or treats from the received objects?
A. Patient orientation, the isocenter against the simulation document, fraction dose and fraction count against the prescription, and a point dose against the system that exported the plan
B. None; a complete message already certifies orientation, isocenter, fractionation, and point dose
C. Only the color assigned to the cord
D. Only that the RT Image carries the Hounsfield units
Answer: A
Objective: II.1
Why: Answer A. DICOM makes the objects readable. It does not decide that they are the approved plan. Head-first versus feet-first, the isocenter, the fractionation, and a point dose are checked after the window says complete. Contour color is not that check, and an RT Image is not the Hounsfield volume.

### Q26
Stem: A CT simulator sends a planning study to the department picture archive. Which statement assigns DICOM and PACS correctly?
A. DICOM is the scanner operating system, and PACS only prints the schedule
B. PACS is the communication standard, and DICOM is the operating system that stores the pixels
C. DICOM is the communication standard so imaging devices and PACS can exchange images. PACS stores the images. DICOM is not an operating system
D. DICOM and PACS are two names for the same operating system
Answer: C
Objective: III.9
Why: Answer C. DICOM is the communication standard imaging devices and a PACS use when they exchange images. PACS is the picture archive that stores those images. An operating system, such as the one that runs the computer, is a different piece of software. A finished transfer still has to be checked before the study is used for planning.
