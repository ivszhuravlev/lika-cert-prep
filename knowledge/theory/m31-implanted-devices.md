# Module 31. Implanted Devices

The exam groups pacemakers and defibrillators with other hardware: glucose monitors, fiducials, prostheses, and spacer gel. The cardiac device question is a planning-behavior question. The numeric dose categories live in AAPM TG-203. This note does not replace that report and does not state one dose that is safe for every generator.

## Pacemakers

**MDCB objectives:** III.13, I.5

**What the exam expects**

You can list the planning behaviors TG-203 is used for: keep the device out of the direct beam, prefer photon energies of 10 MV and below so photoneutrons are not produced, estimate the dose the device will receive, and have the device interrogated. You know dose thresholds are device-specific. You refuse a single universal pacemaker dose limit. Older teaching quoted one gray value for every generator. TG-203 replaced that habit with a risk-based report that combines how dependent the patient is on the device with the dose the device is expected to receive. The category boundaries and the actions that follow from them are in the report. Confirm them there.

**Core facts**

A pacemaker or an implantable defibrillator can be affected by ionizing dose and by neutrons. Neutrons are the reason energy matters even when the device is outside the field. Photoneutron production in the linac head becomes relevant above about 10 MV. Those neutrons can upset electronics and reset or scramble a device that never saw the direct beam. The planning rule the exam tests is: prefer 10 MV or lower so that neutron component is avoided. Do not choose 15 MV or 18 MV for a deep parallel-opposed pair and call the device safe because it is 5 cm outside the light field.

Keep the device out of the direct beam. A beam that clips the generator is the wrong beam arrangement if any other arrangement can cover the target. If the anatomy truly forces dose toward the device, that is a high-attention case: the dose has to be estimated, and the device team has to be involved before treatment, not after a malfunction.

Interrogate the device. Cardiology or the device clinic checks function before treatment and as TG-203 and the vendor direct during and after the course. Have a plan for a patient who is dependent on pacing, including what happens if the device misbehaves during a fraction. An ICD can also deliver a shock if it interprets noise as an arrhythmia. Programming changes are the device team’s decision. The dosimetry decision is beam, energy, and an honest dose estimate.

Estimate the dose with the treatment-planning system, plus in-vivo measurement when the device is close. Out-of-field dose is a weak point of many algorithms. A calculation that says 0 Gy because the device contour is outside the dose grid is not an estimate. Extend the grid or measure. The number you compare with TG-203 is that estimate, for that device, for that course. It is not a number memorized in place of the report.

The report’s management actions scale with risk: observation and interrogation at the low end, more intensive monitoring and possible relocation or scheduling changes when the patient is dependent or the expected dose is higher. Quote the action from TG-203 for the category the dose and the dependence put the patient in. Do not answer “2 Gy is always the limit” or “5 Gy is always safe.” Those figures are not a universal ceiling you can apply to every manufacturer.

Other electronic implants follow the same behaviors even when TG-203 itself is written for cardiac devices. Insulin pumps and continuous glucose monitors are electronics. Keep them out of the direct beam, avoid high-energy neutrons, and follow the vendor’s instruction, which often means removing a pump or a sensor before treatment. Cochlear implants, deep brain stimulators, and pain pumps are the same class of problem: out of the primary beam, energy choice, vendor guidance, and a documented check. Do not invent a gray limit for them.

**Fiducials.** Gold or carbon markers implanted in the prostate or the liver are localization surrogates. They are not the GTV. Match to them when the protocol says they represent the target. A bony match can look fine while the fiducials, and the prostate, have moved. The markers are high-Z and small. They perturb dose locally. They are not a reason to raise the photon energy.

**Prostheses.** A hip replacement is high-Z metal. The CT streak is not the true density, and an uncorrected Hounsfield number will be the wrong input to the dose engine. Override the density inside the metal to the value your commissioning report specifies for that implant, and be honest about the artifact in the soft tissue around it. Beam angles straight through the prosthesis are a calculation problem, especially for a pencil-beam algorithm. Monte Carlo handles the interface better than a pencil beam. Prefer directions that still cover the target and that the algorithm can support. Confirm the override procedure in the TPS commissioning report. There is no single HU number in this note, on purpose.

**Spacer gel.** A hydrogel injected between the prostate and the rectum increases the gap. Contour it as its own structure. It is not rectum and it is not prostate. Its CT density is near water or soft tissue; do not override it as air or as metal. The gel can shift or be absorbed over the course of treatment. A gap that shrinks is a geometry change and belongs in the adaptive conversation. A plan that met a rectal constraint only because of a 1 cm spacer does not still meet it when the spacer is gone.

**Formulas**

There is no universal dose equation for a pacemaker. The arithmetic you do have is the energy rule and the geometry of “outside the field,” which is not the same as “zero dose.”

If a stem gives a device dose and a category table taken from TG-203, apply that table exactly as printed. If the stem gives only “the patient has a pacemaker and the beams are 18 MV,” the tested response is the behavior: high energy produces neutrons, neutrons can upset the device outside the field, and the energy should be 10 MV or below unless a qualified reason and the report say otherwise.

Out-of-field falloff is not inverse square from the isocenter alone. Scatter and leakage dominate outside the aperture. Do not compute device dose as a point-source inverse-square problem unless the stem tells you that model applies.

**Traps**

- One gray limit for every pacemaker and every ICD.
- 18 MV excused because the generator is outside the jaw opening.
- A dose of zero taken from a grid that does not reach the device.
- Fiducials contoured as GTV, or a spacer contoured as rectum.
- A hip prosthesis left at the streak Hounsfield number.
- A glucose sensor ignored because the question said “pacemaker” in the module title and the stem said “CGM.”

**Sources**

- AAPM TG-203, management of radiotherapy patients with implanted cardiac pacemakers and defibrillators. Category boundaries, dose levels, and actions: confirm in the report.
- Vendor instructions for the specific generator, pump, or sensor
- TPS commissioning documentation for prosthesis density overrides

## Implanted Devices Mini-Quiz

**MDCB objectives:** III.13

**Skills this quiz trains**

- Keep the generator out of the direct beam.
- Prefer ≤ 10 MV so photoneutrons are not produced.
- Require interrogation and a real dose estimate, including out-of-field dose.
- Decline a universal pacemaker dose. Point to TG-203.
- Classify fiducial, prosthesis, spacer, and CGM, and state the planning behavior for each.
- Override prosthesis density per commissioning practice, and contour spacer gel as neither rectum nor prostate.

**Traps**

- “2 Gy for every device.”
- Neutrons forgotten once the MLC covers the generator.
- Algorithm out-of-field dose of 0 Gy trusted.
- Spacer or fiducial assigned to the wrong structure.
- Streak artifact used as the hip density.

**Check yourself**

A pelvic plan uses 18 MV laterals. A pacemaker sits in the left chest, well outside the jaws. What is the neutron problem, and what energy behavior does the exam want? The same patient has a hydrogel spacer and bilateral hip prostheses. What is each contour for?

Walk-through: Above about 10 MV the head produces photoneutrons that can upset the device even outside the beam. Prefer 10 MV or below, keep the device out of the direct beam, estimate dose, and interrogate. The spacer is its own structure between prostate and rectum. The hips are metal: override density per the commissioning report and do not pretend the streak is tissue or the true metal HU without that procedure. Dose categories for the pacemaker come from TG-203 for this patient, not from a single memorized gray value.
