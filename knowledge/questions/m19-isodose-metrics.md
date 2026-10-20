# Module 19 — Isodose distributions and dose metrics

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

Rules used in the electron items, stated so the arithmetic can be checked:

- Khan: 90% depth ≈ E/3.2 cm, 80% depth ≈ E/2.8 cm, practical range Rp ≈ E/2 cm.
- Bentel: 90% depth ≈ E/4 cm, 80% depth ≈ E/3 cm.
- Energy loss in water ≈ 2 MeV/cm.
- E is the nominal energy in MeV and depths are in centimeters of water.

## Electrons 101

### Q1
Stem: A 16 MeV electron beam travels through 4.0 cm of water. Using the rule of thumb that electrons lose about 2 MeV per centimeter in water, about how much energy remains?
A. 16 MeV, because energy loss applies only in lead
B. 12 MeV, because the loss is 1 MeV per centimeter
C. 8 MeV
D. 4 MeV, because the practical range consumes the whole beam at E/4
Answer: C
Objective: I.3
Why: Answer C. Multiply path length by the rule-of-thumb stopping rate: 4.0 cm × 2 MeV/cm = 8 MeV removed. Remaining energy is 16 − 8 = 8 MeV. This is an average clinical approximation; the spectrum is broad and the most probable energy falls roughly linearly, but the exam arithmetic is 2 MeV/cm. A loss of 1 MeV/cm would leave 12 MeV, which is not the rule. The E/4 depth is Bentel's approximate 90% dose depth, not the depth where energy reaches zero. Energy is essentially exhausted near the practical range, which for 16 MeV is about 8 cm, not 4 cm.

### Q2
Stem: Using Rp ≈ E/2, what is the practical range of a 15 MeV electron beam in water, and what does that range mean?
A. 7.5 cm; beyond this depth the electron dose has fallen to the bremsstrahlung tail
B. 7.5 cm; this is the depth of the 90% isodose
C. 3.75 cm; this is the depth where half the energy remains
D. 30 cm; practical range is 2E
Answer: A
Objective: I.3
Why: Answer A. E/2 for 15 MeV is 15/2 = 7.5 cm. The practical range is where the electron percent-depth-dose curve, extrapolated, meets the bremsstrahlung tail. Past that depth the remaining dose is photon contamination, not electrons. Bentel's 90% depth would be 15/4 = 3.75 cm. Khan's 90% depth is 15/3.2 ≈ 4.7 cm. Answer C uses Bentel's 90% number for the wrong endpoint. Doubling the energy gives a photon-like path, not an electron range.

### Q3
Stem: For a 12 MeV beam, what 90% depth and what 80% depth does Khan's rule predict?
A. 90% at 4.0 cm and 80% at 3.0 cm
B. 90% at 3.0 cm and 80% at 4.0 cm
C. 90% at 6.0 cm and 80% at 12 cm
D. 90% at 3.75 cm and 80% at 4.3 cm
Answer: D
Objective: I.3
Why: Answer D. Khan places the 90% isodose at E/3.2 and the 80% isodose at E/2.8. For 12 MeV, 12/3.2 = 3.75 cm and 12/2.8 ≈ 4.3 cm. The 80% point is deeper than the 90% point because percent depth dose is falling on the distal side of the electron curve. Answer B is Bentel: E/4 = 3.0 cm and E/3 = 4.0 cm. Answer A swaps Bentel's two depths. Answer C uses E/2 and E, which are not the therapeutic isodoses.

### Q4
Stem: How does surface dose of an electron beam change as the nominal energy is raised from 6 MeV to 20 MeV?
A. Surface dose falls, the same way skin sparing improves for higher-energy photons
B. Surface dose rises; a 6 MeV beam may be near 70 to 80 percent at the surface, while a 20 MeV beam is often near 90 percent or higher
C. Surface dose is 100% at every electron energy because dmax is always on the skin
D. Surface dose is zero until a bolus of E/2 cm is added
Answer: B
Objective: I.3
Why: Answer B. Electrons do not behave like megavoltage photons. Low-energy electrons scatter at large angles and many are scattered out of the beam before they deposit dose at depth, so the surface is relatively lower and dmax is a bit deeper as a fraction of the range. As energy rises, scattering angles tighten, more dose is deposited near the entrance, and the surface dose climbs. It is still not exactly 100% at the surface for clinical beams, so bolus is used when the skin itself must be at full dose. Photon skin sparing moves the other way with energy, which is the trap in A.

### Q5
Stem: Which change increases the bremsstrahlung (x-ray) contamination under an electron beam?
A. Raising the energy from 6 MeV to 20 MeV
B. Adding 0.5 cm of tissue-equivalent bolus, which removes photon contamination
C. Switching from 20 MeV electrons to 6 MV photons for a chest-wall field
D. Decreasing the cone size, which eliminates the photon tail by definition
Answer: A
Objective: I.3
Why: Answer A. Bremsstrahlung is produced in the scattering foils, collimators, and the patient. The photon tail beyond the practical range is a larger fraction of the dose as electron energy rises, on the order of a percent at low energy and several percent at high energy. That tail is the dose past Rp. Bolus shortens the electron range; it does not cancel contamination. A 6 MV photon beam is not an electron beam with a tail; it is a photon treatment. Cone size changes output and flatness, not the existence of the photon component.

## Electrons Quiz

### Q1
Stem: The deepest point of a target must lie on the 90% electron isodose at 3.0 cm of water. What minimum energy does Khan's rule require, what minimum energy does Bentel's rule require, and which rule asks for the higher energy?
A. Khan 12 MeV, Bentel about 9.6 MeV; Khan asks for the higher energy
B. Khan 9.6 MeV, Bentel 12 MeV; Bentel asks for the higher energy
C. Both rules require 6 MeV, because both set the 90% depth at E/2
D. Khan 3 MeV and Bentel 3.2 MeV, because the depth is multiplied by neither factor
Answer: B
Objective: I.3
Why: Answer B. Khan: 90% depth ≈ E/3.2, so E ≈ 3.2 × 3.0 = 9.6 MeV. Check: 9.6/3.2 = 3.0 cm. Bentel: 90% depth ≈ E/4, so E ≈ 4 × 3.0 = 12 MeV. A nominal 10 MeV beam satisfies Khan (10/3.2 = 3.1 cm) and fails Bentel (10/4 = 2.5 cm). Quoting the electron rule without naming the author changes the energy by one nominal step. Answer A swaps the authors. E/2 is the practical range, about 6 cm at 12 MeV, not the 90% depth.

### Q2
Stem: A 9 MeV beam is selected using Khan's rules. What are the approximate 90% depth, 80% depth, and practical range?
A. 2.25 cm, 3.0 cm, and 4.5 cm
B. 3.6 cm, 3.2 cm, and 9 cm
C. 4.5 cm, 2.25 cm, and 3.0 cm
D. 2.8 cm, 3.2 cm, and 4.5 cm
Answer: D
Objective: I.3
Why: Answer D. Khan: 90% at 9/3.2 ≈ 2.8 cm, 80% at 9/2.8 ≈ 3.2 cm, practical range 9/2 = 4.5 cm. The three numbers get deeper in that order. Answer A is Bentel: 9/4 = 2.25 cm and 9/3 = 3.0 cm, with the same practical range. Answer C puts the practical range first.

### Q3
Stem: A 12 MeV electron field is abutted on the skin to a 6 MV photon field. Which junction pattern is the one to look for on the plan?
A. A cold spot on the photon side and a hot spot on the electron side at the surface only
B. A hot spot on the photon side and a cold spot on the electron side
C. Uniform dose across the junction at every depth, because both beams are normalized to 100%
D. A cold spot at depth on both sides and a hot spot in the air above the skin
Answer: B
Objective: III.1
Why: Answer B. Clinical electron isodose lines constrict with depth: the 80% and 90% lines bow inward, away from the geometric field edge. On the electron side of a skin match, coverage pulls away from the junction and a cold spot appears at depth. Electrons also scatter laterally out of their field and into the photon field, where they add to the photon dose and produce a hot spot on the photon side. Normalizing both beams to 100% on their own central axes does not cancel that lateral scatter. The fix is a planned overlap or a feathered junction, not an assumption that two 100% lines add to a uniform 100%.

### Q4
Stem: Two adjacent 9 MeV fields are abutted on the skin to treat a scalp. The composite plan shows a hot streak at depth under the junction. The planner opens a 5 mm skin gap to cool that streak. What appears on the skin in the gap?
A. A hot spot, because a gap always increases electron scatter onto the surface
B. A cold strip, because the surface in the gap is covered by neither field while the deep hot spot was coming from lateral scatter
C. No change at the surface, because electron dose is uniform from the skin to Rp
D. A proton Bragg peak in the gap
Answer: B
Objective: III.1
Why: Answer B. Abutting electron fields on the skin overlap their laterally scattered dose under the junction, so the depth dose there runs hot. Opening a gap reduces that deep overlap. The skin inside the gap is not the entrance surface of either cone, so it is underdosed: a surface cold spot. That is the tradeoff of adjacent electrons. Feathering the junction over the course, or angling the fields, is how the hot streak and the cold strip are balanced. The gap does not create a Bragg peak.

### Q5
Stem: Lead will be used to shield the lens outside a 12 MeV electron field. Using the rule that the lead thickness in millimeters is about half the energy in MeV, how thick should the lead be, and about how thick should a cerrobend cutout be if cerrobend must be about 20% thicker than lead?
A. 12 mm of lead and 12 mm of cerrobend
B. 6 mm of lead and about 7.2 mm of cerrobend
C. 3 mm of lead and 3 mm of cerrobend, because the practical range in metal is E/4
D. 24 mm of lead, because electrons lose 2 MeV per millimeter of lead
Answer: B
Objective: I.3
Why: Answer B. The shielding rule of thumb is millimeters of lead ≈ E/2, so 12/2 = 6 mm of lead. Cerrobend is less dense in the sense that a given thickness stops fewer electrons; about 1.2 times the lead thickness is required. 6 × 1.2 = 7.2 mm of cerrobend. A more conservative lead estimate adds about 1 mm (E/2 + 1 = 7 mm) and would scale cerrobend the same way; the stem asked for E/2. The 2 MeV/cm rule is for water, not for lead, and E/4 is a water depth for the 90% dose, not a lead thickness.

### Q6
Stem: An internal eye shield is proposed under the eyelid for a 16 MeV electron lid treatment so the globe can be protected. Why is that shield a poor match to this energy?
A. Internal shields are safe at 16 MeV because backscatter falls as energy rises
B. At this energy, electrons reach the high-Z shield and backscatter into the eyelid; internal shields are restricted to low energies, about 9 MeV and below
C. 16 MeV electrons stop in 1 mm of tissue, so no shield is needed
D. The shield converts the beam to photons and removes the need for a cutout
Answer: B
Objective: III.7
Why: Answer B. An internal shield works only when the electron energy is low enough that the shield actually stops the beam. Sixteen MeV electrons have a practical range near 8 cm in water and will reach a thin lid shield. Electrons hitting lead or tungsten scatter back into the eyelid and conjunctiva and can raise that dose above the unshielded dose. Internal shields are therefore limited to low energy, about 9 MeV and below. A 16 MeV lid field needs a different technique, not a deeper shield of the same kind. The practical range is not 1 mm.

### Q7
Stem: A 12 MeV beam with no bolus places the 90% isodose at about 3.0 cm in water by Bentel's rule. A 1.0 cm tissue-equivalent bolus is added and the energy is unchanged. Where is the 90% isodose relative to the patient's skin?
A. Still at 3.0 cm, because bolus only changes output
B. At about 2.0 cm, because 1.0 cm of the range is spent in the bolus
C. At the skin surface exactly, for any bolus thickness
D. At 4.0 cm, because bolus adds penetration
Answer: B
Objective: III.7
Why: Answer B. Bolus is tissue-equivalent. Electrons lose range in the bolus before they enter the patient, and the isodose lines move toward the skin by about the bolus thickness. The 90% depth that was at 3.0 cm in a water phantom with no bolus is at about 3.0 − 1.0 = 2.0 cm in the patient. Skin dose rises because the skin is now downstream of 1 cm of buildup. Bolus does not add penetration. It is the correct tool when the target has become more superficial or when the surface dose of the bare beam is too low.

### Q8
Stem: A 2 cm diameter cutout is placed in a 10 cm electron cone for a 9 MeV beam. The planner uses the open-cone output factor. What is wrong with that, physically?
A. Nothing; output is independent of cutout size once the cone is chosen
B. A small cutout loses lateral electron equilibrium, so output falls, dmax moves toward the surface, and the percent depth dose becomes less penetrating than the open-cone curve
C. A small cutout raises the practical range from E/2 to E
D. The open-cone factor is correct because the jaws, not the cutout, set electron output
Answer: B
Objective: I.3
Why: Answer B. Electrons scatter out of a small field and are not replaced by scatter from outside it once the field is narrower than the lateral range of the electrons. Output at the prescription depth drops, the depth of maximum dose moves shallower, and the distal curve falls sooner than the large-field percent depth dose. The open 10 cm cone factor overestimates the dose. Small cutouts are measured individually. The jaws are set to a cone-specific opening, but the cutout in the beam is what the patient sees, and it changes the output. The practical range rule does not increase to E.

### Q9
Stem: A 6 MeV beam treats a chest wall en face. The physician asks to "harden" it to 18 MeV so the skin dose will fall the way it would for photons. What actually happens to the skin dose and the deep dose?
A. Skin dose falls and the practical range shortens
B. Skin dose rises and the practical range lengthens from about 3 cm to about 9 cm, so lung and heart receive more electron dose
C. Both energies stop at 1 cm, so only the bremsstrahlung changes
D. 18 MeV electrons are more skin-sparing than 6 MV photons
Answer: B
Objective: I.3
Why: Answer B. Raising electron energy raises surface dose; it does not mimic photon skin sparing. The practical range goes from 6/2 = 3 cm to 18/2 = 9 cm. On a chest wall that is only 1 to 2 cm thick, a 9 cm range dumps electron dose far into lung and heart, especially once density is considered. If the clinical problem is skin dose at 6 MeV, the tool is bolus, not a higher energy. If the clinical problem is a deep target, electrons may be the wrong modality.

## Protons 101

### Q1
Stem: Which energy is in the range used to treat deep tumors with protons, rather than an electron energy or a kilovoltage energy?
A. 12 MeV
B. 120 kV
C. 200 MeV
D. 1.25 MeV, the mean energy of a cobalt-60 beam
Answer: C
Objective: I.5
Why: Answer C. Clinical proton beams for treatment are commonly in the range of about 70 to 250 MeV, and deep targets use roughly 150 to 250 MeV. Two hundred MeV has a range in water of about 26 cm, which is enough for a deep pelvis or thorax. Twelve MeV is a typical linac electron energy, with a practical range of about 6 cm. One hundred twenty kilovolts is a superficial x-ray beam. Cobalt-60 emits 1.17 and 1.33 MeV photons, not a proton Bragg peak.

### Q2
Stem: A proton prescription is written as 70 Gy (RBE) using a constant clinical RBE of 1.1. What physical dose does the planning system have to deliver?
A. 70 × 1.1 = 77 Gy
B. 70 / 1.1 = 63.6 Gy
C. 70 Gy, because RBE is already included and the physical dose is identical
D. 70 × 0.5 = 35 Gy, because protons are high LET and RBE is 2
Answer: B
Objective: III.3
Why: Answer B. RBE-weighted dose equals physical dose times RBE. With RBE fixed at 1.1, physical dose = 70 / 1.1. Compute 70 ÷ 1.1: 1.1 × 63 = 69.3, remainder 0.7, and 0.7/1.1 = 0.636, so 63.6 Gy. Multiplying by 1.1 instead of dividing reports the photon-equivalent dose as if it were physical, and the patient would be overdosed by 10%. The clinical proton RBE used for prescription is 1.1, not 2. The distal end of the Bragg peak has a higher LET, and the true RBE there may exceed 1.1, which is a reason not to aim the distal end into a critical structure. The prescription itself still uses 1.1.

### Q3
Stem: A pristine Bragg peak is a sharp distal spike from a single proton energy. A clinical target is 6 cm thick in the beam direction. How is a spread-out Bragg peak formed over that thickness?
A. By passing the pristine beam through a flattening filter to make a photon-like percent depth dose
B. By stacking many pristine peaks of different ranges, with weights chosen so the plateau covers the target thickness
C. By adding an electron beam of energy E/2 to fill in the entrance
D. By prescribing to the 50% photon isodose and calling it a Bragg peak
Answer: B
Objective: I.3
Why: Answer B. One proton energy stops at one depth. To cover a target that extends 6 cm along the beam, the machine superimposes peaks whose ranges are stepped through those 6 cm. The deepest peak sets the distal edge. Shallower peaks fill the proximal target. The weights are higher for the deeper peaks in a typical spread-out curve so the sum is flat. That modulation is done with a ridge filter, a modulator wheel, or discrete energy layers in pencil-beam scanning. The result is not a flattened photon beam and it is not an electron range.

### Q4
Stem: Compared with a photon arc that covers the same intracranial target, what happens to dose beyond the distal edge of a correctly ranged proton beam, and what does that do to integral dose?
A. Protons deliver a larger exit dose than photons, so integral dose is higher
B. Primary protons stop; there is essentially no proton exit dose beyond the range, so integral dose to tissue past the target is much lower
C. Integral dose is identical because RBE of 1.1 cancels the Bragg peak
D. The spread-out Bragg peak continues at the prescription dose until it leaves the patient
Answer: B
Objective: I.3
Why: Answer B. The planning advantage of protons is the finite range. Tissue beyond the distal falloff does not receive the primary beam the way every photon beam exits. Integral dose, approximately mean dose times mass, therefore drops for many deep targets because the exit path is missing. A small dose from neutrons and other secondaries remains, and the entrance plateau is not zero. RBE scales the biological dose; it does not create an exit beam. A spread-out peak is flat across the target and then falls at its distal edge. It does not continue through the patient.

### Q5
Stem: A proton beam is aimed so that the distal falloff of the spread-out Bragg peak lies 2 mm proximal to the brainstem. The range uncertainty used by the clinic is several millimeters. What is the planning concern?
A. None; protons have no range uncertainty if the CT is a DICOM file
B. A small range overshoot moves the high dose onto the brainstem, because the prescription dose extends to the distal edge and then falls steeply
C. The brainstem is safer on the distal edge than on the lateral edge, because lateral penumbra is always the larger error
D. Range uncertainty only lengthens photon percent depth dose, not proton range
Answer: B
Objective: III.7
Why: Answer B. The distal edge is both the steepest and the least forgiving border. If the actual range is a few millimeters longer than the planned range, the entire prescription plateau shifts into the brainstem. Clinics therefore avoid ranging out into a serial organ when another beam angle can put that organ on the lateral penumbra instead, and they evaluate range error explicitly in robust optimization. CT Hounsfield units are converted to stopping power with a calibration that itself has uncertainty. That uncertainty is not removed by storing the scan as DICOM.

## Protons Quiz

### Q1
Stem: A pediatric craniospinal prescription is 36 Gy (RBE) in 20 fractions with RBE = 1.1. What is the physical dose per fraction?
A. 1.80 Gy
B. 1.64 Gy
C. 1.98 Gy
D. 3.60 Gy
Answer: B
Objective: III.3
Why: Answer B. The RBE-weighted dose per fraction is 36/20 = 1.80 Gy (RBE). Physical dose per fraction is 1.80/1.1. Compute 1.8 ÷ 1.1: 1.1 × 1.6 = 1.76, remainder 0.04, and 0.04/1.1 ≈ 0.036, so 1.64 Gy. The course physical dose is 36/1.1 = 32.7 Gy. Multiplying by 1.1 instead of dividing gives 1.98 Gy and would raise the delivered dose. Reporting 1.80 Gy as the physical dose forgets to remove the RBE. Two fractions would be 3.60 Gy (RBE), which is not one fraction.

### Q2
Stem: A pelvic proton beam has a planned range of 25.0 cm. The clinic's range uncertainty is 3.5% of the range plus 2 mm. What distal margin does that recipe require?
A. 3.5 mm
B. 8.8 mm
C. 10.8 mm
D. 25 mm
Answer: C
Objective: III.7
Why: Answer C. Three and a half percent of 25.0 cm is 0.035 × 25.0 = 0.875 cm = 8.75 mm. Add the 2 mm absolute term: 8.75 + 2 = 10.75 mm, which rounds to 10.8 mm. Quoting only the 3.5% term leaves out the setup-like absolute margin and gives 8.8 mm. Three and a half millimeters would be 3.5% of 10 cm, not of 25 cm. The whole 25 cm is the range, not the margin. This margin is why a brainstem or a cord sitting a few millimeters past the target is not automatically safe.

### Q3
Stem: A passive-scattering proton plan and a pencil-beam scanning plan deliver the same target dose. The patient has a cardiac device well outside the field. Which delivery produces more secondary neutrons, and why does that matter?
A. Pencil-beam scanning, because magnetic scanning creates neutrons in the air; neutrons are irrelevant to electronics
B. Passive scattering, because more material (scatterers, modulator, aperture, compensator) sits in the beam; neutrons are a device and integral-dose concern even outside the aperture
C. They produce equal neutrons because the prescription RBE is the same
D. Neither produces neutrons; neutrons are limited to photon beams above 10 MV
Answer: B
Objective: I.5
Why: Answer B. Passive scattering spreads and modulates the beam with physical hardware in the beam path. Nuclear interactions in that hardware generate neutrons that reach the patient. Pencil-beam scanning steers a narrow beam magnetically and uses much less material, so the neutron dose outside the field is lower. Those neutrons matter for a pacemaker or defibrillator in the same way high-energy photon neutrons do: the device does not have to be in the aperture. RBE of 1.1 does not measure neutron production. Photon beams above 10 MV are a second, separate neutron source, not the only one.

### Q4
Stem: The proton CT calibration curve in the planning system maps Hounsfield units to relative stopping power. A physicist accidentally assigns the photon electron-density curve instead. What goes wrong in the dose calculation?
A. Nothing; stopping power and electron density are the same number for every tissue
B. The calculated range is wrong, because protons stop according to stopping power, not according to the photon electron-density table
C. Only the lateral penumbra changes; the distal edge stays put
D. The RBE changes from 1.1 to 1.0 and the range is unaffected
Answer: B
Objective: I.3
Why: Answer B. Photon dose engines need electron density (and composition) because photons interact by attenuation and scatter. Protons lose energy continuously, and the quantity that integrates to the range is the relative stopping power along the path. A curve that was commissioned for photons will assign the wrong water-equivalent thickness, especially in bone and in lung, and the Bragg peak will be computed at the wrong depth. The distal edge is exactly what moves. RBE is a biological factor applied after the physical dose; it is not the calibration curve.

### Q5
Stem: A superficial scalp target is treated with pencil-beam scanning. The lowest available energy still ranges past the target, so a 4 cm water-equivalent range shifter is inserted. The shifter is mounted 20 cm upstream of the skin. What is the cost of that air gap?
A. None; a range shifter only changes energy and does not affect spot size
B. The spots scatter in the shifter and then travel through air, so the lateral penumbra at the patient widens as the air gap increases
C. The range shifter creates an exit dose similar to 18 MV photons
D. The Bragg peak is replaced by a 4 cm electron practical range
Answer: B
Objective: III.7
Why: Answer B. A range shifter pulls the Bragg peak toward the surface so a machine whose minimum energy is too high can still treat a shallow target. Protons scatter in the shifter. The larger the gap between the shifter and the skin, the more that scatter fans out, and the lateral edge at the patient gets wider. Pulling the shifter close to the skin, or using a bolus on the skin, keeps the penumbra tighter. The shifter does not give the beam a photon-like exit and it does not turn the beam into electrons.

### Q6
Stem: A passive-scattering plan uses a compensator milled to the distal surface of the target, then smeared. What is smearing for?
A. It sharpens the distal edge to follow every CT voxel of bone
B. It deliberately blurs the compensator so a small setup or motion error does not pull a high-density ray off the target and leave a cold spot or a hot distal spot
C. It removes the aperture so the lateral penumbra becomes zero
D. It converts the spread-out Bragg peak into a pristine peak
Answer: B
Objective: III.7
Why: Answer B. An unsmeared compensator matches the distal target on the planning CT exactly. If the patient shifts, a ray that was planned through soft tissue can pass through bone, stop short, and underdose the distal target, or the opposite error can push dose past the target. Smearing thickens the compensator in a neighborhood around each ray so the distal dose still covers under that shift. The price is a less conformal distal edge. The aperture, not the compensator, is what trims the lateral edge. Smearing does not remove modulation.

### Q7
Stem: Two single-field proton plans cover a target just proximal to an optic nerve. Plan A places the nerve 3 mm beyond the distal falloff. Plan B places the nerve on the lateral penumbra and stops the beam in tissue beyond a different border. Range uncertainty is about 1 cm. Which plan is more robust, and why?
A. Plan A, because the distal falloff is steeper than the lateral penumbra so the nerve dose is always lower
B. Plan B, because a 1 cm range error can carry the prescription dose onto a nerve that sits only 3 mm past the distal edge, whereas a lateral placement uses the penumbra the range error does not directly shift
C. They are equivalent because RBE is 1.1 in both
D. Plan A is required by ICRU because serial organs must lie on the distal edge
Answer: B
Objective: III.7
Why: Answer B. Steepness is only an advantage if the edge is in the right place. A range error of about 1 cm is larger than the 3 mm gap in plan A, so the optic nerve can move from "just outside" to "inside the plateau" without any change in the lateral aperture. Putting the nerve on the lateral border makes the relevant uncertainty the setup and the penumbra, which robust optimization and image guidance also address, and it keeps a range miss from sliding the high dose onto the nerve. RBE does not choose the beam angle.

### Q8
Stem: A photon volumetric modulated arc and a proton pencil-beam plan both deliver 50 Gy (RBE) to a paraspinal target. The cord is distal to the proton beam and is kept out of the photon arc's high dose. Which comparison of integral dose is the expected one?
A. The proton plan has the higher integral dose because the entrance plateau equals the prescription from the skin to the target
B. The proton plan has the lower integral dose because tissue beyond the range receives essentially no primary dose, while every photon beam exits
C. Integral doses match because both prescriptions are 50 Gy
D. The photon plan has zero integral dose outside the PTV because modulation eliminates scatter
Answer: B
Objective: III.1
Why: Answer B. Integral dose adds dose times mass over the body. The proton entrance path does receive plateau dose, so the skin and the proximal tissues are not spared the way a naive "Bragg peak only" picture suggests. Tissue past the distal falloff, which for a photon arc would be an exit path through the patient, receives almost none of the primary proton dose. For a deep or one-sided target that usually makes the proton integral dose lower. Equality of the prescription does not imply equality of the mass that receives dose. Modulation reduces high dose outside the target; it does not remove photon scatter and exit dose.

### Q9
Stem: Full intensity-modulated proton therapy lets each field cover only part of the target, and the sum covers the target. Single-field uniform dose makes each field cover the whole target by itself. Under a range error, which is generally more robust?
A. Full multi-field intensity modulation, because it uses more edges inside the target
B. Single-field optimization, because each beam still covers the target if one beam's range is slightly wrong
C. They are identical once the nominal DVH looks the same
D. Robustness is only a photon concept
Answer: B
Objective: III.7
Why: Answer B. In fully modulated proton therapy the high dose in one part of the target may come from only one field's distal end. A range or setup error that moves that spot leaves a hole that the other fields were not asked to fill. Single-field optimization is less conformal and usually more robust, because each field is a complete, if less elegant, dose. A nominal DVH does not display that difference; robust evaluation under shifted density and shifted setup does.

### Q10
Stem: A proton clinical target is expanded by 5 mm in every direction, the same shell used on the photon plan. The planner marks range uncertainty as finished. One beam is aimed at the target. What is still required?
A. A prescription rewritten in kilovolts, because proton range is set by tube potential
B. A range margin along the beam. Range uncertainty is added as a margin on how far the protons travel
C. Nothing further. A uniform geometric shell is the range margin
D. A lead shield whose thickness in millimeters is half the beam energy, placed on the distal side
Answer: B
Objective: III.7
Why: Answer B. Proton range uncertainty sits on stopping power, tissue composition, and the path, so it is handled by a proximal and distal range margin along the beam, together with a robust check of that margin. The department protocol sets how many millimeters that margin is. A 5 mm shell copied from a photon PTV is a geometric setup margin. It does not add the range margin. Kilovoltage tube potential is not a proton energy. The electron lead rule is not a proton distal margin.

### Q11
Stem: A clinical proton course is prescribed as 44 Gy (RBE). No biological factor other than the generic clinical proton value is given. What physical dose does that prescription call for?
A. 40 Gy
B. 44 Gy
C. 48.4 Gy
D. 88 Gy
Answer: A
Objective: III.3
Why: Answer A. The generic clinical proton RBE is 1.1. RBE-weighted dose is the physical dose times that factor, so the physical dose is the prescribed 44 Gy (RBE) with the factor taken back out. Because 1.1 times 40 equals 44, the physical dose is 40 Gy. Reporting 44 Gy leaves the RBE in the number. Multiplying 44 by 1.1 gives 48.4 Gy and applies the factor a second time. Doubling to 88 Gy uses a factor of 2, which is not the clinical proton value.

### Q12
Stem: A proton field covers a target that is several centimeters thick along the beam. Which description is the spread-out Bragg peak?
A. The entrance region, where the dose is lower than the target dose
B. Photon dose beyond the patient
C. One unspread spike from a single proton energy
D. The flat high-dose region made by stacking pristine peaks across the target thickness
Answer: D
Objective: I.3
Why: Answer D. A single proton energy stops in a narrow Bragg peak. A spread-out Bragg peak stacks peaks of different energies and weights so the high-dose region is flat across the thickness that must be covered. That flat high-dose stretch is the SOBP. The entrance region is proximal to it and is lower than the SOBP dose. Tissue beyond the distal falloff does not keep the prescription dose, and one pristine spike is too narrow to be the spread-out region.

### Q13
Stem: With no extra material in the beam, a proton beam stops at about 15 cm of water. A range shifter of 5 cm water-equivalent thickness is then placed upstream of the patient. What happens to the range in the patient?
A. It lengthens to about 20 cm
B. It stays about 15 cm, because a shifter changes only the spot map
C. It shortens to about 10 cm. The shifter pulls the range shallower
D. The beam leaves the patient as an 18 MV photon exit dose
Answer: C
Objective: III.7
Why: Answer C. A range shifter is material the protons cross before the skin. They lose energy in that material, so less range remains in the patient. A shifter of 5 cm water-equivalent thickness on a 15 cm water range leaves about 15 minus 5, or 10 cm, in the patient. The peak moves shallower, which is why a shifter is used when the lowest available energy still stops too deep. Adding the 5 cm to the 15 cm points the range the wrong way. The shifter does not turn the beam into photons. Scatter in the shifter can widen the lateral penumbra; that widening does not put the range deeper.

### Q14
Stem: Where along a clinical proton beam is the linear energy transfer higher?
A. In the entrance plateau, where the protons are fastest
B. At the distal end, where the protons are slowing and stopping
C. It is the same at every depth and is identical to the generic RBE of 1.1
D. It is the Hounsfield number of the voxel the proton is crossing
Answer: B
Objective: I.3
Why: Answer B. Linear energy transfer is the energy a charged particle loses per unit path. Protons lose more energy per millimeter as they slow down, so LET is higher at the distal end than in the entrance plateau. The prescription still uses the generic RBE of 1.1 unless a protocol states another factor. A higher distal LET is a reason to keep a serial organ off that end. It does not replace 1.1 with the Hounsfield number, and it does not make LET uniform. The entrance is where the protons are fastest and the LET is lower.

### Q15
Stem: A water voxel reads about 0 on the Hounsfield scale. A planner copies that 0 into the relative stopping-power table for the same voxel. What is wrong with that copy?
A. Stopping-power ratio and Hounsfield units are different quantities. Water's relative stopping power is 1, and the planning system converts CT numbers to stopping power through a calibration curve
B. Nothing. The stopping-power ratio is defined to be the Hounsfield number
C. The voxel should be entered as 1.1, because relative stopping power is the proton RBE
D. A Hounsfield value of 0 means the protons have already stopped, so the range table can stay empty
Answer: A
Objective: I.3
Why: Answer A. The Hounsfield scale sets water near 0. Relative stopping power is defined so water is 1. Those are different quantities, and a CT number is not a stopping-power ratio. The dose engine integrates stopping power along each ray, using a calibration curve from Hounsfield units to stopping-power ratio. Entering 0 for water assigns water a stopping power of zero, so the engine takes no energy from the protons there and the calculated range runs too deep. The clinical RBE of 1.1 is a biological factor applied to physical dose. It is not the stopping-power ratio. Air, near −1000 Hounsfield units, is another pair that does not match: its relative stopping power is near 0, not −1000.

## Isodose Chart

### Q1
Stem: An isodose chart shows lines labeled 100%, 95%, 80%, and 50% for a single 6 MV beam. What does a point on the 80% line mean?
A. The point receives 80% of the dose at the chosen normalization point, in the stated plane
B. The point receives 80 Gy, regardless of the prescription
C. Eighty percent of the PTV volume is at that point
D. The point is at 80% of the source-to-skin distance
Answer: A
Objective: III.1
Why: Answer A. An isodose line joins points of equal dose. On a chart normalized to 100% at dmax (a common SSD presentation) or at isocenter (a common SAD presentation), the 80% line is 80% of that reference dose. It is not a dose in gray until the prescription is attached, it is not a DVH point, and it is not a distance. Two charts with the same beam but different normalization points will print different percentages at the same physical point. The doses in gray are what have to be compared.

### Q2
Stem: A wedge is inserted and the isodose lines that were perpendicular to the central axis now tilt. At 10 cm depth the 50% line makes a 30 degree angle with the line drawn perpendicular to the central axis. Which value is the wedge angle on this definition?
A. 60 degrees, because the wedge angle is the complement of that tilt
B. 30 degrees
C. 120 degrees, the hinge of a wedged pair
D. 15 degrees, half the tilt, because wedges are named by hinge angle
Answer: B
Objective: III.1
Why: Answer B. The wedge angle is defined from the tilt of an isodose line, commonly evaluated at 10 cm depth: it is the angle between that isodose line and the perpendicular to the central axis. If that angle is 30 degrees, the wedge angle is 30 degrees. It is not the complement, and it is not the hinge angle between two beams. A separate approximation, wedge angle ≈ 90 − (hinge angle)/2, is used when choosing a wedge for a pair. Here the chart has already measured the tilt, so no further conversion is applied.

### Q3
Stem: Physical penumbra on a photon beam profile is defined at dmax as the lateral distance between which two dose levels?
A. 90% and 10%
B. 80% and 20%
C. 50% and 50%
D. 100% and 0%, from central axis to the jaw
Answer: B
Objective: III.1
Why: Answer B. The physical penumbra is the distance off-axis between the 80% and 20% dose points on the beam profile at the depth of maximum dose (some specifications repeat the measurement at 10 cm). It folds together geometric penumbra from the source size and transmission through the collimator edge, plus scatter. The 90%-to-10% distance is a wider descriptor sometimes quoted, but it is not the standard 80-to-20 definition. The 50% point is approximately the geometric field edge, not a penumbra width by itself.

### Q4
Stem: ICRU 50 describes a hot spot as a volume outside the PTV that receives more than 100% of the specified PTV dose. When is that hot spot considered clinically significant under that definition?
A. Whenever a single voxel exceeds 100%, including inside the PTV
B. When the volume outside the PTV has a minimum diameter of about 15 mm, with a stricter reading for small organs such as the optic nerve
C. Only when it exceeds 150% of the prescription
D. Only when it lies inside the GTV
Answer: B
Objective: III.11
Why: Answer B. ICRU 50 reserved the term hot spot for dose above the specification that sits outside the PTV. A tiny calculation spike was not automatically "clinically significant"; the report used a minimum diameter of about 15 mm. A small organ such as the optic nerve or eye can be injured by a hot volume smaller than that, so the diameter test is not an excuse to ignore a high dose in those structures. A hot voxel inside the PTV is a homogeneity problem, not this definition of a hot spot. The GTV is inside the PTV and is not the place a hot spot, in this ICRU sense, is declared.

### Q5
Stem: An SSD isodose chart is normalized to 100% at dmax on the central axis. An SAD chart for the same energy is normalized to 100% at isocenter. A point at 10 cm depth on the central axis reads 67% on the SSD chart. Why might the SAD chart print a different percentage at the same physical point?
A. It will not; percent depth dose and TMR charts are labeled identically by definition
B. The 100% point has moved from dmax to isocenter, so every percentage is quoted against a different dose
C. SAD charts are required to be labeled in gray and cannot show percentages
D. The point at 10 cm depth is defined as 100% on both charts
Answer: B
Objective: III.1
Why: Answer B. Percentages are fractions of whatever was called 100%. On the SSD chart, 67% means 67% of the dose at dmax. On an SAD chart normalized at isocenter, the dose at isocenter already includes inverse-square and phantom scatter effects relative to dmax, so the same physical point gets a different number. Monitor-unit calculations follow the same split: percent depth dose with an SSD setup, TMR or TPR with an SAD setup. The labels cannot be copied from one chart onto the other without re-normalizing.

## Measurement of Isodose Curves

### Q1
Stem: A profile at dmax shows the 80% dose at 2.4 cm off-axis and the 20% dose at 3.1 cm off-axis on the same side of the central axis. What is the physical penumbra?
A. 5.5 cm
B. 2.75 cm
C. 0.7 cm
D. 3.1 cm
Answer: C
Objective: III.1
Why: Answer C. Penumbra width is the distance between the two stated dose points, not their average and not their sum. 3.1 − 2.4 = 0.7 cm, or 7 mm. Adding them (5.5 cm) or averaging them (2.75 cm) has no definition behind it. Quoting only the 20% location (3.1 cm) gives a field-edge coordinate, not a width. The same subtraction is done on the other side of the field as a symmetry check.

### Q2
Stem: Flatness is computed over the central 80% of the field width at 10 cm depth as (Dmax − Dmin)/(Dmax + Dmin). The measured values, relative to 100% on the central axis, are Dmax = 103 and Dmin = 97. What is the flatness?
A. 6%
B. 3%
C. 103%
D. 1%
Answer: B
Objective: III.1
Why: Answer B. The numerator is 103 − 97 = 6. The denominator is 103 + 97 = 200. Flatness = 6/200 = 0.03 = 3%. Reporting the raw difference, 6%, forgets to divide by the sum and makes the beam look twice as unflat as this definition says. A common commissioning tolerance for photon flatness is on the order of 3%, so this example sits at that kind of limit and would be read against the clinic's own specification, not assumed to pass just because the central axis is 100%.

### Q3
Stem: Left-side and right-side profile areas inside the field are 510 and 490 in the same arbitrary units. Symmetry is defined as (Area_left − Area_right)/(Area_left + Area_right). What is the symmetry?
A. 20%
B. 4%
C. 2%
D. 510%
Answer: C
Objective: III.1
Why: Answer C. The difference of the areas is 510 − 490 = 20. The sum is 510 + 490 = 1000. Symmetry = 20/1000 = 0.02 = 2%. Reporting 20% uses the difference as if it were already a percentage of the sum. A typical photon symmetry tolerance is about 2%, so this beam is at the edge of a common specification. The sign says which side is high; the specification usually uses the absolute value.

### Q4
Stem: A 2 cm stereotactic field has a steep penumbra. An ion chamber with a 6 mm long collecting volume and a diode with a sub-millimeter sensitive volume are both available. Which detector will make the penumbra look artificially wide, and why?
A. The diode, because a small detector averages dose over a larger distance
B. The ion chamber, because it averages dose along its volume and blurs an edge that is narrower than that volume
C. Neither; measured penumbra is independent of detector size
D. The diode, because diodes cannot respond to photons
Answer: B
Objective: III.1
Why: Answer B. Any detector reports an average over its sensitive volume. A 6 mm chamber laid across a penumbra that is only a few millimeters wide mixes the 80% region with the 20% region in a single reading and spreads the apparent edge. A diode, a film, or a diamond detector with a much smaller sensitive region follows the true gradient more closely. The same volume-averaging problem makes a large chamber the wrong tool for small-field output. Diodes do respond to photons; they over-respond to low-energy scatter and are usually corrected, but that is a different limitation from spatial blurring.

### Q5
Stem: Isodose curves for a commissioning scan of a 10 by 10 cm photon beam are measured in a water tank with a scanning ion chamber. Why water, and why a scan rather than a single point?
A. Water is a tissue substitute with a known density, and a scan builds the two-dimensional dose map a single central-axis depth dose cannot show
B. Water is used because it increases the practical range of photons to E/2
C. A single point at dmax fully defines the wedge angle, the penumbra, and the flatness
D. Scanning is required only for electrons; photon isodose lines are calculated and never measured
Answer: A
Objective: III.1
Why: Answer A. Commissioning measures dose in water because the beam data (percent depth dose, profiles, output) are defined in water and then used to calculate dose in the patient via a density correction. A profile scan at several depths, plus a central-axis depth dose, is what gets turned into an isodose chart: flatness, symmetry, penumbra, and wedge tilt all live off-axis. One point at dmax cannot show any of those. Photon beams are measured. The electron practical-range rule does not apply to photons.

## Target Volume Definitions

### Q1
Stem: A lung tumor is visible on CT. Microscopic extension is suspected around it. The tumor moves 8 mm with respiration on a 4D scan. Daily setup uncertainty is estimated at 5 mm. Which volume is which?
A. GTV is the visible tumor, CTV adds the microscopic margin, ITV adds the motion, and PTV adds the setup margin
B. GTV already includes motion, CTV is the setup margin, and PTV is the visible tumor
C. ITV is the visible tumor and GTV is the volume of the 95% isodose
D. PTV is contoured first, and the GTV is the PTV minus the organ-at-risk volume
Answer: A
Objective: III.11
Why: Answer A. ICRU volumes nest in a defined order. The GTV is what you can see or palpate. The CTV expands it for disease you cannot see. The ITV, from ICRU 62, expands the CTV by the internal margin for physiologic motion. The PTV expands that result by the setup margin so the CTV still receives the dose when the patient is not exactly where the plan assumed. Motion does not go into the GTV. The 95% isodose is a treated-volume idea, not a GTV. Organs at risk are contoured separately and do not define the tumor.

### Q2
Stem: A breast tumor has been excised. The pathology report describes positive margins, and the cavity with clips is visible, but no gross tumor remains on the CT. Which statement matches the definitions?
A. A GTV is required on every radical plan, so the clips are contoured as GTV
B. There may be no GTV; the CTV is the region of suspected microscopic residual disease, and the PTV is that CTV plus setup margin
C. The PTV is omitted because there is no GTV to expand
D. The clips are an organ at risk and are blocked
Answer: B
Objective: III.11
Why: Answer B. GTV means gross disease. After a complete excision the gross disease is gone, even if the microscopic margin is not. The clinical target is then a CTV: the cavity, a margin for residual cells, and any elective tissue the physician includes. The PTV is still added, because setup error does not disappear in the postoperative setting. Clips are a localization aid for the cavity, not an organ to block and not themselves a GTV.

### Q3
Stem: The ITV was contoured on a maximum-intensity projection that already includes respiratory motion. The planner then expands the ITV by the same 8 mm motion plus a 5 mm setup margin and calls the result the PTV. What was double-counted?
A. Nothing; motion is added in both the ITV and the PTV by definition
B. The respiratory motion, which is already inside the ITV and should not be added again when going from ITV to PTV
C. The setup margin, which belongs in the GTV
D. The microscopic margin, which belongs in the PTV rather than the CTV
Answer: B
Objective: III.11
Why: Answer B. The ITV is the CTV plus the internal margin. Once the tumor's respiratory positions are inside the ITV, the remaining expansion to the PTV is the setup margin, here 5 mm, not another copy of the 8 mm excursion. Adding the excursion twice makes the high-dose volume larger than the uncertainty requires and irradiates extra lung. The microscopic margin belongs in the CTV, before motion is applied. Setup does not belong in the GTV.

### Q4
Stem: The PTV is covered by the 95% isodose. That 95% isodose surface encloses 420 cm³. The PTV is 300 cm³. A separate 20 Gy isodose encloses 1500 cm³, and 20 Gy is the dose the physician considers significant for the surrounding normal tissue. Which ICRU volume is the 420 cm³, and which is the 1500 cm³?
A. 420 cm³ is the irradiated volume and 1500 cm³ is the GTV
B. 420 cm³ is the treated volume and 1500 cm³ is the irradiated volume
C. Both are the PTV, because every isodose is a PTV
D. 420 cm³ is the internal target volume and 1500 cm³ is the planning organ-at-risk volume
Answer: B
Objective: III.11
Why: Answer B. ICRU defines the treated volume as the volume enclosed by an isodose surface the physician has selected as adequate to achieve the purpose of treatment, here the 95% surface at 420 cm³. It is larger than the PTV because the prescription isodose does not hug the PTV perfectly. The irradiated volume is the volume receiving a dose considered significant for normal-tissue tolerance, here the 20 Gy surface at 1500 cm³. Neither one is the GTV, the ITV, or a planning organ-at-risk volume. Those are contoured structures. Treated and irradiated volumes are dose volumes.

### Q5
Stem: The spinal cord is contoured, then expanded by 3 mm to a planning organ-at-risk volume (PRV). The cord tolerance is applied to the PRV. Why does that expansion exist?
A. The cord grows 3 mm during treatment, and the PRV is a CTV for the cord
B. The cord can move into the high dose by the setup margin; the PRV is the cord plus that margin so the dose limit is applied to where the cord might be
C. A PRV replaces the PTV, and the target is not expanded
D. The PRV is the volume of the 95% isodose inside the cord
Answer: B
Objective: III.11
Why: Answer B. ICRU 62 defined the planning organ-at-risk volume as the organ plus a margin for its geometric uncertainty, analogous to the PTV but built to protect rather than to cover. If the cord limit is applied only to the cord contour drawn on the planning CT, a 3 mm setup shift can put the real cord into a dose the DVH called acceptable. Applying the limit to the PRV is the conservative geometric move. It does not mean the cord has microscopic disease, and it does not redefine the target. Where a PTV and a PRV overlap, the physician sets the priority; the overlap itself is allowed by the definitions.

## DVH Interpretation and Dose Metrics

### Q1
Stem: A structure has a volume of 100 cm³. The differential DVH bins are 10 cm³ from 0 to 10 Gy, 20 cm³ from 10 to 20 Gy, 40 cm³ from 20 to 30 Gy, and 30 cm³ from 30 to 40 Gy. What is the cumulative volume receiving at least 20 Gy?
A. 20 cm³, the height of the 10-to-20 bin
B. 40 cm³, the height of the 20-to-30 bin
C. 70 cm³
D. 100 cm³, because cumulative DVHs always read 100% at every dose
Answer: C
Objective: III.1
Why: Answer C. A differential bin counts volume that received a dose inside that bin and not outside it. A cumulative DVH counts volume that received at least the stated dose. At least 20 Gy means the 20-to-30 bin plus the 30-to-40 bin: 40 + 30 = 70 cm³, which is V20 = 70%. The 20 cm³ bin is tissue that received less than 20 Gy. Reading a single differential bar as a cumulative point is the usual mix-up. The cumulative value at 0 Gy is the whole volume, 100 cm³, and it falls as the dose threshold rises; it is not 100% at 40 Gy.

### Q2
Stem: Using the same bins (centers at 5, 15, 25, and 35 Gy, volumes 10, 20, 40, and 30 cm³), what is the mean dose?
A. 20 Gy, the dose where the cumulative DVH is 70 cm³
B. 24 Gy
C. 35 Gy, the center of the hottest bin
D. 40 Gy, the maximum
Answer: B
Objective: III.1
Why: Answer B. Mean dose is the sum of (bin dose × bin volume) divided by total volume. Using bin centers: (5 × 10) + (15 × 20) + (25 × 40) + (35 × 30) = 50 + 300 + 1000 + 1050 = 2400 Gy·cm³. Divide by 100 cm³: 24 Gy. The cumulative V20 does not equal the mean. The hottest bin center and the maximum are each higher than the mean because most of the volume sits near 25 Gy, not at 40 Gy. A differential DVH makes this average obvious: the tallest bar is the 20-to-30 Gy bin. A cumulative curve would show the same information only after it is interpreted as a distribution, not as a single V20 point.

### Q3
Stem: Two prostate plans have identical rectal DVHs. In plan A the high dose is on the anterior rectal wall. In plan B the same high-dose voxels lie in the rectal lumen and the posterior wall is spared. What can the DVH not tell the planner?
A. The volume of rectum receiving at least 70 Gy
B. Where in the rectum the high dose sits
C. Whether V70 is above or below 15%
D. The mean rectal dose, if the histogram is complete
Answer: B
Objective: III.1
Why: Answer B. A DVH throws away position. Any voxel inside the contour contributes to the same curve, whether it is on the anterior wall (where a prostate plan can cause bleeding) or in the lumen (where it may not). Plans A and B can share V70, mean dose, and D2% and still not be equally safe. Seeing the location requires the isodose display or a sub-contour of the wall. The DVH can answer A, C, and D, which are all functions of dose and volume only.

### Q4
Stem: Plan A delivers a mean dose of 40 Gy to 2 kg of normal tissue. Plan B delivers a mean dose of 5 Gy to 20 kg of normal tissue. Which plan has the higher integral dose, and what is that value?
A. Plan A, at 80 Gy·kg, because the mean dose is higher
B. Plan B, at 100 Gy·kg
C. They are equal, because 40/5 = 20/2
D. Plan A, at 800 Gy·kg
Answer: B
Objective: III.1
Why: Answer B. Integral dose is mean dose multiplied by mass, when the mean is taken over that mass. Plan A: 40 Gy × 2 kg = 80 Gy·kg. Plan B: 5 Gy × 20 kg = 100 Gy·kg. The low-dose bath in plan B deposits more integral dose even though no point looks hot. This is the usual cost of rotational and helical delivery compared with a simple opposed pair, and it is why "the DVH of the PTV looks the same" is not a complete comparison. Answer D multiplies by an extra factor of 10. The ratio of the means is not required to equal the ratio of the masses for the integral doses to match, and here 80 is not 100.

### Q5
Stem: A cord is 6 mm in diameter. The dose grid is 4 mm. The cord DVH maximum is under the limit. Why might that DVH still be the wrong number?
A. A coarse voxel averages dose across a large fraction of the cord and can hide a peak, and the DVH cannot reveal that the grid was too coarse
B. Dose grids do not affect DVHs
C. A maximum on a DVH is always the dose to a mathematical point, independent of voxel size
D. The limit should be compared with the minimum cord dose when the grid is coarse
Answer: A
Objective: IV.6
Why: Answer A. The displayed cord dose is the dose in the voxels the grid actually computed. A 4 mm voxel is most of the width of a 6 mm cord, so the value is an average over white matter, gray matter, and perhaps CSF, not the peak in the cord. A coarse grid can either smear a hot spot down or assign a neighboring hot voxel to the cord, and the histogram itself does not say which happened. The calculation has to be repeated on a finer grid, on the order of 1 to 2 mm for a small serial organ, before the maximum is compared with the limit. The relevant constraint for cord is a maximum or a near-maximum, not the minimum.

### Q6
Stem: The PTV volume is 20 cm³. The prescription isodose encloses 24 cm³. The volume of PTV that actually lies inside the prescription isodose is 19 cm³. What is the RTOG conformity index (prescription volume divided by PTV volume)?
A. 19/20 = 0.95
B. 24/20 = 1.20
C. 19/24 = 0.79
D. 20/24 = 0.83
Answer: B
Objective: III.1
Why: Answer B. The RTOG conformity index is the volume of the prescription isodose divided by the target volume: 24/20 = 1.20. A value of 1 would mean those volumes match. A value above 1 means the prescription cloud is larger than the PTV, which is this plan. The index does not by itself say whether the extra 4 cm³ is hanging off one side while part of the PTV is missed. Here 1 cm³ of PTV is outside the prescription (20 − 19), so coverage is not perfect even though the index is only moderately above 1. The ratio 19/24 is closer to a coverage fraction of the prescription cloud, and it is not the RTOG definition.

### Q20
Stem: The cord limit in use is a maximum of 50 Gy. The cumulative DVH of the contoured cord reports a maximum of 44 Gy. On one axial slice the canal was never contoured, and the isodose display shows 54 Gy inside that canal. Which conclusion is justified?
A. The cord meets the limit, because 50 − 44 = 6 Gy of margin and a DVH maximum already includes every slice
B. The contoured cord is 6 Gy under 50 Gy, but the DVH contains only contoured voxels; the uncontoured slice is 4 Gy over 50 Gy and does not move the histogram
C. The DVH maximum already reports the excess 54 − 44 = 10 Gy
D. A differential DVH adds the missing slice and a cumulative DVH does not
Answer: B
Objective: III.1
Why: Answer B. 50 − 44 = 6 Gy, so the maximum of the contoured cord is under the limit. Both cumulative and differential histograms use only voxels inside the structure, so an uncontoured canal slice never enters the curve. On that slice, 54 − 50 = 4 Gy over the limit. The 10 Gy gap, 54 − 44, is the difference between the isodose on the missing slice and the DVH of a different set of voxels. Changing the plot type does not draw the missing contour.

### Q21
Stem: Every structure that has an optimization objective meets its DVH limit. The parotid mean objective is 26 Gy and the parotid DVH mean is 24 Gy. The esophagus is contoured and has no objective. The isodose display shows 70 Gy inside the esophagus. The prescription is 60 Gy. What has the objective list missed?
A. A parotid failure of 24 − 26 = −2 Gy
B. That the esophagus DVH maximum must equal 60 Gy because that is the prescription
C. Nothing; a structure with no objective cannot contain dose
D. An esophagus hotspot the optimizer was not asked to limit, above the prescription, while the parotid objective is still under its own limit
Answer: D
Objective: III.12
Why: Answer D. An objective constrains only the structure it is attached to. The parotid mean meets its limit: 26 − 24 = 2 Gy under 26 Gy. The esophagus had no objective, so 70 Gy inside it does not turn the objective list red. Relative to the prescription, 70 − 60 = 10 Gy above 60 Gy. That region is visible on the isodose display and on an esophagus DVH if one is computed. Dose is deposited whether or not an objective exists, and a negative parotid margin is not a failure.

### Q22
Stem: On a single axial slice the 95% isodose wraps the PTV and the plan is called conformal from that slice. The PTV is 40 cm³. Over the whole target, the prescription-isodose volume is 52 cm³ and 38 cm³ of the PTV lies inside it. D95 equals the prescription dose, so the coverage objective is met. Which reading is justified?
A. One conformal slice plus a met D95 proves the prescription isodose matches the PTV on every slice
B. The RTOG conformity index is 38/40 = 0.95, so the plan is too tight to be conformal
C. D95 can meet the coverage objective while the prescription cloud is still larger than the PTV and part of the PTV is missed; one slice does not locate that miss
D. The conformity index is 52 − 40 = 12, and a difference of 12 cm³ is a perfect score
Answer: C
Objective: III.1
Why: Answer C. D95 at the prescription dose means at least 95% of the PTV is covered. Here 38/40 = 0.95, so the coverage objective can be met while 40 − 38 = 2 cm³ of PTV is outside the prescription isodose. The RTOG conformity index is 52/40 = 1.30, not 38/40 and not the difference 52 − 40 = 12. Spill outside the PTV is 52 − 38 = 14 cm³. The net volume gap is 14 − 2 = 12 cm³, which hides both the spill and the miss. A Paddick index would be 38² / (40 × 52) = 1444/2080 = 0.694, not 1. The slice that looks wrapped does not show those 2 cm³ and 14 cm³ on the other slices.

### Q23
Stem: A PTV of 50 cm³ has a minimum DVH objective of D90 at the prescription dose, and D90 equals that dose. The prescription-isodose volume is also 50 cm³. The overlap of the PTV and the prescription isodose is 45 cm³. On the isodose display the prescription cloud is shifted off one side of the PTV. Which conclusion matches the numbers?
A. The RTOG index is 50/50 = 1, and D90 can still be met, while 5 cm³ of PTV is outside the prescription isodose and 5 cm³ of that isodose is outside the PTV
B. An index of 1 and a met D90 mean the prescription isodose and the PTV occupy the same space
C. The conformity index is 45/50 = 0.90, so the D90 objective cannot have been met
D. The missed 5 cm³ is the entire prescription-isodose volume
Answer: A
Objective: III.1
Why: Answer A. The RTOG conformity index is prescription-isodose volume divided by PTV volume: 50/50 = 1. That equality is size only. Overlap is 45 cm³, so 50 − 45 = 5 cm³ of PTV is missed and 50 − 45 = 5 cm³ of the prescription cloud sits outside the PTV. D90 covers 90% of 50 cm³, which is 45 cm³, so a D90 objective can be met at the same time the cloud is shifted. The ratio 45/50 = 0.90 is the coverage fraction, not the RTOG index, and it is exactly the coverage D90 describes. Paddick’s index is 45² / (50 × 50) = 2025/2500 = 0.81, which records the shift that an index of 1 does not.

### Q24
Stem: A thoracic plan is reviewed from this dose-volume reading. Combined lungs: volume 2500 cm³, and 900 cm³ receives at least 20 Gy. The lung limit is 30% or less of that volume. Spinal cord: volume 48 cm³, maximum dose 46 Gy. The cord limit is a maximum of 50 Gy. Which conclusion matches those limits?
A. Both pass, because 900 is less than 2500 and 46 is less than 900
B. The lungs fail and the cord passes
C. The cord fails and the lungs pass, because 46 is above 30 and 900 is below 50
D. Both fail, because each reported value is above 20
Answer: B
Objective: III.12
Why: Answer B. The lung fraction at 20 Gy is 900 divided by 2500, which is 0.36, or 36%. That is 6 percentage points over the 30% limit, so the lungs fail. The cord maximum is 46 Gy against a 50 Gy maximum, 4 Gy under the limit, so the cord passes. Choice A compares the raw cubic centimeters with each other. Choice C applies the lung percent to the cord dose and the cord dose to the lung volume. Choice D treats 20 as the limit for both rows.

### Q25
Stem: An evaluation sheet lists two structures. Both parotids, reported as one structure: volume 62 cm³, mean dose 29 Gy, limit a mean under 25 Gy. Rectum: volume 100 cm³, and 15 cm³ receives at least 70 Gy, limit under 20% of the rectum. Which conclusion matches those limits?
A. The parotids fail and the rectum passes
B. The rectum fails and the parotids pass, because 15 cm³ is a dose and 29 Gy is under 100
C. Both pass, because 29 is under 62 and 15 is under 100
D. Both fail, because 29 and 15 are both above 20
Answer: A
Objective: III.12
Why: Answer A. The parotid mean is 29 Gy. The limit is a mean under 25 Gy, and 29 is 4 Gy over that limit, so the parotids fail. The rectum fraction at 70 Gy is 15 divided by 100, which is 0.15, or 15%. That is 5 percentage points under the 20% limit, so the rectum passes. Choice B swaps the two rows. Choice C compares a dose with a volume. Choice D uses 20 as a cutoff for both the parotid mean and the rectal cubic centimeters.

### Q26
Stem: A prostate plan lists the rectum and the cord. Rectum: volume 80 cm³, and 20 cm³ receives at least 70 Gy. The rectum limit is under 20% of that volume. Spinal cord: volume 18 cm³, maximum dose 11 Gy. The cord limit is a maximum of 50 Gy. The cord sits outside the high-dose region. Which conclusion matches those limits?
A. Both pass, because 20 cm³ is under 80 cm³ and 11 Gy is under 50 Gy
B. The cord fails because any cord dose fails a 50 Gy maximum, and the rectum passes because 20 cm³ is under 80 cm³
C. Both fail, because 20 cm³ and 11 Gy are each above zero
D. The rectum fails and the cord passes
Answer: D
Objective: III.12
Why: Answer D. The rectum fraction at 70 Gy is 20 divided by 80, which is 0.25, or 25%. The limit is under 20%, and 25% is 5 percentage points over it, so the rectum fails. The cord maximum is 11 Gy against a 50 Gy maximum, so the cord passes. A cold cord does not repair the rectal row. Choice A stops at 20 cm³ being smaller than 80 cm³ and never forms the percent. Choice B treats the cord maximum as a ban on any cord dose. Choice C fails every row that is above zero.

### Q27
Stem: A second thoracic plan is reviewed from this dose-volume reading. Combined lungs: volume 4000 cm³, and 1000 cm³ receives at least 20 Gy. The lung limit is 30% or less of that volume. Spinal cord: volume 44 cm³, maximum dose 53 Gy. The cord limit is a maximum of 50 Gy. Which conclusion matches those limits?
A. Both fail
B. The lungs fail and the cord passes, because 1000 is above 30 and 53 is under 4000
C. The lungs pass and the cord fails
D. Both pass, because 25 is under 53
Answer: C
Objective: III.12
Why: Answer C. The lung fraction at 20 Gy is 1000 divided by 4000, which is 0.25, or 25%. That is 5 percentage points under the 30% limit, so the lungs pass. The cord maximum is 53 Gy against a 50 Gy maximum, 3 Gy over the limit, so the cord fails. Choice A fails the lungs on a row that meets 30%. Choice B compares 1000 cm³ with 30 percent and 53 Gy with 4000 cm³. Choice D compares the lung percent with the cord dose.

### Q28
Stem: Three rows are printed on one evaluation sheet, and each row has its own limit. Spinal cord: volume 30 cm³, maximum 49 Gy, limit a maximum of 50 Gy. Combined lungs: volume 3500 cm³, and 1400 cm³ receives at least 20 Gy, limit 30% or less of that volume. Both parotids, as one structure: volume 48 cm³, mean dose 16 Gy, limit a mean under 25 Gy. Which rows fail?
A. All three fail
B. Only the lungs fail
C. The cord and the lungs fail, and the parotids pass
D. Only the parotids fail, because 16 Gy is less than 25 Gy
Answer: B
Objective: III.12
Why: Answer B. The cord at 49 Gy is 1 Gy under a 50 Gy maximum, so the cord passes. The lung fraction at 20 Gy is 1400 divided by 3500, which is 0.40, or 40%, and 40% is 10 percentage points over 30%, so the lungs fail. The parotid mean of 16 Gy is 9 Gy under a mean limit of 25 Gy, so the parotids pass. A dose under its limit is a pass. Choice A and choice C fail the cord. Choice D treats the parotid margin under 25 Gy as a failure.

### Q29
Stem: A head-and-neck plan is prescribed to 66 Gy. The objective list and the dose-volume reading are: spinal cord, volume 40 cm³, maximum 45 Gy, limit a maximum of 50 Gy; both parotids, volume 50 cm³, mean 22 Gy, limit a mean under 25 Gy. The oral cavity is outside the PTV, volume 110 cm³, and it has no objective. The isodose display shows 73 Gy inside the oral cavity. Which finding does that review support?
A. The parotids fail, because 22 is under 25
B. The cord fails, because 45 is above 30
C. The plan is clear. Every objective is met, and a structure with no objective receives no dose
D. The oral cavity contains 73 Gy and had no objective, while the cord and the parotids meet their limits
Answer: D
Objective: III.12
Why: Answer D. The cord at 45 Gy is 5 Gy under 50 Gy, and the parotid mean of 22 Gy is 3 Gy under 25 Gy, so both objectives are met. The oral cavity had no objective, and the isodose display still shows 73 Gy there, which is 7 Gy above the 66 Gy prescription. An objective constrains only the structure it is attached to. Dose is deposited in a contoured structure whether or not an objective exists. Choice A and choice B turn passing rows into failures. Choice C treats a missing objective as a missing dose.

### Q30
Stem: A thoracic plan is prescribed to 60 Gy. The objective list and the dose-volume reading are: combined lungs, volume 3200 cm³, 640 cm³ receives at least 20 Gy, limit 30% or less; spinal cord, volume 28 cm³, maximum 42 Gy, limit a maximum of 50 Gy. The brachial plexus is outside the PTV, volume 8 cm³, maximum 69 Gy, and it has no objective. Which finding does that review support?
A. The plexus contains 69 Gy and had no objective, while the lungs and the cord meet their limits
B. The lungs fail, because 640 cm³ is greater than 30
C. The cord fails, because 42 is greater than 30
D. The plan is clear, because a structure with no objective is left out of the dose calculation
Answer: A
Objective: III.12
Why: Answer A. The lung fraction at 20 Gy is 640 divided by 3200, which is 0.20, or 20%. That is 10 percentage points under the 30% limit, so the lungs pass. The cord at 42 Gy is 8 Gy under 50 Gy, so the cord passes. The plexus maximum is 69 Gy, which is 9 Gy above the 60 Gy prescription, and the plexus had no objective. The objective score stays quiet on that 69 Gy region. Choice B compares cubic centimeters with a percent. Choice C compares the cord dose with the lung percent. Choice D leaves the plexus out of the calculation; the dose grid still scores every contoured voxel.

### Q31
Stem: A PTV has a volume of 120 cm³. The prescription isodose encloses 90 cm³. The overlap of the PTV and that prescription isodose is 84 cm³. Which reading of the conformity is justified?
A. The target is fully covered, because the PTV is larger than the prescription cloud
B. The volumes match, so the overlap of 84 cm³ means the index is 1
C. The prescription cloud is smaller than the PTV, and 36 cm³ of the PTV lies outside that cloud
D. The missed PTV is the 6 cm³ of prescription cloud outside the PTV, so coverage is complete
Answer: C
Objective: III.1
Why: Answer C. The conformity comparison of prescription-isodose volume to PTV volume is 90 divided by 120, or 0.75. The prescription cloud is smaller than the target, so the target cannot be fully covered. The PTV outside the prescription isodose is 120 minus 84, which is 36 cm³. The prescription cloud outside the PTV is 90 minus 84, which is 6 cm³. Choice A treats a larger PTV as proof of coverage. Choice B calls unequal volumes a match. Choice D names the spill and calls it the miss. The overlap index that squares 84 and divides by 120 times 90 is 7056 divided by 10800, or 0.65, and that score is pulled down by the uncovered target.

### Q32
Stem: Two plans use the same PTV volume, 70 cm³, and the same prescription-isodose volume, 84 cm³. In plan A the overlap is 70 cm³. In plan B the overlap is 60 cm³. Which statement is justified?
A. The plans are equally conformal, because both prescription clouds are 84 cm³ around a 70 cm³ PTV
B. Plan A covers the whole PTV. Plan B leaves 10 cm³ of PTV outside the prescription isodose. The shared volumes hide that difference
C. Plan B is more conformal, because its overlap is the smaller number
D. Both plans miss 14 cm³ of PTV, because 84 minus 70 is 14
Answer: B
Objective: III.1
Why: Answer B. Both plans have the same size comparison, 84 divided by 70, or 1.20. Size does not locate the cloud. Plan A overlap equals the PTV, so the whole 70 cm³ is covered and the 14 cm³ difference sits outside the PTV as spill. Plan B overlap is 60 cm³, so 70 minus 60 is 10 cm³ of PTV outside the prescription isodose, and 84 minus 60 is 24 cm³ of prescription cloud outside the PTV. Choice A stops at the shared volumes. Choice C treats a smaller overlap as a better score. Choice D calls the 14 cm³ volume difference a miss on both plans, including the plan that covers the PTV.

### Q33
Stem: Plan A reports a near-maximum of 71 Gy, a median of 65 Gy, and a near-minimum of 56 Gy. Plan B reports a near-maximum of 67 Gy, a median of 65 Gy, and a near-minimum of 63 Gy. Which reading matches the ICRU homogeneity comparison?
A. Plan B is more homogeneous. Its spread from near-maximum to near-minimum is 4 Gy, and Plan A's spread is 15 Gy. Divided by the shared median, those spreads are about 0.06 and about 0.23
B. Plan A is more homogeneous, because 71 Gy is higher than 67 Gy
C. The plans match, because both medians are 65 Gy
D. Homogeneity is the near-minimum alone, so Plan A is the more homogeneous plan
Answer: A
Objective: III.1
Why: Answer A. ICRU homogeneity compares the near-maximum, the near-minimum, and the median. Plan A runs from 56 Gy to 71 Gy, a spread of 15 Gy. Divided by the median, 15 divided by 65 is 0.231. Plan B runs from 63 Gy to 67 Gy, a spread of 4 Gy. Divided by the same median, 4 divided by 65 is 0.062. The smaller result is the more homogeneous plan, so Plan B is more homogeneous. Choice B treats a higher near-maximum as an advantage. Choice C equates equal medians with equal homogeneity. Choice D treats the colder near-minimum as the better score.

## Target Volume Definitions, Isodose Distributions, and Dose Metrics Quiz

### Q1
Stem: For the volumes in the previous conformity problem (PTV 20 cm³, prescription isodose volume 24 cm³, overlap 19 cm³), what is the Paddick conformity index, TV_PIV² / (TV × PIV)?
A. 1.20
B. 0.75
C. 0.95
D. 19
Answer: B
Objective: III.1
Why: Answer B. Paddick's index is the square of the overlapping volume, divided by the product of the target volume and the prescription-isodose volume. Overlap squared is 19 × 19 = 361. The product of the volumes is 20 × 24 = 480. The index is 361/480 = 0.752, or 0.75. A perfect plan that covers the target exactly with no spill has an index of 1. This plan loses points twice: once because 1 cm³ of PTV is missed (the 19 instead of 20) and once because the prescription volume is 24 cm³ rather than 20 cm³. The RTOG index of 1.20 does not catch the miss. The raw overlap, 19 cm³, is not an index.

### Q2
Stem: An ICRU 83 report lists PTV D2% = 53.5 Gy, D98% = 46.5 Gy, and D50% = 50.0 Gy. What is the homogeneity index (D2% − D98%)/D50%, and which plan is more homogeneous, this one or a plan with an index of 0.05?
A. This index is 0.14; the plan with index 0.05 is more homogeneous
B. This index is 0.14; the higher index is more homogeneous
C. This index is 7 Gy; homogeneity indexes are reported only in gray
D. This index is 1.07, the ratio D2%/D50%
Answer: A
Objective: III.11
Why: Answer A. Subtract the near-minimum from the near-maximum: 53.5 − 46.5 = 7.0 Gy. Divide by the median: 7.0/50.0 = 0.14. A smaller index means the dose across the PTV is tighter, so 0.05 is the more homogeneous plan. Reporting 7 Gy alone skips the normalization to D50% that makes plans of different prescriptions comparable. The ratio 53.5/50 = 1.07 is a different description of the hot end and is not this index.

### Q3
Stem: A cumulative DVH of a PTV shows that 95% of the volume receives at least 50 Gy. Which statement is the correct reading?
A. D95 is 50 Gy, which means 95% of the PTV is at or above 50 Gy
B. V95 is 50%, because the axes of a cumulative DVH are interchangeable
C. 95% of the prescription is 50 Gy, so the prescription is 52.6 Gy
D. The differential DVH is a spike at 95 Gy
Answer: A
Objective: III.12
Why: Answer A. On a cumulative DVH the statement "95% of the volume receives at least 50 Gy" is exactly the definition of D95 = 50 Gy, and it is also V50Gy = 95%. It does not mean that a differential histogram has a bar at 95 Gy. The axes are not interchangeable: swapping dose and volume turns D95 into a different metric. You cannot recover the prescription from D95 unless the protocol says the prescription is defined as D95. If this protocol does define coverage as D95 equal to 50 Gy, then the prescription is 50 Gy, not 50/0.95.

### Q4
Stem: A differential DVH of a PTV is a single narrow peak centered at 50 Gy. A second plan's differential DVH is a broad hump from 40 Gy to 60 Gy with the same mean dose of 50 Gy. What does the narrow peak mean?
A. The first plan is less homogeneous, because a peak means a hot spot
B. The first plan is more homogeneous: most of the volume receives nearly the same dose
C. The two plans have the same homogeneity index by definition, because the means match
D. The narrow peak means 50% of the volume receives 0 Gy
Answer: B
Objective: III.1
Why: Answer B. In a differential DVH, height is volume in that dose bin. A narrow peak means almost all the voxels sit near one dose, which is a homogeneous target. A broad hump with the same mean has cold voxels near 40 Gy and hot voxels near 60 Gy. The means matching does not make the homogeneity indexes match; ICRU homogeneity uses D2% and D98%, which spread out when the hump widens. Cumulative curves show the same fact differently: the homogeneous plan stays flat and then drops almost vertically at 50 Gy, while the broad plan slopes down across 40 to 60 Gy.

### Q5
Stem: A planner evaluates a cord with a cumulative DVH and a maximum of 45 Gy, inside a 50 Gy limit. The isodose display shows that the 45 Gy region is inside the contoured cord, but the contour was never drawn on the three slices where a 54 Gy finger crosses the canal. The DVH is still under the limit. Which conclusion is justified?
A. The cord is safe because a DVH maximum is a complete description of the organ
B. The DVH only knows the cord that was contoured; the uncontoured slices can exceed the limit without moving the histogram
C. A cumulative DVH includes dose outside the contour as long as the structure name is "cord"
D. Differential DVHs catch missing slices and cumulative DVHs do not, so switching plot type fixes the contour
Answer: B
Objective: III.1
Why: Answer B. Both differential and cumulative histograms are computed on the voxels inside the structure. Missing slices are missing voxels. A 54 Gy finger through an uncontoured canal does not appear, and the reported 45 Gy maximum is the maximum of an incomplete organ. The isodose review is what catches it. Switching from cumulative to differential does not invent the missing contour. This is also why a DVH cannot prove that the contour, the dose grid, or the image registration was right.

### Q6
Stem: The treated volume and the PTV are being reviewed on an isodose chart rather than on a DVH. The 95% isodose covers the PTV and also spills 1.5 cm into the liver outside the PTV. The spill is a connected region about 2 cm across. How should that spill be classified using ICRU language?
A. As part of the GTV, because it receives 95% of the prescription
B. As a hot spot only if it exceeds 107%, and otherwise as neither treated volume nor irradiated volume
C. The 95% cloud is the treated volume and is larger than the PTV; if 95% of the prescription is above the normal-tissue dose the physician calls significant, that spill is also inside the irradiated volume
D. As a planning organ-at-risk volume for the liver
Answer: C
Objective: III.11
Why: Answer C. The treated volume is whatever the chosen therapeutic isodose encloses, here the 95% cloud, and it is allowed to be larger than the PTV. The liver lying in that spill is being treated in the geometric sense even though it is not target. Whether it is also part of the irradiated volume depends on whether that dose is significant for liver tolerance; a dose high enough to be the prescription almost always is. A hot spot in the ICRU 50 sense is dose above 100% of the specification outside the PTV, significant when it is about 15 mm across or more. This spill is at 95%, so it may not meet the "above 100%" hot-spot test, and it is still a conformity problem. It is not GTV and it is not a PRV, which would be a margin on a contoured liver.
