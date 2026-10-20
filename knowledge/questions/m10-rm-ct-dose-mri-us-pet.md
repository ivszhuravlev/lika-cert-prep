# Module 10. Imaging Modalities

Original items. Gaps identified in the RM Review port: the CTDI to DLP to effective-dose chain, typical examination doses, iterative reconstruction, automatic exposure control, line-pair resolution, matrix and pixel size, MRI TR/TE contrast and hardware, Larmor frequency, ultrasound impedance, PET crystals and the F-18 mean life.

## CT Dose Indices and Image Quality Numbers

### Q1
Stem: An abdomen CT reports a CTDIvol of 15 milligray over a scan length of 40 centimeters. Using an abdominal conversion coefficient of 0.015 millisievert per milligray-centimeter, the effective dose is approximately:
A. 0.9 mSv
B. 9 mSv
C. 90 mSv
D. 600 mSv
Answer: B
Objective: I.8
Why: The dose-length product is 15 times 40, which is 600 milligray-centimeters, and the effective dose is 600 times 0.015, which is 9 millisieverts. Check: 9 divided by 0.015 returns 600. 0.9 mSv drops a factor of ten in the coefficient. 90 mSv would be a radiotherapy-scale number for a diagnostic scan. 600 is the DLP itself with the wrong unit attached.

### Q2
Stem: In a 32 centimeter body phantom a pencil chamber reads 10 milligray at the center hole and an average of 16 milligray at the peripheral holes. The weighted CT dose index is:
A. 12 mGy
B. 13 mGy
C. 14 mGy
D. 16 mGy
Answer: C
Objective: I.8
Why: CTDIw weights the center one third and the periphery two thirds: 10 divided by 3 is 3.33, plus 16 times 2 divided by 3 is 10.67, giving 14 milligray. Check: 14 lies closer to the peripheral value, as it must with a two-thirds weight. 13 is the plain average. 12 weights the center two thirds. 16 ignores the center entirely.

### Q3
Stem: A planner tells a patient that the abdomen-pelvis planning CT delivers an effective dose closest to:
A. 0.1 mSv, about the same as a chest radiograph
B. 1 mSv, about the same as a mammogram
C. 100 mSv, about the same as a radiotherapy fraction
D. 10 mSv, about one hundred chest radiographs or three years of natural background
Answer: D
Objective: I.8
Why: An abdomen-pelvis CT runs about 8 to 10 millisieverts, roughly a hundred times a 0.1 millisievert chest radiograph and about three years of the 3 millisievert annual background. A mammogram is about 0.4 millisieverts and a head CT about 2. A 2 gray treatment fraction is on the order of 2,000 millisieverts to the target, far above any diagnostic study.

### Q4
Stem: A CT simulator is upgraded from filtered back-projection to an iterative reconstruction algorithm. The expected effect is:
A. Lower image noise at the same dose, which allows a dose reduction of roughly 25 to 40 percent at equal image quality
B. A new Hounsfield scale that requires the density curve to be redefined with water at plus 1000
C. Better spatial resolution because the detector elements become smaller
D. Elimination of metal artifacts without any override
Answer: A
Objective: I.8
Why: Iterative reconstruction models photon statistics and system geometry, so noise and streaks fall at a given mAs and the technique can be lowered while keeping the same noise. The Hounsfield definition is unchanged, with water still at 0; the density curve is verified after an upgrade, not redefined. Detector size and therefore intrinsic spatial resolution are hardware properties. Metal artifacts are reduced by dedicated algorithms but a dose override is still needed through severe streaks.

### Q5
Stem: A pelvis is reconstructed on a 512 by 512 matrix with a 50 centimeter field of view. The in-plane pixel size is approximately:
A. 0.5 mm
B. 1.0 mm
C. 2.0 mm
D. 0.1 mm
Answer: B
Objective: I.8
Why: Pixel size is the field of view divided by the matrix, 500 millimeters divided by 512, which is 0.98 millimeters, about 1 millimeter. Check: 512 pixels times 0.98 millimeters returns 50 centimeters. 0.5 mm would need a 25 centimeter field of view. 2.0 mm would need a 256 matrix. 0.1 mm is a factor of ten too fine for any body CT.

### Q6
Stem: Automatic exposure control on a CT simulator uses the scout image to:
A. Hold the tube current constant and vary the kilovoltage slice by slice
B. Turn off the beam over the gonads and lenses
C. Modulate the tube current along the patient and around each rotation so that image noise stays roughly constant, lowering dose through thin regions
D. Guarantee that every patient receives less dose than the fixed-mA protocol
Answer: C
Objective: I.8
Why: Tube-current modulation reads the attenuation from the scout and raises or lowers the mA with patient thickness and projection angle to target a chosen noise level, which usually lowers the average dose. The kilovoltage is normally fixed. Organ-based current reduction is a separate feature. In a very large patient the modulation can raise the current above the fixed protocol, so it is a noise target rather than a dose ceiling.

### Q7
Stem: A diagnostic CT is quoted as resolving about 0.7 line pairs per millimeter. This means the scanner separates details roughly:
A. 7 millimeters apart
B. 0.07 millimeters apart
C. 1.4 millimeters apart, and this is finer than film-screen radiography
D. 0.7 millimeters apart, which is coarser than radiographic film but with far better contrast resolution
Answer: D
Objective: I.8
Why: Resolvable detail is about one over twice the spatial frequency, 1 divided by 1.4, which is about 0.7 millimeters per line, and MRI at about 0.3 line pairs per millimeter is coarser still while film-screen radiography resolves 5 to 10. CT is chosen for contrast resolution, a few Hounsfield units, not for fine detail. 7 and 0.07 are decimal errors. 1.4 millimeters is the full line-pair period, and film resolves finer detail than CT, not coarser.

## MRI, Ultrasound and PET Physics Numbers

### Q1
Stem: Protons precess at about 42.6 megahertz per tesla. The Larmor frequency on a 3 tesla scanner is approximately:
A. 128 MHz
B. 64 MHz
C. 42.6 MHz
D. 14.2 MHz
Answer: A
Objective: I.8
Why: Frequency equals the gyromagnetic ratio times the field, 42.58 times 3, which is 127.7 megahertz. Check: 128 divided by 3 returns 42.6. 64 MHz is the 1.5 tesla value. 42.6 MHz forgets to multiply by the field. 14.2 MHz divides by the field instead of multiplying. The frequency lies in the FM radio band, which is why the room is lined with copper.

### Q2
Stem: A pulse sequence with a long repetition time of about 3,000 milliseconds and a short echo time of about 20 milliseconds produces an image that is:
A. T1-weighted, with fat bright and cerebrospinal fluid dark
B. T2-weighted, with cerebrospinal fluid and edema bright
C. Proton-density-weighted, with signal following water content and only modest tissue contrast
D. FLAIR, with the ventricles nulled
Answer: C
Objective: I.8
Why: A long TR removes T1 differences and a short TE removes T2 differences, leaving signal proportional to the number of protons, which is proton-density weighting. T1 weighting needs a short TR with a short TE. T2 weighting needs a long TR with a long TE. FLAIR is a long-TR, long-TE sequence with an added inversion pulse that nulls free fluid.

### Q3
Stem: During an MRI simulation a metal oxygen cylinder is pulled into the bore and pins a therapist. The emergency action that removes the magnetic field, and its hazard, is:
A. Switching off the mains power, which has no hazard because the field disappears instantly
B. Triggering a quench, in which the magnet loses superconductivity and the boiling helium must vent outside or it displaces oxygen in the room
C. Reversing the gradient coils, which cancels the main field
D. Opening the Faraday cage door to let the field escape
Answer: B
Objective: I.8
Why: A superconducting magnet stays at field with no external power, so the only way to drop the field in an emergency is a quench, which dumps the stored energy into the liquid helium; the gas must leave through the quench pipe, and a failed vent fills the room with cold helium, risks asphyxiation and can hold the door shut by pressure. Mains power does not sustain the field. Gradient coils add small position-encoding fields and cannot cancel the main one. The copper cage shields radiofrequency and has nothing to do with the static field.

### Q4
Stem: The copper mesh built into the walls of an MRI room is there to:
A. Confine the fringe magnetic field so the 5 gauss line stays inside the controlled area
B. Correct the uniformity of the main field across the imaging volume
C. Absorb the acoustic noise from the gradient coils
D. Act as a Faraday cage that keeps outside radio signals out and the scanner's radiofrequency in
Answer: D
Objective: I.8
Why: The Larmor signal is a weak radiofrequency signal at tens of megahertz, so the room is a sealed copper enclosure to exclude broadcast and electrical interference that would otherwise appear as zipper artifacts. The fringe field is confined by steel plates or active shield coils. Field uniformity is set by shim coils. Acoustic treatment is separate from either shield.

### Q5
Stem: Soft tissue has an acoustic impedance of 1.6 megarayl and cortical bone about 7.8 megarayl. The fraction of ultrasound intensity reflected at a flat soft-tissue-to-bone boundary is approximately:
A. 43 percent
B. 66 percent
C. 21 percent
D. 99.9 percent
Answer: A
Objective: I.8
Why: The reflected fraction is the square of the impedance difference over the sum: 6.2 divided by 9.4 is 0.66, and 0.66 squared is 0.43. Check: 0.43 is less than the unsquared ratio, as it must be for a number below 1. 66 percent forgets to square. 21 percent is the simple ratio of the two impedances. 99.9 percent is the tissue-to-air value, which is why gel is needed at the skin.

### Q6
Stem: Compared with bismuth germanate, the lutetium oxyorthosilicate crystals used in modern PET scanners are chosen because they:
A. Stop 511 keV photons more completely than any other material and are therefore more sensitive
B. Are the same crystal used in gamma cameras, which lowers cost
C. Scintillate faster and brighter, allowing a shorter coincidence window and time-of-flight localization
D. Do not require attenuation correction from the CT
Answer: C
Objective: I.8
Why: LSO and LYSO have a decay time of about 40 nanoseconds against about 300 for BGO and give several times more light, so random coincidences fall and the arrival-time difference can be used to localize the annihilation along the line of response. BGO actually has the higher stopping power. Gamma cameras use sodium iodide, which is too light for efficient 511 keV detection. Attenuation correction is needed with every crystal because it corrects the patient, not the detector.

### Q7
Stem: The half-life of fluorine-18 is 110 minutes. Its mean life, used to compute the total number of decays from an injected activity, is approximately:
A. 76 min
B. 110 min
C. 220 min
D. 158 min
Answer: D
Objective: I.8
Why: Mean life is the half-life divided by 0.693, which equals 1.44 times the half-life: 1.44 times 110 is 158 minutes. Check: 158 times 0.693 returns 110. 76 minutes multiplies by 0.693 instead of dividing. 110 minutes is the half-life itself. 220 minutes is two half-lives, which is not a defined lifetime. The mean life is always longer than the half-life because the long tail of surviving atoms pulls the average up.
