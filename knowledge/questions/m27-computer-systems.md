# Module 27 — Computer systems management

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Comp-Sci Terms (Simplified)

### Q1
Stem: A planning CT is archived for dose calculation. An engineer offers to store it as a lossy JPEG to save disk space, accepting small pixel changes. Why is that a problem for treatment planning?
A. It is not a problem; Hounsfield units are immune to compression
B. Lossy compression changes pixel values, so the Hounsfield numbers and the density used for dose can change; planning images are kept with lossless compression or uncompressed
C. JPEG increases the bit depth, which makes the dose grid more accurate
D. Lossy compression only affects the RT Plan monitor units, not the image
Answer: B
Objective: III.9
Why: Answer B. Lossy compression deliberately discards information and does not restore the original pixels. A small change in a Hounsfield number changes the density lookup, especially in lung and bone, and it can move a contour threshold. Diagnostic and planning CTs that will be used quantitatively are stored losslessly. The dose grid and the monitor units are separate objects; compressing them with an image codec is not what this offer described, and JPEG does not increase bit depth.

### Q2
Stem: The planning system keeps the open plan in RAM and writes it to disk only when the planner saves. The power fails. What is true of the unsaved work?
A. RAM is non-volatile, so the open plan is still present when the power returns
B. RAM is volatile; unsaved edits that existed only in memory are gone, and the last saved copy on disk is what remains
C. A power loss converts RAM contents into an approved DICOM RT Plan automatically
D. Volatile memory is the long-term archive, so the disk copy is the one that is lost
Answer: B
Objective: III.9
Why: Answer B. Random-access memory needs power to hold data. Disk and solid-state storage do not. Anything done after the last save can disappear in a crash. That is why a long optimization is saved at defined points, and why the archive that will be used next year is the copy written to durable storage, not the session on the screen. A crash does not approve a plan.

### Q3
Stem: A RAID 5 array in the planning server loses one disk and keeps serving plans without interruption. The next week a corrupted script deletes the clinical database on that array. Why did RAID not save the database?
A. RAID 5 rebuilds deleted files from parity after any software deletion
B. RAID protects against a disk failure by spreading parity; it does not keep a logical backup of files a person or a script has deleted or encrypted
C. RAID 5 is an offsite archive by definition
D. Parity means each plan is stored in a second building
Answer: B
Objective: III.9
Why: Answer B. RAID 5 can reconstruct one failed disk from parity spread across the other disks. That is availability during a hardware failure. A delete, a bad script, or ransomware writes the destruction to the array as ordinary data, and the parity is updated to match the destruction. Recovery then depends on a backup that was taken earlier and stored somewhere the script did not reach. RAID is not an offsite archive.

### Q4
Stem: A planner says "the algorithm" and "the data" as if they were the same file. Which distinction is correct?
A. The algorithm is the procedure the software follows; the data are the patient's images, contours, and machine beam tables the procedure runs on
B. The algorithm is the CT dataset; the data are the vendor's source code
C. They are required to be one file so a beam-data edit cannot change dose
D. Data are volatile by definition and algorithms live only in RAM
Answer: A
Objective: III.9
Why: Answer A. An algorithm is the set of steps: how fluence is optimized, how density is converted, how dose is summed. Data are the inputs those steps read: this patient's CT, this structure set, and the commissioned beam model. Editing the beam data changes the dose even when the algorithm version is unchanged, which is why beam data are access-controlled and why a software upgrade and a beam-data change are separate events to validate. They are not one indivisible file.

### Q5
Stem: A checksum computed on an RT Plan file before transfer does not match the checksum computed after the file arrives. What does that mismatch mean?
A. The plan is clinically the better of the two copies, and it should be treated
B. At least one bit changed in transit; the received file is not the file that was sent and should not be imported as if it were
C. Checksums only compare patient names, so a mismatch means a new last name
D. A mismatch is expected for DICOM and confirms a successful C-STORE
Answer: B
Objective: III.9
Why: Answer B. A checksum is a short fingerprint of every byte in the file. If the fingerprint differs, the bytes differ. That can be a truncated transfer, a disk error, or a file that was edited. The safe action is to repeat the transfer and confirm the fingerprints match before the plan is used. A checksum does not score clinical quality, does not read the patient's name as its only input, and a mismatch is a failure, not a successful DICOM store.

## Computer Systems Management

### Q1
Stem: Which statement correctly separates an archive from a backup for a radiotherapy planning system?
A. The archive is the kept clinical record; the backup is a restorable copy made so a failure can be recovered; neither replaces the other
B. A backup is the legal record, and an archive is only a desktop shortcut
C. They are the same task, so a single copy on the planning server satisfies both
D. An archive must be stored only on the same disk as the live database so restore is faster
Answer: A
Objective: III.9
Why: Answer A. The archive is what the department retains so a plan can be looked up years later for a retreatment or a legal question. The backup is the copy used to rebuild the system after a crash, a flood, or a bad upgrade. A backup that is never restored has not been shown to work. An archive sitting only on the live server is lost with the server. One copy in one place fails both jobs.

### Q2
Stem: The hospital information-technology group plans to apply an operating-system security patch to the treatment-planning server tonight, without the treatment-planning vendor. What is the appropriate process?
A. Patch immediately; operating-system changes cannot affect a commissioned planning system
B. Hold the patch until the vendor and the physicist have cleared it; an untested system library change can stop the database or change calculation behavior
C. Patch only the dose algorithm and leave the operating system alone, because they are the same software
D. Apply the patch on the treatment machine console first, as the least critical computer
Answer: B
Objective: III.9
Why: Answer B. A commissioned planning system is a combination of operating system, database, and application that was tested together. A security patch can replace libraries the dose engine or the database uses. Change control means the vendor's compatibility statement, a planned window, a backup taken first, and a physicist check that plans still open and a known test case still calculates. Patching the treatment console first is the higher-risk machine, not the lower-risk one.

### Q3
Stem: A script is shared with the department. It sets every new plan's normalization so that 100% equals the dose at isocenter, and it sets the prescription dose equal to that 100%. Several physicians prescribe to the 95% isodose instead. What can this script do if it is run without checking the prescription?
A. Nothing harmful; normalization scripts read the physician's intent from the DVH automatically
B. It can rescale the plan to the wrong isodose, so the target receives a different dose than the one the physician wrote
C. It can change isocenter dose without changing monitor units
D. It only renames beams, so the dose distribution is untouched
Answer: B
Objective: III.9
Why: Answer B. A script does exactly what it was coded to do, on every plan it is pointed at. If the code assumes "prescription equals dose at isocenter" and the real prescription is "200 cGy to the 95% line," the delivered dose is wrong by the ratio 100/95, about 5 percent, on every patient the script touches. That is a systematic error, which is the dangerous kind. Scripts do not infer intent, and a normalization change that does not change monitor units would not change dose. Review of the first cases, and a script that refuses to run when the prescription type does not match, is part of releasing it.

### Q4
Stem: Two workstations open the same plan. Planner A changes the cord constraint and saves. Planner B, who opened the plan earlier, saves afterward and overwrites A's change. What system feature prevents this class of error?
A. A shared generic login, so the audit trail shows only "staff"
B. Record locking or version control, so the second save cannot silently overwrite the first, plus an audit log of who changed the plan
C. Turning off backups, so only one copy of the plan can exist
D. Storing the plan only in RAM on workstation B
Answer: B
Objective: III.9
Why: Answer B. Clinical plans are a shared record. Without locking or a version check, the last save wins and the cord constraint disappears with no alarm. An audit log that uses individual accounts shows who overwrote what. A shared password makes that investigation impossible. Removing backups or keeping the plan only in RAM protects nothing and loses the record.

### Q5
Stem: The database server fails on a treatment day. The backup from last night was restored last month as a drill, and a newer backup from last night has never been restored. What is the strongest statement about those backups?
A. Both are proven, because a backup file that exists will always restore
B. Last month's drill showed that the restore procedure worked for that backup; last night's file is not proven until it is restored, and the drill should be repeated on a defined schedule
C. A restore drill contaminates the backup, so tested backups must not be kept
D. Restores are only valid for image files, not for the plan database
Answer: B
Objective: III.9
Why: Answer B. A backup is a hypothesis until a restore succeeds. The drill last month is evidence about the procedure and about the backup that was used then. It is not proof that last night's job finished, that the tape or disk is readable, or that the restored database matches the live one. The operational response to today's failure is the documented downtime procedure, which may include treating only with a verified backup or postponing, according to department policy. Image files and plan databases both need tested restores.

## Computers Mini-Quiz

### Q1
Stem: A planner exports an approved plan to the record-and-verify system, then changes the multileaf pattern in the planning system and does not re-export. The patient is treated from the record-and-verify copy. Which plan is delivered, and what is the failure?
A. The edited plan, because the two systems share RAM
B. The previously exported plan; the treatment copy and the planning copy have diverged, and there is no longer a single approved version
C. Neither; DICOM updates the treatment unit automatically when the planning file changes
D. A blend of the two multileaf patterns, averaged control point by control point
Answer: B
Objective: III.9
Why: Answer B. Export makes a copy. Later edits in the planning system do not push themselves to the treatment system unless someone sends them and the receiving system is updated under a controlled process. Treating the older export while the planning system shows a newer, unapproved pattern means the team is no longer looking at the plan the machine will deliver. The fix is version identity: one approved plan, transferred completely, and a check that the treatment system matches that approval. Systems do not average multileaf control points across versions.

### Q2
Stem: Which stored item is beam data rather than a patient-specific file?
A. This patient's RT Structure Set
B. The commissioned percent-depth-dose and output tables for 6 MV on linac 2
C. Today's cone-beam CT
D. The physician's prescription note in the chart
Answer: B
Objective: III.9
Why: Answer B. Beam data belong to the machine and the planning model: depth doses, profiles, output factors, wedge factors, and the density curve. They affect every patient calculated with that model. A structure set, a cone-beam CT, and a prescription note are patient-specific. Editing a 6 MV output table is a commissioning change, not a planning tweak, and it is controlled more tightly than a single patient's contours for that reason.

### Q3
Stem: A voxel in the dose grid is 3 mm on a side. A planner reports a "point dose" of 62 Gy in the cord from that grid. What is that number physically?
A. The dose in a mathematical point with no size
B. A value representing dose over a 3 mm voxel (and often interpolated from the calculation grid), not an infinitesimal point
C. The average dose in the entire cord, regardless of grid size
D. 62 Gy only if the voxel is 3 cm
Answer: B
Objective: III.9
Why: Answer B. A dose grid does not store infinitely small points. Each value is the dose assigned to a voxel, here a 3 mm cube, after the algorithm samples the fluence. A reported maximum can be one hot voxel or an interpolation among voxels. That is why a cord maximum on a coarse grid is a weaker number than a maximum on a fine grid, and why small serial structures are calculated with a tighter grid. It is not the mean cord dose, and the stated voxel is 3 mm, not 3 cm.

### Q4
Stem: The oncology information system, the planning system, and the picture-archiving system all hold data about one patient. Which division of roles is the usual one?
A. The picture archive stores the diagnostic and planning images, the planning system calculates dose, and the oncology information system runs scheduling, record-and-verify, and the treatment chart
B. The picture archive calculates monitor units, and the planning system only stores appointments
C. All three are required to be the same application, so a failure of one is impossible
D. The oncology information system is prohibited from storing DICOM images
Answer: A
Objective: III.9
Why: Answer A. The picture-archiving system is the image library. The treatment-planning system is where contours, beams, and dose are created. The oncology information system is where the appointment, the approved plan, the daily treatment record, and the images used for setup live together. They exchange DICOM and clinical messages, and they fail separately, which is why each needs its own backup and a downtime plan. The archive does not calculate monitor units.

### Q5
Stem: A new script library is placed on the shared drive. It has no version number, no named author, and no test patient. A planner runs it on a clinical case because "the file date is today." What is missing?
A. Nothing; today's date commissions a script
B. Controlled release: a version, an owner, a test on a phantom or a standard patient, and a statement of which prescription types it is allowed to touch
C. A lossy compression step before the script is allowed to read contours
D. A rule that scripts may only run with the energy above 10 MV
Answer: B
Objective: III.9
Why: Answer B. A script that edits clinical plans is software. The minimum control is the same idea as a plan check: someone owns it, the version on the shared drive is the version that was tested, and the test shows what it does to contours, normalization, and beam names. A file date does not do that. Compression and a high-energy restriction are unrelated and, in the energy case, actively unsafe for patients with implanted electronics.
