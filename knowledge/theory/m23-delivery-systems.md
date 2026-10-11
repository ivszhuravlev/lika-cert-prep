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
