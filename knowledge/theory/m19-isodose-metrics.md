# Module 19. Isodose Distributions and Dose Metrics

Photons, electrons, protons, isodose curves, ICRU volumes, and DVHs. Doses below are typical values and worked examples, not prescriptions.

## Electrons 101

**MDCB objectives:** I.3, I.5, III.1, III.7

**What the exam expects**

You can place the 90% depth, the 80% depth, and the practical range from beam energy using the rule the stem names. You can apply the 2 MeV/cm energy-loss rule, the lead-thickness rule, and the low-energy limit for an internal eye shield. You can describe surface dose, the bremsstrahlung tail, a photon–electron skin match, and why adjacent electron fields need overlap or feathering.

**Core facts**

Electrons deposit dose over a finite range and then stop. The therapeutic depth is the depth of the 80% or 90% isodose, not dmax and not the end of the range. Past the practical range the electron dose is gone. What remains is a bremsstrahlung tail: x-ray contamination from electrons stopping in the scattering foils, jaws, and the patient. That tail is a few percent of dose at dmax on a typical linac and is larger at higher electron energy. The percent for a given machine is commissioning data. Confirm it there, and in the methods of AAPM TG-25 and TG-70.

Two rule-of-thumb families are in common use. Use the one the question names. The MDCB exam does not ask you to name Khan versus Bentel; the bank keeps both rules so you can recognize either formula.

Khan:

- Depth of the 90% isodose (cm) ≈ E / 3.2
- Depth of the 80% isodose (cm) ≈ E / 2.8

Bentel:

- Depth of the 90% isodose (cm) ≈ E / 4
- Depth of the 80% isodose (cm) ≈ E / 3

Shared rules, either source:

- Energy loss in water ≈ 2 MeV per cm
- Practical range Rp (cm) ≈ E / 2
- Lead thickness for blocking (mm) ≈ E / 2

E is the nominal energy in MeV. Depths come out in centimeters. Lead thickness comes out in millimeters. Watch the unit.

Surface dose rises as electron energy rises. A 6 MeV beam still has a noticeable buildup; an 18 MeV beam is already high at the skin. Megavoltage photons behave the other way: higher photon energy increases skin sparing. The exam swaps these on purpose.

The useful beam constricts. Multiple scattering pulls the 80% and 90% isodose lines inward relative to the light field as depth increases. The low isodose lines bulge outward. A small cutout also loses side-scatter equilibrium, so output falls and dmax moves. A cone factor measured for the open applicator is the wrong output once a cutout blocks a large part of that cone. Use the commissioned cutout factor.

Internal eye shields are for low energies, about 9 MeV and under. A high-Z shield behind the eyelid backscatters electrons into the lid. That backscatter becomes unacceptable as energy rises, and the shield may not stop the beam. Above that range, shield externally or choose another technique.

Obliquity raises surface dose and pulls the therapeutic depth shallower. Bolus does the same job on purpose when the target includes the skin: it brings the 90% line up to the surface and shortens the range in tissue.

Electron output at an extended distance does not follow inverse square from the nominal photon source. Clinics measure an effective SSD, often shorter than the nominal SSD, and use that. AAPM TG-25 and TG-70 describe the measurement. Do not invent an effective SSD in a calculation the stem did not give.

**Formulas and worked examples**

Take a 12 MeV beam.

Khan, 90% depth: 12 / 3.2 = 3.75 cm.

Khan, 80% depth: 12 / 2.8 = 4.29 cm.

Bentel, 90% depth: 12 / 4 = 3.0 cm.

Bentel, 80% depth: 12 / 3 = 4.0 cm.

Practical range: 12 / 2 = 6.0 cm.

Lead: 12 / 2 = 6 mm of lead.

Energy at 3 cm depth: loss ≈ 2 MeV/cm × 3 cm = 6 MeV, so about 6 MeV remains. By Khan, 3 cm is still shallower than the 90% depth (3.75 cm), so 3 cm is inside the therapeutic region. By Bentel, the 90% depth is exactly 3.0 cm. Same energy, two answers. The stem has to name Khan or Bentel. If it names neither, state which rule you used.

A target whose distal edge is at 3 cm, prescribed to the 90% line:

- Khan: E / 3.2 ≥ 3, so E ≥ 9.6 MeV. A 9 MeV beam is short of 3 cm (9 / 3.2 = 2.8 cm). A 12 MeV beam covers it (3.75 cm).
- Bentel: E / 4 ≥ 3, so E ≥ 12 MeV. On Bentel’s rule, 12 MeV puts 90% exactly at 3 cm.

Also check what is behind the target. At 12 MeV the practical range is 6 cm. A cord at 7 cm sees only the bremsstrahlung tail. A cord at 4 cm is still inside the electron range.

A 6 MeV chest-wall beam:

- Khan 90%: 6 / 3.2 = 1.88 cm. Khan 80%: 6 / 2.8 = 2.14 cm.
- Bentel 90%: 6 / 4 = 1.5 cm. Bentel 80%: 6 / 3 = 2.0 cm.
- Practical range: 3.0 cm. Lead: 3 mm.

A 16 MeV beam:

- Khan 90%: 16 / 3.2 = 5.0 cm. Khan 80%: 16 / 2.8 = 5.71 cm.
- Bentel 90%: 16 / 4 = 4.0 cm. Bentel 80%: 16 / 3 = 5.3 cm.
- Practical range: 8 cm. Lead: 8 mm.

Cerrobend is less dense than lead, so the same millimeters block less. Lead is about 11.3 g/cm³ and Cerrobend about 9.4 g/cm³. The thickness ratio is about 11.3 / 9.4 ≈ 1.2. For 12 MeV, 6 mm of lead scales to about 6 × 1.2 = 7.2 mm of Cerrobend. That is a starting estimate. The cutout you release is the one in the commissioned table.

Photon–electron skin match. Abut the fields on the skin and the junction is hot on the photon side and cold on the electron side. Electrons scatter out of their field readily. The photon penumbra is sharper and receives that electron scatter, so the photon side runs hot. The electron side has lost that scatter, and its useful isodose is already constricting, so the electron side runs cold.

Adjacent electron fields. The useful beam (the 80–90% lines) constricts inside the light-field edges. If two light fields are only abutted, a cold strip sits on the junction. Overlap the skin fields slightly, or feather the junction by moving it during the course. The low isodose lines bulge, so a generous overlap stacks dose at depth and makes a hot spot under the match. Feathering spreads that compromise along the junction instead of leaving it in one place.

**Traps**

- Quoting Khan’s divisor on a question that said Bentel, or the reverse.
- Reporting the practical range as the therapeutic depth. Therapeutic depth is the 80% or 90% line. Rp ≈ E/2 is where the electrons are gone.
- Using centimeters for the lead rule. Lead millimeters ≈ E/2.
- Putting an internal eye shield under a high-energy electron beam. The cutoff taught with these rules is about 9 MeV and under, because of backscatter.
- Assuming surface dose falls as electron energy rises. For electrons, surface dose rises with energy.
- Applying photon inverse square from the nominal source to an extended-SSD electron treatment.
- Ignoring constriction and abutting electron light fields with no overlap and no feather.

**Sources**

- Khan, *The Physics of Radiation Therapy*, for 90% ≈ E/3.2 and 80% ≈ E/2.8
- Bentel, treatment-planning dose calculation, for 90% ≈ E/4 and 80% ≈ E/3
- AAPM TG-25 and TG-70, clinical electron-beam dosimetry, for output, effective SSD, and contamination. Confirm a machine-specific percent in commissioning data.

## Electrons Quiz

**MDCB objectives:** I.3, III.1

**Skills this quiz trains**

- Compute 90% depth, 80% depth, practical range, and lead thickness for a stated energy, and name which depth rule you used.
- Subtract 2 MeV/cm to estimate energy remaining at a depth.
- Decide whether a structure behind the target is inside the electron range or under the bremsstrahlung tail only.
- Place the hot side and the cold side of a photon–electron skin match.
- Explain the surface cold junction of abutted electrons and the deep hot junction of too much overlap.
- Restrict internal eye shields to about 9 MeV and under.

**Traps**

- Khan versus Bentel on the same energy (12 MeV is 3.75 cm at 90% by Khan and 3.0 cm by Bentel).
- Rp used as the prescription depth.
- Lead thickness answered in centimeters.
- Photon skin-sparing logic copied onto electrons.
- Cone factor used in place of a cutout factor.

**Check yourself**

A 9 MeV en face field is prescribed to the 90% isodose. How deep is that line by Khan and by Bentel? How many millimeters of lead does the blocking rule call for? Is an internal eye shield in the energy range these rules allow?

Walk-through:

- Khan 90%: 9 / 3.2 = 2.8 cm.
- Bentel 90%: 9 / 4 = 2.25 cm.
- Lead: 9 / 2 = 4.5 mm.
- Practical range: 9 / 2 = 4.5 cm.
- About 9 MeV is the top of the range given for internal eye shields. A higher energy is past that rule because of backscatter into the lid.

## Protons 101

**MDCB objectives:** I.3, I.5, III.1, III.3

**What the exam expects**

You can describe a Bragg peak and a spread-out Bragg peak, give the clinical energy band the exam uses for deep treatments (about 150–250 MeV), and apply a generic RBE of 1.1. You can say why the distal end is a poor place to park a serial organ, and why a geometric PTV does not capture proton range uncertainty the way it captures photon setup error.

**Core facts**

A proton loses energy continuously and stops. Dose is modest along the entrance plateau, rises sharply in the Bragg peak near the end of range, and falls to nearly nothing beyond the peak. There is essentially no exit dose of the photon kind. A small dose from nuclear secondaries exists; it is not an exit beam.

A pristine peak is too narrow to cover a tumor. A spread-out Bragg peak (SOBP) stacks many pristine peaks of different energies and weights so the high-dose region is flat across the target thickness. Widening the SOBP raises the entrance dose, because more proximal peaks are added under the plateau.

Clinical energies for deep tumors are about 150–250 MeV. In water, 150 MeV reaches on the order of the mid-teens of centimeters, and 250 MeV reaches well past 30 cm. Ocular proton beams are lower energy, on the order of 60–70 MeV, because the eye is a shallow target. Do not answer “150–250 MeV” for an eye beam, and do not answer “70 MeV” for a deep pelvis.

The generic clinical RBE is 1.1. Prescriptions are written in Gy (RBE), also called GyE in older notes:

physical dose (Gy) × 1.1 = dose in Gy (RBE).

The 1.1 is an average used for prescribing and reporting. RBE actually climbs in the last few millimeters of the peak. ICRU 78 is the reporting framework. Confirm any departure from 1.1 in the protocol that authorized it.

Range sits on the stopping power along the ray. Bone, air, contrast, weight loss, and a sinus that fills between fractions move the peak. A uniform PTV expansion does not model that. The uncertainty is mostly along the beam, not a rim around the target. Robust optimization and a range margin are the planning tools. Confirm the numeric range uncertainty in the departmental proton protocol.

Put the distal end in something that can tolerate a range error. A serial organ just beyond the target (cord, brainstem, optic structures) is safer beside a lateral edge than immediately downstream of the peak. The lateral penumbra and the distal falloff are different edges. The distal edge is sharp and then uncertain in position. The lateral edge is where setup error lives.

Pencil-beam scanning paints spots of varying energy. Passive scattering uses foils, apertures, and a range modulator to build the SOBP. Both produce proton dose. The exam distinction is pristine peak versus modulated SOBP, and the larger low-dose neutron component of the scattering hardware.

**Formulas and worked examples**

RBE conversion, generic factor 1.1.

A prescription of 2 Gy (RBE) per fraction is a physical dose of

2 / 1.1 = 1.82 Gy.

A course of 70 Gy (RBE) is a physical dose of

70 / 1.1 = 63.6 Gy.

Going the other way: a physics check that measured 1.50 Gy physical in the SOBP corresponds to

1.50 × 1.1 = 1.65 Gy (RBE).

If a question asks for RBE and the particle is a clinical proton beam with no other factor supplied, the answer is 1.1. Carbon ions and neutrons are different particles with higher RBE. Do not paste 1.1 onto them.

**Traps**

- Describing protons as exponentially attenuated photons that happen to stop. The dose shape is a Bragg peak.
- Calling 150–250 MeV the ocular energy, or calling 70 MeV a deep-pelvis energy.
- Treating Gy and Gy (RBE) as the same number. The factor is 1.1 unless the stem says otherwise.
- Expanding a PTV in all directions and believing range uncertainty has been handled.
- Aiming the distal end at the cord because the falloff “looks sharp” on the nominal plan. The nominal range is not the uncertain range.
- Forgetting that a wider SOBP costs entrance dose.

**Sources**

- ICRU 78, prescribing, recording, and reporting proton-beam therapy (RBE 1.1 and the volume concepts for protons)
- AAPM proton-planning reports used by the department for the numeric range uncertainty. Confirm that margin in the named protocol rather than memorizing one universal percent.

## Protons Quiz

**MDCB objectives:** I.3, III.1, III.3

**Skills this quiz trains**

- Define Bragg peak and SOBP, including the entrance-dose cost of a wider SOBP.
- Quote about 150–250 MeV for deep clinical beams and a lower energy for the eye.
- Convert Gy (RBE) to physical Gy with 1.1, and the reverse.
- Explain range uncertainty along the beam and the danger of a serial organ on the distal end.
- Keep a geometric PTV from being described as a full proton uncertainty model.

**Traps**

- RBE of 1 applied to protons, or RBE of 1.1 applied to neutrons.
- Exit dose described as similar to 6 MV photons.
- One energy used for every site.

**Check yourself**

The prescription is 50 Gy (RBE) to an SOBP. What physical dose is that with RBE 1.1? If the energy in the stem is 70 MeV, which site class is plausible?

Walk-through: Physical dose = 50 / 1.1 = 45.5 Gy. About 70 MeV is an ocular energy, not the 150–250 MeV band used for deep tumors.

## Isodose Chart

**MDCB objectives:** III.1

**What the exam expects**

You can read an isodose chart: what the lines mean, which line is the therapeutic line for that modality, and which planning change bends those lines. You can describe photon penumbra, electron constriction and bulge, and a proton distal falloff as different shapes on the page.

**Core facts**

An isodose line joins points of equal dose. On a classic chart the lines are percents of the central-axis dose at dmax for that energy, field size, and SSD. On a plan they may be percents of the prescription or absolute dose. Read the legend before you call a line “the 100%.”

Photon open fields show buildup to dmax, a gradual fall past dmax, a penumbra at the geometric edge, and exit dose. Increasing energy pushes dmax deeper, increases skin sparing, and increases exit dose. A wedge tilts the lines. Bolus pulls the buildup to the skin. An inhomogeneity bends the lines: lung transmits more photon dose beyond the lung, bone less. Missing tissue at an oblique surface changes the depth along each ray.

The physical penumbra on a photon profile is the distance between the 80% and 20% dose levels, quoted at dmax for the classic definition. Geometric penumbra is the source-size projection and is practiced with the calculation modules. A measured penumbra includes geometric penumbra, scatter, and transmission through the jaw or leaf edge.

Electron charts show a finite range, constriction of the 80–90% lines, bulge of the low lines, and a bremsstrahlung tail past Rp. Proton charts show a plateau, an SOBP or a pristine peak, and a distal falloff with little dose beyond it.

Field size changes the chart. Larger photon fields add scatter and slightly raise the percent depth dose. Very small photon fields lose lateral charged-particle equilibrium, which is why stereotactic commissioning is its own dataset. Electron fields smaller than the equilibrium radius lose output and change shape.

Normalization chooses which physical dose is called 100%. Changing the normalization rescales every line. The chart shape is unchanged; the labels move. That rescaling is worked in the planning-methods module.

**Formulas**

Physical penumbra is a width, not a dose:

penumbra = lateral distance from the 80% point to the 20% point on a profile at the stated depth (classically dmax).

If the 80% point is 5.4 cm off axis and the 20% point is 6.1 cm off axis,

penumbra = 6.1 − 5.4 = 0.7 cm.

There is no further constant to apply. If the stem asks for geometric penumbra, it is a different quantity (source size, source distance, and depth). Do not report this 80–20 width as the geometric formula.

**Traps**

- Reading a plan normalized to dmax as if it were normalized to the PTV mean.
- Calling the photon 50% line the therapeutic electron depth. For electrons the therapeutic lines are 80% and 90%.
- Assuming a bigger field only changes the shape and not the output.
- Describing proton distal falloff with photon penumbra language. They are different edges.
- Forgetting exit dose on a photon chart when an organ sits behind the target.

**Sources**

- ICRU 62 and ICRU 83, for how isodose coverage is reported once the chart is a 3D plan
- Khan and Bentel, for the electron lines drawn on those charts
- AAPM TG-106, accelerator beam-data commissioning, for how a measured chart is produced

## Measurement of Isodose Curves

**MDCB objectives:** III.1, I.5

**What the exam expects**

You know the isodose chart is measured, usually in a scanning water tank, and that the detector has to be small enough for the gradient being measured. You can define the 80–20 physical penumbra and say what flatness and symmetry are asking. Numeric machine tolerances live in the commissioning baseline and in TG-142; confirm the pass number in that report rather than inventing one.

**Core facts**

A scanning water tank moves a detector through the beam and builds percent depth dose and profiles. Those profiles are stacked into isodose curves. The scan is performed at a stated SSD or SAD, energy, and field size. Change any of those and you need another chart or a calculation from commissioned data.

Detector volume averages dose over its cavity. A farmer-type chamber is appropriate for a broad photon profile in a gentle gradient. It is too big for an electron penumbra, a small stereotactic field, or the distal falloff of a proton peak. A small ion chamber, a diode, or film is chosen because the gradient is steep. If the detector is larger than the gradient, the measured penumbra looks wider than the true penumbra and a narrow peak looks shorter.

Scans are normalized to a defined point, classically the central-axis dmax for an isodose chart in percent. An absolute calibration (output in cGy per MU under the local reference conditions) is a separate measurement. Mixing a relative scan with the wrong output is how a correct-looking chart delivers the wrong dose.

Flatness describes how even the profile is over the central portion of the field at a stated depth (commonly 10 cm for megavoltage photons). Symmetry compares the two sides of that profile. Both are judged against the commissioned baseline. The numeric tolerance is in AAPM TG-142 and in the clinic’s commissioning report. Confirm it there.

Electrons are scanned for every cone and for representative cutouts because the chart and the output change with the applicator. Protons are measured as pristine peaks and as SOBPs, with the detector small enough for the distal edge.

**Formulas**

The 80–20 width from the previous lesson is the measured physical penumbra. Repeat the subtraction only when the stem gives two off-axis positions.

A symmetry check is also a subtraction in disguise. If the dose at equal distances left and right is DL and DR, one common way to express asymmetry is the difference relative to the sum or to the central dose, depending on the protocol definition. Use the definition the stem or TG-142 passage gives. Do not divide by an arbitrary constant.

Example of reading a profile, not of inventing a tolerance: central-axis dose at 10 cm is 100% of the local normalization, the dose 8 cm to the left inside the field is 103%, and the dose 8 cm to the right is 101%. The two sides differ by 2 percentage points. Whether that passes is the TG-142 comparison with baseline, confirmed in the report, not a mental guess.

**Traps**

- Measuring a stereotactic or electron penumbra with a large chamber and believing the widened curve.
- Treating a relative isodose chart as an absolute output calibration.
- Quoting a single flatness percent from memory as if every energy and depth used the same pass number. Confirm in TG-142.
- Scanning electrons only at the photon reference field size.

**Sources**

- AAPM TG-106, beam-data commissioning
- AAPM TG-142, ongoing geometric and dosimetric QA. Confirm numeric tolerances in the report.
- AAPM TG-25 and TG-70, electron measurements

## Target Volume Definitions

**MDCB objectives:** III.11, III.1

**What the exam expects**

You can define GTV, CTV, ITV, PTV, and PRV, and you can say which report split the internal margin from the setup margin. You can define treated volume and irradiated volume. For IMRT reporting you use D98 as the near-minimum, D50 as the median dose to report, and D2 as the near-maximum.

**Core facts**

ICRU 50 defined the photon volumes that every exam still uses.

- **GTV**, gross tumor volume: the visible, palpable, or otherwise demonstrable disease.
- **CTV**, clinical target volume: the GTV plus the margin for subclinical microscopic disease that must be treated. A CTV can also be an elective nodal volume with no GTV inside it.
- **PTV**, planning target volume: in ICRU 50, the CTV plus a margin for all geometric uncertainty, motion and setup together.
- **Treated volume**: the tissue enclosed by an isodose surface chosen as adequate for the purpose of treatment. The usual teaching illustration is the volume inside the 95% isodose. The defining isodose is part of the prescription description.
- **Irradiated volume**: the tissue that receives a dose considered significant relative to normal-tissue tolerance. The usual teaching illustration is a lower isodose such as 50%. It is larger than the treated volume.

ICRU 62 split the geometric margin.

- **Internal margin** covers physiologic motion and shape change: respiration, bladder, rectum, swallowing, heartbeat.
- **ITV**, internal target volume: the CTV plus the internal margin.
- **Setup margin** covers day-to-day placement of the patient relative to the beams.
- **PTV**: the ITV plus the setup margin. Equivalently, CTV plus internal margin plus setup margin.
- **OAR**: an organ at risk.
- **PRV**, planning organ-at-risk volume: the OAR plus a margin for its motion and for setup error. You spare the PRV when a serial organ can move into the high dose.

ICRU 50 also asked that dose variation through the target stay within about −5% to +7% of the prescribed dose when a point-dose prescription was appropriate (the familiar 95% to 107% band). The ICRU reference point was to sit where the dose is representative and easy to define: not in a steep gradient, often at the center of the PTV or at the intersection of the beams.

ICRU 83 changed the reporting for IMRT, where a single point is a poor summary of a modulated dose.

- **D98%** is the near-minimum dose (dose covering 98% of the volume).
- **D50%** is the median dose, and it is the absorbed dose ICRU 83 uses to report the PTV.
- **D2%** is the near-maximum dose (only 2% of the volume receives more than this).

The notation: D98 means a dose, the dose that covers 98% of the volume. V20 Gy means a volume, the volume that receives at least 20 Gy. A single-voxel minimum or maximum is still visible in the TPS, and it is not the ICRU near-min or near-max. One noisy voxel should not be reported as the target dose.

Proton and electron plans still need a GTV and a CTV. The margin from CTV to the treated region follows the uncertainties of that modality (range, for protons) rather than a copied photon PTV recipe. Confirm the expansion recipe in the site protocol.

**Formulas**

Volume order, ICRU 62:

PTV = CTV + internal margin + setup margin = ITV + setup margin.

Reporting, ICRU 83, for a PTV whose DVH gives D98% = 66 Gy, D50% = 70 Gy, and D2% = 74 Gy:

- Near-minimum = 66 Gy
- Reported median dose = 70 Gy
- Near-maximum = 74 Gy

If the prescription was 70 Gy, the median matches the prescription and the near-min is 66 / 70 = 0.943, or 94.3% of the prescription. A single-voxel maximum of 76 Gy may exist in the grid and is not the near-maximum. The near-maximum is D2%, here 74 Gy.

**Traps**

- Drawing a PTV and calling it the CTV. The CTV is disease. The PTV is geometry.
- Putting microscopic disease only in the PTV. Microscopic disease belongs in the CTV. The PTV can move with setup; disease does not shrink because the mask was tight.
- Reporting Dmin and Dmax as the ICRU 83 doses. Report D98, D50, and D2.
- Swapping D and V. D95 is a dose. V95 is a volume (or a percent of volume) receiving at least the stated dose.
- Equating treated volume with PTV. The treated volume is an isodose shell. It can be larger or smaller than the PTV and it can be shifted off it.
- Forgetting the PRV and applying an OAR constraint to the organ contour alone when the organ moves.

**Sources**

- ICRU Report 50, photon beam prescribing and reporting
- ICRU Report 62, supplement on margins, ITV, and PRV
- ICRU Report 83, IMRT prescribing and reporting (D98, D50, D2)

## DVH Interpretation and Dose Metrics

**MDCB objectives:** III.1, III.12

**What the exam expects**

You can read a cumulative DVH and a differential DVH and say what each axis means. You can define conformity and homogeneity in words and compute a simple index when the volumes are given. You can state what a DVH cannot prove: where the dose sits, whether the contour is in the right place, and whether the dose grid was fine enough.

**Core facts**

A dose-volume histogram throws away position. It keeps only “how much tissue got how much dose.”

The cumulative DVH, in the convention used in radiotherapy, plots the volume that receives at least dose D. At D = 0 the volume is the whole structure. The curve falls as the dose rises. A steep drop near one dose means the structure is homogeneous. A shoulder or a tail to the right means some of the volume is hotter. A curve that falls early means some of the volume never reached the high dose.

The differential DVH plots the volume inside each dose bin. It is a histogram. Peaks show where the tissue is concentrated in dose. The area under the whole differential DVH is the volume of the structure.

The cumulative value at dose D is the sum of the differential bins from D up to the maximum dose. Given one, you can build the other. They are not two independent measurements.

Absolute DVHs use cubic centimeters. Relative DVHs use percent of the structure. A relative V20 of 30% is a very different volume of lung than of cord. Serial organs (cord, brainstem, optic nerves) are judged by the high-dose end: D2% or a small-volume absolute dose. Parallel organs (lung, liver, parotid, kidneys) are judged by mean dose and by the percent or the absolute volume above a threshold. The numeric limit comes from the named source in the stem (QUANTEC, TG-101, RTOG, Timmerman, or a protocol). Confirm that limit in the named source.

Conformity, in words: the high-dose region follows the shape of the target. The prescription dose covers the target, and tissue outside the target stays below that dose.

Homogeneity, in words: the dose inside the target is even. The near-minimum and the near-maximum sit close to the median.

A common conformity index (RTOG style) is

CI = prescription-isodose volume / target volume.

A value of 1 means the two volumes are equal in size. It does not mean they occupy the same space. A cloud the same size as the PTV, shifted entirely beside it, still scores 1 and treats the wrong tissue.

The Paddick index uses the overlap:

CI_Paddick = (target volume inside the prescription isodose)² / (target volume × prescription-isodose volume).

Perfect overlap scores 1. A miss or a spill pulls the score down.

ICRU 83 homogeneity:

HI = (D2% − D98%) / D50%.

Zero would be perfectly flat. Larger means a wider spread from near-min to near-max.

Optimizer language you should recognize (the full planning use is in the planning-methods module): a minimum DVH objective pushes a percent of the target above a dose, a maximum DVH objective pushes a percent of an OAR below a dose, and an equivalent uniform dose (EUD) objective summarizes an organ with a single biologically weighted dose. A DVH objective still cannot see where the hot voxel sits.

What a DVH cannot prove:

- It cannot prove location. A hot 2% of the PTV may be in the center, on the airway, or against the cord. Open the slices.
- It cannot prove the contour is right, or that it is the structure named in the objective. A perfect rectal DVH on a contour drawn in the prostate is a perfect DVH of the wrong organ.
- It cannot prove the dose grid was fine enough. The DVH bins whatever the grid computed. A coarse grid averages a narrow hotspot, a small serial organ, or a high-gradient match into one bland voxel. Stereotactic plans and high-gradient matches need a finer grid than a palliative parallel-opposed pair. The grid size that was commissioned for that technique is the authority. Confirm it in the TPS commissioning report. A common practice is a few millimeters for conventional plans and a finer grid for stereotactic work; the report, not a proverb, is the tolerance.

**Formulas and worked examples**

Differential to cumulative. A 100 cm³ target, simplified into three bins:

- 20 cm³ receive about 60 Gy
- 70 cm³ receive about 70 Gy
- 10 cm³ receive about 75 Gy

Differential peaks sit at 60, 70, and 75 Gy with heights proportional to 20, 70, and 10 cm³.

Cumulative (“at least this dose”):

- At 60 Gy, volume = 20 + 70 + 10 = 100 cm³
- At 70 Gy, volume = 70 + 10 = 80 cm³
- At 75 Gy, volume = 10 cm³
- Above 75 Gy, volume = 0

The cumulative curve is high on the left and steps down. The differential curve is three spikes. A question that says “the volume receiving at least 70 Gy” wants the cumulative number, 80 cm³, which is 80% of this target. A question that says “how much tissue sits in the 70 Gy bin” wants the differential number, 70 cm³.

Homogeneity. D2% = 74 Gy, D98% = 66 Gy, D50% = 70 Gy.

HI = (74 − 66) / 70 = 8 / 70 = 0.114.

Near-min, median, and near-max are 66, 70, and 74 Gy.

Conformity, size only. Prescription-isodose volume = 120 cm³. PTV = 100 cm³.

RTOG-style CI = 120 / 100 = 1.2.

The prescription cloud is 20% larger than the PTV. You still do not know if the PTV is covered. Add the overlap. Suppose 95 cm³ of the PTV is inside the prescription isodose.

Paddick = 95² / (100 × 120) = 9025 / 12000 = 0.75.

Coverage is 95 / 100 = 95%. Spill and the 5 cm³ miss both keep the Paddick score well below 1. Neither index tells you whether the missed 5 cm³ is at the tumor edge the physician cares about. That is the location limit of every DVH metric.

**Traps**

- Answering a “volume receiving at least X” question with the height of one differential bin.
- Treating CI = 1 as proof of a correct plan.
- Calling a steep cumulative DVH “heterogeneous.” A steep cumulative fall is homogeneous. A broad differential peak, or a long cumulative tail, is heterogeneous.
- Using a percent-volume lung metric on a structure whose absolute volume was never checked.
- Accepting a DVH when the grid, the contour, or the image registration was never looked at.
- Reporting a one-voxel maximum as D2%.

**Sources**

- ICRU 83, for D2, D50, D98, homogeneity, and conformity language in IMRT
- ICRU 50 and 62, for the volumes the DVH is computed on
- QUANTEC, AAPM TG-101, and the protocol named in a constraint question, for the numeric OAR limit. Confirm the number in that source.

## Target Volume Definitions, Isodose Distributions, and Dose Metrics Quiz

**MDCB objectives:** III.1, III.11, III.12

**Skills this quiz trains**

- Define GTV, CTV, ITV, PTV, PRV, treated volume, and irradiated volume, and place ITV and PRV with ICRU 62.
- Report IMRT target dose as D98 near-min, D50 median, and D2 near-max.
- Compute a Khan depth and a Bentel depth for the same energy and a proton physical dose from Gy (RBE) with RBE 1.1.
- Convert a three-bin differential description into cumulative “at least this dose” volumes.
- Define conformity and homogeneity in words, then compute HI or a coverage index from given numbers.
- State the three things a DVH does not prove: location, contour correctness, and grid adequacy.
- Place the hot spot of a photon–electron skin match on the photon side.

**Traps**

- Khan E/3.2 versus Bentel E/4.
- Cumulative volume versus one differential bin.
- Dmin/Dmax reported in place of D98/D2.
- CI = 1 accepted as a located, conformal, grid-adequate plan.
- Proton RBE omitted, or 150–250 MeV used for an eye beam.
- Internal eye shield allowed at high electron energy.

**Check yourself**

1. PTV D2% = 63 Gy, D50% = 60 Gy, D98% = 57 Gy. What are the near-maximum, the reported median, and the near-minimum, and what is HI?
2. A differential description of a 50 cm³ organ: 10 cm³ at 20 Gy, 30 cm³ at 45 Gy, 10 cm³ at 50 Gy. What volume receives at least 45 Gy?

Walk-through:

1. Near-max D2% = 63 Gy. Median D50% = 60 Gy. Near-min D98% = 57 Gy. HI = (63 − 57) / 60 = 6 / 60 = 0.10.
2. At least 45 Gy includes the 45 Gy bin and the 50 Gy bin: 30 + 10 = 40 cm³. The 10 cm³ at 20 Gy is below 45 Gy and stays out.

## Electron Beam Specifications and Cut-out Limits

**Objectives:** I.3, III.1

**What the exam expects**

You can say where an electron profile is specified (the reference plane), how electron symmetry is expressed, and which tolerance class applies. You can apply the lateral-equilibrium rule to decide whether a cut-out is "small" and state what a small cut-out does to output and to dmax. You can say why the electron virtual source sits closer than the nominal 100 cm and when that matters most.

**Core facts**

Reference plane. Electron flatness and symmetry are not specified at dmax or at 10 cm as photon profiles are. TG-25 places the reference plane perpendicular to the central axis at the depth of the 95 percent isodose beyond dmax, which is near the therapeutic depth of the beam. In that plane the distance between the 90 percent level and the geometric edge should stay within about 10 mm along the major axes and 20 mm along the diagonals, and no point in the plane should exceed about 105 percent of the central-axis value at the same depth.

Symmetry. Electron symmetry is the difference between mirror-image points on either side of the central axis in the reference plane; the TG-25 criterion is that the pair differ by no more than about 2 percent. TG-142 then treats profiles as a constancy test: the monthly and annual electron profile checks are within 1 percent of the commissioning baseline. The 3 percent symmetry figure that appears in older items is the TG-40 monthly tolerance, superseded by TG-142. The bank uses TG-25 for the definition and TG-142 for the periodic tolerance.

Lateral equilibrium and cut-outs. An electron field is "large" when its width is at least the lateral range of the electrons, which is reached when the smallest field dimension is at least about the practical range, Rp ≈ E/2 cm. Below that width, electrons scattered out of the field are not replaced by electrons scattered in: output at the prescription depth falls, dmax moves toward the surface, the depth-dose curve becomes less penetrating, and the depth of the 90 percent line shortens. A cut-out whose smallest dimension is below E/2 cm needs its own measured cut-out factor and its own depth-dose curve rather than the open-cone data. For 16 MeV the threshold is 8 cm; for 6 MeV it is 3 cm, which is why low-energy small cut-outs are far less troublesome than high-energy ones.

Virtual SSD. Electrons scatter in the foils, monitor chamber, and air, so the beam behaves as if it came from a virtual point source closer to the patient than the photon target at 100 cm. The virtual (or effective) SSD is measured by placing the cone at several air gaps and plotting the square root of the inverse of the reading against the gap; the intercept gives the distance. Typical values are 80 to 95 cm, and the shortfall is largest for low energies and small cones, where scatter in air and from the applicator is a larger share of the fluence. Inverse-square corrections for extended-distance electron treatments must use the virtual SSD plus the depth, not 100 cm plus the depth.

**Formulas**

Output at an extended distance relative to the standard set-up: ratio = ((SSDv + dmax) / (SSDv + dmax + gap))², where SSDv is the virtual SSD and gap is the extra air distance.

Example. Virtual SSD 85 cm, dmax 1.5 cm, air gap 10 cm: (86.5 / 96.5)² = 0.896² = 0.803. The same gap computed from the nominal 100 cm gives (101.5 / 111.5)² = 0.829, which overstates the output by about 3 percent.

Minimum cut-out dimension for full output: smallest side ≥ E/2 cm. Example: 12 MeV → 6 cm; a 5 by 7 cm cut-out fails on the 5 cm side.

**Traps**

- Specifying electron flatness at dmax or at 10 cm; the reference plane is at the depth of the 95 percent isodose.
- Quoting the 3 percent TG-40 symmetry figure as a TG-142 tolerance.
- Judging a cut-out by its area or its long side; the smallest dimension is what sets lateral equilibrium.
- Using 100 cm as the source distance in an electron inverse-square correction.

**Sources**

- AAPM TG-25 and TG-70, clinical electron-beam dosimetry, for the reference plane, flatness and symmetry criteria, virtual SSD, and small-field behaviour
- AAPM TG-142 for the profile-constancy tolerances
- Khan and Gibbons, electron beam therapy chapter, for the lateral-equilibrium field-size rule

## Hot-Spot Ladders, Lead Edges, and Penumbra Definitions

**Objectives:** III.12, III.1

**What the exam expects**

You can compute the inhomogeneity index as Dmax over Dmin and place an internal maximum on the ladder of what each technique normally accepts. You can describe the hot spot that forms beside a piece of lead placed on the skin in an electron field, and the hot and cold spots around an air cavity. You can state which two dose levels define the penumbra in a given stem and recognise that the 90–20 version is wider than the 80–20 version on the same profile.

**Core facts**

Inhomogeneity index. The simplest target homogeneity measure is the ratio of the target maximum to the target minimum, Dmax / Dmin; a value of 1.00 is perfectly uniform and larger values are less homogeneous. ICRU 83 reports the near-maximum and near-minimum, D2% and D98%, and the homogeneity index (D2% − D98%) / D50%. Both move in the same direction; the point-based ratio is more sensitive to single hot voxels.

Hot-spot ladder by technique. Conventional and 3D conformal photon plans are expected to keep the maximum at about 107 to 110 percent of the prescription, the ICRU 50 band extended slightly for field-in-field breast plans. Inverse-planned IMRT and VMAT plans trade homogeneity for conformity; internal maxima of about 110 to 115 percent are routine and are accepted when they sit inside the target. Stereotactic radiosurgery and SBRT plans prescribe to a low isodose line, commonly 50 to 80 percent, so the internal maximum is 125 to 200 percent of the prescription by design. The same 113 percent maximum is therefore unremarkable in an IMRT plan and a defect in a four-field box.

Lead on the skin. When a lead or cerrobend shield lies directly on the skin inside an electron field, electrons scatter off the vertical face of the shield into the adjacent open tissue. The result is a hot spot just inside the field beside the shield edge, extending a few millimetres under the surface in a tear-drop shape, while the dose under the shield is low. Mirror the geometry: the hot spot is on the open side of the edge, not under the lead. Coating the shield with a few millimetres of wax or bolus absorbs these scattered electrons and smooths the edge.

Air cavities. Electrons crossing an air cavity (nasal cavity, ethmoid cells, maxillary antrum) lose almost no energy, so the dose beyond the cavity is higher and the range is longer than the water calculation predicts. At the lateral walls of the cavity, scatter out of the tissue into the air is not balanced, so hot spots form in the tissue beside the cavity and cold regions sit behind the tissue columns. Filling the nasal cavity with wax or bolus removes the inhomogeneity for a nose or ethmoid electron treatment.

Penumbra definitions. The classic physical penumbra is the lateral distance between the 80 percent and 20 percent points on a profile at a stated depth. Some texts and some review sheets instead use the 90 percent to 20 percent distance; on the same profile the 90–20 width is always larger than the 80–20 width, because the 90 percent point sits farther inside the field. A stem that gives the dose levels defines the quantity; one that does not should be read as 80–20, which is the definition this bank uses.

**Formulas**

Inhomogeneity index = Dmax / Dmin. Example: Dmax 54.6 Gy, Dmin 49.0 Gy → 54.6 / 49.0 = 1.114. Check: 49.0 × 1.114 = 54.6.

Penumbra width = (position of the lower dose level) − (position of the upper dose level). Example: 90 percent at 4.8 cm, 80 percent at 5.1 cm, 20 percent at 5.9 cm from the axis → 80–20 penumbra 0.8 cm, 90–20 penumbra 1.1 cm.

**Traps**

- Reporting a 113 percent IMRT maximum as a violation of a 107 percent rule written for conventional plans.
- Placing the lead-edge hot spot under the shield instead of beside it.
- Mixing the 90–20 and 80–20 definitions, which differ by the 90-to-80 distance.

**Sources**

- ICRU 50, 62, and 83 for dose-uniformity reporting; RTOG stereotactic protocols for the 125 to 200 percent internal maxima
- Khan and Gibbons, electron beam therapy chapter, for shield-edge scatter and air-cavity effects
- AAPM TG-25 and TG-70 for internal shielding and bolus practice
