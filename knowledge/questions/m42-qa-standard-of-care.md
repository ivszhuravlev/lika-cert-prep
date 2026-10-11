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

### Q6
Stem: Weekly image review. The approved cone-beam shift is 0.4 cm anterior. The couch was moved 0.4 cm posterior before the fraction. Monitor units match the plan. What is the status of that fraction?
A. Not acceptable; the direction is opposite the approved shift, so the isocenter moved the wrong way
B. Acceptable, because the shift size matches and the monitor units match
C. Acceptable, because anterior and posterior moves are the same on a parallel-opposed pair
D. Acceptable if the image window was wide enough to see bone
Answer: A
Objective: VII.2
Why: A 0.4 cm posterior move is not a 0.4 cm anterior move. The isocenter is 0.8 cm from the approved point: 0.4 + 0.4 = 0.8 cm. Matching monitor units does not put the target on the isocenter. Opposed beams do not make a reversed shift harmless, and the window level does not check the sign.

### Q7
Stem: Chart check of an en face electron boost. The approved source-to-skin distance is 100 cm. The treatment note shows the cone at 105 cm. Monitor units are the ones calculated for 100 cm. How should that fraction be treated?
A. As delivered correctly, because electron monitor units do not change with distance
B. As delivered correctly if the cone size matches the plan
C. As a setup miss; the longer distance changes output, and the 100 cm monitor units do not correct it
D. As delivered correctly, because 5 cm is inside a 10 cm setup window for electrons
Answer: C
Objective: VII.2
Why: Output falls as the cone moves away from the patient. A pure inverse-square estimate is (100/105)^2. 100/105 = 0.9524, and 0.9524^2 = 0.907, about 9% low. Electron output also depends on the virtual source, which is not the nominal target, so the true change can differ from 9%, and it is still not the approved dose. The cone size does not restore the distance, and there is no 10 cm convenience window.

### Q8
Stem: Weekly chart check of a lung course approved at 6 MV. Fraction 4 was delivered at 10 MV with the monitor units from the 6 MV plan. The portal image for that fraction was signed. What does the check conclude?
A. The fraction matches, because the image was signed and the monitor units match
B. The fraction matches, because 6 MV and 10 MV share one percent depth dose at midplane
C. The fraction does not match; 10 MV is not the approved energy, and those monitor units are not the approved 6 MV dose
D. The fraction matches if the separation is over 25 cm, because the higher energy is then preferred
Answer: C
Objective: VII.2
Why: Energy is part of the approved plan. The same monitor units at 10 MV are a different output and a different depth dose from 6 MV. A signed portal image can confirm position and still miss the energy. Separation does not rewrite the prescription.

### Q9
Stem: The chest-wall plan uses 0.5 cm of bolus every fraction. Today's record shows the bolus was left off. Monitor units match the bolus calculation. What is the chart-check finding?
A. No finding; bolus is comfort and does not change dose
B. No finding, because the monitor units already included a bolus factor, so the dose is unchanged
C. No finding if the source-to-skin distance was 100 cm
D. A setup miss; without bolus the surface dose is not the dose the plan calculated
Answer: D
Objective: VII.2
Why: Bolus is an accessory in the plan. It pulls buildup to the surface. Monitor units calculated with bolus, delivered without it, underdose the surface and change the depth dose. Agreement on source-to-skin distance does not replace the bolus.

### Q10
Stem: Three prior courses name the cord "cord", "Spinal Cord", and "SpCord". Which name follows TG-263 so a later chart check can find the organ?
A. Keep the three nicknames, because each planner may choose a local label
B. SpinalCord
C. PTV_4500, because every serial organ carries its limit in the name
D. Lungs, because the cord is named with the paired-organ rule
Answer: B
Objective: VII.2
Why: TG-263 uses one camel-case name and no space: SpinalCord. Spaces, abbreviations, and nicknames will not match when prior dose is summed. PTV_4500 is a target name, the structure plus an underscore plus the dose in cGy, not the cord. Lungs is the combined lung volume.

### Q11
Stem: A head-and-neck target is prescribed to 7000 cGy. Which structure name follows TG-263?
A. PTV 7000
B. PTV_70Gy
C. PTV_7000
D. SpinalCord
Answer: C
Objective: VII.2
Why: The target name is the structure, an underscore, and the dose in cGy, with no unit text and no space: PTV_7000. A space, a gray label, or an organ name is a different string. SpinalCord is the cord, not this target.

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

### Q20
Stem: The planning system shows 6 MV for the field. The record-and-verify field is armed for 18 MV. The monitor units match. Is the field ready?
A. Yes; matching monitor units fix the depth dose
B. Yes, if the cone-beam bone match is 0 mm
C. Yes, after the wedge name is cleared
D. No. The field is not ready. Energy is part of the approved plan, and 18 MV is not the planned 6 MV beam
Answer: D
Objective: VII.4
Why: The record-and-verify energy has to be the planning energy. The same monitor units at 18 MV are a different depth dose and a different output from 6 MV. A bone match and a wedge label do not clear an energy mismatch. The field stays off until the armed energy is the approved 6 MV.

### Q21
Stem: Breast tangents were planned with a couch kick of 5.7° so the superior border matches a half-beam supraclavicular field. The superior–inferior length is 20 cm and the SAD is 100 cm. The record-and-verify couch is 0.0°. The collimator matches the plan. The monitor units match. What is the field status?
A. Ready, because the collimator creates the superior match and a couch of 0° is acceptable
B. Ready if the gantry is set to 5.7°, because that angle is the posterior lung border and the couch is not part of the superior match
C. Not ready; the loaded couch is not the approved 5.7° kick, and that kick is what aligns the superior border
D. Ready, because the monitor units match and a 5.7° difference is inside a 10° convenience tolerance
Answer: C
Objective: VII.4
Why: The couch kick uses the superior–inferior length. Half of 20 cm is 10 cm. The ratio 10/100 = 0.10, and arctan(0.10) = 5.71°, reported as 5.7°. That angle takes the superior divergence out of the tangent so the border can meet a half-beam supraclavicular field. The collimator does not create that match, so a collimator that agrees with the plan does not clear a couch of 0°. The posterior border is a gantry angle or a half-beam jaw, not this 5.7° kick, so rotating the gantry to 5.7° is the wrong correction. Matching monitor units does not apply the couch angle, and there is no 10° tolerance that replaces the approved value.

### Q22
Stem: The approved gantry for a posterior field is 180°. The record-and-verify field is armed at gantry 0°. The monitor units match. What should happen?
A. Treat; 0° and 180° deliver the same entrance for a parallel-opposed plan
B. Treat, because the monitor units already include the posterior depth
C. Do not treat; gantry 0° is an anterior entrance and is not the approved posterior field
D. Treat after doubling the monitor units to compensate for the flip
Answer: C
Objective: VII.4
Why: Gantry angle selects which side of the patient the beam enters. 0° and 180° are opposite entrances. Matching monitor units at the wrong gantry treats the wrong path through the patient. Doubling the monitor units is not a geometry correction.

### Q23
Stem: The approved plan is an open 6 MV field with no wedge. The record-and-verify field has a 45° physical wedge in the path. The monitor units match the open-beam calculation. What is the status?
A. Ready, because a wedge with matching monitor units is an open beam
B. Not ready; the wedge is an accessory the plan does not have, and the open-beam monitor units would underdose through it
C. Ready if the wedge factor is typed as 1 at the console without a record
D. Ready, because a 45° wedge has wedge factor 1
Answer: B
Objective: VII.4
Why: The record-and-verify accessory has to match the approved plan. A physical wedge that is not in the plan changes the dose per monitor unit and tilts the distribution. Open-beam monitor units through that wedge underdose the calculation point by about the wedge factor. A 45° angle is not a factor of 1, and an unrecorded edit is not an approved plan change.

### Q24
Stem: An SAD prostate plan lists the anterior source-to-skin distance as 88 cm with the isocenter at 100 cm from the source. Record and verify shows that anterior skin distance as 92 cm. Energy, gantry, and monitor units match. Is the field ready?
A. Yes; SAD plans ignore skin distance
B. Yes, because 4 cm is inside the daily 3% output window
C. No; the skin is not at the planned distance, so the isocenter is not at the planned depth
D. Yes if the collimator angle is 0°
Answer: C
Objective: VII.4
Why: At a fixed source-to-axis distance of 100 cm, a skin distance of 92 cm instead of 88 cm means the surface moved. The isocenter depth changed by 92 − 88 = 4 cm. The monitor units were calculated for the planned depth. Energy and gantry do not correct that, and a percent output tolerance is not a skin-distance tolerance. A collimator of 0° is a different parameter.

### Q25
Stem: Image guidance asks for a couch move of 0.6 cm to the patient's left. The couch was moved 0.6 cm to the patient's right, and the field was then armed. Energy, gantry, and monitor units match. What is the field status?
A. Ready; equal left and right moves cancel across the course
B. Not ready; the shift sign is reversed, and the isocenter is 1.2 cm from the approved point
C. Ready, because the monitor units already contain the shift
D. Ready if the morning laser check was inside 2 mm
Answer: B
Objective: VII.4
Why: The patient needed 0.6 cm left and received 0.6 cm right. The miss is 0.6 + 0.6 = 1.2 cm. Monitor units, energy, and gantry do not move the couch back. A 2 mm laser tolerance is a machine check. It does not authorize a reversed patient shift.

### Q26
Stem: An electron boost was approved on a 10×10 cm cone with a measured cutout. Record and verify has a 15×15 cm cone armed. Monitor units match the 10×10 calculation. The energy matches. What is the status?
A. Ready, because electron cones of one energy share one output
B. Ready, because a larger cone can only increase coverage and not dose
C. Not ready; the cone is an accessory, and these monitor units belong to the 10×10 cone
D. Ready if the cutout factor in the chart is left at 1
Answer: C
Objective: VII.4
Why: Cone size changes electron output. Monitor units computed for the 10×10 cone are the wrong dose per monitor unit on a 15×15 cone. Matching energy does not select the cone. Leaving the cutout factor at 1 without a measurement is not a clearance to treat.

### Q27
Stem: The approved field uses a 30° wedge, and the monitor units use that wedge factor. Record and verify has a 60° wedge in the path. What should happen?
A. Treat; any wedge in the path satisfies a wedged plan
B. Treat, because 60° minus 30° is inside the 1° collimator tolerance
C. Do not treat; a 60° wedge is not the approved accessory, and the 30° monitor units are not the dose through it
D. Treat if the wedge is physical rather than dynamic
Answer: C
Objective: VII.4
Why: The accessory has to be the approved wedge. A 60° wedge has a different transmission from a 30° wedge, so the approved monitor units do not deliver the approved dose. The difference 60 − 30 = 30° is not a collimator-angle error, and the 1° tolerance belongs to gantry and collimator readouts. Physical versus dynamic does not turn 60° into 30°.

### Q28
Stem: A scar boost was planned with 6 MeV electrons. Record and verify is armed for 12 MeV. The cone matches and the monitor units match. What is the field status?
A. Ready, because both energies treat the skin and the cone is correct
B. Not ready; 12 MeV is not the approved energy, and the practical range is about twice as deep
C. Ready, because electron monitor units depend only on the cone
D. Ready if the gantry is 0°
Answer: B
Objective: VII.4
Why: Energy is part of the plan. Practical range in centimeters is about half the nominal energy in MeV: 6/2 = 3 cm and 12/2 = 6 cm. The same monitor units at 12 MeV cover a deeper volume than the approved boost. The cone and the gantry do not select the energy.

### Q29
Stem: The approved photon field is open, with no tray. Record and verify requires a blocking tray and a custom block. Monitor units match the open-beam calculation. What is the status?
A. Ready, because a block only improves conformality and the monitor units can stay open-beam
B. Not ready; the tray and block are accessories the plan does not have, and open-beam monitor units through them are not the approved dose
C. Ready if the block is thinner than 8 cm of Cerrobend
D. Ready, because the tray factor is 1 for every photon energy
Answer: B
Objective: VII.4
Why: A tray and a block change dose per monitor unit. The tray attenuates the beam, and the block removes scatter the open-beam monitor units assumed. Those monitor units do not deliver the approved dose. Block thickness and a guessed tray factor of 1 are not a plan check.

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

### Q6
Stem: Which task is inside the dosimetrist's scope when a physician has already signed the prescription?
A. Designing the beams and calculating the monitor units
B. Replacing the total dose because the cord histogram is hot
C. Signing the annual calibration report as the physicist
D. Waiving a written directive so an HDR fraction can start
Answer: A
Objective: VII.6
Why: Scope includes treatment planning and monitor-unit calculation inside a signed prescription. Changing the total dose is a new prescription. The calibration signature belongs to the physicist. A written directive is not optional.

### Q7
Stem: A vaginal-cuff HDR plan needs dwell times. Who may calculate them, and what may that person not do?
A. The dosimetrist may calculate dwell times under the written directive, and may not choose the prescription dose
B. The dosimetrist may both calculate the dwell times and write the prescription
C. Only the vendor may enter dwell times, and the dosimetrist may not plan brachytherapy
D. The dosimetrist signs the source calibration in place of the physicist, then the dwell times are optional
Answer: A
Objective: VII.6
Why: Brachytherapy planning is in scope. The prescription and the written directive stay with the physician. Source calibration is a physics signature. Calculating the times does not make the dosimetrist the authorized user.

### Q8
Stem: A plan is ready for signatures. Which pair matches the standard of practice?
A. The dosimetrist signs the prescription, and the therapist signs the calibration
B. The physician signs the prescription and the plan approval, and the physicist signs the plan check
C. The record-and-verify import signs both, so no clinical signature is required
D. Continuing-education credits from the past year stand in for both signatures
Answer: B
Objective: VII.6
Why: The physician owns the medical order and the plan approval. The physicist owns the technical plan check and the machine calibration. A DICOM transfer is not a signature. Continuing education maintains the CMD credential. It does not sign the chart.

### Q9
Stem: What does CMD certification require after the exam, and what does it not grant?
A. Nothing further; the certificate is permanent and includes the right to prescribe
B. A radioactive-materials license issued by the regulator, renewed as a source inventory
C. Continuing education on the board's cycle, without transferring the physician's or the physicist's signature
D. A new TG-51 calibration signed by the dosimetrist each year
Answer: C
Objective: VII.6
Why: Certified Medical Dosimetrist is the MDCB credential. Keeping it takes continuing education. The credential does not create an independent prescriber and does not move the calibration or the prescription onto the dosimetrist.

### Q10
Stem: The delivered shift was reversed. Editing the prescription would make the cord dose on the histogram match what was delivered. What is the ethical limit?
A. Edit the prescription so the chart agrees, and leave the event out of the report
B. Report the mismatch and leave any dose change with the physician
C. Sign the physicist's plan check so the fraction can be repeated tonight
D. Delete the image that shows the reversed shift
Answer: B
Objective: VII.6
Why: The ethical limit is an honest record and a prescription the dosimetrist does not rewrite. Hiding the shift is outside scope. A repeated fraction and a dose change are the physician's decision. The physicist's signature is not the dosimetrist's to apply.

### Q11
Stem: Which set of duties sits with planning inside dosimetry practice?
A. Prescribing the dose, signing TG-51, and waiving chart checks
B. Simulation setup, documentation, teaching, and participation in the checks a physicist assigns
C. Monitor units only, with simulation and education excluded
D. Source leak tests signed in place of the radiation safety officer
Answer: B
Objective: VII.6
Why: Scope includes simulation, documentation, education, and quality-assurance participation, along with planning and monitor units. Prescribing, the calibration signature, and skipping the chart check are outside that work. A leak-test signature stays with radiation safety, not with the dosimetrist in place of the safety officer.

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

### Q6
Stem: A reversed couch shift is scored as severe, uncommon, and hard to detect. How does a TG-100 failure-mode analysis use that score?
A. Drop the mode, because uncommon events are not reviewed
B. Multiply severity, occurrence, and detectability, and fix a high product before adding another generic output test
C. Add only a daily door-interlock test, because every high score is an interlock problem
D. Lower the detectability number by agreeing not to review images
Answer: B
Objective: VII.7
Why: The risk priority number is severity × occurrence × detectability. Detectability is scored high when the miss is unlikely to be caught. A high product is where the clinic changes the process, for example with a forced shift check or a second signature. An unrelated interlock test does not catch a reversed shift, and deciding not to look makes detection worse.

### Q7
Stem: One failure mode is scored severity 8, occurrence 2, and detectability 7. A second mode is scored 4, 4, and 4. Which comparison follows failure-mode and effects analysis?
A. The first mode ranks higher, with a risk priority number of 112 against 64
B. The first mode ranks higher because the scores add to 17, which beats 12
C. The modes are equal because each list has three scores
D. The second mode ranks higher because occurrence is the only factor and 4 is greater than 2
Answer: A
Objective: VII.7
Why: The risk priority number is the product of the three scores. First mode: 8 × 2 = 16, and 16 × 7 = 112. Second mode: 4 × 4 = 16, and 16 × 4 = 64. The higher product is the earlier process fix. Adding gives 8 + 2 + 7 = 17 against 4 + 4 + 4 = 12, which is a different combination and not the analysis. Occurrence alone would ignore a severe miss that is hard to detect.

### Q8
Stem: A course prescribed as 5000 cGy was delivered as 6100 cGy. The patient and the site were correct. Which statement fits a medical-event review?
A. The excess divided by the delivered dose is about 18%, so the 20% line is not met
B. The excess is 22% of the prescribed total, past the about-20% total-dose line
C. A medical event on dose requires a single fraction 50% high, and the course total does not count
D. A voluntary incident system replaces the telephone report to the regulator
Answer: B
Objective: VII.7
Why: The baseline is the prescription. (6100 − 5000) / 5000 = 1100/5000 = 0.22 = 22%, past about 20% of the total prescribed dose. Dividing by the delivered dose instead gives 1100/6100 = 0.180 = 18% and uses the wrong baseline. The absolute difference, 11 Gy, is also well above a 0.5 Sv organ threshold, so that threshold does not remove the event. A 50% single-fraction miss is a separate line. A voluntary learning report does not replace the regulatory report.

### Q9
Stem: One fraction prescribed as 200 cGy is delivered as 340 cGy. Later fractions stay on the original plan, and the running total is still inside 20% of the course prescription. How does the single-fraction rule apply?
A. It does not apply, because the course total has not moved by 20%
B. It applies; this fraction is 70% above the prescribed fraction, past the about-50% line
C. It applies only when the patient was the wrong person
D. It does not apply, because the excess divided by the delivered fraction is about 41%, under 50%
Answer: B
Objective: VII.7
Why: The baseline is the prescribed fraction. (340 − 200) / 200 = 140/200 = 0.70 = 70%, past about 50% of that fraction. Dividing by the delivered fraction gives 140/340 = 0.412 = 41% and uses the wrong baseline. The course can still be inside 20% of the total and this fraction can still qualify. Wrong patient is a different medical-event case.

### Q10
Stem: A medical event is discovered Tuesday afternoon. Which clock matches 10 CFR 35.3045?
A. A written report within 24 hours and no telephone call
B. A telephone report within about 15 days and a written report within a year
C. A telephone report within about 24 hours, and a written report within about 15 days
D. No regulatory report if the case is also entered in a voluntary learning system
Answer: C
Objective: VII.7
Why: The regulator is told by telephone within about 24 hours of discovery, by the next calendar day, and receives a written report within about 15 days. The referring physician and the patient are notified as well. A voluntary system does not replace that report.

### Q11
Stem: Patient A's approved plan is delivered to patient B. The monitor units matched patient A's chart. Which description fits 10 CFR 35.3045?
A. Not a medical event, because the monitor units matched a signed plan
B. Not a medical event unless patient B's dose also differed by 20% from patient A's prescription
C. A medical event; the dose went to the wrong patient
D. A daily output failure, because only a calibration miss can be a medical event
Answer: C
Objective: VII.7
Why: Wrong patient is a medical event even when the beam parameters matched some approved plan. The 20% dose line is for a dose difference on the intended administration. It is not a requirement that the wrong person also fail a percentage test against the other chart. Output constancy is a machine check, not this event.

### Q12
Stem: A pelvis plan is delivered to the thorax. Energy, monitor units, and the wedge match the pelvis field. What is the regulatory description?
A. Not a medical event, because the field parameters matched the plan that was loaded
B. A medical event; the dose went to the wrong site
C. In tolerance, because a site change is covered by the 2 mm laser allowance
D. A voluntary near miss only, with no telephone report
Answer: B
Objective: VII.7
Why: Wrong site is a medical event. Matching the pelvis energy, monitor units, and wedge shows the wrong plan was delivered as loaded. It does not make the thorax the prescribed site. A laser tolerance is a machine geometric check. Discovery still starts the telephone report within about 24 hours and the written report within about 15 days.

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

### Q6
Stem: Morning checks on an IMRT linac: lasers are 1.8 mm from the isocenter marks, and output is 1.2% from baseline. Which reading matches TG-142?
A. Both pass; IMRT lasers are allowed 2 mm and output is allowed 3%
B. Lasers fail the 1.5 mm IMRT tolerance, and output passes the 3% daily window
C. Output fails, because a laser miss automatically voids the 1% annual calibration
D. Lasers pass, because they share the 2 mm optical-distance tolerance
Answer: B
Objective: VII.9
Why: Daily IMRT lasers are 1.5 mm. 1.8 mm is over that tolerance and under the 2 mm non-IMRT number, which is the wrong class of machine. Daily output constancy is 3%, and 1.2% is inside it. The annual 1% calibration is a different check, and the optical distance indicator is not the laser tolerance.

### Q7
Stem: A stereotactic unit's daily laser check is 1.2 mm off the isocenter. Output constancy is 0.8%. What is the laser result?
A. Pass; SRS lasers use the 2 mm non-IMRT tolerance
B. Pass; SRS lasers use the 1.5 mm IMRT tolerance
C. Fail; SRS lasers are held to 1 mm
D. Pass, because 1.2 mm is inside the 2 mm light-versus-radiation tolerance
Answer: C
Objective: VII.9
Why: The SRS laser tolerance is 1 mm. 1.2 mm fails it. The 2 mm and 1.5 mm numbers belong to non-IMRT and IMRT units. Light-versus-radiation coincidence is a different test. Output at 0.8% does not clear the laser.

### Q8
Stem: At isocenter the light field edge and the radiation field edge differ by 3 mm. Jaw readout and gantry angle are inside their own tolerances. What fails?
A. Nothing; light and radiation may differ by 5 mm
B. The gantry, because a 3 mm light miss is scored as 3°
C. Light-and-radiation coincidence; the tolerance is 2 mm
D. Nothing on a monthly check; this comparison is only an annual calibration
Answer: C
Objective: VII.9
Why: Light-field and radiation-field coincidence is 2 mm. A 3 mm difference fails. The jaw and the gantry can pass on the same check. A millimeter is not converted into a degree, and the comparison is not reserved for the TG-51 day.

### Q9
Stem: A symmetric jaw sits 3 mm from the set position. The collimator angle indicator is 0.4° from the mechanical angle. Which parameter fails?
A. The collimator angle; 0.4° is over the 1° tolerance
B. The jaw; jaw position is 2 mm, while 0.4° is inside the 1° angle tolerance
C. Both, because jaw and angle share a 1 mm rule
D. Neither; jaws are allowed 5 mm and angles are allowed 2°
Answer: B
Objective: VII.9
Why: Symmetric jaw position is 2 mm, so 3 mm fails. Gantry and collimator angle indicators are 1°, so 0.4° passes. The two tolerances are not interchangeable, and 5 mm or 2° is looser than this report.

### Q10
Stem: The gantry indicator reads 90.0° when the mechanical check is 91.4°. Output is 1% from baseline. What is the angle result?
A. Pass; gantry angle is allowed 2°
B. Pass; 1.4° is covered by the 2 mm laser tolerance
C. Fail; gantry and collimator angle indicators are held to 1°
D. Fail only because the output has used up the 1% annual budget
Answer: C
Objective: VII.9
Why: 91.4 − 90.0 = 1.4°, which is past 1°. The laser tolerance is a length, not an angle. Output at 1% is its own check and does not decide the gantry indicator.

### Q11
Stem: A picket-fence image shows one leaf pair jogged out of an otherwise straight fence. Morning output is inside 3%. What follows?
A. The MLC is cleared, because output constancy includes leaf position
B. The fence has found a leaf-position error, and a passing output does not clear it
C. The fence is a CT-number test, so the simulator density table is rebuilt
D. A jog is the commissioned tongue-and-groove and is ignored
Answer: B
Objective: VII.9
Why: The picket fence is the MLC leaf-position check. A jog means a leaf is not on the line the plan will use. Daily output does not measure that leaf. The image is not a Hounsfield check, and tongue-and-groove is not a reason to accept a broken fence. Patient-specific IMRT QA remains a separate measurement.

### Q12
Stem: Monthly photon profile constancy: flatness has moved 1.6% from baseline and symmetry has moved 0.4%. What is the call?
A. Both pass; flatness and symmetry are allowed 3%, the same as daily output
B. Flatness fails the 1% tolerance and symmetry passes
C. Both fail, because symmetry is held to 0.2%
D. Both pass; 1% is only the annual absolute-dose tolerance and does not apply to profiles
Answer: B
Objective: VII.9
Why: Flatness and symmetry are 1%. 1.6% fails and 0.4% passes. The 3% figure is daily output constancy, not the profile. The annual 1% absolute dose is a calibration comparison, not a reason to ignore a monthly profile.

### Q13
Stem: Annual radiation-isocenter coincidence is 1.6 mm on a conventional linac and 1.2 mm on an SRS linac. Which machine fails?
A. The conventional linac only
B. The SRS linac only
C. Both
D. Neither
Answer: B
Objective: VII.9
Why: Conventional radiation isocenter is 2 mm, so 1.6 mm passes. SRS radiation isocenter is 1 mm, so 1.2 mm fails. The two machines do not share one tolerance.

### Q14
Stem: On an SBRT unit the imaging isocenter and the treatment isocenter differ by 1.4 mm. A conventional linac in the same clinic measures 1.7 mm on the same test. Which unit fails the imaging-to-treatment check?
A. The SBRT unit only
B. The conventional linac only
C. Both
D. Neither, because both are inside 2 mm and SBRT uses the 2 mm number
Answer: A
Objective: VII.9
Why: Imaging-to-treatment isocenter is at or under 2 mm, and at or under 1 mm for SRS/SBRT. The SBRT result of 1.4 mm fails the 1 mm line. The conventional result of 1.7 mm is inside 2 mm. Using 2 mm for the SBRT unit is the wrong machine class.

### Q15
Stem: A Winston–Lutz test places the ball 1.3 mm from the center of the radiation field. How is that scored?
A. Pass; the limit is 2 mm, the same as a conventional radiation isocenter
B. Fail; Winston–Lutz is at or under 1 mm
C. Pass; the test only confirms that the door interlock opens
D. Fail only when the ball is also more than 40 HU from water
Answer: B
Objective: VII.9
Why: Winston–Lutz compares a ball at isocenter with the radiation field over several angles. The offset limit is at or under 1 mm, so 1.3 mm fails. The 2 mm conventional isocenter tolerance is a different check. The test is not a door interlock and not a CT-number test.

### Q16
Stem: The annual wedge-factor check is 2.7% from the commissioned value. The same day's absolute output is 0.6% from the TG-51 standard. What fails?
A. Output; annual absolute dose is allowed only 0.2%
B. The wedge factor; constancy is 2%, and output passes the 1% annual tolerance
C. Both
D. Neither; a wedge factor may drift 5% if output is inside 1%
Answer: B
Objective: VII.9
Why: Wedge-factor constancy is 2%, so 2.7% fails. Annual absolute output is about 1%, so 0.6% passes. A passing calibration does not clear the wedge, and 5% is looser than the wedge tolerance.

### Q17
Stem: Monthly electron energy, taken from the depth of the energy index, has moved 3 mm from baseline. Output constancy that morning is 1.5%. What fails?
A. Output; electrons are held to 1% every month
B. Nothing; electron energy may move 5 mm, and 1.5% is inside the 2% monthly output window
C. Electron energy; the tolerance is 2 mm or 2%
D. Both, because any energy shift fails output automatically
Answer: C
Objective: VII.9
Why: Monthly electron energy is 2 mm or 2%. A 3 mm shift fails. Monthly output constancy is about 2%, so 1.5% passes and does not decide the energy. A 5 mm allowance is looser than the energy rule.

### Q18
Stem: The CT simulator's morning water scan reads +40 HU. Lasers meet at the imaging plane and the couch index matches the scale. What has failed?
A. Nothing; water is defined as +40 HU
B. The lasers, because a Hounsfield error means the lasers moved
C. HU constancy; water should sit near 0 HU, and the densities sent to planning will be high
D. The couch, because Hounsfield units are the couch-travel test
Answer: C
Objective: VII.9
Why: TG-66 holds water near 0 HU, on the order of 5 HU. A reading of +40 is well outside that. Tissue is assigned a density that is too high, and the dose calculation follows. Lasers and the couch can pass on the same morning. They do not measure the CT number.

### Q19
Stem: Water reads 1 HU and the simulator lasers agree with the imaging plane. The couch index used for shifts is 4 mm longer than the position in the scan. Which TG-66 item failed?
A. HU constancy
B. The lasers
C. The couch; indexed travel does not match the position the plan will use
D. None; TG-66 does not include the couch, and 4 mm is inside a 1 cm setup habit
Answer: C
Objective: VII.9
Why: Water at 1 HU is near 0, so HU constancy passes. Lasers on the imaging plane pass. Couch indexing is its own TG-66 check. A 4 mm index error moves every shift written from that scan. There is no 1 cm couch allowance in that check.

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
