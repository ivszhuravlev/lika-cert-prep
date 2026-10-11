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
- Treatment planning is 42% of the test and is not covered in modules 1–16. Physics here is the tool set those later items use.
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

Domain III, Treatment Planning, 42%. Isodose and DVH, site oncology, radiobiology, anatomy, delivery systems, special procedures, planning methods, OAR constraints, computers and DICOM, automation, ICRU volumes, optimization, implanted devices. ICRU volume names are introduced in module 16 because localization uses them. The planning work itself is outside this set.

Domain IV, Dose Calculation Methods, 13%. Algorithms, beam modifiers, special calculations, inhomogeneity, deformable accumulation, dose-grid limits. Module 13 starts inhomogeneity corrections. Monitor units, gaps, and wedges are later.

Domain V, Brachytherapy, 5%. Source characteristics, HDR and LDR, applicators, surveys, NRC and state rules, calculations. Module 3 supplies the half-lives and the permanent-implant total-dose relation those items reuse.

Domain VI, Radiation Protection, 9%. ALARA and dose limits, monitoring, vault barriers, detectors.

Domain VII, Quality Assurance and Standard of Care, 9%. Commissioning, plan and chart checks, measurement devices, record and verify, beam QA, AAMD scope, incident reporting, deliverability, sim and machine QA.

**Traps**

Memorizing the percentages and missing which objective a stem belongs to. A Hounsfield-unit item is I.9. A shift from tattoos to isocenter is II.7. A half-life used to correct a source activity is I.7 and often V.1 at the same time. The arithmetic is the same.

**Sources**

Public MDCB CMD Test Specifications Matrix, 2023 Job Task Analysis. Public CMD exam handbook.

## MDCB Formula Sheet

**MDCB:** I.6, I.7, I.9, I.10. Working formulas for modules 2–16. This is not a reproduction of a printed card.

**What the exam expects**

You may be given constants in the stem. You are still expected to know which formula applies, what each symbol means, and which time or distance unit matches the constant. The public handbook states what is supplied at the current exam. Read that handbook for the live sheet. The relations below are the ones these modules require you to execute. Symbols are defined again inside the lesson that uses them.

**Core facts**

Decay and activity

- Decay constant: λ = ln(2) / T½ = 0.693 / T½. λ carries 1/time. T½ and t must share one unit.
- Activity and atoms: A = A0 exp(−λt). N = N0 exp(−λt). A = λN.
- After n half-lives: A = A0 / 2^n. n = t / T½. n does not have to be an integer.
- Mean life: τ = 1/λ = 1.443 T½.
- Complete decay, as in a permanent implant: total dose = initial dose rate × τ = initial dose rate × 1.443 × T½.
- Physical and biological removal: 1/Te = 1/Tp + 1/Tb.
- Transient equilibrium activity ratio, branching fraction 1: A2/A1 = λ2 / (λ2 − λ1).

Photons

- E in keV and λ in angstroms: E = 12.4 / λ. Speed of light: c = λν.
- Compton scattered photon: E′ = E / [1 + α(1 − cos θ)], with α = E / 0.511 and E in MeV.
- Narrow-beam transmission: I = I0 exp(−μx). HVL = 0.693 / μ. TVL = 2.30 / μ.

Geometry, CT, dose ratios

- Magnification: M = (source-to-image distance) / (source-to-object distance) = image size / object size.
- Hounsfield: HU = 1000 (μ − μ_water) / μ_water.
- Inverse square: dose rate scales as 1/r^2.
- PDD is a percent of dose at dmax for a stated SSD. TAR is dose in phantom over dose in free space at the same point. TMR is dose at depth over dose at dmax for the same field size at the point. TMR = TAR / BSF when BSF is TAR at dmax. Sp = Sc,p / Sc.
- Mayneord factor (inverse square only), SSD1 to SSD2:

F = [(SSD2 + dmax) / (SSD1 + dmax)]^2 × [(SSD1 + d) / (SSD2 + d)]^2

- Equivalent depth: d′ = Σ ρ_i t_i.

Units

- 1 Ci = 3.7×10^10 Bq. 1 Gy = 100 cGy = 100 rad. 1 cGy = 1 rad. 1 Sv = 100 rem. 1 R = 2.58×10^−4 C/kg. About 0.876 rad in air per roentgen under charged-particle equilibrium.
- Equivalent dose: H = w_R D. For photons and electrons, w_R = 1, so the number in sievert equals the number in gray.

**Traps**

Using 0.693 × T½ as λ. Using τ = 0.693 T½. Multiplying a permanent-implant dose rate by the half-life and omitting 1.443. Mixing days and hours inside one exponent. Inverting magnification. Treating 1 Gy as 1 rad.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public MDCB test specifications, objective I.10.

## Studying Tips

**MDCB:** study method for the 2023 blueprint. Not a content objective.

**What the exam expects**

Items are short. The work is choosing the correct relation and not misreading the unit, the geometry, or which quantity is held constant. Recognition of a term is not enough on a calculation stem.

**Core facts**

- For every worked example in modules 3, 6, 8, and 12, cover the arithmetic and repeat it. The tutorial lessons are the ones that chain more than one step.
- Write λ with its unit before substituting t. If T½ is in days, t is in days, or convert both to hours. Do this before touching the exponential.
- On a geometry stem, write source, object, and image in that order and assign the three distances. Then form M.
- On a unit stem, convert one step at a time and write the unit after each step. Stop at the unit the question asks for.
- Keep a single half-life card: Co-60 5.26 y, Cs-137 30 y, Ir-192 73.8 d, I-125 59.4 d, Pd-103 17 d, Au-198 2.7 d, Ra-226 1600 y, I-131 8 d, P-32 14.3 d, Sr-90 28.8 y, Y-90 64 h, Tc-99m 6 h, F-18 110 min. These are the recall values used in this set.
- When a lesson ends in a quiz heading, that paragraph is the skill list. If you cannot do the skill cold, return to the worked example. Do not move on because the paragraph sounded familiar.
- Domain III is 42%. After these sixteen modules, isodose, DVH, site planning, and radiobiology still dominate the score. Modules 1–16 are the part you stop missing.

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

- One file per module, modules 1–16 only, under `knowledge/theory/`.
- Every public lesson title is a second-level heading, in the same order as the public curriculum list. Quiz lessons are included. A quiz section is a statement of the skills and the traps. It is not a set of items and it is not copied from any course.
- Teaching sections carry the MDCB objective ids from the 2023 matrix (I.1, II.3, and so on).
- Calculation lessons (decay constant, activity, half-life and mean life, the radioactivity tutorial, wavelength and frequency, both magnification lessons, units and the unit-conversion tutorial) walk a numeric problem in this order: given data, formula with symbols, substitution, arithmetic, meaning, usual wrong turn. Repeat that sequence on paper.
- If a numeric constant is not one you are expected to recall, the note says to confirm it in Khan rather than inventing a digit.
- Modules 17 onward (registration, IGRT, isodose and DVH, oncology, radiobiology, MU calculations, brachytherapy planning, protection, QA) are outside this set. Do not treat silence here as an omission from the exam. Domain III alone is 42%.

Suggested pass through one module: read the objective id, write the formulas, do the worked numbers with the solution covered, then read the quiz paragraph and list which of those skills you could not start. Fix that lesson before the next module.

**Traps**

Skipping a lesson because the title says quiz or tutorial. Those headings are where the skill is named. Studying modules out of order before decay, units, and magnification are reliable, then missing later items that only reuse those three skills.

**Sources**

Public curriculum lesson list used as the heading list. Public MDCB 2023 test specifications for the objective ids.
