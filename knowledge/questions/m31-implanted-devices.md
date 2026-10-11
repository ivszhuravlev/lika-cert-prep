# Module 31 — Implanted devices

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Pacemakers

### Q1
Stem: A patient with an implanted cardioverter-defibrillator needs pelvic radiotherapy. The device is in the left upper chest, well outside the planned fields. A colleague proposes 18 MV photons to improve penetration through a large separation. What is the device-related objection?
A. There is none; a device outside the collimated field cannot be affected
B. Photons above 10 MV produce photoneutrons in the linac head, and those neutrons can upset a cardiac device even when it is outside the primary beam
C. 18 MV is forbidden because the photoelectric effect in the device is stronger at 18 MV than at 6 MV
D. The objection applies only to pacemakers, not to defibrillators
Answer: B
Objective: III.13
Why: Answer B. AAPM TG-203 treats neutron-producing beams as a device hazard. The photonuclear threshold in the high-Z materials of the head is near 8 to 10 MV, so 15 MV and 18 MV beams generate neutrons that reach the patient and the generator even outside the geometric field. The practical rule is to plan these patients with 10 MV or below, commonly 6 MV. Being outside the jaws is not enough. The photoelectric effect actually falls as energy rises, so C has the physics backward. Defibrillators are cardiac implantable devices under the same guidance, and a shock-therapy malfunction is part of the risk, not a reason to ignore it.

### Q2
Stem: The treatment-planning system reports 0.3 Gy to a pacemaker 6 cm outside the field edge over the full course. Why is that number not sufficient by itself to classify the patient?
A. Out-of-field dose from leakage and patient scatter is poorly modeled by many planning systems, which often underestimate it; TG-203 risk bands need a conservative estimate or a measurement
B. Planning systems overestimate out-of-field dose by a fixed factor of 100, so the true dose is 0.003 Gy and no further work is required
C. Any displayed dose below 2 Gy is defined as zero for cardiac devices
D. The displayed dose is already a neutron dose, so the beam energy does not matter
Answer: A
Objective: III.13
Why: Answer A. Collimator scatter, head leakage, and internal patient scatter dominate far outside the field. Commissioned beam models are built to be accurate inside and near the field, not at 6 cm and beyond, and they do not include a full photoneutron calculation. TG-203 uses device-dose bands of under 2 Gy, 2 to 5 Gy, and above 5 Gy, together with pacing dependence, to set the management level. Those bands should be entered with a conservative out-of-field estimate or a measurement, not with an optimistic planning-system tail. The display is not automatically a neutron dose, and a number under 2 Gy is a low band only if it is believable and the patient is not pacing dependent.

### Q3
Stem: Two patients will each receive an estimated 1.5 Gy to the generator from a 6 MV plan. One is pacing dependent. The other has an intrinsic rhythm and rarely uses the pacemaker. How does dependence change the TG-203 management?
A. It does not; only the dose band matters, so both patients are managed identically
B. Dependence raises the risk category at the same device dose, so the pacing-dependent patient needs closer cardiac and treatment-time precautions
C. Dependence lowers the risk, because a dependent patient cannot have a clinically noticeable malfunction
D. Dependence matters only if the energy is above 18 MV
Answer: B
Objective: III.13
Why: Answer B. TG-203 combines the dose band with whether the patient needs the device to sustain a heartbeat. A malfunction that would be a transient mode change in a non-dependent patient can be a loss of cardiac output in a dependent one. At the same 1.5 Gy (the under-2 Gy band) the dependent patient is managed more aggressively: cardiology involvement, interrogation around the course, and the monitoring the department's policy assigns to that higher category. Dose is not the only axis. Dependence is relevant at 6 MV, not only at high energy.

### Q4
Stem: A left chest-wall plan would otherwise enter through a pacemaker generator. The device cannot be moved before the start date. Which planning decision agrees with device guidance?
A. Keep the entrance through the generator and add 1 cm of bolus over it to harden the beam
B. Rearrange the beams so the generator is out of the primary beam, keep the energy at or below 10 MV, and estimate the scattered dose
C. Switch from 6 MV to 18 MV so the dose to the metal falls
D. Ignore the generator because TG-203 applies only to abdominal implant sites
Answer: B
Objective: III.13
Why: Answer B. Direct irradiation of the generator is the high-dose situation the guidance tells the planner to design away. Alternative angles, a change in technique, or a discussion about relocating the device are the tools. Bolus over the can does not make primary beam acceptable, and it may increase the dose to the device. Raising the energy adds neutrons. The anatomic site of the implant is not limited to the abdomen; chest-wall and breast cases are a common version of this problem because the device sits near the field.

### Q5
Stem: Before and after a course that delivers dose near a defibrillator, the cardiology service interrogates the device. During treatment the therapist asks whether to place a magnet on the generator for every fraction "so it will be safe." What is the right response?
A. Yes; a magnet is part of the immobilization mold and does not change device behavior
B. No; a magnet can suspend tachycardia therapy on a defibrillator, and that decision belongs to cardiology, not to a routine setup
C. Yes, but only if the plan uses 18 MV, because the magnet absorbs neutrons
D. No; interrogation itself reprograms the linac energy
Answer: B
Objective: III.13
Why: Answer B. For many defibrillators a magnet disables shock therapy while it is in place. That might be what cardiology wants for a monitored fraction, or it might leave the patient unprotected from a real arrhythmia. It is a clinical decision documented by the device team, not a setup shortcut. A magnet is not a neutron shield and is not an immobilization device. Interrogation reads and may reprogram the generator; it does not change the treatment machine energy.

## Implanted Devices Mini-Quiz

### Q1
Stem: Three gold fiducials were implanted in the prostate. On today's orthogonal images two fiducials match the plan and the third has moved 1.5 cm inferiorly, consistent with migration. How should localization use the markers?
A. Average all three, so the migrated seed pulls the isocenter inferiorly
B. Match to the stable pair, and do not let the migrated seed define the gland; report the migration
C. Match to the migrated seed only, because it has the largest signal
D. Abandon fiducials and match the pelvic bones for the rest of the course without telling anyone
Answer: B
Objective: III.13
Why: Answer B. Fiducials are a surrogate, not the tumor. A seed that has migrated into the periprostatic tissue or toward the bladder no longer marks the gland. Including it in the average shifts the true prostate off the plan. The stable seeds still carry the localization, and the physician should know a marker has moved because a future fraction may lose another one. Bone match is the wrong primary surrogate for prostate when markers were placed specifically because the gland moves relative to bone.

### Q2
Stem: A prostate CT shows bright and dark streaks between two hip prostheses. The uncorrected plan uses a pencil-beam algorithm and sends both lateral beams through the metal. Which planning response is appropriate?
A. Trust the pencil-beam dose behind the metal; high-Z implants are accurately handled by pencil beam
B. Keep the laterals but override the black streaks to air so the metal "stands out"
C. Avoid beam entrance through the prostheses when the target can be covered otherwise, override artifact streaks to tissue rather than air, and do not rely on pencil beam for the dose in the shadow of the metal
D. Delete the prostheses from the contour set so they do not affect the image
Answer: C
Objective: III.13
Why: Answer C. A hip prosthesis both attenuates the beam and creates streak artifact. The dark streaks are reconstruction error, not gas; overriding them to air makes the calculation even less like the patient. Pencil-beam and simple convolution models handle the lack of lateral equilibrium and the high-Z interface poorly. If a beam must pass through the implant, a more appropriate algorithm and a defined density for the metal are required, and a measurement may be needed. Deleting the contour hides the problem and leaves the bad Hounsfield numbers in the dose grid.

### Q3
Stem: A hydrogel spacer is placed between the prostate and the rectum after the planning CT, and treatment is about to start on that pre-procedure scan. On CT the gel looks similar to soft tissue. What is the planning problem?
A. None; the spacer is a radiation shield equivalent to several millimeters of lead, and the old CT is conservative
B. The planning CT does not contain the anatomy that will be treated; the rectal wall will sit farther from the prostate, and the gel is not a shield
C. The gel adds a known 10 Gy to the rectum and must be included as a source
D. Hydrogel is visible only on megavoltage port films, so the CT is the correct geometry by definition
Answer: B
Objective: III.13
Why: Answer B. A rectal spacer works by distance. It moves the rectal wall away from the prostate, typically on the order of a centimeter, and it is absorbed over the following months. It does not stop photons or protons the way lead does. A CT performed before placement has the wrong rectal position, the wrong target relationships, and no representation of the gel. The patient needs a planning dataset that shows the post-procedure anatomy (often with MRI, because the gel's CT contrast is subtle). Treating on the pre-gel scan calculates the wrong organ dose.

### Q4
Stem: A patient wears a continuous glucose monitor and an insulin pump on the abdomen. The abdomen is inside a palliative anterior-posterior pair. The devices are electronic and the manufacturer lists a radiation limit well below the planned dose. What should the plan and the treatment pathway do?
A. Treat through the devices; consumer electronics are unaffected by megavoltage dose
B. Move the sensors and pump out of the primary beam when that is possible, identify a glucose-check backup with the patient, and do not assume the displayed glucose during the beam is valid
C. Increase the energy above 10 MV so the electronics see fewer photons
D. Contour the pump as a fiducial and match to it daily instead of to the target
Answer: B
Objective: III.13
Why: Answer B. Continuous glucose monitors and insulin pumps are implantable or wearable electronics with dose limits far below a therapeutic fraction. Direct irradiation can damage the sensor or the pump and can make the reading wrong at the moment it is most needed. They should be out of the primary beam if the anatomy allows, the patient needs a non-irradiated way to check glucose, and the device clinic should be involved when the manufacturer's limit will be exceeded. Raising the energy adds neutrons, which is the wrong direction for electronics. The pump is not a target surrogate.

### Q5
Stem: A postmastectomy chest wall will be treated with 9 MeV electrons. The reconstruction includes a tissue expander with a dense magnetic port on the chest wall, inside the electron field. Using the practical-range rule of about E/2 in centimeters, what is the main dosimetric concern at the port?
A. The port is nearly transparent to 9 MeV electrons, so the chest wall under it receives the same dose as the surrounding tissue
B. The high-Z port attenuates and backscatters electrons; tissue in its shadow can be underdosed, and the practical range of about 4.5 cm does not describe the path through metal
C. The port focuses electrons and doubles the skin dose uniformly across the whole chest wall
D. The magnet removes the bremsstrahlung contamination, so the energy should be raised to 20 MeV to compensate
Answer: B
Objective: III.13
Why: Answer B. Nine MeV electrons have a practical range near 9/2 = 4.5 cm in water, which is why that energy was a candidate for a chest wall. A dense metal port is not water. It stops and backscatters electrons, so the tissue distal to the port can be cold while the upstream surface gets extra backscatter. The port has to be contoured, the shadow considered in the plan, and a different energy, a photon plan, or a port-aware arrangement discussed if the cold spot covers target. The magnet does not collimate the beam into a uniform skin boost, and it does not clean up photon contamination.
