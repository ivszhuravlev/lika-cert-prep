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
Why: Answer B. TG-203 combines the dose band with whether the patient needs the device to sustain a heartbeat. A malfunction that would be a transient mode change in a non-dependent patient can be a loss of cardiac output in a dependent one. At 1.5 Gy the dose band is low, under 2 Gy. Dependence moves that patient up one category, to intermediate. Dose is not the only axis. Dependence is relevant at 6 MV, not only at high energy.

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

### Q6
Stem: A 6 MV pelvic course is estimated to deliver 1.6 Gy to a pacemaker that sits outside the jaws. The patient is not pacing dependent. Which TG-203 category does this exam assign before any other flag is applied?
A. Low, because the device dose is under 2 Gy and the patient is not pacing dependent
B. Intermediate, because every pacemaker dose of 1 Gy or more is the middle band
C. High, because a cardiac device is high risk at 6 MV even when the dose is under 2 Gy
D. Exempt, because 1.6 Gy is under the historical TG-34 citation and no category applies
Answer: A
Objective: III.13
Why: Answer A. The dose bands are low under 2 Gy, intermediate from 2 Gy through 5 Gy, and high above 5 Gy. At 1.6 Gy a patient who is not pacing dependent stays low. The energy is 6 MV, so the neutron flag is not raised, and the generator is outside the beam. Intermediate starts at 2 Gy. The historical TG-34 citation of 2 Gy does not erase the category, and a dose under that citation is not a reason to skip the band.

### Q7
Stem: The same 6 MV plan delivers an estimated 1.6 Gy to the generator, and this patient is pacing dependent. How does dependence change the category?
A. It does not. Under 2 Gy every patient stays low, dependent or not
B. It moves the patient up one category, from low to intermediate
C. It moves the patient two categories, from low to high, because dependence skips the middle band
D. It lowers the category, because a dependent patient is already monitored and the dose no longer counts
Answer: B
Objective: III.13
Why: Answer B. Read the dose band first. Under 2 Gy is low for a patient who is not dependent. Pacing dependence moves the patient up one category, so this patient is intermediate. There is no skip from low to high at this dose. Dependence does not make the dose smaller. A dose under 2 Gy is not always the low category, and it is not a statement that the device is safe.

### Q8
Stem: The estimated generator dose is 2 Gy from a 6 MV plan. The patient is not pacing dependent. A colleague says 2 Gy is the low band and is therefore safe. What is wrong with that reading?
A. Nothing. TG-203 calls every dose of 2 Gy or less the low band, and low means safe for every generator
B. 2 Gy is already high, so the colleague should have said high rather than low
C. On this exam 2 Gy is the start of the intermediate band, not the low band, and 2 Gy is not a dose that is always safe
D. 2 Gy is a neutron fluence, so the band system does not apply at 6 MV
Answer: C
Objective: III.13
Why: Answer C. Low is under 2 Gy. Intermediate runs from 2 Gy through 5 Gy, so 2 Gy itself is intermediate for a patient who is not pacing dependent. The older TG-34 citation of 2 Gy is why the number feels like a universal ceiling. TG-203 replaced that single figure. Calling 2 Gy safe ignores the middle band, ignores a pacing-dependent patient who would move up again, and ignores neutrons if the energy were above 10 MV.

### Q9
Stem: A 6 MV plan is estimated to deliver 4 Gy to a defibrillator. The patient is pacing dependent. Which category applies?
A. Low, because 4 Gy is under 2 Gy once dependence is included
B. Intermediate, because dependence does not change a dose that is already between 2 Gy and 5 Gy
C. Intermediate, because a defibrillator uses a different band that tops out at 10 Gy
D. High. The dose is in the intermediate band, and pacing dependence moves the patient up one category
Answer: D
Objective: III.13
Why: Answer D. From 2 Gy through 5 Gy the band is intermediate. A pacing-dependent patient moves up one category, to high. A defibrillator uses the same bands as a pacemaker. Dependence does not pull a 4 Gy estimate under 2 Gy. The generator still has to stay out of the direct beam, and interrogation before and after is still required.

### Q10
Stem: A 6 MV estimate to the generator is 6 Gy. The patient has an intrinsic rhythm and is not pacing dependent. Which category applies, and what does dependence do at this dose?
A. High. Above 5 Gy the category is high without dependence. A pacing-dependent patient at 6 Gy is also high. There is no category above high
B. Intermediate, because 6 Gy is only 1 Gy past 5 Gy and the middle band absorbs that
C. Low, because the patient is not pacing dependent and dependence is the only way to reach high
D. High only for a pacemaker. A defibrillator at 6 Gy stays intermediate
Answer: A
Objective: III.13
Why: Answer A. High is a device dose above 5 Gy. Dependence is not required to reach it. If this patient were pacing dependent, the category would stay high. The step up cannot create a fourth band. A defibrillator is classified with the same bands. Six gray is not a safe result and it is not the middle band. The beams still should not enter through the generator, and the device team still interrogates before and after.

### Q11
Stem: The planning system shows 0.8 Gy to a pacemaker outside a pelvic field. The plan uses 18 MV. The patient is not pacing dependent. A colleague keeps 18 MV because 0.8 Gy is the low band. What is the neutron decision?
A. Agree. Under 2 Gy is safe at every energy, including 18 MV
B. Disagree. Above 10 MV the beam produces neutrons, and that neutron exposure is high risk even when the photon estimate is under 2 Gy. Bring the energy to 10 MV or below
C. Agree if the patient is pacing dependent, because dependence cancels neutrons
D. Disagree only when the estimate is above 5 Gy. Under 2 Gy, 18 MV is the preferred energy
Answer: B
Objective: III.13
Why: Answer B. The dose band alone would be low: 0.8 Gy, not pacing dependent, and outside the jaws. Neutrons from a beam above 10 MV are a separate flag. TG-203 manages neutron-producing irradiation as high risk, so the low gray value does not license 18 MV. Being outside the field does not stop neutrons. Dependence does not cancel them. The planning rule stays: 10 MV or below, device out of the direct beam, a real estimate, interrogation before and after. Two gray is not always safe, and neither is 0.8 Gy on an 18 MV plan.

### Q12
Stem: A review sheet says “keep every pacemaker under 2 Gy” and attributes that sentence to TG-34. How should that 2 Gy figure be used on this exam?
A. As the TG-203 low band, which is safe for a pacing-dependent patient and for an 18 MV beam
B. As the high-band threshold, so any dose under 5 Gy is low
C. As the historical TG-34 citation. TG-203 uses low under 2 Gy, intermediate from 2 Gy through 5 Gy, and high above 5 Gy. Two gray is not a dose that is always safe
D. As a daily fraction limit, so a course may deliver 2 Gy to the generator at every fraction
Answer: C
Objective: III.13
Why: Answer C. TG-34 is the older report, and 2 Gy is the single number reviews still quote from it. TG-203 replaced that habit with three bands plus a step up for pacing dependence, and with high-risk management when the energy is above 10 MV. Two gray is the start of the intermediate band, not a clearance. It is not the top of the low band, it is not the high threshold, and it is not a per-fraction allowance.

### Q13
Stem: Two patients, neither pacing dependent, are planned at 6 MV with the generators outside the beam. One estimate is 5 Gy. The other is 5.4 Gy. How do the bands differ, and which fact is still true of both?
A. Both are low, because 5 Gy is the TG-34 safe dose and 5.4 Gy rounds down
B. 5 Gy is high and 5.4 Gy is intermediate, because the bands reverse above 5 Gy
C. Both are high, because intermediate stops at 2 Gy
D. 5 Gy is intermediate, because that band runs through 5 Gy. 5.4 Gy is high, because high is above 5 Gy. Neither number means the dose is always safe, and both still need the device out of the beam and interrogation before and after
Answer: D
Objective: III.13
Why: Answer D. Intermediate is 2 Gy through 5 Gy, so 5 Gy is still intermediate for a patient who is not pacing dependent. High starts above 5 Gy, so 5.4 Gy is high. A pacing-dependent patient at 5 Gy would move up to high. Rounding 5.4 Gy into the middle band is the wrong direction. Five gray is not a universal safe dose. The behavioral rules do not turn off in either band: stay at 10 MV or below, keep the generator out of the direct beam, and interrogate before and after.

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

### Q20
Stem: A pacemaker contour lies outside the calculated grid. The planning system reports 0 Gy to the generator for a 6 MV pelvic course. What is that 0 Gy?
A. A measured out-of-field dose
B. Proof the device is under every management band in the cardiac-device report
C. A neutron dose, so the energy can be raised to 18 MV
D. Not an estimate. The grid never reached the device, so the grid is extended or the dose is measured
Answer: D
Objective: III.13
Why: Answer D. A displayed 0 Gy from a contour outside the grid has not scored leakage and patient scatter. Out-of-field dose is a weak point of many algorithms. The number brought to the device report is an estimate that includes that region, or a measurement. It is not a reason to add a neutron-producing energy.

### Q21
Stem: One memorized generator limit, 2 Gy, is applied to every pacemaker and every defibrillator. What is wrong with that habit?
A. Nothing. The cardiac-device report replaced dependence and vendor guidance with a single 2 Gy ceiling
B. The report combines pacing dependence with the estimated device dose. One gray value is not the limit for every generator
C. The 2 Gy figure applies only when the energy is 18 MV
D. Defibrillators are exempt from any dose estimate
Answer: B
Objective: III.13
Why: Answer B. Management scales with pacing dependence and with the estimated device dose. The bands are low under 2 Gy, intermediate from 2 Gy through 5 Gy, and high above 5 Gy. Dependence moves the patient up one category. Two gray is the historical TG-34 citation and the start of the intermediate band, not a dose that is always safe, and 5 Gy is not a universal safe dose. Energy above 10 MV adds neutrons and is managed as high risk.

### Q22
Stem: Three gold prostate markers are contoured as the gross target, and the energy is raised from 6 MV to 18 MV because the markers are high-Z. Which statement matches their use?
A. They are a localization surrogate, not the gross target. They perturb dose locally and are not a reason to raise the photon energy
B. They are the gross target, and 18 MV is required so the markers do not cast a shadow
C. They replace a rectal spacer and are overridden as air
D. A bony match is preferred, because the markers cannot move relative to the gland
Answer: A
Objective: III.13
Why: Answer A. Markers represent the target when the protocol says they do. They are not the tumor volume. High-Z seeds perturb dose in a small region. Neutrons from 18 MV are not the remedy. A bony match can look acceptable while the gland and the seeds have moved.

### Q23
Stem: Hydrogel between the prostate and the rectum is contoured as rectum. Its CT appearance is near soft tissue, and that contour is overridden to air. What is the error?
A. None. Spacer gel is air and is part of the rectum
B. None. The gel is a lead shield, and air is a conservative override
C. The gel is its own structure, near water or soft tissue. It is not rectum, air, or metal
D. The override is required because gel has the density of cortical bone
Answer: C
Objective: III.13
Why: Answer C. Contour the spacer as its own structure. Do not assign it to rectum or to prostate, and do not override it as air or as metal. It works by distance. It does not stop the beam the way lead does.

### Q24
Stem: A rectal constraint was met only because spacer gel held about 1 cm between the prostate and the rectum. On a later scan the gel has been absorbed and the gap is gone. What follows?
A. The original rectal histogram still describes the anatomy now being treated
B. Loss of the gel lowers the rectal dose with no new calculation
C. Absorption of the gel is a change in beam energy
D. The plan that passed because of the gap does not still pass when the gap is gone. The geometry is rechecked
Answer: D
Objective: III.13
Why: Answer D. Spacer gel can shift or be absorbed. A gap that shrinks is a change in anatomy. Rectal dose that depended on that centimeter of separation is not the dose on the later scan. Absorption is not an energy change, and it does not by itself spare the rectum.

### Q25
Stem: A cochlear implant sits beside a head-and-neck target. The stem prints no gray limit for that implant. Which planning behavior fits?
A. Treat through it at 18 MV, because only cardiac devices have a neutron concern
B. Keep it out of the primary beam, avoid neutron-producing energies, follow the vendor instruction, and do not invent a gray limit
C. Contour it as a fiducial and match the isocenter to the implant instead of to the target
D. Override it to air so the dose to the device becomes zero
Answer: B
Objective: III.13
Why: Answer B. A cochlear implant, a deep-brain stimulator, or a pain pump is the same class of problem as other electronics: out of the primary beam, energy at or below about 10 MV unless qualified guidance says otherwise, the vendor's instruction, and a documented check. A number the stem did not give is not a limit to invent. An air override does not remove the hardware, and the implant is not the localization surrogate.
