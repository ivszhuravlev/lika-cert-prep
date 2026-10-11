# Module 10. Imaging Modalities

Original notes for MDCB objective I.8. Dose is calculated on CT. Other modalities are fused or used for setup. They do not replace the density table.

## Computed Tomography (CT)

**MDCB:** I.8, I.9, II.1, II.4

**What the exam expects**

You know what a planning CT must include, what the pixel value means, and which other x-ray images are for setup rather than for monitor units. You know the artifacts that change a contour or a density. Hounsfield arithmetic is module 11. This lesson is the modality.

**Core facts**

A planning CT is a map of linear attenuation, scaled to Hounsfield units, acquired on a flat indexed table with external lasers. The planning system converts HU to relative electron density or physical density through a calibration curve measured in a phantom. That conversion is the only reason CT is the dose-calculation data set.

Typical scan settings are on the order of 80–140 kV. mAs changes noise. It should not change HU if the scanner is linear and the beam-hardening correction is stable. kV does change the HU of bone and contrast, because the photoelectric effect is still active at CT energies. A density curve commissioned at 120 kV is the curve for 120 kV scans.

Slice thickness is a resolution choice. SRS and SBRT and small targets need thin slices, on the order of 1–2 mm. A 5 mm slice averages a small node with the tissue around it (partial-volume effect) and shifts the DVH. Pitch is table travel per rotation divided by the collimated beam width. The exam point is that pitch, thickness, and field of view are acquisition parameters, not window settings.

Window width and window level change the gray display. They do not change the stored HU. A lung window and a soft-tissue window are two views of one data set. Contouring the body on a tight window can clip the skin. “Full windows” in the simulation objective means you look at the window that actually shows the structure you are localizing, including a window wide enough to show skin.

Artifacts that change the plan:

- Metal: streaks of falsely high and low HU. Override the artifact, or the dose in the streak is fiction.
- Motion: blurred or duplicated anatomy. A blurred target is the wrong CTV.
- Beam hardening: the center of a large patient looks darker (cupping) if the correction fails.
- Truncation: the patient is wider than the field of view. The body contour is cut off. Scatter and skin dose are then wrong. Rescan, or extend the contour only with a method the clinic has validated.
- Partial volume: a small high-contrast object fills only part of the voxel and its HU is averaged downward.

4DCT sorts images into breathing phases. The maximum-intensity projection (MIP) shows the brightest voxel along the motion and is used to draw a lung ITV. The average CT is a density set closer to what the beam sees over the breathing cycle. Dose is calculated on the average CT or on a chosen phase, not on the MIP. The MIP assigns tumor density to every voxel the tumor passed through.

Other x-ray images in this objective:

- kV planar and kV CBCT: setup and IGRT, good contrast, cone-beam scatter makes CBCT HU less trustworthy than simulation CT for a new dose calculation.
- MV planar and MV CBCT: setup with the treatment beam, poorer contrast, less sensitive to high-Z artifacts.
- Digitally reconstructed radiograph: a calculation from the planning CT at a beam angle, compared with a portal image. It is not a second CT.

Surface-guided radiation therapy (SGRT) is in the same blueprint objective and is not a CT. Cameras track the skin surface. There is no ionizing dose and no internal anatomy. It is used for posture and for breath-hold coaching. A surface match does not prove the internal target is at the isocenter if the internal anatomy moved relative to the skin.

**Traps**

Calculating dose on a CBCT or a MIP because “it is a CT.” Changing the window and believing the densities changed. Using an 80 kV density curve on a 120 kV scan for a bone-heavy site. Ignoring truncation because the target itself is inside the reconstructed circle.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-66 for CT simulation. Public blueprint I.8 and I.9.

## MRI

**MDCB:** I.8, II.5

**What the exam expects**

You know what MRI is good for, why it cannot drive the monitor-unit calculation by itself, and the geometric errors that matter when it is fused to CT. You can separate T1 and T2 contrast at the level of “what is bright.”

**Core facts**

MRI signal comes from protons in a magnetic field, tipped by radiofrequency pulses. There is no ionizing dose from the imaging itself. Soft-tissue contrast is the reason it is fused for brain, prostate, cervix, liver, and cord.

T1-weighted images: fat is bright, fluid is relatively dark. T2-weighted images: fluid is bright. FLAIR suppresses free fluid. Diffusion-weighted images show restricted diffusion as bright on DWI and dark on the ADC map; many tumors restrict. You are not reading a diagnostic report on this exam. You are expected not to contour “edema” and “tumor” as the same brightness on the wrong sequence.

MRI pixel values are not Hounsfield units. They must not be sent through the CT-to-density table. An MR-only planning path uses a synthetic CT or a registered planning CT so that each voxel still has an electron density. A fusion that is pretty and an unassigned density grid is not a dose calculation.

Geometric distortion comes from gradient nonlinearity (worse far from the magnet center) and from magnetic-susceptibility changes at air, bone, and metal. A target contoured on a distorted MRI and copied onto CT can be in the wrong place by millimeters. That is a PTV question as well as an image question. Chemical-shift artifact shifts fat relative to water.

Safety items that show up next to imaging questions: a conventional pacemaker or a ferromagnetic implant may be a contraindication; some devices are MR-conditional at a stated field strength. The magnet is always on. RF heating and projectile risk are MRI hazards, not CT hazards.

An MR-linac adds the treatment-beam problem from module 7: the magnetic field deflects secondary electrons. The imaging advantage is an image in the treatment position. The dosimetry does not become “CT-free” just because the image is MR.

**Traps**

HU assigned by rescaling MRI gray values. Contouring on MRI without checking the fusion registration. Treating distortion at the periphery of a large field of view as negligible for a stereotactic target. Calling MRI a density modality because cortical bone is dark.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.8.

## Positron Emission Tomography (PET)

**MDCB:** I.8, I.1

**What the exam expects**

You describe coincidence detection of two 511 keV annihilation photons, the F-18 half-life, and what PET does and does not contribute to a plan. You do not treat an SUV number as a universal GTV definition or as a density.

**Core facts**

F-18, recall half-life 110 min, decays by positron emission. The positron annihilates with an electron. Two 0.511 MeV photons leave in opposite directions. The scanner records a coincidence line between two detectors that fire together. That electronic collimation is the image. Lead collimators of a gamma camera are not the PET method.

The common tracer is FDG, a glucose analog. Uptake is high in many tumors and also in brain, heart, inflammatory tissue, brown fat, and excreted tracer in the bladder and ureters. A hot focus is not automatically GTV. A protocol may set an SUV threshold or a physician contour. SUV 2.5 is not a law of physics. SUV is a normalized activity concentration, not a dose in gray.

Spatial resolution is several millimeters, worse than CT. A small node can be missed or can look larger than it is (partial volume). Respiratory motion between the PET acquisition and the CT acquisition misregisters lung and liver lesions. The fusion can be pretty and still place the FDG cloud in the wrong rib space. 4D PET or a matched breathing phase is the fix when the clinic has it.

Attenuation correction of the PET images uses the CT. A metal artifact or a misregistered CT produces a false hot or cold spot on the corrected PET. Dose is still calculated on the planning CT, with densities overridden where the CT is wrong. PET does not replace that CT.

Activity falls while the patient waits. From the half-life lesson: 55 minutes is half of 110, so 70.7% of the F-18 activity remains, not 50%. The imaging dose to the patient is a radiopharmaceutical dose, not a beam dose.

**Formulas**

Annihilation: two photons, 0.511 MeV each.

Remaining activity: A = A0 × 2^(−t / 110 min), with t in minutes.

**Worked example**

Given: an F-18 dose is assayed at 10.0 mCi for a PET slot. The injection is delayed 110 minutes. Recall half-life 110 min. Find the activity at injection if nothing was drawn off.

Formula: n = t / T½. A = A0 / 2^n.

Substitution: n = 110/110 = 1.

Arithmetic: A = 10.0 / 2 = 5.0 mCi.

Meaning: one half-life, half the activity. The scanner will count fewer coincidences unless the acquisition time is extended. This is the same exponential as module 3, applied to a modality.

Usual wrong turn: 110 minutes treated as two half-lives because “110 is a large number of minutes,” leaving 2.5 mCi. Or the delay ignored because the assay label still says 10 mCi.

**Traps**

One 1.022 MeV photon instead of two 511 keV photons. PET used as the electron-density grid. A bladder hot spot contoured as tumor. SUV treated as gray. Coincidence imaging described as a collimator grid.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Recall half-life F-18 = 110 min. Public blueprint I.8 and I.1.

## Ultrasound

**MDCB:** I.8

**What the exam expects**

You know that ultrasound is non-ionizing, real-time, and operator-dependent, and that it does not provide electron density. You can compute depth from a round-trip time using 1540 m/s, and you remember the factor of one-half.

**Core facts**

A transducer sends a short pulse and listens for echoes. Echoes form at boundaries where acoustic impedance changes (skin, bladder wall, prostate capsule, needle). The image is built from the round-trip time. Soft-tissue systems assume a speed of 1540 m/s. If the real speed is different, the depth is wrong.

There is no ionizing dose. That is why ultrasound is used for prostate brachytherapy needle guidance, for interfraction bladder and prostate position, and for some breast and soft-tissue localization. It does not see cleanly through bone, lung, or gas. A large patient and a poor acoustic window can hide the target. The operator’s hand pressure moves the prostate; the image and the anatomy are coupled.

Ultrasound gray values are not HU. There is no density table to feed a photon calculation. The modality localizes. The planning CT still calculates.

Doppler shows flow. It is not a radiation quantity. Do not confuse it with dose painting.

**Formulas**

Depth = c × t / 2

- c: assumed speed, 1540 m/s in soft tissue
- t: round-trip time
- the factor 1/2: the pulse goes to the reflector and back

**Worked example**

Given: an echo returns 100 μs after the pulse. c = 1540 m/s. Find the depth of the reflector.

Formula: depth = c × t / 2

Substitution: t = 100×10^−6 s = 1.00×10^−4 s. depth = 1540 × 1.00×10^−4 / 2

Arithmetic: 1540 × 1.00×10^−4 = 0.154 m round trip. Depth = 0.077 m = 7.7 cm.

Meaning: a 100 μs echo is a reflector at 7.7 cm, not at 15.4 cm. The extra factor of two is the return trip.

Usual wrong turn: depth = c × t = 15.4 cm, forgetting the factor 1/2. Or using 1540 cm/s, which is 100 times too slow and puts the reflector at 0.77 mm.

**Traps**

Ultrasound used as a density correction inside lung. Bone described as a good acoustic window. Round-trip time used as a one-way time. A claim that ultrasound “deposits no energy,” which is false in the acoustic sense and true in the ionizing-radiation sense. The exam means no ionizing dose.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.8. Soft-tissue speed 1540 m/s is the standard assumed value; confirm in Khan if a stem quotes a different calibration speed.

## Imaging Modalities Quiz

This quiz checks which modality supplies electron density (CT), which supplies soft-tissue contrast without density (MRI), which is coincidence detection of 511 keV pairs (PET), and which is a non-ionizing round-trip echo (ultrasound). It also checks MIP versus average CT, window level versus stored HU, and SGRT as a surface surrogate. The traps are calculating dose on MRI, on PET, or on a MIP; treating SUV as gray; forgetting the factor 1/2 in an ultrasound depth; and accepting CBCT HU as a commissioned planning-CT density table.
