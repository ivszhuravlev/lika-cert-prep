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

### Q20
Stem: A gated field needs 2.00 minutes of beam-on time. The duty cycle is 30%. How long is the gated slot on the clock?
A. 0.60 minutes, because 2.00 × 0.30 shortens the slot
B. 6.67 minutes, because clock time is beam-on time divided by the duty cycle
C. 2.00 minutes, because the monitor units fix the clock
D. 2.30 minutes, the sum of the beam-on time and the duty cycle
Answer: B
Objective: II.3
Why: 2.00 / 0.30 = 6.67 minutes. Multiplying by 0.30 makes gating look faster than free breathing. The monitor units are unchanged. The beam is enabled only 30% of the time, so the room time is longer.

### Q21
Stem: The ITV was drawn as the union of the CTV positions. The 4DCT excursion is 1.0 cm superior and 0.8 cm inferior. The setup margin is 0.5 cm. What extra margin belongs on that ITV?
A. 1.5 cm superior, the excursion plus the setup margin, added again
B. 1.0 cm superior and 0.8 cm inferior, the excursion copied onto the ITV
C. No planning-target margin, because an ITV already includes setup
D. 0.5 cm, the setup margin. The excursion is already inside the ITV
Answer: D
Objective: II.3
Why: The ITV is the CTV plus the internal margin. The planning target is that ITV plus setup. Adding the 1.0 cm excursion again covers lung the ITV already includes. Setup is not part of the ITV definition.

### Q22
Stem: A left-breast plan was scanned, contoured, and calculated in deep-inspiration breath hold. The first fraction is delivered while the patient breathes freely. What is wrong?
A. Nothing, because breath hold and free breathing share one external contour
B. Nothing, if the monitor units match the breath-hold plan
C. The plan and the delivery are different geometries. The heart position the plan used is not the free-breathing position
D. The energy has to change from 6 MV to 18 MV to cover the free-breathing heart
Answer: C
Objective: II.3
Why: Deep inspiration moves the heart inferior and posterior, away from the left chest wall. A free-breathing delivery puts that heart back toward the tangent. Matching monitor units does not restore the breath-hold anatomy, and the photon energy is not the mismatch.

### Q23
Stem: Liver stereotactic fields were planned on a 4DCT taken with the abdominal compression plate in place. Treatment is set up without the plate. Which ITV is now in use?
A. The wrong one. Motion was measured with the plate on, and the excursion without the plate is larger than the one the plan covered
B. The same one, because a plate changes density and not motion
C. A larger ITV automatically, because the planning system expands the target when the plate is removed
D. An ITV of zero, because removing the plate stops the diaphragm
Answer: A
Objective: II.3
Why: The internal target is measured with the device that will be on the patient. Taking the plate off lets the diaphragm travel farther than the compressed scan. The contour does not grow by itself. Compression reduces motion. It does not set that motion to zero.

### Q24
Stem: Surface guidance shows the chest surface inside the breath-hold tolerance. The target is a lower-lobe lung tumor. What has the surface system confirmed?
A. The superior-inferior position of the tumor, because the skin and a lower-lobe tumor are one rigid body
B. That the tracking margin can be set to zero
C. The Hounsfield numbers of the tumor
D. The surface that was watched. A surface match does not measure the tumor when the surface and the tumor disagree
Answer: D
Objective: II.3
Why: Surface guidance can coach and interrupt a breast breath hold. It does not see a lower-lobe tumor's superior-inferior position when the chest wall and the tumor move differently. A surface trace inside tolerance is not a zero-margin tracking result, and it does not edit the CT numbers.

### Q25
Stem: A tracking model was built from chest-wall markers at the start of the fraction. Midway through, the relationship between the skin and the tumor has drifted. The aperture is still following the original model. What is the beam following?
A. The tumor, because a model built at the start of the fraction cannot drift
B. The original correlation, which no longer describes the tumor
C. A new 4DCT that the linac acquires at every control point
D. The average-CT density, which corrects the drift without a new model
Answer: B
Objective: II.3
Why: A chest-marker model is only as good as the correlation it was built on. A baseline shift is that relationship changing during the fraction. The aperture then follows the old model, not the tumor. The average CT does not update the correlation, and the linac is not acquiring a new 4DCT at each control point.
