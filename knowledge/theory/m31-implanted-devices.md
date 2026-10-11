# Module 31. Implanted Devices

The exam groups pacemakers and defibrillators with other hardware: glucose monitors, fiducials, prostheses, and spacer gel. The cardiac device question is a planning-behavior question and a category question. AAPM TG-203 is the report. On this exam the dose bands are low under 2 Gy, intermediate from 2 Gy through 5 Gy, and high above 5 Gy. A pacing-dependent patient moves up one category. Beams above 10 MV add neutrons and are managed as high risk. Historical TG-34 is often cited for 2 Gy. That figure is not a dose that is always safe.

## Pacemakers

**MDCB objectives:** III.13, I.5

**What the exam expects**

You can list the planning behaviors TG-203 is used for: keep the device out of the direct beam, prefer photon energies of 10 MV and below so photoneutrons are not produced, estimate the dose the device will receive, and have the device interrogated before treatment and after the course. You can place that estimate in the teaching bands: low under 2 Gy, intermediate from 2 Gy through 5 Gy (2 Gy and 5 Gy themselves are intermediate), and high above 5 Gy. You then move a pacing-dependent patient up one category. A patient already in the high band stays high. You treat a beam above 10 MV as high risk because of neutrons, even when the gray value would have been a lower band. You do not call 2 Gy safe for every patient. Historical TG-34 is the older single-number citation of 2 Gy. TG-203 replaced that habit. A pacing-dependent patient, or a plan above 10 MV, is not cleared by a dose under 2 Gy.

**Core facts**

A pacemaker or an implantable defibrillator can be affected by ionizing dose and by neutrons. Neutrons are the reason energy matters even when the device is outside the field. Photoneutron production in the linac head becomes relevant above about 10 MV. Those neutrons can upset electronics and reset or scramble a device that never saw the direct beam. The planning rule the exam tests is: prefer 10 MV or lower so that neutron component is avoided. Do not choose 15 MV or 18 MV for a deep parallel-opposed pair and call the device safe because it is 5 cm outside the light field.

Keep the device out of the direct beam. A beam that clips the generator is the wrong beam arrangement if any other arrangement can cover the target. If the anatomy truly forces dose toward the device, that is a high-attention case: the dose has to be estimated, and the device team has to be involved before treatment, not after a malfunction.

Interrogate the device. Cardiology or the device clinic checks function before treatment and as TG-203 and the vendor direct during and after the course. Have a plan for a patient who is dependent on pacing, including what happens if the device misbehaves during a fraction. An ICD can also deliver a shock if it interprets noise as an arrhythmia. Programming changes are the device team’s decision. The dosimetry decision is beam, energy, and an honest dose estimate.

**Dose categories.** The bands this exam teaches are low under 2 Gy, intermediate from 2 Gy through 5 Gy, and high above 5 Gy. The same bands apply to a pacemaker and to a defibrillator. Read the band from the estimated dose to the generator for the whole course, then apply pacing dependence. A patient who is not dependent stays in the band the dose names. A pacing-dependent patient moves up one category: under 2 Gy becomes intermediate, and 2 Gy through 5 Gy becomes high. Above 5 Gy the category is high whether or not the patient is dependent. There is no category above high.

Neutrons sit on top of the dose band. Photoneutron production in the linac head is the reason energies above 10 MV are avoided. TG-203 manages that neutron-producing irradiation as high risk, including when the estimated dose is under 2 Gy. The planning response is still to use 10 MV or below. Do not keep 15 MV or 18 MV because the calculated dose sits in the low band or because the generator is outside the jaws.

TG-34 is the older report. Reviews still cite it for a 2 Gy pacemaker limit. TG-203 replaced that single number with the three bands plus dependence. Use 2 Gy as the historical citation and as the start of the intermediate band, not as proof that every patient at or under 2 Gy is safe. Vendor limits can be tighter than the band. The out-of-field estimate can be wrong. Dependence or neutrons can move the patient out of the band the gray value suggested. Do not answer that 2 Gy is always safe, or that 5 Gy is always safe.

Estimate the dose with the treatment-planning system, plus in-vivo measurement when the device is close. Out-of-field dose is a weak point of many algorithms. A calculation that says 0 Gy because the device contour is outside the dose grid is not an estimate. Extend the grid or measure. The number you place in the band is that estimate, for that device, for that course.

Management scales with the category. The low end is observation and interrogation before and after the course. A higher category, from dose, from pacing dependence, or from neutrons, brings more intensive monitoring and, when the anatomy forces a high dose, a conversation about relocating the device or changing the schedule. Interrogation is not cancelled because the band is low. The generator still stays out of the direct beam in every band. Programming changes remain the device team's decision.

Other electronic implants follow the same behaviors even when TG-203 itself is written for cardiac devices. Insulin pumps and continuous glucose monitors are electronics. Keep them out of the direct beam, avoid high-energy neutrons, and follow the vendor’s instruction, which often means removing a pump or a sensor before treatment. Cochlear implants, deep brain stimulators, and pain pumps are the same class of problem: out of the primary beam, energy choice, vendor guidance, and a documented check. Do not invent a gray limit for them.

**Fiducials.** Gold or carbon markers implanted in the prostate or the liver are localization surrogates. They are not the GTV. Match to them when the protocol says they represent the target. A bony match can look fine while the fiducials, and the prostate, have moved. The markers are high-Z and small. They perturb dose locally. They are not a reason to raise the photon energy.

**Prostheses.** A hip replacement is high-Z metal. The CT streak is not the true density, and an uncorrected Hounsfield number will be the wrong input to the dose engine. Override the density inside the metal to the value your commissioning report specifies for that implant, and be honest about the artifact in the soft tissue around it. Beam angles straight through the prosthesis are a calculation problem, especially for a pencil-beam algorithm. Monte Carlo handles the interface better than a pencil beam. Prefer directions that still cover the target and that the algorithm can support. Confirm the override procedure in the TPS commissioning report. There is no single HU number in this note, on purpose.

**Spacer gel.** A hydrogel injected between the prostate and the rectum increases the gap. Contour it as its own structure. It is not rectum and it is not prostate. Its CT density is near water or soft tissue; do not override it as air or as metal. The gel can shift or be absorbed over the course of treatment. A gap that shrinks is a geometry change and belongs in the adaptive conversation. A plan that met a rectal constraint only because of a 1 cm spacer does not still meet it when the spacer is gone.

**Formulas**

There is no universal dose equation for a pacemaker. The arithmetic you do have is the energy rule and the geometry of “outside the field,” which is not the same as “zero dose.”

If a stem gives a device dose, place it in the band first: under 2 Gy is low, 2 Gy through 5 Gy is intermediate, and above 5 Gy is high. Then move a pacing-dependent patient up one category. If the energy is above 10 MV, neutrons make the case high risk even when the dose band was lower. If the stem gives only “the patient has a pacemaker and the beams are 18 MV,” the tested response is the behavior: high energy produces neutrons, neutrons can upset the device outside the field, and the energy should be 10 MV or below.

Out-of-field falloff is not inverse square from the isocenter alone. Scatter and leakage dominate outside the aperture. Do not compute device dose as a point-source inverse-square problem unless the stem tells you that model applies.

**Traps**

- One gray limit for every pacemaker and every ICD, or the sentence “2 Gy is always safe.”
- A dose of 2 Gy placed in the low band. On this exam 2 Gy starts the intermediate band.
- A pacing-dependent patient left in the band the dose alone would name.
- 18 MV excused because the generator is outside the jaw opening, or because the estimate is under 2 Gy.
- A dose of zero taken from a grid that does not reach the device.
- Fiducials contoured as GTV, or a spacer contoured as rectum.
- A hip prosthesis left at the streak Hounsfield number.
- A glucose sensor ignored because the question said “pacemaker” in the module title and the stem said “CGM.”

**Sources**

- AAPM TG-203, management of radiotherapy patients with implanted cardiac pacemakers and defibrillators. Bands used here: low under 2 Gy, intermediate 2 Gy through 5 Gy, high above 5 Gy. Pacing dependence moves the patient up one category. Neutrons from beams above 10 MV are high risk.
- AAPM TG-34, the older pacemaker report, often cited for 2 Gy. That citation is not the TG-203 category system, and 2 Gy is not a dose that is always safe.
- Vendor instructions for the specific generator, pump, or sensor
- TPS commissioning documentation for prosthesis density overrides

## Implanted Devices Mini-Quiz

**MDCB objectives:** III.13

**Skills this quiz trains**

- Place the estimated device dose: low under 2 Gy, intermediate from 2 Gy through 5 Gy, high above 5 Gy.
- Move a pacing-dependent patient up one category. Do not call 2 Gy always safe. Remember TG-34 as the historical 2 Gy citation, not as the current system.
- Treat beams above 10 MV as neutron-producing and high risk.
- Keep the generator out of the direct beam in every band.
- Prefer ≤ 10 MV so photoneutrons are not produced.
- Require interrogation before and after, and a real dose estimate, including out-of-field dose.
- Classify fiducial, prosthesis, spacer, and CGM, and state the planning behavior for each.
- Override prosthesis density per commissioning practice, and contour spacer gel as neither rectum nor prostate.

**Traps**

- “2 Gy is always safe,” or one gray limit for every device.
- A pacing-dependent patient left in the low band.
- Neutrons forgotten once the dose is under 2 Gy or the MLC covers the generator.
- Algorithm out-of-field dose of 0 Gy trusted.
- Spacer or fiducial assigned to the wrong structure.
- Streak artifact used as the hip density.

**Check yourself**

A pelvic plan uses 18 MV laterals. A pacemaker sits in the left chest, well outside the jaws. The estimate, once the grid reaches the device, is 1.2 Gy. The patient is pacing dependent. What is the neutron problem, what energy does the exam want, and what category applies? The same patient has a hydrogel spacer and bilateral hip prostheses. What is each contour for?

Walk-through: Above 10 MV the head produces photoneutrons. That neutron exposure is high risk even though 1.2 Gy is under 2 Gy, so the energy comes down to 10 MV or below. On a 6 MV plan the same 1.2 Gy is the low band for a patient who is not pacing dependent, and intermediate for this pacing-dependent patient, one category up. Two gray is the historical TG-34 citation and the start of the intermediate band, not a dose that is always safe. Keep the device out of the direct beam, estimate dose with a grid that reaches it, and interrogate before and after. The spacer is its own structure between prostate and rectum. The hips are metal: override density per the commissioning report and do not pretend the streak is tissue or the true metal HU without that procedure.
