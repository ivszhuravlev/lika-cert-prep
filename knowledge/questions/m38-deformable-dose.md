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
