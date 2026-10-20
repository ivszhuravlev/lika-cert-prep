# Module 18. IGRT

This module is the toolbox: which image is acquired, what anatomy it can show, and how a match becomes a couch correction. The ways those images mislead you are module 32. Learn the tool here, then learn its limits.

## Treatment Verification

**MDCB objectives:** II.6, I.8

**What the exam expects**

You can name the common image-guidance methods and the anatomy each one actually sees. You can say what the reference image is (planning CT or DRR from that CT). You can describe a shift as a rigid correction in the patient coordinate system, including the difference between a three-degree couch and a six-degree couch. You can separate imaging used to aim the beam from the planning CT used to calculate dose.

**Core facts**

Image guidance compares the patient on the treatment table with the patient the plan was calculated on. The comparison produces a rigid correction: translations, and rotations if the couch and the protocol allow them. After the couch moves, a second image is the confirmation that the correction landed.

The reference for a cone-beam or a CT-on-rails match is the planning CT, in the same orientation (head-first supine or whatever was simulated). The reference for a portal image is the digitally reconstructed radiograph from that planning CT in the same beam’s-eye view. Matching today to yesterday’s cone-beam walks the isocenter off the anatomy that was planned.

What each method can show:

| Method | What you can verify |
| --- | --- |
| kV orthogonal pair | Bone and fiducials on two projections. Two 2D images support a 3D translation. Soft tissue and rotation are weak. |
| MV portal / EPID | The treatment aperture in the beam’s-eye view, and bony alignment. Soft-tissue contrast is poor. This is the image of the beam you are about to treat with. |
| kV CBCT | A volume: soft tissue, bone, fiducials, bladder filling, rectal gas. Acquired on the linac. Used to align. It is a different dataset from the planning CT. |
| MVCT (helical tomotherapy) | A volume from the treatment-energy beam, detuned for imaging. Soft-tissue contrast is less than kV CBCT. It is the onboard image for that machine. |
| Fiducial match | Marker position as a surrogate for the target (prostate, liver). The marker is not the GTV. |
| Surface guidance (SGRT) | The external surface, often in real time, including breath-hold. Internal targets that are not locked to that surface are invisible to it. |
| Fluoroscopy or electromagnetic tracking | Intrafraction motion of a surrogate. |

Daily imaging is the usual expectation for stereotactic treatments and for many modulated courses. The required frequency and the shift that triggers a physician or a physics review are departmental. Confirm those action levels in the departmental IGRT policy. AAPM TG-142 is the machine QA document for the imager (geometry, image quality, isocenter coincidence). A TG-142 imaging tolerance is not the same number as the clinical margin or the clinical action level.

A practical verification sequence:

1. Confirm the patient, the site, the plan, the energy, and the accessories (bolus, mask, knee rest).
2. Acquire the image the protocol names.
3. Match on the anatomy the protocol names. Pelvic bone, prostate soft tissue, fiducials, and surface are four different matches.
4. Apply the translation. Apply a rotation only when the couch has that degree of freedom and the protocol allows it.
5. Decide whether the residual, or the size of the shift, needs a repeat image.
6. Treat. For gated or breath-hold treatment, the gating trace has to match the simulated phase or the simulated deep-inspiration level, not merely the average free-breathing surface.

Cone-beam geometry is a cone, so one rotation covers a limited length and a limited diameter. Anatomy outside that field of view is truncated. The Hounsfield numbers are not the commissioned planning-CT density table. Module 32 is the full list of reasons a cone-beam must not be dropped into the dose engine as if it were the simulation CT.

Respiratory motion management is verified, not assumed. A four-dimensional planning CT defined an internal target over the breathing cycle. Guidance has to confirm that today’s motion is the motion that was planned: amplitude, phase, breath-hold level, or an internal surrogate such as an implanted marker. Surface guidance is well suited to a breast deep-inspiration breath hold because the target is tied to the surface. It is a poor sole check for a prostate.

Shifts are reported in a coordinate system. Know the sign convention your department uses (IEC couch coordinates versus patient left–right). A correctly computed 0.7 cm left shift applied with the opposite sign is a 1.4 cm error. Read the direction in the room, not only the number on the screen.

**Formulas**

The couch correction is rigid. The same small-angle estimate used for registrations tells you when a rotation matters. A point a distance r from the match center, rotated by an angle θ in radians, is displaced by about rθ.

Example: the match is centered at the nasopharynx. A supraclavicular node is 20 cm inferior. The proposed correction is a 2° pitch and no translation.

2° = 2 × π / 180 = 0.0349 rad.

Displacement at the node ≈ 20 × 0.0349 = 0.70 cm.

Seven millimeters at the end of the field is a real setup change. On a three-degree-of-freedom couch you cannot apply that pitch. You then either accept a compromise translation or reset the patient. On a six-degree couch you can apply it only if the protocol says rotations of that size are allowed, and you still re-image.

**Traps**

- Using yesterday’s cone-beam as the new reference.
- Matching bone for a target that moves inside the pelvis or the lung.
- Treating a surface-guidance camera as an internal image.
- Reading a TG-142 imager tolerance as the clinical PTV margin.
- Applying a rotation the couch cannot perform, or applying the correct centimeters in the wrong direction.
- Calling a portal image a soft-tissue volumetric match. A portal image shows the aperture and the bone in that beam’s-eye view.

**Sources**

- AAPM TG-142, quality assurance of medical accelerators, including imaging geometry. Monthly coincidence of imaging and treatment isocenters is ≤2 mm (≤1 mm for SRS/SBRT). That machine test is not a site’s clinical action level.
- AAPM TG-179, quality assurance for CT-based image guidance
- AAPM TG-147, nonradiographic localization, including surface imaging
- AAPM TG-75 and TG-180, management of imaging dose. A cone-beam dose is real. No single patient dose is stated here, because it depends on the protocol.
- ICRU 62, setup margin and internal margin, which are the uncertainties image guidance is trying to shrink
- de Boer and Heijmen, the no-action-level (NAL) and extended NAL (eNAL) offline setup protocols

## When the shift is enough

**MDCB:** II.6

**What the exam expects**

You can decide from the image and the departmental policy whether the team finishes localization and treats, or whether the fraction stops for a physician. You can separate online correction from offline NAL and eNAL. You know a kilovoltage cone-beam dose is not zero. You know an MR-linac adaptive trigger is a protocol concept for when a rigid shift is the wrong tool. You do not invent a millimeter action level for a site.

**Core facts**

The departmental IGRT policy names, for each site and technique, what the treating team may correct and what finding stops the fraction for a physician. Physics is included when that policy says so. The clinical rule is not the TG-142 test of imaging-to-treatment isocenter coincidence: ≤2 mm for a non-stereotactic machine and ≤1 mm for SRS/SBRT. A passed monthly isocenter test does not write the prostate action level.

In tolerance. The match is on the anatomy the protocol names. Filling, body shape, and devices agree with the plan. The correction is a rigid shift the couch can apply, and its size is inside the action level for that site. Complete the localization the policy allows and treat. A nonzero shift inside that level is not, by itself, a physician call.

Stop and call. The correction is outside the action level. Or the image shows a change a rigid shift cannot restore: bladder empty on a full-bladder plan, rectum full of gas with the prostate moved off the nodes, a mask bridging the neck, a weight change that puts an organ in the high dose. A bone residual driven under the action level does not clear that image. Lasers on the tattoos do not either. Hold the beam and call the physician. Averaging a bone shift with a soft-tissue shift forces a number under the limit and satisfies neither anatomy.

Online and offline. Online correction acquires the image and applies the shift before that fraction is treated. It addresses today’s setup, systematic and random, within what a rigid couch can do. Offline review looks after the fraction, or before a later one, and changes the setup for future fractions.

NAL, the no-action-level protocol, is offline. The mean setup error from an initial set of images estimates the systematic error, and that correction is applied on later fractions with no threshold. eNAL, extended NAL, repeats the estimate on later images so a drift is caught, and the update applies to future fractions. Neither protocol moves the couch for today’s random residual before beam-on. That step is online correction. Neither protocol replans the dose.

Imaging dose. A kilovoltage cone-beam deposits dose. Daily imaging adds that dose every fraction. It is small beside a therapeutic fraction, and it is not zero. It is not the prescription. It does not appear in the therapeutic dose grid unless the department has a validated way to include it. The dose is deposited when the scan runs, whether or not the shift is large. Skipping a required image does not remove the localization error the image was for.

MR-linac adaptive trigger. The clinic defines what finding starts a replan instead of a couch shift. A pure translation with stable organ shape is localization. A shape change, an organ at risk in the high dose, or a target a rigid shift cannot restore is the kind of finding that triggers adaptation and a physician review. There is no universal millimeter for that trigger in this note. How the adapted plan is checked is module 28.

**Traps**

A TG-142 isocenter tolerance copied in as every site’s action level. A bone residual inside the action level accepted while the protocol’s soft-tissue target is outside it. NAL described as an online shift or as a same-day replan. Cone-beam dose called zero because the beam is kilovoltage, or subtracted one-for-one from the prescription. Every MR-linac image treated as an automatic replan.

## IGRT Mini-Quiz

**MDCB objectives:** II.6, I.8

**Skills this quiz trains**

- Match the image type to the anatomy it can prove: bone, aperture, soft tissue, fiducial, or surface.
- Name the planning CT or the DRR as the reference, and keep a prior cone-beam from becoming the reference.
- Separate a translation-only couch from a six-degree couch.
- Estimate the displacement at the end of a long target from a small rotation.
- State that cone-beam Hounsfield numbers are not the planning density table.
- Place TG-142 on the imager and the departmental policy on the clinical action level.
- Decide when an in-tolerance rigid shift is treated and when the image requires a physician.
- Separate online correction from offline NAL and eNAL.
- Treat cone-beam dose as real and separate from the prescription.
- Treat an MR-linac adaptive trigger as a protocol concept, not a universal millimeter.

**Traps**

- Bone match accepted for prostate localization.
- Surface guidance accepted as proof the prostate or a lung tumor is on target.
- Portal image described as a soft-tissue 3D match.
- A 2° rotation dismissed at a site 20 cm from the match point.
- Imaging QA tolerance copied in as the PTV expansion.

**Check yourself**

A left breast deep-inspiration breath-hold plan is monitored with surface guidance, and the surface is within the departmental tolerance for the whole fraction. A prostate plan the same afternoon is also on the surface-guidance system, with an equally quiet surface trace and no cone-beam and no fiducials. Which case has the target tied to the signal the camera can see?

Walk-through: The breast target moves with the chest wall, so the surface is a direct surrogate for that treatment. The prostate moves with rectum and bladder and is invisible to a surface camera. A quiet skin trace does not locate the prostate. That prostate fraction still needs the internal check the protocol names (fiducials or soft-tissue cone-beam).

## CBCT Physics and Named Localization Systems

**Objectives:** II.6, I.8

**What the exam expects**

You can describe how a cone-beam image is formed and reconstructed, and you can choose between a full-fan and a half-fan acquisition. You know what the detector is made of, why a bowtie filter is in the beam, and how kilovoltage and megavoltage cone-beams differ in contrast and dose. You can give a typical dose for one kilovoltage cone-beam and scale it over a course. You can describe the stereoscopic kilovoltage system, transrectal ultrasound, and surface guidance as named tools, and you can run an offline correction protocol with an action level.

**Core facts**

How a cone-beam is made. A kilovoltage x-ray tube and a flat-panel detector are mounted on the gantry at right angles to the treatment head. As the gantry rotates, several hundred two-dimensional projections are acquired through the whole volume at once, and the volume is reconstructed by filtered back projection, the cone-beam (Feldkamp) version of the same algorithm a diagnostic CT uses. Because the whole length of the volume is irradiated in one rotation, the scatter reaching the panel is far larger than in a fan-beam scanner, which lowers contrast, produces cupping, and makes the Hounsfield numbers unreliable for dose calculation. Iterative reconstruction is available on newer systems and reduces noise but does not remove scatter.

Full-fan versus half-fan. In a full-fan scan the detector is centered on the beam axis, every projection covers the whole cross-section, and a rotation of about 200 degrees is enough; the reconstructed diameter is around 25 cm, which fits a head or a neck. In a half-fan scan the detector is shifted sideways so each projection covers roughly one half of the patient, a full 360-degree rotation is needed to see both halves, and the reconstructed diameter grows to around 45 to 50 cm, which fits a pelvis or a thorax. Each mode has its own bowtie filter. The bowtie is thick at the edges and thin in the middle, so it attenuates the beam where the patient is thin, evens out the signal across the panel, cuts skin dose at the periphery, and reduces the scatter that drives cupping. Scanning a pelvis in full-fan mode truncates the anatomy and produces a ring of bright artifact at the edge of the field of view.

The detector. The flat panel is amorphous silicon, a large array of thin-film photodiodes and switches read out electronically. An indirect panel places a cesium iodide or gadolinium oxysulfide scintillator over the silicon; the scintillator converts x-rays to light and the photodiodes convert light to charge. The same panel technology, with a thicker build-up plate, is the electronic portal imaging device on the megavoltage side. Panels are calibrated for dark current, gain, and dead pixels, and a dropped calibration shows as ring artifacts.

Kilovoltage versus megavoltage cone-beam. Kilovoltage photons still interact partly by the photoelectric effect, so bone and soft tissue separate and a kilovoltage cone-beam shows prostate, bladder, and a lung tumor. A megavoltage cone-beam taken with the treatment beam at low monitor units is almost pure Compton interaction, so contrast tracks electron density only, soft-tissue detail is poor, and the dose per scan is several times higher. Its advantages are that it is unaffected by metal streak artifacts from hips or dental work and that it is acquired with the treatment beam through the treatment isocenter. Helical tomotherapy uses a detuned megavoltage fan beam for the same purpose.

Imaging dose. A kilovoltage cone-beam typically deposits on the order of 1 to 3 cGy to the imaged volume; TG-180 quotes organ doses of roughly 0.5 to 5 cGy per scan, with the pelvis at the high end and the head at the low end. Daily imaging over a 35-fraction course adds tens of centigray, about 1 percent of a 70 Gy prescription. TG-180 suggests accounting for imaging dose when it reaches roughly 5 percent of the therapeutic dose, which is unusual for kilovoltage imaging and more likely with daily megavoltage imaging. Protocols that reduce the dose use a lower tube current, a shorter arc, or a smaller field of view, and skip imaging that the protocol does not require. The dose is deposited whether the shift turns out to be large or zero.

Stereoscopic kilovoltage system. The ExacTrac design mounts two kilovoltage tubes in the floor and two flat panels in the ceiling so that two oblique projections through the isocenter are taken at once. An infrared camera tracks reflective body markers for pre-positioning, the stereoscopic pair is fused to digitally reconstructed radiographs to find translations and rotations, and a six-degree-of-freedom robotic couch applies the correction. Images can be taken at any gantry angle during treatment, so the system also catches intrafraction motion. It matches bone or implanted fiducials and does not see soft tissue; cranial radiosurgery and spine stereotactic treatments are its usual applications. The robotic radiosurgery system uses the same geometry inverted, with ceiling tubes and floor panels, and corrects by moving the robot rather than the couch.

Transrectal ultrasound. For prostate brachytherapy the imaging that guides the needles is transrectal ultrasound, a probe in the rectum on a stepper that is mechanically registered to the needle template. The volume study for planning, the live needle placement, and the intraoperative seed or catheter check are all done on the same probe, with no ionizing radiation and in the treatment position. Its limits are operator dependence, probe pressure that deforms the gland, and difficulty seeing seeds once many are in place, which is why a postimplant CT is still done. Transabdominal ultrasound was an early external-beam prostate localization tool with the same probe-pressure problem.

Surface guidance. Three camera pods project a structured light pattern onto the patient and reconstruct the surface many times per second, comparing it with a reference surface from the planning CT body contour or from a surface captured at the first fraction. The system reports six-degree-of-freedom deviations continuously, with no dose, and can hold the beam when the surface leaves tolerance. It is well suited to breast, deep-inspiration breath hold, extremities, and open-face-mask cranial radiosurgery, and it supports tattoo-free setup. It fails when the surface is covered by a blanket or a bolus sheet, loses accuracy on a very large patient, and never sees an internal target that is not locked to the skin.

Correction protocols and action levels. An online protocol images every fraction, applies the shift before the beam, and reduces both systematic and random error. An offline protocol images the first several fractions, usually three to five, averages the measured shifts to estimate the systematic error, and applies that average from the next fraction on without a daily image; it reduces the systematic component only. The action level is the shift below which no correction is applied, so the team does not chase millimeter noise; above it the couch moves and, past a second larger level, the patient is re-imaged or reset. Image guidance shrinks the setup component of the PTV margin; it does not shrink the ITV, which is a motion volume defined at planning.

**Formulas**

Course imaging dose ≈ dose per scan × number of scans; 2 cGy × 35 scans = 70 cGy, and 70 / 7,000 = 1 percent of a 70 Gy prescription.

Offline systematic correction = mean of the first n measured shifts, applied from fraction n + 1.

**Worked example (offline protocol)**

Given: an offline protocol images the first four fractions and the anterior-posterior shifts are +4, +2, +5, and +1 mm, with positive meaning posterior. Mean = (4 + 2 + 5 + 1) / 4 = 12 / 4 = 3 mm posterior. Check: the deviations from 3 are +1, −1, +2, −2 and sum to zero. From fraction five the couch is set 3 mm posterior of the tattoos at every fraction without imaging. The 1 to 2 mm day-to-day scatter around that mean is random and remains in the margin. Had the first-day shift of 4 mm been used alone, the correction would have carried one day's random error into every later fraction.

**Traps**

- Describing cone-beam reconstruction as a simple sum of projections. The projections are filtered before back projection.
- Choosing full-fan for a pelvis; the field of view truncates the patient.
- Calling the flat panel a film cassette or an image intensifier. It is an amorphous-silicon array with a scintillator.
- Saying a megavoltage cone-beam has better soft-tissue contrast, or that a kilovoltage cone-beam has zero dose.
- Describing the stereoscopic system as a soft-tissue imager. It matches bone and fiducials.
- Expecting an offline protocol to correct a fraction's random error, or an online protocol to shrink the ITV.

**Sources**

- AAPM TG-179, quality assurance for image-guided radiation therapy using CT-based technologies, for cone-beam geometry and image quality tests.
- AAPM TG-180, image guidance doses delivered during radiotherapy, for the per-scan dose ranges and the 5 percent accounting threshold.
- AAPM TG-147, nonradiographic localization, for surface imaging and electromagnetic systems.
- AAPM TG-142 for imaging-to-treatment isocenter coincidence tolerances.
- de Boer and Heijmen for the offline no-action-level protocol.

## Tracking System Geometry and 4D-CT Modes

**Objectives:** II.6

Items on tracking systems ask where the hardware sits and what each system can and cannot see, and 4D-CT items ask whether the images were sorted before or after acquisition.

Prospective versus retrospective 4D-CT. In a prospective acquisition the respiratory signal triggers the scanner, so images are acquired only inside a chosen gate (for example, end-exhale at 30 to 70% of the cycle). The product is one image set at one breathing phase, with lower dose and no sorting artifacts, and it is the right data set when the patient will be treated with gating in that same window. In a retrospective acquisition the scanner runs continuously (cine or low-pitch helical) while the respiratory trace is recorded, and the images are binned afterward into typically ten phase bins or into amplitude bins. The product is the whole breathing cycle: a maximum-intensity projection for the ITV, an average-intensity image for the dose calculation, and any phase for a gating or tracking plan. Retrospective 4D-CT costs several times the dose of a single helical scan and shows duplicated or missing anatomy when breathing is irregular. The standard 4D-CT used for lung SBRT planning is retrospective.

CyberKnife. A compact 6 MV linac on a robotic arm delivers hundreds of non-coplanar beams. Its imaging is two kilovoltage x-ray tubes mounted in the ceiling, aimed down at the isocenter, with two flat-panel detectors flush in the floor. The two oblique projections are compared with digitally reconstructed radiographs to localize the skull (6D skull tracking), the spine (Xsight spine), or implanted fiducials (fiducial tracking); the robot then corrects the beam direction rather than moving the couch. For respiratory motion the Synchrony system reads infrared markers on a vest with a camera, builds a correlation model between the surface and the fiducial or lung tumor position from periodic x-ray pairs, and moves the robot in real time to follow the model; the x-rays are repeated every 30 to 60 seconds to update the model. Note the geometry: tubes in the ceiling, detectors in the floor, which is the reverse of ExacTrac.

ExacTrac. Two kilovoltage x-ray tubes are recessed in the floor on either side of the couch, aimed up through the isocenter at two flat-panel detectors mounted on the ceiling. An infrared camera tracks reflective markers on the patient or on a frame and drives a robotic couch with six degrees of freedom; the stereoscopic x-ray pair, matched to DRRs on bone or implanted fiducials, verifies and corrects the position with sub-millimeter residuals. It is used for intracranial and spine SRS and for frameless setups, and it can be fired during gantry rotation at angles where the panels are not blocked. It does not image soft tissue directly, and the infrared system by itself only sees the surface. Mnemonic: ExacTrac floor tubes, ceiling panels; CyberKnife ceiling tubes, floor panels.

Electromagnetic transponders. The Calypso system (now Varian) implants three wireless transponders ("beacons"), each a small glass capsule with a resonant circuit, in or around the target. A flat array positioned over the patient excites the beacons at their individual frequencies and reads their positions about ten times per second; infrared cameras locate the array relative to the room isocenter. Three beacons are needed because three points define the centroid, the rotation and the inter-beacon distances that reveal migration or prostate deformation. There is no imaging dose, the beacons are continuously tracked during the beam, and the system can hold the beam if the target leaves a tolerance box. It is used far more in prostate than in lung: the prostate is a well-defined, non-deforming organ where beacon migration is minimal and the dominant problem is slow intrafraction drift from rectal and bladder filling, which the system catches well. In lung the beacons must be placed bronchoscopically with a pneumothorax risk, they can migrate in soft lung tissue, the beacon-to-array distance can exceed the system range in large patients, and the fast, large respiratory motion is better handled by gating or correlation-model tracking. The beacons also create MRI susceptibility artifacts of a centimeter or more, which matters for MRI-based prostate planning.

**Traps**

Prospective 4D-CT said to produce ten phases. CyberKnife and ExacTrac geometries swapped. ExacTrac described as a soft-tissue imager. Calypso described as an imaging device or as using two beacons. Transponders described as more common in lung than prostate. Synchrony described as tracking the tumor directly without a surrogate model.

**Sources**

AAPM TG-76 (respiratory motion) for 4D-CT acquisition modes. AAPM TG-147 (nonradiographic localization) for electromagnetic and infrared systems. AAPM TG-135 (robotic radiosurgery QA) for the CyberKnife imaging geometry. Vendor technical descriptions of ExacTrac and Calypso.
