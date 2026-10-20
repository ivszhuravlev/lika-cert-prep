# Module 42. Quality assurance and standard of care

Original notes for MDCB CMD prep. Domain VII is about 9% of the exam. Objectives VII.1 through VII.9, and detectors (VI.4).

Tolerances below are the ones these items test. A stem that prints a different clinic limit wins over a memorized number.

## QA and TPS Commissioning

**Objectives:** VII.1

**What the exam expects:** The treatment planning system is commissioned before clinical use: calculated dose versus measured dose for the energies, field sizes, depths, and heterogeneities the clinic will use. Absolute dose on the machine is TG-51 in water. Annual output is tied back to that calibration at about 1%.

**TG-51, absolute dose in water**

\[
D_w^Q = M \cdot k_Q \cdot N_{D,w}
\]

- \(D_w^Q\): absorbed dose to water at the reference point in beam quality \(Q\)
- \(M\): ion-chamber reading with the corrections applied (temperature and pressure, polarity, recombination, electrometer)
- \(N_{D,w}\): absorbed-dose-to-water calibration coefficient from an accredited laboratory
- \(k_Q\): beam-quality correction factor, taking the chamber from the calibration beam (usually Co-60) to the user’s beam

Photon beam quality is \(\%dd(10)_x\): the percent depth dose at 10 cm for a 10×10 cm² field, with electron contamination removed (the subscript \(x\)) for the higher energies where the protocol uses a lead foil. Electron beam quality is \(R_{50}\), the depth of 50% dose, obtained from the ionization curve by the conversion in the protocol. TG-51 is a water-tank measurement, not a solid-water shortcut, unless a later addendum the stem cites allows one.

### Worked example

**Given.** For a commissioned beam, the planning system calculates 100.0 cGy at the reference point. A water-tank measurement, already corrected, reads 98.5 cGy for the same MU.

**Arithmetic.**

\[
\frac{98.5 - 100.0}{100.0} = -0.015 = -1.5\%
\]

**Check.** \(100.0 - 98.5 = 1.5\), and \(1.5/100 = 1.5\%\).

**Result means.** Calculation and measurement differ by 1.5%. That is outside a 1% annual-style agreement. The beam data or the model is not released for clinical use until the difference is understood. A 1.5% gap is not repaired by changing a patient’s MU on the first day.

**Wrong turns**

- Commissioning in a hand calculation (PDD only) and calling the TPS commissioned.
- Using \(\%dd(10)\) with electron contamination still in the curve when the protocol asks for \(\%dd(10)_x\).
- Using \(R_{50}\) to pick a photon \(k_Q\), or \(\%dd(10)_x\) to pick an electron factor.
- Quoting TG-51 as a monthly constancy check. Monthly output is a constancy measurement (about 2%). The annual absolute calibration is TG-51 (about 1%).

**Traps.** Name the protocol (TG-51), the medium (water), and the beam-quality index (photons versus electrons) in the same sentence.

**Sources.** AAPM TG-51 (and TG-51 addendum) for \(N_{D,w}\), \(k_Q\), \(\%dd(10)_x\), and \(R_{50}\). AAPM TG-53 for TPS commissioning. TG-142 for the annual tie to TG-51.

## Clinical Data: Plan Checks, Chart Reviews, Image Reviews

**Objectives:** VII.2

**What the exam expects:** A plan check before the first treatment confirms prescription, volumes, beam energy, MU, accessories, and the independent calculation. A weekly chart check confirms that what has been delivered still matches the prescription and that cumulative dose is on track. Image review confirms the patient is in the planned position; a shift is applied in the direction the image shows, and the size of the shift is compared with the action level.

### Worked example

**Given.** The approved plan has 180 MU for a field. The record-and-verify system is loaded with 200 MU for that field. Weekly chart check, or the initial physics check, catches it before the beam goes on.

**Arithmetic.**

\[
\frac{200 - 180}{180} = \frac{20}{180} = 0.111 = 11.1\%
\]

**Check.** \(180 \times 1.111 = 200\). \(180 \times 0.10 = 18\), plus \(180 \times 0.011 = 2\), equals 20.

**Result means.** If the plan is correct, the loaded field would deliver about 11% more monitor units than approved. The fraction is not treated until the plan and the record-and-verify system agree. Image review is a separate question: a 5 mm shift recommendation is not an MU error, and an MU error is not fixed by shifting the couch.

**Wrong turns**

- Dividing the 20 MU difference by 200 and calling it 10%. Use the approved plan as the baseline unless the stem says the plan was the wrong document.
- Approving a chart because last week’s fractions were correct while this week’s MU edit is unreviewed.
- Signing an image review that shows the wrong site because the MU checked out.

**Traps.** Three reviews, three questions: does the plan match the prescription, does the chart match the plan, does the image match the setup?

**Structure names (TG-263).** A chart check can add a prior course only if the organ has one name. TG-263 writes targets as the structure, an underscore, and the dose in cGy with no space and no decimal: PTV_7000 is the planning target prescribed to 7000 cGy. Organs use one camel-case name and no space: SpinalCord, Lungs. Lungs is both lungs together. A unilateral lung is a different name. Three courses that call the cord “cord”, “Spinal Cord”, and “SpCord” will hide a prior dose. The name does not change the dose. It makes the dose findable.

**Sources.** AAPM TG-275 (plan and chart review) and the weekly chart-check cadence from TG-40 that items still test. TG-142 does not replace the chart check. AAPM TG-263 for structure names.

## Record and Verify Systems and EMR

**Objectives:** VII.4

**What the exam expects:** The record-and-verify system (and the electronic medical record it feeds) must match the approved plan: MU, energy, gantry, collimator, couch, MLC, and accessories such as the wedge. A mismatch is a hold, not a note for later. The EMR is the chart of record; a local spreadsheet is not.

### Worked example

**Given.** Breast tangents were planned with a couch kick of 5.7° so the superior border matches a half-beam supraclavicular field. The superior–inferior length is 20 cm at SAD 100 cm. The record-and-verify couch is 0.0°. The collimator does not create that superior match. The posterior border is set by the gantry or by a half-beam jaw.

**Arithmetic.** The mismatch is \(5.7^\circ - 0^\circ = 5.7^\circ\). No tolerance of “a couple of degrees” replaces the approved couch angle.

**Check.** Half the superior–inferior length is \(20/2 = 10\) cm. At SAD 100 cm the ratio is \(10/100 = 0.10\), and \(\arctan(0.10) = 5.71^\circ\), reported as 5.7°. \(\tan(5.7^\circ) \approx 0.10\). That triangle is the couch kick. A couch left at 0° leaves the superior border diverging. Rotating the collimator does not remove that superior divergence.

**Result means.** Treat the mismatch as a setup error. Loading a couch of 0° puts the superior border back on a diverging edge. The posterior lung border is a different border: gantry angle, so the posterior edges are coplanar, or a half-beam jaw. It is not this 5.7° kick, and it is not a collimator rotation. The dosimetrist does not “fix it at the machine” by editing the plan without a new check.

**Wrong turns**

- Assuming the record-and-verify database cannot drift from the exported plan.
- Overriding an interlock to match an accessory the plan does not have (wedge in the tray, factor not in the MU: module 34).
- Documenting the change only in a hallway conversation. The EMR has to hold the approved plan.
- Calling the 5.7° a collimator angle for the superior match, or assigning it to the gantry as the posterior lung border. The couch uses the superior–inferior length. The posterior border is the gantry or a half-beam.

**Traps.** Read every parameter the stem lists, not only MU. Energy 10 MV loaded against 6 MV planned is the same class of error. A couch of 0° against a 5.7° kick is the same class of error.

**Sources.** Clinical record-and-verify practice under TG-142 (accessories and interlocks) and TG-275 (chart contents).

## Treatment Beam QA Measurement and Analysis (eg IMRT, electron cutout factors)

**Objectives:** VII.5

**What the exam expects:** IMRT or VMAT patient-specific QA uses a gamma comparison and an ion-chamber point dose. The stem sets the gamma criteria (often 3% and 3 mm, or 3% and 2 mm) and the pass-rate threshold (often 95%). Electron cutout factors are measured, especially for small cutouts, because the calculation misses the loss of lateral scatter.

Gamma ≤ 1 means the point is inside the dose-difference or the distance-to-agreement ellipse. A low-dose threshold (often 10% of maximum) keeps noise in the penumbra from dominating the score. TG-218 is the AAPM report on this analysis. Quote the stem’s numbers, not a memorized pass rate, when they differ.

**Cutout factor**

\[
\text{cutout factor} = \frac{\text{dose with the cutout}}{\text{dose with the reference open cone}}
\]

at the same MU, same energy, same cone, at the calibration depth.

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times \text{cutout factor}}
\]

### Worked example: gamma and chamber

**Given.** The clinic’s rule is gamma 3%/2 mm, global normalization, pass if at least 95% of points in the threshold region have gamma ≤ 1, and ion chamber within 3% in a low-gradient region. This plan scores 96.4% gamma and the chamber reads −4.2%.

**Arithmetic.** \(96.4 \ge 95\), so gamma meets the rule. \(|-4.2| > 3\), so the chamber fails. \(4.2 - 3.0 = 1.2\) percentage points over the chamber tolerance.

**Check.** The signs: a chamber reading of −4.2% means measured dose is 4.2% below calculated (confirm the stem’s sign convention; here “−4.2%” is measured minus calculated, relative to calculated).

**Result means.** The plan is not released. Gamma can pass while the absolute dose fails. Both are required. A 96.4% gamma score does not average away a 4.2% chamber miss.

### Worked example: electron cutout

**Given.** Calibration: 1.0 cGy/MU at dmax for the open reference cone, at the electron calibration geometry the stem states (same sentence you would use for photons: here the open cone is the reference, 1.0 cGy/MU at dmax). Measured cutout factor = 0.880. Prescription 200 cGy to dmax through that cutout. No other factor.

**Substitute.** \(\mathrm{MU} = 200 / (1.0 \times 0.880) = 227.3\) MU.

**Check.** \(227.3 \times 0.880 = 200.0\) ( \(200/0.880 = 227.27\), and \(227.27 \times 0.880 = 200\) ).

**If the factor is left at 1.000.** MU = 200, delivered dose \(= 200 \times 0.880 = 176\) cGy. The patient is underdosed. \(176/200 = 0.880\), the cutout factor itself. Same pattern as a wedge factor omitted while the modifier is in the beam.

**Result means.** Small electron cutouts are measured. A calculated factor of 1.00 for a small cutout is not close enough to defend.

**Wrong turns**

- Releasing on gamma alone.
- Using a photon \(S_c\) table as the electron cutout factor.
- Khan versus Bentel energy rules (module 45) substituted for a measured output factor. Those rules pick an energy. The cutout factor still has to be measured at that energy.
- PDD mixed into an electron MU that the stem already states at dmax.

**Traps.** Two IMRT numbers, two decisions. Write “gamma: pass/fail” and “chamber: pass/fail” on separate lines.

**Sources.** AAPM TG-218 for IMRT QA analysis. TG-51 and TG-142 for output. Electron cutout measurements as required in clinical medical-physics practice when lateral equilibrium fails (TG-106 beam-data spirit: measure what you cannot calculate reliably).

## AAMD Scope of Practice

**Objectives:** VII.6

**What the exam expects:** The medical dosimetrist does not prescribe. The radiation oncologist prescribes dose, fractionation, and the medical intent. The dosimetrist designs the plan inside that prescription, calculates, documents, and participates in checks. The medical physicist checks the plan and the machine. Changing 2 Gy × 25 into a different fractionation is a prescription change even when the physical total looks similar.

**What the practice includes.** The work is the plan and the record of the plan, inside a prescription someone else wrote.

- Treatment planning: beam arrangement, apertures, weights, and the dose distribution that meets the written prescription.
- Monitor-unit calculations, including a calculation a second person can check.
- Brachytherapy planning: source placement, dwell times, and the dose to the target and to organs, still under the written directive.
- Quality-assurance participation: plan checks, chart checks, and measurements the physicist assigns. Participation is not the signature on the machine calibration.
- Simulation: immobilization, scan limits, setup marks, and the shifts treatment will reproduce.
- Documentation: prescription, structures, beams, dose, and the calculation record in the chart.
- Education: teaching students and staff, and the dosimetrist’s own continuing education.

**Signatures.** The physician signs the prescription and approves the plan as the medical order. The medical physicist signs the plan check and the machine calibration. A dosimetrist’s calculation does not replace either signature.

**CMD.** Certified Medical Dosimetrist (CMD) is the credential from the Medical Dosimetrist Certification Board. Keeping it requires continuing education on the cycle the board sets. The credential shows the person met the exam standard. It does not create an independent prescriber, and it does not move the physician’s or the physicist’s signature onto the dosimetrist.

**Ethical limit.** Do the work you are competent to do, document it honestly, and stop at the edge of the prescription. Do not change a dose so the DVH looks cleaner, do not hide a mismatch, and do not sign a document that belongs to the physician or the physicist. When the request crosses that line, hand it back to the person whose license covers it.

### Worked example

**Given.** A physician has prescribed 2.0 Gy × 25 fractions. A colleague suggests the dosimetrist “just change it” to 1.8 Gy × 28 fractions so the total looks the same.

**Arithmetic.** \(2.0 \times 25 = 50.0\) Gy. \(1.8 \times 28 = 50.4\) Gy. The physical totals differ by 0.4 Gy. Biologically they also differ because the fraction size changed (EQD2, module 38). The first course is already 2 Gy per fraction, so its EQD2 is 50 Gy. The second course, with \(\alpha/\beta = 3\) Gy, is

\[
50.4 \times \frac{1.8+3}{2+3} = 50.4 \times \frac{4.8}{5} = 50.4 \times 0.96 = 48.4 \text{ Gy EQD2}
\]

**Check.** \(4.8/5 = 0.96\). \(50.4 \times 0.96 = 48.384\).

**Result means.** The totals are not interchangeable, and the dosimetrist does not make them interchangeable. The physician writes the new prescription. The dosimetrist then plans to that prescription. Scope is the point of the item; the arithmetic shows why “almost 50 Gy” is not a reason to edit the order.

**Wrong turns**

- The dosimetrist selecting beam energy, total dose, or fractionation as a medical decision.
- The dosimetrist approving the plan in place of the physicist or the physician.
- Treating a verbal hallway change as a prescription. The prescription is in the chart.

**Traps.** Helpful calculation is in scope. Choosing the dose is not.

**Sources.** AAMD Scope of Practice and Practice Standards, including the ethical limit on independent prescription. MDCB certification and continuing education for the CMD credential. The prescription is the physician’s under state medical practice and under the clinic’s standard of care. The physicist’s signature covers the plan check and the calibration.

## Measurement Equipment (Diodes, ion chambers, TLD, Survey Meters)

**Objectives:** VII.3, VI.4

**What the exam expects:** Pick the instrument for the job. An ion chamber, with a calibration coefficient and corrections, is the absolute-dose instrument (TG-51). A diode gives an immediate in-vivo or relative reading and is energy and direction dependent. A TLD integrates and is read later (in vivo or a badge). A survey meter (ion chamber or Geiger, depending on the instrument) measures exposure rate for HDR surveys and area checks; it does not replace TG-51. OSL is the usual personnel badge and can be reread.

**Temperature-pressure correction** (ion chamber, vented to air), reference 22°C and 760 mmHg:

\[
C_{TP} = \left(\frac{273.2 + T}{273.2 + 22.0}\right) \times \left(\frac{760}{P}\right)
\]

- \(T\): air temperature in the room (°C)
- \(P\): pressure (mmHg)
- \(C_{TP}\): multiplies the reading. A warmer room or a lower pressure means less air in the chamber, a lower raw reading, and a correction above 1

### Worked example

**Given.** \(T = 24.0^\circ\)C, \(P = 750\) mmHg. A constancy reading that ignored \(C_{TP}\) was called 1.000 cGy/MU.

**Substitute.**

\[
C_{TP} = \left(\frac{273.2+24.0}{273.2+22.0}\right) \times \left(\frac{760}{750}\right) = \left(\frac{297.2}{295.2}\right) \times \left(\frac{760}{750}\right)
\]

**Arithmetic.** \(297.2/295.2 = 1.0068\). \(760/750 = 1.01333\). \(1.0068 \times 1.01333 = 1.020\).

**Check.** \(295.2 \times 1.0068 = 297.2\). \(1.0068 \times 1.01 = 1.0169\), and \(1.0068 \times 0.00333 \approx 0.0034\), sum 1.0203. Corrected output \(= 1.000 \times 1.020 = 1.020\) cGy/MU.

**Result means.** The uncorrected 1.000 cGy/MU was low. Temperature and pressure account for a 2.0% rise. That is large enough to matter next to a 2% monthly tolerance and a 3% daily tolerance. A diode used for the same constancy has its own factors; it does not use this \(C_{TP}\) unless the stem says the diode system was set up that way. A survey meter answers “is the HDR source retracted?” and does not produce \(N_{D,w}\).

**Wrong turns**

- Inverting \(C_{TP}\) (using 22°C over the room temperature), which yields about 0.980 and moves the dose the wrong way.
- Using a Geiger survey meter for TG-51.
- Using a TLD result the same afternoon. TLDs are read after processing.
- Forgetting polarity and recombination exist. This example isolates temperature and pressure; TG-51 still wants the rest of \(M\).

**Traps.** Match the question’s verb. “Absolute dose in water” is the ion chamber. “Right now, on the patient” is often the diode. “Badge” is TLD or OSL. “Is the source in the patient?” is the survey meter.

**Sources.** AAPM TG-51 for the chamber correction and the 22°C, 760 mmHg (101.33 kPa) reference. TG-142 for the instruments used in machine QA.

## Measurement Equipment Quiz

**Skills this quiz checks**

- Assign ion chamber, diode, TLD, OSL, and survey meter to absolute dose, in-vivo, badge, and HDR survey.
- Compute \(C_{TP}\) and apply it in the correct direction (hot room or low pressure raises the correction).
- Keep a survey-meter reading out of a TG-51 dose calculation.
- Name \(N_{D,w}\) and \(k_Q\) as the absolute-dose factors, with \(\%dd(10)_x\) or \(R_{50}\) as the quality index.

## Incident Reporting for Patient Safety (Quality Improvement, ROILS, Root Cause Analysis, Process Improvement)

**Objectives:** VII.7

**What the exam expects:** RO-ILS (Radiation Oncology Incident Learning System, ASTRO and AAPM) is the voluntary national incident-learning system. It is not a regulator and it is not a punishment log. Near misses are reported. Root-cause analysis asks how the process let the error through. Process improvement changes that step (a forcing function, a checklist, a second calculation) rather than stopping at “be more careful.” TG-100 scores that process with failure-mode and effects analysis. A medical event under 10 CFR 35.3045 is a required report, separate from RO-ILS.

The public lesson title spells the acronym ROILS. The system’s name is RO-ILS.

### Worked example

**Given.** A wedge with factor 0.60 was in the beam. The MU calculation omitted the factor. Prescribed dose 200 cGy at a point where every other factor is 1 and the open output is 1.0 cGy/MU (calibration: 1.0 cGy/MU at dmax, 10×10, SAD 100). Delivered dose was \(200 \times 0.60 = 120\) cGy.

**Arithmetic.** Delivered/prescribed \(= 0.60\). Shortfall \(= 80\) cGy, which is 40% of 200 cGy. The event is the underdose case from module 34.

**Check.** \(200 \times 0.6 = 120\). \(200 - 120 = 80\).

**Result means.** This is an incident (the wrong dose was delivered) and it belongs in the clinic’s reporting system. A voluntary RO-ILS submission is appropriate; RO-ILS does not replace the clinic’s own review or any state-required report. A useful root cause is a process hole: the second check did not compare the accessory in the room with the factor in the MU. “The planner was rushed” can be true and still not be the whole cause. A process change is a required wedge check that the calculation and the console both display before the beam enables.

**Wrong turns**

- Calling RO-ILS mandatory, or calling it an NRC inspection.
- Ending the analysis at a single person with no change to the checklist.
- Hiding a near miss because the patient was not harmed. Near misses are the point of incident learning.
- Fixing the next MU and skipping the report.

**Traps.** Separate three layers: care for the patient and the physician’s dose decision, the clinic’s incident review, and a voluntary RO-ILS submission.

**Sources.** ASTRO/AAPM RO-ILS program description (voluntary incident learning). Standard root-cause and process-improvement practice in the clinic’s quality program.

### Process improvement (TG-100 and FMEA)

TG-100 applies failure-mode and effects analysis to the radiotherapy process. Map the steps from simulation through planning, the plan check, record-and-verify, and treatment. For each step, list how it can fail. Score severity, occurrence, and detectability. Detectability is scored so a failure nobody would notice gets a high number. The risk priority number is the product of the three scores. Work on the high products first: a forcing function, a second check, or a checklist that makes the miss visible. Adding the same output test to every high score is not the method. A near miss that is severe and hard to detect is a reason to change the process, which is the same idea as the RO-ILS example above.

### Medical event (10 CFR 35.3045)

A medical event is a regulatory miss, not a voluntary learning report. For these items, 10 CFR 35.3045 is met when the delivered dose differs from the prescription by about 20% or more of the total dose, or by about 50% or more of a single fraction, or the dose went to the wrong site or the wrong patient. The regulation also requires the absolute dose to clear a threshold, on the order of 0.05 Sv effective dose or 0.5 Sv to an organ, so a trivial absolute error is not automatically an event. On an external-beam course the percentage lines are the ones that decide.

The report is a telephone call to the regulator within about 24 hours of discovery (by the next calendar day) and a written report within about 15 days. The referring physician and the patient are notified as well. A RO-ILS submission does not replace that report, and the regulatory report does not replace the clinic’s root-cause review.

## Factors and Limitations of Deliverable Plans

**Objectives:** VII.8

**What the exam expects:** A plan that meets the DVH can still be undeliverable. Limits that show up on items: MLC leaf travel and carriage position, very small segments or very low MU per segment, collision of gantry, couch, or imaging arms with the patient, modulation that the leaf speed cannot follow, and VMAT gantry speed versus dose rate.

### Worked example

**Given.** One VMAT arc is 360° and 900 MU. The machine’s maximum gantry speed is 6.0°/s. The maximum dose rate is 600 MU/min.

**Arithmetic.** At 6.0°/s a 360° arc takes \(360/6 = 60\) s \(= 1.00\) min. In that minute the machine at 600 MU/min delivers at most 600 MU. The plan asks for 900 MU, which needs \(900/600 = 1.50\) min \(= 90\) s. The gantry speed that fits is \(360/90 = 4.0\)°/s.

**Check.** \(6 \times 60 = 360\). \(600\) MU in 60 s is 10 MU/s, and \(10 \times 90 = 900\) MU. \(4.0 \times 90 = 360\).

**Result means.** The arc does not fit at maximum gantry speed. It can still be delivered if the gantry slows to 4.0°/s and the dose rate stays at 600 MU/min, and only if leaf travel over those 90 s is also legal. If leaf speed, carriage travel, or a collision zone forbids that motion, the plan is recalculated (fewer MU, a second arc, or less modulation). A DVH that looks acceptable does not answer this.

**Wrong turns**

- Approving 900 MU because 600 MU/min times 1.5 minutes equals 900, without checking that the gantry is allowed to take 1.5 minutes.
- Ignoring a collision because the isodose looks fine.
- Treating a 2 MU segment as harmless. Very small segments are where tongue-and-groove and detector noise dominate the QA.

**Traps.** Deliverability is a machine question. Dose-grid uncertainty (module 39) is a calculation question. A plan can fail either one.

**Sources.** MLC and VMAT delivery limits as commissioned under TG-142. The numeric limits (6°/s, 600 MU/min) are the stem’s machine data in any real item; this example states them.

## QA Requirements: Sim and Treatment Equipment

**Objectives:** VII.9, VII.1

**What the exam expects:** TG-142 cadence and the tolerances named in this course.

- Daily: door interlock functional, output constancy about 3%.
- Monthly: output constancy about 2%.
- Annual: TG-51 absolute output about 1%.
- Optical distance indicator (ODI): commonly 2 mm.
- Weekly chart checks (the chart lesson above).

Mechanical and beam checks in the same report, beyond output, the ODI, and the door:

- Lasers (daily): 2 mm, 1.5 mm for IMRT, and 1 mm for SRS. TG-142 puts SBRT on that same 1 mm laser line.
- Light-field and radiation-field coincidence: 2 mm.
- Jaw position (symmetric): 2 mm.
- Gantry angle and collimator angle indicators: 1°.
- MLC: a picket-fence test. A leaf that is out shows as a jog in the fence line. The fence is the leaf-position check. It does not replace patient-specific IMRT QA.
- Flatness and symmetry: 1% (monthly profile constancy, and the annual change from baseline).
- Radiation isocenter, the annual coincidence of the radiation and mechanical isocenters: 2 mm, and 1 mm for SRS.
- Imaging-to-treatment isocenter: at or under 2 mm, and at or under 1 mm for SRS/SBRT.
- Winston–Lutz: at or under 1 mm. A small ball at isocenter is imaged through a small field at several angles. The offset of the ball from the field center is the miss.
- Wedge-factor constancy, the annual transmission check: 2%.
- Electron energy, monthly: 2 mm or 2% on the depth index (often \(R_{50}\)) against baseline.

A daily output of 2.8% can pass while a 1.8 mm laser on an IMRT unit fails (tolerance 1.5 mm). Name the test and the machine class (non-IMRT, IMRT, SRS/SBRT) before you pick the number. A failed interlock stops the day even when output is perfect.

**CT simulation (TG-66).** The simulator has its own constancy tests. Water is held near 0 HU (constancy on the order of 5 HU, not tens). A drift of tens of HU changes the CT-to-density table and therefore the calculated dose. Air stays near −1000 HU. Lasers have to meet the imaging plane, commonly within about 2 mm. If they do not, every tattoo and every shift written from that scan is biased. Couch travel and indexing are checked so a shift marked on the scan is the shift treatment will use. An index that is off by several millimeters is a failed couch check. Simulation still also confirms field size and the optical distance before a patient is marked.

### Worked example

**Given.** Morning output reads 1.028 cGy/MU against a baseline of 1.000 cGy/MU. The same morning the ODI reads 98.5 cm when the mechanical distance is 100.0 cm.

**Arithmetic.** Output difference \(= (1.028 - 1.000)/1.000 = 0.028 = 2.8\%\). ODI error \(= 100.0 - 98.5 = 1.5\) cm \(= 15\) mm.

**Check.** \(1.028 - 1 = 0.028\). \(15\) mm is \(15/2 = 7.5\) times the 2 mm tolerance.

**Result means.** 2.8% is inside the daily output window of about 3% and outside the monthly window of about 2%. If this is the daily check, output constancy passes and is watched. If this is the monthly check, output fails. The ODI fails either way: 15 mm against 2 mm. Do not treat on a 15 mm optical-distance error. The door interlock is a separate daily check; a passed output does not excuse a taped-open door.

**Wrong turns**

- Applying the 3% daily window to the annual TG-51 comparison, where the expectation is about 1%.
- Calling a 15 mm ODI error “within 2 cm” and treating. The tolerance is 2 mm.
- Skipping the interlock because the output was 2.8%.
- Using the 3% daily output window as the tolerance for lasers, jaws, flatness, or the wedge factor.
- Using the non-IMRT laser tolerance (2 mm) on an IMRT unit (1.5 mm) or an SRS unit (1 mm).

**Traps.** Say which check it is (daily, monthly, annual) before you pick 3%, 2%, or 1%. Say which machine class it is before you pick 2 mm, 1.5 mm, or 1 mm.

**Sources.** AAPM TG-142 for linear-accelerator QA tolerances (daily interlock and output constancy, monthly output, annual absolute dose, and the mechanical, MLC, imaging, and wedge checks above). ODI tolerance of 2 mm is the common mechanical tolerance these items use. Weekly chart review as in TG-40 / TG-275. AAPM TG-66 for CT-simulator HU constancy, lasers, and couch. Winston–Lutz at or under 1 mm for the SRS isocenter check.

## QA and Standard of Care Quiz

**Skills this quiz checks**

- TG-51: water, \(N_{D,w}\), \(k_Q\), \(\%dd(10)_x\) for photons, \(R_{50}\) for electrons.
- TG-142: daily interlock, daily output about 3%, monthly output about 2%, annual TG-51 about 1%, ODI about 2 mm, plus lasers 2 mm (1.5 mm IMRT, 1 mm SRS), light/radiation coincidence 2 mm, jaw 2 mm, gantry and collimator angle 1°, picket fence, flatness and symmetry 1%, radiation isocenter 2 mm (1 mm SRS), imaging-to-treatment isocenter at or under 2 mm (at or under 1 mm for SRS/SBRT), Winston–Lutz at or under 1 mm, wedge factor 2%, electron energy 2 mm or 2%. TG-66: HU constancy, lasers, and couch. Plus a weekly chart check.
- IMRT QA: gamma and ion chamber are both required; one can pass while the other fails.
- Electron cutout factor measured for small fields, and placed in the MU denominator.
- AAMD scope: planning, monitor units, brachytherapy planning, QA participation, simulation, documentation, and education. The dosimetrist does not prescribe. The physician and the physicist sign. CMD is kept with continuing education. The ethical limit is the prescription.
- RO-ILS is voluntary incident learning; root cause is the process. TG-100 ranks failures by severity × occurrence × detectability. A medical event (about 20% of the total dose, about 50% of a fraction, wrong site, or wrong patient) is a telephone report within about 24 hours and a written report within about 15 days.
- Deliverability: MLC travel, small segments, collision, modulation, gantry speed versus dose rate.
- Record-and-verify parameters match the plan, including accessories, SSD, shift sign, and angles. The breast 5.7° example is a couch kick from a 20 cm superior–inferior length, not a collimator angle.

## Isocenter Tests: Star Shot, Spoke Shot, and Winston–Lutz

**Objectives:** VII.9

**What the exam expects:** Name the film test for each rotation axis, read its result as a radius, and keep it apart from the Winston–Lutz test. The tolerance is the TG-142 radiation-isocenter line: 2 mm for non-IMRT and IMRT machines, 1 mm for SRS and SBRT. Both numbers already appear in the QA cadence lesson; this lesson names the tests that produce them.

**Star shot.** A film (or the EPID) is exposed through a narrow slit, a few millimetres wide and the length of the field, several times while one axis is rotated between exposures: for example at 0°, 60°, and 120°, or every 30°. Each exposure draws a line through the isocenter. If the axis were perfect, every line would pass through one point. In practice they bound a small region, and the result is the radius of the smallest circle that touches all the lines. Which axis is tested depends on what is rotated and where the film is placed.

- Collimator star: the film lies flat on the couch at isocenter height, perpendicular to the beam, and the collimator is rotated between exposures. The lines cross at the collimator rotation axis.
- Couch star: the film again lies flat at isocenter, the collimator and gantry stay fixed, and the couch is rotated between exposures. The lines cross at the couch rotation axis.
- Gantry star, often called the spoke shot: the film is held vertically in the plane of gantry rotation (perpendicular to the gantry axis), with the slit set along the gantry axis, and the gantry is rotated between exposures. The lines cross at the gantry rotation axis. The pattern looks like wheel spokes, which gives the name.

The three circles together describe the radiation isocenter, the volume within which the three axes meet. A couch that is sagging under load shows up as a couch star that does not close, and a gantry whose axis walks as it rotates shows up as a large spoke-shot radius. The star shot measures the beam, so it is a radiation-isocenter test; a mechanical pointer and a dial indicator measure the mechanical isocenter, and the TG-142 annual item is the coincidence of the two.

**Winston–Lutz.** A small radiopaque ball is placed at the mechanical isocenter on the lasers or on the couch pointer and imaged through a small field (a cone or a small MLC field) at a set of gantry, collimator, and couch angles. For each image the offset between the ball's shadow and the field center is measured. The maximum offset is the result, and for SRS it must be at or under 1 mm. Winston–Lutz tests the whole chain, lasers to ball to beam, at the angles that will be used, and it is done before SRS sessions as well as annually. The star shot isolates one axis at a time; Winston–Lutz asks whether the three axes and the setup system agree where the beam will go.

### Worked example

**Given.** On an SRS-capable linac, the collimator star gives a radius of 0.4 mm, the couch star 0.7 mm, and the spoke shot 1.2 mm. The machine also treats conventional patients.

**Arithmetic.** The SRS/SBRT tolerance is 1 mm. 0.4 and 0.7 are inside it. 1.2 mm is 0.2 mm over. For the non-SRS class the tolerance is 2 mm, and all three are inside it.

**Check.** \(1.2 - 1.0 = 0.2\) mm over the SRS line. \(2.0 - 1.2 = 0.8\) mm under the conventional line.

**Result means.** Conventional treatments may continue. The SRS program is on hold until the gantry axis is adjusted and the spoke shot repeats under 1 mm. A passing Winston–Lutz from last month does not clear the gantry, because the Winston–Lutz result is a different measurement and the machine has moved since.

**Wrong turns**

- Reading the star-shot radius as a diameter, or reporting the diameter when the tolerance is written as a radius. State which one the stem uses; this bank reports the radius.
- Testing the couch with a film held vertically, or the gantry with a film lying flat. The film must be perpendicular to the axis being tested.
- Calling the picket fence an isocenter test. The picket fence is a leaf-position test.
- Using the Winston–Lutz result to replace the collimator star. Winston–Lutz is a combined test, not an axis-by-axis test.

**Traps.** Rotate one axis, place the film perpendicular to that axis, draw lines, fit a circle, report a radius. Then compare with 1 mm (SRS) or 2 mm (otherwise).

**Sources.** AAPM TG-142 (radiation isocenter ±2 mm, ±1 mm SRS/SBRT; coincidence of radiation and mechanical isocenter). Star-shot and Winston–Lutz methods as described in standard linac acceptance and SRS QA practice (Winston and Lutz, 1988).

## Calibration Intervals, Secondary MU Checks, and the TG-40 to TG-142 Transition

**Objectives:** VII.1, VII.5, VII.9

**What the exam expects:** The intervals and tolerances that surround the TG-142 table rather than being in it: how often the chamber and the survey meter go back for calibration, how far an independent monitor-unit calculation may differ from the planning system, how the dynamic wedge is checked, which document commissions the planning system, and which numbers changed between TG-40 and TG-142.

**Instrument calibration intervals.** The reference ionization chamber and electrometer used for TG-51 carry an absorbed-dose-to-water coefficient from an Accredited Dosimetry Calibration Laboratory (ADCL). The AAPM recommendation this bank uses is recalibration every two years, and after any repair. A well-type chamber for brachytherapy source strength follows the same two-year ADCL cycle. Survey meters (ion-chamber and Geiger–Müller instruments used for area and patient surveys) are calibrated annually and after repair, as a licence condition under 10 CFR 20.1501. A field instrument such as a daily-output device or a diode array is cross-calibrated against the reference chamber locally; it does not go to the ADCL.

**Independent MU verification (TG-114).** Before the first fraction a second calculation, by a different program or by hand, checks the planning-system monitor units. Agreement is judged against an action level that depends on the geometry. For a simple homogeneous point in a conventional field the bank uses 3 percent. Where heterogeneity, small fields, off-axis points, or IMRT make the two algorithms legitimately differ, the action level widens to about 5 percent. A discrepancy past the action level is investigated before treatment; it is not averaged, and it is not "fixed" by changing the delivered MU to the second program's value. The second check catches a wrong input (energy, SSD, depth, wedge factor, prescription point) and a beam-model error at the point; it does not detect an output drift, a leaf-position error, or patient motion, which belong to machine QA, patient-specific QA, and imaging.

**Dynamic wedge.** An enhanced dynamic or virtual wedge is a moving jaw, so its wedge factor and its angle depend on software and jaw motion rather than on a piece of steel. TG-142 lists the dynamic wedge among the IMRT-class monthly checks: wedge-factor constancy at 2 percent, with the full wedge-angle verification (the 60° setting over the full field, plus a spot check of another angle and field size) annually. The physical wedge is different hardware with different checks: placement accuracy at 2 mm monthly and the transmission factor at 2 percent annually, as the QA cadence lesson lists. An omitted wedge factor in an MU calculation is a plan-check item, not a wedge QA item.

**Planning-system commissioning: TG-53 and MPPG 5.a.** AAPM TG-53 (1998) was the comprehensive quality-assurance document for treatment-planning systems, covering acceptance, commissioning, periodic QA, and the whole planning process. AAPM Medical Physics Practice Guideline 5.a (2015, with a later revision) is the current prescription for commissioning and QA of the dose-calculation side of a TPS for photons and electrons: which test geometries to measure, and how close calculation must come. Its teaching tolerances are about 2 percent in the high-dose, low-gradient region on the central axis, a distance criterion of about 2 mm in the penumbra, and 3 to 5 percent in low-dose regions outside the field. When an item asks which document a physicist follows to commission the dose calculation today, the answer is MPPG 5.a; TG-53 is the broader legacy process document. TG-106 covers the beam-data measurement that feeds the model, and TG-119 is the IMRT commissioning test suite.

**IMRT patient-specific QA reminder.** TG-218 criteria as used in this bank: gamma at 3 percent and 2 mm with a 10 percent low-dose threshold, tolerance 95 percent of points, action limit 90 percent, plus an ion-chamber point dose. The IMRT QA lesson above has the worked example. Patient-specific QA is done before the first fraction and does not detect a wrong contour or a wrong margin.

**TG-40 (1994) versus TG-142 (2009).** TG-40 was the first comprehensive radiotherapy QA report: linac, simulator, planning system, brachytherapy, and the chart-check program in one document, with one set of tolerances for every linac. TG-142 replaced its linac section and kept the daily, monthly, and annual structure. What changed, in the figures items still test:

| Check | TG-40 | TG-142 |
| --- | --- | --- |
| Annual absolute output | 2% | 1% |
| Flatness and symmetry | 3% flatness, 2% symmetry (absolute) | 1% change from baseline |
| Lasers | 2 mm for all | 2 mm non-IMRT, 1.5 mm IMRT, 1 mm SRS/SBRT |
| Isocenter | 2 mm diameter (mechanical) | ±2 mm radiation isocenter, ±1 mm SRS/SBRT |
| Machine classes | one class | non-IMRT, IMRT, SRS/SBRT |
| Imaging and MLC tests | not present | kV/MV planar, CBCT, picket fence, dynamic-wedge checks added |

Daily output constancy at 3 percent and monthly at 2 percent did not change. The weekly chart check and the simulator and TPS sections of TG-40 were not replaced by TG-142; they moved to TG-275 (chart review), TG-66 (CT simulator), and TG-53/MPPG 5.a (planning system). When a stem cites TG-40 numbers, answer with TG-40 numbers and know that TG-142 is the current reference.

**Daily, monthly, annual.** Daily is safety and the few things that drift overnight: door interlock, audio-visual, lasers, ODI, output constancy at 3 percent, and the imaging-to-treatment isocenter check for IGRT machines. Monthly is constancy against baseline: output at 2 percent, profiles at 1 percent, electron energy at 2 mm or 2 percent, mechanical indicators at 1° and 2 mm, the dynamic wedge, and imaging geometry. Annual is the absolute calibration (TG-51 at 1 percent), the full mechanical and dosimetric survey against commissioning (isocenter coincidence, wedge transmission, output versus gantry angle and dose rate, MU linearity, imaging dose), and the beam-quality index. A monthly result inside its tolerance does not satisfy an annual test with a tighter one.

### Worked example

**Given.** An independent calculation returns 206 MU for a field the planning system computed at 200 MU, at a homogeneous point in a conventional field. The clinic's action level for that geometry is 3 percent.

**Arithmetic.** \((206 - 200) / 200 = 6 / 200 = 0.030 = 3.0\%\). The difference sits at the action level. Clinic policy decides whether "at" is "over"; this bank treats a result at the action level as requiring investigation before treatment.

**Check.** \(200 \times 1.03 = 206\). If the point had been in lung with a heterogeneity correction, the action level would be about 5 percent and 3.0 percent would be inside it.

**Result means.** For a homogeneous point, 3.0 percent is the edge of what two algorithms should disagree by; the planner confirms depth, SSD, field size, and the wedge factor before the first fraction. Using 206 MU because the second program said so is not an investigation.

**Wrong turns**

- Dividing by the second-check MU instead of the planning-system MU. \(6 / 206 = 2.9\%\), which quietly moves the result under the line.
- Applying the 5 percent heterogeneity action level to a homogeneous water-equivalent point.
- Sending the daily-output diode array to the ADCL, or letting the reference chamber run for five years on one coefficient.
- Citing TG-53 as the document that sets today's dose-calculation tolerances. That is MPPG 5.a.

**Traps.** Two years for the chamber, one year for the survey meter. Three percent for a simple MU check, about five where heterogeneity makes algorithms disagree. TG-40 numbers when the stem says TG-40; TG-142 otherwise.

**Sources.** AAPM TG-51 and the ADCL calibration recommendation (two years). 10 CFR 20.1501 for survey-meter calibration. AAPM TG-114 for independent MU verification action levels. TG-142 for the dynamic-wedge and the daily, monthly, and annual structure. AAPM TG-53 and MPPG 5.a for the planning system; TG-106 and TG-119 for beam data and IMRT commissioning. TG-218 for IMRT QA.

## Safety Culture: Two Identifiers, Swiss Cheese, FMEA Numbers, Fault Trees, and Staffing

**Objectives:** VII.7, VII.6

**What the exam expects:** Four safety-culture tools with one fact each: the two-identifier rule, the Swiss-cheese model, the TG-100 risk-priority-number scale and its action trigger, and the fault tree. Plus the staffing ratios from the ISCRO "Blue Book" that ASTRO's safety documents carried forward. The incident-reporting lesson above has RO-ILS, root-cause analysis, and the medical-event rules; this lesson adds the numbers and the names.

**Two patient identifiers.** Before any procedure, including simulation, plan approval, and every treatment fraction, the patient is identified with two independent identifiers: full name and date of birth, or name and medical record number. A photograph in the record-and-verify system is a common third check. The room number, the bed, and the appointment time are not identifiers, because they describe where the patient is rather than who the patient is. The rule is the first of The Joint Commission's National Patient Safety Goals, and a wrong-patient treatment is both a medical event (10 CFR 35.3045) and the failure this rule exists to stop.

**Swiss-cheese model.** James Reason's model pictures each defence (the plan check, the independent MU calculation, record-and-verify, pre-treatment imaging, the time-out) as a slice of cheese with holes. No single slice is solid. An error reaches the patient when the holes in every slice line up on the same day. The design lesson is that defences must be independent, so that one cause does not open the same hole in all of them, and that near misses (an error that stopped at slice three) are the data that show where the holes are. Blaming the person at the last slice does not close the holes in the earlier ones.

**TG-100 numbers.** Failure-mode-and-effects analysis scores each failure mode on three scales from 1 to 10: occurrence O (how likely), severity S (how bad for the patient), and detectability D (how likely it goes unnoticed, so a failure nobody would catch scores 10). The risk priority number is the product, \(\mathrm{RPN} = O \times S \times D\), so the scale runs from 1 to 1,000. The TG-100 example sets a working trigger for action at an RPN above about 125 or a severity of 8 or more regardless of RPN; a mode with S = 10 and a low RPN still gets a control because the consequence is catastrophic. The scales are roughly logarithmic in the underlying probabilities, so a step of one is a large change. The process map comes first, the FMEA second, and the fault tree third.

**Fault tree.** A fault-tree analysis starts from one unwanted outcome (the top event, such as wrong dose to the target) and works backward through AND and OR gates to the causes that could produce it, and to the causes of those causes, until the tree reaches the basic events that a quality-management step could prevent or detect. The FMEA lists failure modes forward from the process; the fault tree reasons backward from the harm. TG-100 uses the tree to decide where a check or a forcing function cuts the most branches at once. In the TG-100 IMRT analysis the most frequent root causes were human (procedural slips and communication), followed by missing procedures and inadequate training, which is why the recommended controls are checklists, standardized communication, and independent review rather than more hardware tests.

**Staffing ratios.** The ISCRO "Blue Book" (Inter-Society Council for Radiation Oncology, 1991) gave the staffing guidance that items still quote: about one dosimetrist per 300 patients treated per year, one qualified medical physicist per 400 patients per year, one radiation oncologist per 200 to 250 patients per year, and two therapists per treatment machine (more when the daily load is high). ASTRO's Safety Is No Accident (2012, updated 2019) carries the same structure and adds that complex techniques (IMRT, SRS, brachytherapy) raise the staffing need above the simple ratio. The ratios are per year of new patients, not per day, and they are minimums for a conventional case mix.

### Worked example

**Given.** FMEA of the shift entry at simulation. Occurrence 4, severity 8, detectability 5.

**Arithmetic.** \(\mathrm{RPN} = 4 \times 8 \times 5 = 160\). 160 is above the 125 trigger. Severity 8 also meets the severity-alone trigger.

**Check.** \(4 \times 8 = 32\), \(32 \times 5 = 160\). Lowering detectability to 2 by adding an independent check of the shift against the CT reference point gives \(4 \times 8 \times 2 = 64\), under 125, but S is still 8, so the mode stays on the watch list even after the control is added.

**Result means.** This failure mode gets a control now: a second person compares the entered shift with the simulation record before the first fraction, which attacks D. Severity cannot be changed by a check; occurrence can be lowered by a template or a forcing function in the software. Either way the item is tracked because of its severity.

**Wrong turns**

- Adding O + S + D. The RPN is a product, and the range is 1 to 1,000, not 3 to 30.
- Scoring detectability high when the failure is easy to detect. High D means hard to detect.
- Dismissing a mode with RPN 90 and S = 10. Severity alone can trigger action.
- Using the room number as the second identifier.
- Quoting the dosimetrist ratio as per day. It is about 300 patients per year.

**Traps.** Two identifiers, both about the person. Cheese slices are independent defences. RPN from 1 to 1,000, act above about 125 or at high severity. Fault tree reasons backward from harm. One dosimetrist per 300 patients a year.

**Sources.** The Joint Commission National Patient Safety Goal 1 (two identifiers). Reason's Swiss-cheese model as used in TG-100 and RO-ILS teaching. AAPM TG-100 for FMEA scales, RPN, the 125 and severity-8 trigger used in its example, and fault-tree analysis. ISCRO Blue Book (1991) and ASTRO Safety Is No Accident for staffing. The ratios are the teaching values this bank uses.

## Source Drift: Lens Limits, Cataract Thresholds, and Penumbra Definitions

**Objectives:** admin, VI.1

**What the exam expects:** Three facts whose "right" number depends on which source and which year the item writer used. Know both values, know which one is current, and know which one this bank keys when the stem does not say.

**Lens of the eye.** The occupational lens limit in NCRP Report 116 and in 10 CFR 20.1201 is 150 mSv per year. ICRP's 2011 statement on tissue reactions lowered its recommended occupational lens limit to 20 mSv per year averaged over five years, with no single year above 50 mSv, after epidemiology showed cataracts at lower doses than the older models assumed. The NRC did not change its regulation, so the U.S. legal limit is still 150 mSv. The bank's rule: "according to NCRP" or "under 10 CFR 20" is 150 mSv; "according to ICRP" or "current international recommendation" is 20 mSv. The public lens figure in NCRP 116 is 15 mSv; question sets that print 50 mSv or 5 mSv for the public lens are using a wrong key, and the bank does not import them.

**Cataract threshold.** Older texts give the threshold for a radiation-induced cataract as about 2 Gy in a single acute exposure and about 5 Gy (sometimes quoted up to 8 Gy) when fractionated, and some practice tests key 2 Gy in one place and 5 Gy in another. ICRP's 2011 review set the threshold at about 0.5 Gy whether the dose is acute or protracted, and that revision is what drove the lens-limit change above. The bank keys 0.5 Gy as the current threshold. When a stem says "classically" or quotes an older text, 2 Gy single and 5 Gy fractionated are the legacy values. A clinical planning constraint for the lens (several grey, module 43) is a different number again; it is a tolerance chosen against cataract risk over years, not the threshold itself.

**Penumbra width.** Physical penumbra is the lateral distance between two isodose lines at a stated depth. The classic definition, used by Khan and by most of the bank (modules 05 and 19), is the 80 percent to 20 percent distance. Some course material and some practice tests use 90 percent to 20 percent, which gives a wider number for the same profile, and at least one test set uses both in different places. Geometric penumbra, from source size and distances, is a third quantity with its own formula (module 36). The bank's rule: compute 80 to 20 when the stem does not specify; compute whatever the stem specifies when it does; never report a geometric-penumbra formula result as a measured 80 to 20 width.

**How to answer a drifting item.** Read the stem for a source cue (NCRP, NRC, ICRP, "classically", "current"). If there is a cue, follow it. If there is none, pick the current value, and expect the legacy value to appear as a distractor. If both values appear as options with no cue, the item is flawed; pick the current value and move on.

**Sources.** NCRP Report 116 and 10 CFR 20.1201 (150 mSv lens, 15 mSv public lens). ICRP 2011 statement on tissue reactions and ICRP Publication 118 (20 mSv lens, 0.5 Gy cataract threshold). Khan for the 80–20 physical penumbra. The drift itself is documented in the review of the practice-test sets this bank was checked against.
