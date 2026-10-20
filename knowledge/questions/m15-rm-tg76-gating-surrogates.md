# Module 15. Patient Immobilization and Motion Management Techniques

Original items. The TG-76 threshold, acquisition and gating modes, the MIP, compression and breath hold, and surrogates.

## TG-76 Thresholds, Gating Modes, and Surrogates

### Q1
Stem: A 4DCT shows a lung tumor moving 7 mm superior-inferior and 2 mm in the other directions. According to TG-76, what should the team do?
A. Nothing special, because the dominant direction is under 1 cm
B. Consider a motion-management technique, because the excursion exceeds 5 mm
C. Require real-time tracking, because any measured motion mandates it
D. Repeat the scan, because only motion over 2 cm is reportable
Answer: B
Objective: II.3
Why: TG-76 recommends considering a respiratory management technique when motion exceeds 5 mm in any direction, provided the patient tolerates it and the department offers it. Seven millimeters crosses that threshold. One centimeter and two centimeters are not the published thresholds, and the report does not mandate one specific technique; an ITV, gating, compression, or breath hold are all options.

### Q2
Stem: Which description matches a retrospective 4DCT acquisition?
A. The scanner is triggered to acquire only during a chosen breathing window, producing a single-phase data set
B. The patient holds a deep breath and a standard helical scan is taken
C. The scanner oversamples every couch position across a full breathing cycle while the trace is recorded, and the images are sorted into phases afterward
D. Two fast scans at inhale and exhale are registered to form the ITV
Answer: C
Objective: II.3
Why: A retrospective 4DCT acquires continuously with the respiratory trace, then bins the images by phase or amplitude after the scan, which is why it yields all ten phases plus the maximum-, average-, and minimum-intensity projections and a higher CT dose. Triggered acquisition inside a window is prospective gating. A breath-hold scan and a pair of extreme-phase scans are other ways to capture one or two positions, not a retrospective sort.

### Q3
Stem: A gating system is set so the beam turns on whenever the marker block lies within a displacement window of 3 mm around the end-exhale position, regardless of where the patient is in the timing of the cycle. Which gating mode is this?
A. Amplitude-based gating
B. Phase-based gating
C. Prospective breath-hold gating
D. Duty-cycle gating
Answer: A
Objective: II.3
Why: Amplitude gating keys the beam to the surrogate's displacement, which handles an irregular period well but is vulnerable to baseline drift. Phase gating keys the beam to a percentage of the cycle in time and assumes a regular rhythm. A breath hold is not a gate on a free-breathing trace, and duty cycle is a property of any gate, not a mode.

### Q4
Stem: The gating window is narrowed from the 30 to 70 percent phases to the 40 to 60 percent phases. What changes?
A. Residual motion inside the gate increases and treatment time falls
B. Residual motion is unchanged and the monitor units fall
C. Residual motion inside the gate decreases, the duty cycle falls, and the fraction takes longer
D. The ITV must be enlarged to cover the phases that were removed
Answer: C
Objective: II.3
Why: A narrower window admits less of the breathing excursion, so the target moves less while the beam is on, but the beam is enabled for a smaller fraction of each cycle. The monitor units are fixed by the plan, so the clock time rises as the duty cycle falls. The phases outside the gate are not treated, so the gated target volume shrinks rather than grows.

### Q5
Stem: A lower-lobe tumor sits on the dome of the diaphragm. The ITV is contoured on the maximum-intensity projection. What is the risk?
A. The MIP overstates the motion because the diaphragm adds a bright rim
B. Part of the excursion is hidden because the bright tumor merges with the bright diaphragm, so the ITV is too small
C. The MIP cannot be generated for tumors below the carina
D. The dose will be wrong because the MIP has the correct density only in lung
Answer: B
Objective: II.3
Why: The MIP keeps the brightest value each voxel takes over the cycle, which outlines a solid tumor cleanly against dark lung but loses the boundary where the tumor abuts soft tissue of similar density. Against the diaphragm, chest wall, or mediastinum the envelope is underestimated, and the fix is to contour each phase and combine the contours. The MIP is never the dose-calculation set, but that is a separate problem from the contour.

### Q6
Stem: A liver SBRT candidate has 1.8 cm of diaphragmatic motion, cannot hear coaching instructions, and cannot reliably hold a breath. Which TG-76 technique fits best?
A. Abdominal compression, with the ITV measured on a repeat 4DCT with the device in place
B. Audio-coached deep-inspiration breath hold
C. Phase-gated delivery with verbal coaching
D. No technique, because the motion is under 2 cm
Answer: A
Objective: II.3
Why: Compression is passive and needs no patient participation, which is why it suits a patient who cannot follow instructions or hold a breath. It cuts motion by about half rather than removing it, so the residual is measured with the plate on and covered by the ITV. Breath hold and coached gating both depend on the patient responding to cues. The 5 mm threshold has been exceeded more than threefold.

### Q7
Stem: What distinguishes active breathing control from a voluntary deep-inspiration breath hold?
A. Active breathing control uses an abdominal plate and voluntary breath hold does not
B. Active breathing control is used for right-sided breast only
C. Voluntary breath hold is monitored by a kilovoltage cone-beam during the hold
D. Active breathing control measures lung volume with a spirometer and closes a valve at a preset level, whereas a voluntary hold relies on the patient and a surface or marker monitor
Answer: D
Objective: II.4
Why: Active breathing control enforces the breath-hold volume with a spirometer and a valve that stops airflow at the chosen level. A voluntary deep-inspiration hold is reached by the patient, with surface imaging or a marker block confirming the level. Neither uses a compression plate, both are used for left-sided breast heart sparing, and a cone-beam is not the monitor for the hold itself.

### Q8
Stem: A gating trace comes from an infrared marker block on the abdomen. Which assumption does that approach make?
A. The tumor is visible on the infrared camera
B. The marker reports the tumor position without any imaging dose and without error
C. The surface motion keeps a stable relationship, including timing, with the tumor motion
D. The block replaces the need for a 4DCT
Answer: C
Objective: II.3
Why: An external surrogate is useful only while the surface and the tumor move together. The relationship can have a phase lag, differ between inhale and exhale, and drift during the fraction. The camera sees reflective dots, not the tumor; the absence of imaging dose does not make the surrogate error-free; and the excursion still has to be measured with a 4DCT or fluoroscopy.

### Q9
Stem: Which statement describes an implanted electromagnetic transponder system such as Calypso?
A. It is a kilovoltage imaging system that shows the prostate on each fraction
B. Three implanted beacons are excited by an array over the patient and their positions are reported continuously without ionizing radiation
C. It is a surface camera that tracks reflective markers taped to the skin
D. It images the beacons once before the beam and cannot detect motion during delivery
Answer: B
Objective: II.3
Why: The electromagnetic system localizes implanted wireless transponders several times per second, giving real-time position without imaging dose, and is used mainly for prostate with a lung version available. It is a localization tool, not an imaging device, so it does not display anatomy. The surface-camera description fits an optical system, and the one-shot description is the opposite of continuous tracking.

### Q10
Stem: Compared with an infrared marker block on the abdomen, implanted fiducials seen on kilovoltage imaging offer which advantage and which cost?
A. They track the tumor region directly but require an invasive placement with a pneumothorax risk in lung and can migrate
B. They avoid any imaging dose but cannot detect rotation
C. They are placed on the skin but need at least three to see translation
D. They remove the need for a 4DCT because motion is visible in real time
Answer: A
Objective: II.3
Why: Internal fiducials sit near the tumor and bypass the surface-to-tumor correlation problem, at the price of an invasive procedure, a pneumothorax risk for transthoracic placement, and possible migration. They are seen by kilovoltage imaging, which carries dose. At least three markers are needed to detect rotation, not translation. The excursion for planning is still measured on the 4DCT.
