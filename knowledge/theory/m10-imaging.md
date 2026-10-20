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

## CT Dose Indices and Image Quality Numbers

**Objectives:** I.8

**What the exam expects**

You can walk the chain from the measured CT dose index to the effective dose of a scan, with the right unit at each step, and you can place common examinations on a millisievert scale. You know the acquisition and reconstruction choices that lower dose or improve resolution, and you can compute a pixel size from the field of view and the matrix.

**Core facts**

The CT dose index (CTDI) is measured with a 100 mm pencil ion chamber in a standard acrylic phantom, 16 cm for head and 32 cm for body, in milligray. Because the periphery of a body phantom receives more dose than the center, the weighted index is CTDIw = one third of the center value plus two thirds of the average peripheral value. Dividing by pitch gives CTDIvol, the volume index that the scanner displays: a pitch above 1 spreads the same tube output over more table travel and lowers CTDIvol in proportion. CTDIvol is a dose to the phantom per rotation-length, still in mGy; it is not the patient dose.

Multiplying CTDIvol by the scanned length gives the dose-length product, DLP, in mGy·cm. Multiplying DLP by a region-specific conversion coefficient k gives the effective dose in mSv. Typical k values (ICRP and European guidance) are about 0.0021 mSv per mGy·cm for the head, 0.0059 for the neck, 0.014 for the chest, and 0.015 for the abdomen and pelvis. The head coefficient is small because the brain and skull contain few radiosensitive organs; the trunk coefficients are larger because lung, stomach, colon, breast and gonads sit in the beam. A handout that defines DLP as effective dose times length has the chain backwards.

Order-of-magnitude effective doses to remember: a chest radiograph about 0.1 mSv, a two-view mammogram about 0.4 mSv, a head CT about 2 mSv, a chest CT about 7 mSv, an abdomen-pelvis CT about 8 to 10 mSv, a PET/CT about 10 to 25 mSv depending on the CT technique, and natural background about 3 mSv per year in the United States. A planning CT with a long scan range and a 4DCT acquisition sits at the upper end of the diagnostic range; that dose is justified by the treatment but is still recorded.

Noise in a CT image falls as the square root of the mAs, so halving the dose raises the noise by about 41 percent. Iterative reconstruction models the statistics and the system geometry instead of filtering the back-projection, which lowers noise at a given dose; in practice it allows a 25 to 40 percent dose reduction for the same image quality. Automatic exposure control (tube-current modulation) reads the scout and adjusts the mA along the patient and around each rotation so that noise stays constant: thinner regions and the anterior-posterior direction get less current. It lowers the average dose in most patients but can raise the current in a large patient, so it is a noise-targeting tool, not a dose cap. Other reductions are a higher pitch, a lower kV for small patients, organ-based tube-current reduction over the breasts and lenses, and limiting the scan length to the planning range.

Spatial resolution is quoted in line pairs per millimeter. A system that resolves f line pairs per millimeter separates details about 1/(2f) apart. Diagnostic CT resolves roughly 0.7 lp/mm, about 0.7 mm detail, and places a marker to about 0.5 mm; MRI is about 0.3 lp/mm; film-screen radiography reaches 5 to 10 lp/mm; a kV flat panel sits near 1 to 2 lp/mm. Contrast resolution is where CT wins: it separates tissues differing by a few Hounsfield units that no radiograph can separate.

The reconstructed matrix is normally 512 by 512. Pixel size is the reconstruction field of view divided by the matrix: a 50 cm field of view gives about 0.98 mm pixels, a 25 cm targeted reconstruction gives about 0.49 mm. The voxel is the pixel area times the slice thickness; a 1 mm pixel with a 3 mm slice is a 3 mm³ voxel. A smaller field of view improves in-plane sampling but does not improve the intrinsic detector resolution, and a field of view that excludes part of the patient produces the truncation artifact described earlier. Each stored pixel uses 12 bits, 4,096 levels, usually mapped to the range −1,024 to +3,071 HU; a 9-bit depth would give only 512 levels, and the display shows 256 grays of which the eye distinguishes a few dozen, which is why windowing exists.

Scanner generations are exam vocabulary. First and second generation translated and rotated a pencil or narrow fan beam. Third generation, which is every modern multidetector scanner, rotates the tube and a detector arc together; a single miscalibrated detector element therefore traces a ring in the image. Fourth generation used a stationary full ring of detectors with only the tube rotating, which removed ring artifacts at the cost of more scatter. Helical (spiral) acquisition with slip rings and multidetector rows is an addition to third-generation geometry, not a new generation.

**Formulas**

CTDIw = (1/3) CTDI_center + (2/3) CTDI_periphery, in mGy.

CTDIvol = CTDIw / pitch, in mGy.

DLP = CTDIvol × scan length, in mGy·cm.

Effective dose E = k × DLP, in mSv, with k in mSv per mGy·cm.

Pixel size = field of view / matrix. Resolvable detail ≈ 1 / (2 × lp/mm).

**Worked example**

Given: an abdomen-pelvis planning CT at pitch 1.0 reports a center phantom dose of 10 mGy and a peripheral average of 16 mGy per rotation; the scan covers 40 cm; k for the abdomen is 0.015 mSv per mGy·cm. Find CTDIw, CTDIvol, DLP and E.

CTDIw = 10/3 + 2 × 16/3 = 3.33 + 10.67 = 14 mGy. At pitch 1.0, CTDIvol = 14 mGy.

DLP = 14 × 40 = 560 mGy·cm.

E = 0.015 × 560 = 8.4 mSv.

Meaning: the scan lands in the 8 to 10 mSv band expected for an abdomen-pelvis CT, about eighty chest radiographs. Had the pitch been 1.4, CTDIvol would have fallen to 10 mGy, the DLP to 400 mGy·cm and the effective dose to 6 mSv, with more noise unless the reconstruction compensates.

Usual wrong turn: averaging center and periphery equally (13 mGy). Multiplying CTDIvol by pitch instead of dividing. Reporting DLP in mGy or in mSv. Using the head coefficient for a body scan, which would give 1.2 mSv.

**Traps**

CTDIvol quoted as the patient's organ dose. Effective dose in mGy. A pitch below 1 described as a dose-saving setting. Iterative reconstruction described as changing the HU scale. Automatic exposure control described as always lowering dose. A smaller field of view described as improving detector resolution. Line pairs per millimeter read as millimeters.

**Sources**

Bushberg, *The Essential Physics of Medical Imaging*, CT chapter. AAPM Report 96 (CTDI, DLP, effective dose). ICRP Publication 102 (k coefficients). AAPM TG-66 (CT simulation). Public blueprint I.8.

## MRI, Ultrasound and PET Physics Numbers

**Objectives:** I.8

**What the exam expects**

You can state which repetition and echo times produce T1, T2 and proton-density contrast and what each makes bright, give the Larmor frequency at a clinical field strength, name the hardware that makes the field uniform and keeps the room quiet, describe a quench, and give the frequency range, reflection rule and acoustic-impedance idea for ultrasound. For PET you know the detector crystals, the coincidence window, and the mean life of F-18.

**Core facts**

Hydrogen protons precess at the Larmor frequency, which is the gyromagnetic ratio times the field: about 42.58 MHz per tesla. At 1.5 T that is about 64 MHz and at 3 T about 128 MHz, in the radiofrequency band, which is why the magnet room is an RF-shielded enclosure. Clinical scanners run at 0.5 to 3 T, with 1.5 T and 3 T the common choices and 7 T a research field; higher field gives more signal but more susceptibility distortion and more RF heating. Other nuclei with spin (fluorine-19, sodium-23, phosphorus-31) can be imaged; nuclei with even numbers of both protons and neutrons have no net spin and give no signal.

Contrast is chosen with the repetition time TR and the echo time TE. A short TR (under about 700 ms) with a short TE (under about 30 ms) gives T1 weighting: fat and sub-acute blood are bright, cerebrospinal fluid and most fluid are dark, white matter is brighter than gray matter, and gadolinium contrast shortens T1 so enhancing tumor is bright. A long TR (over about 2,000 ms) with a long TE (over about 80 ms) gives T2 weighting: cerebrospinal fluid, edema and most tumors are bright. A long TR with a short TE gives proton-density weighting, in which signal follows water content and tissue contrast is modest. FLAIR is a T2 sequence with an inversion pulse that nulls free fluid, so edema stays bright while the ventricles turn dark. Short TR with long TE is simply a noisy image and is not used.

The main field comes from a superconducting coil in liquid helium. Shim coils (and passive shim pieces) correct the homogeneity of that field over the imaging volume; without them the Larmor frequency would vary across the patient and fat suppression and geometry would fail. Gradient coils add small linear field variations that encode position and make the acoustic noise. RF coils transmit the excitation pulse and receive the signal; phased-array and quadrature surface coils improve the signal-to-noise ratio. Two shields surround the room: steel plates (passive magnetic shielding) or active shield coils confine the fringe field so that the 5-gauss line stays inside controlled space, and a copper mesh (Faraday cage) lines the room to keep external radio signals out and the scanner's RF in. The two shields are often confused; steel is for the static field, copper is for the radiofrequency.

A quench is the sudden loss of superconductivity: the coil becomes resistive, the stored energy boils the helium, and the gas must vent outside through the quench pipe. If the vent fails the room fills with cold helium, displacing oxygen, and the door can be forced shut by pressure. A quench is deliberately triggered only when a person is pinned against the magnet or in a fire; otherwise the magnet is never switched off, which is the origin of the missile-effect hazard. Other hazards are RF heating of tissue and of conductive loops, peripheral nerve stimulation from fast gradients, acoustic noise, and the device concerns already listed.

Geometric accuracy is about 1 to 2 mm near the isocenter and degrades toward the edge of the field of view from gradient nonlinearity, and near air and metal from susceptibility; MRI resolution is about 0.3 lp/mm, roughly half the CT figure. Fat-suppressed gadolinium T1 images are the usual head-and-neck fusion series; T2 is the prostate and cervix series; T1 with and without contrast plus FLAIR is the brain series.

Diagnostic ultrasound uses 1 to 20 MHz, generated and received by a piezoelectric crystal. Higher frequency gives a shorter wavelength, so better axial resolution and a longer near (Fresnel) zone, but more attenuation and less depth; a 3 to 5 MHz probe is for the abdomen and a 7 to 12 MHz probe for the breast, thyroid and transrectal work. Attenuation is about 0.5 dB per cm per MHz in soft tissue. The wavelength at 5 MHz is 1,540 divided by 5 million, about 0.3 mm. Echoes arise where acoustic impedance, density times sound speed, changes: soft tissue is about 1.6 megarayl, bone about 7.8 and air about 0.0004. The fraction of intensity reflected at a flat boundary is the square of the impedance difference divided by the impedance sum; soft tissue to bone reflects about 40 percent and soft tissue to air more than 99.9 percent, which is why coupling gel is needed and why bone and lung cast shadows. Artifacts to name are reverberation, acoustic shadowing and enhancement, mirror image and side lobes. Bioeffects are heating and cavitation, both negligible at diagnostic output. AAPM TG-128 covers QA of ultrasound prostate localization systems.

PET detectors are dense scintillators that stop 511 keV photons. Bismuth germanate (BGO) has the highest stopping power but is slow and dim; lutetium oxyorthosilicate (LSO, and LYSO) is fast and bright, allowing short coincidence windows and time-of-flight localization; gadolinium oxyorthosilicate (GSO) is intermediate. Sodium iodide, the gamma-camera crystal, is too light for efficient 511 keV detection. Two photons arriving within the coincidence window (a few to about 12 nanoseconds) define a line of response; this electronic collimation makes PET 10 to 100 times more sensitive than collimated SPECT. Resolution of about 4 to 5 mm is limited by positron range, the small non-collinearity of the photon pair, and crystal size. Corrections for attenuation (from the CT), scatter, randoms and dead time are applied before SUV is meaningful.

Decay arithmetic for the tracer uses the mean life as well as the half-life. The mean life is the half-life divided by 0.693, which is 1.44 times the half-life; for F-18 that is 1.44 × 110 = 158 minutes. The total number of decays from an injected activity equals that activity times the mean life, which is how the internal dose from a tracer is estimated. The standard adult FDG injection is about 10 to 15 mCi (370 to 555 MBq) after a 4 to 6 hour fast with blood glucose under about 200 mg/dL, a 60 minute uptake period and voiding before the scan; an SUV above about 2.5 is the usual flag for malignancy, with the caveats given earlier. Cyclotron-produced positron emitters other than F-18 are carbon-11 (20 min), nitrogen-13 (10 min) and oxygen-15 (2 min); gallium-68 and rubidium-82 come from generators.

**Formulas**

Larmor frequency f = 42.58 MHz per tesla × B.

Reflected intensity fraction R = ((Z2 − Z1) / (Z2 + Z1))², with Z = density × speed of sound.

Mean life τ = T½ / 0.693 = 1.44 × T½. Cumulated activity = A0 × τ.

**Worked example**

Given: a 3 T scanner, a soft-tissue to bone interface with impedances 1.6 and 7.8 megarayl, and a 10 mCi F-18 injection with no excretion.

Larmor: 42.58 × 3 = 127.7 MHz, call it 128 MHz. At 1.5 T it is 63.9 MHz.

Reflection: (7.8 − 1.6)/(7.8 + 1.6) = 6.2/9.4 = 0.66; squared, 0.43. About 43 percent of the intensity returns at the bone surface, leaving little to image behind it.

Mean life: 1.44 × 110 = 158 min. Total decays = 10 mCi × 3.7 × 10^7 decays per second per mCi × 158 × 60 s = 3.5 × 10^12 disintegrations.

Meaning: three independent numbers, each one step from a memorised constant. The mean life is longer than the half-life, never shorter; forgetting to square the impedance ratio gives 66 percent; using 42.58 as the frequency at 3 T forgets to multiply by the field.

**Traps**

Shim coils described as RF shielding or copper mesh described as magnetic shielding. Quench described as the normal shutdown. Proton density given as short TR and short TE. Higher ultrasound frequency described as deeper penetration. Impedance mismatch described as the reason sound passes easily. NaI listed as a PET crystal. Mean life taken as 0.693 times the half-life.

**Sources**

Bushberg, *The Essential Physics of Medical Imaging*, MRI, ultrasound and nuclear medicine chapters. Khan and Gibbons, *The Physics of Radiation Therapy*, imaging chapter. AAPM TG-128 (ultrasound prostate localization QA). AAPM TG-108 (PET/CT shielding). Public blueprint I.8.
