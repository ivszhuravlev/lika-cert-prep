# Module 42. Quality Assurance and Standard of Care

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## QA and TPS Commissioning

### Q1
Stem: What is the point of TPS commissioning before the first patient?
A. Copy another clinic's beam model without measurement
B. Turn on the default CT-density curve and skip checks
C. Show that calculated dose matches measurement for the clinical range
D. Commission only one 10×10 cm open field at dmax
Answer: C
Objective: VII.1
Why: Commissioning compares the planning system with measured dose over energies, field sizes, depths, modifiers, and heterogeneities that you will actually use. A single open field is not that test. Correct choice: Show that calculated dose matches measurement for the clinical range. A model has to be tied to this machine's data. The CT-to-density table is part of commissioning, not an unreviewed default. One point cannot represent wedges, blocks, inhomogeneity, or small fields.

### Q2
Stem: Commissioning baseline later used for TG-142. Compute the percent deviation of this annual check. Expected output is 1 cGy/MU and the measurement is 1.027 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -2.7%
B. 2.6%
C. 102.7%
D. 2.7%
Answer: D
Objective: VII.1
Why: Substitute (1.027 − 1) / 1 × 100 = 0.027 / 1 × 100 = 2.70%, reported as 2.7%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -2.7%. Dividing the difference by the measurement instead of the expected value gives 2.6%. Reporting the ratio as a percent (100 × measured/expected) gives 102.7%, which is not the deviation.

### Q3
Stem: An algorithm is changed from pencil beam to convolution. What else has to happen before clinical use?
A. Nothing, if the MU second check is unchanged
B. Only the wedge names are edited
C. The CT scanner is replaced
D. Recommission or revalidate the beam model
Answer: D
Objective: VII.1
Why: A different algorithm is a different dose. It needs its own measured comparison before patients are planned on it. Correct choice: Recommission or revalidate the beam model. The second check does not prove the new algorithm against measurement. The dose engine changed. Wedge labels are not the validation. The scanner may be fine. The dose model is what changed.

### Q4
Stem: Which data set is part of TPS commissioning rather than a daily linac check?
A. The CT number to density table
B. Door interlock function
C. Morning output constancy within 3%
D. The in-room camera
Answer: A
Objective: VII.1
Why: Dose in heterogeneous tissue depends on the CT-to-density curve loaded in the TPS. That curve is commissioned. Daily door and output checks do not build it. Correct choice: The CT number to density table. That is a daily safety check on the machine, TG-142 style. That is daily output, not the density table. The camera is a safety monitor, not a dose model.

### Q5
Stem: TG-142 annual x-ray output calibration tolerance, relative to the standard, is which value?
A. 3%
B. 1%
C. 2%
D. 5%
Answer: B
Objective: VII.1
Why: TG-142 output constancy is 3% daily and 2% monthly. The annual absolute calibration is 1%. Correct choice: 1%. 3% is the daily output constancy tolerance. 2% is the monthly output constancy tolerance. 5% is looser than the TG-142 annual calibration tolerance.

## Clinical Data: Plan Checks, Chart Reviews, Image Reviews

### Q1
Stem: Chart check. Confirm the written total. The prescription is 180 cGy per fraction for 28 fractions. What is the total dose in cGy?
A. 4860 cGy
B. 5040 cGy
C. 208.0 cGy
D. 50.4 cGy
Answer: B
Objective: VII.2
Why: Total = dose per fraction × number of fractions = 180 × 28 = 5040 cGy, which is 50.40 Gy. Reported in cGy as asked: 5040 cGy. Using one fewer fraction (forgetting the last fraction, or confusing sessions with intervals) gives 4860 cGy. Adding the fraction number to the daily dose gives 208.0 cGy. Writing the gray value (50.40) but leaving the unit as cGy gives 50.4 cGy, a 100-fold unit error.

### Q2
Stem: Chart check. A different fractionation. The prescription is 200 cGy per fraction for 25 fractions. What is the total dose in cGy?
A. 5000 cGy
B. 4800 cGy
C. 225.0 cGy
D. 50.0 cGy
Answer: A
Objective: VII.2
Why: Total = dose per fraction × number of fractions = 200 × 25 = 5000 cGy, which is 50.00 Gy. Reported in cGy as asked: 5000 cGy. Using one fewer fraction (forgetting the last fraction, or confusing sessions with intervals) gives 4800 cGy. Adding the fraction number to the daily dose gives 225.0 cGy. Writing the gray value (50.00) but leaving the unit as cGy gives 50.0 cGy, a 100-fold unit error.

### Q3
Stem: A weekly physics chart check is meant to catch which class of problem?
A. Only the vendor's software license date
B. The half-life of Ir-192 on a linac-only course
C. A course that has drifted from the approved plan, images, or prescription
D. Replacing the physician's prescription with a new dose
Answer: C
Objective: VII.2
Why: Weekly chart review looks at cumulative dose, fractions delivered, image guidance, shifts, and whether treatment still matches the approved plan. It is a standard-of-care review, separate from the daily machine interlock test. Correct choice: A course that has drifted from the approved plan, images, or prescription. License dates are not the weekly clinical check. No brachytherapy source is in this course. The dosimetrist and the physicist do not rewrite the prescription on a chart check. They verify the plan still matches it.

### Q4
Stem: Which item belongs in a pre-treatment plan check?
A. Prescription dose, fractionation, energy, and laterality match the plan
B. The patient's parking spot
C. Mayneord F for every SAD plan
D. Deleting the prior-irradiation history to simplify the DVH
Answer: A
Objective: VII.2
Why: The plan check confirms the physician's prescription: site, laterality, total dose, dose per fraction, energy, and technique, plus contours, hot spots, and prior dose. Correct choice: Prescription dose, fractionation, energy, and laterality match the plan. Not a plan parameter. SAD plans use TMR. Mayneord F is an SSD PDD adjustment, not a universal check. Prior dose is part of the check, especially for cord, heart, and retreats.

### Q5
Stem: Image review before treatment should confirm what?
A. The isocenter and shifts on the approved image match the plan
B. That the picture is aesthetically sharp only
C. That bolus can be ignored if the image is dark
D. That a CBCT replaces the written prescription
Answer: A
Objective: VII.2
Why: Someone compares the setup image with the plan: correct patient, isocenter, shift direction, and any bolus or device that should be visible. A reversed anterior shift is a classic miss. Correct choice: The isocenter and shifts on the approved image match the plan. Sharpness is not the clinical question. The match and the shifts are. Bolus has to be present if it was planned, regardless of window level. Imaging does not rewrite the prescription.

## Record and Verify Systems and EMR

### Q1
Stem: What does a record-and-verify system compare at treatment?
A. It replaces the physics plan check
B. Set MU, energy, jaws, gantry, and couch against the approved plan
C. It recalculates Clarkson scatter
D. It leak-tests the HDR source
Answer: B
Objective: VII.4
Why: Record and verify stops a delivery that does not match the approved parameters: MU, energy, collimator, gantry, and couch. It is not a substitute for contour review or an independent MU calculation. Correct choice: Set MU, energy, jaws, gantry, and couch against the approved plan. R&V is a delivery interlock. It does not review contours or the prescription's clinical intent. It does not perform a Clarkson integration. That is a source QC task, not linac R&V.

### Q2
Stem: Which standard carries images and RT plan objects between the scanner, TPS, and R&V?
A. A private spreadsheet as the only transfer
B. DICOM
C. HL7 as the only RT plan format
D. PDF screenshots of the isodose
Answer: B
Objective: III.9
Why: DICOM, including RT Structure, RT Plan, and RT Dose, is the transfer standard between CT, planning, and delivery. Correct choice: DICOM. A spreadsheet is not the image-and-plan transfer standard. HL7 moves clinical messages. RT images, structures, plan, and dose ride on DICOM. A picture is not a transferable plan object.

### Q3
Stem: A manual MU override is typed at the console. What has to be true?
A. Overrides are invisible and need no record
B. Any therapist may change the prescription dose this way
C. The override resets the TG-51 calibration
D. The override is documented and matches an approved plan change
Answer: D
Objective: VII.4
Why: The EMR and the R&V record are the legal treatment record. An override that is not documented, or that does not match a checked plan, is a treatment-process failure. Correct choice: The override is documented and matches an approved plan change. An unrecorded override breaks the medical record. The prescription is the physician's. An MU change follows an approved plan. Typing MU does not recalibrate the machine.

### Q4
Stem: The TPS says 6 MV and the R&V field is armed for 18 MV. The MU numbers match. What is the status?
A. Treat, because MU match is sufficient
B. Treat if the wedge factor is 1
C. Switch to electrons without telling anyone
D. Do not treat. Energy is part of the plan
Answer: D
Objective: VII.4
Why: Energy is a primary prescription and R&V parameter. Matching MU at 18 MV instead of 6 MV is not the approved plan. Correct choice: Do not treat. Energy is part of the plan. The same MU at the wrong energy is the wrong dose and the wrong depth dose. The wedge does not excuse the energy. An unplanned modality change is not a fix.

### Q5
Stem: Where does the signed prescription live for later review?
A. Only in a personal email folder
B. Only on a sticky note on the console
C. It is optional if DICOM transferred
D. In the EMR, tied to the delivered R&V record
Answer: D
Objective: VII.4
Why: The EMR holds the clinical record, and the R&V system holds the delivered parameters. Together they are what a later chart review can audit. Correct choice: In the EMR, tied to the delivered R&V record. Email is not the treatment record. The console note is not the legal record. DICOM moves the technical plan. The clinical prescription and delivery record still have to exist in the chart.

## Treatment Beam QA Measurement and Analysis (eg IMRT, electron cutout factors)

### Q1
Stem: TG-218's universal tolerance for IMRT QA, using 3%/2 mm and a 10% dose threshold, is which pass rate?
A. 95%
B. 90%
C. 100%
D. 80%
Answer: A
Objective: VII.5
Why: TG-218 recommends gamma analysis at 3%/2 mm with a 10% threshold, a universal tolerance of 95% of points passing, and an action limit of 90%. Correct choice: 95%. 90% is the action limit, not the tolerance. TG-218 does not require a perfect 100% pass as the tolerance. 80% is below the action limit.

### Q2
Stem: A measured gamma pass rate is 93% under the TG-218 criteria above. How is it classified?
A. A full pass of the 95% tolerance
B. Below the 90% action limit
C. Meaningless because gamma ignores the plan
D. Below tolerance and above the action limit
Answer: D
Objective: VII.5
Why: 95% is the tolerance and 90% is the action limit. 93 sits between them, so the plan is investigated rather than ignored and rather than treated as a hard action-limit failure. Correct choice: Below tolerance and above the action limit. 93 is less than 95. 93 is still above 90. The result is interpretable: it missed tolerance and has not crossed the action limit.

### Q3
Stem: Electron output. The cutout factor used in the MU was higher than the measured factor. The cutout was planned with output factor 0.96, but the measured factor for that cutout is 0.9. The MU were calculated with the planned factor for an intended 200 cGy. Delivered dose = intended × (true factor / factor used), because MU = dose/(calibration × factor × …) and a factor that is too high makes the MU too small. What dose is delivered?
A. 200.0 cGy
B. 187.5 cGy
C. 213.3 cGy
D. 188.0 cGy
Answer: B
Objective: VII.5
Why: Factor ratio = 0.9 / 0.96 = 0.9375. Delivered = 200 × 0.9375 = 187.50 cGy, reported as 187.5 cGy. The patient is underdosed when the factor used in the MU calculation is larger than the true output factor. Assuming the intended dose was delivered gives 200.0 cGy. Inverting the factor ratio gives 213.3 cGy and would claim an overdose. Subtracting the raw factor difference from 1 and multiplying gives 188.0 cGy, which is not how an output factor enters the MU equation.

### Q4
Stem: Small electron cutouts should get their output factor from where?
A. A guess from the cone factor alone
B. A measurement of that cutout
C. Sterling's equivalent square only
D. The wedge factor
Answer: B
Objective: VII.5
Why: Electron cutout factors, especially for small fields, are measured. Calculating them from the open cone alone misses scatter from the cutout edges. Correct choice: A measurement of that cutout. The cutout blocks part of the cone. Small cutouts change output and need measurement. An electron cutout factor is not a photon equivalent-square lookup. A wedge factor is the wrong modifier.

### Q5
Stem: An array pass does not prove which of the following?
A. That a fluence was compared with a calculation
B. That a gamma score was computed
C. That the contours and the prescription were correct
D. That the measurement had a threshold
Answer: C
Objective: VII.5
Why: IMRT QA checks delivery against the calculated fluence or dose. It does not know whether the PTV was drawn on the wrong lung or the prescription was 10 Gy high. Plan review still has to do that. Correct choice: That the contours and the prescription were correct. That is what the array did. The score exists. It just does not audit anatomy. The analysis used a threshold. The limit of the test is elsewhere.

## AAMD Scope of Practice

### Q1
Stem: Under the AAMD scope, who writes the clinical prescription?
A. The dosimetrist, independently
B. The radiation oncologist
C. The manufacturer of the TPS
D. The record-and-verify system
Answer: B
Objective: VII.6
Why: The radiation oncologist prescribes. The dosimetrist designs the plan and performs dose calculations under the direction of the physician and the medical physicist, and documents that work. Correct choice: The radiation oncologist. Dosimetrists design and calculate plans. They do not independently prescribe. The vendor does not prescribe. Software does not hold a medical license.

### Q2
Stem: Which task is inside dosimetry practice?
A. Calculating and documenting the planned dose distribution
B. Independently approving a new total dose the physician did not order
C. Signing a TG-51 calibration report as the physicist
D. Waiving a missing written directive for HDR
Answer: A
Objective: VII.6
Why: Scope includes plan design, calculation, and clear documentation. It does not include an independent prescription or a physicist's calibration signature. Correct choice: Calculating and documenting the planned dose distribution. Changing the prescription is not in scope. Machine calibration is a physics responsibility. The directive is a medical and regulatory requirement.

### Q3
Stem: A physician asks for a plan that exceeds a published cord correlate and documents the reason. What is the dosimetrist's role?
A. Refuse to print the DVH
B. Calculate the plan and make the dose visible for the physician's decision
C. Change the prescription to 50 Gy without being asked
D. Turn heterogeneity off so the cord looks cooler
Answer: B
Objective: VII.6
Why: The dosimetrist's job is an honest plan and an honest DVH. The physician accepts the clinical tradeoff and documents it. Quietly editing the dose is outside scope. Correct choice: Calculate the plan and make the dose visible for the physician's decision. Hiding the dose is not advocacy. The dosimetrist does not rewrite the order. That falsifies the dose.

### Q4
Stem: Which product is a dosimetrist expected to hand off?
A. An undocumented set of MU
B. A verbal plan with no structures
C. A documented plan with calculation checks traceable to the prescription
D. A calibration factor Ndw
Answer: C
Objective: VII.6
Why: Practice standards expect a plan that someone else can check: prescription, beams, dose, and the calculation record. Correct choice: A documented plan with calculation checks traceable to the prescription. Undocumented MU cannot be checked later. Structures and documentation are part of the work. Ndw belongs to the physics calibration.

### Q5
Stem: Who is the appropriate supervisor for a dosimetrist's technical dose calculation?
A. The patient
B. A qualified medical physicist, with the physician directing the clinical plan
C. The front-desk scheduler only
D. No one, once certified
Answer: B
Objective: VII.6
Why: The clinical plan is directed by the radiation oncologist and the technical calculation is performed with the medical physicist. Certification defines the profession. It does not create an independent prescriber. Correct choice: A qualified medical physicist, with the physician directing the clinical plan. The patient consents. The patient does not supervise the calculation. Scheduling is not technical supervision. Certification does not remove physician and physicist direction.

## Measurement Equipment (Diodes, ion chambers, TLD, Survey Meters)

### Q1
Stem: Which instrument is used for absolute linac output under TG-51?
A. A Geiger-Mueller pancake survey meter
B. A diode left on the skin only
C. An ion chamber in water
D. Radiochromic film with no calibration curve
Answer: C
Objective: VI.4, VII.3
Why: TG-51 absorbed dose to water is measured with a calibrated ion chamber in a water phantom, with kQ and the usual corrections. A GM survey meter is for finding radiation, not for calibrating a linac. Correct choice: An ion chamber in water. A GM meter saturates in a linac beam and is not an absolute output chamber. A diode can do in-vivo dosimetry. It is not the TG-51 absolute standard. Uncalibrated film is not an absolute output measurement.

### Q2
Stem: A diode used for entrance dose differs from a TLD how?
A. The diode must be annealed for an hour before it can be read
B. The diode measures exposure rate for a regulatory survey
C. The diode reads immediately and is angle sensitive
D. The diode is immune to direction
Answer: C
Objective: VI.4, VII.3
Why: Diodes give an immediate reading and must be placed with their angular dependence in mind. TLDs integrate dose and are read later. Correct choice: The diode reads immediately and is angle sensitive. That delay pattern fits TLD, not a diode. Surveys use ion-chamber or GM survey meters. Diodes have angular and energy dependence. That is why placement matters.

### Q3
Stem: Why is a GM survey meter a poor choice for measuring linac head leakage close to the head while the beam is on?
A. It saturates at high dose rate
B. It cannot detect photons
C. It is the TG-51 standard
D. It measures only neutrons
Answer: A
Objective: VI.4, VII.3
Why: GM tubes are sensitive and dead-time limited. In a high dose-rate beam they saturate and read low. An ion-chamber survey meter is the tool for a quantitative exposure-rate measurement. Correct choice: It saturates at high dose rate. GM tubes detect photons and charged particles. Saturation is the problem, not blindness. TG-51 uses an ion chamber, not a GM tube. A standard GM tube is not a neutron rem-meter.

### Q4
Stem: An ion chamber is corrected to the TG-51 reference of 22°C and 101.33 kPa. Use Ctp = (273.2 + T) / 295.2 × 101.33 / P, with T in °C and P in kPa. The 295.2 is 273.2 + 22, the usual 22°C reference, and 101.33 kPa is the pressure reference. T = 25°C and P = 101.33 kPa. What is Ctp?
A. 0.9899
B. 1.0000
C. 1.0102
D. 1.1364
Answer: C
Objective: VI.4, VII.3
Why: Temperature ratio = (273.2 + 25) / 295.2 = 298.2 / 295.2 = 1.0102. Pressure ratio = 101.33 / 101.33 = 1.0000. Ctp = 1.0102 × 1.0000 = 1.0102, reported as 1.0102. A warm room (T above 22°C) with standard pressure makes Ctp greater than 1, so the raw reading is corrected upward. Inverting both the temperature and pressure ratios gives 0.9899. Applying only the pressure ratio gives 1.0000. Dividing the Celsius temperature by 22 and ignoring kelvin and pressure gives 1.1364.

### Q5
Stem: TLD is best described as which kind of dosimeter?
A. An integrating dosimeter read after the exposure
B. A real-time survey meter
C. A water-tank scanner
D. A primary calibration of Ndw by itself
Answer: A
Objective: VI.4, VII.3
Why: Thermoluminescent dosimeters store signal and are read later on a reader. They suit in-vivo points where an immediate diode reading is unnecessary. Correct choice: An integrating dosimeter read after the exposure. That is a survey instrument, not a TLD chip. A tank uses an ion chamber or diode under motion. The calibration coefficient lives with the ion chamber and the standards lab.

## Measurement Equipment Quiz

### Q1
Stem: Quiz. Chamber air is 20°C and the pressure is 98 kPa. Apply the stated Ctp formula. Use Ctp = (273.2 + T) / 295.2 × 101.33 / P, with T in °C and P in kPa. The 295.2 is 273.2 + 22, the usual 22°C reference, and 101.33 kPa is the pressure reference. T = 20°C and P = 98 kPa. What is Ctp?
A. 0.9737
B. 0.9932
C. 1.0340
D. 1.0270
Answer: D
Objective: VI.4, VII.3
Why: Temperature ratio = (273.2 + 20) / 295.2 = 293.2 / 295.2 = 0.9932. Pressure ratio = 101.33 / 98 = 1.0340. Ctp = 0.9932 × 1.0340 = 1.0270, reported as 1.0270. A warm room (T above 22°C) with standard pressure makes Ctp greater than 1, so the raw reading is corrected upward. Inverting both the temperature and pressure ratios gives 0.9737. Applying only the temperature ratio gives 0.9932. Applying only the pressure ratio gives 1.0340.

### Q2
Stem: Quiz. Monthly output measurement versus 1.000 cGy/MU. Expected output is 1 cGy/MU and the measurement is 0.975 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. 2.5%
B. -2.6%
C. 97.5%
D. -2.5%
Answer: D
Objective: VII.1
Why: Substitute (0.975 − 1) / 1 × 100 = -0.025 / 1 × 100 = -2.50%, reported as -2.5%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives 2.5%. Dividing the difference by the measurement instead of the expected value gives -2.6%. Reporting the ratio as a percent (100 × measured/expected) gives 97.5%, which is not the deviation.

### Q3
Stem: Quiz. Another cutout-factor miss. The cutout was planned with output factor 0.94, but the measured factor for that cutout is 0.88. The MU were calculated with the planned factor for an intended 180 cGy. Delivered dose = intended × (true factor / factor used), because MU = dose/(calibration × factor × …) and a factor that is too high makes the MU too small. What dose is delivered?
A. 168.5 cGy
B. 180.0 cGy
C. 192.3 cGy
D. 169.2 cGy
Answer: A
Objective: VII.5
Why: Factor ratio = 0.88 / 0.94 = 0.9362. Delivered = 180 × 0.9362 = 168.51 cGy, reported as 168.5 cGy. The patient is underdosed when the factor used in the MU calculation is larger than the true output factor. Assuming the intended dose was delivered gives 180.0 cGy. Inverting the factor ratio gives 192.3 cGy and would claim an overdose. Subtracting the raw factor difference from 1 and multiplying gives 169.2 cGy, which is not how an output factor enters the MU equation.

### Q4
Stem: A diode and a TLD disagree by 4% on an entrance measurement. Which limitation belongs to the diode?
A. It can only be read the next day
B. Angular dependence
C. It saturates like a GM tube in every geometry
D. It measures HVL directly
Answer: B
Objective: VI.4, VII.3
Why: Diodes are fast and directionally sensitive. A tilted diode changes the reading even when the dose did not. TLDs avoid that particular problem and pay for it with a delayed readout. Correct choice: Angular dependence. That delay is the TLD. Diode entrance dosimetry is routine. The characteristic problem in this list is angle. An HVL needs a transmission series, not a single diode reading.

### Q5
Stem: Which meter should quantify exposure rate at 1 m from an LDR patient?
A. A Farmer chamber in a 30 cm water tank at the bedside
B. A GM meter known to be pegged off scale
C. Radiochromic film left for a month with no calibration
D. An ion-chamber survey meter
Answer: D
Objective: VI.4, VII.3
Why: A calibrated ion-chamber survey meter measures exposure rate without the saturation that knocks out a GM tube near a source. Correct choice: An ion-chamber survey meter. A water-tank calibration setup is not a bedside survey. An off-scale GM reading is not a number. Uncalibrated film is not a survey.

### Q6
Stem: TG-142 daily x-ray output constancy tolerance is which value?
A. 1%
B. 2%
C. 3%
D. 10%
Answer: C
Objective: VII.9
Why: Daily output constancy is 3%, monthly is 2%, and annual absolute calibration is 1%. Correct choice: 3%. 1% is the annual calibration tolerance. 2% is the monthly tolerance. 10% is far outside TG-142 daily output constancy.

### Q7
Stem: Quiz. A warm room at 28°C and pressure 100 kPa. Use Ctp = (273.2 + T) / 295.2 × 101.33 / P, with T in °C and P in kPa. The 295.2 is 273.2 + 22, the usual 22°C reference, and 101.33 kPa is the pressure reference. T = 28°C and P = 100 kPa. What is Ctp?
A. 0.9672
B. 1.0203
C. 1.0133
D. 1.0339
Answer: D
Objective: VI.4, VII.3
Why: Temperature ratio = (273.2 + 28) / 295.2 = 301.2 / 295.2 = 1.0203. Pressure ratio = 101.33 / 100 = 1.0133. Ctp = 1.0203 × 1.0133 = 1.0339, reported as 1.0339. A warm room (T above 22°C) with standard pressure makes Ctp greater than 1, so the raw reading is corrected upward. Inverting both the temperature and pressure ratios gives 0.9672. Applying only the temperature ratio gives 1.0203. Applying only the pressure ratio gives 1.0133.

### Q8
Stem: Film or an array can measure a beam. What do they not replace?
A. An absolute TG-51 calibration of output
B. A relative profile
C. A gamma map
D. A light-field check
Answer: A
Objective: VI.4, VII.3
Why: Relative tools need a calibration chain back to an ion chamber and TG-51 if you want cGy. They do not themselves replace that absolute calibration. Correct choice: An absolute TG-51 calibration of output. They are often exactly how a profile is measured. An array is a common gamma tool. Some QA uses film for light-versus-radiation. The thing they do not replace is the absolute calibration.

### Q9
Stem: Quiz. A second morning reading versus 1.000 cGy/MU. Expected output is 1 cGy/MU and the measurement is 1.045 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -4.5%
B. 4.3%
C. 104.5%
D. 4.5%
Answer: D
Objective: VII.1
Why: Substitute (1.045 − 1) / 1 × 100 = 0.045 / 1 × 100 = 4.50%, reported as 4.5%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -4.5%. Dividing the difference by the measurement instead of the expected value gives 4.3%. Reporting the ratio as a percent (100 × measured/expected) gives 104.5%, which is not the deviation.

## Incident Reporting for Patient Safety (Quality Improvement, ROILS, Root Cause Analysis, Process Improvement)

### Q1
Stem: What is RO-ILS?
A. A federal enforcement fine
B. A voluntary radiation-oncology incident-learning system
C. The linac daily output tolerance
D. A brachytherapy leak test
Answer: B
Objective: VII.7
Why: RO-ILS is the Radiation Oncology Incident Learning System. Clinics submit events and near misses so others can learn. It is voluntary and non-punitive in design. Correct choice: A voluntary radiation-oncology incident-learning system. RO-ILS is learning, run with ASTRO and AAPM, not a fine schedule. That is TG-142. Leak tests are source QC.

### Q2
Stem: A root-cause analysis after a wrong-shift event should emphasize what?
A. How the process allowed the shift to be reversed
B. Only which person to blame
C. The patient's insurance group
D. Whether the wedge angle was 60°
Answer: A
Objective: VII.7
Why: Root-cause analysis looks for the system: unclear shift language, no second check, a console that accepted a reversed direction. Naming a person is not the whole analysis. Correct choice: How the process allowed the shift to be reversed. Blame without a process change leaves the next person in the same trap. Insurance is not the cause of a reversed shift. The event was a shift. The analysis stays on the shift path unless the evidence says otherwise.

### Q3
Stem: A near miss is caught before treatment. Why report it?
A. The same process could reach a patient next time
B. Near misses are not worth recording
C. Only events over 5 Gy are learning opportunities
D. Reporting replaces the plan check
Answer: A
Objective: VII.7
Why: A near miss shows a hole in the process before a patient is hurt. Incident-learning systems want those events. Correct choice: The same process could reach a patient next time. They are often the cheapest warning you will get. Learning is not limited to a dose cutoff. The plan check still happens. Reporting is additional.

### Q4
Stem: Which content belongs in a useful incident report?
A. Only the reporter's job title
B. What happened, how it was found, and the dose or potential dose
C. A guess with no timeline
D. The patient's photo ID only
Answer: B
Objective: VII.7
Why: A useful report says what was planned, what happened, who caught it, and what dose was delivered or could have been delivered. That is what a later review can learn from. Correct choice: What happened, how it was found, and the dose or potential dose. Title without facts does not teach the next clinic. The timeline is how you find the missed check. Identity may matter, but the event facts are the report.

### Q5
Stem: Which response improves the process after a repeated documentation miss?
A. Tell staff to be more careful and change nothing else
B. Change the checklist so the miss is hard to skip
C. Stop chart rounds
D. Turn off the R&V tolerance
Answer: B
Objective: VII.7
Why: Process improvement changes the system: a forced field in the EMR, a second check, a clearer shift form. 'Be careful' alone does not do that. Correct choice: Change the checklist so the miss is hard to skip. An exhortation without a process change tends to fail again. Removing the review removes a detection step. Loosening the interlock hides the next error.

## Factors and Limitations of Deliverable Plans

### Q1
Stem: Which plan is not deliverable even if the DVH looks acceptable?
A. A plan whose cord Dmax is below the physician's limit
B. A posterior beam that collides the gantry with the patient or couch
C. A coplanar 6 MV plan with normal MU
D. A plan normalized to the prescription
Answer: B
Objective: VII.8
Why: Clearance is a deliverability limit. A beautiful DVH that the gantry cannot reach is not a treatment. Correct choice: A posterior beam that collides the gantry with the patient or couch. An acceptable cord dose does not create a collision. That can be deliverable. Normalization does not by itself make the geometry impossible.

### Q2
Stem: Very high modulation with many tiny low-MU segments mainly risks what?
A. A lower wedge factor by definition
B. Automatic removal of all penumbra
C. Exemption from IMRT QA
D. Unstable delivery and a plan that is sensitive to small MLC errors
Answer: D
Objective: VII.8
Why: Tiny segments and very low MU per segment are hard for the MLC and the dose model. The plan may pass a DVH and still be a poor delivery. Correct choice: Unstable delivery and a plan that is sensitive to small MLC errors. Modulation is not a physical wedge factor. Penumbra remains. Highly modulated plans need QA, not an exemption.

### Q3
Stem: A field is wider than the MLC carriage can travel. What is the limitation?
A. The equivalent square formula fails above 10 cm
B. TG-51 cannot calibrate fields over 20 cm
C. The MLC cannot cover the aperture the plan drew
D. HVL of the jaw becomes zero
Answer: C
Objective: VII.8
Why: Leaves and carriages have travel limits. A jaw opening the MLC cannot cover will not match the planned aperture. Split the field or change the geometry. Correct choice: The MLC cannot cover the aperture the plan drew. Sterling's formula is not limited to 10 cm. The hardware is the limit here. Calibration is a separate problem. The carriage travel is mechanical. No.

### Q4
Stem: Imaging dose from daily CBCT is omitted from the plan dose. What is the honest statement?
A. Imaging dose is always zero
B. The omission makes the PTV colder
C. QUANTEC already added imaging
D. The plan dose is not the total dose the patient receives from imaging plus treatment
Answer: D
Objective: VII.8
Why: If the displayed dose excludes CBCT, you should not pretend the DVH is the patient's entire dose. For most definitive courses the imaging contribution is a small addendum. It is still a limit on what the plan number means. Correct choice: The plan dose is not the total dose the patient receives from imaging plus treatment. CBCT dose is small compared with therapy, but it is not zero. Omitting imaging from the TPS does not change the treatment beams. It understates total dose. QUANTEC correlates are therapy dose-volume data, not an automatic imaging add-on.

### Q5
Stem: Which change can make a previously deliverable plan undeliverable?
A. Renaming the course in the EMR
B. Printing the DVH in color
C. Writing the prescription in Gy instead of cGy with the number converted correctly
D. Adding a couch kick that now hits the patient
Answer: D
Objective: VII.8
Why: Non-coplanar angles buy dose conformity and spend clearance. A new couch angle has to be checked on the machine geometry, not only on the DVH. Correct choice: Adding a couch kick that now hits the patient. A name change does not move the gantry. Color is not clearance. A correct unit conversion does not change geometry.

## QA Requirements: Sim and Treatment Equipment

### Q1
Stem: A CT simulator water phantom reads about +80 HU in the center after a morning scan. What does that suggest?
A. The result is expected because water is 80 HU
B. Only the laser names need editing
C. The CT number calibration is off, so densities will be wrong
D. The brachytherapy source inventory failed
Answer: C
Objective: VII.9
Why: Water should sit near 0 HU and air near −1000. A water reading of +80 HU will push tissue densities high in the TPS and bias dose. Correct choice: The CT number calibration is off, so densities will be wrong. Water is defined near 0 HU, not +80. Lasers do not shift the Hounsfield number of water. This is a CT number, not a source count.

### Q2
Stem: Which sim check protects against a left-right swap?
A. Measure the wedge factor
B. Compute two HVL of lead
C. Confirm patient orientation and the DICOM orientation tags before planning
D. Run an HDR leak test
Answer: C
Objective: VII.9
Why: Head-first versus feet-first, and supine versus prone, have to match the scan and the plan. A flipped orientation treats the wrong side. Orientation is checked at simulation and again at import. Correct choice: Confirm patient orientation and the DICOM orientation tags before planning. A wedge factor will not catch a flipped patient. Shielding math is unrelated. Wrong modality.

### Q3
Stem: Daily treatment-machine safety checks in the TG-142 sense include which item?
A. Door interlock functional
B. Annual TG-51 calibration only
C. A full commissioning of a new algorithm
D. Leak-testing every HDR source every morning
Answer: A
Objective: VII.9
Why: TG-142 daily checks include safety interlocks such as the door, plus output constancy at 3%. The morning test does not replace annual calibration. Correct choice: Door interlock functional. The annual calibration is not the daily safety test. That is commissioning, not the morning check. Sealed-source leak tests are periodic, not the linac door check.

### Q4
Stem: Lasers on the CT simulator are used to do what?
A. Calibrate absolute dose in cGy/MU
B. Mark a reproducible setup origin that planning and treatment can share
C. Generate Ir-192 dwell times
D. Replace the CT-density table
Answer: B
Objective: VII.9
Why: Simulator lasers define the setup marks and the origin that shifts are written from. If the lasers do not match the imaging isocenter, every shift is biased. Correct choice: Mark a reproducible setup origin that planning and treatment can share. Dose calibration is a linac measurement. Dwell times come from the brachytherapy plan. Lasers do not assign density.

### Q5
Stem: A planning scan stops short of the lungs for a breast tangent plan. Why is that a sim QA failure?
A. The data set does not cover the beams and the relevant anatomy
B. Tangent plans never need CT
C. Only the isocenter slice is required
D. The missing anatomy can be replaced by Mayneord F
Answer: A
Objective: VII.9
Why: Simulation has to cover the targets, the organs at risk, and the beam paths, including flash and exit. A scan that clips the lung is an incomplete data set. Correct choice: The data set does not cover the beams and the relevant anatomy. Modern tangent plans are CT based. Entrance, exit, lung, and heart need to be in the scan. Mayneord F does not invent missing slices.

## QA and Standard of Care Quiz

### Q1
Stem: Quiz. Is this deviation inside a 3% daily tolerance? Compute the deviation first. Expected output is 1 cGy/MU and the measurement is 1.041 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -4.1%
B. 3.9%
C. 104.1%
D. 4.1%
Answer: D
Objective: VII.9
Why: Substitute (1.041 − 1) / 1 × 100 = 0.041 / 1 × 100 = 4.10%, reported as 4.1%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -4.1%. Dividing the difference by the measurement instead of the expected value gives 3.9%. Reporting the ratio as a percent (100 × measured/expected) gives 104.1%, which is not the deviation.

### Q2
Stem: Quiz. Another morning output. Expected output is 1 cGy/MU and the measurement is 1.034 cGy/MU. Percent deviation = (measured − expected) / expected × 100. What is the deviation?
A. -3.4%
B. 3.4%
C. 3.3%
D. 103.4%
Answer: B
Objective: VII.9
Why: Substitute (1.034 − 1) / 1 × 100 = 0.034 / 1 × 100 = 3.40%, reported as 3.4%. A positive result means the beam is hotter than the calibration value. Reversing measured and expected flips the sign and gives -3.4%. Dividing the difference by the measurement instead of the expected value gives 3.3%. Reporting the ratio as a percent (100 × measured/expected) gives 103.4%, which is not the deviation.

### Q3
Stem: Quiz. Chart-check arithmetic. The prescription is 250 cGy per fraction for 20 fractions. What is the total dose in cGy?
A. 4750 cGy
B. 270.0 cGy
C. 50.0 cGy
D. 5000 cGy
Answer: D
Objective: VII.2
Why: Total = dose per fraction × number of fractions = 250 × 20 = 5000 cGy, which is 50.00 Gy. Reported in cGy as asked: 5000 cGy. Using one fewer fraction (forgetting the last fraction, or confusing sessions with intervals) gives 4750 cGy. Adding the fraction number to the daily dose gives 270.0 cGy. Writing the gray value (50.00) but leaving the unit as cGy gives 50.0 cGy, a 100-fold unit error.

### Q4
Stem: Quiz. Cutout factor used versus measured. The cutout was planned with output factor 0.91, but the measured factor for that cutout is 0.85. The MU were calculated with the planned factor for an intended 220 cGy. Delivered dose = intended × (true factor / factor used), because MU = dose/(calibration × factor × …) and a factor that is too high makes the MU too small. What dose is delivered?
A. 220.0 cGy
B. 235.5 cGy
C. 205.5 cGy
D. 206.8 cGy
Answer: C
Objective: VII.5
Why: Factor ratio = 0.85 / 0.91 = 0.9341. Delivered = 220 × 0.9341 = 205.49 cGy, reported as 205.5 cGy. The patient is underdosed when the factor used in the MU calculation is larger than the true output factor. Assuming the intended dose was delivered gives 220.0 cGy. Inverting the factor ratio gives 235.5 cGy and would claim an overdose. Subtracting the raw factor difference from 1 and multiplying gives 206.8 cGy, which is not how an output factor enters the MU equation.

### Q5
Stem: A gamma pass rate of 88% is below which TG-218 line?
A. It still meets the 95% tolerance
B. It meets the action limit because 88 rounds to 90
C. TG-218 has no action limit
D. The 90% action limit
Answer: D
Objective: VII.5
Why: Tolerance is 95% and the action limit is 90% for the TG-218 universal criteria (3%/2 mm, 10% threshold). 88 is below 90, so this is past the action limit, not a tolerance pass. Correct choice: The 90% action limit. 88 is below 95 and below 90. 88 does not round to 90, and it should not be waved through. The action limit is 90%.

### Q6
Stem: Which statement matches AAMD scope?
A. Dosimetrists set the total dose without a physician
B. Dosimetrists calculate plans and do not independently prescribe
C. Dosimetrists sign TG-51 calibrations as the physicist
D. Dosimetrists may skip documentation if the plan looks good
Answer: B
Objective: VII.6
Why: The scope is plan design and dose calculation under physician and physicist direction, with documentation. It is not an independent prescription. Correct choice: Dosimetrists calculate plans and do not independently prescribe. Prescribing is the physician's role. Calibration is physics. Documentation is part of the standard.

### Q7
Stem: RO-ILS is best used for what?
A. Replacing the NRC as the HDR regulator
B. Calibrating ion chambers
C. Setting the NCRP occupational limit
D. Learning from incidents and near misses
Answer: D
Objective: VII.7
Why: RO-ILS collects events so clinics can change processes. It is voluntary learning, not a calibration service and not a regulator. Correct choice: Learning from incidents and near misses. RO-ILS does not issue radioactive-materials licenses. That is a physics standards-lab chain. The limit comes from NCRP and regulation, not from an incident database.

### Q8
Stem: Daily linac QA in the TG-142 cadence includes which pair?
A. Annual end-to-end SRS only
B. Semiannual source leak test and a written directive
C. Commissioning a new CT-density curve every morning
D. Output constancy and the door interlock
Answer: D
Objective: VII.9
Why: The daily TG-142 highlights are safety (door interlock functional) and dosimetry (x-ray output constancy within 3%). Weekly chart review is a separate clinical cadence. Correct choice: Output constancy and the door interlock. SRS end-to-end is not the daily test. Those are brachytherapy regulatory tasks. The density curve is commissioned, not rebuilt daily.

### Q9
Stem: Quiz. Another chart-check total. The prescription is 150 cGy per fraction for 30 fractions. What is the total dose in cGy?
A. 4350 cGy
B. 180.0 cGy
C. 4500 cGy
D. 45.0 cGy
Answer: C
Objective: VII.2
Why: Total = dose per fraction × number of fractions = 150 × 30 = 4500 cGy, which is 45.00 Gy. Reported in cGy as asked: 4500 cGy. Using one fewer fraction (forgetting the last fraction, or confusing sessions with intervals) gives 4350 cGy. Adding the fraction number to the daily dose gives 180.0 cGy. Writing the gray value (45.00) but leaving the unit as cGy gives 45.0 cGy, a 100-fold unit error.
