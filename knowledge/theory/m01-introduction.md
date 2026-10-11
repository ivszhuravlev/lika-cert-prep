# Module 1. Introduction

Original study notes for the MDCB CMD exam. Lesson titles match the public curriculum list. These notes are not DoseGrid course text and not an MDCB publication.

## Hello

**MDCB:** exam format, as stated in the public CMD exam handbook. Not a content-domain objective.

**What the exam expects**

The public handbook describes a 155-question exam, 3 hours 50 minutes, English only, aimed at U.S. practice. A few unscored pilot items are mixed in. A small number of items are performance-based in ProKnow (plan evaluation, isodose display, DVH, anatomy, beam arrangement, contouring). The content weights come from the 2023 Job Task Analysis. You are expected to compute, not only to recognize vocabulary. Stems change one condition at a time: SSD versus SAD, half-life versus mean life, image size versus object size, rad versus rem. The answer changes with that one condition.

**Core facts**

- 230 minutes for 155 questions is about 90 seconds per item. A calculation that runs past three minutes has to be paid for by faster items.
- Domain weights in the public test-specifications matrix: Radiation Physics 14%, Localization 8%, Treatment Planning 42%, Dose Calculation Methods 13%, Brachytherapy 5%, Radiation Protection 9%, Quality Assurance and Standard of Care 9%.
- Modules 2–12 in this set carry Domain I. Modules 13–16 carry the start of Domain II (patient data, position, motion, simulation, localization inside the planning system).
- Treatment planning is 42% of the test. Modules 1–16 do not carry it. Later modules in this set do. Physics in the early modules is the tool set those items use.
- Half-lives, decay, magnification, and unit conversion are written out in full in the lessons that own them. Redo the arithmetic with the page covered.

**Traps**

Treating every module as equal time. Physics is 14% and localization is 8%, and both are full of items that are either right or wrong with no partial credit. Spending the whole review on vocabulary and skipping the substitution step is how those items are missed.

**Sources**

Public MDCB CMD exam handbook and the 2023 CMD Test Specifications Matrix.

## Medical Dosimetrist Certification Board Content Breakdown

**MDCB:** all seven domains of the 2023 test specifications. This lesson is the weight map.

**What the exam expects**

Items are written to the job-task objectives, not to chapter titles. A single stem can sit in physics (a half-life) and still be scored as brachytherapy if the source is an implant, or sit in localization if the question is which CT data set is legal for dose calculation. Know the objective number so you can tell what skill is being scored.

**Core facts**

Domain I, Radiation Physics, 14%. Objectives I.1 through I.10: decay modes, production of x-rays and particle beams, beam characteristics, interactions, treatment machines, magnification, half-lives, imaging, Hounsfield units, and computations of dose, activity, dose equivalent, exposure, and HVL.

Domain II, Localization, 8%. Objectives II.1 through II.7: import and validate patient data, positioning, immobilization and motion, simulation parameters, registration, IGRT, and localizing the patient inside the planning system. Modules 13–16 cover II.1, II.2, II.3, II.4, and II.7. Registration and IGRT are later modules.

Domain III, Treatment Planning, 42%. Isodose and DVH, site oncology, radiobiology, anatomy, delivery systems, special procedures, planning methods, OAR constraints, computers and DICOM, automation, ICRU volumes, optimization, implanted devices. ICRU volume names are introduced in module 16 because localization uses them. The planning work itself is in later modules of this set.

Domain IV, Dose Calculation Methods, 13%. Algorithms, beam modifiers, special calculations, inhomogeneity, deformable accumulation, dose-grid limits. Module 13 starts inhomogeneity corrections. Monitor units, gaps, and wedges are later.

Domain V, Brachytherapy, 5%. Source characteristics, HDR and LDR, applicators, surveys, NRC and state rules, calculations. Module 3 supplies the half-lives and the permanent-implant total-dose relation those items reuse.

Domain VI, Radiation Protection, 9%. ALARA and dose limits, monitoring, vault barriers, detectors.

Domain VII, Quality Assurance and Standard of Care, 9%. Commissioning, plan and chart checks, measurement devices, record and verify, beam QA, AAMD scope, incident reporting, deliverability, sim and machine QA.

**Traps**

Memorizing the percentages and missing which objective a stem belongs to. A Hounsfield-unit item is I.9. A shift from tattoos to isocenter is II.7. A half-life used to correct a source activity is I.7 and often V.1 at the same time. The arithmetic is the same.

**Sources**

Public MDCB CMD Test Specifications Matrix, 2023 Job Task Analysis. Public CMD exam handbook.

## MDCB Formula Sheet

**MDCB:** I.6, I.7, I.9, I.10, III.3, IV.1, IV.2, IV.3, V.6, VI.3. One working sheet for modules 1–45. This is not a reproduction of a printed card. Each line is an original short form. The lesson that owns the relation shows the arithmetic.

**What the exam expects**

You may be given constants in the stem. You are still expected to know which formula applies, what each symbol means, and which time or distance unit matches the constant. The public handbook states what is supplied at the current exam. Read that handbook for the live sheet. PDD and TMR never share one monitor-unit line. Decay λ and wavelength λ are different symbols that happen to use the same letter.

**Core facts**

Decay and activity

- λ = 0.693 / T½. λ is the decay constant (per unit time). T½ is the half-life. 0.693 is ln(2). T½ and t share one unit.
- A = A0 e^(−λt). A is activity at time t. A0 is the assay activity. The same exponential is N = N0 e^(−λt) for the number of nuclei. A = λN.
- After n half-lives: A = A0 / 2^n, with n = t / T½. n need not be an integer.
- Mean life: τ = 1/λ = 1.443 T½. Permanent-implant total dose = initial dose rate × τ.
- Two removal paths: 1/Te = 1/Tp + 1/Tb. Te is the effective half-life, Tp physical, Tb biologic.
- Transient equilibrium, branching fraction 1: A2/A1 = λ2 / (λ2 − λ1). Subscript 1 is the parent, 2 the daughter.

Photons and HVL transmission

- Photon energy: E (keV) = 12.4 / λ(Å). Here λ is wavelength in angstroms, not the decay constant. c = λν, with ν the frequency.
- Compton scattered photon: E′ = E / [1 + α(1 − cos θ)], with α = E / 0.511 and E in MeV. θ is the photon scatter angle.
- Narrow-beam transmission: I = I0 e^(−μx). I0 is the reading with no absorber, I the transmitted reading, μ the linear attenuation coefficient, x the thickness in μ’s length unit.
- HVL = 0.693 / μ. Through n half-value layers the transmission is (1/2)^n. TVL = 2.30 / μ, which is about 3.32 HVL.

Inverse-square law (ISL)

- I2 = I1 (d1 / d2)^2. I is dose rate or intensity when distance is the only change. d1 and d2 are source-to-point distances in one unit. On an SSD setup the source distance to a point at depth d is SSD + d.

Monitor units

Course calibration for these lines: 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. Factors of 1 may be omitted only when the stem sets them to 1.

- SSD (PDD, no TMR): MU = D / [Ḋ_cal × Sc(rc) × Sp(rd) × (PDD/100) × WF × TF × ISF], and ISF = [SAD / (SSD + dm)]^2.
- SAD (TMR, no PDD): MU = D / [Ḋ_cal × Sc(rc) × Sp(rd) × TMR(d, rd) × WF × TF × (SAD/SPD)^2].
- D is the dose wanted at the point (cGy). Ḋ_cal is the calibration output (cGy/MU). Sc is collimator scatter for the jaw equivalent square rc. Sp is phantom scatter for the treated opening rd. PDD is percent depth dose. TMR is the tissue-maximum ratio at depth d for the field at the point. WF and TF are the wedge factor and tray factor. ISF moves calibration from SAD to the actual dmax. dm is the depth of dmax. SPD is the source-to-point distance. At isocenter, SPD = SAD and (SAD/SPD)^2 = 1.

Gap

- gap = (L1/2)(d/SSD1) + (L2/2)(d/SSD2). gap is the skin separation between the two light-field edges. L1 and L2 are the field lengths on the skin along the match. d is the depth where those geometric edges should meet. SSD1 and SSD2 are the source-to-skin distances.

Equivalent square

- side = 4A/P = 2ab/(a+b). A is the rectangle’s area, P its perimeter, and a and b its sides. The result is the side of the equivalent square. Jaws set Sc. The opening at the patient sets Sp.

Wedge and hinge

- wedge angle = 90° − (hinge angle)/2. The wedge angle is the tilt of a chosen isodose, not the slope of the metal. The hinge angle is the angle between the central axes of a symmetric pair. The wedge factor WF is a measured dose ratio in the MU denominator, not this angle.

Geometric penumbra

- P = s (SSD + d − SDD) / SDD. P is the geometric penumbra at depth d. s is the source size. SSD is source-to-skin distance. d is depth. SDD is source-to-diaphragm distance. Physical penumbra is the 80%–20% width at dmax, a different measurement.

Timer error

- R = Ḋ (t + τ). R is the measured dose. Ḋ is the dose rate while the source is actually in treatment position. t is the timer setting. τ is the timer error (end effect), negative when source transit eats time. The setting that delivers a prescribed dose is t = (dose / Ḋ) − τ.

Mayneord F

- F = [(SSD2 + dm) / (SSD1 + dm)]^2 × [(SSD1 + d) / (SSD2 + d)]^2. Then PDD at SSD2 = PDD at SSD1 × F. SSD1 is the table SSD, SSD2 the treatment SSD, dm the dmax depth, d the point depth. F corrects inverse square inside a PDD only. Do not apply it to TMR.

BED and EQD2

- BED = D [1 + d / (α/β)], with D = n × d. BED is the biologically effective dose. D is total physical dose, n the number of fractions, d the dose per fraction, α/β the tissue parameter (about 3 Gy late, about 10 Gy early or tumor, unless the stem states another value).
- EQD2 = D (d + α/β) / (2 + α/β) = BED / [1 + 2/(α/β)]. EQD2 is the total dose in 2 Gy fractions that matches that BED. Add EQD2 values only when they share one α/β.

TG-43 dose rate

- Ḋ(r, θ) = Sk × Λ × [G(r, θ) / G(r0, θ0)] × g(r) × F(r, θ). Ḋ is the dose rate in water at distance r and angle θ. Sk is air-kerma strength (1 U = 1 µGy m²/h). Λ is the dose-rate constant. G is the geometry function (1/r² for a point source). G(r0, θ0) is G at the reference point, usually 1 cm on the transverse axis. g(r) is the radial dose function. F(r, θ) is the anisotropy function.

Exposure rate

- exposure rate = Γ × A / d². Γ is the specific gamma-ray constant, A the activity, d the distance. If Γ is in R cm²/(mCi h), then A is in mCi, d is in cm, and the rate is in R/h. The recall constants are in module 40.

Primary barrier

- B = P d² / (W U T). B is the transmission the barrier may allow. P is the weekly design limit behind the barrier, in the same dose unit as W. d is the distance from the source to the protected point (meters when W is quoted at 1 m). W is the workload at 1 m. U is the use factor. T is the occupancy factor. Number of tenth-value layers n = log10(1/B), and thickness = n × TVL.

Temperature-pressure correction

- C_TP = [(273.2 + T) / (273.2 + 22)] × (760 / P). C_TP multiplies a vented ion-chamber reading. T is the local temperature in °C. P is the local pressure in mmHg. 22°C and 760 mmHg are the TG-51 reference. A warmer room or a lower pressure makes C_TP greater than 1.

Geometry, CT, dose ratios

- Magnification: M = (source-to-image distance) / (source-to-object distance) = image size / object size.
- Hounsfield: HU = 1000 (μ − μ_water) / μ_water.
- PDD is a percent of dose at dmax for a stated SSD. TAR is dose in phantom over dose in free space at the same point. TMR is dose at depth over dose at dmax for the same field size at the point. TMR = TAR / BSF when BSF is TAR at dmax. Sp = Sc,p / Sc.
- Equivalent depth: d′ = Σ ρ_i t_i.

Units

- 1 Ci = 3.7×10^10 Bq. 1 Gy = 100 cGy = 100 rad. 1 cGy = 1 rad. 1 Sv = 100 rem. 1 R = 2.58×10^−4 C/kg. About 0.876 rad in air per roentgen under charged-particle equilibrium.
- Equivalent dose: H = w_R D. For photons and electrons, w_R = 1, so the number in sievert equals the number in gray.

**Traps**

Using 0.693 × T½ as λ, or τ = 0.693 T½. Omitting 1.443 on a permanent implant. Mixing days and hours in one exponent. Using the wavelength formula with the decay constant. Forgetting the square on an inverse-square ratio. Putting PDD in an SAD line or TMR in an SSD line. Using the full field length in the gap. Taking the arithmetic mean as the equivalent square. Setting the wedge angle equal to half the hinge. Putting SSD in the penumbra denominator. Dropping τ, or applying Mayneord F to a TMR. Adding BED values that used different α/β. Multiplying Sk in U by a per-mCi gamma constant. Forgetting d² in the barrier, or using U = 1 on a primary wall that is not fully used. Inverting C_TP.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, for the external-beam, decay, and shielding relations. AAPM TG-43 for the brachytherapy dose-rate line. AAPM TG-51 for C_TP. NCRP 151 for the primary-barrier symbols. Hall and Giaccia for BED and EQD2. Public MDCB test specifications.

## Studying Tips

**MDCB:** study method for the 2023 blueprint. Not a content objective.

**What the exam expects**

Items are short. The work is choosing the correct relation and not misreading the unit, the geometry, or which quantity is held constant. Recognition of a term is not enough on a calculation stem.

**Core facts**

- For every worked example in modules 3, 6, 8, and 12, cover the arithmetic and repeat it. The tutorial lessons are the ones that chain more than one step.
- Write λ with its unit before substituting t. If T½ is in days, t is in days, or convert both to hours. Do this before touching the exponential.
- On a geometry stem, write source, object, and image in that order and assign the three distances. Then form M.
- On a unit stem, convert one step at a time and write the unit after each step. Stop at the unit the question asks for.
- Keep a single half-life card: Co-60 5.26 y, Cs-137 30 y, Cs-131 9.7 d, Ir-192 73.8 d, I-125 59.4 d, Pd-103 17 d, Au-198 2.7 d, Ra-226 1600 y, I-131 8 d, P-32 14.3 d, Sr-90 28.8 y, Y-90 64 h, Ru-106 374 d, Tc-99m 6 h, F-18 110 min. These are the recall values used in this set.
- When a lesson ends in a quiz heading, that paragraph is the skill list. If you cannot do the skill cold, return to the worked example. Do not move on because the paragraph sounded familiar.
- Domain III is 42%. Isodose, DVH, site planning, and radiobiology dominate the score and live in later modules of this set. Modules 1–16 are the physics and early localization you stop missing before that work.

**Traps**

Rereading prose without substituting numbers. Changing a memorized formula during the exam because the stem “looks similar” to a different ratio (PDD used where TMR belongs, half-life used where mean life belongs).

**Sources**

Public MDCB CMD exam handbook. Weights from the 2023 test specifications matrix.

## How I Passed (A Note from our Founder)

This is an original note on what passing the MDCB CMD exam requires. It is not a note from DoseGrid’s founder, and it is not a personal claim that anyone in particular has passed.

**MDCB:** whole-exam strategy tied to the 2023 blueprint.

**What the exam expects**

A pass depends on executing the standard calculations correctly under a clock, and on knowing the definitions the calculations sit on. The public exam is 155 questions in 3 hours 50 minutes. Most stems are ordinary multiple choice. A few are performance-based plan-evaluation tasks. Nothing in the format rewards long derivation. It rewards the correct formula, the correct substitution, and the correct rejection of the nearby wrong number.

**Core facts**

The score is concentrated in treatment planning (42%), then physics (14%), dose calculation (13%), protection (9%), quality assurance (9%), localization (8%), and brachytherapy (5%). Modules 1–16 are the physics and the first half of localization. They are where decay, magnification, units, machine geometry, CT number, and patient setup get decided. Later planning items assume those decisions are already automatic.

What has to be automatic before a candidate is ready:

- Activity after an arbitrary time, including a non-integer number of half-lives, with λ = 0.693/T½ and with the half-life table above.
- Mean life = 1.443 × half-life, and total dose from complete decay = initial dose rate × mean life.
- Secular equilibrium (daughter activity equals parent) versus transient equilibrium (daughter activity exceeds parent, then follows the parent half-life).
- Photon interaction by energy and Z: coherent, photoelectric (about Z^3/E^3), Compton in tissue at therapy energies, pair production only above 1.022 MeV.
- Magnification = source-to-image distance / source-to-object distance, and true size = image size / M.
- HU = 1000 (μ − μ_water) / μ_water, with air at −1000 and water at 0, and with the CT-to-density table, not the raw HU, used for dose.
- TAR, TMR, TPR, PDD, BSF, Sc, and Sp kept as different ratios. PDD depends on SSD. TAR, TMR, and TPR, with field size at the point, do not.
- Linac components in beam order, what is removed for electrons, and what a flattening-filter-free beam looks like.
- Shifts as a coordinate difference between the reference mark and the isocenter, with the couch direction stated separately so it is not reversed.

The practical standard is this: given numbers you have not seen, you can write the formula, substitute, and land on the same result twice. Familiarity with the paragraph is not that standard.

**Traps**

Confusing time spent with items earned. Reading a decay solution and then, on a fresh stem, multiplying by 0.693 instead of dividing by the half-life. Calling a flattened and an unflattened beam the same shape. Adding a motion margin on top of an ITV that already contains the motion.

**Sources**

Public MDCB exam handbook and 2023 test specifications matrix. Calculation relations as in Khan and Gibbons, *The Physics of Radiation Therapy*.

## How to Navigate this Course

**MDCB:** how this theory set is organized against the public curriculum. Not a content objective.

**What the exam expects**

Nothing on the exam asks how a review course is menu’d. This heading exists so the notes stay aligned with the public lesson list. Use it as the operating rule for these files.

**Core facts**

- One file per module, modules 1–45, under `knowledge/theory/`, with the matching items in `knowledge/questions/`.
- Every public lesson title is a second-level heading, in the same order as the public curriculum list. Quiz lessons are included. A quiz section is a statement of the skills and the traps. It is not a set of items and it is not copied from any course.
- Teaching sections carry the MDCB objective ids from the 2023 matrix (I.1, II.3, and so on).
- Calculation lessons (decay constant, activity, half-life and mean life, the radioactivity tutorial, wavelength and frequency, both magnification lessons, units and the unit-conversion tutorial) walk a numeric problem in this order: given data, formula with symbols, substitution, arithmetic, meaning, usual wrong turn. Repeat that sequence on paper.
- If a numeric constant is not one you are expected to recall, the note says to confirm it in Khan rather than inventing a digit.
- Modules 17–45 use the same file rule and carry registration, IGRT, isodose and DVH, oncology, radiobiology, monitor units, brachytherapy, protection, and QA. Domain III is 42% and is inside this set. A topic that is quiet in an early module is still on the exam when a later module owns it.

Suggested pass through one module: read the objective id, write the formulas, do the worked numbers with the solution covered, then read the quiz paragraph and list which of those skills you could not start. Fix that lesson before the next module.

**Traps**

Skipping a lesson because the title says quiz or tutorial. Those headings are where the skill is named. Studying modules out of order before decay, units, and magnification are reliable, then missing later items that only reuse those three skills.

**Sources**

Public curriculum lesson list used as the heading list. Public MDCB 2023 test specifications for the objective ids.
