# Module 25. Planning Methodologies

Energy, normalization, and beam weight change the dose the patient receives even when the apertures look the same. Historical field arrangements are still how the exam describes a plan in words.

## Beam Energy

**MDCB objectives:** III.7, I.3, I.5

**What the exam expects**

You can pick a photon energy for the depth and the clinical constraint, and an electron energy for a therapeutic depth using the rule the stem names. You know when 6 MV is the better choice even if a higher energy penetrates farther: modulation, neutrons, and implanted electronics.

**Core facts**

Higher megavoltage photon energy pushes dmax deeper, increases skin sparing, increases exit dose, and widens the penumbra from lateral electrons. Above about 10 MV the accelerator head produces photoneutrons. That is a shielding issue and an electronics issue. For a pacemaker or a defibrillator, prefer 10 MV or below so photoneutrons do not upset the device (TG-203, module 31).

In inverse-planned treatments, 6 MV is the usual energy. The optimizer buys penetration with beam directions instead of with 18 MV, and it avoids the neutron component and the wider penumbra. Deep 3D conformal pelvis fields still sometimes use 10–18 MV laterals to keep the subcutaneous dose down. That is a 3D reason, not an IMRT default.

Percent depth dose depends on energy, depth, field size, SSD, and how much of the field is blocked. An off-axis factor depends on the distance from the central axis.

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

If the stem says Khan, the minimum is 9.6 MeV, so a 10 MeV beam clears 3 cm (10/3.2 = 3.1 cm) and 9 MeV does not (9/3.2 = 2.8 cm). If the stem says Bentel, 12 MeV is the minimum and it lands exactly on 3 cm. Report the rule with the energy.

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

**Parallel opposed.** Two fields 180° apart, equal weight for a midline target. Simple and homogeneous when the separation is modest. Entrance hot spots grow with separation and with lower energy. Palliative spine, whole brain, and many femur fields are still opposed pairs. Whole brain is typically 30 Gy in 10. A femur met may be 8 Gy once, 20 Gy in 5, or 30 Gy in 10. Three or more photon beams that cross in the target generally make the target dose more homogeneous than one beam, which falls from the entrance to the exit.

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

## Named Site Techniques: IMN, Off-Cord, and Past-Pointing

**Objectives:** III.7, III.2

**What the exam expects**

You can describe the two ways internal mammary nodes are covered with tangents, say when and why a lung plan comes off the cord, and define past-pointing for a partial arc. These are vocabulary items: the stem names the technique and asks what problem it solves.

**Core facts**

Internal mammary nodes. Standard tangents stop at the medial breast edge and do not cover the internal mammary chain. Two classic solutions exist. Wide (deep) tangents move the posterior border medially and deeper so the first three intercostal spaces are inside the tangent; the price is more ipsilateral lung and, on the left, more heart in the field. The partially-wide or mini-tangent variant deepens only the upper part of the tangent, where the nodes lie, and keeps the lower border shallow with a block or MLC. The alternative is a separate anterior IMN field matched to the medial border of the tangents; it is often a mixed photon–electron field (for example 70 percent electrons and 30 percent photons) so the deep dose to the heart and lung is limited while the surface is covered. The match line between the anterior field and the medial tangent is the junction to watch.

Off-cord at 45 Gy. In a classic AP/PA lung or esophagus plan the spinal cord receives nearly the full dose of every fraction. The accepted plan is to deliver the opposed pair to about 40–45 Gy and then change to an oblique or off-cord arrangement (an anterior field plus a posterior oblique, or opposed obliques) that excludes the cord while the tumor is carried to 60–66 Gy. The 45 Gy point is the conventional cord tolerance used for that switch; QUANTEC places the 0.2 percent myelopathy risk at 50 Gy to the full cord cross-section, and the bank uses 45 Gy as the planning switch point because it leaves a margin below the QUANTEC figure. The second phase is called a cone-down or an off-cord boost. Inverse planning makes the same decision continuously by writing the cord constraint into the whole course.

Past-pointing. In rotation therapy with a full 360-degree arc the dose maximum lands at the isocenter. With a partial arc (for example 180 or 240 degrees) the dose maximum shifts toward the entrance side of the arc, because more of the beams enter from that side. To bring the maximum back onto the tumor the isocenter is placed past the tumor center, on the side away from the arc. That deliberate displacement is past-pointing. It is a 3D-arc and conformal-arc technique; VMAT optimizers remove the need for it by modulating the fluence instead of moving the isocenter.

**Traps**

- Describing wide tangents as a technique that spares the heart. They cover the nodes by including more heart and lung.
- Coming off the cord at 60 Gy. The switch happens at the cord tolerance, around 45 Gy, not at the tumor dose.
- Placing the past-pointed isocenter on the arc side of the tumor. It goes away from the arc.
- Treating past-pointing as a VMAT setting.

**Sources**

- Bentel, treatment planning and dose calculation in radiation oncology, for IMN techniques and arc therapy
- Khan and Gibbons, rotation therapy section
- QUANTEC spinal cord summary (module 43), for the 50 Gy figure that the 45 Gy planning habit sits under

## Surface Dose, APBI, and Plan Quality Indices

**Objectives:** III.7, III.12

**What the exam expects**

You can state which setup choices raise the surface dose of a megavoltage photon beam, list the ASTRO suitability criteria for accelerated partial-breast irradiation and the standard brachytherapy schedule, predict where the hot spot sits in each classic field arrangement, and compute a conformation number.

**Core facts**

Surface dose. For a megavoltage photon beam the surface dose rises with field size (more head scatter and more contaminant electrons from the collimator and air), with a blocking tray or any accessory in the beam (the tray is an electron source, and the closer it sits to the skin the worse it is; a 15–20 cm tray-to-skin distance is the usual minimum), and with oblique incidence (the buildup region is compressed along the surface, so the dose at the skin rises as the beam tilts). Surface dose falls as energy rises and as SSD increases, because the contaminant electrons spread and are absorbed in air. Bolus, of course, raises it deliberately. A physical wedge can slightly lower the electron contamination by absorbing it, but the exam items are the three increases: field size, tray, obliquity.

APBI eligibility. The ASTRO consensus statement defines a suitable group for accelerated partial-breast irradiation outside a trial: age 50 or older, invasive ductal carcinoma or low- to intermediate-grade DCIS, tumor 2 cm or smaller for invasive disease (DCIS up to 2.5 cm; later guidance extends suitable tumors to 3 cm), negative margins of at least 2 mm, node-negative disease, no lymphovascular invasion, and estrogen-receptor-positive status. Patients between those limits are cautionary, and young patients, large tumors, positive nodes, or positive margins are unsuitable. The standard brachytherapy APBI schedule is 34 Gy in 10 fractions, twice daily, at least 6 hours apart, over 5 days; the external-beam equivalent is 38.5 Gy in 10 fractions BID. Shorter schedules (30 Gy in 5 fractions every other day, 40 Gy in 15 daily) are now also used.

Hot-spot expectations by technique. Parallel-opposed photon fields put the hot spots near dmax at both entrances; they grow with separation and shrink with higher energy. A four-field box is homogeneous in the center with small hot spots at the field entrances. A wedged pair without the right wedge angle is hot along the thin side where the two entrances stack. Field-in-field breast plans aim to pull the hot spot below about 107–110 percent. An inverse plan's hot spot is expected inside the PTV, typically up to about 107–110 percent of the prescription, and a hot spot outside the target is a plan defect even when the number is small. Stereotactic plans intentionally run 125–200 percent at the center. More beams generally improve conformity and raise the maximum inside the target.

Conformation number. The RTOG conformity index (prescription isodose volume divided by target volume) does not say whether the prescription volume is on the target. The conformation number of van't Riet does: CN = (target volume covered by the prescription isodose / target volume) × (target volume covered by the prescription isodose / total prescription isodose volume). The first factor is coverage, the second is the fraction of prescribed-dose tissue that is target. CN runs from 0 to 1 and 1 is ideal.

**Formulas**

CN = (TV_RI / TV) × (TV_RI / V_RI), where TV is the target volume, V_RI the volume enclosed by the prescription isodose, and TV_RI the part of the target inside that isodose.

The PTV is 100 cc, the prescription isodose encloses 130 cc, and 95 cc of the PTV is inside it. Coverage = 95 / 100 = 0.95. Selectivity = 95 / 130 = 0.731. CN = 0.95 × 0.731 = 0.694. Check: 0.694 / 0.95 = 0.731. The RTOG conformity index for the same plan is 130 / 100 = 1.30 and says nothing about the 5 cc of PTV that was missed.

**Traps**

- Saying surface dose falls as the field opens. It rises.
- Moving the tray closer to the skin to tighten the penumbra and forgetting the electron contamination.
- Calling a 45-year-old with a 2.5 cm node-positive tumor suitable for APBI.
- Quoting 34 Gy in 10 fractions as a once-daily schedule; it is twice daily over 5 days.
- Treating a 108 percent hot spot outside the PTV as acceptable because the number is small.
- Reporting the RTOG conformity index as if it measured coverage.

**Sources**

- Khan and Gibbons, skin dose section, for field size, tray, and obliquity
- ASTRO consensus statement on accelerated partial-breast irradiation (2009, updated 2016), for the suitable, cautionary, and unsuitable groups
- NSABP B-39 / RTOG 0413, for the 34 Gy brachytherapy and 38.5 Gy external-beam schedules
- van't Riet et al., for the conformation number; RTOG 0813 and 0915 for the conformity index (module 19)

## Technique Trade-offs and Delivery Contingencies

**Objectives:** III.7, III.12

**What the exam expects**

You can state what a VMAT plan typically gains and loses against a fixed-field IMRT plan, explain why a physical wedge on the medial tangent is a contralateral-breast problem and what replaces it, predict the three things that change when beams are added to a conformal plan, handle an IMRT fraction that stopped part-way through, and name the checks that are specific to a vertex field.

**Core facts**

VMAT against fixed-field IMRT. For comparable objectives the arc plan is usually more conformal (the prescription isodose hugs the target from 360 degrees), uses fewer monitor units and less beam-on time, but is often slightly less homogeneous inside the target (a higher D2 or hot spot) and spreads a larger low-dose bath because every angle is an entrance path. The low-dose volume grows because the dose is painted around the full circumference rather than along seven or nine paths; it is not primarily a leakage effect, and jaw tracking trims the leakage part. Which plan is better is a trade between conformity and the volume of tissue under a few gray.

Medial physical wedge and the contralateral breast. A physical wedge scatters photons out of the beam toward the patient's midline. On the medial tangent that scatter lands on the contralateral breast, and the steeper the wedge the more it scatters. Measured contralateral breast doses are highest with physical wedges on the medial field and lowest with open or field-in-field tangents; a dynamic wedge produces far less peripheral scatter because no metal is in the beam. The planning preference is therefore a dynamic wedge or field-in-field subfields medially, and if a physical wedge is unavoidable it goes on the lateral field. Field-in-field also drops the wedge factor out of the monitor-unit calculation, so the fields need fewer MU.

Adding beams. Going from four to nine coplanar fields with the same normalization makes the prescription isodose more conformal, raises the maximum inside the target (conformity and homogeneity trade against each other), and spreads the penumbra and entrance dose of each beam over more of the surrounding tissue. The entrance dose per beam falls, the volume receiving a low dose rises, and the integral dose typically rises or stays about the same; it does not fall because the beams are individually weaker.

Partially delivered IMRT fraction. If the machine faults after some fields of an IMRT fraction have been delivered, the record-and-verify log shows exactly which fields and how many monitor units were given. The physicist reconstructs the delivered dose from those fields, as a partial plan, because the fields contribute very unevenly to different parts of the target and the organs. The fraction of total monitor units delivered is not the fraction of dose at any particular point, and the fraction of fields delivered is not either unless the per-field contributions are given. Once the delivered dose is known, the physician decides whether to deliver the remaining fields when the machine returns, to deliver them on another day, or to design a make-up. The two errors to refuse are repeating the whole fraction without the estimate (which double-doses the fields already given) and crediting the fraction as complete.

Vertex field. A vertex field enters the top of the skull with the couch rotated about 90 degrees and the gantry near horizontal. Two checks are specific to it. First, clearance: with the couch kicked, the gantry head and the imaging arms pass close to the couch end and the patient's shoulders, so the geometry is dry-run in the treatment position before the first fraction, and the table height is recorded because it changes the clearance. Second, the exit path: the beam exits inferiorly through the neck and trunk, so the CT dataset must include the whole entrance and exit path (a scan that clips the vertex calculates the field through air) and the exit dose through the body is reviewed.

**Formulas**

Delivered isocenter dose for a partial fraction = sum of the planned isocenter contributions of the fields that were completed. Nine fields contribute 30, 25, 20, 25, 20, 20, 25, 20, and 15 cGy (total 200 cGy). Fields 1 to 5 completed: 30 + 25 + 20 + 25 + 20 = 120 cGy at the isocenter. The remaining 80 cGy is in fields 6 to 9. Check: 120 + 80 = 200. The naive 5/9 × 200 = 111 cGy assumes equal field weights and is wrong here; and the 120 cGy describes only the isocenter, not the coverage of the PTV, which needs the partial-plan calculation.

**Traps**

- Saying VMAT is more homogeneous and has a smaller low-dose volume. The usual direction is the reverse on both.
- Putting a steep physical wedge on the medial tangent and ignoring the contralateral breast.
- Reporting that adding beams lowers the target maximum. Conformity rises and so does the internal maximum.
- Crediting an interrupted IMRT fraction by the percentage of monitor units delivered.
- Repeating the whole fraction after a fault because "IMRT cannot be partially credited".
- Approving a vertex field from the planning screen without a clearance dry run and without the exit path in the CT.

**Sources**

- Khan and Gibbons, IMRT and arc therapy chapters, for the VMAT versus IMRT comparison
- Published tangent-breast scatter measurements comparing physical wedges, dynamic wedges, and field-in-field (the direction is consistent across them: physical wedge medially is highest)
- AAPM TG-100 and departmental incident-handling policy, for the partial-fraction workflow
- Simulation and planning texts (Bentel) for vertex-field geometry and clearance
