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
| Au-198 | 2.7 days | permanent, historical | — |

HDR means a dose rate at the prescription point of at least 12 Gy/h. LDR is roughly 0.4–2 Gy/h. MDR sits between them. Pulsed dose rate delivers LDR-like total doses in short pulses. I-125 and Pd-103 permanent seeds are low dose rate in the tissue sense and are not HDR afterloaders.

## Radioactive Source Characteristics

**Objectives:** V.1, I.7

**What the exam expects:** Match the nuclide to the job (HDR Ir-192, LDR Cs-137, I-125 and Pd-103 seeds). Use half-life for remaining activity. Use mean life only when the question is total dose from complete decay. Autoradiography checks whether activity is uniform along a source or a ribbon.

**Core facts**

Energies to memorize, the same numbers as the table: Ir-192 about 380 keV mean, Cs-137 662 keV, I-125 about 28 keV, Pd-103 about 21 keV. Ir-192 is the HDR nuclide. Cs-137 is the historical LDR tube. I-125 and Pd-103 are the permanent seeds. Pd-103 is the softer and the shorter-lived of those two seeds.

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
