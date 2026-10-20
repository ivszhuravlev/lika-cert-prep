# Module 23. Treatment Delivery Systems

Original items. Dynamic-MLC QA tests, dynamic conformal arc versus VMAT, delivery-time trade-offs, IMRT beam separation, compensator IMRT, and electron obliquity.

## Dynamic MLC QA, Conformal Arcs, and Compensator IMRT

### Q1
Stem: A physicist is commissioning sliding-window IMRT on a new linac and asks for the classic set of dynamic-MLC tests. Which list is that set?
A. Output constancy, flatness, symmetry, and light-field to radiation-field coincidence
B. A picket-fence image at gantry zero, repeated weekly
C. Mid-leaf transmission and the dosimetric leaf gap
D. Leaf speed, leaf acceleration and deceleration, positional accuracy of a sliding gap, dose-rate stability, and a beam-interrupt test
Answer: D
Objective: III.5
Why: Dynamic delivery assumes that each leaf is at the programmed position when the programmed monitor units have accumulated, so the test set checks speed, speed changes, gap width, independence from dose rate, and recovery after a beam hold. Output, flatness, symmetry, and light-field coincidence are general machine tests that do not exercise leaf motion. A picket fence is one positional check, not the set. Transmission and the dosimetric leaf gap are planning-system parameters measured once, not the dynamic test suite.

### Q2
Stem: In a leaf-speed test, every leaf pair sweeps a fixed gap across the field at a programmed speed and the fluence is recorded on a detector array. One leaf's track shows a band of lower intensity than its neighbors. What does that band mean?
A. That leaf is moving faster than programmed, so the gap exposes each point for too short a time
B. The accelerator dose rate drifted during the sweep
C. Gantry sag moved the whole field
D. The flattening filter is off center
Answer: A
Objective: III.5
Why: The dose at a point under a sweeping gap is proportional to how long the gap is open over it; a leaf that runs fast shortens that time along its own track and leaves a cold band, and a slow leaf leaves a hot band. TG-142 lists leaf travel speed among the monthly IMRT checks, with a loss of leaf speed greater than 0.5 cm per second as the action level. A dose-rate drift would affect all leaves together, not one track. Gantry sag and a filter offset shift or tilt the whole field rather than one leaf's path.

### Q3
Stem: A sliding-gap positional test is run with a nominal 10 mm gap. Measurement shows the gap actually delivered was 10.5 mm. By about what percentage does the delivered fluence differ from the expected value?
A. 0.5 percent
B. 2 percent
C. 5 percent
D. 10.5 percent
Answer: C
Objective: III.5
Why: Fluence under a sweeping gap is proportional to the gap width, so the error is 0.5 / 10 = 0.05, or 5 percent. Check: a 10.5 mm gap exposes each point 5 percent longer than a 10 mm gap. Half a percent is the error in millimeters misread as a percentage. Two percent has no basis in the ratio. Reporting 10.5 percent confuses the gap width with the error; note that the same 0.5 mm error on a 5 mm gap would be a 10 percent error, which is why sub-millimeter gap accuracy matters for sliding window.

### Q4
Stem: During a dynamic-MLC interrupt test, a sliding-window field is deliberately paused by a beam hold part-way through and then resumed. What result shows that the machine passed?
A. The resumed field delivers about half the planned dose
B. The interrupted and uninterrupted fluence maps agree within tolerance, showing the leaves resumed from the correct positions and the remaining monitor units were delivered
C. A hot line appears where the leaves stood during the pause
D. The field restarts from the first control point and the total dose doubles
Answer: B
Objective: III.5
Why: The test proves that after a hold the control system knows where the leaves were and how many monitor units remain, so the completed field matches an uninterrupted delivery. A half-dose field would mean the remainder was never delivered. A hot line at the pause position would mean the beam stayed on while the leaves stopped, which is a failure. Restarting from the first control point would double-dose the first part of the field, also a failure.

### Q5
Stem: The same sliding-window pattern is delivered at 100, 300, and 600 monitor units per minute and the three fluence maps are compared. What is the purpose of this test?
A. To find the dose rate that produces the highest output
B. To measure leaf transmission at each dose rate
C. To calibrate gantry rotation speed
D. To confirm that the delivered fluence does not depend on dose rate, because leaf motion is synchronized to accumulated monitor units rather than to clock time
Answer: D
Objective: III.5
Why: In dynamic delivery the leaf positions are tied to the fraction of monitor units delivered; if the controller kept time instead, a change in dose rate would change where the leaves are when a given dose is delivered and the fluence would shift. Agreement across dose rates is the pass criterion. Output is calibrated by monitor units and is not what the test seeks. Leaf transmission is a static measurement unrelated to dose rate. Gantry speed is a VMAT parameter and the test is run at a fixed gantry angle.

### Q6
Stem: During an arc, the MLC continuously reshapes so that the aperture matches the beam's-eye-view outline of the target at every gantry angle, while the dose rate and gantry speed remain constant. What is this technique, and how does it differ from VMAT?
A. A dynamic conformal arc; only the aperture follows the target, with no fluence modulation inside the field and no dose-rate variation
B. VMAT; any arc with moving leaves is modulated by definition
C. Classical rotation therapy; the aperture is fixed
D. Helical tomotherapy; the binary leaves follow the target
Answer: A
Objective: III.5
Why: A dynamic conformal arc is a 3D conformal technique whose leaves track the projected target shape, so it is conformal but not modulated; VMAT adds variable dose rate, variable gantry speed, and inverse-optimized apertures that need not match the outline. Moving leaves alone do not make an arc VMAT. Rotation therapy uses a fixed aperture, which this stem rules out. Helical tomotherapy is a ring gantry with couch motion and a binary fan-beam collimator.

### Q7
Stem: Two IMRT plans deliver the same fluence maps, one by step-and-shoot with many segments per field and one by sliding window. Which statement about delivery is the usual expectation?
A. Step-and-shoot is faster because it uses fewer monitor units
B. The two take the same time because the fluence is identical
C. Sliding window usually takes less clock time per field despite needing more monitor units, because there is no beam-off dead time between segments
D. Sliding window takes longer because the leaves must sweep across the entire field
Answer: C
Objective: III.5
Why: Step-and-shoot turns the beam off between segments and waits for leaves to settle, so a heavily segmented field accumulates dead time; sliding window keeps the beam on throughout the sweep. The monitor-unit comparison and the time comparison go in opposite directions: sliding window spends more MU and less time. Fewer monitor units do not make step-and-shoot faster when the pauses dominate. Identical fluence does not imply identical delivery mechanics.

### Q8
Stem: A planner sets up a seven-field prostate IMRT plan. Which rule about beam angles do IMRT planning guidelines follow?
A. Use parallel-opposed pairs so that entrance and exit doses cancel
B. Avoid directly opposed beams and keep each beam's entry at least about 10 to 15 degrees away from the exit path of any other beam
C. Confine all beams to a 90 degree sector on the anterior side
D. Always use an even number of beams
Answer: B
Objective: III.5
Why: Opposed beams traverse the same ray, so their fluences along it are nearly interchangeable; the pair adds little freedom to the optimizer while stacking entrance and exit dose on one line, which is why a 10 to 15 degree separation from any other beam's exit is the rule and odd numbers of equispaced beams (5, 7, 9) satisfy it automatically. Entrance and exit doses add, they do not cancel. A single sector forfeits the dose spreading that multiple angles provide. Even numbers of equispaced beams produce exactly the opposed pairs the rule avoids.

### Q9
Stem: A clinic delivers IMRT with milled solid brass compensators instead of MLC modulation. Compared with MLC-based IMRT, which description is correct?
A. Identical resolution and monitor units; the compensator only lowers skin dose
B. Coarser spatial resolution, more monitor units, and more leakage
C. Beam hardening is eliminated because no metal is in the beam
D. Finer spatial resolution, fewer monitor units and less leakage than sliding window, but one device per field with the risk of mounting the wrong compensator or the wrong orientation
Answer: D
Objective: III.5
Why: The milling bit is finer than a leaf width, the whole field is open at once so no MU are spent with leaves covering the target, and there is no interleaf leakage; the price is fabrication, beam hardening in the thick regions, and a manual mounting step that must be verified against the plan like a block. The compensator does not lower skin dose; it is kept 15 to 20 cm off the skin for that reason. Resolution is finer, not coarser. Metal in the beam hardens it.

### Q10
Stem: An electron beam strikes a sloping skin surface about 30 degrees from the normal, and the air gap is not filled with bolus. Compared with normal incidence, what happens to the depth-dose distribution measured perpendicular to the skin?
A. The depth of maximum moves deeper and the surface dose falls
B. The depth of maximum moves toward the surface, the surface dose rises, and the low-value isodose lines bulge outward and deeper at the edges
C. Nothing changes, because electron depth dose does not depend on the angle of incidence
D. The practical range doubles
Answer: B
Objective: III.5
Why: Oblique incidence shortens the perpendicular distance over which electrons build up, so dmax is shallower and the surface dose is higher, while side scatter from the thick side of the slope pushes the low-dose lines outward and deeper. The practical range along the beam is unchanged, not doubled. Deeper dmax with lower surface dose is the reverse of what obliquity does. Electron depth dose is strongly dependent on incidence angle, which is why bolus is used to level a sloping surface.
