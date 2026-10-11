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

**Sources.** AAPM TG-275 (plan and chart review) and the weekly chart-check cadence from TG-40 that items still test. TG-142 does not replace the chart check.

## Record and Verify Systems and EMR

**Objectives:** VII.4

**What the exam expects:** The record-and-verify system (and the electronic medical record it feeds) must match the approved plan: MU, energy, gantry, collimator, couch, MLC, and accessories such as the wedge. A mismatch is a hold, not a note for later. The EMR is the chart of record; a local spreadsheet is not.

### Worked example

**Given.** Breast tangents were planned with a collimator angle of 5.7° so the superior border follows a half-beam supraclavicular field (module 36). The record-and-verify collimator is 0.0°.

**Arithmetic.** The mismatch is \(5.7^\circ - 0^\circ = 5.7^\circ\). No tolerance of “a couple of degrees” is in play: the approved value is 5.7° and the loaded value is 0°.

**Check.** \(\tan(5.7^\circ) \approx 0.10\), which is the 10 cm half-field at SAD 100 cm from the breast lesson. A collimator at 0° does not produce that match.

**Result means.** Treat the mismatch as a setup error. Loading 0° reintroduces the divergence the collimator angle was there to remove. The dosimetrist does not “fix it at the machine” by editing the plan without a new check.

**Wrong turns**

- Assuming the record-and-verify database cannot drift from the exported plan.
- Overriding an interlock to match an accessory the plan does not have (wedge in the tray, factor not in the MU: module 34).
- Documenting the change only in a hallway conversation. The EMR has to hold the approved plan.

**Traps.** Read every parameter the stem lists, not only MU. Energy 10 MV loaded against 6 MV planned is the same class of error.

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

**Sources.** AAMD Scope of Practice and Practice Standards. The prescription is the physician’s under state medical practice and under the clinic’s standard of care.

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

**What the exam expects:** RO-ILS (Radiation Oncology Incident Learning System, ASTRO and AAPM) is the voluntary national incident-learning system. It is not a regulator and it is not a punishment log. Near misses are reported. Root-cause analysis asks how the process let the error through. Process improvement changes that step (a forcing function, a checklist, a second calculation) rather than stopping at “be more careful.”

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

Simulation QA uses the same spirit: lasers, field size, and ODI within the mechanical tolerance before a patient is marked. A failed interlock stops the day even when output is perfect.

### Worked example

**Given.** Morning output reads 1.028 cGy/MU against a baseline of 1.000 cGy/MU. The same morning the ODI reads 98.5 cm when the mechanical distance is 100.0 cm.

**Arithmetic.** Output difference \(= (1.028 - 1.000)/1.000 = 0.028 = 2.8\%\). ODI error \(= 100.0 - 98.5 = 1.5\) cm \(= 15\) mm.

**Check.** \(1.028 - 1 = 0.028\). \(15\) mm is \(15/2 = 7.5\) times the 2 mm tolerance.

**Result means.** 2.8% is inside the daily output window of about 3% and outside the monthly window of about 2%. If this is the daily check, output constancy passes and is watched. If this is the monthly check, output fails. The ODI fails either way: 15 mm against 2 mm. Do not treat on a 15 mm optical-distance error. The door interlock is a separate daily check; a passed output does not excuse a taped-open door.

**Wrong turns**

- Applying the 3% daily window to the annual TG-51 comparison, where the expectation is about 1%.
- Calling a 15 mm ODI error “within 2 cm” and treating. The tolerance is 2 mm.
- Skipping the interlock because the output was 2.8%.

**Traps.** Say which check it is (daily, monthly, annual) before you pick 3%, 2%, or 1%.

**Sources.** AAPM TG-142 for linear-accelerator QA tolerances (daily interlock and output constancy, monthly output, annual absolute dose). ODI tolerance of 2 mm is the common mechanical tolerance these items use. Weekly chart review as in TG-40 / TG-275.

## QA and Standard of Care Quiz

**Skills this quiz checks**

- TG-51: water, \(N_{D,w}\), \(k_Q\), \(\%dd(10)_x\) for photons, \(R_{50}\) for electrons.
- TG-142: daily interlock, daily output about 3%, monthly output about 2%, annual TG-51 about 1%, ODI about 2 mm, plus a weekly chart check.
- IMRT QA: gamma and ion chamber are both required; one can pass while the other fails.
- Electron cutout factor measured for small fields, and placed in the MU denominator.
- AAMD scope: the dosimetrist does not prescribe.
- RO-ILS is voluntary incident learning; root cause is the process.
- Deliverability: MLC travel, small segments, collision, modulation, gantry speed versus dose rate.
- Record-and-verify parameters match the plan, including accessories and angles.
