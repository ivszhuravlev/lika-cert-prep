# Module 13 — Acquisition of Patient Data

Original items on data integrity, contour corrections, and heterogeneity.

## General Introduction

### Q1
Stem: Acquisition of patient data sits mainly in which exam domain?
A. Localization
B. Brachytherapy
C. Radiation protection
D. Quality assurance only, with no planning consequence
Answer: A
Objective: II.1
Why: Managing, importing, and validating the data set is a localization task. A bad data set still changes the plan, but the blueprint home for this work is localization, not brachytherapy or personnel protection.

### Q2
Stem: A data set is “complete” for planning when it includes:
A. The treatment position, the external contour, the target region, and the organs needed for the constraints and the beam paths
B. Only the slices that contain the GTV
C. A diagnostic scan in a different position, as long as the name matches
D. The DRR only, with no axial images
Answer: A
Objective: II.1
Why: Beams, scatter, and organ constraints all need anatomy outside the GTV. A scan that clips the body or stops before an organ at risk is not complete. A diagnostic position that cannot be reproduced is the wrong data set even if the name is right.

### Q3
Stem: The exam default for an unlabeled axial image is head-first supine. A data set that was acquired feet-first supine must be:
A. Identified as feet-first in the plan and in the shifts, not assumed to be the default
B. Treated as head-first, because the default overrides the scan header
C. Rotated 90° in-plane until it looks supine
D. Assigned a density of water and planned without looking at orientation
Answer: A
Objective: II.1
Why: Feet-first reverses the superior-inferior mapping relative to a head-first import if the header is misread. The default applies when the stem does not say otherwise. It does not erase a known feet-first setup. A 90° rotation does not fix a superior-inferior flip.

### Q4
Stem: Before contours are drawn, the dosimetrist checks the import against the written simulation. The check that prevents a left-right swap is:
A. Confirming orientation markers, header orientation, and a known anatomic side against the setup photos
B. Confirming only that the slice thickness is 3 mm
C. Confirming only the patient’s birth year
D. Renaming the file to head-first supine
Answer: A
Objective: II.1
Why: A laterality error survives a correct slice thickness and a correct date of birth. The header, the skin marks, and one unmistakable anatomic side have to agree. Renaming a file does not reverse the pixels.

### Q5
Stem: Contrast, bladder filling, and immobilization are recorded at simulation because:
A. Treatment has to reproduce them, and the density and position they create have to be interpreted on purpose
B. They are required only for the billing document
C. They replace the CT-density table
D. They set the decay constant of the beam
Answer: A
Objective: II.1
Why: A full bladder or a contrast-filled organ is part of the geometry the plan will assume. If treatment does not match, or if contrast is left as high density, the delivered dose is not the planned dose. None of these steps replaces the density curve or changes λ.

## Acquisition of Patient Data

### Q1
Stem: A planning CT clips the posterior body contour on several slices. The dose calculation will:
A. Treat the missing tissue as air and mis-estimate scatter and attenuation
B. Automatically restore the body from the room air
C. Be unaffected, because the contour is only a display
D. Increase the HU of the remaining tissue to compensate
Answer: A
Objective: II.1
Why: The external contour tells the algorithm where the patient ends. A clipped back is calculated as air, so depth, scatter, and beam attenuation are wrong. The system does not invent the missing tissue, and it does not rescale HU to make up for it.

### Q2
Stem: Slice thickness of 5 mm is used for a 1 cm intracranial target that will be planned stereotactically. The risk is:
A. Partial-volume averaging of the target and a coarse DRR and contour
B. A change in the photon decay constant
C. Automatic conversion of the scan to MRI
D. No risk, because thickness does not affect small targets
Answer: A
Objective: II.4
Why: A target comparable to the slice thickness is averaged with surrounding tissue, and the reconstructed edges and DRRs become stair-stepped. Stereotactic scans use much thinner slices. Slice thickness is not a decay constant and it does not turn CT into MRI.

### Q3
Stem: The scan length for a lung plan stops at the carina even though the fields and the lung constraint extend to the diaphragm. This data set is:
A. Too short. Organs used for constraints and tissue in the beam path have to be inside the scan.
B. Acceptable, because only the GTV must be scanned
C. Acceptable if the missing lung is assigned HU of +1000
D. Too long
Answer: A
Objective: II.4
Why: A lung V20 or mean-lung dose needs the lungs that are in the irradiated volume, and the beam needs the tissue it actually crosses. Stopping at the carina drops both. Assigning the missing volume a bone HU would make the gap worse. The scan is short, not long.

### Q4
Stem: DICOM import succeeds and the images appear. Validation is still required because:
A. A successful transfer can still carry the wrong orientation, the wrong slice spacing, or the wrong patient
B. DICOM cannot store orientation
C. Import always mirrors left and right
D. The planning system recalculates HU as SUV
Answer: A
Objective: II.1
Why: DICOM does store orientation and spacing, and a clean transfer can still be the wrong study or a mislabeled orientation. Import does not always mirror the patient, and it does not turn HU into SUV. Validation is the human check after the network check.

### Q5
Stem: 4DCT phases are imported for a lung target. The phase used for the dose calculation should be:
A. An average-density CT, not the maximum-intensity projection
B. The maximum-intensity projection, because its densities are the true average
C. The phase with the largest HU in the heart, regardless of the tumor
D. A single random phase with the body contour deleted
Answer: A
Objective: II.1
Why: The MIP is a composite for drawing the motion envelope of a solid tumor in lung. Its voxel values are maxima, not tissue densities, so dose on a MIP is not a real patient dose. The average CT carries a usable density. Deleting the body contour removes the scatter geometry.

### Q6
Stem: A lumpectomy cavity has a positive margin on the pathology report. The same physician redraws that cavity a few millimeters differently on a second sitting. Breathing and daily setup also move the tissue. What is the planning-target margin for?
A. Setup variation and internal motion, so the clinical target still receives the dose
B. The positive surgical margin, drawn as the planning target instead of as clinical disease
C. The physician's inconsistent drawing, which that margin is defined to hide
D. Only the wire on the scar, with motion and setup left outside the volume
Answer: A
Objective: II.1
Why: The planning target is the geometric allowance for setup uncertainty and for motion. A positive surgical margin is residual disease, so it is included in the clinical target. Inconsistent drawing is fixed by redrawing the contour. It is not a margin. The scar wire is a marker, not the volume that setup and motion are meant to cover.

### Q7
Stem: On the treatment couch the patient has gained weight, and the separation through the treated field is larger than the separation on the planning CT. What happens before the beam is turned on?
A. The dosimetrist tells the radiation oncologist before treatment. The old plan was calculated on the smaller separation and is not delivered while the change is only written down afterward
B. The planned monitor units are delivered today, and the weight gain is mentioned at the weekly chart check
C. The separation is ignored, because a weight change alters dose only for beams below 100 kV
D. The wedge angle is increased by the number of kilograms gained, and treatment proceeds
Answer: A
Objective: II.1
Why: A larger separation lengthens the path, lowers the midplane dose for the same entrance, and can move the hot spots. The calculation on the old contour is no longer the dose this patient will receive. The dosimetrist stops and tells the radiation oncologist before treatment so the physician can order a new scan or a new calculation. Treating first and noting the weight later delivers the outdated plan. Kilovoltage is not the only energy that sees path length, and body weight is not a wedge angle.

## Corrections for Contour Irregularities

### Q1
Stem: A sloping surface leaves less tissue over point A than a flat phantom would have at the same geometric distance from the central axis. If the flat-phantom depth is used uncorrected, the dose at A is:
A. Underestimated, because the true depth is smaller and attenuation is less
B. Overestimated, because missing tissue always adds attenuation
C. Exact, because contour shape does not change depth dose
D. Zero, because the algorithm cannot cross a slope
Answer: A
Objective: IV.4
Why: Missing tissue shortens the path. Less attenuation means more dose than the flat-phantom lookup at the longer path. Using the uncorrected deeper path predicts too little dose. Contour shape is a standard correction, not a reason for zero dose.

### Q2
Stem: An isodose-shift factor of 0.70 is stated for this energy. The tissue deficit along a ray is 2.0 cm. How far are the isodose curves shifted for that deficit, and in which direction?
A. 1.4 cm away from the source
B. 2.0 cm toward the source
C. 0.70 cm toward the source
D. 2.7 cm away from the source
Answer: A
Objective: IV.4
Why: Shift distance = 0.70 × 2.0 = 1.4 cm. For missing tissue the isodoses move downstream, away from the source, because the beam reaches a given percent dose at a greater geometric depth from the nominal flat surface. 2.0 cm uses the full deficit and ignores the factor. 0.70 cm drops the 2.0 cm. 2.7 cm adds the factor to the deficit.

### Q3
Stem: The effective-SSD method corrects a contour irregularity mainly for:
A. Inverse square, when the surface is closer to or farther from the source than the nominal SSD
B. The change in photon energy across the field
C. The half-life of the machine
D. A full heterogeneity correction inside lung
Answer: A
Objective: IV.4
Why: Effective SSD adjusts the inverse-square term for the air gap or the stand-in distance. It is not an energy shift, not a decay correction, and not the lung-density correction. Those are separate steps.

### Q4
Stem: A TAR-ratio contour correction uses the tissue deficit as a change in depth. If the nominal depth is 8 cm and 2 cm of tissue is missing, the TAR in the numerator is the TAR for a depth of:
A. 6 cm
B. 10 cm
C. 8 cm
D. 2 cm
Answer: A
Objective: IV.4
Why: Missing tissue reduces the depth that should be looked up: 8 − 2 = 6 cm. 10 cm would be an excess of tissue, not a deficit. 8 cm is the uncorrected depth. 2 cm is the deficit itself, not the remaining depth.

### Q5
Stem: Which comparison of contour-correction methods is correct?
A. Effective SSD is an inverse-square correction. The TAR ratio also changes the depth used for attenuation and scatter. The isodose shift moves the chart by a fraction of the gap.
B. All three methods change only the half-life.
C. The isodose shift is exact for every energy with a factor of 1.44.
D. TAR ratio ignores depth and corrects only the SSD.
Answer: A
Objective: IV.4
Why: The three classic methods do different jobs. Effective SSD does not by itself replace a depth change in TAR. The shift factor is an energy-dependent fraction such as 0.5 to 0.7, not the mean-life factor 1.44. TAR is a depth-and-field-size table.

## Corrections for Tissue Inhomogeneities

### Q1
Stem: A ray crosses 5.0 cm of soft tissue (relative density 1.0), then 6.0 cm of lung (relative density 0.30), then 2.0 cm of soft tissue. The water-equivalent depth is:
A. 8.8 cm
B. 13.0 cm
C. 1.8 cm
D. 22.0 cm
Answer: A
Objective: IV.4
Why: Water-equivalent depth = 5.0 × 1.0 + 6.0 × 0.30 + 2.0 × 1.0 = 5.0 + 1.8 + 2.0 = 8.8 cm. 13.0 cm is the physical path with no density correction. 1.8 cm keeps only the lung term. 22 cm uses 6.0 / 0.30 = 20 cm of water in the lung and then adds the 2 cm, inverting the density.

### Q2
Stem: A 6 MV beam traverses lung and then soft tissue. A calculation that forces the whole path to unit density, compared with a proper density correction, will:
A. Over-attenuate the lung and underestimate the dose beyond it
B. Under-attenuate the lung and overestimate the dose beyond it
C. Be exact, because Compton scatter does not depend on density
D. Change the beam energy from 6 MV to 15 MV
Answer: A
Objective: IV.4
Why: Lung attenuates less than water. A water path removes too many photons, so the dose predicted downstream is too low. Compton probability per centimeter does depend on electron density even though it depends weakly on Z. The nominal energy is not changed by the density correction.

### Q3
Stem: A small 15 MV field is centered on a tumor surrounded by lung. Besides the average density along the ray, the planner should expect:
A. Lateral electronic disequilibrium, which can underdose the tumor relative to a broad-beam hand calculation
B. A Bragg peak inside the tumor
C. No difference from a 6 MV large field in water
D. Photoelectric buildup in the lung air
Answer: A
Objective: IV.4
Why: High-energy electrons travel farther, and low-density lung does not replace the electrons that scatter out of a small field. The target can be underdosed compared with a homogeneous TAR ratio. Photons do not make a Bragg peak. Photoelectric effect is not the MV lung problem.

### Q4
Stem: At megavoltage energies, a dense bone affects photon dose mainly through:
A. Its electron density, a modest effect compared with the dramatic bone HU on a kV image
B. Photoelectric absorption as large as on the CT scan
C. Pair production only
D. A change in the monitor-unit definition
Answer: A
Objective: IV.4
Why: Compton scatter, which dominates MV dose in tissue, follows electron density. Bone is denser than water, so attenuation rises, but not by the factor the kV CT contrast suggests. Pair production is not required for the effect. The MU definition is a calibration statement, not a bone correction.

### Q5
Stem: A modern superposition or Monte Carlo algorithm, compared with a one-dimensional TAR ratio through lung, is preferred because it:
A. Accounts for scatter from the actual 3D density distribution, including rebuild-up at interfaces
B. Ignores density and is therefore faster and more accurate
C. Uses the MIP data set as the density
D. Replaces the need for an external contour
Answer: A
Objective: IV.4
Why: A 1D equivalent depth corrects the primary along the ray and handles lateral scatter poorly. Superposition, collapsed cone, Acuros-type solvers, and Monte Carlo transport the scatter in heterogeneous geometry. They still need a real density volume and an external contour, not a MIP.

## Acquisition of Patient Data Mini-Quiz

### Q1
Stem: Contrast is present in a vessel that will be empty at treatment. The override used for a photon plan is closest to:
A. Soft-tissue or blood density, not the raw high HU and not air
B. Air, because contrast is not tissue
C. Titanium density, because both are high Z
D. No override, because kV HU equals MV attenuation
Answer: A
Objective: IV.4
Why: The vessel will contain blood, not iodine and not air, during treatment. The CT number is a kV photoelectric effect. Leaving it, or painting it as metal or air, assigns the wrong MV attenuation.

### Q2
Stem: A patient is scanned head-first supine and a second scan is feet-first supine. After a rigid registration that ignores the header, the cord contour from the second scan:
A. Can land on the wrong superior-inferior end of the target
B. Is guaranteed to match because both scans are supine
C. Flips only the left-right axis
D. Cannot be imported, so the error is impossible
Answer: A
Objective: II.1
Why: Supine does not fix the head-foot direction. A feet-first series that is read as head-first maps the superior slices onto the inferior end. Left-right is a separate axis. DICOM will import the series; the orientation still has to be validated.

### Q3
Stem: Physical path length through a slab of relative density 0.25 is 8.0 cm. The water-equivalent thickness of that slab alone is:
A. 2.0 cm
B. 8.0 cm
C. 32 cm
D. 0.25 cm
Answer: A
Objective: IV.4
Why: Water-equivalent thickness = 8.0 × 0.25 = 2.0 cm. 8.0 cm ignores the density. 32 cm divides by 0.25. 0.25 cm reports the density as a thickness.

### Q4
Stem: An obliquely incident beam crosses more tissue than a perpendicular beam to the same point on the central-axis depth scale. The uncorrected perpendicular PDD will:
A. Overestimate the dose, because the true path is longer
B. Underestimate the dose, because oblique entry removes tissue
C. Be exact if the SSD is unchanged
D. Apply a Mayneord correction automatically
Answer: A
Objective: IV.4
Why: Obliquity increases the path length, so attenuation is greater and the dose is lower than the en-face PDD at the nominal depth. Mayneord’s factor changes SSD; it is not an obliquity correction. An unchanged nominal SSD does not cancel the longer path.

### Q5
Stem: Which data-check failure is a localization error rather than a later optimization error?
A. The imported CT is the wrong patient, discovered after the name and the setup photo disagree
B. The optimizer weight on the cord is too low
C. The wedge angle is 15° instead of 30°
D. The DVH normalization point is the mean instead of the volume
Answer: A
Objective: II.1
Why: Patient identity and orientation are data-validation steps. Objective weights, wedge angle, and DVH normalization are planning choices made after a valid data set exists. A wrong-patient CT cannot be repaired by an optimizer.
