# Module 40. Brachytherapy

Original items. Written for the RM Review porting wave, round 2: implant classification, GYN applicator families and loadings, Manchester-era organ limits, eye plaques, prostate candidacy, seed anisotropy, patient exposure rate with body transmission, HDR timer QA and interlocks, planning-system checks, and inverse permanent-implant and milligram-hour arithmetic.

## Applicator Families, Loading Patterns, and Implant Classification

### Q1
Stem: A single HDR catheter is placed through a bronchoscope into the left main bronchus and dose is prescribed 1 cm from the catheter axis. Which class of brachytherapy implant is this?
A. Interstitial
B. Intracavitary
C. Intraluminal
D. Surface mold
Answer: C
Objective: V.2
Why: A catheter running down a tubular organ such as the bronchus, esophagus, or bile duct is an intraluminal (endoluminal) implant, dosed radially at a fixed distance from the axis. Interstitial (option A) means sources inserted into the tissue itself, as with prostate seeds or Syed needles. Intracavitary (option B) means sources placed in a natural cavity without piercing tissue, as with tandem and ovoids or a vaginal cylinder. A surface mold (option D) sits on skin or an organ surface, as with a Freiburg flap or an eye plaque.

### Q2
Stem: In an esophageal HDR plan with equal dwell times at every position along the catheter, the reference isodose narrows toward both ends of the treated length. How does the planner correct this?
A. Lengthen the dwell times at the first and last few positions so the isodose becomes a cylinder of constant radius
B. Lengthen the dwell times at the center of the catheter where the tumor is thickest
C. Prescribe at 0.5 cm instead of 1 cm from the axis
D. Add a second catheter parallel to the first
Answer: A
Objective: V.2
Why: Dwells in the middle of a line receive contributions from neighbors on both sides, while the end dwells have neighbors on one side only, so equal times give a cigar-shaped isodose that tapers at the ends; weighting the end dwells more heavily (which geometric optimization does automatically) restores a cylindrical reference isodose. Option B makes the taper worse by adding dose where it is already highest. Option C changes the prescription distance and does not fix the shape. Option D is not possible in a single-lumen esophageal applicator and does not address the end fall-off.

### Q3
Stem: A Manchester-style LDR cervix insertion is prescribed 700 cGy to point A. Under the classical rule that the bladder reference point should not exceed about 80% of the point A dose, what is the highest acceptable bladder point dose?
A. 490 cGy
B. 560 cGy
C. 630 cGy
D. 525 cGy
Answer: B
Objective: V.6
Why: 0.80 × 700 = 560 cGy. Check: 560 / 700 = 0.80. Option A is 70% (490 cGy), the lower end of the rectal range of 70 to 80% of point A, not the bladder figure. Option C is 90%, which would mean the ovoids or packing need adjustment. Option D is 75%. These fractions are checks on the geometry of the insertion read at the ICRU 38 points; the modern volumetric equivalents are the bladder D2cc and rectum D2cc EQD2 limits.

### Q4
Stem: During a tandem-and-ovoid insertion the physician can fit either small ovoids or large ovoids in the vaginal fornices. Why does the classical intracavitary rule favor the largest ovoids and the longest tandem the anatomy allows?
A. Larger ovoids hold more source positions, so the treatment time is shorter
B. Larger ovoids need less vaginal packing, so the procedure is faster
C. A longer tandem lowers the point A dose and spares the bladder
D. Larger ovoids keep the vaginal mucosa farther from the sources, so the mucosal dose is lower for the same point A dose and the pear-shaped isodose is wider; a longer tandem covers the whole uterine canal to the fundus
Answer: D
Objective: V.2
Why: Dose falls steeply with distance near a source, so moving the mucosal surface outward by a few millimeters lowers its dose markedly while point A, farther away, changes little; the wider ovoid separation also broadens the pear to cover more parametrium, and a tandem that reaches the fundus treats the entire canal. Option A confuses ovoid size with dwell count; treatment time is set by the plan, not the applicator diameter. Option B is not a dosimetric argument; packing is still used to push bladder and rectum away. Option C is wrong because point A is defined relative to the os, not the tandem length.

### Q5
Stem: Which statement correctly contrasts the ring applicator with Fletcher-Suit shielded ovoids for HDR cervix treatment?
A. The ring gives a fixed, reproducible geometry with the tandem but carries no tungsten shielding, so bladder and rectal sparing comes from dwell weighting; Fletcher ovoids carry internal tungsten shields on their bladder and rectal sides
B. The ring carries tungsten shields and the Fletcher ovoids are unshielded
C. Both applicators are unshielded and differ only in the tandem curvature
D. The ring is used only for LDR and the Fletcher ovoids only for HDR
Answer: A
Objective: V.2
Why: The ring fixes the ovoid-equivalent as a circle around the cervix at a set angle to the tandem, which makes fraction-to-fraction geometry reproducible, but the ring is unshielded, and the dwell positions nearest the tandem are usually left inactive to limit mucosal dose; the Fletcher-Suit (Fletcher-Suit-Delclos) colpostats have tungsten shields that cut the dose at the bladder and rectal points by roughly 10 to 25%. Option B reverses the shielding. Option C ignores the Fletcher shields. Option D is false; both are used with HDR afterloaders, and Fletcher-style sets were also the LDR standard.

### Q6
Stem: A patient with carcinoma of the uterine corpus has an enlarged, irregular uterine cavity that a single tandem cannot cover. Which classical applicator was designed for this situation?
A. Henschke applicator
B. Fletcher-Suit tandem with 45 degree curvature
C. Heyman capsules packed to fill the cavity
D. Syed-Neblett template
Answer: C
Objective: V.2
Why: Heyman capsules (and the Simon-Heyman afterloading version) are small source capsules packed into a large endometrial cavity so that the whole uterine wall is treated; the loading is counted in capsule-hours. The Henschke applicator (option A) is a tandem with hemispherical ovoids rigidly attached with their axes parallel to the tandem, a fixed-geometry cervix applicator, not a packing system. A 45 degree tandem (option B) follows a strongly flexed uterus but still treats only along one line. The Syed-Neblett template (option D) is an interstitial perineal template for parametrial disease.

### Q7
Stem: A radium-era tandem is loaded 15-10-10 mg from the fundus to the external os. What is this loading pattern called, and what is its purpose?
A. Dumbbell loading, to boost both the fundus and the os
B. Indian club loading, to put the heaviest source at the fundus so the upper end of the pear-shaped isodose is fuller
C. Uniform loading, to give the same dose along the whole canal
D. Peripheral loading, to spare the urethra
Answer: B
Objective: V.2
Why: Indian club loading is heavy at the fundal tip and lighter below, like the shape of the club; it fills out the fundal end of the dose distribution. Dumbbell loading (option A) is heavy at both ends with a lighter middle, for example 15-10-15 mg. Uniform loading (option C) is equal strengths, for example 10-10-10 mg. Peripheral loading (option D) is a prostate seed pattern, not a tandem pattern. HDR dwell weighting reproduces any of the three.

### Q8
Stem: A choroidal melanoma has an apical height of 9 mm. Which episcleral plaque is appropriate, and why?
A. A Ru-106 beta plaque, because beta dose falls off slowly enough to reach 9 mm
B. A Ru-106 beta plaque, because the gold COMS plaque is reserved for tumors under 5 mm
C. Either plaque, because both deliver 85 Gy to the apex at the same dose rate
D. A COMS gold plaque loaded with I-125 or Pd-103 seeds, because the photon dose reaches a 9 mm apex while the Ru-106 beta range limits that plaque to tumors of roughly 5 to 6 mm or less
Answer: D
Objective: V.2
Why: The COMS plaque is a gold-alloy shell, 12 to 20 mm across, with a Silastic insert holding I-125 (or Pd-103) seeds; the gold shields the orbit and the photon dose is prescribed 85 Gy to the tumor apex over several days. Ru-106 is a beta emitter with a steep fall-off that suits thin tumors, roughly 5 to 6 mm apical height or less, and spares the opposite retina. Option A inverts the beta range argument. Option B reverses the thickness rule. Option C is wrong because the beta plaque cannot deliver a therapeutic apex dose at 9 mm without an excessive scleral dose.

### Q9
Stem: A patient is evaluated for a permanent prostate seed implant. The volume study shows a 72 cc gland, and the anterior-lateral template rows are blocked by the pubic bone on the transrectal ultrasound images. What is the usual management?
A. Three months or so of androgen-deprivation therapy to shrink the gland, then repeat the volume study to see whether the pubic-arch interference has cleared
B. Proceed with the implant and load extra seeds in the posterior rows to compensate
C. Switch to a smaller template with 2.5 mm hole spacing
D. Implant through a suprapubic approach instead of the perineum
Answer: A
Objective: V.2
Why: Pubic-arch interference means the pubic bone blocks the needle paths to the anterior-lateral gland, and it is common in glands above about 50 to 60 cc; neoadjuvant hormonal therapy shrinks the prostate by roughly a third, which often clears the arch and also reduces the seed and needle count. Option B leaves part of the gland uncovered, which no posterior loading can fix. Option C does not move the needles around bone. Option D is not a seed-implant approach; the transperineal template is the technique.

### Q10
Stem: Compared with an HDR Ir-192 source, how does the anisotropy of an I-125 or Pd-103 seed differ, and why?
A. Seeds are less anisotropic because they are shorter than the Ir-192 source
B. Seeds and Ir-192 have the same anisotropy because TG-43 normalizes both to the transverse axis
C. Seeds are more anisotropic because their 21 to 28 keV photons are heavily attenuated by the titanium end welds and by self-absorption along the seed axis, while 380 keV Ir-192 photons pass the capsule ends with little loss
D. Seeds are more anisotropic because they are implanted in tissue rather than an applicator
Answer: C
Objective: V.1
Why: Anisotropy is the drop in dose along the source axis relative to the transverse axis, and it is governed by how much the encapsulation and the source itself attenuate the photons leaving the ends; low-energy seed photons lose a large fraction in the welds and in the source core, so typical anisotropy factors are about 0.93 to 0.95 for seeds against about 0.98 for Ir-192. Option A has the direction wrong and the wrong cause. Option B confuses the normalization at 90 degrees, where F equals 1 for every source, with the behavior at other angles. Option D is irrelevant; anisotropy is a source property measured in water.

### Q11
Stem: A current protocol prescribes 125 Gy for Pd-103 prostate monotherapy, while a textbook from the mid-1990s lists 115 Gy for the same treatment. Which statement explains the difference?
A. The dose was raised in the 2000s because 115 Gy was found to be clinically inadequate
B. 115 Gy is the boost dose after external beam and 125 Gy is monotherapy
C. The two numbers are for Pd-103 and Cs-131 respectively
D. The same treatment was relabeled when the 1999 NIST air-kerma-strength standard and revised TG-43 parameters changed the calculated dose by about 8%; 115 Gy is the pre-1999 convention and 125 Gy is the post-1999 equivalent
Answer: D
Objective: V.2
Why: The seeds and the clinical dose delivered did not change; the calibration standard and the dose-rate constant did, so the number written for the same implant rose from 115 to 125 Gy (I-125 went through a similar relabeling from 160 to 145 Gy with TG-43 in 1995). Option A invents a clinical escalation. Option B is wrong; the Pd-103 boost after about 45 Gy of external beam is about 100 Gy. Option C is wrong; Cs-131 monotherapy is 115 Gy, but the 1990s textbook figure predates clinical Cs-131 and refers to Pd-103.

## Patient Exposure Rate, Timer QA, and Independent Plan Checks

### Q1
Stem: An inpatient has a temporary Ir-192 interstitial implant totaling 200 mCi. The exposure rate constant is 4.69 R cm² per mCi per hour and the body transmission factor is 0.70. What is the exposure rate at 1 m from the patient?
A. 93.8 mR/h
B. 65.7 mR/h
C. 134 mR/h
D. 0.657 mR/h
Answer: B
Objective: V.6
Why: Exposure rate = Γ × A / d² × T = 4.69 × 200 / 100² × 0.70 = 938 / 10000 × 0.70 = 0.0938 × 0.70 = 0.0657 R/h = 65.7 mR/h. Check: 65.7 / 0.70 = 93.8 mR/h, the unattenuated value, and 93.8 × 10000 / 200 = 4.69, the constant. Option A omits the body transmission and overstates the rate. Option C divides by the transmission instead of multiplying. Option D has the R to mR conversion wrong by a factor of 100.

### Q2
Stem: During HDR timer QA, a well chamber reads 62.0 units for a 30 second dwell and 122.0 units for a 60 second dwell at the same position. What is the end effect, expressed as equivalent dwell time?
A. 2.0 s
B. 0.5 s
C. 1.0 s
D. 31 s
Answer: C
Objective: V.6
Why: Slope = (122.0 − 62.0) / (60 − 30) = 60.0 / 30 = 2.00 units per second. Intercept = 62.0 − 2.00 × 30 = 2.0 units. End effect = intercept / slope = 2.0 / 2.00 = 1.0 s. Check: 2.00 × 60 + 2.0 = 122.0, the second reading. Option A is the intercept in reading units, not converted to time. Option B halves the result. Option D treats the intercept as if it added to the dwell time directly. The end effect is the transit dose delivered while the source travels to and from the dwell, and it matters most for short dwells.

### Q3
Stem: A plot of HDR well-chamber reading against set dwell time for 10, 20, 40, and 80 seconds is a straight line that does not pass through the origin. What does this result establish?
A. The timer is linear, and the non-zero intercept is the transit (end-effect) dose
B. The timer is non-linear and must be repaired before clinical use
C. The source strength has decayed since the last calibration
D. The well chamber has a leakage current that must be subtracted
Answer: A
Objective: V.3
Why: A straight line proves that dose is proportional to dwell time, which is the linearity test; the slope is the dose rate and the intercept is the dose delivered during source travel, so the two quantities come from one plot. Option B contradicts the straight line. Option C would change the slope, not the intercept, and is a separate decay check. Option D would also appear as an intercept, but leakage is tested with the source retracted and is normally negligible against a transit dose. Timer accuracy is expected within about 1 s or 1%.

### Q4
Stem: Which pair of features satisfies the requirement that an HDR afterloader be protected against unauthorized operation by two independent measures?
A. The door interlock and the area radiation monitor
B. The emergency stop button and the hand crank
C. The source-on indicator light and the intercom
D. A removable console key together with an operator password or access code
Answer: D
Objective: V.5
Why: Security means preventing someone from starting the unit; a key that is removed and controlled plus a password (or a key-controlled console plus a locked treatment room) are two independent barriers. Options A and C are radiation-safety controls that protect people in and around the room during treatment, not security against unauthorized use. Option B lists emergency devices for a stuck source. The console, keys, and room are secured whenever the unit is unattended.

### Q5
Stem: An HDR suite contains a ceiling-mounted C-arm for applicator imaging. What interlock is expected between the imaging x-ray unit and the afterloader?
A. The x-ray unit must be powered off before the afterloader can be installed in the room
B. The two systems are interlocked so that the x-ray tube cannot expose while the HDR source is out of the safe and the source cannot leave the safe while the x-ray tube is exposing
C. The x-ray unit and the afterloader share one timer so that imaging and treatment finish together
D. No interlock is needed because diagnostic x-rays and Ir-192 gamma rays have different energies
Answer: B
Objective: V.5
Why: Staff may be in the room for imaging and must never be there while the source is out, and the area radiation monitor must not be fooled by x-ray scatter, so the two sources of radiation are interlocked against simultaneous operation. Option A is not an interlock and would make imaging impossible. Option C is not a safety function and would be dangerous. Option D ignores that the hazard is the presence of people during source exposure, not the spectrum.

### Q6
Stem: During commissioning of a brachytherapy planning system, the dose rate at 2 cm on the transverse axis of a single Ir-192 source is computed as 11.40 cGy/h, while the hand calculation from the TG-43 consensus table gives 11.15 cGy/h. What is the percentage difference?
A. 2.2%
B. 0.25%
C. 22%
D. 1.1%
Answer: A
Objective: V.6
Why: Difference = 11.40 − 11.15 = 0.25 cGy/h; 0.25 / 11.15 = 0.0224, about 2.2%. Check: 11.15 × 1.022 = 11.40. This is outside the usual per-point tolerance of about 2% for single-source comparisons against TG-43 tables (about 5% is the looser figure for overall agreement of a multi-source plan or for points very near the source), so the radial dose function at 2 cm and the source model are checked before clinical use. Option B is the absolute difference mislabeled as a percentage. Option C misplaces the decimal. Option D halves the correct value.

### Q7
Stem: An I-125 permanent prostate implant is prescribed 145 Gy to complete decay. The half-life is 59.4 days. What initial dose rate at the prescription isodose is required?
A. 10.2 cGy/h
B. 4.89 cGy/h
C. 7.05 cGy/h
D. 169 cGy/h
Answer: C
Objective: V.6
Why: Initial dose rate = D / (1.443 × half-life × 24) = 14500 / (1.443 × 59.4 × 24) = 14500 / (85.71 × 24) = 14500 / 2057 = 7.05 cGy/h. Check: 7.05 × 2057 = 14502 cGy. Option A omits the 1.443 (14500 / 1425.6) and would overdose by 44%. Option B applies 1.443 twice. Option D is the dose rate per day (14500 / 85.71) mislabeled as per hour. Some texts write 1.44 instead of 1.443; the result differs by 0.2%.

### Q8
Stem: An LDR cervix insertion is loaded with a tandem of 15, 10, and 10 mg-Ra-eq and two ovoids of 10 mg-Ra-eq each, and remains in place for 48 hours. How many milligram-hours does the insertion deliver?
A. 1680 mg-h
B. 2640 mg-h
C. 3600 mg-h
D. 960 mg-h
Answer: B
Objective: V.6
Why: Total strength = 15 + 10 + 10 + 10 + 10 = 55 mg-Ra-eq; 55 × 48 = 2640 mg-h. Check: 2640 / 48 = 55. Option A uses only the tandem (35 × 48). Option C uses 75 mg-Ra-eq, as if the ovoids were 20 mg each. Option D uses only the ovoids (20 × 48). Milligram-hours is the integrated strength the Manchester intracavitary tables were written in; multiplying by 7.227 U per mg-Ra-eq converts it to the TRAK in U-hours.
