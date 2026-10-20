# Module 40. Brachytherapy

Original items. Written for the RM Review porting wave: LDR prostate workflow, APBI devices, templates and surface applicators, special applications, HDR QA numbers, TG-59 roles, GYN reference points, and medical-event thresholds.

## Site Procedures, Applicators, and HDR Program Numbers

### Q1
Stem: In a transperineal LDR prostate seed implant, why are most seeds placed in the peripheral needles with few or none in the central needles?
A. The peripheral needles are easier to see on transrectal ultrasound
B. Uniform loading would leave the periphery of the gland below the prescription dose
C. The urethra runs through the center of the gland and uniform loading would push its dose above about 150% of prescription
D. Peripheral loading reduces the total number of seeds needed by about half
Answer: C
Objective: V.2
Why: Peripheral (or modified peripheral) loading is the Manchester idea applied to the prostate: more activity at the edge flattens the dose and keeps the urethra, which runs through the center, below about 150% (urethral D10 under 150% and D30 under 130% are common goals). Option A is not the reason; the volume study on TRUS in the dorsal lithotomy position, with 5 mm axial steps and the 5 mm template grid superimposed, images every needle position. Option B is backwards: uniform loading over-doses the center, not the periphery. Option D is false; the seed count is set by the total activity needed, not by the loading pattern.

### Q2
Stem: An I-125 prostate preplan prescribed to 145 Gy reports V100 of 97%, D90 of 108%, V150 of 71%, V200 of 19%, urethral D10 of 140%, and rectal V100 of 0.6 cm³. Which value signals a plan that should be reworked before the implant?
A. The V100 coverage
B. The V150 hot-spot volume
C. The D90 coverage dose
D. The rectal V100 volume
Answer: B
Objective: V.2
Why: V150 is usually held to about 50 to 60% of the prostate volume, so 71% means too much of the gland sits at one and a half times prescription and the plan should be relaxed. V100 of at least 95% (option A) and D90 above 100% of prescription (option C) are coverage goals that this plan meets. Rectal V100 under 1 cm³ (option D) and urethral D10 under 150% are also met. V200 of about 20% or less is at the limit but acceptable.

### Q3
Stem: A nomogram and preplan call for a total apparent activity of 40 mCi of I-125 in seeds of 0.40 mCi each. Following the usual practice of ordering about 10% spare seeds, how many seeds are ordered?
A. 110 seeds
B. 100 seeds
C. 90 seeds
D. 121 seeds
Answer: A
Objective: V.6
Why: Seed count = total activity / activity per seed = 40 / 0.40 = 100 seeds, and about 10% extra are ordered to cover dropped, misfired, or extra-needle seeds: 100 × 1.10 = 110 seeds. Check: 110 × 0.40 = 44 mCi, 10% above the planned 40 mCi. Option B has no spare seeds. Option C subtracts the margin instead of adding it. Option D applies the 10% twice. A lower per-seed strength raises the count (40 / 0.30 = 133 planned seeds), so count and strength trade off against each other.

### Q4
Stem: After an I-125 permanent prostate implant, when is the post-implant CT for final dosimetry usually obtained, following AAPM TG-137?
A. 1 day after the implant
B. 16 days after the implant
C. 90 days after the implant
D. 30 days after the implant
Answer: D
Objective: V.2
Why: TG-137 recommends post-implant imaging at about 30 ± 7 days for I-125, when the edema that enlarges the gland has resolved; a same-day scan reads low on D90 because the swollen gland spreads the seeds apart. Option A is acceptable as an early check but not as the final dosimetry. Option B is the interval used for Pd-103, whose shorter half-life calls for earlier imaging (about 10 days for Cs-131). Option C is too late to be useful because most of the dose has already been delivered. A post-implant D90 of at least 90% of prescription is the usual adequacy threshold.

### Q5
Stem: A clinic receives 120 I-125 seeds for a prostate implant. Following AAPM guidance, what is the minimum number of seeds that must be assayed in the well chamber before the implant?
A. 10 seeds
B. 6 seeds
C. 12 seeds
D. 120 seeds
Answer: C
Objective: V.3
Why: At least 10% of the seeds or ten seeds, whichever is more, are assayed; 10% of 120 is 12, which exceeds 10, so 12 seeds. Check: 12 / 120 = 0.10. Option A is the floor that applies to orders of 100 or fewer seeds. Option B is 5%. Option D is the full batch, which is not required for loose seeds (a third-party assay traceable to the vendor's calibration is also acceptable). The mean should agree with the certificate within about 3%; a discrepancy beyond 5% is resolved with the vendor before use.

### Q6
Stem: For balloon or strut-based accelerated partial-breast brachytherapy, how is the evaluation target volume PTV_eval constructed?
A. The lumpectomy cavity plus a 2 cm margin, including the balloon volume
B. The 1 cm shell outside the device surface, minus the device volume, limited to 5 mm inside the skin surface and excluding the chest wall and pectoralis
C. The whole ipsilateral breast minus the skin
D. The 1 cm shell outside the device surface including the device volume and any portion extending beyond the skin
Answer: B
Objective: V.2
Why: PTV_eval is the tissue within 1 cm of the applicator surface, with the device itself removed because it contains no breast tissue, trimmed to 5 mm below the skin and excluding chest wall and pectoralis so that the coverage statistic (at least 90% of the prescription to at least 90% of PTV_eval) is not diluted by non-target volume. Option A uses a whole-breast style margin. Option C is a whole-breast volume. Option D includes the balloon and air, which would inflate the DVH. The prescription is 34 Gy in 10 fractions twice daily, at least 6 hours apart, specified 1 cm from the device surface, with V150 no more than 50 cm³ and V200 no more than 10 cm³.

### Q7
Stem: On the planning CT for a single-lumen breast balloon, the shortest distance from the balloon surface to the skin surface is 4 mm. What is the usual minimum balloon-to-skin distance for this device, and is this case plannable?
A. 7 mm; the case is not plannable with a single-lumen balloon
B. 5 mm; the case is plannable
C. 2 mm; the case is plannable
D. 10 mm; the case is plannable only with a smaller balloon
Answer: A
Objective: V.2
Why: A single central dwell cannot shape the dose away from the skin, so a single-lumen balloon needs at least about 7 mm of tissue between balloon and skin to keep the skin maximum below 145% of prescription; with 4 mm the skin would exceed that limit. Option B's 5 mm is the limit that a multi-lumen balloon (Contura) or a strut device (SAVI) can reach by weighting the dwells away from the skin, because those devices have more catheters and therefore more freedom to shape the dose, with SAVI offering the most. Option C would place the skin near 200% of prescription. Option D's 10 mm is comfortable but is not the minimum, and a smaller balloon does not change the skin distance.

### Q8
Stem: A 5 cm diameter breast balloon is treated with a single central dwell position and prescribed 1 cm from the balloon surface. Ignoring tissue attenuation, what dose does the balloon surface receive relative to the prescription?
A. 140%
B. 51%
C. 100%
D. 196%
Answer: D
Objective: V.6
Why: The surface is at the balloon radius, 2.5 cm from the source, and the prescription point is at 2.5 + 1.0 = 3.5 cm. Inverse square gives (3.5/2.5)² = 1.4² = 1.96, so the surface receives about 196%, roughly double the prescription. Check: 2.5² × 1.96 = 12.25 = 3.5². Option A is the unsquared ratio. Option B is the inverse, the prescription relative to the surface. Option C ignores the fall-off altogether. The balloon must also conform to the cavity, with no more than about 10% of the PTV_eval volume as air or fluid pockets.

### Q9
Stem: A patient with bulky cervical cancer extending into the parametria cannot accommodate a standard tandem. Which applicator is designed for this situation?
A. Leipzig applicator
B. Freiburg flap
C. Syed-Neblett template
D. Single-channel vaginal cylinder
Answer: C
Objective: V.2
Why: The Syed-Neblett template is a perineal acrylic plate with needle holes in concentric rings around a vaginal obturator; needles are driven through it into the cervix, parametria, or vagina and afterloaded, today usually with HDR Ir-192, when a tandem cannot be placed or disease is bulky or lateral (MUPIT is the same idea with a different plate). Option A is a shielded surface cup for small skin lesions. Option B is a flexible surface mold for curved skin. Option D treats the vaginal mucosa only to about 5 mm depth and cannot reach parametrial disease.

### Q10
Stem: Which skin brachytherapy applicator is a tungsten-shielded cup, 1 to 3 cm in diameter, used with a single dwell position for a small lesion prescribed at about 3 mm depth?
A. Leipzig applicator
B. Freiburg flap
C. Syed template
D. Strut-based breast applicator
Answer: A
Objective: V.2
Why: The Leipzig applicator is the shielded cup for a single HDR dwell over a small flat skin lesion; the Valencia version adds a flattening filter for a flatter profile. The Freiburg flap (option B) is a flexible silicone mat of 1 cm spheres that holds parallel catheters 1 cm apart and 5 mm above the skin, conforms to curved surfaces such as the scalp or a limb, and is prescribed at about 3 to 5 mm depth. Option C is an interstitial GYN template. Option D is an APBI device. Lesions deeper than about 4 to 5 mm are better treated with electrons or interstitial catheters.

### Q11
Stem: During HDR planning, the dosimetrist drags the 100% isodose line on the display away from the rectum, and the system adjusts the nearby dwell times so the line passes through the new position. What is this technique called, and what must be done afterward?
A. Geometric optimization; nothing further, because the total time is unchanged
B. Graphical optimization; recheck the DVH and the hot-spot volumes because the dose has moved somewhere else
C. Inverse planning; re-enter the objectives because they have been overwritten
D. Dose-point optimization; delete the dose points that are no longer met
Answer: B
Objective: V.2
Why: Graphical optimization is the manual, local step of dragging an isodose line, with the software changing adjacent dwell weights to follow it; every drag moves dose elsewhere, so the DVH and the V150 and V200 volumes must be rechecked after each change. Option A, geometric optimization, sets dwell times inversely to the dose each dwell receives from its neighbors and lengthens the end dwells. Option C, inverse planning (IPSA, HIPO), minimizes a penalty function and is not a manual drag. Option D, dose-point optimization, solves a least-squares fit to dose points on the applicator surface or at depth.

### Q12
Stem: A Sr-90/Y-90 applicator is pressed against the sclera after pterygium excision. Which statement about this treatment is correct?
A. The dose comes from 662 keV gamma rays and requires a shielded room
B. The applicator must be decay-corrected weekly because of the short half-life
C. The dose falls to half within about 1 cm, so the lens must be shielded with lead
D. The Y-90 beta particles, 2.28 MeV maximum, deposit the dose within millimeters, falling to about half within 1 mm, and the 28.8-year half-life means the dose rate is updated about yearly
Answer: D
Objective: V.1
Why: The Sr-90/Y-90 eye applicator is a sealed beta source; the Y-90 betas give surface dose rates of several cGy per second and a steep fall-off, so the lens is spared by depth rather than by lead, and the long half-life (about 2.4% loss per year) means an annual decay update is enough. Option A describes Cs-137, not a beta source. Option B contradicts the 28.8-year half-life. Option C overstates the beta range by a factor of ten.

### Q13
Stem: Which statement distinguishes electronic brachytherapy, such as a miniature x-ray tube operated at about 50 kV, from HDR Ir-192 brachytherapy?
A. There is no radionuclide, so byproduct-material licensing does not apply and little room shielding is needed, but output must be verified for each tube and the low energy raises the relative dose to bone and to the surface
B. Its photon energy is higher than that of Ir-192, so more shielding is needed
C. It requires a sealed-source leak test every six months
D. It can be used only for interstitial prostate implants
Answer: A
Objective: V.1
Why: Electronic brachytherapy (Xoft Axxent, Intrabeam) produces x-rays of about 50 kV from a tube in a balloon, surface cone, or spherical applicator; with no radionuclide the NRC byproduct rules and leak tests (option C) do not apply and staff can remain nearby, but each tube's output is verified and the low energy increases bone and surface dose relative to Ir-192, whose mean energy is about 380 keV. Option B inverts the energies. Option D is wrong; its uses are intracavitary breast, skin, and intraoperative applications.

### Q14
Stem: Historically, intravascular brachytherapy was used for in-stent coronary restenosis. What prescription and sources were typical, and why is it rarely used today?
A. About 50 Gy at 1 cm from the source axis with I-125 seeds; replaced by bypass surgery
B. About 5 Gy at the vessel wall with Cs-137 tubes; replaced by balloon angioplasty
C. A single dose of roughly 15 to 20 Gy at 2 mm from the source axis with beta (Sr-90/Y-90, P-32) or gamma (Ir-192) sources; replaced by drug-eluting stents
D. About 34 Gy in 10 fractions with Ir-192; replaced by external beam
Answer: C
Objective: V.2
Why: Intravascular brachytherapy delivered a single dose of about 15 to 20 Gy prescribed 2 mm from the source axis, using beta sources such as Sr-90/Y-90 or P-32 or gamma Ir-192 seed trains, to inhibit neointimal proliferation after stenting; drug-eluting stents made it largely obsolete. Option A has the wrong dose, distance, and nuclide. Option B is far too low a dose, and angioplasty is the procedure being treated, not the replacement. Option D is the APBI breast prescription.

### Q15
Stem: During the NRC-required HDR source-position check, the dummy marker and the active source position are compared by autoradiograph or with a position check ruler. What positional agreement is required?
A. Within 2.5 mm
B. Within 1 mm
C. Within 0.5 mm
D. Within 5 mm
Answer: B
Objective: V.3
Why: The afterloader must place the source within 1 mm of the planned position; this is checked at each source exchange and at least quarterly in the full calibration required by 10 CFR 35.633, and in many clinics daily. Option A is the common step size (2.5 mm, with 5 and 10 mm also selectable and 1 mm on newer units), not a tolerance. Option C is tighter than the regulation requires. Option D would be a full step off and would misplace every dwell. The timer must be accurate within 1 s (or 1%) and the transit dose characterized.

### Q16
Stem: A new Ir-192 HDR source is measured in the well chamber at 7% below the vendor certificate value. What should be done before the first treatment?
A. Enter the certificate value in the console because the vendor's calibration is traceable to NIST
B. Average the certificate and the measured value and treat
C. Enter the measured value and treat, because the institution's measurement always governs
D. Stop and resolve the discrepancy with the vendor, because a difference above 5% is outside the acceptance limit
Answer: D
Objective: V.3
Why: The institution treats with its own measured source strength, but the measurement should agree with the certificate within about 3%, and a difference above 5% is an acceptance failure that must be resolved (remeasure, check the well chamber calibration and sweet spot, contact the vendor) before clinical use. Option A ignores the local measurement entirely. Option B hides a possible error by averaging. Option C would be correct for a difference inside the tolerance but not for 7%. The well chamber carries an ADCL calibration for Ir-192 renewed every 2 years.

### Q17
Stem: Before the first HDR treatment of the day, the operator surveys the afterloader with the source in its safe and reads 3 mR/h at 10 cm from the surface. The door interlock, source indicator lights, area monitor, audio and video links, emergency kit, and the console date and decayed source strength all check out. What action follows?
A. Do not treat; the leakage limit with the source in the safe is 1 mR/h at 10 cm from the surface
B. Treat; 3 mR/h is below the 10 mR/h limit for the afterloader surface
C. Treat; leakage is checked only quarterly
D. Treat after moving the afterloader 1 m farther from the patient
Answer: A
Objective: V.4
Why: With the source shielded in the safe, the exposure rate at 10 cm from the afterloader surface should not exceed 1 mR/h; 3 mR/h means the shield or the source position in the safe is wrong and treatment stops until it is resolved. Option B invents a limit. Option C is wrong; the safe survey is part of the daily check along with the door interlock, source indicators, area monitor, communication links, emergency stop and retract, emergency kit, and the decayed source strength in the console. Option D does not fix a shielding fault.

### Q18
Stem: During an HDR fraction the source fails to retract. The console retract command and the emergency stop have not returned the source to the safe. Following TG-59 roles, what is the next step and who performs it?
A. The dosimetrist pulls the transfer tubes from the applicator
B. The physician turns the emergency hand crank on the afterloader
C. The authorized medical physicist turns the emergency hand crank to retract the source manually
D. The radiation safety officer surveys the room and calls the vendor
Answer: C
Objective: V.5
Why: TG-59 assigns the manual crank to the physicist, who is present at every treatment start together with the authorized user physician. If the crank also fails, the physician removes the applicator with the source inside and places it in the shielded emergency container, after which the room is surveyed, the patient is surveyed and not released until the reading is at background, and the event is reported. Option A assigns the task to the wrong person, and pulling tubes is not an emergency step. Option B swaps the roles. Option D is done later, not as the next step. Emergency drills are run at least annually.

### Q19
Stem: On an anterior radiograph of a cervix brachytherapy insertion, a point is marked at the intersection of a horizontal line tangent to the top of the acetabula and a vertical line tangent to their inner edge. What reference point is this?
A. Point B of the Manchester system
B. The ICRU 38 pelvic-wall point, representing the distal parametrium and obturator nodes
C. The lower corner of the lymphatic trapezoid, representing the external iliac nodes
D. The ICRU 38 rectal reference point
Answer: B
Objective: V.2
Why: ICRU 38 defines the pelvic-wall point on the AP film by the acetabular tangents (and on the lateral film at the mid-distance between the right and left points); it stands for the distal parametrium and obturator nodes and receives a dose similar to point B. Option A, point B, is 5 cm lateral to the midline at the level of point A and is not anchored to the acetabulum. Option C is drawn 6 cm lateral to the midline at the pelvic-brim level on the lymphatic trapezoid, whose upper corners sit 2 cm lateral at L4 for the low para-aortic nodes. Option D is 5 mm behind the posterior vaginal wall at the level of the ovoids.

### Q20
Stem: A written directive for HDR cervix treatment prescribes 700 cGy per fraction for 4 fractions, 2800 cGy total. In fraction two, a transfer-tube error delivers 1000 cGy to the prescription point; the other three fractions are correct. Under 10 CFR 35.3045, is this a medical event by the dose criteria?
A. Yes, because any fraction more than 20% off the directive is a medical event
B. Yes, because the total dose is more than 50% off the directive
C. No, because HDR deviations are judged only on the total dose
D. No by the dose criteria: the fraction deviation is 43%, below the 50% single-fraction threshold, and the total deviation is 11%, below the 20% threshold
Answer: D
Objective: V.5
Why: Single-fraction deviation = (1000 − 700) / 700 = 300 / 700 = 42.9%, below 50%. Total delivered = 1000 + 3 × 700 = 3100 cGy, a deviation of 300 / 2800 = 10.7%, below 20%. Check: a fraction of 1050 cGy would reach exactly 50% and be reportable. Option A uses the total-dose threshold for a fraction. Option B miscalculates the total deviation. Option C is wrong because the single-fraction criterion exists. Wrong site, wrong patient, wrong nuclide, and wrong route are medical events regardless of dose; for permanent implants the 2018 rule uses total source strength more than 20% off the directive, or more than 20% of the strength outside the treatment site; notification is by telephone no later than the next calendar day and in writing within 15 days.

### Q21
Stem: A semiannual wipe test of a Cs-137 LDR tube reads 0.006 µCi of removable activity. What is this in becquerels, and does the source pass?
A. 6 Bq; passes
B. 222 Bq; fails, because the limit is 185 Bq
C. 2220 Bq; fails
D. 60 Bq; passes
Answer: B
Objective: V.5
Why: 1 µCi = 37000 Bq, so 0.006 × 37000 = 222 Bq, which exceeds the 185 Bq (0.005 µCi) leak-test limit; the source is leaking, is removed from use, and the finding is reported as the license requires. Check: 185 / 37000 = 0.005 µCi, and 0.006 is above it. Options A and D use a wrong conversion factor. Option C is ten times too high (it corresponds to 0.06 µCi). Some review sheets print the limit as 0.05 µCi, which is a factor of ten too high; the regulatory figure is 0.005 µCi.
