# Module 23. Treatment Delivery Systems

Machine differences the exam actually scores: how the beam is on or off while the leaves move, what a beamlet is, what helical tomotherapy adds, and what happens to integral dose when you add beams.

## Rotation Therapy and VMAT

**MDCB objectives:** III.5, I.5

**What the exam expects**

You can separate an old conformal arc from VMAT, describe helical tomotherapy, and explain why adding beams or arcs tightens the high dose and spreads the low dose. You can define a beamlet as a fluence element the optimizer weights, not as an aperture the machine fires by itself.

**Core facts**

Classic rotation therapy is an arc with a fixed aperture. Gantry speed and dose rate are steady. The high-dose region is pulled into the center of the rotation. There is no intensity modulation inside the field. It is still a reasonable mental model for why a full rotation surrounds a deep target, and it is a poor description of a modern arc plan.

VMAT modulates during the rotation. Gantry angle, dose rate, gantry speed, and MLC shape all change while the beam is on. The plan is inverse-planned from objectives. Delivery is usually faster than a seven-to-nine-field step-and-shoot plan of similar complexity. Monitor units still rise when the modulation is heavy, because leaves cover part of the field during beam-on. “VMAT always uses fewer monitor units than IMRT” is too strong. “VMAT is beam-on during motion and usually spends less clock time than many static IMRT angles” is the fair statement.

Helical tomotherapy puts a 6 MV linac on a ring. The couch moves through the bore while the source rotates, so the trajectory is a helix. The field is a fan. Leaves of the binary collimator are either open or closed and they switch quickly. Jaw width, pitch, and modulation factor are the plan parameters you should recognize.

Pitch is couch travel per rotation divided by the fan width. Pitch below 1 means successive rotations overlap. A pitch that is too high leaves a thread of dose ripple. The acceptable pitch is a commissioning and planning rule. Confirm it in the tomotherapy planning protocol.

The modulation factor limits how uneven the leaf-open times may be. A higher factor allows sharper intensity changes, keeps leaves closed for more of the beam-on time, and lengthens the fraction. It is the tomotherapy cousin of “more modulation, more monitor units.” Image guidance on that machine is an MVCT acquired with the treatment beam detuned for imaging, not a kV cone-beam.

A beamlet (bixel) is one small element of a fluence map. Inverse planning divides each beam direction into beamlets and assigns a weight to each. The leaf sequencer turns that fluence into MLC motion: segments for step-and-shoot, a sweeping gap for sliding window, or open-times for binary leaves. A beamlet is not a deliverable control point by itself. If the sequencer cannot reproduce the map, the delivered fluence is not the optimized fluence. That is why a plan QA measurement exists.

Integral dose is the energy deposited in the patient, the dose integrated over mass. For a fixed target dose, every new entrance path deposits dose in tissue that was not in the original fields. Adding beams or arcs usually conforms the high dose better and raises the volume of tissue receiving a low dose. The integral dose goes up. A parallel organ and a contralateral structure feel that bath. A serial organ next to the target often prefers the conformal high-dose edge anyway. The trade is real: tighter 95% coverage is not free tissue.

**Formulas**

Pitch, helical tomotherapy:

pitch = couch travel per rotation / field width.

If the couch moves 1.0 cm per rotation and the field width is 2.5 cm,

pitch = 1.0 / 2.5 = 0.40.

That pitch overlaps. Whether 0.40 is the value your planning protocol wants is a local rule. Confirm it in the protocol. The exam point is the definition and the direction: higher pitch, less overlap, more risk of ripple.

Integral dose, conceptually:

energy imparted ≈ sum of (dose × mass) over the body.

You rarely compute this as a single number on an exam. You use it to predict the direction of a change. Two full arcs versus a weighted parallel-opposed pair: the arcs pull high dose off the subcutaneous tissue and paint a low dose around the torso. Integral dose and the low-dose volume rise. State that direction.

**Traps**

- Calling every arc VMAT. An unmodulated arc is rotation therapy.
- Describing tomotherapy as step-and-shoot C-arm IMRT. The delivery is helical, the collimator is binary, and the imaging is MVCT.
- Treating a beamlet weight as a monitor-unit setting the therapist dials in.
- Adding fields until the DVH of the target is perfect and never looking at the low-dose wash or the integral dose.
- Assuming more beams always reduce lung mean dose. Sometimes the extra paths cross more lung.

**Sources**

- AAPM TG-148, quality assurance for helical tomotherapy, for pitch, modulation, and MVCT practice. Confirm numeric tolerances in the report.
- ICRU 83, for the fluence-to-dose reporting that inverse planning produces
- Planning-system commissioning reports, for the local pitch and modulation limits

## Static IMRT

**MDCB objectives:** III.5, I.5

**What the exam expects**

You can contrast step-and-shoot with sliding window on two points: whether the beam is off while the leaves move, and which technique uses more monitor units and which carries more dead time. You can still define a beamlet, because static IMRT is inverse planning too.

**Core facts**

Static IMRT, or segmented multileaf collimation (step-and-shoot), delivers a stack of discrete apertures. The beam is on for a segment. The beam turns off. The leaves step to the next aperture. The beam turns on again. Intensity is a staircase of segment doses. Monitor units are spent only while an aperture is open. Clock time includes the dead time of leaf motion and of the checks between segments. A highly segmented plan can be slow even when the monitor units look moderate.

Sliding window, or dynamic multileaf collimation, keeps the beam on while a gap between opposed leaves sweeps across the field. The dose at a point depends on how long the gap exposes it. The fluence can be smoother than a short list of segments. Because the beam is on while leaves cover most of the field, more monitor units are required for the same target dose. Dead time between segments largely disappears. The usual exam contrast is: sliding window uses more monitor units and usually less dead time; step-and-shoot turns the beam off while the leaves move and usually uses fewer monitor units for a comparable map.

Both start from beamlets. Building the intensity profile that meets the plan goals is intensity modulation, the fluence optimization. The optimizer produces that fluence. The sequencer produces either segments or a trajectory. If the leaf speed, the minimum gap, or the minimum segment monitor units cannot realize a beamlet, the delivered dose departs from the optimized dose. Plan QA is the check.

Leaf transmission and interleaf leakage are present in both techniques and are larger, as a fraction of the target dose, when the monitor units are high. A sliding-window plan with a large MU-to-dose ratio puts more leakage into the patient outside the nominal aperture. That leakage is one reason integral dose and the low-dose bath rise with heavy modulation, even inside a single beam.

Forward-planned field-in-field is not inverse IMRT. The planner copies the open field, closes a subfield over a hot spot, and weights the subfield by hand. It is the usual whole-breast technique. It has segments and beam-off leaf motion, and it has no beamlet optimizer. Call it field-in-field unless the stem describes inverse objectives.

**Formulas**

A schematic, not a machine measurement, to fix the monitor-unit direction. Suppose an open 10 × 10 reference delivers about 1 cGy per monitor unit at the calibration point. A 180 cGy fraction from that open field is on the order of 180 MU plus the TMR, output-factor, and inverse-square corrections you already know. A sliding-window version of a modulated field that leaves the aperture covered for a large fraction of beam-on time can require several times those monitor units to deposit the same 180 cGy in the target. A step-and-shoot version spends its monitor units only in open segments, so the MU total is typically lower, and the clock adds the pauses. Quote this as a direction. Quote a measured MU only when the stem prints one.

Efficiency, in words:

monitor units per gray go up as the leaves block more of the beam during beam-on.

Sliding window does that blocking while the beam is on. Step-and-shoot does the moving while the beam is off.

**Traps**

- Reversing the monitor-unit statement. Sliding window is the high-MU, beam-on-while-moving technique.
- Reversing the dead-time statement. Step-and-shoot pays dead time between segments.
- Calling field-in-field a sliding-window inverse plan.
- Forgetting leakage when MU per gray is very high.
- Describing binary tomotherapy leaves with sliding-window language. Binary leaves open and close; they do not sweep a C-arm gap. (Delivery context is in the rotation lesson.)

**Sources**

- ICRU 83, IMRT reporting and the meaning of a modulated fluence
- AAPM IMRT commissioning and plan-QA guidance used in the department. Confirm measurement tolerances in the named report (TG-119 is the common IMRT commissioning report).
- Machine specifications for minimum segment width and leaf speed, because those limits decide whether the sequencer can build the beamlet map

## Treatment Delivery Systems Mini-Quiz

**MDCB objectives:** III.5, I.5

**Skills this quiz trains**

- Define step-and-shoot as beam off while leaves move, and sliding window as beam on with more monitor units and usually less dead time.
- Define helical tomotherapy: ring gantry, couch motion, binary MLC, fan beam, pitch, modulation factor, MVCT.
- Define a beamlet as an optimizer fluence element, then a sequencer product as the deliverable motion.
- Predict that integral dose and the low-dose volume rise as beams or arcs are added, even when the target DVH improves.
- Separate field-in-field and plain arcs from inverse VMAT.

**Traps**

- High MU assigned to step-and-shoot and dead time assigned to sliding window.
- Tomotherapy described as a C-arm with a conventional MLC.
- Beamlet confused with a treatment field.
- Conformity treated as a free improvement with no integral-dose cost.
- Pitch inverted (travel divided by width, not the other way around).

**Check yourself**

A plan changes from five static step-and-shoot fields to two VMAT arcs. The PTV D98 improves and the 5 Gy isodose now covers most of the axial contour. What happened to conformity of the high dose, and what happened to integral dose? Is the arc delivery beam-off between leaf positions the way step-and-shoot is?

Walk-through: High-dose conformity improved. Integral dose and the low-dose bath increased because more tissue is traversed. VMAT leaves move with the beam on during the arc. That is not step-and-shoot dead time. Monitor units depend on how hard the arcs are modulated.

## IMRT and VMAT Delivery Parameters

**Objectives:** III.5, I.5

**What the exam expects**

You can name the three optimizer families and say what each one trades. You can state why a minimum monitor-unit count is set per segment, define the IMRT factor and say where it belongs in a shielding calculation, and describe the delivery settings a VMAT planner chooses before the optimizer runs: arc length, avoidance sectors, collimator angle, and jaw tracking. You can give the usual exam direction for monitor units in VMAT versus fixed-field IMRT.

**Core facts**

Optimizers. A gradient method follows the slope of the cost function downhill from a starting fluence. It is fast and deterministic, and it stops in the first valley it finds, so it can be trapped in a local minimum when the problem is not convex. Simulated annealing is stochastic: it tries random changes and sometimes accepts a change that makes the cost worse, with a probability that falls as a control parameter called temperature is lowered. That occasional uphill step is how it climbs out of a local minimum. It is slow, and it is the classic textbook contrast to gradient descent. Direct aperture optimization (DAO) does not optimize a fluence map at all. The variables are the leaf positions and the weights of a fixed number of deliverable apertures, so there is no separate leaf-sequencing step and no gap between the optimized fluence and the delivered fluence. DAO plans typically need fewer segments and fewer monitor units for comparable quality. Most VMAT engines are aperture-based for the same reason.

Minimum monitor units per segment. A step-and-shoot segment that fires for a fraction of a monitor unit is delivered while the dose rate and the beam symmetry are still settling, and a tiny aperture is poorly modeled by the planning system. Departments therefore set a floor, commonly on the order of 3 MU per segment (the exact number is a commissioning choice, typically 2–5 MU). Raising the floor removes the smallest segments, simplifies the plan, and lowers the total MU at some cost in modulation.

IMRT factor. The IMRT factor is the monitor units needed to deliver a fraction with modulation divided by the monitor units a conventional open or wedged plan would need for the same prescribed dose. Values of 2–10 are quoted, with about 3–5 as the usual average for a C-arm linac; helical tomotherapy is higher. The patient dose at the isocenter does not change, so the primary-barrier workload does not change. Head leakage and MLC transmission scale with monitor units, so the leakage (and scatter) workload is multiplied by the IMRT factor in the NCRP 151 method. That is the single place the factor enters a shielding calculation.

VMAT and monitor units. The exam direction is that a VMAT plan uses fewer monitor units and less beam-on time than a fixed-field IMRT plan of comparable quality, especially when the comparison is with sliding-window IMRT, because the arc delivers dose from every angle with relatively open apertures instead of sweeping a narrow gap at a few angles. Heavily modulated arcs narrow that gap; the direction is typical, not guaranteed.

Jaw tracking. With jaw tracking the collimator jaws follow the MLC aperture at every control point instead of sitting at the plan's outer field edge. Closed leaves transmit about 1–2 percent and interleaf leakage is higher still; a jaw parked over the closed leaves cuts that transmission to the jaw value. The result is less dose outside the aperture, a smaller low-dose bath, and slightly less MLC-transmission dose inside the patient. It does not change the optimized fluence inside the open aperture.

Collimator angle and offset between arcs. A collimator angle of 0 degrees lines the interleaf leakage and the tongue-and-groove effect up along the direction of leaf travel for the whole arc. Planners rotate the collimator, typically 10–45 degrees, and when two arcs are used they give the arcs different or mirrored angles (for example 30 and 330 degrees) so the leakage lines of one arc do not land on the leakage lines of the other. The offset also lets the leaves cover a target longer than the leaf travel in one arc. A collimator angle near 90 degrees puts leaf motion along the short axis of the field; that is the fixed-field trick from the MLC lesson, not the same idea as the arc offset.

Avoidance sectors. An avoidance sector is a span of gantry angles inside the arc where the beam is held off while the gantry keeps rotating. It is set before optimization to keep the beam from entering through something the planner does not want as an entrance: a contralateral breast, the arms, a shoulder, the couch rails or edge, or an implanted device. A partial arc is the same idea applied to one end of the rotation. Non-coplanar arcs and couch kicks are a separate tool; avoidance sectors are about which coplanar angles are allowed to fire.

**Formulas**

IMRT factor = MU per fraction with modulation / MU per fraction for the conventional delivery of the same dose.

A conventional 4-field plan delivering 200 cGy needs 250 MU. The IMRT plan for the same prescription needs 1,000 MU. The factor is 1,000 / 250 = 4. Check: 4 × 250 = 1,000. The leakage workload used for the secondary barriers is multiplied by 4; the primary workload is not.

**Traps**

- Describing simulated annealing as the fast deterministic method, or gradient descent as the one that escapes local minima.
- Treating DAO as a leaf sequencer that runs after a fluence optimization. DAO replaces that two-step chain.
- Multiplying the primary-barrier workload by the IMRT factor. Only leakage and scatter scale with monitor units.
- Calling a 0-degree collimator the default for a two-arc plan.
- Treating an avoidance sector as a beam-off pause that stops the gantry. The gantry rotates through; the beam is held.
- Saying jaw tracking changes the fluence inside the aperture. It only trims transmission outside it.

**Sources**

- Khan and Gibbons, inverse planning chapter, for optimizer families and leaf sequencing
- NCRP 151, for the IMRT factor applied to the leakage workload
- Vendor planning-system documentation, for minimum segment MU, jaw tracking, and arc setup options

## Dynamic MLC QA, Conformal Arcs, and Compensator IMRT

**Objectives:** III.5

**What the exam expects**

You can list the classic commissioning and QA tests for a dynamic MLC and say what each one catches. You can tell a dynamic conformal arc from VMAT in one sentence. You can state which static IMRT technique is faster on the clock and why, give the beam-angle rule that keeps IMRT fields from opposing one another, list what a solid compensator buys and what it risks, and describe how an electron beam's depth dose changes when it hits the skin obliquely.

**Core facts**

Dynamic-MLC test set. Sliding-window and VMAT delivery depend on leaves being where the control point says they are, at the moment the monitor units say they should be. The classic test set checks each assumption separately. The leaf-speed test sweeps a fixed gap across the field at several programmed speeds; a leaf that runs slow or fast leaves a band of higher or lower fluence along its path. The acceleration and deceleration test asks the leaves to change speed mid-sweep and looks for over- or under-exposure at the transitions. The positional-accuracy (gap) test sweeps a narrow gap, usually 5 to 10 mm, and compares the delivered fluence with the expected value; because fluence is proportional to gap width, a 0.5 mm error on a 10 mm gap is a 5 percent dose error, and the same error on a 5 mm gap is 10 percent. The dose-rate stability test delivers the same sweep at several dose rates (for example 100, 300, and 600 MU per minute); leaf motion is tied to accumulated monitor units, not to clock time, so the fluence should not depend on the dose rate. The interrupt test holds the beam part-way through a dynamic field and resumes; the resumed field must match the uninterrupted field, which proves the leaves recover their positions and the remaining monitor units are delivered. TG-142 puts leaf position accuracy for IMRT at 1 mm, lists loss of leaf speed greater than 0.5 cm per second as the monthly action level, and asks for moving-window and segmental IMRT tests at the four cardinal gantry angles.

Dynamic conformal arc versus VMAT. In a dynamic conformal arc (DCA) the MLC reshapes continuously so the aperture matches the beam's-eye-view outline of the target at every gantry angle, while dose rate and gantry speed stay constant. There is no fluence modulation inside the aperture and no inverse optimization; it is a conformal 3D arc with moving leaves. VMAT adds variable dose rate, variable gantry speed, and inverse-planned apertures that do not need to match the target outline. A stem that says the leaves follow the target shape with a constant dose rate is describing DCA.

Sliding window versus step-and-shoot on the clock. Step-and-shoot turns the beam off between segments and waits for the leaves to settle; a field with many segments accumulates a lot of dead time. Sliding window keeps the beam on while the leaves sweep, so there is no inter-segment pause. The usual expectation is that sliding window uses more monitor units but less wall-clock time per field than a heavily segmented step-and-shoot delivery of the same fluence. Both are far slower than a VMAT arc of comparable quality.

Beam separation. IMRT plans typically use 5 to 9 fields. The planning rule is to avoid parallel-opposed pairs: keep each beam's entry path at least about 10 to 15 degrees away from the exit path of any other beam. Opposed beams traverse the same ray, so their fluences along that ray are nearly interchangeable; the pair adds little new freedom to the optimizer while stacking entrance and exit dose on one line. Odd numbers of equispaced beams (5, 7, 9) satisfy the rule automatically.

Compensator IMRT. A modulated field can be delivered with a milled solid compensator (brass, or a tin-filled or steel-filled resin) in place of leaf motion. The compensator has spatial resolution limited only by the milling bit, not by the leaf width, so the fluence is finer than an MLC can produce. Because the beam is open across the whole field at once, the monitor units are lower than a sliding-window delivery and the leakage through closed leaves does not exist. The costs are fabrication time, beam hardening in the thick parts, one physical device per field, and the human error of mounting the wrong compensator or the right one in the wrong orientation; the verification step for a compensator field is to check the device identifier and orientation against the plan, exactly as a block is checked.

Electron obliquity. When an electron beam strikes the skin at an angle rather than along the normal, the depth-dose curve measured perpendicular to the skin changes in three ways. The depth of maximum moves toward the surface, the surface dose rises, and the low-value isodose lines bulge outward and deeper at the edges because of side scatter from the thick side of the slope. The practical range measured along the beam is unchanged. An unfilled air gap on a curved or sloping surface is the everyday cause; bolus that levels the surface removes the obliquity.

**Formulas**

Fractional fluence error in a sliding-gap test ≈ (gap error) / (nominal gap). For a 10 mm gap with a 0.5 mm error, 0.5 / 10 = 0.05, or 5 percent. Check: a 10.5 mm gap exposes each point 5 percent longer than a 10 mm gap.

**Traps**

- Calling the interrupt test a check of output constancy. It checks that leaves and monitor units resume correctly.
- Describing DCA as modulated because the leaves move. The aperture follows the outline; nothing inside it is modulated.
- Reversing the clock-time statement. Sliding window spends more MU and less time; step-and-shoot pays dead time between segments.
- Using parallel-opposed IMRT beams. The rule is a 10 to 15 degree separation from any other beam's exit.
- Saying compensator IMRT has coarser resolution than an MLC. The milling bit is finer than the leaf.
- Moving electron dmax deeper under oblique incidence. It moves shallower, and the surface dose rises.

**Sources**

- AAPM TG-142, table of monthly and annual MLC tests for IMRT machines; LoSasso, Chui, and Ling for the sliding-gap and leaf-speed tests
- Khan and Gibbons, IMRT delivery chapter, for compensator-based IMRT and leaf sequencing
- Khan and Gibbons, electron beam chapter, for oblique incidence
