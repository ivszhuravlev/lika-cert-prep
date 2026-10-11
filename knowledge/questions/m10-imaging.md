# Module 10 — Imaging Modalities

Original items on CT, MRI, PET, ultrasound, and how those studies are used for planning.

## Computed Tomography (CT)

### Q1
Stem: A planning CT is acquired on a curved diagnostic couch and then used as if the patient will be treated on a flat-top linac. The main problem is:
A. The body shape and internal anatomy will not match the treatment position.
B. Hounsfield numbers are defined only on a flat couch.
C. CT cannot see bone.
D. Slice thickness has no effect on a DRR.
Answer: A
Objective: I.8
Why: Simulation uses a flat tabletop and the same immobilization as treatment so the external contour and the organs match the beam geometry. HU exists for any CT. CT sees bone well. Thick slices do degrade DRRs and small-target definition.

### Q2
Stem: Window width and window level on a CT display control, respectively:
A. Contrast range, and the center of that range
B. Slice thickness, and kVp
C. Magnification, and couch height
D. Activity, and half-life
Answer: A
Objective: I.8
Why: Width is how many HU are mapped from black to white. A narrow width raises contrast. Level is the HU at the center of the window. Raising the level moves the window toward higher HU and makes more of the image fall below the window (darker) on a standard grayscale display. Slice thickness, kVp, magnification, and activity are not the window controls.

### Q3
Stem: A lung window is centered near −600 HU with a wide width. A soft-tissue window is centered near +40 HU with a narrow width. Viewing lung parenchyma on the soft-tissue window fails because:
A. Almost all of the lung HU values sit below the soft-tissue window and display as black
B. Lung is brighter than cortical bone on a soft-tissue window
C. Windowing changes the stored HU and therefore the dose calculation
D. A wide window is required by law to be centered at 0
Answer: A
Objective: I.8
Why: Display windowing does not rewrite the pixels used for dose. It only maps them to gray levels. Lung HU near −700 to −800 are far below a window centered at +40, so the lung looks uniformly black and nodules are easy to miss. Bone, not aerated lung, is bright on a soft-tissue window.

### Q4
Stem: Pitch on a helical CT is table travel per rotation divided by the collimated beam width. Pitch greater than 1 means:
A. The table moves farther than the collimated width in one rotation, so dose tends to fall and interpolation has to fill the helix
B. The slices overlap heavily and dose necessarily falls
C. The scanner has switched to MRI
D. kVp is above 120
Answer: A
Objective: I.8
Why: Pitch > 1 is a stretched helix: less overlap, generally less dose, and a greater demand on interpolation. Pitch < 1 overlaps and usually raises dose. Pitch is not a magnetic-resonance mode and it is not the tube potential.

### Q5
Stem: Cone-beam CT on a linac differs from the fan-beam planning CT in that CBCT:
A. Collects a large volume in one rotation and has more scatter, so raw HU are less reliable for dose calculation
B. Has no scatter and can replace the planning CT with no further check
C. Uses positron annihilation
D. Cannot be registered to the planning CT
Answer: A
Objective: I.8
Why: CBCT is an IGRT geometry. Extra scatter softens contrast and makes HU less accurate than the simulation CT. It is registered to the planning CT every day it is used. It is not a PET acquisition.

## MRI

### Q1
Stem: A T1-weighted image uses a short TR and a short TE. On that image:
A. Fat is bright and fluid is relatively dark
B. Fluid is bright and fat is always dark
C. Cortical bone is the brightest tissue
D. Air is bright
Answer: A
Objective: I.8
Why: T1 weighting emphasizes tissues with a short T1, so fat and gadolinium-enhanced tissue are bright and simple fluid is darker. Cortical bone and air have essentially no free protons and stay dark on both T1 and T2 images.

### Q2
Stem: A T2-weighted image uses a long TR and a long TE. Cerebrospinal fluid and edema appear:
A. Bright
B. Dark, the same as cortical bone
C. Invisible because MRI cannot see fluid
D. Bright only if the sequence is FLAIR
Answer: A
Objective: I.8
Why: Long T2 tissues, including water, CSF, and edema, stay bright on a T2-weighted image. FLAIR is a T2-type sequence with the CSF signal suppressed, so CSF goes dark while edema can remain bright. That is the opposite of “bright only on FLAIR.”

### Q3
Stem: MRI is fused to CT for a brain target. The dose calculation should be based on:
A. The CT, because MRI does not provide electron density
B. The MRI, because T2 intensity is proportional to physical density
C. Either data set, because both are already in Hounsfield units
D. The PET SUV, converted by dividing by 1000
Answer: A
Objective: I.8
Why: Dose engines need electron density or physical density, which the CT-to-density table supplies. MRI signal depends on proton relaxation, not on electron density, and geometric distortion can remain after fusion. SUV is not a density.

### Q4
Stem: Geometric distortion on MRI is worst:
A. Near metal and toward the edge of a large field of view
B. Only inside the CT bore, not the MRI bore
C. When the sequence is any T1 image, and never on T2
D. When gadolinium shortens T1, which moves anatomy by a known 5 mm
Answer: A
Objective: I.8
Why: Susceptibility artifacts around metal and gradient nonlinearity away from isocenter move anatomy on the image relative to the true position. That is why an MRI contour is checked against CT after fusion. Distortion is not limited to one weighting, and gadolinium changes signal, not a fixed 5 mm shift.

### Q5
Stem: A patient with a legacy pacemaker is scheduled for an MRI simulation. The imaging concern, separate from the treatment-beam neutron concern, is:
A. The magnetic field and the RF can move or heat an unsafe device
B. MRI uses megavoltage photons
C. MRI exposure is counted in the lifetime dose because it is ionizing
D. The pacemaker makes T2 fluid dark
Answer: A
Objective: I.8
Why: MRI is non-ionizing, but the static field, gradient switching, and RF are hazards for non-conditional implants. That is a different problem from photoneutrons produced by a high-energy treatment beam. MRI does not itself deliver megavoltage dose.

## Positron Emission Tomography (PET)

### Q1
Stem: F-18 FDG PET detects:
A. Near-simultaneous 511 keV photons from positron annihilation
B. A single 140 keV photon, as in a Tc-99m bone scan
C. Protons that stop in the tumor
D. Ultrasound echoes from FDG
Answer: A
Objective: I.8
Why: F-18 (half-life about 110 minutes) emits a positron. The positron annihilates with an electron and the scanner records two 511 keV photons in coincidence. Tc-99m is a single-photon emitter. PET is not a proton Bragg-peak image and it is not ultrasound.

### Q2
Stem: PET images are attenuated more strongly in the center of the body than at the skin. Modern PET/CT corrects that attenuation using:
A. The CT, rescaled to 511 keV
B. The MRI T1 signal
C. A constant SUV of 2.5 everywhere
D. No correction, because 511 keV photons do not interact
Answer: A
Objective: I.8
Why: The CT provides a map of attenuation that is converted from kV effective energy to 511 keV. Without it, deep uptake is underestimated. 511 keV photons still undergo Compton scatter. SUV is a measured result, not an input correction, and MRI intensity is not a 511 keV attenuation map.

### Q3
Stem: SUV is a convenient number, but it changes with uptake time, blood glucose, and body-size normalization. A planning decision that treats SUV as a hard tumor edge should also:
A. Be checked against the CT anatomy and the nuclear-medicine protocol, because SUV is not a geometric margin
B. Replace the CTV expansion entirely
C. Be converted directly to Hounsfield units by multiplying by 1000
D. Ignore motion, because PET frames are shorter than a breath
Answer: A
Objective: I.8
Why: PET adds metabolic information. The numeric SUV is not a contour by itself, and a free-breathing PET is blurred by motion. It does not replace a CTV expansion and it does not become a density table.

### Q4
Stem: Random coincidences on a PET scanner increase when the injected activity is very high because:
A. Unrelated photons are more likely to fall inside the coincidence time window
B. The positron range becomes zero
C. 511 keV photons become 140 keV photons
D. The CT tube current defines the coincidence window
Answer: A
Objective: I.8
Why: A random coincidence pairs two photons that did not come from the same annihilation. The chance of that rises steeply with count rate. Positron range and photon energy are properties of F-18, not of the activity setting. The CT current is not the PET timing window.

### Q5
Stem: Compared with the planning CT, a PET scan has:
A. Poorer spatial resolution, and it is used to supplement the anatomic volume rather than to replace the CT geometry
B. Better spatial resolution than CT, and no need for fusion
C. The same pixel size as ultrasound by definition
D. A direct measurement of electron density
Answer: A
Objective: I.8
Why: Coincidence localization, positron range, and non-colinearity limit PET resolution to several millimeters, worse than CT. The CT remains the geometric and density data set. PET does not measure electron density.

## Ultrasound

### Q1
Stem: Diagnostic ultrasound produces an image from:
A. Echoes of high-frequency sound at tissue interfaces
B. Photoelectric absorption of kV photons
C. Positron annihilation
D. Proton stopping power
Answer: A
Objective: I.8
Why: A piezoelectric transducer sends a pulse and listens for reflections. There is no ionizing radiation. Photoelectric CT, PET, and proton range are different modalities.

### Q2
Stem: Raising the ultrasound frequency generally:
A. Improves spatial resolution and reduces penetration
B. Improves penetration and reduces resolution
C. Changes the assumed speed of sound from 1540 m/s to the speed of light
D. Converts the study into ionizing radiation
Answer: A
Objective: I.8
Why: Higher frequency means a shorter wavelength and a better axial resolution, but soft tissue attenuates it faster, so deep structures disappear. Soft-tissue scanners assume about 1540 m/s, not 3 × 10^8 m/s. Sound is non-ionizing at diagnostic intensities.

### Q3
Stem: Air and cortical bone limit ultrasound because:
A. They reflect or absorb the beam so strongly that structures behind them are shadowed
B. They are acoustically identical to soft tissue
C. They emit 511 keV photons when the probe is applied
D. The gel cannot be used over them for infection-control reasons only
Answer: A
Objective: I.8
Why: A large impedance mismatch at air or bone sends the echo back and leaves a shadow. Gel is used to remove the air gap at the skin so the sound can enter. Bone does not annihilate positrons under a probe.

### Q4
Stem: Transrectal ultrasound is used in prostate brachytherapy mainly to:
A. See the gland and the needles in real time and to estimate the gland volume
B. Replace the post-implant CT for electron density
C. Measure Ir-192 exposure rate
D. Produce a Hounsfield look-up table
Answer: A
Objective: I.8
Why: Real-time ultrasound guides the needles and the volume study. It does not provide the electron-density map a CT provides, it does not survey a source, and it does not generate HU.

### Q5
Stem: Bladder filling changes from the ultrasound simulation to treatment. The prostate can shift because:
A. The full or empty bladder moves the gland and the rectum relative to the skin marks
B. Ultrasound deposits enough dose to shrink the bladder
C. Sound waves change the Hounsfield number of urine permanently
D. A full bladder removes the need for immobilization
Answer: A
Objective: I.8
Why: Pelvic anatomy is mobile with bladder and rectal filling. The simulation protocol and the treatment protocol have to match. Ultrasound does not deliver a therapeutic dose and does not rewrite CT numbers.

## Imaging Modalities Quiz

### Q1
Stem: Which modality adds ionizing dose during an image-guided session?
A. kV CBCT
B. Surface-guided cameras (SGRT)
C. Diagnostic ultrasound
D. MRI
Answer: A
Objective: I.8
Why: kV cone-beam CT uses an x-ray tube and delivers a small additional dose. SGRT, ultrasound, and MRI do not use ionizing radiation for the image. SGRT still does not see internal anatomy.

### Q2
Stem: kV planar images show bone against soft tissue more clearly than MV portal images because:
A. Photoelectric absorption is still important at kV energies and is not the main MV interaction
B. MV photons cannot exit the patient
C. kV images are acquired with the flattening filter as the detector
D. MV images have a Bragg peak
Answer: A
Objective: I.8
Why: kV contrast is photoelectric and Z-dependent. MV contrast is mostly Compton and is poorer for bone versus soft tissue. MV images do exit the patient; that is how a portal image is formed. The detector is not the flattening filter, and photons do not have a Bragg peak.

### Q3
Stem: A 4DCT is sorted into respiratory phases. For contouring the envelope of a lung tumor that is denser than the surrounding lung, the data set usually used is:
A. The maximum-intensity projection, with the average CT kept for the dose calculation
B. The maximum-intensity projection for both the contour and the dose calculation
C. A single end-inspiration slice, because motion is zero there
D. The PET SUV map alone
Answer: A
Objective: I.8
Why: The MIP keeps the brightest voxel over the breathing cycle, which traces a solid tumor moving in aerated lung. The densities in a MIP are not a real patient, so the dose is calculated on an average CT. End inspiration is one phase, not zero motion. PET does not define the geometric envelope by itself.

### Q4
Stem: FLAIR images of the brain are used when the clinician wants:
A. A T2-like image in which bright CSF has been suppressed
B. A CT density table
C. A positron coincidence map
D. Cortical bone displayed bright
Answer: A
Objective: I.8
Why: FLAIR nulls the cerebrospinal fluid so periventricular edema is not hidden by bright CSF. It is still MRI. Bone stays dark. It is not CT and not PET.

### Q5
Stem: A metal hip replaces the femoral head. On the planning CT the streaks run across the pelvis. Those streaks are:
A. Artifacts from the high-Z metal, and the densities in the streaks should not be trusted for dose without an override or a metal-artifact plan
B. True Hounsfield numbers of soft tissue, safe to use uncorrected
C. Ultrasound shadows stored as CT
D. Proof that the scanner pitch was zero
Answer: A
Objective: I.8
Why: Metal saturates the detectors and beam-hardening and photon-starvation streaks assign false HU to nearby tissue. Dose calculated through those false densities can be wrong. The fix is an artifact-reduction reconstruction, a density override, or both, not a belief that every pixel is accurate.
