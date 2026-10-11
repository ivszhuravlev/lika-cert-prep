# Module 25 — Planning methodologies

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Beam Energy

### Q1
Stem: A left whole-breast tangent plan can be calculated with 6 MV or with 18 MV. The breast separation is 20 cm and the skin and tumor bed are part of the target. Why is 6 MV the usual choice?
A. 18 MV deposits more dose in the buildup region and at the chest-wall–lung interface than 6 MV
B. 18 MV increases skin sparing and lateral disequilibrium in lung, so the superficial breast and the tissue next to lung can be underdosed relative to 6 MV
C. 6 MV cannot cover a 20 cm separation at any wedge angle
D. 18 MV is required whenever the prescription is below 2 Gy per fraction
Answer: B
Objective: III.7
Why: Answer B. Higher photon energy pushes dmax deeper and reduces surface dose. In a breast tangent the target includes tissue near the skin and a thin chest wall next to low-density lung, where high-energy electrons travel farther laterally and the dose at the interface falls. Eighteen MV also produces neutrons, which matters if a cardiac device is nearby. A modest separation of about 20 cm is well within 6 MV, often with field-in-field segments rather than a higher energy. Very large separations are the situation where a higher energy, or more fields, is reconsidered, not a standard breast.

### Q2
Stem: A pelvic plan has a mid-separation of 28 cm. Opposed 6 MV fields produce hot spots in the subcutaneous tissue and poor dose at the midline relative to the hot spots. Which energy change addresses that geometry?
A. Drop to a superficial kilovoltage beam so dmax moves to the midline
B. Raise the photon energy into the 10 to 18 MV range so the percent depth dose at midline improves and the entrance hot spots fall
C. Switch to 6 MeV electrons, whose practical range is about 3 cm, to treat the midline
D. Keep 6 MV and add a 1 cm bolus over the whole pelvis to move dmax to the skin
Answer: B
Objective: III.7
Why: Answer B. For a large separation the 6 MV percent depth dose at 14 cm depth is low, so the entrance regions must be driven high to make the midline reach the prescription. A 10 or 18 MV beam has a higher percent depth dose at depth and a lower entrance dose for the same midline dose. The cost is neutron production above 10 MV and a deeper buildup, which is acceptable for a deep pelvic target and not acceptable as a default for a superficial one. Electrons of 6 MeV stop near 3 cm. Bolus would make the subcutaneous hot spot worse. Kilovoltage beams do not treat a midline pelvic target.

### Q3
Stem: A patient with a pacemaker needs a pelvis plan, and the separation would ordinarily tempt the planner to use 18 MV. Which energy decision respects both the separation and the device?
A. Use 18 MV and rely on the device being outside the field
B. Use 6 MV or at most 10 MV, and add fields or accept a different hot-spot compromise rather than introduce photoneutrons
C. Use 18 MeV electrons for the midline pelvic nodes
D. Use cobalt-60 because its energy is above the neutron threshold and below 6 MV
Answer: B
Objective: III.7
Why: Answer B. Photoneutrons appear in high-Z linac components once the photon energy is above about 10 MV. TG-203 therefore keeps cardiac implantable devices on beams of 10 MV or below even when the generator is outside the aperture. If 6 MV through a large separation is too hot laterally, the planner adds fields, changes beam angles, or uses a modulated plan at allowed energies. Electrons will not reach a pelvic midline. Cobalt-60 is about 1.25 MV and does not solve a 28 cm separation by being "above the neutron threshold"; it is below that threshold.

### Q4
Stem: An electron energy is being chosen for a posterior cervical boost. The deepest target point that must sit on the 90% isodose is at 3.0 cm of water-equivalent depth. Using Khan's approximation that the 90% depth in centimeters is E/4, what energy is required?
A. 6 MeV, because 6/4 = 1.5 cm
B. 9 MeV, because 9/4 = 2.25 cm
C. 12 MeV, because 12/4 = 3.0 cm
D. 15 MeV, because the 90% depth is E/2 = 7.5 cm and 15 MeV is the next energy above 3 cm
Answer: C
Objective: III.7
Why: Answer C. Khan's planning rule puts the 90% isodose at about E/4 centimeters. Setting E/4 = 3.0 gives E = 12 MeV. Check: 12/4 = 3.0 cm, which lands on the distal target. Six MeV reaches 90% at about 1.5 cm and 9 MeV at about 2.25 cm, both short of 3 cm. The E/2 rule is the practical range, not the 90% depth; using it as if it were the therapeutic isodose would pick an energy that is hot and too penetrating. Bentel's 90% approximation (about E/3.2) would give 3.2 × 3.0 = 9.6 MeV, so a 10 MeV beam would look adequate under Bentel and inadequate under Khan. The stem asked for Khan.

### Q5
Stem: A chest-wall electron field of 9 MeV is aimed at a thin chest wall that is 1.5 cm of soft tissue, then lung. The planning CT assigns the lung a relative density of 0.25. Using a practical range of E/2 and the 2 MeV/cm rule only as a check, about how far into the lung can the electrons still travel?
A. They stop at the pleura because lung density is too low to support a dose
B. Remaining range after 1.5 cm of tissue is about 4.5 − 1.5 = 3.0 cm of water, which is about 3.0/0.25 = 12 cm of this lung
C. Remaining range is 9/2 = 4.5 cm of lung, because density is ignored for electrons
D. Remaining range is 2 MeV per cm times 0.25, or 0.5 cm of lung
Answer: B
Objective: III.7
Why: Answer B. The practical range of a 9 MeV beam is about 9/2 = 4.5 cm of water. The chest wall uses 1.5 cm of that water-equivalent range, leaving about 3.0 cm of water-equivalent range. In lung at relative density 0.25, physical distance is water-equivalent distance divided by density: 3.0/0.25 = 12 cm. Electrons can therefore stream far past the chest wall and reach heart or lung that a water phantom calculation would have called safe. This is why electron energy for a chest wall is chosen from the CT, not from a ruler on the skin. The 2 MeV/cm rule gives the same caution in energy units: 1.5 cm of tissue removes about 3 MeV, leaving about 6 MeV, which is still a multi-centimeter range in water and a much longer range in lung.

## Normalization

### Q1
Stem: A plan is normalized so that 100% is the dose at isocenter. The physician prescribes 180 cGy per fraction to the 95% isodose. What dose does isocenter receive per fraction?
A. 180 cGy
B. 180 × 0.95 = 171 cGy
C. 180 / 0.95 = 189.5 cGy
D. 180 / 0.05 = 3600 cGy
Answer: C
Objective: III.7
Why: Answer C. If the 95% isodose is defined as 180 cGy, then 1% of the isocenter dose is 180/95 cGy, and 100% is 180/0.95. Compute 180 ÷ 0.95: 0.95 × 189 = 179.55, and 180 − 179.55 = 0.45, so 0.45/0.95 ≈ 0.47. Isocenter receives about 189.5 cGy. Choosing A treats the isocenter as the prescription point, which is a different normalization. Choosing B assigns 180 cGy to isocenter and then gives the 95% line only 171 cGy, which underdoses the line the physician named. Dividing by 0.05 has no meaning in this normalization.

### Q2
Stem: The same plan has a hotspot of 108% of the isocenter dose. With 180 cGy prescribed to the 95% line, what is the hotspot dose, and what is it as a percent of the prescribed 180 cGy?
A. 1.08 × 189.5 ≈ 204.6 cGy, which is 204.6/180 ≈ 114% of the prescription
B. 108% of 180 cGy = 194.4 cGy, because percents are always taken against the prescription
C. 108% − 95% = 13 cGy
D. 0.95 × 108 = 102.6 cGy
Answer: A
Objective: III.7
Why: Answer A. From the previous normalization, isocenter is 180/0.95 ≈ 189.5 cGy. A point at 108% of isocenter receives 1.08 × 189.5. First, 1.08 × 190 = 205.2, and 1.08 × 0.5 = 0.54, so 1.08 × 189.5 = 204.66 cGy, about 204.7 cGy. Relative to the prescription, 204.7/180 = 1.137, or about 114% of 180 cGy. The arithmetic identity is 108/95 = 1.137. B would be correct only if 100% had been defined as the prescription rather than as isocenter. Subtracting percentages and multiplying 0.95 by 108 do not produce a dose.

### Q3
Stem: A three-dimensional plan reports the ICRU reference point at isocenter as 100% of the prescription, the PTV minimum as 93%, and a point outside the PTV as 110%. ICRU 50/62 guidance for this style of plan was to keep the PTV between 95% and 107% of the prescription. Which finding is outside that window?
A. The reference point at 100%
B. Both the 93% PTV minimum and the 110% point are outside the 95% to 107% window
C. Only a point inside the PTV can violate the window, so 110% outside the PTV is compliant by definition
D. 93% is acceptable because the window is 90% to 110%
Answer: B
Objective: III.11
Why: Answer B. For three-dimensional conformal planning, ICRU 50 and 62 asked that the dose to the PTV lie between 95% and 107% of the prescribed dose, with the prescription reported at the ICRU reference point. A PTV minimum of 93% is a cold spot inside the target, below 95%. A point at 110% exceeds 107%. Whether that 110% point is also a clinically significant hot spot depends on its location and size: ICRU 50 called a hot spot a volume outside the PTV receiving more than 100% of the specified dose, and treated it as significant when its minimum diameter reached about 15 mm. The reference point at 100% is the definition of the prescription in this normalization, not a violation. The window is not 90% to 110%.

### Q4
Stem: An intensity-modulated plan is prescribed to cover 95% of the PTV with the prescription dose. The reporting follows ICRU 83. Which dose-volume values replace a single ICRU reference-point dose as the description of the PTV?
A. Only the mean dose, because ICRU 83 forbids D98 and D2
B. The near-minimum D98%, the median D50%, and the near-maximum D2%
C. The dose at isocenter only, which ICRU 83 requires to be exactly 107%
D. V20 of the lung, which ICRU 83 defines as the PTV prescription
Answer: B
Objective: III.11
Why: Answer B. ICRU 83 was written for modulated plans, where a single point can sit in a steep gradient and misrepresent the target. The report asks for the dose that covers 98% of the PTV (near-minimum), the median dose D50%, and the dose that covers the hottest 2% (near-maximum). Homogeneity can then be written (D2% − D98%)/D50%. The mean dose is optional additional information, not a ban on D98 and D2. Isocenter is not required to be 107%. Lung V20 is an organ-at-risk metric, not the PTV prescription.

### Q5
Stem: A planner renormalizes a plan so that the old 95% isodose becomes the new 100%. A point that was 105% before renormalization becomes what percent?
A. 105%, because renormalizing changes the prescription text but not the isodose labels
B. 105/95 ≈ 110.5%
C. 105 × 0.95 ≈ 99.8%
D. 95/105 ≈ 90.5%
Answer: B
Objective: III.7
Why: Answer B. Renormalization multiplies every relative dose by the same factor. To make the old 95% line read 100%, the factor is 100/95. A point at 105% becomes 105 × (100/95) = 105/0.95. Compute 105/0.95: 0.95 × 110 = 104.5, remainder 0.5, and 0.5/0.95 ≈ 0.53, so 110.5%. The absolute doses in gray scale with the same factor if the prescription cGy stays attached to the new 100%. The point does not stay at 105%, and it does not drop to 99.8% or 90.5%.

## Beam Weighting

### Q1
Stem: Two opposed lateral fields deliver 180 cGy to isocenter per fraction, with equal beam weights defined as equal dose contribution at isocenter. The right lateral delivers 0.45 cGy per monitor unit at isocenter. The left lateral delivers 0.60 cGy per monitor unit at isocenter. How many monitor units does each side need?
A. Right 200, left 150
B. Right 150, left 200
C. Right 400, left 300, because each side must deliver the full 180 cGy
D. Right 81, left 108, because monitor units equal dose times cGy per monitor unit
Answer: A
Objective: III.7
Why: Answer A. Equal weight at isocenter means each beam contributes 90 cGy of the 180 cGy. Monitor units are dose divided by dose per monitor unit. Right: 90/0.45 = 200. Left: 90/0.60 = 150. The right beam needs more monitor units because each monitor unit is worth less at isocenter, which is what a greater depth or a thicker path looks like in the calculation. It is not the case that each beam delivers the full 180 cGy. Multiplying instead of dividing inverts the output and produces the numbers in D.

### Q2
Stem: A wedged pair has a hinge angle of 120 degrees between the central axes. Using the approximation wedge angle = 90 degrees minus half the hinge angle, what wedge angle balances the pair?
A. 120 degrees
B. 60 degrees
C. 30 degrees
D. 90 degrees
Answer: C
Objective: III.7
Why: Answer C. The planning approximation is wedge angle = 90 − (hinge angle)/2. Half of 120 is 60, and 90 − 60 = 30 degrees. A 60 degree wedge would fit a hinge of 60 degrees, because 90 − (60/2) = 60. A 90 degree wedge would imply a hinge of 0, which is not a pair. The hinge itself is not the wedge angle. This relation aims the thick ends of the wedges so the hot spot where the two entrances overlap is pulled down.

### Q3
Stem: An anterior field and a posterior field contribute dose at isocenter in the ratio 2:1, anterior to posterior. The prescription at isocenter is 200 cGy. How many cGy does each beam contribute at isocenter?
A. Anterior 200, posterior 100
B. Anterior 133 cGy, posterior 67 cGy
C. Anterior 100, posterior 50
D. Anterior 50, posterior 150
Answer: B
Objective: III.7
Why: Answer B. A weight ratio of 2:1 means the anterior beam delivers twice the posterior beam's dose at the normalization point, and the two contributions sum to 200 cGy. Let the posterior contribution be x. Then 2x + x = 200, so 3x = 200 and x = 66.7 cGy. The anterior contribution is 133.3 cGy. Check: 133.3 + 66.7 = 200, and 133.3/66.7 = 2. Answer A sums to 300. Answer C sums to 150. Answer D inverts the ratio.

### Q4
Stem: Beam weight is defined at isocenter. Two opposed beams have equal weight and very different path lengths. Which statement about monitor units is true?
A. Equal weight means equal monitor units
B. Equal weight means equal dose from each beam at isocenter, so the beam with the lower dose per monitor unit at isocenter receives more monitor units
C. The beam with the shorter path length always receives more monitor units when weights are equal
D. Weight is defined as the jaw size, so equal weight means equal equivalent squares
Answer: B
Objective: III.7
Why: Answer B. In the usual planning definition, weight is the relative dose each beam contributes at a stated point, here isocenter. Equal weights therefore mean equal cGy at that point, not equal monitor units and not equal jaw settings. The beam that is attenuated more, or that has the lower output at isocenter, needs more monitor units to deposit its share. That is typically the longer path, not the shorter one. Defining weight as jaw size confuses beam weight with field size.

### Q5
Stem: A three-field pelvis (anterior and two laterals) is weighted so each field contributes the same dose at isocenter. The anterior path to isocenter is shorter than either lateral path. Which field is expected to have the lowest monitor units for its one-third share of the isocenter dose?
A. The anterior field
B. The left lateral
C. The right lateral
D. All three must match the lateral monitor units because the weights are equal
Answer: A
Objective: III.7
Why: Answer A. Each field owes the same cGy at isocenter. Dose per monitor unit is higher for the anterior field because the depth is smaller (the percent depth dose or TMR is higher). Monitor units equal contribution divided by dose per monitor unit, so the anterior field needs fewer monitor units. The laterals need more. Equal dose weight does not force equal monitor units; it forces the opposite when the depths differ.

## Normalization Mini-Quiz

### Q1
Stem: A plan is normalized to 100% at isocenter, and isocenter is 200 cGy per fraction. The PTV minimum lies on the 93% isodose. What is the PTV minimum dose?
A. 193 cGy
B. 186 cGy
C. 215 cGy
D. 93 cGy
Answer: B
Objective: III.7
Why: Answer B. With this normalization, percent is a fraction of the isocenter dose. The minimum is 0.93 × 200 = 186 cGy. A 7% cold relative to isocenter is 14 cGy, and 200 − 14 = 186, not 193. If instead the physician had wanted the 93% line to be 200 cGy, the isocenter would have to be raised to 200/0.93 ≈ 215 cGy, which is answer C and is a different prescription. The number 93 is a percent, not a dose in cGy.

### Q2
Stem: Continuing from a plan with isocenter at 200 cGy and the PTV minimum at 186 cGy on the 93% line: the physician changes the prescription so the 93% line must receive 200 cGy. By what factor do all doses scale, and what is the new isocenter dose?
A. Scale by 200/186 = 1.075; new isocenter dose is 215 cGy
B. Scale by 186/200 = 0.93; new isocenter dose is 186 cGy
C. Scale by 93/100; new isocenter dose is 186 cGy while the minimum stays 200 cGy without scaling
D. No scaling is possible; percent isodose lines cannot be assigned a prescription
Answer: A
Objective: III.7
Why: Answer A. The 93% line is currently 186 cGy and must become 200 cGy. The scale factor is 200/186. Compute 200 ÷ 186: 186 × 1.07 = 199.02, remainder 0.98, and 0.98/186 ≈ 0.005, so the factor is about 1.075. New isocenter dose is 200 × 1.075 = 215 cGy, which is also 200/0.93. Every other point, including hot spots, scales by the same 1.075. Scaling by 0.93 would lower the minimum further. You cannot move only the minimum to 200 cGy and leave isocenter at 200 cGy without changing the shape of the dose distribution; a pure renormalization moves them together.

### Q3
Stem: After the rescaling in the previous problem, a hotspot that was 105% of the old isocenter (210 cGy) becomes how many cGy, and what percent of the new 200 cGy prescription is that?
A. 210 cGy, which is 105% of the new prescription
B. 210 × (200/186) ≈ 226 cGy, which is 226/200 ≈ 113% of the prescription
C. 210 × 0.93 ≈ 195 cGy, which is 97.5% of the prescription
D. 105% of 186 cGy = 195 cGy
Answer: B
Objective: III.7
Why: Answer B. The hotspot scales with everything else by 200/186. Compute 210 × 200 / 186. First, 210/186 = 1.1290, because 186 × 1.129 = 186 × 1.1 = 204.6 and 186 × 0.029 = 5.394, summing to 209.994. Then 1.129 × 200 = 225.8 cGy. As a percent of the prescription, 225.8/200 = 112.9%, about 113%. Equivalently, the hotspot was 105/93 of the new prescription: 105 ÷ 93 = 1.129. It does not stay 210 cGy, because the prescription was deliberately moved off isocenter.

### Q4
Stem: A physician writes "prescribe 50 Gy to the 100% isodose" and does not say what 100% refers to. The plan on the screen has 100% at isocenter, PTV D95 equal to 95% of isocenter, and a hotspot of 110% of isocenter. Which clarification is required before the plan is approved?
A. None; "100%" always means the PTV minimum in every planning system
B. Whether 50 Gy is attached to isocenter or to a covering isodose, because those choices differ by the ratio of the two lines
C. None; a hotspot of 110% proves 100% is the prescription by ICRU 83
D. Whether 50 Gy is a BED or a monitor-unit setting
Answer: B
Objective: III.7
Why: Answer B. The same percent labels support two different treatments. If 100% at isocenter is 50 Gy, the PTV D95 is 0.95 × 50 = 47.5 Gy. If the physician meant 50 Gy to cover 95% of the PTV, isocenter must be 50/0.95 ≈ 52.6 Gy and the hotspot becomes 1.10 × 52.6 ≈ 57.9 Gy. That is a real difference in both coverage and hot spot. The note has to name the point or the dose-volume value that receives 50 Gy. ICRU 83 does not define the prescription as whatever point is 110%.

### Q5
Stem: A protocol asks for the PTV to receive between 95% and 107% of 60 Gy, in the ICRU 50 sense. The reported PTV minimum is 58.2 Gy and the reported PTV maximum is 63.0 Gy. Does the PTV satisfy the window?
A. Yes; 58.2/60 = 97% and 63.0/60 = 105%, both inside 95% to 107%
B. No; 58.2 Gy is 95% of 60 Gy only if the window is applied to monitor units
C. No; 63.0 Gy is 107% of 60 Gy exactly, and the rule excludes 107%
D. Yes, but only if 58.2 Gy is first converted to EQD2 with α/β = 10
Answer: A
Objective: III.11
Why: Answer A. The window in gray is 0.95 × 60 = 57.0 Gy through 1.07 × 60 = 64.2 Gy. The minimum, 58.2 Gy, is 58.2/60 = 0.970, or 97.0%. The maximum, 63.0 Gy, is 63/60 = 1.050, or 105%. Both sit inside 57.0 to 64.2 Gy. This check is on physical dose to the PTV as the protocol stated it. It is not an EQD2 conversion and not a monitor-unit check. A maximum of exactly 64.2 Gy would be at the 107% edge the ICRU window included, but that is not the number in this plan.

## Site Specific Treatment Planning and Historical Techniques

### Q1
Stem: A three-field breast technique matches opposed tangents to a supraclavicular field. Which geometric trick makes the superior border of the tangents non-divergent so it can meet the inferior border of the supraclavicular field?
A. Rotating the collimator until the tangent superior border is the half-beam axis, or using a single isocenter on the match line so the superior and inferior jaws meet without divergence
B. Increasing the electron energy of the tangents until divergence disappears
C. Using a physical wedge with the heel pointed inferiorly, which removes superior divergence
D. Matching the fields on the skin only, because divergence is zero at 100 cm source-to-skin distance
Answer: A
Objective: III.2
Why: Answer A. Tangent beams diverge into the supraclavicular field and produce a hot or cold match if both beams are open past isocenter. Half-beam blocking (the match line on the central axis) removes divergence at that border. A single-isocenter technique puts the isocenter on the match line, uses the inferior jaws for the tangents and the superior jaws for the supraclavicular field, and the central axes themselves form the match. A couch kick can also take the superior divergence out of the tangents when the isocenter is inside the breast. Wedges modulate intensity; they do not remove geometric divergence. Divergence is not zero just because the skin is at 100 cm.

### Q2
Stem: Field-in-field segments are added to whole-breast tangents. The segments block the 105% to 110% islands inside the breast. What planning method is this, and what device is it often replacing?
A. Inverse-planned volumetric modulated arcs replacing the need for any physician contour
B. Forward-planned subfields that flatten the hot spots, used instead of physical wedges
C. A bolus design to increase skin dose over the entire breast for every fraction
D. A proton range shifter sequenced as a sliding window
Answer: B
Objective: III.7
Why: Answer B. Field-in-field planning is forward planning: the dosimetrist copies the open tangent, closes the multileaf collimator around a hot island, and weights that segment so the hot spot comes down. The prescription isodose then covers the breast with a smaller maximum than the open wedges would have produced. It is not an inverse arc, it is not bolus, and it does not change the photon energy. Bolus is a separate decision when the skin itself is a target, as it often is for a chest wall.

### Q3
Stem: A classic mantle field for Hodgkin lymphoma covered the cervical, supraclavicular, axillary, and mediastinal nodes in one anterior-posterior pair, with blocks for the lungs, larynx, and humeral heads. How is modern involved-site radiotherapy different for early favorable disease after chemotherapy?
A. It still treats a full mantle to 40 Gy, because the historical volume is required
B. It treats the node regions that originally contained disease, to a lower dose on the order of 20 to 30 Gy, and it does not routinely cover every uninvolved mantle site
C. It replaces photons with total skin electrons
D. It omits the mediastinum even when the mediastinum was the site of bulk disease
Answer: B
Objective: III.2
Why: Answer B. The mantle field is a historical large-field technique. Current involved-site and involved-node approaches, after effective chemotherapy, limit the irradiated volume to the original disease with a margin for uncertainty, and early favorable doses are commonly in the 20 to 30 Gy range rather than a uniform 40 Gy mantle. That reduction is why heart, breast, and lung dose are lower than in the historical field. It does not mean a site of original bulk disease is dropped from the volume. Total skin electron therapy is a different disease and a different target.

### Q4
Stem: A single posterior spine field is prescribed to a depth of 6 cm. The cord is 4 cm from the posterior surface. The beam is 6 MV, with dmax at about 1.5 cm. Past dmax, percent depth dose falls with depth. How does the cord dose compare with the dose at the prescription depth?
A. The cord receives less than the prescription because it is closer to the skin
B. The cord receives more than the prescription because it is shallower than the 6 cm point and both points are past dmax
C. The cord receives exactly the prescription because a single posterior field is flat from 1.5 cm to 6 cm
D. The cord receives zero because the beam enters from the posterior surface and dose starts at the anterior vertebral body
Answer: B
Objective: III.2
Why: Answer B. For 6 MV, dose builds up to about 1.5 cm and then declines. The cord at 4 cm is past dmax but closer to dmax than the 6 cm prescription point, so its percent depth dose is higher. Prescribing 30 Gy to 6 cm therefore puts more than 30 Gy on the cord. That may be acceptable or not depending on the cord limit and the fractionation, but it is not equal to the prescription and it is not lower. A parallel-opposed pair or a prescription point chosen at the cord changes this relationship. The beam does not skip the posterior tissues.

### Q5
Stem: An extremity soft-tissue sarcoma will be treated with photons to the limb compartment. The plan covers the target circumferentially with opposed fields that spare a longitudinal strip of soft tissue. Why is that strip left out?
A. To leave a path for lymphatic drainage and to avoid a ring of fibrosis that acts like a tourniquet
B. To raise the integral dose by forcing the beam through the contralateral limb
C. Because sarcoma is radioresistant below 20 Gy and the strip is the only region treated
D. Because the strip is the GTV and must be blocked on every sarcoma
Answer: A
Objective: III.2
Why: Answer A. A fully circumferential high-dose shell around a limb scars the draining lymphatics and can produce severe edema distal to the field. The classical planning rule is to keep an unirradiated strip of tissue along the limb, as long as that strip is not part of the target volume. The block is not the GTV. Integral dose is not a reason to treat the opposite leg. Preoperative doses are often about 50 Gy in 25 fractions; postoperative doses are higher, on the order of 60 to 66 Gy, because the microscopic residual is dispersed in a hypoxic surgical bed. The strip rule applies to both.

## Planning Methodology Quiz

### Q1
Stem: A forward-planned field-in-field breast plan and an inverse-planned arc both remove a hot spot. Which description of the methods is correct?
A. Forward planning sets the apertures and weights, then evaluates the dose; inverse planning sets dose objectives and lets the optimizer create the fluence
B. Inverse planning is defined as the planner drawing each segment by hand; forward planning forbids wedges and segments
C. They are biologically different prescriptions; inverse planning always changes α/β
D. Forward planning cannot block a 110% island inside a tangent
Answer: A
Objective: III.7
Why: Answer A. The direction of the work is the definition. In forward planning the dosimetrist chooses energy, angles, apertures, and weights, including small segments that cover a hot island, and then looks at the dose. In inverse planning the dosimetrist enters objectives and constraints (target coverage, organ maximums, dose-volume points) and the optimizer proposes beamlet weights, which a sequencer turns into apertures. Either method can cool a breast hot spot. Neither method changes the α/β of the tissue.

### Q2
Stem: A parallel organ and a serial organ are both in an inverse plan. The lung objective is a mean dose. The cord objective is a maximum dose. Which equivalent-uniform-dose parameter matches each organ?
A. Lung: a large positive a, because a large positive a approaches the minimum dose. Cord: a = 1
B. Lung: a near 1, because a = 1 reproduces the mean dose. Cord: a large positive a, because a large positive a approaches the maximum dose
C. Both organs use a large negative a, which approaches the maximum
D. Equivalent uniform dose cannot represent a maximum, so the cord must be optimized as a mean
Answer: B
Objective: III.12
Why: Answer B. Niemierko's equivalent uniform dose uses a parameter a that selects which part of the dose distribution dominates. As a approaches positive infinity, the equivalent dose approaches the maximum, which fits a serial organ such as cord, where a small hot spot matters. As a approaches negative infinity, it approaches the minimum, which is used to punish cold spots in a tumor. At a = 1 the equivalent dose is the mean, which fits a parallel organ such as lung when the mean dose is the chosen objective. Assigning the cord a mean-dose objective would allow a hot voxel as long as the average stayed low, which is the wrong biology for myelopathy.

### Q3
Stem: A historical four-field pelvic box and a modern volumetric modulated arc both treat the same prostate and seminal vesicles to 78 Gy. The box delivers high dose to a rectangular volume that includes a large part of the bladder and rectum. What is the planning reason to move to the arc or to fixed-field intensity modulation?
A. The modulated plan can carve a concave high dose around the rectum and lower the bladder and rectal volume at high dose
B. The box always has a steeper falloff outside the PTV than a modulated arc
C. Modulation removes the need for a rectal contour
D. A four-field box cannot be weighted, so it cannot place 78 Gy at isocenter
Answer: A
Objective: III.7
Why: Answer A. The clinical problem in prostate planning is that the rectum and bladder wrap the target. A box's high-dose region is essentially the intersection of four beams and cannot bend. Intensity modulation and arcs can, which is why rectal V70 and bladder high-dose volume fall when the same 78 Gy is delivered with modulation, at the cost of more low-dose scatter. The rectum still has to be contoured; otherwise the optimizer has nothing to spare. A box can be weighted and can deliver a prescription to isocenter. Its limitation is shape, not arithmetic.

### Q4
Stem: An optimizer reports that the cord maximum, the parotid mean, and the PTV D95 cannot be met together. The planner tightens all three objectives and reoptimizes. The score worsens and the PTV develops a cold spot. What is the planning interpretation?
A. The optimizer failed; a feasible plan always appears if the penalties are increased
B. The objectives are in conflict on this anatomy; tightening an infeasible set does not create a solution, and the physician has to choose the tradeoff
C. Cold spots in the PTV are required by ICRU when a cord objective is present
D. Switching the energy from 6 MV to 6 MeV will satisfy all three without a tradeoff
Answer: B
Objective: III.12
Why: Answer B. Inverse planning searches the objectives it is given. If no beam arrangement can cover the PTV and hold the cord and the parotid at the requested levels, the cost function will sacrifice the objective with the weaker penalty, often the target. Raising every penalty keeps the problem infeasible. The useful output is the tradeoff: how much PTV coverage is lost per gray of cord, or what a slightly lower prescription would do. That choice is the physician's. Electrons of 6 MeV will not treat a deep head-and-neck volume.

### Q5
Stem: A proton plan and a photon arc plan both cover a base-of-skull target. The proton plan uses robust optimization. What extra scenarios is the proton optimizer evaluating that a standard photon PTV expansion does not?
A. Only the daily flatness of the photon beam
B. Range uncertainty and setup error, because a proton stops and a few millimeters of extra range can move the high dose onto a distal organ
C. The α/β of every voxel, recalculated each iteration as if it were a BED optimizer
D. Neutron shielding thickness in the vault wall
Answer: B
Objective: III.7
Why: Answer B. A photon PTV expands the target geometrically so that setup error still leaves the CTV inside the high dose. A proton beam has an additional error: the range. Stopping power, not just the geometric outline, decides where the distal falloff sits. Robust optimization computes the dose under shifted setups and under scaled densities (a few percent of the range) and penalizes a plan that only looks good in the nominal case. That is not a photon flatness check, not a radiobiology solver, and not a vault calculation.
