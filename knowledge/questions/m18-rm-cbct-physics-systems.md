# Module 18. IGRT

Original items. Cone-beam acquisition and reconstruction, detector and filter hardware, kilovoltage versus megavoltage imaging dose and contrast, named localization systems, and correction protocols.

## CBCT Physics and Named Localization Systems

### Q1
Stem: A linac acquires several hundred kilovoltage projections while the gantry rotates and produces a volumetric image. Which reconstruction method turns those projections into the volume?
A. Maximum-intensity projection across the gantry angles
B. Deformable registration of each projection to the planning CT
C. Filtered back projection using a cone-beam algorithm
D. Simple summation of the projections without filtering
Answer: C
Objective: I.8
Why: Cone-beam CT reconstructs by filtered back projection, the Feldkamp cone-beam form of the algorithm diagnostic CT uses; the projections are high-pass filtered before being smeared back along their rays. Unfiltered summation produces a blurred image, which is why the filter step exists. A maximum-intensity projection is a display derived from an already reconstructed volume, and deformable registration is a comparison tool, not a reconstruction.

### Q2
Stem: A pelvis cone-beam is needed for a prostate patient. Which acquisition mode is appropriate and why?
A. Half-fan, because the laterally offset detector with a full 360-degree rotation gives a field of view of about 45 to 50 cm
B. Full-fan, because a 200-degree rotation lowers the imaging dose
C. Full-fan, because the pelvis fits inside its 25 cm field of view
D. Half-fan, because it uses the megavoltage beam and avoids hip-prosthesis streaks
Answer: A
Objective: I.8
Why: In half-fan mode the panel is shifted sideways so each projection covers about half the patient, a full rotation covers both halves, and the reconstructed diameter grows to roughly 45 to 50 cm, which contains a pelvis. Full-fan reconstructs about 25 cm and truncates a pelvis with a bright ring at the edge of the field of view; it fits a head or a neck. The choice of fan mode is independent of beam energy.

### Q3
Stem: A bowtie filter is placed in the kilovoltage cone-beam. What does it do?
A. Converts the kilovoltage spectrum to a monoenergetic beam
B. Hardens the beam uniformly so that bone appears brighter
C. Blocks the central ray to protect the detector from saturation
D. Attenuates the beam more at the edges where the patient is thin, evening the detector signal, reducing peripheral skin dose, and reducing scatter-driven cupping
Answer: D
Objective: I.8
Why: The bowtie is thick at the edges and thin in the center, matching the patient's thickness profile so the panel sees a flatter signal and the thin periphery is not overexposed. That lowers skin dose at the edges and cuts the scatter that causes cupping. It does not make the beam monoenergetic, it hardens the beam more at the edges than the center rather than uniformly, and it does not block the central ray.

### Q4
Stem: What is the detector used for kilovoltage cone-beam imaging and for modern portal imaging?
A. A xenon-gas ionization array
B. A flat-panel amorphous-silicon photodiode array under a scintillator
C. A film cassette with intensifying screens
D. An image intensifier with a video camera
Answer: B
Objective: I.8
Why: The flat panel is a large amorphous-silicon array of photodiodes and switches read out electronically, with a cesium iodide or gadolinium oxysulfide scintillator converting x-rays to light; on the megavoltage side the same panel sits under a build-up plate as the electronic portal imaging device. Xenon detectors belong to earlier diagnostic CT. Film and image intensifiers were the predecessors the flat panel replaced.

### Q5
Stem: A patient with bilateral hip prostheses is imaged with a megavoltage cone-beam instead of a kilovoltage one. Which statement about that choice is correct?
A. The megavoltage image is free of metal streak artifacts but has poorer soft-tissue contrast and a higher dose per scan
B. The megavoltage image has better soft-tissue contrast because the beam is more penetrating
C. The megavoltage image has the same dose as the kilovoltage one because both are low-monitor-unit scans
D. The megavoltage image shows the prostate better because photoelectric contrast is stronger at high energy
Answer: A
Objective: I.8
Why: Megavoltage photons interact almost entirely by Compton scattering, so contrast depends on electron density alone and soft tissue is poorly separated, while the dose per usable image is several times that of a kilovoltage cone-beam. The benefit is immunity to the streak artifacts that high-Z metal produces at kilovoltage energies, plus acquisition with the treatment beam through the treatment isocenter. Photoelectric contrast is what the kilovoltage beam has and the megavoltage beam lacks.

### Q6
Stem: A localization system uses two floor-mounted kilovoltage tubes and two ceiling-mounted flat panels to take a simultaneous oblique pair, tracks infrared body markers for pre-positioning, and drives a six-degree-of-freedom robotic couch. What is this system, and what can it match?
A. A surface-guidance system that matches the skin contour
B. An electromagnetic transponder system that matches implanted beacons
C. A stereoscopic kilovoltage system such as ExacTrac that matches bone or implanted fiducials, not soft tissue
D. A megavoltage cone-beam that matches soft tissue through metal
Answer: C
Objective: II.6
Why: The stereoscopic kilovoltage design fuses two oblique projections to digitally reconstructed radiographs, derives translations and rotations, and corrects with a robotic couch; it can image at any gantry angle during treatment, which is why it is used for cranial and spine stereotactic work. Its images are planar, so it localizes bone and fiducials and cannot align a soft-tissue interface. Surface, electromagnetic, and cone-beam systems have different hardware and different targets.

### Q7
Stem: Which imaging guides needle placement during a permanent-seed or HDR prostate implant, and what is its main limitation?
A. Kilovoltage cone-beam, limited by scatter
B. Transrectal ultrasound on a stepper registered to the template, limited by operator dependence and probe pressure that deforms the gland
C. Megavoltage portal imaging, limited by poor contrast
D. MRI in the operating room, limited by seed artifacts
Answer: B
Objective: II.6
Why: Transrectal ultrasound provides the volume study, live needle guidance, and the intraoperative check in the treatment position with no ionizing radiation; the probe sits on a stepper that is mechanically registered to the needle template. It depends on the operator, the probe deforms the prostate, and seeds become hard to see once many are placed, which is why a postimplant CT follows. Cone-beam, portal imaging, and intraoperative MRI are not the standard needle-guidance tool.

### Q8
Stem: What does a surface-guidance system measure, and in which situation does it fail?
A. The internal target position by infrared transmission through the skin; it fails on obese patients only
B. The position of implanted markers; it fails when fewer than three are present
C. The position of pelvic bone from a projected light pattern; it fails when the couch rotates
D. The external surface, reconstructed from a projected light pattern by several camera pods and compared with a reference surface; it fails when the surface is covered or when the target is not fixed to the skin
Answer: D
Objective: II.6
Why: Camera pods project structured light, reconstruct the surface many times per second, and report six-degree-of-freedom deviations from the planning-CT body contour or a captured reference, with no dose and the ability to hold the beam. A blanket, a bolus sheet, or a thermoplastic mask over the region removes the surface it needs, and an internal target that moves independently of the skin is invisible to it. The system does not transmit through skin, see markers, or see bone.

### Q9
Stem: An offline correction protocol images the first four fractions. The measured anterior-posterior shifts are +4, +2, +5, and +1 mm posterior. What correction is applied from the fifth fraction, and which error component does it address?
A. 4 mm posterior, the first-day value, addressing random error
B. 3 mm posterior, the mean, addressing the systematic setup error
C. 5 mm posterior, the maximum, addressing both components
D. 0 mm, because the protocol applies no action level
Answer: B
Objective: II.6
Why: Mean = (4 + 2 + 5 + 1) / 4 = 3 mm. Check: the deviations from 3 are +1, −1, +2, −2 and sum to zero. The mean estimates the systematic error, and the offline protocol applies it from the next fraction without a daily image; the day-to-day scatter around the mean is random and stays in the margin. Using the first day's value or the maximum carries one day's random error into every later fraction. The phrase no action level means no threshold on the applied mean, not a zero correction.

### Q10
Stem: A kilovoltage cone-beam deposits about 2 cGy per scan. A prostate course of 35 fractions to 70 Gy is imaged daily. What is the total imaging dose and its fraction of the prescription?
A. 2 cGy, about 0.03 percent, because imaging dose is not cumulative
B. 7 Gy, about 10 percent
C. 35 cGy, about 0.5 percent
D. 70 cGy, about 1 percent
Answer: D
Objective: II.6
Why: Total = 2 cGy × 35 = 70 cGy, and 70 / 7,000 = 0.01, about 1 percent of the prescription. Check: 1 percent of 70 Gy is 0.7 Gy. The dose is deposited at every scan, so it accumulates. Thirty-five centigray would be 1 cGy per scan. Seven gray would be 20 cGy per scan, which is in the megavoltage imaging range, not kilovoltage. TG-180 quotes roughly 0.5 to 5 cGy per kilovoltage cone-beam and suggests accounting for imaging dose when it approaches 5 percent of the therapeutic dose.
