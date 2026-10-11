# Module 23 — Treatment delivery systems

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Rotation Therapy and VMAT

### Q1
Stem: A prostate plan is delivered as a volumetric modulated arc on a C-arm linac. During the arc the gantry rotates, the multileaf collimator leaves move, and the dose rate changes. Which description matches this delivery?
A. The gantry is fixed at eight static angles and the beam is held while the leaves step to the next shape
B. The beam is on while the gantry travels and the leaves and dose rate are modulated together
C. A binary collimator and a couch that moves continuously through a fan beam
D. An unmodulated 360 degree arc with fixed leaves and a constant dose rate only
Answer: B
Objective: III.5
Why: Answer B. Volumetric modulated arc therapy ties three motions together: gantry angle, multileaf shape, and dose rate (and sometimes gantry speed). The beam stays on while those parameters change, within the machine's speed and dose-rate limits. A is step-and-shoot intensity-modulated delivery at fixed gantry angles. C is helical tomotherapy. D is a classic conformal arc with no intensity modulation; a VMAT plan that needs modulation will slow the gantry or vary the dose rate rather than stay on that simple path.

### Q2
Stem: Helical tomotherapy delivers a 6 MV fan beam while the couch moves through the bore. Which hardware statement is correct?
A. The multileaf collimator is binary: a leaf is open or closed, not parked at an intermediate position, and the unit does not have an electron mode
B. The leaves form a conventional rounded-end multileaf aperture that holds partial leaf positions, and an electron cone can be mounted
C. The couch is locked and the gantry jumps between static IMRt fields
D. A flattening filter spreads the fan beam into a 40 by 40 cm flat field at isocenter
Answer: A
Objective: III.5
Why: Answer A. A helical unit uses a narrow fan defined by a jaw (commonly field widths on the order of 1, 2.5, or 5 cm) and a binary multileaf collimator whose leaves snap between open and closed. The gantry rotates continuously and the couch translates, so the beam paints a helix. There is no electron scattering foil or electron applicator on that machine. B describes a conventional C-arm multileaf and an electron mode the helical unit does not have. C is static gantry intensity modulation. D is the opposite of a fan-beam collimator; helical units are unflattened fan beams.

### Q3
Stem: For a similar prostate target, why does a helical delivery often give a larger low-dose bath in the normal tissue than a pair of opposed conformal fields?
A. The helix stops the beam at the distal edge of the target the way a proton Bragg peak does
B. The rotating fan beam enters from all angles, so a large volume of normal tissue receives some dose even when the high dose is conformal
C. Binary leaves transmit nothing, so the integral dose is lower than an unmodulated anterior-posterior pair
D. The couch motion removes scatter, so tissue outside the field width receives zero dose
Answer: B
Objective: III.5
Why: Answer B. Integral dose is, roughly, mean dose times mass. A conformal parallel-opposed pair dumps dose in the entrance and exit slabs and relatively little outside those slabs. A helical fan approaches the target from a full rotation, so many more kilograms of tissue receive a low dose. That trade can be acceptable when a concave high dose must bend around a critical structure, and it is a real cost for a simple target where opposed fields would have spared the lateral tissues. A describes protons, not megavoltage photons. C is backwards: modulation and rotation tend to raise the low-dose integral, and binary leaves still have some transmission. D is wrong because scatter, leakage, and the helical entrance paths all leave dose outside a single fan width.

### Q4
Stem: A tomotherapy pitch that is too coarse for the fan width produces a thread artifact. What does the planner see, and what is pitch?
A. Pitch is the couch travel per rotation relative to the field width; too high a pitch leaves a ripple in dose along the superior-inferior direction
B. Pitch is the gantry angle between static step-and-shoot beams; the artifact is a lateral horn from the flattening filter
C. Pitch is the electron energy; the artifact is a Bragg peak
D. Pitch is the multileaf transmission; the artifact is a hot spot only at dmax on the central axis
Answer: A
Objective: III.5
Why: Answer A. In helical delivery, pitch is how far the couch advances during one gantry rotation, divided by the fan width. If the couch advances too far for that fan, adjacent helices do not blend and the dose along the patient long axis ripples. That is the thread effect. It is not a flattening-filter horn, a proton peak, or ordinary leaf transmission. Closing the pitch (slower couch relative to the fan) and using an appropriate field width reduces it, at the cost of treatment time.

### Q5
Stem: A C-arm volumetric modulated arc and a seven-field sliding-window intensity-modulated plan cover the same prostate PTV to the same prescription. Which comparison of delivery is the usual one?
A. The arc usually takes longer and uses more monitor units, because the gantry must stop at each beamlet
B. The arc is usually faster, and its monitor units are often lower than a highly modulated fixed-gantry sliding-window plan, because the beam stays on while the gantry moves
C. Both deliveries use a binary multileaf and a moving couch, so time and monitor units are identical
D. The arc cannot modulate the dose rate, so it cannot produce a concave dose distribution
Answer: B
Objective: III.5
Why: Answer B. Fixed-gantry sliding-window delivery pays a monitor-unit cost because the beam is on while leaves travel across each field, and the therapist waits for mode-up and gantry motion between fields. A volumetric modulated arc keeps the beam on through a long gantry travel and typically finishes a prostate in a few minutes with fewer monitor units than that sliding-window arrangement. The arc is still more monitor units than an unmodulated three-dimensional plan. C describes helical tomotherapy, not a C-arm arc. D is wrong: dose-rate and gantry-speed changes are part of how the arc modulates. If the requested modulation exceeds leaf speed or gantry speed, the plan is undeliverable until the objectives are relaxed.

## Static IMRT

### Q1
Stem: In step-and-shoot (segmental) intensity-modulated delivery, when is the beam on?
A. Only while the leaves are parked at a static shape; the beam is held off while the leaves move to the next segment
B. The entire time the leaves are in motion, with no static segments
C. Only during gantry rotation between fixed fields
D. Continuously, while the couch translates through a fan beam
Answer: A
Objective: III.5
Why: Answer A. Step-and-shoot splits the fluence into a stack of static apertures called segments. Dose is delivered with the leaves still, then radiation stops, the leaves move, and the next segment is delivered. Sliding window does the opposite: radiation stays on during leaf motion. C confuses this with gantry motion between fields. D is helical delivery.

### Q2
Stem: Compared with step-and-shoot for a similar fluence, why does sliding-window delivery usually require more monitor units?
A. The leaves cannot move, so each beamlet is delivered by a separate couch kick
B. The beam remains on while leaves travel, including while they are covering part of the field, so more monitor units are used to deliver the same fluence pattern
C. Sliding window uses a physical compensator, and the compensator transmission is counted as extra monitor units
D. Step-and-shoot delivers the same modulation with the jaws closed, which always uses more monitor units than an open window
Answer: B
Objective: III.5
Why: Answer B. In a sliding window the leaves sweep while radiation is on. Much of that beam time is spent with a given point covered by a leaf, so the monitor units needed to leave behind a modulated fluence are higher than a segmented delivery that turns the beam off during motion. The extra monitor units increase leaf transmission and head leakage. A is not sliding window. C describes a physical compensator, which is a different device. D has the monitor-unit comparison backwards and does not describe how segments work.

### Q3
Stem: In inverse planning, the optimizer assigns a fluence weight to each beamlet. What is a beamlet?
A. A deliverable static multileaf segment with a minimum monitor-unit setting
B. A small element of a beam, a bixel, into which the field is divided so the optimizer can raise or lower intensity locally
C. The mechanical isocenter used for a Winston-Lutz test
D. One control point in a volumetric modulated arc, which already includes gantry angle and every leaf position
Answer: B
Objective: III.5
Why: Answer B. A beamlet (bixel) is a subdivision of a beam's cross-section used during optimization. The cost function rewards or penalizes the dose that results from each beamlet weight, producing an ideal fluence map. Leaf sequencing then turns that map into something the machine can deliver: either step-and-shoot segments or a sliding-window trajectory, which are described by control points. A beamlet is not itself a segment, not the isocenter, and not a full arc control point. The sequencer is also where tongue-and-groove and minimum-segment-width limits appear; the ideal beamlet map does not automatically obey them.

### Q4
Stem: A static intensity-modulated plan uses nine fixed gantry angles. The leaves move only while the beam is off. The total monitor units are 980 for a 200 cGy fraction. An unmodulated four-field box for the same fraction would use about 280 monitor units. What is the practical consequence of the higher monitor units?
A. More radiation time is spent with leaves blocking the field, so collimator transmission and head leakage contribute more dose outside the target
B. The higher monitor units prove the tumor receives a higher prescription
C. Leakage decreases as monitor units increase, because the leaves are thicker at high monitor units
D. The four-field box is more modulated because it uses fewer monitor units
Answer: A
Objective: III.5
Why: Answer A. Modulation throws away photons. To leave a non-uniform fluence, the leaves cover parts of the field for much of the beam-on time, so the machine must run more monitor units for the same target dose. Leakage through the leaves (on the order of 1 to 2 percent) and scatter from the head are multiplied by those extra monitor units, which raises the low-dose bath. The prescription is still 200 cGy; monitor units are not the prescribed dose (B). Leakage fraction does not fall just because the monitor-unit count rose (C). Fewer monitor units in the box plan means less modulation, not more (D).

### Q5
Stem: A sliding-window sequence shows a dark streak where neighboring leaves meet, running the length of leaf travel. The dose under that streak is low. What is the usual cause?
A. The tongue-and-groove underdose, from the overlapping tongue-and-groove design that reduces interleaf leakage but can leave a cold line if adjacent leaves do not expose that junction long enough
B. A proton distal falloff
C. The flattening filter having been left in for a flattening-filter-free beam
D. Geometric penumbra from an extended source-to-skin distance on an electron cone
Answer: A
Objective: III.5
Why: Answer A. Multileaf leaves are stepped so that a tongue on one leaf fits a groove on the next. That overlap cuts interleaf leakage, but the overlap region is thicker until both leaves have moved clear. If the sequencer does not keep the junction irradiated long enough, a cold stripe appears along the direction of travel. Sliding-window sequences are designed to synchronize neighboring leaves so this tongue-and-groove effect is minimized. B, C, and D are unrelated machines and beam types.

## Treatment Delivery Systems Mini-Quiz

### Q1
Stem: Place these deliveries in the order that usually has the lowest monitor units for the same prostate prescription and then the highest: unmodulated 3D conformal beams, step-and-shoot, sliding window.
A. Sliding window, then step-and-shoot, then 3D conformal
B. 3D conformal lowest, step-and-shoot in the middle, sliding window highest
C. Step-and-shoot lowest, sliding window in the middle, 3D conformal highest
D. All three use the same monitor units if the prescription dose is the same
Answer: B
Objective: III.5
Why: Answer B. An unmodulated conformal plan delivers nearly open apertures, so almost every monitor unit contributes to the target and the monitor-unit count stays near the prescription divided by the output. Step-and-shoot blocks parts of the field but turns the beam off while the leaves move, so the monitor units rise. Sliding window keeps the beam on during travel, so the monitor units rise further for a comparable fluence. Equality of prescription dose does not imply equality of monitor units, because monitor units count photons leaving the head, including those stopped by leaves.

### Q2
Stem: A small stereotactic field is planned with a 6 MV flattening-filter-free beam. Which change relative to a flattened 6 MV beam is expected?
A. Dose rate is much higher and the open profile is peaked in the center rather than flat
B. Dose rate falls, and the profile becomes flatter than a filtered beam out to 40 cm
C. The beam becomes an electron beam because the filter was the only source of photons
D. Neutron production increases sharply because the filter was what had been absorbing neutrons at 6 MV
Answer: A
Objective: I.5
Why: Answer A. The flattening filter absorbs a large fraction of the central photons to build up the edges of a large field. Removing it leaves the forward-peaked bremsstrahlung spectrum, so the dose rate can rise into the range of roughly 1400 monitor units per minute and higher, and the profile is peaked. That peak is acceptable for a small stereotactic aperture sitting on the central axis. It is a poor match to a large flat field. The beam is still photons. At 6 MV, photoneutron production is already negligible; taking the filter out does not create a neutron problem. Neutron production becomes relevant above about 10 MV.

### Q3
Stem: Which delivery system uses many non-isocentric beams from a robot-mounted 6 MV linac, with the beam aimed from a set of nodes rather than from a single isocenter?
A. A cobalt-60 Gamma Knife with a helmet of circular collimators
B. A robotic radiosurgery linac (CyberKnife-type) that can place beams from many directions without a fixed isocenter
C. A helical fan-beam unit with binary leaves and a moving couch
D. A conventional C-arm linac restricted to coplanar step-and-shoot fields around one isocenter
Answer: B
Objective: I.5
Why: Answer B. A robotic radiosurgery unit mounts a compact linac on a robot arm. Each beam comes from a node in space and is not required to share one isocenter, which is useful for irregular targets and for tracking. A Gamma Knife is a cobalt-60 device: many sources focus on an isocenter (a shot), and larger targets are built from several shots. C is helical tomotherapy. D is standard isocentric C-arm delivery.

### Q4
Stem: A Gamma Knife plan treats an intracranial target with cobalt-60 sources focused through a collimator helmet. The sources are one half-life old. What happens to the treatment time for the same shot dose, and what is a shot?
A. Treatment time is unchanged because cobalt-60 does not decay; a shot is one electron cutout
B. Treatment time approximately doubles because the dose rate has fallen by half; a shot is one isocenter delivered with a chosen collimator
C. Treatment time is cut in half because decay increases the dose rate; a shot is a helical pitch
D. Treatment time doubles, and a shot is the patient-specific intensity-modulated sliding window
Answer: B
Objective: I.5
Why: Answer B. Cobalt-60 decays with a half-life of about 5.26 years. After one half-life the activity, and therefore the dose rate, is half, so the time required to deliver the same dose is about twice as long. A shot is one isocentric exposure through a collimator size (4 mm, 8 mm, or similar, depending on the unit). Multiple shots are packed to shape a larger target. The device does not deliver electrons, helical pitch, or multileaf sliding windows.

### Q5
Stem: An inverse-planned fluence map is handed to a leaf sequencer. The sequencer reports that the map cannot be delivered unless the minimum leaf gap is widened. What is the sequencer doing, and what should the planner not assume?
A. The sequencer converts ideal beamlet weights into machine motions; an ideal fluence is not automatically deliverable
B. The sequencer recalculates tumor α/β and can ignore mechanical limits if the cost function was low
C. The sequencer replaces the need for patient-specific measurement of a highly modulated field
D. Widening the leaf gap does not change the delivered fluence, so the dose distribution is identical to the ideal map
Answer: A
Objective: III.5
Why: Answer A. Optimization often works on beamlets that are freer than the real multileaf collimator. The sequencer has to respect leaf speed, interdigitation rules, tongue-and-groove, minimum gap, and minimum monitor units per segment. If the only way to sequence the map is to open a gap the optimizer did not intend, the delivered fluence changes and the dose must be recomputed with the real apertures. A low cost function on the ideal map does not override hardware (B). Highly modulated fields still need a patient-specific delivery check because the delivered aperture, not the beamlet map, is what the patient receives (C). D is wrong because forcing a wider gap fills in fluence the map had set near zero.
