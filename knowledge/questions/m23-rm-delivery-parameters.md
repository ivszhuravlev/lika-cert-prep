# Module 23. Treatment Delivery Systems

Original items. Delivery settings and optimizer vocabulary for IMRT and VMAT.

## IMRT and VMAT Delivery Parameters

### Q1
Stem: A VMAT plan is re-optimized with jaw tracking enabled and nothing else changed. What does jaw tracking change about the delivered dose?
A. The optimized fluence inside each aperture becomes more uniform
B. Transmission through closed leaves and interleaf leakage outside the aperture are reduced, lowering the low-dose bath
C. The gantry can rotate faster because the jaws carry part of the modulation
D. The number of control points is halved because the jaws replace half of the leaf motion
Answer: B
Objective: III.5
Why: With jaw tracking the jaws follow the MLC opening at every control point and park over the closed leaves, so the 1–2 percent leaf transmission and the higher interleaf leakage outside the aperture are cut to the jaw transmission value. That lowers peripheral and low-dose-bath dose. The fluence inside the open aperture is set by the leaves and is not changed, gantry speed is governed by dose rate and leaf speed limits, and the control-point count is a planning setting unrelated to the jaws.

### Q2
Stem: A head-and-neck plan is produced two ways with similar target coverage and organ sparing: nine fixed-field sliding-window IMRT beams and two full VMAT arcs. Which statement about delivery is the usual exam expectation?
A. The sliding-window plan uses fewer monitor units because the beam is off while leaves move
B. Both plans use the same monitor units because the prescribed dose is the same
C. The VMAT plan uses fewer monitor units and less beam-on time
D. The VMAT plan uses more monitor units because dose is spread over 360 degrees
Answer: C
Objective: III.5
Why: VMAT delivers from every angle through relatively open apertures while the gantry moves, so a comparable plan typically needs fewer monitor units and shorter beam-on time than fixed-field IMRT, and the gap is largest against sliding window, which sweeps a narrow slit with the beam on. Sliding window is the high-MU technique, not the low one; beam-off during motion describes step-and-shoot. Monitor units are not fixed by the prescribed dose because the leaves block part of the beam for different fractions of the time. Spreading dose over many angles does not by itself raise monitor units.

### Q3
Stem: An optimizer evaluates a random change to the beamlet weights and, occasionally, keeps a change that makes the cost function worse, with that chance shrinking as the run proceeds. Which optimizer family is this?
A. Simulated annealing
B. Gradient descent
C. Direct aperture optimization
D. Leaf sequencing
Answer: A
Objective: III.5
Why: Accepting an uphill move with a probability that falls as a temperature parameter is lowered is the defining behavior of simulated annealing; it is how the method escapes a local minimum, at the cost of speed. Gradient descent always moves downhill and is deterministic. Direct aperture optimization is defined by what it optimizes (leaf positions and segment weights), not by this acceptance rule, although it may use annealing internally. Leaf sequencing converts a fluence map into segments and is not an optimizer.

### Q4
Stem: A planning system reaches its optimized fluence in a few seconds by stepping repeatedly in the direction that lowers the cost function fastest. What is the recognized limitation of that approach?
A. It cannot handle dose-volume objectives
B. It requires the segments to be defined before it starts
C. It produces a different answer every time it is run
D. It can stop in a local minimum because it never accepts an uphill step
Answer: D
Objective: III.5
Why: A gradient method follows the local slope and halts in the first valley it reaches, so for a non-convex problem it can miss a better solution elsewhere. It handles dose-volume objectives routinely. Needing predefined apertures describes direct aperture optimization. Producing a different result on each run is a property of stochastic methods such as simulated annealing, not of a deterministic gradient search.

### Q5
Stem: An inverse-planning engine treats the leaf positions and the weights of a fixed number of deliverable apertures as the variables it adjusts, so no separate conversion from a fluence map to segments is needed. Which approach is this, and what is its usual practical benefit?
A. Fluence-map optimization; it allows an unlimited number of beamlets
B. Direct aperture optimization; fewer segments and fewer monitor units for comparable plan quality
C. Simulated annealing; it guarantees the global minimum
D. Forward planning; the planner weights each aperture by hand
Answer: B
Objective: III.5
Why: Direct aperture optimization (DAO) optimizes the deliverable apertures themselves, so the delivered fluence equals the optimized fluence and the plan typically needs fewer segments and lower MU than a fluence-then-sequence chain. Fluence-map optimization is the two-step method DAO replaces. Simulated annealing is a search strategy, not a definition of the variables, and nothing guarantees a global minimum in these problems. Forward planning has no optimizer adjusting the apertures.

### Q6
Stem: A department's step-and-shoot IMRT template sets a floor on the monitor units any single segment may deliver. What floor is typical, in MU?
A. 0.5 MU
B. 3 MU
C. 20 MU
D. 50 MU
Answer: B
Objective: III.5
Why: A floor on the order of 3 MU per segment (commissioning choices run about 2–5 MU) is typical: the dose rate and symmetry are still stabilizing in the first fraction of a monitor unit, and very small segments are poorly modeled. A 0.5 MU floor would not remove those problem segments. Floors of 20 or 50 MU would strip most of the modulation out of a plan whose total is a few hundred MU per field.

### Q7
Stem: A conventional four-field plan delivers the 200 cGy fraction with 250 MU. The IMRT plan for the same prescription delivers it with 1000 MU. What is the IMRT factor?
A. 0.25
B. 750 MU
C. 4
D. 1250 MU
Answer: C
Objective: I.5
Why: The IMRT factor is the modulated MU divided by the conventional MU for the same dose: 1000 / 250 = 4. Check: 4 × 250 = 1000. Dividing the other way gives 0.25, which is the inverse. Subtracting gives 750 MU and adding gives 1250 MU; neither is a ratio, and the factor is dimensionless.

### Q8
Stem: A physicist uses an IMRT factor of 4 in an NCRP 151 shielding calculation for a vault that will treat mostly modulated plans. Which workload does the factor multiply?
A. The leakage and scatter workload used for the secondary barriers
B. The primary-barrier workload, because four times the monitor units means four times the primary beam
C. The use factor for each primary barrier
D. The occupancy factor of the adjacent rooms
Answer: A
Objective: I.5
Why: Head leakage and MLC transmission scale with monitor units, so the leakage (and patient-scatter) workload is multiplied by the IMRT factor. The primary beam still deposits the same dose at the isocenter per fraction, so the primary workload is unchanged. Use factor describes how often the beam points at a barrier and occupancy describes who is behind it; neither depends on modulation.

### Q9
Stem: A left-breast VMAT plan uses a 220-degree arc, and within it the planner defines a 40-degree span of gantry angles where the beam does not fire while the gantry continues to rotate. What is that span called, and why is it used?
A. A couch kick, to make the arc non-coplanar
B. A collimator offset, to smear interleaf leakage
C. A control-point gap, to let the dose rate stabilize
D. An avoidance sector, to prevent the beam from entering through the contralateral breast or the arm
Answer: D
Objective: III.5
Why: An avoidance sector is a set of gantry angles inside the arc where the beam is held off while rotation continues, chosen before optimization so unwanted entrance paths (contralateral breast, arms, couch rails, implanted devices) are excluded. A couch kick rotates the couch and is a different tool. Collimator offset concerns the leaf-leakage lines, not the gantry angles. Dose rate does not need a 40-degree pause to stabilize.

### Q10
Stem: A two-arc prostate VMAT plan sets the collimator to 30 degrees on the first arc and 330 degrees on the second. What is the reason for using two different, mirrored collimator angles rather than 0 degrees on both?
A. Interleaf leakage and tongue-and-groove lines from one arc do not stack on the lines from the other, and the leaves can cover a longer target
B. Mirrored angles halve the monitor units because each arc carries half the fluence
C. A 0-degree collimator is forbidden by the record-and-verify system during arc delivery
D. The angles are chosen so that the beam avoids the femoral heads
Answer: A
Objective: III.5
Why: At 0 degrees the leakage between leaves and the tongue-and-groove underdose line up along the leaf-travel direction for the whole arc; rotating the collimator and offsetting the arcs spreads those lines so they do not coincide, and the rotated leaf bank can span a target longer than the leaf travel. Monitor units are set by modulation, not by mirrored angles. Zero degrees is allowed, just not preferred. Beam entrance through the femoral heads is governed by gantry angles and avoidance sectors, not by collimator rotation.
