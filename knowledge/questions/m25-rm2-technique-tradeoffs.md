# Module 25. Planning Methodologies

Original items. VMAT versus fixed-field IMRT, the medial physical wedge and the contralateral breast, what adding beams changes, the partially delivered IMRT fraction, and vertex-field checks.

## Technique Trade-offs and Delivery Contingencies

### Q1
Stem: A prostate plan is produced as two VMAT arcs and as seven step-and-shoot IMRT fields with the same objectives. Which set of differences is the usual expectation for the VMAT plan?
A. Less conformal, more monitor units, and more homogeneous inside the target
B. Identical in every metric because the objectives are the same
C. More conformal, fewer monitor units, but typically slightly less homogeneous inside the target and a larger low-dose bath
D. More homogeneous inside the target and a smaller low-dose volume
Answer: C
Objective: III.7
Why: The arc hugs the target from every angle, which tightens the prescription isodose and needs fewer monitor units, but the hot spot inside the target is usually a little higher and the dose is spread around the whole circumference so more tissue receives a few gray. Fewer, not more, monitor units is the VMAT direction. Different delivery mechanics give different metrics even with identical objectives. Better homogeneity with a smaller low-dose volume reverses both usual directions.

### Q2
Stem: A VMAT plan's 5 Gy isodose covers much more of the body contour than the seven-field IMRT plan it replaced. Why?
A. The arc enters from every angle, so low dose is spread around the full circumference rather than concentrated along seven entrance paths
B. VMAT uses more monitor units, so leakage dominates the low-dose region
C. The VMAT dose grid is coarser and smears the isodose
D. VMAT cannot use jaw tracking
Answer: A
Objective: III.7
Why: The low-dose bath follows the entrance paths; 360 degrees of entrance paint a thin ring of dose around the whole patient. VMAT typically uses fewer monitor units than fixed-field IMRT, so leakage is not the driver. Grid size is a calculation setting that does not create dose. Jaw tracking is available for VMAT and reduces the leakage share, which is not the main cause here.

### Q3
Stem: Tangential breast fields are planned with 30 degree physical wedges on both the medial and lateral fields. The physicist flags the medial wedge. Why?
A. Physical wedges cannot be used with a rotated collimator on tangents
B. The medial wedge hardens the beam, which raises the ipsilateral lung dose
C. A medial field is not permitted to carry a wedge factor
D. Photons scattered from the physical wedge in the medial field increase the dose to the contralateral breast; a dynamic wedge or field-in-field is preferred medially
Answer: D
Objective: III.7
Why: Metal in the medial beam scatters toward the midline and onto the opposite breast, and the steeper the wedge the more it scatters; a dynamic wedge has no metal and scatters far less, and field-in-field removes the wedge altogether, so if a physical wedge is unavoidable it goes on the lateral field. Physical wedges work at any collimator angle. Beam hardening slightly reduces, not raises, lung dose and is not the concern. Wedge factors apply to whichever field carries the wedge.

### Q4
Stem: A planner replaces the wedges on a pair of breast tangents with forward-planned field-in-field subfields. Besides the hot-spot control the subfields provide, which two changes follow?
A. Higher monitor units and higher contralateral breast dose
B. Lower contralateral breast dose from wedge scatter and fewer monitor units because no wedge factor is in the calculation
C. A larger low-dose bath and a longer treatment time
D. Loss of skin sparing and a deeper dmax
Answer: B
Objective: III.7
Why: Removing the metal removes the wedge scatter that reaches the contralateral breast, and removing the wedge factor from the denominator of the monitor-unit calculation lowers the monitor units. Monitor units fall, not rise. Field-in-field uses the same two tangent directions, so the low-dose bath does not grow and the extra subfields add seconds, not minutes. Skin sparing and dmax depend on energy and bolus, not on the wedge.

### Q5
Stem: A conformal plan is changed from four to nine equally spaced coplanar fields with the same prescription normalization. Which combination of effects is expected?
A. Better conformity of the prescription isodose, a higher maximum inside the target, and the penumbra and entrance dose of each beam spread over more of the surrounding tissue
B. Worse conformity and a lower maximum inside the target
C. No change in conformity, only a change in monitor units
D. A lower integral dose because each beam is weaker
Answer: A
Objective: III.7
Why: More directions let the prescription isodose follow the target more closely, and that tighter sculpting usually raises the internal maximum; at the same time each beam's penumbra and entrance dose land in new tissue, so the low-dose volume grows. Conformity improves rather than worsens. The dose distribution, not only the monitor units, changes. Integral dose does not fall when the same target dose is delivered through more paths; the per-beam entrance dose falls but the total deposited energy does not.

### Q6
Stem: A nine-field IMRT fraction prescribes 200 cGy at the isocenter. The record-and-verify log shows fields 1 through 5 completed before a machine fault stopped treatment. The planned isocenter contributions in treatment order are 30, 25, 20, 25, 20, 20, 25, 20, and 15 cGy. About how much isocenter dose was delivered?
A. 111 cGy
B. 200 cGy
C. 120 cGy
D. 80 cGy
Answer: C
Objective: III.7
Why: Add the completed fields: 30 + 25 + 20 + 25 + 20 = 120 cGy. Check: the remaining four fields sum to 20 + 25 + 20 + 15 = 80 cGy and 120 + 80 = 200 cGy. The 111 cGy figure is 5/9 of 200 and assumes equal field weights, which the stem contradicts. Eighty cGy is the undelivered remainder. Two hundred cGy ignores the fault. The isocenter number is only the first estimate; physics still reconstructs the partial plan to see what the rest of the PTV and the organs received.

### Q7
Stem: The fault in the previous scenario is cleared the same afternoon. What is the appropriate handling of the interrupted fraction?
A. Repeat the entire fraction, because an incomplete IMRT fraction cannot be credited
B. Count the fraction as complete, because more than half the fields were delivered
C. Deliver the whole fraction again tomorrow and disregard today's fields
D. Physics documents the delivered fields and estimates the delivered dose, and the remaining fields or a make-up are delivered as the physician directs; nothing is repeated without that estimate
Answer: D
Objective: III.7
Why: The record-and-verify log identifies exactly which fields were given, so the delivered dose is reconstructed and the physician decides whether to finish the remaining fields that day, finish them later, or design a make-up. Repeating the whole fraction would deliver fields 1 to 5 twice. Crediting the fraction as complete leaves 80 cGy at the isocenter undelivered and the PTV coverage unknown. Ignoring the delivered fields and repeating tomorrow is the same double dose one day later.

### Q8
Stem: A therapist proposes crediting an interrupted sliding-window IMRT fraction as 60 percent delivered because 60 percent of the total monitor units had been given. What is the objection?
A. Monitor units are not recorded during IMRT delivery
B. Individual IMRT fields contribute very unevenly to different parts of the target and the organs, so the fraction of monitor units is not the fraction of dose at any particular point; the delivered fields must be recalculated as a partial plan
C. Sliding window deposits its dose only at the end of each field
D. The monitor-unit count includes leakage, so it overstates the delivered dose
Answer: B
Objective: III.7
Why: A modulated field may deliver most of its dose to one part of the PTV and almost none to another, so 60 percent of the MU can be 90 percent of the dose in one region and 20 percent in another; only a recalculation of the completed fields tells the physician what was delivered. Monitor units are logged field by field in the record-and-verify system. Sliding window deposits dose continuously as the gap sweeps. Leakage is a small addition, not the reason the MU fraction fails.

### Q9
Stem: A brain plan adds a vertex field that enters through the top of the skull with the couch rotated 90 degrees. Which checks are specific to this field before it is approved?
A. Verify gantry clearance from the couch and the patient's shoulders in the actual treatment position, including the table height, and confirm that the beam's exit path through the neck and trunk lies inside the CT dataset and the exit dose is acceptable
B. Confirm the wedge factor is below 0.6
C. Confirm the field is exactly parallel-opposed to the posterior field
D. Verify the field is coplanar with the lateral fields
Answer: A
Objective: III.7
Why: With the couch kicked the gantry head passes close to the couch end and the shoulders, so the setup is dry-run and the table height recorded, and because the beam exits inferiorly through the body the CT must include that path or the field is calculated through air. A wedge is not part of the vertex geometry. A vertex field has no opposed partner inside the skull; its opposite would enter through the trunk. The field is non-coplanar by design, which is the point of using it.
