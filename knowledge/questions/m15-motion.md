# Module 15 — Patient Immobilization and Motion Management Techniques

Original items on respiratory motion, 4DCT data sets, and the devices that limit or follow motion.

## Management of Respiratory Motion

### Q1
Stem: A lower-lobe lung tumor moves 1.5 cm superior-inferior on a 4DCT. An upper-lobe tumor in the same patient moves 3 mm. The usual pattern this illustrates is:
A. Lower-lobe and diaphragmatic targets move more than upper-lobe targets, and the largest component is often superior-inferior
B. Upper-lobe targets always move more than 1.5 cm
C. Motion is only left-right
D. Motion of 1.5 cm can be ignored because the CT slice is thicker
Answer: A
Objective: II.3
Why: The diaphragm drives lower-lobe, liver, and inferior targets more than apical targets. The dominant direction is usually superior-inferior. A 1.5 cm excursion is large compared with stereotactic margins and is not erased by slice thickness.

### Q2
Stem: An ITV is constructed for a free-breathing lung plan. The ITV is meant to cover:
A. The CTV plus its respiratory excursion
B. Only the setup error, with motion excluded
C. The prescription isodose
D. The immobilized external contour
Answer: A
Objective: II.3
Why: ICRU internal margin accounts for physiologic motion. The ITV is that internal volume around the CTV. Setup uncertainty is added afterward to make the PTV. The ITV is not an isodose line and it is not the skin contour.

### Q3
Stem: A lung GTV is drawn on the maximum-intensity projection and the dose is calculated on that same MIP. Why is the dose calculation the weak step?
A. MIP voxel values are the brightest pixel over the cycle, not the tissue density the beam will see
B. MIP is the average density, so it is the preferred calculation set
C. A MIP cannot show a tumor that is denser than lung
D. Dose calculation is illegal on any 4DCT-derived image
Answer: A
Objective: II.3
Why: The MIP is a useful envelope for a solid tumor moving through low-density lung. Those voxel values are maxima, so calculating dose on them assigns the wrong density along the path. The average CT, or a gated phase with its own density, is the calculation data set. Dose calculation on a properly chosen 4DCT phase or average is routine.

### Q4
Stem: End-exhalation gating is often preferred to end-inspiration gating because:
A. Exhalation is more reproducible and the residual motion inside the gate is smaller for many patients
B. Inspiration always has zero tumor motion
C. Gating removes the need for a CTV
D. The duty cycle at exhalation is 100%, so treatment time does not change
Answer: A
Objective: II.3
Why: Patients can hold or revisit a quiet exhale more consistently than a full inhale, so the gate is tighter. Inspiration is not motion-free. The CTV for microscopic disease remains. A respiratory gate has a duty cycle below 100%, so the beam-on time gets longer.

### Q5
Stem: Deep-inspiration breath hold for a left breast tangent is used to:
A. Increase the distance between the chest wall and the heart
B. Increase motion of the heart into the tangent
C. Replace all bolus
D. Change 6 MV photons into electrons
Answer: A
Objective: II.3
Why: A deep inspiration pushes the heart inferior and posterior relative to the left chest wall, so less heart sits in the tangent. The technique is a motion-management choice, not a bolus substitute and not a change of particle.

### Q6
Stem: Abdominal compression for liver SBRT is intended to:
A. Limit diaphragm excursion so the target motion is smaller
B. Increase the breathing amplitude for a larger ITV
C. Create a CT density of zero in the liver
D. Replace fiducials by stopping the heart
Answer: A
Objective: II.3
Why: Compression reduces the superior-inferior travel of liver and lower-lung targets so the ITV or the gated window can be smaller. It does not increase amplitude, it does not zero the liver density, and it does not stop cardiac motion or universally remove the need for a surrogate.

## Respiratory Motion Management Mini-Quiz

### Q1
Stem: Which strategy covers motion by enlarging the irradiated volume rather than by turning the beam on only in one phase?
A. An ITV from a 4DCT, treated while the patient breathes freely
B. Respiratory gating
C. Breath hold
D. Real-time tracking with a moving aperture
Answer: A
Objective: II.3
Why: Motion-encompassing methods (ITV, slow CT, MIP contour) irradiate the whole path. Gating and breath hold limit when the beam is on. Tracking moves the aperture with the target. Those are different TG-76 families.

### Q2
Stem: A gated treatment has a 30% duty cycle. Compared with treating the same monitor units continuously, the delivery:
A. Takes substantially longer, because the beam is off during most of the breathing cycle
B. Takes the same time, because MU are unchanged
C. Takes less time, because gating raises the dose rate by 1/0.30
D. Cannot be combined with IMRT
Answer: A
Objective: II.3
Why: Duty cycle is the fraction of time the beam is enabled. At 30%, most of the breathing period is waited out, so session time rises even though the MU total is the plan MU. The linac does not automatically multiply dose rate by 1/0.30 to erase that wait. Gated IMRT and VMAT are used clinically.

### Q3
Stem: Real-time tracking still needs a surrogate (fiducial, surface, or implanted marker) because:
A. The tumor itself is often not continuously visible on the treatment imager, so a correlated signal stands in for it
B. A surrogate removes any need to check the correlation with the tumor
C. Tracking works only if the surrogate is known to be uncorrelated
D. Surrogates are required for head-and-neck plans with no respiratory motion
Answer: A
Objective: II.3
Why: Liver and some lung tumors are hard to see on planar images or CBCT in real time. A fiducial or surface trace is useful only while its correlation with the tumor holds. An uncorrelated signal would aim the beam at the wrong place. Sites without the motion do not need respiratory tracking.

### Q4
Stem: Audio-visual coaching is added to gating or breath hold in order to:
A. Help the patient repeat the same amplitude or phase so the residual motion inside the window stays small
B. Increase irregular breathing, which improves 4DCT sorting
C. Replace the 4DCT entirely
D. Change the HU of the lung
Answer: A
Objective: II.3
Why: Coaching reduces irregular cycles that both smear a 4DCT and break a gate. It does not replace the planning images, and it does not change density. Irregular breathing is the problem, not the goal.

### Q5
Stem: A 4DCT of an irregular breather shows a duplicated diaphragm and a tumor that appears cut in half on one phase. Those findings are:
A. Sorting artifacts, and the data set should not be used for an ITV until the scan is repeated or re-binned
B. Proof that the tumor has two GTVs
C. The normal appearance of a maximum-intensity projection
D. A sign that abdominal compression was perfect
Answer: A
Objective: II.3
Why: Phase or amplitude sorting assumes a reasonably regular trace. A cough or a missed breath assigns slices to the wrong phase and can duplicate or truncate anatomy. That is not a second tumor and it is not what a clean MIP looks like. Compression is irrelevant to a sorting error already in the images.
