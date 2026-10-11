# Module 38. Deformable dose accumulations

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Deformable Registration and Dose Accumulation

### Q1
Stem: What does deformable dose accumulation try to add?
A. Dose in voxels that share the same CT coordinates
B. Only the DVH points above 95%
C. Dose to the same tissue element after it moves
D. Monitor units from each fraction
Answer: C
Objective: IV.5
Why: Deformable registration estimates where each bit of tissue went, and accumulation paints the dose onto that moving element. Adding voxels that merely sit at the same x, y, z misses organ motion. Correct choice: Dose to the same tissue element after it moves. That is a rigid, same-grid sum. Deformable accumulation is used when the tissue has moved. The tool maps a dose distribution, not a single DVH statistic. MU are not deformed. Dose is.

### Q2
Stem: Where is a deformable map especially untrustworthy?
A. A rigid skull with a good bone match
B. A water phantom with no motion
C. Two identical CT scans taken minutes apart with no change
D. Sliding lung against the chest wall
Answer: D
Objective: IV.5
Why: Lung slides along the chest wall. A smooth deformable algorithm often shears that interface incorrectly, so dose mapped from lung into rib, or the reverse, can be fiction. Correct choice: Sliding lung against the chest wall. Bone in the skull is a favorable rigid problem, not the failure mode of DIR. There is nothing to deform. The map should be nearly the identity. That is an easy case, not a hard one.

### Q3
Stem: A voxel that received 2.0 Gy is mapped into a region the deformation stretched by a volume factor of 1.5. What dose should be recorded for that tissue element?
A. 3.0 Gy
B. 2.0 Gy
C. 1.5 Gy
D. 0.75 Gy
Answer: B
Objective: IV.5
Why: If the correspondence is right, the tissue element still received 2.0 Gy. The wrong scaling 2.0 × 1.5 = 3.0 invents dose, and 2.0 / 1.5 = 1.33 would dilute it. A wild volume change is a reason to distrust the map, not a reason to scale the gray. The recorded dose for that element is 2.0 Gy. 3.0 Gy multiplies dose by the volume factor. Dose is energy per mass, not a volume. 1.5 is the stretch factor, not the dose. Dividing 2.0 by 1.5 treats dose as if it diluted with the painted volume.

### Q4
Stem: Daily CTs show rectal gas appearing and disappearing. What is the right level of trust in a deformable sum through that gas?
A. High, because the algorithm always conserves dose
B. High if the dice coefficient of the rectal contour is above 0.9
C. The sum is exact once both plans use the same dose grid
D. Low, because gas has no stable tissue to follow
Answer: D
Objective: IV.5
Why: Gas is not a stable piece of the patient. A deformable vector through a bubble that did not exist yesterday has nothing reliable to follow, so the accumulated dose there should not be treated as exact. Correct choice: Low, because gas has no stable tissue to follow. Many maps do not conserve energy, and gas has no anatomy to lock onto. A contour score can look good while the interior correspondence is wrong. Grid size is a sampling issue. It does not create tissue identity inside moving gas.

### Q5
Stem: An accumulated parotid DVH looks smooth after 20 fractions of deformable mapping. What can that DVH not prove?
A. That the registration was accurate
B. That a mean dose was computed from the mapped distribution
C. That the planner remembered to export a dose
D. That the dose grid had a finite spacing
Answer: A
Objective: IV.5
Why: A smooth accumulated DVH is an output of the map you gave it. Overlap scores and pretty curves do not prove the vectors are right, especially after weight loss or in the abdomen. Correct choice: That the registration was accurate. A mean can be computed from any map, accurate or not. The DVH existing shows a dose was sampled. It does not validate the vectors. Every clinical grid has a spacing. Smoothness does not audit it.

### Q6
Stem: After a trustworthy deformable registration, an organ with α/β = 3 Gy has already received 40 Gy in 2 Gy fractions and will receive 30 Gy in 10 fractions of 3 Gy. What is the biological sum?
A. 70 Gy
B. 76 Gy EQD2
C. 66 Gy EQD2
D. 106 Gy, the sum of the two BEDs
Answer: B
Objective: IV.5
Why: The first course is already in 2 Gy fractions, so its EQD2 is 40 Gy. The second course: EQD2 = 30 × (3+3)/(2+3) = 30 × 6/5 = 36 Gy. The biological sum is 40 + 36 = 76 Gy EQD2. Adding the physical doses gives 70 Gy and ignores fraction size. 66 Gy uses (3+3)/(3+3) or a similar slip. Adding BEDs, 40×(1+2/3)=66.7 and 30×(1+3/3)=60, sums to about 127, not an EQD2.

### Q20
Stem: Deformable dose accumulation is run from a planning CT to a later CT for a lung target. The software finishes with no error flag. The voxels in question lie where lung meets chest wall, and the lung has slid along that wall between scans. How should the mapped dose on that interface be used?
A. As the delivered dose, because an error-free run means the slip plane was preserved
B. As unreliable; a smooth deformable algorithm commonly shears a sliding lung–chest wall boundary and can assign lung dose to chest wall or chest-wall dose to lung
C. As exact once the accumulated DVH looks smooth
D. As a rigid voxel sum, which is the preferred method exactly where tissue slides
Answer: B
Objective: IV.5
Why: Answer B. Lung slides along the chest wall. Most deformable algorithms apply a smooth transform and smear that slip plane, so dose near the interface can be given to the wrong tissue. A finished run with no error message does not prove the vectors followed the slide. A smooth DVH is only the output of whatever map was supplied. Adding voxels that share planning-CT coordinates is the method that ignores the motion; it is not the fix for a sliding boundary.

### Q21
Stem: The simulation CT shows little rectal gas. A scan during treatment shows a large gas pocket that was not present at simulation. A deformable vector is driven through the pocket and the doses are summed. What level of trust does that sum deserve inside the new gas?
A. High, because a deformable map conserves dose in tissue that appeared between scans
B. High when the rectal contour Dice coefficient is above 0.9, regardless of the interior
C. Low; gas that appears between scans is not stable tissue, so the vector has nothing reliable to follow
D. High once both dose grids use the same spacing, because spacing creates tissue identity
Answer: C
Objective: IV.5
Why: Answer C. Gas is not a piece of the patient that can be followed from one scan to the next. A vector through a bubble that did not exist at simulation has no stable tissue to lock onto, so the dose assigned inside that pocket should not be treated as exact. Contour overlap can look good while the interior correspondence is wrong. Matching the dose-grid spacing only controls sampling. It does not create tissue identity, and a new gas volume is not a place where energy conservation rescues the map.

### Q22
Stem: A voxel that received 2.0 Gy is mapped into tissue the deformation stretched by a volume factor of 1.5. Which report is defensible?
A. 3.0 Gy, because the dose scales by the volume factor
B. 2.0/1.5 Gy, because the dose dilutes with the painted volume
C. 2.0 Gy, because a factor of 1.5 confirms that the same element was found
D. No precise dose; the stretch means the map is not reliable, and neither 2.0 Gy nor a value rescaled by 1.5 can be defended
Answer: D
Objective: IV.5
Why: Answer D. A volume factor of 1.5 is evidence that the correspondence failed, not a number to multiply or divide into the gray. Dose is energy per mass. Multiplying 2.0 by 1.5 to get 3.0 invents energy. Dividing 2.0 by 1.5 invents a dilution the map did not measure. Reporting 2.0 Gy as if the same element had been found treats the broken correspondence as proof. The defensible statement is that the map is not reliable there, so no precise dose should be quoted for that element.

### Q23
Stem: After substantial weight loss the deformable map compresses an old high-dose region into less tissue. The accumulated maximum is printed to a tenth of a gray. Why is that printed value not a dose to trust?
A. Dose is energy per mass; squeezing the old distribution into a body that has lost mass does not conserve energy, so the tenths of a gray are not a corrected result
B. Multiplying the original gray by the volume factor restores the energy and makes the tenth of a gray exact
C. A smooth accumulated curve conserves energy even when the patient has lost a large amount of mass
D. Mass change affects only the lung–chest wall interface, so a neck sum is exact
Answer: A
Objective: IV.5
Why: Answer A. Warping dose from a larger body onto a smaller one does not conserve energy. The same energy cannot be squeezed into less mass and still mean the original gray. A printout to 0.1 Gy only shows the precision of the arithmetic on that map. It does not repair the mass change. Scaling by the volume factor is not a defended correction. Smoothness does not restore conservation, and weight loss in the neck is the same mass problem as weight loss anywhere else.

### Q24
Stem: Chest-wall dose has been accumulated across a sliding lung boundary for an entire course. The chest-wall DVH is smooth, and the lung contour overlap score is high. What do those displays fail to prove?
A. That some dose values were sampled
B. That the software wrote a curve
C. That the vectors followed the correct tissue across the slip plane
D. That the dose grid had a finite spacing
Answer: C
Objective: IV.5
Why: Answer C. A smooth accumulated DVH and a high overlap score are outputs of the map that was supplied. They show that a curve was computed from sampled dose. They do not show that a sliding lung–chest wall interface was followed rather than sheared. Every clinical grid has a spacing. Overlap and smoothness do not audit it, and they do not audit the vectors.

### Q25
Stem: Rectal gas is present on the second scan and absent on the first. In the same map, a voxel of 2.0 Gy is painted into tissue stretched by a volume factor of 1.5. Which conclusion should be reported?
A. The tissue received exactly 2.0 Gy, because new gas does not weaken correspondence
B. The tissue received 3.0 Gy, the product of 2.0 and 1.5
C. The tissue received 2.0/1.5 Gy, because dose dilutes with the stretch
D. The map is not reliable in that region; appearing gas and a large volume change are reasons to withhold a precise dose
Answer: D
Objective: IV.5
Why: Answer D. Gas that appears between scans gives the algorithm nothing stable to follow, and a stretch of 1.5 is a further sign the correspondence is not trustworthy. Neither finding supplies a factor that turns 2.0 Gy into a corrected dose. The product 3.0 Gy and the quotient 2.0/1.5 Gy are invented scalings. Quoting 2.0 Gy as exact ignores both warnings. The report should say the map is not reliable there.
