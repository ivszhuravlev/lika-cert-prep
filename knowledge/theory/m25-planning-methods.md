# Module 25. Planning Methodologies

Energy, normalization, and beam weight change the dose the patient receives even when the apertures look the same. Historical field arrangements are still how the exam describes a plan in words.

## Beam Energy

**MDCB objectives:** III.7, I.3, I.5

**What the exam expects**

You can pick a photon energy for the depth and the clinical constraint, and an electron energy for a therapeutic depth using the rule the stem names. You know when 6 MV is the better choice even if a higher energy penetrates farther: modulation, neutrons, and implanted electronics.

**Core facts**

Higher megavoltage photon energy pushes dmax deeper, increases skin sparing, increases exit dose, and widens the penumbra from lateral electrons. Above about 10 MV the accelerator head produces photoneutrons. That is a shielding issue and an electronics issue. For a pacemaker or a defibrillator, prefer 10 MV or below so photoneutrons do not upset the device (TG-203, module 31).

In inverse-planned treatments, 6 MV is the usual energy. The optimizer buys penetration with beam directions instead of with 18 MV, and it avoids the neutron component and the wider penumbra. Deep 3D conformal pelvis fields still sometimes use 10–18 MV laterals to keep the subcutaneous dose down. That is a 3D reason, not an IMRT default.

Electrons are chosen so the 80% or 90% depth covers the distal target and the practical range spares what is behind it. The two depth rules:

- Khan: 90% ≈ E/3.2, 80% ≈ E/2.8
- Bentel: 90% ≈ E/4, 80% ≈ E/3
- Practical range ≈ E/2
- Energy loss ≈ 2 MeV/cm

Match the rule to the stem. A full worked set is in the isodose module. One selection example is below so this lesson is not only a pointer.

Superficial and orthovoltage kilovoltage beams are for very shallow targets. They are not “low-energy megavoltage.” Skin dose is high and percent depth dose falls quickly.

**Formulas and a worked energy pick**

The distal target is at 3.0 cm. The prescription is to the 90% electron line. Nothing critical sits before 6 cm.

Khan: E / 3.2 ≥ 3, so E ≥ 9.6 MeV. A 9 MeV beam gives 9 / 3.2 = 2.8 cm and stops short. A 12 MeV beam gives 12 / 3.2 = 3.75 cm and covers 3.0 cm.

Bentel: E / 4 ≥ 3, so E ≥ 12 MeV. At 12 MeV, Bentel’s 90% depth is 12 / 4 = 3.0 cm, exactly the target depth.

Practical range at 12 MeV: 12 / 2 = 6 cm. A structure at 7 cm is past the electrons and sees only bremsstrahlung. A structure at 4 cm is still in the electron beam: remaining energy ≈ 12 − (2 MeV/cm × 4 cm) = 4 MeV.

If the stem says Khan, 12 MeV is the first common energy that clears 3 cm, and 9 MeV does not. If the stem says Bentel, 12 MeV is the minimum and it lands exactly on 3 cm. Report the rule with the energy.

Photon side of the same idea: a midline pelvic point on a large patient is a penetration problem. An 18 MV parallel-opposed pair spares the subcutaneous tissue relative to 6 MV and exits more. Once the plan is a multi-arc 6 MV VMAT, the energy choice has already been made for modulation and neutrons, and the arcs replace the high-energy laterals.

**Traps**

- Choosing 18 MV for modulated head-and-neck or for a patient with a pacemaker.
- Covering an electron target to dmax or to Rp instead of to the 80–90% line.
- Mixing Khan and Bentel divisors.
- Calling 6 MV and 6 MeV the same beam.

**Sources**

- Khan and Bentel, for the electron depth rules
- AAPM TG-203, for the 10 MV neutron threshold around implanted electronics
- AAPM TG-25 and TG-70, for clinical electron energy selection

## Normalization

**MDCB objectives:** III.7, III.1, III.12

**What the exam expects**

You can say what “100%” means on the plan in front of you, and you can rescale every dose, including the organs at risk, when the normalization changes. You know the ICRU 50 reference-point habit and the ICRU 83 habit of reporting D50, D98, and D2.

**Core facts**

Normalization picks the dose that is called 100%, or it scales the whole distribution so that one chosen condition is met. Common choices:

- 100% at isocenter or at the ICRU reference point
- 100% at dmax of one beam (an old point-dose habit)
- PTV mean, or D50%, set equal to the prescription
- D95% of the PTV set equal to the prescription, or 95% of the PTV covered by 95% of the prescription

These are different plans only in scale if the fluence is frozen. The shape is unchanged. Every organ dose moves by the same factor. A normalization that lifts the target also lifts the cord.

ICRU 50 wanted the reference point in a region of gentle gradient, representative of the PTV, and wanted target dose to stay within about −5% to +7% of the prescription. ICRU 83, for IMRT, reports the median D50% and describes the spread with D98% and D2%. A plan normalized so that D95% equals the prescription can still have a D50% several percent higher. Say which one you set.

Coverage language: “95% of the PTV receives at least 100% of the prescription” is a DVH statement. It is not the same sentence as “the isocenter is 100%.”

**Formulas and a worked rescale**

The prescription is 200 cGy per fraction. On the current normalization, PTV D95% is 190 cGy and the cord D2% is 140 cGy. You renormalize so D95% equals 200 cGy. The scale factor is

200 / 190 = 1.053

Cord D2% becomes

140 × 1.053 = 147 cGy

A mean parotid dose that was 80 cGy becomes 80 × 1.053 = 84 cGy. Nothing about the apertures improved the cord. The labels moved. If 147 cGy per fraction times the number of fractions now fails the cord constraint, the fix is a new fluence, not a quieter normalization.

Second direction. The plan is normalized to 100% at dmax, and the PTV mean is 93%. The prescription is 180 cGy to the PTV mean. The dmax dose that must be delivered is

180 / 0.93 = 193.5 cGy

You prescribed 180 cGy to the mean. On this distribution that forces the dmax point to 193.5 cGy.

**Traps**

- Changing normalization and reading the old absolute OAR doses as if they were still valid.
- Treating “100% isodose” as a universal physical dose.
- Setting D95% to the prescription and reporting that value as the ICRU 83 median. The median is D50%.
- Normalizing a proton plan in physical gray and prescribing in Gy (RBE) without the 1.1 factor.

**Sources**

- ICRU 50, reference point and the −5% to +7% guidance
- ICRU 83, D50, D98, and D2 for IMRT

## Beam Weighting

**MDCB objectives:** III.7

**What the exam expects**

You can turn a weight ratio into a share of the isocenter dose, and you know that a weight defined at dmax is not the same statement as a weight defined at isocenter. You can predict which side of a parallel-opposed pair runs hotter when the weights are unequal.

**Core facts**

A beam weight is that beam’s contribution relative to the other beams, at a stated point. In most modern planning systems the point is the isocenter. Older conventions weight at dmax. A weight of 1.0 at dmax delivers less to a deep isocenter than a weight of 1.0 at isocenter, because of attenuation. Read the definition before you compare two plans.

Equal weights on a parallel-opposed pair, in a flat homogeneous patient, put the midplane dose in the middle and leave hot spots toward both entrances, near dmax. The hot spots grow as the separation grows and as the energy falls. Unequal weights shift the midplane balance toward the heavier beam and make that beam’s entrance hotter still.

A wedge is not a weight. A weight scales the whole beam. A wedge tilts the dose across the beam. Field-in-field subfields are a way to remove a hot spot without changing the nominal open-beam weight by hand.

For a wedged pair, the classic relation between hinge angle φ (the angle between the central axes) and wedge angle θ is

θ ≈ 90° − φ / 2

Heels of the wedges point at the thin side of the patient, where the two entrances would otherwise stack. A physical wedge, a dynamic wedge, or a field-in-field slope can all produce that tilt. The formula is the design rule for the classic pair.

**Formulas and worked weights**

Two opposed beams, weights 2 and 1 at the isocenter. Each beam, if given weight 1, would contribute 100 cGy to the isocenter.

Heavy beam: 2 × 100 = 200 cGy

Light beam: 1 × 100 = 100 cGy

Isocenter total: 300 cGy

Share from the heavy beam: 200 / 300 = 0.67, or 67%

Share from the light beam: 100 / 300 = 0.33, or 33%

The entrance on the heavy side is the hot entrance. If the prescription is 200 cGy to the isocenter, scale the whole plan by 200/300 = 0.667. The heavy beam then contributes 133 cGy at the isocenter and the light beam 67 cGy. Entrances scale by the same 0.667. This is normalization and weighting together. Do both steps.

Wedged pair. Hinge angle 90°.

θ = 90 − 90/2 = 90 − 45 = 45°

Each beam gets a 45° wedge.

Hinge angle 120°.

θ = 90 − 120/2 = 90 − 60 = 30°

Each beam gets a 30° wedge. A wider hinge needs a shallower wedge. A narrower hinge needs a steeper wedge. If the hinge is 60°, θ = 90 − 30 = 60°.

**Traps**

- Adding weights as if they were already percent doses. Weights 2 and 1 are a 2:1 ratio, which is 67% and 33% of the isocenter dose, not 200% and 100% of the prescription, until you normalize.
- Mixing dmax weights with isocenter weights.
- Calling the wedge factor a beam weight. The wedge factor belongs in the monitor-unit calculation. The wedge angle belongs in the shape of the isodose lines.
- Pointing both wedge heels the same way and stacking the hot spots.

**Sources**

- Bentel and Khan, for wedged-pair geometry and weight definitions
- ICRU 50, for the reference point those weights are aiming at

## Normalization Mini-Quiz

**MDCB objectives:** III.7, III.1

**Skills this quiz trains**

- Identify what is set to 100% or to the prescription.
- Multiply every dose, OAR doses included, by the scale factor.
- Separate D95, D50, and isocenter normalization.
- Convert a weight ratio into a fraction of isocenter dose, then scale to the prescription.

**Traps**

- Rescaling the target and leaving the cord number unchanged.
- Reporting D95 as the ICRU median.
- Treating a 2:1 weight as 200 cGy and 100 cGy after the prescription was already 180 cGy to isocenter.

**Check yourself**

Isocenter doses from the two beams are in the ratio 3:1 before normalization, and the isocenter currently reads 240 cGy. The prescription is 200 cGy to the isocenter. What does each beam contribute after normalization?

Walk-through: The heavy beam is 3/4 of 240 = 180 cGy. The light beam is 1/4 of 240 = 60 cGy. Scale factor = 200/240 = 5/6 ≈ 0.833. After scaling, the heavy beam contributes 180 × 5/6 = 150 cGy and the light beam contributes 60 × 5/6 = 50 cGy. Sum = 200 cGy. Any OAR dose on the old plan is also multiplied by 5/6.

## Site Specific Treatment Planning and Historical Techniques

**MDCB objectives:** III.7, III.2, III.12

**What the exam expects**

You can name the classic arrangement for a site and the problem it was built to solve: parallel opposed, four-field box, three-field, wedged pair, breast tangents, field-in-field, en face electrons, and inverse planning for a concave target. You can describe a photon–electron match and an electron–electron junction. Modern IMRT did not delete this vocabulary. Stems still use it.

**Core facts**

**Parallel opposed.** Two fields 180° apart, equal weight for a midline target. Simple and homogeneous when the separation is modest. Entrance hot spots grow with separation and with lower energy. Palliative spine, whole brain, and many femur fields are still opposed pairs. Whole brain is typically 30 Gy in 10. A femur met may be 8 Gy once, 20 Gy in 5, or 30 Gy in 10.

**Four-field box.** AP, PA, and two laterals. The classic whole pelvis. The laterals spare rectum or bladder relative to a pure AP/PA, depending on weights and energy. A common historical choice was higher energy on the laterals of a large patient. The modern version is often VMAT with the same organs to spare. Recognize the box when a stem describes it.

**Three-field.** PA plus laterals, or an anterior field plus wedged laterals. Used for rectum and for some upper-abdominal targets so the anterior bowel or the perineum is not an entrance. Short-course rectum is 25 Gy in 5. Long-course is 50.4 Gy in 28. The technique name does not tell you which dose. The stem does.

**Wedged pair.** Two fields with a hinge, wedges with heels to the thin side, wedge angle about 90° minus half the hinge. The usual superficial lateralized target is a parotid. Compute the angle as in the weighting lesson.

**Breast tangents.** Opposed tangential fields that flash off the anterior breast and meet on a straight posterior edge. That posterior edge is made non-divergent so the lung does not receive a diverging deep border: half-beam block, collimator rotation, or a couch kick. A mono-isocentric match places the isocenter on the junction with the supraclavicular field so both the tangents and the supraclavicular field are non-divergent at the match. Field-in-field subfields pull hot spots out of the breast without a physical wedge. Conventional dose is 45–50.4 Gy plus a boost. Hypofractionation is 40 Gy in 15 or 42.5 Gy in 16. Left-sided tangents are the heart and LAD problem. The geometric tangent calculation (gantry, central-axis depth, flash) is practiced in the calculation modules. Here you name the arrangement and the reason for the non-divergent posterior border.

**En face electrons.** Chest wall, a scar boost, a posterior neck boost after the cord has had its photon dose. Pick the energy so the 80–90% line covers the target (Khan or Bentel, as named). Block with lead about E/2 millimeters thick.

**Photon–electron junction.** Hot on the photon side, cold on the electron side. Move the match or feather it if the cold line sits on tumor.

**Adjacent electrons.** The useful beam constricts, so the skin fields need a small overlap or a feather. Too much overlap is a hot spot at depth where the low isodoses bulge.

**Inverse planning.** Head and neck, prostate with rectum spared, and many anal and gynecologic volumes are concave. Objectives on minimum target DVH, maximum OAR DVH, and sometimes EUD drive the beamlet weights. The planner still chooses energy (usually 6 MV), the arc or the beam angles, the normalization, and whether the objectives match the protocol. Autoplanning can draft this. It does not sign it.

**Half-beam and field matching.** A half-beam block puts the central axis on the match line so divergence into the neighboring field is removed on that side. Mono-isocentric breast fields are the standard example. A gap calculation for diverging photon fields is a later calculation lesson. Do not invent a skin gap for electrons with the photon gap formula. Electron junctions are an overlap or a feather because of constriction.

**Inhomogeneity.** Lung plans and TBI lung doses are calculated with heterogeneity on. A homogeneous calculation through lung is the wrong chart. Density overrides for contrast and metal are the inhomogeneity module. Mention them when the historical technique crosses a hip prosthesis or oral contrast.

**Traps**

- Using a photon skin gap as the recipe for abutting electrons.
- Forgetting which side of a photon–electron match is hot.
- Treating field-in-field breast as sliding-window inverse IMRT.
- Putting 18 MV on a pacemaker patient because the separation is large.
- Quoting a four-field box dose without reading whether the site is preoperative rectum, prostate, or cervix. The box is a shape. The dose is the regimen in the oncology module.
- Wedging the wrong heel and creating the hot spot the wedge was meant to remove.

**Sources**

- Bentel, for historical field arrangements and the wedged-pair relation
- Khan, for electron matching and beam energy
- ICRU 50, 62, and 83, for how those arrangements are prescribed and reported
- Site doses as typical regimens in the oncology module, confirmed against the prescription in front of you

## Planning Methodology Quiz

**MDCB objectives:** III.7, III.2

**Skills this quiz trains**

- Select electron energy with a named 90% rule and check Rp behind the target.
- Keep modulated plans and electronic implants at or below 10 MV unless the stem gives a reason not to.
- Rescale a plan and every OAR with one factor.
- Convert a weight ratio to isocenter contributions.
- Compute a wedge angle from a hinge angle.
- Name tangents, box, wedged pair, three-field, and field-in-field, and place the hot side of a photon–electron match.
- Explain electron overlap or feathering at the skin.

**Traps**

- Khan versus Bentel.
- Normalization that silently raises the cord.
- Weights defined at dmax compared with weights at isocenter.
- Photon gap formula used on electrons.
- 18 MV chosen next to a pacemaker.

**Check yourself**

Hinge angle 100°. What wedge angle does the classic formula assign? A photon field abutted to an electron field on the skin: which side is hot?

Walk-through: θ = 90 − 100/2 = 90 − 50 = 40°. Each beam is a 40° wedge if the formula is being followed exactly. The hot side of the skin match is the photon side. The electron side is cold.
