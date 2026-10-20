# Module 40. Brachytherapy

Original notes for MDCB CMD prep. Domain V is about 5% of the exam. Objectives V.1 through V.6, plus half-lives (I.7) and machine characteristics (I.5).

Half-life and mean life do different jobs. Remaining activity uses the half-life. Total dose from a permanent implant, after complete decay, uses the mean life \(1.443 \times T_{1/2}\).

Nuclides these items name:

| Source | Half-life | Role on the exam | Energy to remember |
| --- | --- | --- | --- |
| Ir-192 | 73.8 days | HDR (and LDR) remote afterloading | mean energy about 0.38 MeV (about 380 keV) |
| Cs-137 | 30 years | LDR tubes, historical GYN | 0.662 MeV (662 keV) |
| I-125 | 59.4 days | permanent seeds | about 28 keV |
| Pd-103 | 17.0 days | permanent seeds | about 21 keV |
| Co-60 | 5.26 years | external beam and some HDR | about 1.25 MeV |
| Au-198 | 2.7 days | permanent, historical | 0.412 MeV |

HDR means a dose rate at the prescription point of at least 12 Gy/h. LDR is roughly 0.4–2 Gy/h. MDR sits between them. Pulsed dose rate delivers LDR-like total doses in short pulses. I-125 and Pd-103 permanent seeds are low dose rate in the tissue sense and are not HDR afterloaders.

## Radioactive Source Characteristics

**Objectives:** V.1, I.7

**What the exam expects:** Match the nuclide to the job (HDR Ir-192, LDR Cs-137, I-125 and Pd-103 seeds). Use half-life for remaining activity. Use mean life only when the question is total dose from complete decay. Autoradiography checks whether activity is uniform along a source or a ribbon.

**Core facts**

Energies to memorize, the same numbers as the table: Ir-192 about 380 keV mean, Cs-137 662 keV, I-125 about 28 keV, Pd-103 about 21 keV. Ir-192 is the HDR nuclide. Cs-137 is the historical LDR tube. I-125 and Pd-103 are the permanent seeds. Pd-103 is the softer and the shorter-lived of those two seeds.

Lead half-value layers, if a source item asks for one, follow the same energy order and are the module 3 teaching values: Co-60 12 mm, Cs-137 6.5 mm, Ir-192 "3–6 mm" with about 3 mm as the narrow-beam figure, Au-198 about 2.5 mm, I-125 0.025 mm, Pd-103 about 0.008 mm, and filtered Ra-226 (mean 0.83 MeV) about 8 mm. Published teaching tables disagree by a millimeter or two: Khan-style tables print Cs-137 5.5 mm, Ir-192 2.5 mm, and Co-60 11 mm, while other review sheets print 6.5, 3–6, and 12 mm, so the defensible statement is Cs-137 5.5–6.5 mm, Ir-192 2.5–6 mm, Co-60 11–12 mm. The exam spaces its options far enough apart (for example 0.025, 2.5, 6, 12 mm) that either figure in a range picks the same letter; this bank keeps 12, 6.5, and 3–6 so that its theory and keys match, and treats 2.5 mm as the Ir-192 answer when both 2.5 mm and 6 mm are offered. A stem that needs an HVL for a shielding calculation prints it, and the printed value wins.

**Formulas**

\[
A = A_0 e^{-\lambda t}
\qquad
\lambda = \frac{0.693}{T_{1/2}}
\qquad
\text{mean life} = 1.443\, T_{1/2}
\]

- \(A_0\): activity at calibration
- \(A\): activity after time \(t\)
- \(\lambda\): decay constant
- \(T_{1/2}\): half-life, same time unit as \(t\)
- Mean life: average life of a nucleus. Activity falls to \(1/e \approx 37\%\) after one mean life, not to 50%.

After \(n\) half-lives, activity is \(A_0 / 2^n\).

### Worked example

**Given.** An Ir-192 source is 10.0 Ci at calibration. \(T_{1/2} = 73.8\) days. What is the activity after two half-lives, and what would a mean-life mistake produce?

**Substitute.** Two half-lives: \(t = 2 \times 73.8 = 147.6\) days. \(A = 10.0 / 2^2 = 10.0 / 4 = 2.50\) Ci.

**Mean-life distractor, shown so it can be rejected.** Mean life \(= 1.443 \times 73.8\).

\[
1.443 \times 70 = 101.01
\qquad
1.443 \times 3.8 = 5.48
\qquad
\text{mean life} = 106.5 \text{ days}
\]

Activity after one mean life is \(10.0 / e = 10.0 \times 0.368 = 3.68\) Ci, not 5.0 Ci and not 2.50 Ci.

**Check.** \(73.8 \times 2 = 147.6\). \(10/4 = 2.5\). \(1.443 \times 73.8 = 106.5\) days, which is longer than one half-life and shorter than two, matching 37% remaining rather than 25%.

**Result means.** After 147.6 days the source is 2.50 Ci. HDR inventory and the treatment dose rate both follow this decay. The factor 1.443 is reserved for integrating a permanent implant to infinite time (the calculations lesson).

Autoradiography: a film or detector under a wire or a seed ribbon. Uniform blackening means uniform activity. A blank spot means a missing or weak source. It is a source check, not a patient survey.

**Wrong turns**

- Using mean life to halve the activity.
- Using half-life alone as the total-dose multiplier for a permanent implant (that misses the 1.443).
- Swapping I-125 (59.4 d, about 28 keV) and Pd-103 (17 d, about 21 keV). Pd-103 decays faster, so the same total dose starts at a higher initial dose rate.
- Calling Cs-137 an HDR source. HDR in current practice is Ir-192 (Co-60 exists in some afterloaders; the stem will say so).

**Traps.** Write the time unit next to \(T_{1/2}\) before you divide. Days in the numerator and years in the half-life is a factor-of-365 error.

**Sources.** Khan and Gibbons, brachytherapy radionuclides and mean life. AAPM TG-43 for the quantities that use source strength rather than mgRaEq.

## HDR and LDR Treatment Planning

**Objectives:** V.2, V.3

**What the exam expects:** Manchester point A, the prescription point for a vaginal cylinder, and the fact that a point-source inverse square is only the geometry term of TG-43. Applicators you should recognize: tandem and ovoids, vaginal cylinder, interstitial needles, and permanent seeds.

**Point A** is 2 cm superior to the external cervical os and 2 cm lateral to the uterine canal. It is a geometry point, not a structure you contour on MRI, though modern plans also dose a target volume. **Point B** is 5 cm from the patient’s midline at the same superior level (3 cm lateral to point A) and stands in for the pelvic sidewall lymph nodes in the Manchester system.

ICRU 38 bladder and rectum points are film points, not contoured volumes. The bladder point uses a Foley balloon filled with 7 cm³ of contrast. On the anterior radiograph the point is the center of the balloon. On the lateral radiograph it is the posterior surface of the balloon. The rectum point is 5 mm behind the posterior vaginal wall, on the midline, at the level of the middle of the ovoids.

GEC-ESTRO correlates used in this bank are volume doses. Coverage is HR-CTV D90, the dose that covers 90% of the high-risk clinical target volume (residual gross disease plus the cervix at the time of brachytherapy). Rectum D2cc is often held near 65–75 Gy EQD2. Bladder D2cc is held near 80–90 Gy EQD2. D2cc is the dose to the hottest 2 cm³ of that organ. These are the correlates this bank uses.

Prescriptions to memorize: vaginal cuff HDR is 7 Gy × 3 at 0.5 cm from the cylinder surface. Cervix HDR is often 7 Gy × 4, or 5.5 Gy × 5. One common prostate HDR boost is 13.5 Gy × 2. I-125 monotherapy is 145 Gy. Pd-103 monotherapy is 125 Gy. An I-125 eye plaque is 85 Gy to the apex.

TRAK, total reference air kerma, is the sum over sources of (reference air-kerma rate times duration). It indexes the application at the reference distance. It is not the tumor dose and not point A.

A vaginal cylinder prescribes at a stated depth in tissue from the cylinder surface, often 5 mm. Distance from a central source to that point is cylinder radius plus that depth.

The full TG-43 dose rate is in the calculations lesson. The geometry term alone, for a point source, is

\[
\frac{G(r)}{G(r_0)} = \left(\frac{r_0}{r}\right)^2
\]

with \(r_0 = 1\) cm. Anisotropy \(F\) and radial dose \(g(r)\) are still missing if you stop here.

### Worked example

**Given.** A central-channel cylinder has radius 2.0 cm. Dose is specified 0.5 cm out in tissue. A point-source estimate gives 800 cGy/min at 1.0 cm on the transverse axis, with \(g = 1\) and \(F = 1\) assumed for this estimate only.

**Substitute.** Prescription distance \(r = 2.0 + 0.5 = 2.5\) cm.

\[
\dot{D}(2.5) = 800 \left(\frac{1.0}{2.5}\right)^2 = 800 \times 0.160 = 128 \text{ cGy/min}
\]

**Check.** \(2.5^2 = 6.25\), and \(128 \times 6.25 = 800\).

**Result means.** Geometry alone drops the dose rate from 800 cGy/min at 1 cm to 128 cGy/min at the 5 mm depth. A real TG-43 calculation also multiplies by \(g(r)\) and \(F(r,\theta)\). Using 128 cGy/min as the final answer when the stem supplies those factors understates or overstates the dose.

**Wrong turns**

- Point A marked 2 cm superior and 2 cm **anterior**, or 2 cm lateral from the skin. Lateral is from the uterine canal, and the superior step is from the external os.
- Prescribing a cylinder on the surface when the order says 5 mm depth, or the reverse.
- Inverse square from the surface instead of from the source. The 2.5 cm is from the center.
- PDD or TMR in a brachytherapy time calculation.

**Traps.** Draw the os, the canal, point A, and point B before any arithmetic. Then ask whether the stem wants Manchester point A or a contoured volume.

**Sources.** Manchester system as presented in Khan and Gibbons. ICRU point A definitions agree with the 2 cm by 2 cm description used here.

## HDR and LDR Delivery Systems

**Objectives:** V.2, I.5

**What the exam expects:** HDR uses a remote afterloader: the source is driven out of a shielded safe, through transfer tubes, into the applicator, and then retracted. The operator is outside the room. LDR Cs-137 was manual or remote; permanent seeds are implanted and stay. After an HDR fraction the source must be confirmed retracted by the unit **and** by a survey of the patient.

The source steps along the catheter and dwells (stops) at each planned position. Dwell time at a stop is the dose from that stop divided by the dose rate there. The times loaded for treatment are the times decayed to the treatment date. Before the source leaves the safe, check the transfer-tube length against the plan: a long or short tube shifts every dwell even when the times are numerically right. The survey meter is on before the source is sent out. After the source returns, survey the patient and compare the reading with background. The emergency kit has long tongs and a shielded container for a source that will not park. AAPM TG-56 is the brachytherapy physics code of practice. AAPM TG-59 is the HDR treatment-delivery report. Those names are the whole of the tolerance story in this note. There is no tolerance table here.

### Worked example

**Given.** Background in the room is 0.10 µSv/h. After the afterloader reports “source retracted,” a survey at the patient reads 0.12 µSv/h. On a different run the meter reads 2.0 mSv/h at the patient.

**Arithmetic.** \(2.0\) mSv/h \(= 2000\) µSv/h. \(2000 / 0.10 = 20000\). The emergency reading is about 20,000 times background. The 0.12 µSv/h reading is within a hair of background (\(0.02\) µSv/h above it).

**Check.** \(0.12 - 0.10 = 0.02\). \(2.0\) mSv/h is not 2.0 µSv/h. A unit slip of 1000 changes a safe reading into an emergency.

**Result means.** The 0.12 µSv/h survey supports “source out of the patient and source retracted.” The 2.0 mSv/h survey means the source is still out. Do not release the patient. Follow the emergency procedure for a stuck source (retract from the console, then the emergency hand crank if the plan requires it, then the shielded safe). The console light by itself is not the survey.

**Wrong turns**

- Surveying only the afterloader head and not the patient.
- Treating “source out” as the normal treatment state and sending the patient home. After treatment, source out of the patient means retracted.
- Skipping the pre-treatment background, so a slightly hot reading has nothing to be compared with.

**Traps.** Read the unit on the meter (µSv/h versus mSv/h) before you call a reading background.

**Sources.** NRC 10 CFR 35, HDR emergency and survey practice, as taught with TG-43 era afterloaders. Khan and Gibbons, remote afterloading.

## Brachytherapy treatment device verification (seeds applicators)

**Objectives:** V.3, V.4

**What the exam expects:** Count and assay seeds. Autoradiograph a ribbon for uniformity. Check applicator length, diameter, and channel (the cylinder radius that set \(r = 2.5\) cm above). A missing seed shows up as a short assay and as a blank on the film.

### Worked example

**Given.** The order is 10 seeds at 0.40 mCi each. The well-chamber assay of the batch is 3.60 mCi. An autoradiograph of the loaded ribbon shows one blank position.

**Substitute.** Expected activity \(= 10 \times 0.40 = 4.00\) mCi. Apparent seed count \(= 3.60 / 0.40 = 9\).

**Check.** \(9 \times 0.40 = 3.60\). \(4.00 - 3.60 = 0.40\) mCi, exactly one seed.

**Result means.** One seed is missing or inactive. The autoradiograph agrees with the assay. Do not implant the ribbon as if it were 10 seeds. Uniform blackening would have supported a uniform source; the blank is the failure.

**Wrong turns**

- Accepting the assay because 3.60 is “close” to 4.00. It is 10% low, and the film shows why.
- Using autoradiography as a patient survey meter.
- Ignoring applicator radius when the plan was made for a 2.0 cm cylinder and a 2.5 cm cylinder was sterilized instead. Every dwell distance changes.

**Traps.** Compare three numbers: seeds ordered, activity assayed, spots on the film.

**Sources.** AAPM TG-43 and TG-137 style seed-assay practice (batch assay and autoradiography of ribbons). The uniformity check is the skill named in the blueprint.

## Secondary/Independent Calculations

**Objectives:** V.6, V.2

**What the exam expects:** An independent check of dwell time from prescription dose and dose rate at the point, plus a decay correction from the calibration date. The second person uses the source strength, the day, and the distance, not a copy of the planner’s MU-style scratch work.

**Core facts**

Dwell time is the dose divided by the dose rate at that dwell. The plan time used on the machine is that time decayed to the treatment date. A source that has decayed since calibration is weaker, so the dwell gets longer if the prescribed dose stays the same. Leaving the calibration-day times in place underdoses. Mean life is not this correction. Mean life is the permanent-implant integral.

**Formulas**

\[
t = \frac{D}{\dot{D}}
\qquad
\dot{D}_{\text{today}} = \dot{D}_{\text{cal}}\, e^{-0.693\, t / T_{1/2}}
\]

- \(D\): prescription dose (cGy)
- \(\dot{D}\): dose rate at the prescription point on the treatment day (cGy per unit time)
- \(t\) in the first formula: treatment time
- \(t\) in the exponent: time since calibration, same unit as \(T_{1/2}\)

### Worked example: dwell time

**Given.** Prescription 600 cGy at point A. Independent dose rate at point A today is 450 cGy/min.

**Substitute.** \(t = 600/450 = 1.333\) min \(= 80\) s.

**Check.** \(450 \times (80/60) = 450 \times 4/3 = 600\) cGy.

**Result means.** The channel needs 80 seconds of source dwell, in whatever dwell-position split the plan uses, for 600 cGy at this dose rate. A plan that says 80 seconds agrees. A plan that says 1.33 hours has the unit wrong by 60.

### Worked example: decay missed

**Given.** The 600 cGy plan was computed with the calibration-day dose rate. Treatment is 8.0 days later. Ir-192 half-life is 73.8 days. The source was not decayed in the plan.

**Substitute.**

\[
\frac{0.693 \times 8.0}{73.8} = \frac{5.544}{73.8} = 0.07512
\]

\[
e^{-0.07512} = 0.9276
\qquad
\text{delivered} = 600 \times 0.9276 = 556.6 \text{ cGy}
\]

**Check.** \(0.693 \times 8 = 5.544\). \(5.544/73.8 = 0.07512\). \(600 \times 0.93 = 558\), and \(600 \times 0.0024 = 1.44\), so \(558 - 1.44 = 556.6\).

**Result means.** The patient receives about 557 cGy, not 600 cGy, because the source is weaker than the plan assumed. Forgetting decay on an HDR source underdoses. Applying the decay factor twice underdoses again. Using 1.443 here is the mean-life mistake: this is an 8-day HDR fraction, not a permanent implant.

**Wrong turns**

- Half-life versus mean life on a short HDR course.
- Hours versus minutes on the dwell time.
- Decaying Cs-137 by a large factor over a week. Its half-life is 30 years; a week is negligible. Ir-192 over a week is not.
- PDD in the time formula.

**Traps.** Date of calibration, date of treatment, and half-life go on the page before the exponential.

**Sources.** Khan and Gibbons, decay correction and treatment time. TG-43 source strength is what \(\dot{D}\) came from.

## Surveying (background pre and post implant, shielding, bedside dose)

**Objectives:** V.4

**What the exam expects:** Survey background before the procedure. After HDR, survey with the source retracted and confirm the reading matches background (previous lesson). For an inpatient LDR implant, inverse square turns a reading at 1 m into a bedside reading. Portable shields and the afterloader safe are the shielding, not a lead apron as the whole plan.

**Formula.** Same inverse square as module 33, now for exposure or dose rate around a source:

\[
\dot{D}_2 = \dot{D}_1 \left(\frac{d_1}{d_2}\right)^2
\]

### Worked example

**Given.** A survey reads 0.040 mSv/h at 1.0 m from an LDR patient. The bedside chair is 0.50 m from the patient. Inverse square only.

**Substitute.**

\[
\dot{D}(0.50) = 0.040 \left(\frac{1.0}{0.50}\right)^2 = 0.040 \times 4 = 0.160 \text{ mSv/h}
\]

**Check.** \(0.160 \times (0.50/1.0)^2 = 0.160 \times 0.25 = 0.040\).

**Result means.** Halving the distance quadruples the dose rate, from 0.040 mSv/h at 1 m to 0.160 mSv/h at the bedside. Visitor time limits use the bedside number, not the 1 m number. A shield between the chair and the patient is a transmission problem (module 36), applied after this geometry.

**Wrong turns**

- Linear distance: half the distance, half the rate (0.020 mSv/h), which is the wrong direction and the wrong power.
- Forgetting the pre-implant background and subtracting nothing, or subtracting background twice.
- Surveying an HDR patient only before the source is sent out and skipping the post-treatment survey.

**Traps.** “Source out” after HDR means you are proving the source is **not** in the patient. “Source retracted” is the console status that must agree with the meter.

**Sources.** 10 CFR 35 survey requirements after HDR. Khan and Gibbons, exposure around an implant and inverse square.

## Regulatory requirements for radioactive sources (NRC vs. State requirements)

**Objectives:** V.5

**What the exam expects:** The Nuclear Regulatory Commission licenses byproduct material in non-agreement states. An agreement state has taken that licensing authority under an agreement with the NRC and enforces compatible rules. The medical-use requirements (surveys, source inventory, written procedures, authorized users) still apply. Know which authority signs the license at the facility in the stem.

A sealed-source leak test is due on the regulatory interval (commonly six months for many sources). The usual pass criterion is 185 Bq, which is 0.005 µCi. A higher reading means the source is leaking and is removed from use.

A written directive (10 CFR 35.40) is dated and signed by the authorized user before the treatment, and it names the patient. The teaching contents are the nuclide and the site, plus either the dose or the activity and the time. Before an HDR fraction the directive states the radionuclide, the treatment site, the dose per fraction, the number of fractions, and the total dose. Before a temporary LDR implant it states the radionuclide, the site, and the dose. If that LDR order is written as activity instead of dose, it states the total source strength and the exposure time. Before a permanent seed implant it states the radionuclide, the site, and the total source strength.

A medical event (10 CFR 35.3045), in the usual teaching form, is treatment of the wrong patient, a dose to the wrong site, or a delivered dose that differs from the prescribed dose by the regulatory threshold: about 20% of the prescribed dose, or about 50% of a single fraction. Report it verbally in about 24 hours and in writing in about 15 days.

Patient release (10 CFR 35.75) is allowed when the total effective dose equivalent to any other individual is not likely to exceed 5 mSv.

The authorized user is the physician on the license who signs the written directive and is responsible for the administration. The authorized medical physicist calibrates the source, prepares and checks the plan, and checks the dwells. The radiation safety officer runs the safety program: inventories, leak tests, surveys, and the reports the license requires.

The inventory idea in this bank is quarterly: a physical count of each brachytherapy source, with its nuclide, nominal activity, and location. That count is not the six-month leak test. After an HDR fraction, survey the patient once the source has returned to the safe. Do not treat the console light as that survey.

### Worked example

**Given.** A leak test measures 300 Bq. The limit in the stem is 185 Bq (0.005 µCi).

**Arithmetic.** \(300 > 185\). The excess is \(300 - 185 = 115\) Bq. In microcuries, \(185\) Bq \(= 0.005\) µCi because \(1\) µCi \(= 37000\) Bq and \(0.005 \times 37000 = 185\).

**Check.** \(37000 \times 0.005 = 185\). \(300/37000 = 0.0081\) µCi, which is above 0.005 µCi.

**Result means.** The source fails the leak test. It comes out of service. Agreement-state licensees and NRC licensees both honor this criterion when their regulations adopt it. “We are an agreement state” does not retire the leak test.

**Wrong turns**

- Treating an agreement state as unregulated.
- Converting 0.005 µCi as 5 Bq or 5000 Bq. The factor is 37000 Bq per µCi.
- Using NCRP occupational dose limits as the leak-test threshold. Leak test is activity on the wipe, not a personnel dose.

**Traps.** The stem’s phrase “agreement state” tells you who inspects. It does not change the physics of the source.

**Sources.** 10 CFR 35 (medical use) and the agreement-state program under the Atomic Energy Act. Leak-test activity 185 Bq (0.005 µCi) is the standard sealed-source criterion in that framework.

## Brachytherapy Quiz

**Skills this quiz checks**

- Match Ir-192, Cs-137, I-125, and Pd-103 to half-life, energy, and HDR, LDR, or permanent seeds.
- Place point A 2 cm up from the external os and 2 cm lateral to the canal.
- Use half-life for remaining activity and mean life (\(1.443 \times T_{1/2}\)) only for complete decay.
- Require both a retracted-source indicator and a post-treatment patient survey.
- Read a seed assay against the order and an autoradiograph.
- Separate NRC states from agreement states without dropping the survey or leak-test requirement.
- Match Ir-192 about 380 keV, Cs-137 662 keV, I-125 about 28 keV, and Pd-103 about 21 keV.
- Place the ICRU 38 bladder and rectum points, and use this bank’s GEC-ESTRO correlates: HR-CTV D90, rectum D2cc near 65–75 Gy EQD2, bladder D2cc near 80–90 Gy EQD2.
- Recognize vaginal cuff 7 Gy × 3 at 0.5 cm, cervix 7 Gy × 4 or 5.5 Gy × 5, prostate HDR 13.5 Gy × 2, I-125 145 Gy, Pd-103 125 Gy, and an I-125 eye plaque of 85 Gy to the apex.
- State the written-directive contents, the medical-event teaching thresholds (about 20% of the prescribed dose, or about 50% of a fraction) and the report clocks (about 24 hours verbal, about 15 days written), and patient release at 5 mSv.

## Brachytherapy Calculations

**Objectives:** V.6, V.1

**What the exam expects:** Write the TG-43 dose-rate equation with every symbol, evaluate it at a point, and compute permanent-implant total dose as initial dose rate times 1.443 times half-life. Units of dose rate and half-life have to match.

Air-kerma strength is the source specification in this equation. 1 U = 1 µGy m²/h = 1 cGy cm²/h. A microgray times a square meter is the same product as a centigray times a square centimeter. Apparent activity, in mCi or Ci, is a derived label on some source certificates. This bank does not use a single mCi-per-U factor. If a problem wants activity, the stem gives the activity. Do not multiply a strength in U by a constant written per mCi.

**TG-43**

\[
\dot{D}(r,\theta) = S_K \cdot \Lambda \cdot \frac{G(r,\theta)}{G(r_0,\theta_0)} \cdot g(r) \cdot F(r,\theta)
\]

- \(\dot{D}(r,\theta)\): dose rate at distance \(r\) and angle \(\theta\)
- \(S_K\): air-kerma strength, the source specification. 1 U = 1 µGy m² h⁻¹ = 1 cGy cm² h⁻¹. Apparent activity is a derived label, not a second definition of U
- \(\Lambda\): dose-rate constant (cGy h⁻¹ U⁻¹), converts strength to dose rate at the reference point in water
- \(G(r,\theta)\): geometry function. For a point source, \(G = 1/r^2\)
- \(G(r_0,\theta_0)\): geometry function at the reference point, usually \(r_0 = 1\) cm and \(\theta_0 = 90^\circ\) (transverse axis). Call this \(G_0\)
- \(g(r)\): radial dose function, absorption and scatter along the transverse axis. \(g(r_0) = 1\) by definition
- \(F(r,\theta)\): anisotropy function. \(F(r, 90^\circ) = 1\). It drops when the point looks down the source axis

**Permanent implant, complete decay**

\[
D_{\text{total}} = \dot{D}_0 \times 1.443 \times T_{1/2}
\]

- \(\dot{D}_0\): initial dose rate
- \(T_{1/2}\): half-life in the same time unit as the dose rate’s denominator
- \(1.443\): \(1/\ln 2\), so \(1.443 \times T_{1/2}\) is the mean life

### Worked example: TG-43

**Given.** \(S_K = 40000\) U. The source model’s \(\Lambda = 1.115\) cGy h⁻¹ U⁻¹ (use the model’s constant; this is the value for the example). At \(r = 2.0\) cm on the transverse axis, the source is treated as a point, \(g(2) = 0.980\) from the source table in the stem, and \(F = 1\).

**Substitute.** At 1 cm on the transverse axis, \(G/G_0 = 1\), \(g = 1\), \(F = 1\), so

\[
\dot{D}(1, 90^\circ) = 40000 \times 1.115 = 44600 \text{ cGy/h}
\]

At 2 cm, \(G/G_0 = (1/2)^2 = 0.25\).

\[
\dot{D}(2, 90^\circ) = 44600 \times 0.25 \times 0.980 \times 1 = 11150 \times 0.980
\]

**Arithmetic.** \(40000 \times 1.115 = 44600\). \(44600 \times 0.25 = 11150\). \(11150 \times 0.98 = 11150 - 223 = 10927\) cGy/h.

**Check.** \(11150 \times 0.02 = 223\), and \(11150 - 223 = 10927\). Dropping \(g(r)\) leaves 11150 cGy/h, about 2% high. Using \((1/2)\) instead of \((1/2)^2\) leaves a factor of 0.5 and about 21850 cGy/h.

**Result means.** The dose rate 2 cm out on the transverse axis is 10927 cGy/h, which is 109.3 Gy/h. That is an HDR-scale rate at 2 cm for a 40000 U Ir-192 source. Geometry supplies the factor of 1/4. The radial dose function supplies the extra 2%.

### Worked example: permanent implant

**Given.** Pd-103, half-life 17.0 days. Initial dose rate 10.0 cGy/h. The implant is permanent.

**Substitute.** \(T_{1/2} = 17.0 \times 24 = 408\) h.

\[
D = 10.0 \times 1.443 \times 408
\]

**Arithmetic.** \(1.443 \times 400 = 577.2\). \(1.443 \times 8 = 11.544\). Mean life \(= 588.744\) h. \(10 \times 588.744 = 5887\) cGy.

**Check.** \(1.443 \times 408 = 588.744\). If the 1.443 is omitted, \(10 \times 408 = 4080\) cGy, which is the half-life mistake and is low by the factor 1.443 (\(4080 \times 1.443 = 5887\)).

**Result means.** The total dose delivered as the seeds decay completely is 5887 cGy (58.87 Gy), not 4080 cGy. I-125 problems are the same formula with 59.4 days. HDR dwell time is not this formula.

**Wrong turns**

- Half-life in the permanent-dose product without 1.443.
- Mean life in an HDR decay over a few days.
- \(G/G_0 = r_0/r\) without the square.
- \(S_K\) in mCi multiplied by \(\Lambda\) in per-U, with no conversion. The stem should give air-kerma strength in U for this equation. Exposure-rate constants (next lesson) are the mCi route.
- Point A used as \(r = 1\) cm. Point A is 2 cm lateral.

**Traps.** Write the unit of \(\dot{D}_0\) and the unit of \(T_{1/2}\) on the same line. Convert days to hours before multiplying a cGy/h dose rate.

**Sources.** Nath et al., AAPM TG-43 (and TG-43U1 updates) for the dose-rate equation. Khan and Gibbons for the mean-life integral of a permanent implant.

## Brachytherapy Calculations Quiz

**Skills this quiz checks**

- Evaluate \(S_K \Lambda (G/G_0) g F\) and name each factor.
- Square the geometry ratio for a point source.
- Compute permanent-implant total dose with 1.443 and a half-life in the dose rate’s time unit.
- Reject the half-life-only product (the 4080 cGy pattern) and reject mean life on a short HDR decay.
- Keep mCi and U from being multiplied by the wrong constant.
- State 1 U as 1 µGy m²/h and as 1 cGy cm²/h, and keep apparent activity as a label rather than a universal mCi-per-U factor.
- Take dwell time as dose divided by dose rate at the dwell, with the plan time decayed to the treatment date.
- Define TRAK as the sum over sources of reference air-kerma rate times duration.

## Exposure Rate Calculation Tutorial

**Objectives:** V.6, I.10

**What the exam expects:** Exposure rate from a point source falls as \(1/d^2\). Use the specific gamma-ray constant the stem gives. If the stem does not give one, the memory values below are the usual approximations, and the stem still wins when it prints a different \(\Gamma\).

**Formula**

\[
X = \frac{\Gamma A}{d^2}
\]

- \(X\): exposure rate
- \(\Gamma\): specific gamma-ray constant (exposure rate constant)
- \(A\): activity
- \(d\): distance from a point source

Units travel together. If \(\Gamma\) is in R cm² mCi⁻¹ h⁻¹, then \(A\) is in mCi, \(d\) is in cm, and \(X\) is in R/h.

Approximate constants when the stem is silent:

- Ir-192: about 4.69 R cm² mCi⁻¹ h⁻¹
- Cs-137: about 3.26 R cm² mCi⁻¹ h⁻¹
- Co-60: about 13.1 R cm² mCi⁻¹ h⁻¹
- Ra-226: about 8.25 R cm² mg⁻¹ h⁻¹ (milligrams of radium, not mCi)

No I-125 constant is memorized here; use the stem.

### Worked example

**Given.** Ir-192, \(\Gamma = 4.69\) R cm² mCi⁻¹ h⁻¹, \(A = 10\) mCi, \(d = 100\) cm.

**Substitute.**

\[
X = \frac{4.69 \times 10}{100^2} = \frac{46.9}{10000} = 0.00469 \text{ R/h}
\]

**Arithmetic.** \(4.69 \times 10 = 46.9\). \(100^2 = 10000\). \(46.9/10000 = 0.00469\) R/h \(= 4.69\) mR/h.

**Check.** At 50 cm the rate is four times higher because distance is halved: \(4.69 \times 4 = 18.76\) mR/h. And \(4.69 \times 10 / 50^2 = 46.9/2500 = 0.01876\) R/h. Same answer.

**Result means.** A 10 mCi Ir-192 source produces about 4.69 mR/h at 1 m under this constant, point-source, no-shielding conditions. A bedside shield is an extra transmission factor. TG-43, not this equation, is how the implant dose in tissue is calculated. This equation is the survey and room-exposure route.

**Wrong turns**

- Forgetting to square \(d\): \(46.9/100 = 0.469\) R/h, one hundred times too high.
- Using the radium constant 8.25 with mCi of iridium.
- Using Co-60’s 13.1 for Ir-192.
- Reporting R/h when the question asks for mR/h (factor of 1000).
- Half-life corrections mixed into \(\Gamma\). Decay the activity first, then apply \(\Gamma\) to the activity on that day.

**Traps.** Write \(\Gamma\)’s units above the substitution. If they contain cm², the distance is in cm. A distance of 1 m entered as “1” with a cm-based \(\Gamma\) is wrong by \(100^2\).

**Sources.** Khan and Gibbons, exposure rate constant and inverse square. The numeric constants above are the traditional approximate values; a problem that prints \(\Gamma\) wants that printed value.

## Classical Implant Systems, Radium Equivalence, and Line Sources

**Objectives:** V.2, V.1, V.6

**What the exam expects:** Tell the three classical interstitial systems apart by their distribution rule and their prescription point, convert between millicuries and milligram-radium-equivalent with the ratio of gamma constants, separate active length from physical length, and know what a Sievert integral and an along-and-away table are for. None of this replaces TG-43; it is the vocabulary that still appears in items and in older applicator literature.

**Manchester (Paterson–Parker).** The design goal is a dose that is uniform to within about ±10% over the treated plane, evaluated 0.5 cm from the plane of the sources. To get that, the activity is distributed non-uniformly: more at the periphery, less in the middle. For a planar implant the periphery-to-center split depends on the area. Under 25 cm², two thirds of the activity goes to the periphery and one third to the center. From 25 to 100 cm² the split is half and half. Over 100 cm² only one third is on the periphery and two thirds in the center. Needles are spaced no more than 1 cm apart, and the ends of the plane are closed with crossing needles. If an end cannot be crossed, the effective treated area is reduced by 10% for each uncrossed end before the table is read. The stated (prescribed) dose is 10% above the minimum dose in the plane, so the minimum is about 90% of what is written. A single plane covers a slab up to about 1 cm thick; two parallel planes handle thicknesses up to about 2.5 cm; anything thicker is a volume implant. Volume rules divide the activity into eighths: a cylinder gets four parts in the belt, two in the core, and one at each end; a sphere gets six parts in the shell and two in the core; a cube gets one part on each of six faces and two in the core. The belt needs at least eight needles and the core at least four, and each uncrossed end of a volume implant removes 7.5% of the effective volume. The historical tables are written in milligram-hours of radium per 1000 R, which is why milligram-radium-equivalent survives as a unit.

**Quimby and Memorial.** Quimby used uniformly spaced sources of equal linear activity. The dose is then non-uniform: hottest at the center of the plane and lower at the edges. For a planar Quimby implant the stated dose is the maximum dose in the treatment plane (center), and for a volume implant it is the minimum dose inside the implanted volume. For the same minimum peripheral dose, a Quimby implant needs more total milligram-hours than a Manchester implant. The Memorial system extended Quimby into the computer era: seeds of equal strength on a 1 cm lattice, with nomograms that give total activity from the average dimension of the target. The prostate seed nomograms descend from that work.

**Paris.** Built for Ir-192 wires and ribbons of uniform linear activity. The sources are straight, parallel, equidistant, of equal length, and arranged so their midpoints lie in one central plane perpendicular to the sources, either in a single plane or in two planes forming squares or triangles. Spacing is typically 8–15 mm (the original description allows about 5–20 mm, wider for larger volumes). Nothing is crossed, so each line must be longer than the target: the active length runs about 30–40% beyond the target length so that the end fall-off still covers it. The basal dose is the arithmetic mean of the local minimum dose rates found between adjacent sources in the central plane. The reference isodose, which is the prescription surface, is 85% of the basal dose. For a single plane the treated thickness is roughly half the spacing.

**ICRU 58 vocabulary.** ICRU Report 58 (interstitial reporting) took the Paris idea and gave it names. The mean central dose (MCD) is the mean of the local minimum doses between sources in the central plane, which is the basal dose. The minimum target dose (MTD) is the lowest dose at the periphery of the clinical target volume, which in a Paris implant is the reference dose. The high-dose volume is the tissue enclosed by 150% of the MCD. The low-dose volume is the part of the CTV that receives less than 90% of the prescribed dose. Dose uniformity is reported as the spread of the individual central minima and as the dose homogeneity index, MTD divided by MCD (0.85 in a Paris implant). ICRU 58 also asks for the TRAK, the source description, and the time pattern, and it notes that for interstitial work the PTV is usually taken equal to the CTV because the sources move with the tissue.

**Contrasts to remember.** Manchester: non-uniform activity, uniform dose, prescription 10% above the minimum, needles crossed. Quimby: uniform activity, non-uniform dose, central hot spot, planar prescription at the maximum. Paris: uniform linear activity, uncrossed parallel lines, prescription at 85% of the basal dose. Every modern HDR optimizer produces the same trade-off: push dwell weight to the periphery to flatten the dose (Manchester-like) or leave it uniform and accept a hot center (Quimby-like).

**Milligram-radium-equivalent.** One milligram of Ra-226 in equilibrium with its daughters, filtered by 0.5 mm of platinum, gives an exposure rate of 8.25 R/h at 1 cm, so \(\Gamma_{Ra} = 8.25\) R cm² mg⁻¹ h⁻¹. A source of any nuclide is "N mg-Ra-eq" when it produces the same exposure rate at the same distance as N mg of radium. The conversion is a ratio of gamma constants:

\[
\text{mg-Ra-eq} = A_{\text{mCi}} \times \frac{\Gamma_{\text{nuclide}}}{8.25}
\qquad
A_{\text{mCi}} = \text{mg-Ra-eq} \times \frac{8.25}{\Gamma_{\text{nuclide}}}
\]

Because \(0.876\) cGy of air kerma corresponds to 1 R, one mg-Ra-eq is \(8.25 \times 0.876 = 7.227\) cGy cm² h⁻¹, that is, 7.227 U of air-kerma strength. Milligram-hours (mg-h) is strength multiplied by time, the integrated quantity the Manchester tables are written in.

### Worked example: mg-Ra-eq

**Given.** A Cs-137 tube is labeled 30 mCi. \(\Gamma_{Cs} = 3.26\) R cm² mCi⁻¹ h⁻¹.

**Substitute.** \(30 \times 3.26 / 8.25 = 97.8 / 8.25 = 11.85\) mg-Ra-eq.

**Check.** The cesium constant is less than half the radium constant, so a millicurie of cesium is worth less than half a milligram of radium: \(11.85 / 30 = 0.395\) mg-Ra-eq per mCi. The inverted ratio, \(30 \times 8.25 / 3.26 = 75.9\), would make a weak emitter look stronger than radium and is the classic wrong turn. In air-kerma strength the tube is \(11.85 \times 7.227 = 85.6\) U.

**Result means.** The tube behaves like 11.85 mg of radium for exposure-rate purposes. An order written as "15 mg-Ra-eq of Cs-137" is \(15 \times 8.25 / 3.26 = 38.0\) mCi.

**Active versus physical length.** The active length is the length of the radioactive material inside the capsule. The physical (overall) length includes the inactive end caps and eyelet, so it is always longer. A typical Cs-137 intracavitary tube has an active length of about 1.4 cm inside a 2.0 cm capsule. Classical radium needles were specified by linear activity, 0.66 mg/cm for full intensity and 0.33 mg/cm for half intensity, over their active length. Ir-192 ribbon seeds are about 3 mm long on 1 cm centers. An HDR Ir-192 source is a cylinder roughly 3.5–5 mm long and under 1 mm in diameter at the end of a drive cable, which is why the first dwell position sits a few millimeters short of the catheter tip. Dose tables and Sievert integrals use the active length; what fits in an applicator, and how far a source center is from the tip, uses the physical length.

**Sievert integral and along-and-away tables.** A line source is treated as a row of point elements. Each element contributes \(\Gamma\,dA / r^2\), reduced by oblique filtration through the capsule wall, \(e^{-\mu t \sec\theta}\), and the contributions are integrated over the active length. The result is the Sievert integral. Because it depends only on the point's position relative to the source center, it is tabulated for a unit strength (1 mg-Ra-eq or 1 U), one active length, and one filtration, as a grid of distance along the source axis versus distance away from it. To use the table for an implant, locate each source's center, express the calculation point as (along, away) for that source, read or interpolate the table, multiply by that source's strength, and add the sources. Far from a source the line behaves like a point: beyond about twice the active length the inverse-square estimate is within a few percent of the integral. Closer in, the dose falls more slowly than \(1/d^2\), approaching \(1/d\) for a point very near a long line, and the point-source shortcut overstates the fall-off.

### Worked example: along-and-away table

**Given.** Two identical Cs-137 tubes of 20 mg-Ra-eq each lie end to end on one axis with their centers 2.0 cm apart. Point P is 1.5 cm from the axis, directly opposite the center of the first tube. The table for this tube, in cGy/h per mg-Ra-eq, reads 2.90 at (along 0, away 1.5 cm) and 1.10 at (along 2.0, away 1.5 cm).

**Substitute.** First tube: \(20 \times 2.90 = 58.0\) cGy/h. Second tube, 2.0 cm along the axis from P's foot: \(20 \times 1.10 = 22.0\) cGy/h. Total \(= 80.0\) cGy/h.

**Check.** A point-source estimate for the second tube is \(20 \times 7.227 / (2.0^2 + 1.5^2) = 144.5 / 6.25 = 23.1\) cGy/h, a little above the table's 22.0 because the table also carries oblique filtration and the finite length. The order of magnitude agrees, so the table reading was taken at the right cell.

**Result means.** Each source needs its own (along, away) pair; using the first tube's coordinates for both would give \(2 \times 58 = 116\) cGy/h, 45% high.

**Wrong turns**

- Giving Quimby the periphery-heavy loading, or Manchester the hot center. It is the other way round.
- Prescribing a Paris implant to the basal dose instead of 85% of it.
- Multiplying by \(8.25/\Gamma\) when converting mCi to mg-Ra-eq (the ratio must make a weak gamma emitter worth fewer milligrams).
- Using the physical length as the active length in a dose table.
- Applying inverse square to a point closer than about two active lengths from a long source.

**Traps.** When a stem says "stated dose" with Manchester, the minimum in the plane is 10% lower. When it says "reference dose" with Paris, the basal dose is higher by the factor 1/0.85.

**Sources.** Khan and Gibbons, implant systems and radium-equivalent specification; ICRU Report 58 for interstitial reporting terms; Paterson–Parker and Paris descriptions as summarized in standard texts.

## Decay Arithmetic for Permanent Implants and Afterloaders

**Objectives:** V.6, I.7

**What the exam expects:** Four decay calculations beyond the plain exponential: the dose from a decaying implant that is removed before it has fully decayed, the removal time that delivers a prescribed dose, the rescaling of an HDR or applicator treatment time when the source has decayed between planning and treatment, and a half-life or crossing time recovered from two activities. All four use the same two constants: \(\lambda = 0.693 / T_{1/2}\) and the mean life \(T_{avg} = 1.443\, T_{1/2}\).

**Dose from a decaying source over a finite time.** If the dose rate starts at \(\dot{D}_0\) and decays with the source, the dose delivered by time \(t\) is the integral of \(\dot{D}_0 e^{-t/T_{avg}}\):

\[
D(t) = \dot{D}_0\, T_{avg}\left(1 - e^{-t/T_{avg}}\right)
\qquad
\frac{D(t)}{D_{\infty}} = 1 - e^{-t/T_{avg}}
\]

\(D_\infty = \dot{D}_0 T_{avg}\) is the familiar permanent-implant total. The bracket is the fraction of that total delivered so far. After one half-life it is exactly one half (\(1 - e^{-0.693} = 0.500\)); after two half-lives three quarters; 90% of the total has been delivered after \(2.303\, T_{avg} = 3.32\, T_{1/2}\). Solving for the time that delivers a chosen dose:

\[
t = -T_{avg} \ln\left(1 - \frac{D}{\dot{D}_0 T_{avg}}\right)
\]

which only has a solution when \(D\) is less than \(D_\infty\). For a short HDR fraction the bracket is indistinguishable from \(t / T_{avg}\) and \(t = D/\dot{D}\) is exact enough; for a multi-day Ir-192 LDR implant the correction is a few percent and the exam expects it.

### Worked example: I-125 implant removed early

**Given.** An I-125 implant started at 7.0 cGy/h. The prescription assumed complete decay. The seeds are removed (prostatectomy) after 60 days. \(T_{1/2} = 59.4\) d.

**Substitute.** \(T_{avg} = 1.443 \times 59.4 = 85.7\) d \(= 2057\) h. \(D_\infty = 7.0 \times 2057 = 14400\) cGy \(= 144\) Gy. Fraction delivered \(= 1 - e^{-60/85.7} = 1 - e^{-0.700} = 1 - 0.497 = 0.503\). Delivered dose \(= 144 \times 0.503 = 72.5\) Gy.

**Check.** Sixty days is almost exactly one half-life (59.4 d), and one half-life delivers one half of the total: \(144 / 2 = 72\) Gy. The small excess over 72 comes from the extra 0.6 day. Ignoring decay would give \(7.0 \times 24 \times 60 = 10080\) cGy, 101 Gy, which overstates the dose by 39%.

**Result means.** The gland received about 72.5 Gy, not the 144 Gy total and not the 101 Gy that a constant dose rate would give.

### Worked example: removal time for an Ir-192 LDR implant

**Given.** A temporary Ir-192 implant is to deliver 60 Gy. The initial dose rate at the prescription isodose is 50 cGy/h. \(T_{1/2} = 73.8\) d.

**Substitute.** \(T_{avg} = 1.443 \times 73.8 = 106.5\) d \(= 2556\) h. \(D_\infty = 50 \times 2556 = 127800\) cGy. Ratio \(D / D_\infty = 6000 / 127800 = 0.0469\). \(t = -2556 \times \ln(1 - 0.0469) = -2556 \times \ln(0.9531) = 2556 \times 0.0481 = 122.9\) h.

**Check.** Without decay, \(6000 / 50 = 120\) h. The source loses about 1% per day, so over five days the average dose rate is about 2.5% below the starting value and the time should be about 2.5% longer: \(120 \times 1.025 = 123\) h. Agrees.

**Result means.** Schedule removal at about 123 hours, roughly 3 hours later than the no-decay estimate. Removing at 120 h underdoses by about 1.5 Gy.

**Rescaling an HDR or applicator time for decay.** For the same dose from the same geometry, dose rate times time is constant, so

\[
t_2 = t_1 \frac{A_1}{A_2} = t_1\, e^{\lambda \Delta t}
\]

where \(\Delta t\) is the time elapsed from the planning (or calibration) date to the treatment date. The later treatment is always longer. Rules of thumb: Ir-192 loses about 1% per day (so a 10-day delay adds about 10% to the time), Co-60 about 1% per month, Cs-137 about 2.3% per year, Sr-90 about 2.4% per year. The afterloader does this from its decay table every day; the independent check reproduces it by hand.

### Worked example: fraction two after ten days

**Given.** Fraction one of a cylinder course ran a total dwell of 300 s. Fraction two is 10 days later on the same Ir-192 source with the same plan.

**Substitute.** \(\lambda \Delta t = 0.693 \times 10 / 73.8 = 0.0939\). \(e^{0.0939} = 1.098\). \(t_2 = 300 \times 1.098 = 329.5\) s, about 330 s.

**Check.** Ten days at about 1%/day is about 10% more time: \(300 \times 1.10 = 330\) s. Dividing instead of multiplying gives 273 s, which would underdose a weaker source, the wrong direction.

**Result means.** The second fraction needs about 330 s of total dwell. If the afterloader still shows 300 s, its decay table or source date is wrong and treatment stops until it is resolved.

**Half-life from two assays.** Two measurements of the same source separated by \(\Delta t\) give

\[
T_{1/2} = \frac{0.693\, \Delta t}{\ln(A_1 / A_2)}
\]

For example, a seed batch that reads 4.00 mCi and, 30 days later, 2.82 mCi has \(\ln(4.00/2.82) = \ln 1.418 = 0.3496\), so \(T_{1/2} = 0.693 \times 30 / 0.3496 = 59.5\) d, which identifies I-125. The same algebra gives the decay constant directly as \(\ln(A_1/A_2)/\Delta t\).

**Equal-activity crossing time.** Two sources of different nuclides have equal activity when \(A_1 e^{-\lambda_1 t} = A_2 e^{-\lambda_2 t}\), that is,

\[
t = \frac{\ln(A_2 / A_1)}{\lambda_2 - \lambda_1}
\]

with source 2 the one that starts stronger and decays faster. With 10 mCi of I-125 and 25 mCi of Pd-103: \(\lambda_I = 0.693/59.4 = 0.01167\) d⁻¹, \(\lambda_{Pd} = 0.693/17.0 = 0.04077\) d⁻¹, difference 0.02910 d⁻¹, \(\ln 2.5 = 0.916\), so \(t = 0.916 / 0.02910 = 31.5\) d. At that time both read about 6.9 mCi (\(10 e^{-0.367} = 6.93\); \(25 e^{-1.284} = 6.93\)). Some study keys print about 34 days for this problem; the bank uses 31.5 d because the arithmetic above is reproducible and the check closes. The qualitative point is more often tested: the shorter-lived nuclide must start with more activity to deliver the same total dose, and it is the hotter source only until the crossing time.

**Wrong turns**

- Using the half-life instead of the mean life inside the finite-time bracket (\(1 - e^{-t/T_{1/2}}\) overstates the delivered fraction).
- Rescaling a treatment time downward for a source that has decayed.
- Taking \(\ln(A_2/A_1)\) with the activities in the wrong order and getting a negative half-life.
- Forgetting that the crossing-time formula needs the difference of the decay constants, not their ratio.

**Traps.** When the stem says "removed after" or "explanted," the bracket applies. When it says "same plan, later date," the exponential ratio applies. Neither needs TG-43 factors because geometry has not changed.

**Sources.** Khan and Gibbons, decay and dose from temporary and permanent implants; AAPM TG-56 for decay correction practice; the finite-time integral as presented in standard brachytherapy physics texts.

## Site Procedures, Applicators, and HDR Program Numbers

**Objectives:** V.2, V.3, V.5

**What the exam expects:** The LDR prostate workflow from volume study to post-implant CT, the balloon and strut devices used for accelerated partial-breast irradiation and their numbers, the names of the interstitial templates and surface applicators, the point systems beyond Manchester A and B, the HDR QA tolerances a dosimetrist should recognize, who does what in an HDR emergency, and the current medical-event thresholds. Transport labels are mentioned only as vocabulary; the protection module carries the detail.

**LDR prostate workflow.** Candidates have a gland of roughly 20–60 cm³, no severe outlet obstruction, and no pubic-arch interference; a large gland is sometimes downsized with hormonal therapy first. The volume study is transrectal ultrasound (TRUS) in the dorsal lithotomy position with the probe in a stepper, axial images every 5 mm from base to apex, and the template grid (5 mm holes) superimposed. The prostate, urethra (Foley or aerated gel), and anterior rectal wall are contoured; the PTV is the prostate plus about 3–5 mm except 0 mm posteriorly toward the rectum. Loading is peripheral or modified peripheral: most seeds in the outer rows, few or none in the central needles, which keeps the urethra under about 150% while the periphery reaches prescription. Uniform loading, the Quimby pattern, over-doses the urethra. Monotherapy prescriptions are I-125 145 Gy, Pd-103 125 Gy, and Cs-131 115 Gy; as a boost after 45 Gy of external beam they drop to about 110, 100, and 85 Gy. Individual seed strengths are around 0.3–0.6 mCi apparent (about 0.4–0.8 U) for I-125 and higher for Pd-103, and an implant uses about 60–120 seeds depending on gland volume, nuclide, and strength. The seed count is total activity from the nomogram or plan divided by the per-seed strength, and about 10% extra is ordered. At least 10% of the seeds, or ten seeds, whichever is more, are assayed in a well chamber (a third-party assay traceable to the vendor's calibration is acceptable); the mean should agree with the certificate within about 3%, and a disagreement beyond 5% is resolved with the vendor. Preplan goals: V100 at least 95% (often 98–99%), D90 above 100% of prescription, V150 no more than about 50–60%, V200 no more than about 20%; urethra D10 below 150% and D30 below 130%; rectum V100 under 1 cm³. In the operating room the needles go in anterior rows first so that later needles do not shadow the ultrasound image of the ones still to be placed; seeds are delivered either one at a time with a Mick applicator or as pre-loaded strands, which migrate less and hold the periphery better. Fluoroscopy or cone-beam CT confirms the distribution, cystoscopy retrieves any seed in the bladder, and a GM survey of the room, drapes, and waste finds dropped seeds. The base is the hardest region to cover. Post-implant CT is done at about 30 days for I-125 (edema has resolved; TG-137 says 30 ± 7 days), about 16 days for Pd-103 and about 10 days for Cs-131; a same-day CT is acceptable but reads low because of edema. Post-implant D90 of at least 90% of prescription is the usual adequacy threshold, with the same urethral and rectal metrics. Patients leave the same day: the dose to others from I-125 or Pd-103 in the pelvis is far below the 5 mSv release criterion.

**Accelerated partial-breast brachytherapy.** The devices are a single-lumen balloon (MammoSite), multi-lumen balloons (Contura, with a central lumen and four offset lumens plus vacuum ports), and the strut-based SAVI, whose expandable struts around a central catheter give the most catheters and the most freedom to shape dose away from skin and ribs. The balloon is 4–5 cm in diameter (about 35–70 cm³) and must conform to the cavity with no more than about 10% of the PTV volume as air or fluid pockets. The prescription is 34 Gy in 10 fractions, twice daily at least 6 hours apart, over about 5 days, specified at 1 cm from the balloon or device surface. PTV_eval is the 1 cm shell outside the device surface, minus the device volume, trimmed to 5 mm inside the skin surface and excluding the chest wall and pectoralis. Goals: at least 90% of the prescription to at least 90% of PTV_eval; V150 no more than 50 cm³; V200 no more than 10 cm³; maximum skin dose no more than 145% (multi-lumen plans aim lower, about 125%); rib maximum about 145%. The device-to-skin distance should be at least 7 mm; a multi-lumen device can be planned down to about 5 mm. With a single central dwell the balloon surface sits at about 200% of the prescription, because the surface is at 2.5 cm from the center and the prescription at 3.5 cm: \((3.5/2.5)^2 = 1.96\).

**Templates and surface applicators.** The Syed–Neblett template is a perineal acrylic plate with needle holes on concentric rings around a vaginal obturator; needles are driven through it into the cervix, parametria, or vagina and afterloaded, usually with HDR Ir-192 today, when a tandem cannot be placed or disease is bulky or lateral. MUPIT is the same idea with a different plate. The Freiburg flap is a flexible silicone mat of 1 cm spheres that holds parallel catheters 1 cm apart and 5 mm above the skin; it conforms to curved surfaces (scalp, limbs, trunk) and is prescribed at about 3–5 mm depth. The Leipzig applicator is a tungsten-shielded cup, 1–3 cm in diameter, for a single dwell over a small skin lesion, prescribed at about 3 mm depth; the Valencia version adds a flattening filter for a flatter profile. Lesions deeper than about 4–5 mm are better served by electrons or by interstitial catheters.

**Optimization vocabulary.** Geometric optimization sets dwell times inversely to the dose each dwell receives from its neighbors, so end dwells get longer. Dose-point optimization adjusts times by least squares to meet dose points on the applicator surface or at depth. Inverse planning (IPSA, HIPO) minimizes a penalty function over target and organ objectives. Graphical optimization is a manual step after one of those: the planner drags an isodose line on the display, and the system changes the nearby dwell times so the line passes through the new position. It is quick and local, and because every change moves dose somewhere else, the DVH and the hot-spot volumes are re-checked after each drag.

**Special applications.** The Sr-90/Y-90 pterygium applicator is a sealed beta source pressed on the sclera after excision; Y-90 betas have a 2.28 MeV maximum energy, the dose falls to about half within a millimeter, surface dose rates are several cGy per second, and the 28.8-year half-life means the decay-corrected dose rate is updated about once a year. Electronic brachytherapy uses a miniature x-ray tube at about 50 kV (Xoft Axxent, Intrabeam) in a balloon, surface cone, or spherical applicator; there is no radionuclide, so byproduct-material licensing does not apply, the room needs little shielding, and staff can stay nearby, but the output must be verified per tube and the low energy raises the dose to bone and the surface relative to Ir-192. Intravascular brachytherapy treated in-stent coronary restenosis with beta (Sr-90/Y-90, P-32) or gamma (Ir-192) sources, prescribing about 15–20 Gy at 2 mm from the source axis; drug-eluting stents replaced it. Intraluminal HDR for the bronchus or esophagus is prescribed at 1 cm from the catheter axis in a few fractions (for example 7.5 Gy × 3 endobronchial).

**GYN points beyond A and B.** The lymphatic trapezoid (ICRU 38, from Fletcher) is drawn on the AP film: a line from the S1–S2 junction to the top of the symphysis, a second line from the midpoint of that line to the anterior middle of L4, and a trapezoid whose lower corners are 6 cm lateral to the midline at the pelvic-brim level (external iliac nodes), whose upper corners are 2 cm lateral at L4 (low para-aortic nodes), and whose side midpoints stand for the low common iliac nodes. The pelvic-wall points, also ICRU 38, lie on the AP film at the intersection of a horizontal tangent to the top of the acetabula with a vertical tangent to their inner edge, and on the lateral film at the mid-distance between the right and left points; they stand for the distal parametrium and obturator nodes and receive a dose similar to point B. ICRU Report 89 (2016) is the current cervix report: it keeps point A and the ICRU bladder and rectal points for continuity and adds the GEC-ESTRO volumes (GTV-res, HR-CTV, IR-CTV) with D90, D98, and D2cc reporting.

**HDR QA numbers.** Source strength is measured in a well chamber on receipt of each new source (Ir-192 is exchanged about every 3 months); the measured value should agree with the vendor certificate within about 3%, a difference beyond 5% must be resolved with the vendor before clinical use, and the institution treats with its own measured value. The well chamber has an ADCL calibration for that nuclide, renewed every 2 years, and a sweet-spot (position of maximum reading) check. Source positional accuracy is within 1 mm, demonstrated with an autoradiograph or a position check ruler against the dummy marker; the NRC full calibration (at each source exchange and at least quarterly) includes that 1 mm positioning requirement, timer accuracy and linearity, and source strength. Timer accuracy is within 1 s (or 1%), with the transit (end-effect) dose characterized. The step size is selectable, usually 2.5, 5, or 10 mm (newer units allow 1 mm), and the number of dwell positions per channel is finite, so a plan that asks for more positions than the channel allows is rejected. With the source in the safe, the exposure rate at 10 cm from the afterloader surface should not exceed 1 mR/h. Before the first treatment of each day the operator confirms the door interlock, the source-exposed indicator lights, the audio and video links, the area radiation monitor, the emergency stop and retract, the emergency kit, the clock and date, and the decayed source strength in the console. Emergency drills are run at least annually. The authorized user physician and the authorized medical physicist are physically present when a treatment starts; the physicist is the person who retracts the source with the emergency crank if the drive fails, and the physician is the person who removes the applicator from the patient and places it in the shielded container if the source still will not retract (TG-59 roles). The patient is surveyed after every fraction and is not released until the reading is at background.

**Medical events, current form (10 CFR 35.3045).** A medical event is a delivered total dose differing from the written directive by 20% or more, a single fraction differing by 50% or more, a dose outside the prescribed range, or an administration to the wrong patient, with the wrong radionuclide, by the wrong route, or to the wrong site (each dose criterion also requires an absolute threshold, 0.05 Sv effective, 0.5 Sv to an organ, or 0.5 Sv to skin, which brachytherapy doses always exceed). For permanent implants the 2018 rule replaces dose with source strength: a medical event is a total implanted source strength more than 20% off the written directive, or more than 20% of the implanted strength outside the treatment site as documented on the post-implant portion of the directive, which the physician completes within 60 days. Notification goes to the NRC or agreement state by telephone no later than the next calendar day, to the referring physician and the patient within 24 hours, and in writing within 15 days. The old "recordable event" category and its 10% threshold no longer exist.

**Transport labels.** Shipments of sealed sources carry a DOT category label chosen by two readings: the surface dose rate and the transport index (TI), which is the maximum dose rate at 1 m from the package in mrem/h, rounded up to one decimal. White-I is used when the surface is no more than 0.5 mrem/h and the TI is effectively zero; Yellow-II when the surface is no more than 50 mrem/h and the TI no more than 1; Yellow-III when either number is higher (surface up to 200 mrem/h in ordinary shipments, TI up to 10). A seed shipment or an HDR source container arriving with a label is checked for the TI and surveyed on receipt; the package-receipt survey, Type A versus Type B packaging, and the exclusive-use rules belong to the protection module.

**Wrong turns**

- Loading a prostate uniformly: the urethra, which runs through the center, exceeds 150%.
- Post-implant CT on the day of the implant used as the final dosimetry; edema makes the gland larger and D90 lower than the 30-day result.
- Prescribing a balloon at the surface instead of 1 cm, or including the balloon volume in PTV_eval.
- Expecting the physicist to pull the applicator in an HDR emergency; the crank is the physicist's job, the applicator is the physician's.
- Quoting a 10% "recordable event" threshold; the current rule has only medical events at 20% total and 50% per fraction.

**Traps.** A stem that gives skin-to-balloon distance in millimeters is asking whether the case is plannable (7 mm comfortable, 5 mm with a multi-lumen device, less than that usually not). A stem that gives seeds outside the gland on the post-implant CT is asking about the 20% source-strength rule, not the dose rule.

**Sources.** AAPM TG-56, TG-59, TG-64, TG-137, and TG-128 for prostate and HDR practice; NSABP B-39 and ABS guidance for the balloon and strut numbers; ICRU 38 and ICRU 89 for the GYN points; 10 CFR 35.3045, 35.633, 35.643 and 49 CFR 172 for the regulatory figures.

## Applicator Families, Loading Patterns, and Implant Classification

**Objectives:** V.2, V.3, V.1

**What the exam expects:** Sort an implant into one of four classes by where the sources sit, name the GYN applicators and what makes each one different, recognize the radium-era tandem loadings by their nicknames, apply the Manchester-era organ limits as fractions of the point A dose, and know the eye-plaque and prostate-candidacy facts that still appear as recall items. Two source-physics facts ride along: low-energy seeds are more anisotropic than Ir-192, and the Pd-103 prescription changed with the 1999 calibration standard.

**Four classes of implant.** Interstitial means the sources are inserted into the tissue itself: prostate seeds, Syed-template needles into the parametria, Ir-192 catheters through a breast or a tongue. Intracavitary means the sources sit in a natural body cavity next to the tumor without piercing tissue: tandem and ovoids in the uterus and vaginal fornices, a vaginal cylinder, a ring applicator, a breast balloon in the surgical cavity. Intraluminal (endoluminal) means a single catheter runs down a tubular organ: endobronchial, esophageal, or biliary HDR. Surface (mold or plaque) means the sources sit on the skin or on an organ surface: a Freiburg flap, a Leipzig cup, an episcleral eye plaque. The class decides the geometry of the dose: an interstitial implant is dosed from inside the volume, so a Manchester or Paris distribution rule applies; an intraluminal line is dosed radially from one axis, so the dose is prescribed at a fixed distance (usually 1 cm) from the catheter axis.

**Why end dwells are weighted up in a line.** A dwell in the middle of a long catheter is surrounded by neighbors, and their contributions add up; the first and last dwells have neighbors on one side only. With equal dwell times the isodose tapers at both ends into a cigar shape and the reference dose does not reach the ends of the target. The planner (or geometric optimization) gives the end dwells longer times, so the isodose becomes a cylinder of roughly constant radius along the treated length. Reversing the weighting, heavy in the middle, makes the taper worse.

**Manchester-era organ limits.** Before volumetric D2cc reporting, bladder and rectal doses were read at the ICRU 38 points and compared with the point A dose as a fraction: bladder at or below about 80% of point A, rectum at or below about 70–80% of point A. The limits are checks on the applicator geometry, not prescription points. A bladder point at 90% of point A means the ovoids are too close to the bladder or the packing is inadequate; the remedy is repacking or re-insertion, not re-prescribing. This bank's volumetric correlates (rectum D2cc near 65–75 Gy EQD2, bladder D2cc near 80–90 Gy EQD2) are the modern equivalents and appear in the planning lesson above.

**Largest ovoids, longest tandem.** The intracavitary rule is to use the largest ovoids and the longest tandem that the anatomy accepts. Larger ovoids move the vaginal mucosa farther from the sources, so for the same point A dose the mucosal surface dose is lower, and the pear-shaped isodose is wider so it covers more of the parametria. A longer tandem reaches the fundus and treats the whole uterine canal. Small ovoids squeezed into a wide vagina are a geometry error even when point A reads correctly.

**Applicator names.** The Fletcher-Suit (Fletcher-Suit-Delclos) applicator is the classical tandem-and-ovoid set: tandems come with 15, 30, and 45 degree curvatures to follow the uterine flexion, the ovoids (colpostats) are cylindrical with removable caps that enlarge their diameter, and the ovoids carry internal tungsten shields on the bladder and rectal sides that cut the dose to those organs by roughly 10–25% at the reference points. The ring applicator fixes the ovoid equivalent as a ring around the cervix at a set angle to the tandem; its geometry is reproducible from fraction to fraction, which is why it is popular for HDR, but the ring itself is unshielded, so organ sparing comes from dwell weighting rather than from tungsten, and the ring dwell positions nearest the tandem are usually left inactive. The Henschke applicator has hemispherical ovoids rigidly attached to the tandem with the ovoid axes parallel to the tandem, a fixed geometry that was easy to afterload. Heyman capsules (and the Simon-Heyman afterloading version) are small capsules packed into a large uterine cavity for endometrial (uterine corpus) carcinoma, where a single tandem cannot cover the whole wall; many capsules fill the cavity and the loading is counted in capsule-hours of radium or its equivalent.

**Radium-era tandem loadings.** Tandems were loaded with radium or Cs-137 tubes in three recognized patterns, written as milligrams from fundus to os. Uniform loading is the same strength in every position, for example 10-10-10 mg. Indian club loading puts the heaviest source at the fundus and lighter ones below, for example 15-10-10 mg, so that the fundal end of the pear is fuller. Dumbbell loading puts heavier sources at both ends with a lighter middle, for example 15-10-15 mg, when both the fundus and the region near the os need more dose. The nicknames describe the shape of the activity profile, not the applicator. HDR dwell optimization reproduces whichever pattern the plan needs.

**Eye plaques.** The COMS (Collaborative Ocular Melanoma Study) plaque is a gold-alloy shell, 12–20 mm in diameter, with a Silastic insert that holds I-125 (or Pd-103) seeds in a fixed pattern; the gold shields the orbit and the dose is prescribed to the tumor apex, 85 Gy over several days, as the planning lesson lists. Ru-106 plaques are beta emitters: a thin ruthenium layer sealed in silver, with a steep fall-off that limits them to thinner tumors, roughly 5–6 mm apical height or less, where the shallow range is an advantage because the dose to the opposite retina and optic nerve is small. A thick tumor needs the photon plaque; a thin one can use either.

**Prostate seed candidacy.** Pubic-arch interference means the pubic bone blocks the anterior-lateral needle paths on the transperineal template, so part of a large gland cannot be reached; it is checked on the volume study (and sometimes CT) before the implant. Glands larger than about 50–60 cm³ are the usual candidates for a few months of hormonal (androgen-deprivation) therapy first, which shrinks the gland by roughly a third and often clears the arch. A large gland also needs more seeds and more needles, so the dosimetric and surgical arguments agree.

**Anisotropy by energy.** The anisotropy function F and the anisotropy factor are farther from 1 for I-125 and Pd-103 than for Ir-192. The low-energy photons (about 21–28 keV) are heavily attenuated by the titanium end welds and by self-absorption in the seed along its axis, so the dose along the seed axis is markedly lower than on the transverse axis; typical anisotropy factors are around 0.93–0.95 for seeds against about 0.98 for Ir-192, whose 380 keV photons pass the capsule ends with little loss. In a seed implant the seeds point in all directions, which is one reason an anisotropy factor (a 1D average) was once accepted; TG-43U1 recommends the full 2D function when orientations are known.

**Pd-103 dose convention.** The monotherapy prescription for Pd-103 is 125 Gy. Before 1999 the same clinical treatment was written as 115 Gy; the number rose when NIST introduced the 1999 air-kerma-strength standard for low-energy seeds and TG-43 parameters were revised, so the same seeds delivered the same dose but the calculated value came out about 8% higher. A 115 Gy figure in an older text is the pre-1999 convention, not a lower dose. The I-125 figure (145 Gy) was likewise 160 Gy in pre-TG-43 (1995) dosimetry.

**Wrong turns**

- Calling a vaginal cylinder interstitial, or a breast balloon interstitial. Nothing is pierced; both are intracavitary.
- Weighting the middle dwells of an endobronchial line more heavily than the ends.
- Treating the 80% bladder rule as a prescription point rather than a check on the insertion.
- Attributing tungsten shielding to the ring applicator; the shields belong to the Fletcher ovoids.
- Reading "Indian club" as heavy at the os; the club head is at the fundus.
- Assigning a Ru-106 plaque to a 10 mm thick melanoma.
- Expecting Ir-192 to be more anisotropic than I-125 because it is a longer source; the energy effect dominates.

**Traps.** When a stem lists "15, 30, 45 degrees" it is describing Fletcher tandem curvatures. When it says "fixed geometry, reproducible, unshielded" it is describing the ring. When it says "capsules packed into an enlarged uterus" it is Heyman.

**Sources.** Khan and Gibbons, intracavitary applicators and radium loadings; Fletcher's textbook descriptions as summarized in standard reviews; COMS protocol and ABS eye-plaque guidance; AAPM TG-43U1 for anisotropy and the 1999 NIST standard; ABS prostate brachytherapy guidance for candidacy.

## Patient Exposure Rate, Timer QA, and Independent Plan Checks

**Objectives:** V.6, V.4, V.3

**What the exam expects:** Compute the exposure rate at a distance from a patient who contains sources, including the body's own attenuation; read a timer linearity test and extract the end effect; name the security and interlock features of an HDR suite; run an inverse permanent-implant calculation (what initial dose rate delivers a prescribed total); compute milligram-hours for a temporary implant; and state how a brachytherapy planning system is checked against TG-43 tables.

**Exposure rate from a patient with body transmission.** The point-source formula of the exposure-rate lesson gains one factor: the fraction of the radiation that gets through the patient's tissue on the way out.

\[
X = \frac{\Gamma A}{d^2} \times T
\]

- \(X\): exposure rate at the point of interest
- \(\Gamma\): exposure rate constant (R cm² per mCi per h, or per mg-Ra-eq per h if the strength is in milligrams)
- \(A\): total source strength in the patient, in the unit \(\Gamma\) expects
- \(d\): distance from the implant, in cm when \(\Gamma\) is in cm²
- \(T\): body transmission factor (typically about 0.5–0.7 for a pelvic Cs-137 or Ir-192 implant at 1 m), given in the stem

### Worked example: exposure at 1 m from an LDR GYN patient

**Given.** A tandem-and-ovoid insertion holds a total of 60 mg-Ra-eq of Cs-137. \(\Gamma_{Ra} = 8.25\) R cm² mg⁻¹ h⁻¹. Body transmission \(T = 0.60\). Distance 1.0 m.

**Substitute.** \(d = 100\) cm. Unshielded point-source rate \(= 8.25 \times 60 / 100^2 = 495 / 10000 = 0.0495\) R/h \(= 49.5\) mR/h. With transmission: \(49.5 \times 0.60 = 29.7\) mR/h.

**Check.** \(29.7 / 0.60 = 49.5\), and \(49.5 \times 10000 / 60 = 8250 = 8.25 \times 1000\), so the constant was applied in the right unit. Halving the distance to 50 cm would give \(29.7 \times 4 = 119\) mR/h.

**Result means.** A visitor at 1 m receives about 30 mR/h, not 50, because the pelvis absorbs 40% of the photons. Dividing by \(T\) (82.5 mR/h) is the sign error; forgetting \(T\) overstates the dose rate and over-restricts visitors. Because the strength is in mg-Ra-eq, the radium constant is the right one even though the nuclide is cesium.

**Timer linearity and end effect.** Dose should be proportional to dwell time. The test exposes a chamber or well for several set times and plots reading against time. A straight line proves linearity (the slope is the dose rate); the line does not pass through the origin because the source delivers dose while it travels to and from the dwell position. That intercept is the end effect, also called the transit dose, and it is expressed as the equivalent number of seconds of dwell. Two readings are enough: slope \(= (R_2 - R_1)/(t_2 - t_1)\), intercept \(= R_1 - \text{slope} \times t_1\), end effect in seconds \(= \text{intercept}/\text{slope}\). The acceptance figure for timer accuracy is about 1% or 1 s; a transit dose of a fraction of a second per dwell matters for short dwells and many positions and the planning system or the afterloader should account for it.

### Worked example: end effect from two readings

**Given.** Well-chamber readings of 41.0 units for a 20 s dwell and 121.0 units for a 60 s dwell.

**Substitute.** Slope \(= (121.0 - 41.0)/(60 - 20) = 80.0/40 = 2.00\) units per second. Intercept \(= 41.0 - 2.00 \times 20 = 41.0 - 40.0 = 1.0\) unit. End effect \(= 1.0 / 2.00 = 0.50\) s.

**Check.** \(2.00 \times 60 + 1.0 = 121.0\), the second reading. A 0.5 s end effect on a 20 s dwell is 2.5% of the dose; on a 2 s dwell it would be 25%, which is why many short dwells need the correction.

**Result means.** Each time the source travels out and back it delivers the equivalent of half a second of dwell. Reporting 1.0 s (the intercept in reading units, not converted) or 2.0 s (the slope) is the common slip.

**Security and interlocks.** An HDR afterloader is secured against unauthorized use by two independent measures, for example a removable console key plus an operator password or access code, or a key-controlled console plus a locked treatment room. The console and the room are secured whenever the unit is unattended. The treatment room door carries an interlock that retracts the source if the door opens and prevents the source from leaving the safe unless the door is closed; after an interlock interruption the unit may be restarted only from the console. When an imaging x-ray unit (C-arm, simulator, or CT) shares the room, an interlock prevents the x-ray tube and the HDR source from being exposed at the same time, so that nobody is in the room for imaging while the source is out and the area radiation monitor reading is not confused by x-ray scatter. A viewing system, an intercom, an independent area radiation monitor with its own power backup, and a visible source-on indicator at the door complete the set.

**Planning-system check against TG-43 tables.** When a brachytherapy TPS is commissioned, and whenever a source model is added, the dose rate it computes at a set of points around a single source is compared with hand values from the published TG-43 (TG-43U1) consensus tables for that source model. The usual acceptance is about 2% at individual points (tighter on the transverse axis, looser along the source axis where the anisotropy table is coarse) and about 5% for the overall agreement of a multi-source plan or for points very close to the source. A larger difference means a wrong source model, a wrong \(\Lambda\), a geometry function set to point when the table is for a line, or a unit mix-up between U and mCi, and treatment waits until it is explained.

### Worked example: single-point TPS check

**Given.** The TPS reports 11.40 cGy/h at 2 cm on the transverse axis; the hand calculation from the TG-43 table gives 11.15 cGy/h.

**Substitute.** Difference \(= 11.40 - 11.15 = 0.25\) cGy/h. Percent \(= 0.25 / 11.15 = 0.0224 = 2.2\%\).

**Check.** \(11.15 \times 1.022 = 11.40\). The per-point tolerance is about 2%, so 2.2% is outside it and the \(g(r)\) value at 2 cm is the first thing to compare.

**Inverse permanent-implant calculation.** The forward formula, \(D = \dot{D}_0 \times 1.443 \times T_{1/2}\), is inverted to find the initial dose rate that delivers a prescribed total:

\[
\dot{D}_0 = \frac{D}{1.443 \times T_{1/2} \times 24}
\]

with \(T_{1/2}\) in days, the 24 converting to hours, and \(\dot{D}_0\) in cGy/h when \(D\) is in cGy. Some texts write 1.44 for 1.443; the difference is 0.2% and either is accepted.

### Worked example: I-125 at 145 Gy

**Given.** I-125 monotherapy, 145 Gy, \(T_{1/2} = 59.4\) days.

**Substitute.** Mean life in hours \(= 1.443 \times 59.4 \times 24\). \(1.443 \times 59.4 = 85.71\) d. \(85.71 \times 24 = 2057\) h. \(\dot{D}_0 = 14500 / 2057 = 7.05\) cGy/h.

**Check.** \(7.05 \times 2057 = 14502\) cGy. Omitting 1.443 gives \(14500 / 1425.6 = 10.2\) cGy/h, which would overdose by 44% if the seeds were ordered to that rate. For Pd-103 at 125 Gy the same arithmetic gives \(1.443 \times 17.0 \times 24 = 588.7\) h and \(12500 / 588.7 = 21.2\) cGy/h, three times the I-125 rate, as the shorter half-life requires.

**Result means.** An I-125 implant prescribed to 145 Gy must start at about 7 cGy/h at the prescription isodose. That number drives the total activity ordered.

**Milligram-hours for a temporary implant.** The integrated strength of a temporary LDR implant is the total source strength multiplied by the time in place, in mg-Ra-eq-hours (mg-h). Manchester intracavitary tables were written in mg-h: a classical radium cervix insertion was about 7000–8000 mg-h in two insertions. The quantity is the ancestor of TRAK (reference air-kerma rate times time); since 1 mg-Ra-eq = 7.227 U, mg-h times 7.227 gives the TRAK in cGy cm² (U-hours), the same integrated strength in modern units.

### Worked example: mg-h

**Given.** Tandem loaded 15-10-10 mg-Ra-eq (Indian club) plus two ovoids of 20 mg-Ra-eq each, in place for 48 hours.

**Substitute.** Total strength \(= 15 + 10 + 10 + 20 + 20 = 75\) mg-Ra-eq. \(75 \times 48 = 3600\) mg-h.

**Check.** \(3600 / 75 = 48\) h. Removing the implant 6 hours early would cut it to \(75 \times 42 = 3150\) mg-h, a 12.5% shortfall. Decay of Cs-137 over two days is negligible, so no decay factor is needed here; for Ir-192 ribbons the finite-time integral of the decay lesson would apply.

**Result means.** The insertion is 3600 mg-h. If the order was 3600 mg-h and the loading changed to 60 mg-Ra-eq, the time would become 60 hours.

**Wrong turns**

- Dividing by the transmission factor, or dropping it, in the patient exposure-rate calculation.
- Reading the end effect as the intercept in dose units without dividing by the dose rate.
- Treating the door interlock as the security measure; security is the key-and-code pair, the interlock is a radiation-safety control.
- Using 5% as the per-point tolerance against TG-43 tables; per point is about 2%.
- Inverting the permanent-implant formula without 1.443, or with the half-life in days against a dose rate in cGy/h.
- Multiplying mg-Ra-eq by time in days when the tables are in hours.

**Traps.** "Patient contains" plus "transmission" means multiply by \(T\). "Readings at two dwell times" means slope and intercept. "Total dose prescribed, find the initial dose rate" means divide by the mean life in hours.

**Sources.** Khan and Gibbons, exposure around implanted patients and milligram-hours; AAPM TG-56 and TG-59 for HDR timer, transit-dose, interlock, and security practice; 10 CFR 35.610 and 35.615 for the security and interlock requirements; AAPM TG-43U1 and TG-56 for the planning-system comparison tolerances.
