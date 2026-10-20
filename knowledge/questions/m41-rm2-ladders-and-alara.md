# Module 41. Radiation Protection

Original items. Round 2 of the RM Review porting wave: order-of-magnitude ladders (out-of-field dose, exposure rates around patients, occupational doses, shielding thicknesses, QA error sizes) plus ALARA investigational levels, bioassay timing, and survey cadences.

## Magnitude Ladders: Out-of-Field Dose, ALARA Levels, Exposure Rates, Shielding, and QA Errors

### Q1
Stem: A pregnant patient needs 50 Gy to a supraclavicular target. The uterus sits about 30 cm from the nearest field edge, where the unshielded peripheral dose is about 0.3 percent of the central-axis dose. What is the estimated unshielded fetal dose for the course?
A. 1.5 Gy
B. 0.15 Gy
C. 0.015 Gy
D. 0.5 Gy
Answer: B
Objective: VI.1
Why: Peripheral dose is the central-axis course dose times the out-of-field fraction: 50 Gy × 0.003 = 0.15 Gy, inside the 0.1 to 0.25 Gy band that the 0.2 to 0.5 percent ladder predicts at 30 cm. 1.5 Gy uses 3 percent, the figure for a point a few centimetres from the edge, not 30 cm. 0.015 Gy drops a factor of ten. 0.5 Gy takes 1 percent, which is the 10 cm figure. Check: 0.15 / 50 = 0.003.

### Q2
Stem: The unshielded fetal estimate for a course is 0.15 Gy. A lead bridge over the abdomen cuts the peripheral dose to one third. What is the shielded estimate, and how does it compare with the 0.05 to 0.1 Gy level at which TG-36 asks for shielding and a careful risk discussion?
A. 0.05 Gy, at the lower end of that level
B. 0.10 Gy, above the level, so the course cannot proceed
C. 0.45 Gy, because shielding scatters dose toward the fetus
D. 0.015 Gy, a factor of ten below the level
Answer: A
Objective: VI.1
Why: 0.15 Gy / 3 = 0.05 Gy, which sits at the bottom of the 0.05 to 0.1 Gy band and is a typical shielded result; TG-36 treats doses in this region as the point where shielding, field choice, and a documented risk discussion are expected, not as an absolute bar to treatment. 0.10 Gy halves instead of dividing by three and misreads the band as a prohibition. 0.45 Gy multiplies; a bridge reduces head leakage and collimator scatter, it does not add dose. 0.015 Gy divides by ten, more than a lead bridge delivers. Check: 0.05 × 3 = 0.15.

### Q3
Stem: Which ordering of out-of-field dose, expressed as a fraction of the central-axis dose, matches the distance from the field edge?
A. About 1 percent at 2 cm, 5 percent at 10 cm, 0.3 percent at 30 cm
B. About 50 percent at 2 cm, 10 percent at 10 cm, 5 percent at 30 cm
C. About 0.5 percent at every distance, because leakage is uniform
D. About 5 percent at 2 cm, 1 percent at 10 cm, 0.2 to 0.5 percent at 30 cm
Answer: D
Objective: VI.1
Why: Close to the edge the penumbra tail and patient scatter dominate and the dose is a few percent (about 5 percent at 2 cm); by 10 cm it is near 1 percent; by 30 cm, where head leakage and collimator scatter dominate, it is a few tenths of a percent. Option A inverts the two near values, so dose would rise with distance. Option B describes the penumbra inside about 1 cm of the edge, not centimetres outside it. Leakage is roughly uniform at a few tenths of a percent, but it is the floor of the ladder, not the whole curve.

### Q4
Stem: A radiation safety program follows the NRC model program in Regulatory Guide 8.18 and sets ALARA investigational levels as fractions of the applicable quarterly limit. Taking the quarterly whole-body limit as 12.5 mSv, what are Level I and Level II?
A. 1.25 mSv and 3.75 mSv per quarter
B. 5 mSv and 15 mSv per quarter
C. 0.5 mSv and 5 mSv per quarter
D. 12.5 mSv and 50 mSv per quarter
Answer: A
Objective: VI.1
Why: The model program sets Level I at about 10 percent and Level II at about 30 percent of the applicable quarterly limit: 0.10 × 12.5 = 1.25 mSv and 0.30 × 12.5 = 3.75 mSv. The bank's earlier lesson is right that each licensee writes its own levels; this item asks for the model-program figures that most clinics copy. 5 and 15 mSv apply 10 and 30 percent to the annual limit of 50 mSv rather than to the quarter. 0.5 and 5 mSv are the declared-pregnancy monthly and gestation numbers. 12.5 and 50 mSv are the quarterly and annual limits themselves. Check: 3.75 / 1.25 = 3, the 30-to-10 ratio.

### Q5
Stem: A badge report shows a therapist at 2.0 mSv for the quarter under a program with Level I at 1.25 mSv and Level II at 3.75 mSv. What follows, and who reviews it?
A. Nothing, because 2.0 mSv is under the 12.5 mSv quarterly limit
B. The RSO investigates and documents the cause, and the result is reported to the radiation safety committee, which meets at least quarterly
C. The worker is removed from radiation duties until the next quarter
D. An NRC medical-event report is filed within 24 hours
Answer: B
Objective: VI.1
Why: 2.0 mSv is above Level I (by 0.75 mSv) and below Level II (by 1.75 mSv), so the program calls for an RSO review of how the dose was received and a record of the finding, reviewed by the radiation safety committee, which 10 CFR 35.24 requires to meet at least quarterly. Being under the regulatory limit does not switch off ALARA; the levels exist precisely to act below the limit. Removal from duty is not an ALARA response to a dose a sixth of the limit, though a Level II exceedance would require corrective action to reduce future dose. Medical-event reports concern patient doses, not staff badges.

### Q6
Stem: A technologist who declared her pregnancy in writing three months ago now wants to work the cardiac PET list again without the fetal-monitor restrictions. Which statement is correct?
A. The declaration is permanent until delivery
B. Only the RSO can cancel a declaration, after a dose review
C. She may withdraw the declaration in writing at any time, after which the ordinary occupational limits apply again
D. Withdrawing the declaration requires a physician's note confirming the pregnancy has ended
Answer: C
Objective: VI.1
Why: Under 10 CFR 20.1003 and 20.1208 the declaration is voluntary and written, and the worker may withdraw it in writing whenever she chooses; once withdrawn, the 5 mSv gestation limit and 0.5 mSv monthly recommendation stop applying and the adult 50 mSv limits govern. Neither the RSO nor a physician controls the decision, although counselling about the risk is part of the 10 CFR 19 instruction. A declaration does not have to run to delivery, and withdrawal does not require the pregnancy to have ended.

### Q7
Stem: A nuclear-medicine technologist prepares and administers a 150 mCi therapeutic I-131 capsule from an open vial. Within what interval does Regulatory Guide 8.20 ask for a thyroid bioassay count?
A. Within 30 days, at the next quarterly badge exchange
B. Immediately, before leaving the hot lab
C. Within 24 hours, with a whole-body count
D. Within 72 hours of the handling, and not sooner than about 6 hours
Answer: D
Objective: VI.2
Why: Volatile iodine concentrates in the thyroid over several hours, so the guide asks for the count between roughly 6 and 72 hours after handling large quantities of I-131 or I-125; the 72 hour window catches an intake before the 8 day physical half-life and biological clearance erase it. A month later the activity is a fraction of a hundredth of a microcurie and the intake is undetectable. Counting immediately misses iodine that has not yet reached the gland. A whole-body count is for nuclides that distribute generally; iodine is counted at the neck with a thyroid probe.

### Q8
Stem: Under 10 CFR 35.70, how often must a nuclear-medicine licensee survey with a meter the areas where radiopharmaceuticals requiring a written directive were prepared or administered, and how often must removable contamination be wiped?
A. Meter survey weekly, wipes monthly
B. Meter survey daily on days of use, wipes weekly
C. Both daily
D. Meter survey monthly, wipes quarterly with the leak tests
Answer: B
Objective: VI.2
Why: The rule asks for an end-of-day meter survey of preparation and administration areas on each day of use and a weekly wipe survey for removable contamination; the meter finds spills and misplaced sources, the wipe finds contamination too low or too spread out to see on a meter. Weekly meter surveys would leave a spill unseen for days. Wiping daily is not required by the rule, though many departments do it in the hot lab. Quarterly is the brachytherapy sealed-source inventory and semi-annual is the leak test; neither is a contamination survey.

### Q9
Stem: Rank these staff groups by typical annual occupational effective dose, highest first.
A. Radiation therapists, nuclear-medicine technologists, interventional cardiologists
B. Nuclear-medicine technologists, radiation therapists, interventional cardiologists
C. Interventional cardiologists, nuclear-medicine and PET technologists, radiation therapists
D. All three are about equal at the 50 mSv limit
Answer: C
Objective: VI.1
Why: Interventional and cath-lab staff stand beside the patient while the beam is on and record the highest doses in medicine, several millisieverts a year at the collar and more under long fluoroscopy loads. Nuclear-medicine and PET technologists handle unshielded patients who are the source and typically record a few millisieverts. Radiation therapists stand outside a shielded vault and usually read near background, well under 1 mSv. Nobody in routine practice approaches the 50 mSv limit, which is why ALARA levels are set in low single-digit millisieverts.

### Q10
Stem: Which set of exposure rates fits the four situations: beside a freshly treated I-131 patient, at the visitor line about 1 m from an I-131 bed, at 1 m from a prostate-seed patient at discharge, and natural background?
A. About 1 mR/h, about 100 mR/h, about 0.02 mR/h, about 0.1 mR/h
B. About 10 R/h, about 1 R/h, about 100 mR/h, about 1 mR/h
C. About 100 mR/h at every position, because the patient is the source
D. About 100 mR/h, about 1 to 2 mR/h, about 0.1 mR/h, about 0.02 mR/h
Answer: D
Objective: VI.2
Why: A 100 to 150 mCi I-131 patient reads on the order of 100 mR/h at the bedside, about 20 to 30 mR/h at 1 m immediately after dosing, and the visitor line is set where the reading has fallen to 1 to 2 mR/h; a Pd-103 or I-125 seed implant reads about 0.1 mR/h at 1 m through the pelvis, and background is about 0.01 to 0.02 mR/h. Option A scrambles the order so the far point reads more than the near one. Option B is a thousand times too high throughout; 10 R/h is a sealed-source or treatment-beam figure. Dose rate falls with distance even when the patient is the source.

### Q11
Stem: A dosimetrist is asked to recognise shielding thicknesses by room. Which pairing is correct?
A. Linac primary barrier about 0.6 m concrete; HDR vault about 2.5 m concrete
B. CT room walls about 25 mm lead; PET uptake room about 1.5 mm lead
C. Linac primary barrier about 2.5 m concrete, secondary about 1 m, HDR vault about 0.6 m, CT room about 1.5 mm lead, PET rooms 3 to 25 mm lead
D. Every therapy room needs about 1 m of concrete regardless of the source
Answer: C
Objective: VI.3
Why: Megavoltage primary barriers for a busy 6 to 18 MV machine run about 2 to 2.5 m of ordinary concrete, secondary walls about 1 m, and an HDR Ir-192 vault about half a metre to 0.6 m; a CT simulator needs about 1.5 mm of lead in the walls, and a PET suite needs 3 to 25 mm of lead depending on workload and distance because 511 keV photons have a lead tenth-value layer of about 1.5 cm. Option A swaps linac and HDR. Option B swaps CT and PET, putting the thick lead on the kilovoltage room. A single thickness for every room ignores the three-order-of-magnitude range of photon energies and workloads.

### Q12
Stem: A posting reads "Grave Danger, Very High Radiation Area." Which measurement condition does that wording certify, and how does it differ from the high-radiation-area sign?
A. More than 1 mSv in one hour at 30 cm, the same as the high-radiation sign with stronger words
B. More than 5 Gy in one hour measured at 1 m from the source or from a surface it penetrates, whereas the "Caution" or "Danger, High Radiation Area" sign is more than 1 mSv in one hour at 30 cm
C. More than 0.05 mSv in one hour at 30 cm
D. Any area where a linac is energised
Answer: B
Objective: VI.1
Why: The very-high-radiation-area definition in 10 CFR 20.1003 is an absorbed dose above 5 Gy in one hour at 1 m, and the sign must read "Grave Danger"; the high-radiation-area definition is 1 mSv in one hour at 30 cm and the sign may read either "Caution" or "Danger." The two tiers differ in both the quantity (sievert versus gray) and the distance (30 cm versus 1 m), so option A is wrong on both. 0.05 mSv in one hour at 30 cm is the ordinary "Caution, Radiation Area" sign. An energised linac vault is posted as a high or very high radiation area by measurement, not by the fact of being on.

### Q13
Stem: A 6 MV plan calls for a 60 degree wedge with a wedge factor of 0.60, and the MU were computed with that factor. The wedge is left out of the beam for a fraction. By how much does the delivered dose differ from the prescribed fraction dose?
A. 40 percent low
B. 60 percent high
C. 67 percent high
D. 25 percent high
Answer: C
Objective: VI.1
Why: The MU were inflated by 1 / 0.60 = 1.667 to make up for the wedge; with the wedge missing, the open beam delivers 1.667 times the prescription, which is 67 percent high. Forty percent low is the opposite error, a wedge left in the beam when the MU assumed none (delivered = 0.60 of prescription). Sixty percent high confuses the factor with the excess. Twenty-five percent high is the error for a 0.80 wedge factor, the low end of the 25 to 300 percent ladder that runs from thin wedges to a 0.25 factor. Check: 1 / 0.6 = 1.667, and 1.667 × 0.6 = 1.0.

### Q14
Stem: On the ladder of common planning and setup errors, which single error produces the largest dose change?
A. Normalising the plan to the 50 percent isodose line when the prescription meant the 100 percent line
B. Setting the SSD 1 cm long at a nominal 100 cm
C. Turning lung heterogeneity correction off for a central lung target
D. Omitting a 15 degree wedge with a factor of 0.95 from the MU calculation
Answer: A
Objective: VI.1
Why: Prescribing to the 50 percent line while the plan was meant for the 100 percent line doubles the dose everywhere in the volume, a 100 percent error. A 1 cm SSD error at 100 cm changes the dose by the inverse-square ratio (100 / 101) squared, about 2 percent. Heterogeneity on versus off in lung changes target dose by roughly 5 to 30 percent depending on the path length and energy. A 0.95 wedge factor omitted gives about 5 percent. Check: 1 / 0.5 = 2.0, against 1.02, 1.05 to 1.30, and 1.05 for the others.
