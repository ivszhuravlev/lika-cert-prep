# Module 42. QA and Standard of Care

Original items. Written for the RM Review porting wave; gaps in isocenter film tests, calibration intervals, the TG-40 to TG-142 transition, safety-culture numbers, source drift, end-to-end tests, and TG-275.

## Isocenter Tests: Star Shot, Spoke Shot, and Winston–Lutz

### Q1
Stem: A physicist wants to measure the gantry rotation axis with a film test. How is the film placed, and what is the test called?
A. Flat on the couch at isocenter height, called a collimator star
B. Flat on the couch while the couch is rotated, called a couch star
C. Taped to the gantry head so it turns with the beam, called a Winston–Lutz test
D. Held vertically in the plane of gantry rotation with a narrow slit along the gantry axis, called a spoke shot
Answer: D
Objective: VII.9
Why: The gantry star, or spoke shot, needs the film perpendicular to the gantry axis, so it stands vertically in the plane the gantry sweeps, and the narrow slit field draws one line per gantry angle through the isocenter. A film lying flat on the couch is perpendicular to the beam, not to the gantry axis, so it serves the collimator star (collimator rotated) or the couch star (couch rotated). A film attached to the head turns with the beam and records nothing about the axis. Winston–Lutz images a ball bearing, not a slit on film.

### Q2
Stem: On an SRS-capable linac, the collimator star-shot lines bound a smallest circle whose diameter is 1.6 mm. What result is reported, and does it meet the TG-142 SRS tolerance?
A. 1.6 mm, which fails the 1 mm SRS tolerance
B. 0.8 mm, which passes the 1 mm SRS tolerance
C. 0.8 mm, which fails because SRS requires 0.5 mm
D. 3.2 mm, which fails the 2 mm conventional tolerance
Answer: B
Objective: VII.9
Why: The star-shot result is the radius of the minimum circle touching all lines, and TG-142 writes the radiation-isocenter tolerance as a radius: 1 mm for SRS/SBRT and 2 mm otherwise. Half of 1.6 mm is 0.8 mm, which is under 1 mm, so the collimator axis passes. Reporting 1.6 mm confuses diameter with radius and produces a false failure. There is no 0.5 mm SRS line in TG-142. Doubling to 3.2 mm has no basis. Check: 0.8 × 2 = 1.6 mm, and 1.0 − 0.8 = 0.2 mm of margin.

### Q3
Stem: What does a Winston–Lutz test measure that a set of three star shots does not?
A. The offset between a radiopaque ball placed at the setup isocenter and the field center, imaged at combined gantry, collimator, and couch angles
B. The radius of the collimator rotation axis alone
C. The leaf-position accuracy of the multileaf collimator
D. The absolute output of the beam in water
Answer: A
Objective: VII.9
Why: Winston–Lutz places a small ball at the isocenter defined by the lasers or the couch pointer and images it through a small field at the gantry, collimator, and couch combinations the treatment will use; the largest ball-to-field offset is the result, at or under 1 mm for SRS. It therefore tests the whole chain, setup system to beam, rather than one axis. The star shot isolates each rotation axis separately. Leaf-position accuracy is the picket-fence test. Absolute output is TG-51.

### Q4
Stem: During a couch star shot, which component is rotated between exposures, and what does a circle that will not close to a small radius most likely indicate?
A. The collimator is rotated; a large radius means the jaws are miscalibrated
B. The gantry is rotated; a large radius means the gantry sags
C. The couch is rotated with gantry and collimator fixed; a large radius means the couch rotation axis wanders, for example from sag under load or bearing play
D. The couch is translated longitudinally; a large radius means the ODI is off
Answer: C
Objective: VII.9
Why: The couch star holds the gantry and collimator still, exposes a slit field, rotates the couch to several angles, and re-exposes; the lines intersect at the couch rotation axis, and a wide minimum circle means that axis is not fixed, as with a sagging or worn couch. Rotating the collimator is the collimator star and rotating the gantry is the spoke shot. Translation does not test a rotation axis, and the ODI is a distance readout checked separately.

## Calibration Intervals, Secondary MU Checks, and the TG-40 to TG-142 Transition

### Q1
Stem: How often should the reference ionization chamber and electrometer used for TG-51 output calibration be returned to an Accredited Dosimetry Calibration Laboratory?
A. Every month, with the output check
B. Every six months, with the leak tests
C. Every two years, and after any repair
D. Every five years, when the TG-51 protocol is revised
Answer: C
Objective: VII.1
Why: The AAPM recommendation this bank uses is an ADCL recalibration of the reference chamber and electrometer every two years, plus after any repair or suspected damage; the well-type chamber for brachytherapy follows the same cycle. Monthly and six-monthly intervals are machine-QA and sealed-source cadences, not chamber calibration cadences. Five years would let the calibration coefficient drift undetected across hundreds of annual and monthly measurements that depend on it.

### Q2
Stem: Under the NRC survey requirements, how often must a clinic's survey meters be calibrated?
A. Annually, and after repair
B. Every two years, like the reference chamber
C. Only when the battery check fails
D. Once at purchase; the daily background check suffices afterward
Answer: A
Objective: VII.9
Why: 10 CFR 20.1501 requires that instruments used for required surveys be calibrated periodically for the radiation measured, and the licence condition clinics operate under is annual calibration plus recalibration after repair. The two-year interval belongs to the ADCL calibration of the reference dosimetry chamber. A battery check and a daily background or check-source reading confirm the instrument works that day; they do not establish its calibration.

### Q3
Stem: A planning system computes 180 MU for a homogeneous point in a conventional open field. The independent check program gives 188 MU. The clinic's action level for that geometry is 3 percent. What is the discrepancy and the outcome?
A. 4.4 percent, over the action level, so the plan is investigated before the first fraction
B. 4.3 percent, within the 5 percent level that applies to every check
C. 8 percent, so the delivered MU is changed to 188
D. 2.2 percent, under the action level, so the plan proceeds
Answer: A
Objective: VII.2
Why: The discrepancy is referenced to the planning-system value: (188 − 180) / 180 = 8 / 180 = 0.044, or 4.4 percent, which exceeds the 3 percent action level for a simple homogeneous geometry, so the inputs (depth, SSD, field size, wedge factor, prescription point) are checked before treatment. Dividing by 188 gives 4.3 percent, and the 5 percent level is reserved for heterogeneous, small-field, or IMRT points where algorithms legitimately differ. Eight is the MU difference, not a percentage, and the response to a discrepancy is investigation, not substituting the second program's number. 2.2 percent halves the result for no reason. Check: 180 × 1.044 = 188.

### Q4
Stem: An enhanced dynamic wedge is in clinical use on an IMRT-class linac. Which check does TG-142 list monthly for it?
A. Full 60 degree wedge-angle verification over the whole field
B. Wedge placement accuracy within 2 mm
C. Wedge transmission factor within 2 percent, measured in water with the full TG-51 setup
D. Wedge-factor constancy within 2 percent
Answer: D
Objective: VII.9
Why: Because a dynamic wedge is produced by a moving jaw under software control, TG-142 asks for a monthly constancy check of the dynamic-wedge factor at 2 percent, with the full wedge-angle verification at the 60 degree setting (plus a spot check of another angle and field size) annually. Placement accuracy within 2 mm is the monthly check for a physical wedge, which is hardware that can be seated wrongly. The transmission-factor check at 2 percent is the annual physical-wedge check and does not require a TG-51 setup.

### Q5
Stem: A physicist is commissioning the dose-calculation algorithm of a new photon and electron planning system. Which document gives the current test set and tolerances?
A. TG-53, the comprehensive planning-system QA report
B. MPPG 5.a, the AAPM practice guideline for TPS dose-calculation commissioning
C. TG-142, the linear-accelerator QA report
D. TG-119, the IMRT commissioning test suite
Answer: B
Objective: VII.1
Why: Medical Physics Practice Guideline 5.a is the current prescription for commissioning and QA of a planning system's photon and electron dose calculation: which geometries to measure and how close calculation must come, with teaching tolerances near 2 percent on the central axis in the high-dose region, about 2 mm in the penumbra, and 3 to 5 percent out of field. TG-53 is the broader 1998 process document it supersedes for this purpose. TG-142 covers the machine, not the planning system. TG-119 tests IMRT delivery accuracy after the beam model exists.

### Q6
Stem: Which statement correctly describes a change from TG-40 to TG-142?
A. TG-142 loosened the annual output tolerance from 1 percent to 2 percent
B. TG-142 moved the daily output constancy check from 3 percent to 1 percent
C. TG-142 replaced the single tolerance table of TG-40 with separate columns for non-IMRT, IMRT, and SRS/SBRT machines, and added imaging and MLC tests
D. TG-142 added a weekly chart-check requirement that TG-40 lacked
Answer: C
Objective: VII.9
Why: TG-142 kept the daily, monthly, and annual structure but gave machine-class-specific tolerances (for example lasers at 2, 1.5, and 1 mm; isocenter at 2 and 1 mm) and added kV and MV planar imaging, CBCT, picket-fence, and dynamic-wedge checks that TG-40 could not anticipate. The annual output tolerance tightened from 2 percent to 1 percent, the opposite of option A. Daily output constancy stayed at 3 percent. The weekly chart check came from TG-40 and now lives in TG-275; TG-142 does not address it.

### Q7
Stem: The annual TG-51 calibration of a 6 MV beam gives 1.015 cGy per MU under reference conditions where the nominal value is 1.000 cGy per MU. How does this compare with the TG-142 annual tolerance?
A. 1.5 percent, within the 3 percent annual tolerance
B. 1.5 percent, outside the 1 percent annual tolerance, so the output is adjusted
C. 0.15 percent, well within tolerance
D. 15 percent, requiring the beam to be taken out of service
Answer: B
Objective: VII.1
Why: The deviation is (1.015 − 1.000) / 1.000 = 1.5 percent, and the TG-142 annual absolute-dose tolerance for TG-51 calibration is 1 percent, so the machine output is reset to 1.000 cGy per MU. Three percent is the daily constancy window, not the annual limit. 0.15 percent misplaces the decimal, and 15 percent reads 0.015 as a fraction of 0.1. Check: 1.000 × 1.015 = 1.015, and 1.5 − 1.0 = 0.5 percentage points past the line.

## Safety Culture: Two Identifiers, Swiss Cheese, FMEA Numbers, Fault Trees, and Staffing

### Q1
Stem: Before a treatment fraction, which pair satisfies the two-patient-identifier rule?
A. Treatment room number and appointment time
B. Full name and the bed the patient arrived in
C. The patient's photograph and the therapist's recollection of the patient
D. Full name and date of birth
Answer: D
Objective: VII.7
Why: The Joint Commission's first National Patient Safety Goal requires two identifiers that belong to the person, such as full name and date of birth or full name and medical record number; a photograph in the record-and-verify system is a common additional check. Room number, appointment time, and bed describe where the patient is, not who the patient is, and two patients can share them. A staff member's recollection is not an identifier.

### Q2
Stem: In the Swiss-cheese model of accident causation, what does a slice of cheese represent, and what do the holes mean?
A. Each slice is one defensive layer such as a plan check or pre-treatment imaging, and the holes are that layer's weaknesses; harm occurs when holes in every layer line up
B. Each slice is one staff member, and the holes are their training gaps
C. Each slice is one treatment fraction, and the holes are days the patient missed
D. Each slice is one regulator, and the holes are rules that overlap
Answer: A
Objective: VII.7
Why: Reason's model pictures independent barriers, none of them perfect, so that an error reaches the patient only when the weaknesses of all of them align on the same event; the lesson is to keep defences independent and to learn from near misses that stopped partway through. Slices are process layers rather than people, fractions, or agencies, and the model exists to move attention from blaming the last person to closing the earlier holes.

### Q3
Stem: In a TG-100 failure-mode-and-effects analysis, a failure mode is scored occurrence 3, severity 9, and detectability 6. What is its risk priority number?
A. 18
B. 27
C. 162
D. 1,620
Answer: C
Objective: VII.7
Why: The RPN is the product of the three scores: 3 × 9 × 6 = 162, on a scale that runs from 1 to 1,000. Adding the scores gives 18, which is not how the index is defined. Twenty-seven multiplies only occurrence and severity. 1,620 is off by a factor of ten and exceeds the maximum possible value. Check: 3 × 9 = 27, and 27 × 6 = 162, which is above the working trigger of about 125 and also carries a severity of 9, so the mode gets a control on both grounds.

### Q4
Stem: How does fault-tree analysis differ from the FMEA step in TG-100?
A. The fault tree scores each step with occurrence, severity, and detectability, while the FMEA draws a diagram
B. The fault tree starts from one unwanted outcome and works backward through AND and OR gates to the causes, while the FMEA lists failure modes forward from each process step
C. The fault tree is done by the therapists and the FMEA by the physicists
D. They are the same tool under two names
Answer: B
Objective: VII.7
Why: A fault tree is a backward-reasoning diagram: the top event (for example wrong dose to the target) sits at the top, and logic gates connect it to the combinations of basic events that could produce it, which shows where a single check cuts the most branches. The FMEA is the forward enumeration of how each step can fail, and it is the FMEA that carries the O, S, and D scores. Both are multidisciplinary exercises. They are complementary steps, not synonyms.

### Q5
Stem: Using the ISCRO Blue Book staffing guidance that ASTRO's safety documents carried forward, how many full-time dosimetrists are indicated for a department treating about 900 new patients per year?
A. 3
B. 2
C. 9
D. 1
Answer: A
Objective: VII.6
Why: The teaching ratio is about one dosimetrist per 300 patients treated per year, so 900 / 300 = 3. Two would correspond to 600 patients, and one to 300. Nine divides by 100 rather than 300. Check: 3 × 300 = 900. The ratio is a minimum for a conventional case mix and per year of new patients, not per day; a heavy IMRT, SRS, or brachytherapy load raises the need above it.

## Source Drift: Lens Limits, Cataract Thresholds, and Penumbra Definitions

### Q1
Stem: What is the annual occupational dose limit to the lens of the eye under 10 CFR 20.1201?
A. 20 mSv
B. 50 mSv
C. 150 mSv
D. 500 mSv
Answer: C
Objective: VI.1
Why: The NRC lens limit, which follows NCRP Report 116, is 150 mSv (15 rem) per year, and the NRC did not change it after ICRP's 2011 statement. Twenty millisieverts per year averaged over five years is the ICRP 2011 recommendation and is the correct answer only when the stem says ICRP or asks for the current international recommendation. Fifty millisieverts is the whole-body effective-dose limit. Five hundred millisieverts is the limit for skin, extremities, and individual organs.

### Q2
Stem: According to the ICRP 2011 statement on tissue reactions, what is the threshold absorbed dose for a radiation-induced cataract?
A. 2 Gy for an acute exposure only
B. 5 Gy for a fractionated exposure only
C. 10 Gy regardless of fractionation
D. About 0.5 Gy whether the exposure is acute or protracted
Answer: D
Objective: VI.1
Why: ICRP's 2011 review lowered the cataract threshold to about 0.5 Gy for both acute and protracted exposure, and that revision drove the lens-limit reduction to 20 mSv per year. Two grey acute and five grey fractionated are the legacy textbook values that older practice tests still key; the bank treats them as historical and uses 0.5 Gy when a stem asks for the current threshold. Ten grey is not a published threshold and is near the clinical lens-tolerance figures used in planning, which are a different quantity.

### Q3
Stem: A measured profile at 10 cm depth places the 90 percent isodose at 4.55 cm off axis, the 80 percent at 4.75 cm, the 50 percent at 5.00 cm, and the 20 percent at 5.35 cm. With no definition stated, what penumbra width does this bank report?
A. 4 mm
B. 6 mm
C. 8 mm
D. 10 mm
Answer: B
Objective: admin
Why: The bank's default physical penumbra is the 80 to 20 percent distance: 5.35 − 4.75 = 0.60 cm, or 6 mm. The 90 to 20 definition that some course material uses gives 5.35 − 4.55 = 0.80 cm, or 8 mm, and is used only when the stem specifies it. Four millimetres is roughly the 90 to 50 distance (5.00 − 4.55 = 0.45 cm), which is not a penumbra definition. Ten millimetres would need the 20 percent line at 5.75 cm. Check: 4.75 + 0.60 = 5.35.

## End-to-End Tests, TG-275 Plan Review, and the Task-Group Directory

### Q1
Stem: An SBRT program upgrades its planning system to a new major version. The linac passes its monthly TG-142 checks and the Winston–Lutz test the next morning. What else does TG-101 call for before the next SBRT patient?
A. Nothing further; the machine tests cover the change
B. A new TG-51 calibration, because the planning system changed
C. A repeat of the picket-fence test at SRS tolerance
D. A repeat end-to-end test, running a phantom with a hidden target through simulation, planning, export, image guidance, and delivery, with dose and position measured
Answer: D
Objective: VII.9
Why: The end-to-end test is the only check that exercises the hand-offs between the planning system and the rest of the chain, so TG-101 requires it at commissioning and after any change to a link, including a planning-software upgrade; the expected overall localization accuracy is about 1 to 2 mm. Machine QA and Winston–Lutz never see the planning system. TG-51 calibrates the beam, which did not change. The picket fence tests leaf positions, which also did not change.

### Q2
Stem: Which best describes AAPM TG-275?
A. The report that sets linac mechanical and imaging tolerances
B. The report on physics plan and chart review, which ranks initial-check, weekly, and end-of-treatment items by risk and asks that the reviewer be independent of the planner
C. The report on the IMRT patient-specific QA tolerance and action limits
D. The report on CT-simulator QA
Answer: B
Objective: VII.2
Why: TG-275 (2020) grew out of a failure-mode analysis of the plan-review process and gives a prioritized checklist for the initial plan check before the first fraction (prescription match, correct CT and patient, isocenter and shifts, constraints, independent MU check, accessories, image-guidance instructions), the weekly chart check, and the end-of-treatment check, and it recommends independent review before the plan is scheduled. Linac tolerances are TG-142, IMRT QA limits are TG-218, and CT-simulator QA is TG-66.

### Q3
Stem: A new PET/CT scanner is being installed next to the simulation suite. Which AAPM report addresses the shielding of its uptake and scanning rooms?
A. TG-108
B. TG-66
C. TG-142
D. TG-119
Answer: A
Objective: VII.9
Why: TG-108 is the PET and PET/CT shielding report; the injected patient is the source, and the 511 keV photons require roughly 1.5 cm of lead per tenth-value layer, so diagnostic x-ray shielding data do not apply. TG-66 is CT-simulator QA, not shielding. TG-142 covers linac QA. TG-119 is the IMRT commissioning test suite.

### Q4
Stem: Which AAPM report defines the action levels for an independent monitor-unit verification of a treatment plan?
A. TG-51
B. TG-106
C. TG-114
D. TG-263
Answer: C
Objective: VII.2
Why: TG-114 addresses the independent verification of monitor units and dose, including how to set action levels by geometry (about 3 percent for simple homogeneous points, widening toward 5 percent where heterogeneity, small fields, or modulation make algorithms differ). TG-51 is reference beam calibration in water. TG-106 describes beam-data commissioning measurements. TG-263 standardizes structure names.
