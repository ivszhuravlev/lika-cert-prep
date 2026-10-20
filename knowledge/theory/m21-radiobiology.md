# Module 21. Radiobiology

The exam uses the linear-quadratic model, the cell cycle, and a conversion between fractionation schemes. α/β values and doses in the examples are the standard teaching numbers, not a prescription for a patient.

## Cell Survival Curve

**MDCB objectives:** III.3

**What the exam expects**

You can sketch the idea of a cell-survival curve, write the linear-quadratic surviving fraction, and say what the shoulder means. You can define D0, Dq, and the extrapolation number well enough to recognize them in a stem. You can connect a wider shoulder with sensitivity to fractionation, and a straight steep curve with high-LET radiation.

**Core facts**

Surviving fraction is plotted on a log scale against dose on a linear scale. For low-LET radiation (photons, clinical protons) the curve has a shoulder at low dose and then bends downward. The shoulder is accumulation and repair of sublethal damage. Split the dose, leave time for repair, and more cells survive than if the same total dose is given at once.

The linear-quadratic model:

S = exp(−αD − βD²)

α is the linear, single-track coefficient. β is the quadratic coefficient, from interaction of damage from separate tracks. Their ratio α/β, in gray, is the dose at which the linear and quadratic contributions to killing are equal. A large α/β means the linear term dominates and fractionation matters less. A small α/β means the quadratic term matters and dose per fraction matters a lot.

Late-responding tissues are taught with α/β ≈ 3 Gy. Early-responding tissues and most tumors are taught with α/β ≈ 10 Gy. Prostate cancer is the usual exception, often modeled near 1.5 Gy. Use the value in the stem. If the stem is silent, state which conventional value you used.

High-LET radiation (neutrons, alpha particles, carbon ions) produces a steeper curve with little shoulder. There is less sublethal damage to repair, less sparing from fractionation, and an oxygen enhancement ratio closer to 1. Clinical protons are low LET with a generic RBE of 1.1, not a high-LET particle. RBE is the dose of a reference radiation divided by the dose of the test radiation that produces the same effect. It depends on the endpoint, the dose, and the LET. It is not a single constant of nature, except where a report tells you to use one. For protons that report value is 1.1 (ICRU 78).

Older curve language still shows up:

- **D0**: the dose that reduces survival to 37% (1/e) along the straight logarithmic portion.
- **Dq**: the quasithreshold dose, a measure of shoulder width.
- **n**: the extrapolation number, where that straight portion would hit the survival axis at zero dose.

A larger shoulder means a larger Dq and more repair between fractions.

**Formulas and a worked survival**

These α and β values are a teaching pair with α/β = 10 Gy. They are not a measured tumor.

α = 0.30 Gy⁻¹, β = 0.03 Gy⁻².

One fraction of 2 Gy:

αD = 0.30 × 2 = 0.60

βD² = 0.03 × 4 = 0.12

αD + βD² = 0.72

S = exp(−0.72) = 0.49

Two fractions of 2 Gy with full repair between them (each fraction contributes its own αD + βD², and the quadratic term does not cross the gap):

S = 0.49 × 0.49 = 0.24

The same 4 Gy in a single fraction:

αD = 0.30 × 4 = 1.20

βD² = 0.03 × 16 = 0.48

Sum = 1.68

S = exp(−1.68) = 0.19

More cells survive 2 Gy + 2 Gy than survive 4 Gy at once (0.24 versus 0.19) because the βD² term punishes the large single dose. That is the shoulder, and it is why fractionation spares tissues with a low α/β even more than this α/β = 10 example.

**Traps**

- Using α/β = 10 for a late-cord or late-heart question by reflex. Late tissue in these notes is ≈ 3 Gy unless the stem says otherwise.
- Using α/β = 3 for a generic tumor-control question. Generic tumor is ≈ 10 Gy. Prostate is the low exception.
- Pasting the proton RBE of 1.1 onto neutrons.
- Treating D0 as a total prescription dose. D0 is a slope parameter on a survival curve.

**Sources**

- Hall and Giaccia, *Radiobiology for the Radiologist*, for the linear-quadratic curve, OER, and RBE
- ICRU 78, for the clinical proton RBE of 1.1

## Cell Cycle

**MDCB objectives:** III.3

**What the exam expects**

You can order the cycle and name the most sensitive and most resistant phases. You can list the four Rs and say what each one does to a fractionated course. You can define LET, RBE, and the oxygen enhancement ratio at the level of a recognition question.

**Core facts**

The cycle is G1, S, G2, and M, plus G0 for cells that have left the cycle.

- **M**, mitosis, is the most sensitive phase. Late **G2** is sensitive with it.
- **Late S** is the most resistant phase.
- **G1** length varies widely. Early G1 is relatively resistant. Sensitivity rises toward the end of a long G1. A long G1 therefore holds many cells in that resistant early stretch, not in a sensitive one.
- **G0** cells are out of cycle until they are recruited.

The four Rs of fractionation:

- **Repair** of sublethal damage between fractions. This is the shoulder. An interval of about 6 hours is the common teaching assumption for substantial repair when a twice-daily schedule is planned. The interval a protocol actually requires is written in that protocol. Confirm it there (head-and-neck BID, total-body irradiation).
- **Repopulation**: surviving cells divide. A gap in treatment gives the tumor time to repopulate. Head and neck cancers are the classic place this hurts, especially after the first few weeks. The basic EQD2 formula does not subtract repopulation. Two schedules with the same EQD2 and very different overall times are not the same biological treatment.
- **Redistribution** (reassortment): cells that survive a fraction were enriched in resistant phases. Given time, they move into sensitive phases before the next fraction.
- **Reoxygenation**: hypoxic cells that survive become better oxygenated as the tumor shrinks and blood flow reaches them. This is a reason fractionation helps kill tumors that started hypoxic.

The oxygen enhancement ratio is the dose required under hypoxia divided by the dose required in air for the same effect. For photons it is about 2.5 to 3. High-LET radiation has an OER closer to 1, because the damage depends less on oxygen.

LET is energy deposited per unit track length. As LET rises, RBE rises, the shoulder shrinks, and the OER falls. Past a peak in LET the RBE falls again because the energy is wasted in overkill of cells that are already dead. Photons and clinical protons sit on the low-LET side. Neutrons sit higher.

Serial and parallel organs are a planning translation of this biology. A serial organ (cord, brainstem, optic pathway) loses function when a small segment is destroyed, so the high-dose end of the DVH dominates. A parallel organ (lung, liver, kidney, parotid) loses function in proportion to the subunit killed, so mean dose and volume dominate. The number you apply is still the one in QUANTEC, TG-101, or the protocol.

The gestational window of highest risk for radiation-related cognitive injury is about 8-15 weeks, not 0-7 weeks and not after 25 weeks.

**Traps**

- Answering “late S” as the most sensitive phase. Late S is the most resistant. M is the most sensitive.
- Calling early G1 the sensitive part of G1. Early G1 is resistant. Sensitivity rises late in G1.
- Listing repopulation as a reason to insert an unplanned break.
- Assuming the plain EQD2 has already accounted for a two-week delay. It has not.
- Treating all normal tissues as serial and quoting only a max dose for lung or liver.

**Sources**

- Hall and Giaccia, for cycle sensitivity, the four Rs, OER, and LET
- QUANTEC, for the serial-versus-parallel organ metrics at conventional fractionation. Confirm numbers in the report.

## BEDs

**MDCB objectives:** III.3

**What the exam expects**

You can compute BED and EQD2 from total dose, dose per fraction, and α/β, and you can show the substitution. You use ≈ 3 Gy for late effects and ≈ 10 Gy for early effects and generic tumors, and you can switch to a stem-specified value such as 1.5 Gy for prostate. You can rank two palliative schedules, or a hypofractionated course against 2 Gy fractions, without calling unequal EQD2s the same treatment.

**Core facts**

With n fractions of dose d, total dose D = n × d.

Biologically effective dose:

BED = n d (1 + d / (α/β)) = D (1 + d / (α/β))

Equivalent dose in 2 Gy fractions:

EQD2 = D (d + α/β) / (2 + α/β)

These two are the same model. The bridge is

EQD2 = BED / (1 + 2 / (α/β))

because a 2 Gy fraction has BED per gray of (1 + 2 / (α/β)).

Assumptions inside the basic formula: full repair between fractions, the same dose per fraction, and no subtraction for repopulation. At very large dose per fraction (stereotactic regimens) the quadratic model is being used beyond the range where it was built. Compute it when the question asks, and judge the plan by TG-101 and the protocol.

Add EQD2 values for sequential courses only when they share the same α/β. External beam and brachytherapy are added that way for cervix. You cannot add a BED computed at α/β = 3 to a BED computed at α/β = 10.

**Formulas and worked examples**

**1. Identity check.** 60 Gy in 20 fractions, so d = 3 Gy. Late tissue, α/β = 3.

BED = 20 × 3 × (1 + 3/3) = 60 × (1 + 1) = 60 × 2 = 120 Gy

EQD2 = 60 × (3 + 3) / (2 + 3) = 60 × 6 / 5 = 72 Gy

Bridge: 1 + 2 / (α/β) = 1 + 2/3 = 5/3

EQD2 = 120 / (5/3) = 120 × 3/5 = 72 Gy

Same course, generic tumor, α/β = 10.

BED = 60 × (1 + 3/10) = 60 × 1.3 = 78 Gy

EQD2 = 60 × (3 + 10) / (2 + 10) = 60 × 13 / 12 = 65 Gy

Bridge: 78 / (1 + 2/10) = 78 / 1.2 = 65 Gy

Hypofractionation of 3 Gy raises the late EQD2 (72 Gy) more than the generic-tumor EQD2 (65 Gy). That is the late-tissue cost of a larger fraction.

**2. Prostate exception.** The same 60 Gy in 20 fractions with α/β = 1.5.

EQD2 = 60 × (3 + 1.5) / (2 + 1.5) = 60 × 4.5 / 3.5 = 60 × 9/7 = 77.1 Gy

BED = 60 × (1 + 3/1.5) = 60 × (1 + 2) = 180 Gy

With the low α/β, 60 Gy in 20 fractions lands in the high 70s EQD2, which is why it is compared with a conventional high-70s prostate course. With α/β = 10 it was only 65 Gy. Name the α/β in the answer.

**3. Whole brain, 30 Gy in 10 fractions, d = 3 Gy.**

Late, α/β = 3: EQD2 = 30 × (3 + 3) / 5 = 30 × 6/5 = 36 Gy

Tumor, α/β = 10: EQD2 = 30 × (3 + 10) / 12 = 30 × 13/12 = 32.5 Gy

Thirty gray in ten fractions is hotter for late effects than 30 Gy in 2 Gy fractions (which would be 30 Gy EQD2 by definition). It is still a palliative brain dose, not 60 Gy GBM treatment. GBM at 60 Gy in 30 fractions is already 2 Gy per fraction, so EQD2 = 60 Gy for every α/β.

**4. Three bone-pain schedules, late α/β = 3.**

8 Gy × 1: EQD2 = 8 × (8 + 3) / 5 = 8 × 11/5 = 17.6 Gy

BED = 8 × (1 + 8/3) = 8 × 11/3 = 29.3 Gy

20 Gy in 5, d = 4: EQD2 = 20 × (4 + 3) / 5 = 20 × 7/5 = 28 Gy

30 Gy in 10, d = 3: EQD2 = 30 × 6/5 = 36 Gy

Same α/β = 10, for comparison:

8 Gy × 1: EQD2 = 8 × (8 + 10) / 12 = 8 × 18/12 = 12 Gy

20 Gy in 5: EQD2 = 20 × (4 + 10) / 12 = 20 × 14/12 = 23.3 Gy

30 Gy in 10: EQD2 = 32.5 Gy, from example 3

For late tissue the order of increasing EQD2 is 8/1, then 20/5, then 30/10. All three are accepted palliative schedules because pain relief, not a curative EQD2, is the goal. They are not interchangeable when prior cord dose is in the field.

**5. Rectum, long course versus short course.**

50.4 Gy in 28 fractions, d = 1.8 Gy, α/β = 10:

EQD2 = 50.4 × (1.8 + 10) / 12 = 50.4 × 11.8 / 12 = 49.6 Gy

α/β = 3:

EQD2 = 50.4 × (1.8 + 3) / 5 = 50.4 × 4.8 / 5 = 48.4 Gy

25 Gy in 5 fractions, d = 5 Gy, α/β = 10:

EQD2 = 25 × (5 + 10) / 12 = 25 × 15/12 = 31.3 Gy

α/β = 3:

EQD2 = 25 × (5 + 3) / 5 = 25 × 8/5 = 40 Gy

Long course is about 50 Gy EQD2. Short course is a lower tumor EQD2 on the α/β = 10 model and about 40 Gy EQD2 for late effects. Recognize both. Do not call them equal.

**6. Breast, 40 Gy in 15 fractions.** d = 40/15 = 8/3 Gy.

α/β = 3: EQD2 = 40 × (8/3 + 3) / 5 = 40 × (17/3) / 5 = 40 × 17 / 15 = 45.3 Gy

α/β = 10: EQD2 = 40 × (8/3 + 10) / 12 = 40 × (38/3) / 12 = 40 × 38 / 36 = 42.2 Gy

Breast tumor is sometimes modeled with α/β near 4 rather than 10.

EQD2 = 40 × (8/3 + 4) / (2 + 4) = 40 × (20/3) / 6 = 40 × 20 / 18 = 44.4 Gy

The generic exam values remain 3 and 10 unless the stem specifies another. 42.5 Gy in 16 is the other hypofractionated whole-breast regimen to recognize; convert it with the same formula if a stem asks.

**7. Cervix, external beam plus a worked HDR illustration.** Not a prescription. Confirm the schedule and the OAR limits in ABS guidance or EMBRACE.

External beam 45 Gy in 25 fractions, d = 1.8 Gy, α/β = 10:

EQD2 = 45 × (1.8 + 10) / 12 = 45 × 11.8 / 12 = 44.3 Gy

Illustrative HDR, 7 Gy × 4, D = 28 Gy, α/β = 10:

EQD2 = 28 × (7 + 10) / 12 = 28 × 17 / 12 = 39.7 Gy

Sum, tumor α/β = 10: 44.3 + 39.7 = 84.0 Gy EQD2

The same physical doses at late α/β = 3:

External beam: 45 × (1.8 + 3) / 5 = 45 × 4.8 / 5 = 43.2 Gy

HDR: 28 × (7 + 3) / 5 = 28 × 2 = 56 Gy

Sum, late: 43.2 + 56 = 99.2 Gy EQD2

The HDR physical dose of 28 Gy adds about 40 Gy EQD2 to the tumor tally and 56 Gy EQD2 to the late tally. Large fractions cost late-responding organs more. That is why rectum, sigmoid, and bladder are tracked as EQD2 and why the limits have to be read from the protocol rather than guessed. Other HDR fractionations (for example 5.5 Gy × 5 or 6 Gy × 5) are in clinical use. Convert the one in the stem. Do not memorize a single brachytherapy prescription as the only correct one.

**8. A stereotactic conversion, with the model’s limit stated.** 54 Gy in 3 fractions, d = 18 Gy, α/β = 10:

BED = 54 × (1 + 18/10) = 54 × 2.8 = 151.2 Gy

EQD2 = 54 × (18 + 10) / 12 = 54 × 28 / 12 = 126 Gy

α/β = 3:

BED = 54 × (1 + 18/3) = 54 × 7 = 378 Gy

EQD2 = 54 × (18 + 3) / 5 = 54 × 21 / 5 = 226.8 Gy

This is the arithmetic the exam wants if it asks for BED. It is a poor reason to apply a conventional QUANTEC cord limit as if the patient had received 226.8 Gy in 2 Gy fractions. Stereotactic limits are in TG-101 and the protocol. Confirm them there.

**Traps**

- Forgetting the square on the fraction size. BED uses d / (α/β), and the dose per fraction appears again because D = n d. Dropping d and using only total dose erases fractionation.
- Adding EQD2 values computed at different α/β.
- Treating EQD2 as a physical dose the machine should deliver tomorrow. It is a common currency for comparing schedules.
- Ignoring overall time and unplanned gaps.
- Using one α/β for a comparison the stem split into “late complication” and “tumor control.”
- Trusting the linear-quadratic number alone at SBRT doses.

**Sources**

- Hall and Giaccia, for the derivation and the meaning of α/β
- ICRU 83, for reporting the physical dose you then convert
- ABS guidance and EMBRACE, for cervix EQD2 goals and OAR limits. Confirm the numbers in those sources.
- AAPM TG-101, for stereotactic constraints when the BED is very large

## Radiobiology Quiz

**MDCB objectives:** III.3

**Skills this quiz trains**

- Write S = exp(−αD − βD²) and explain the shoulder with a split-dose comparison.
- Place peak sensitivity in M (and late G2) and peak resistance in late S.
- List repair, repopulation, redistribution, and reoxygenation.
- Compute BED and EQD2 with the substitution written out.
- Use α/β ≈ 3 for late effects, ≈ 10 for early effects and generic tumors, and the stem’s value when it gives one.
- Rank 8 Gy × 1, 20 Gy in 5, and 30 Gy in 10 by late EQD2, and convert 60 Gy in 20 at two different α/β values.
- Add external-beam and brachytherapy EQD2 only at a shared α/β.

**Traps**

- α/β of 10 used for a late effect, or 3 used for a generic tumor, or 10 used for prostate when the stem said 1.5.
- BED and EQD2 treated as unrelated formulas.
- A treatment gap ignored because EQD2 matched.
- An SBRT BED used to pick a conventional QUANTEC limit.
- RBE, LET, and OER mixed: protons 1.1 and low LET; OER about 2.5–3 for photons; OER closer to 1 at high LET.

**Check yourself**

A regimen is 45 Gy in 25 fractions. Convert to EQD2 at α/β = 10 and at α/β = 3.

Walk-through: d = 45/25 = 1.8 Gy.

α/β = 10: EQD2 = 45 × (1.8 + 10) / 12 = 45 × 11.8 / 12 = 44.3 Gy.

α/β = 3: EQD2 = 45 × (1.8 + 3) / 5 = 45 × 4.8 / 5 = 43.2 Gy.

Fractions of 1.8 Gy sit slightly below the 2 Gy reference, so both EQD2 values sit slightly below 45 Gy. The gap between them is small. The gap opens wide once the fraction size is 5–7 Gy, as in the HDR example above.

## Radiosensitivity and Cell Biology

**Objectives:** III.3

The law of Bergonié and Tribondeau, from 1906, states that cells are most radiosensitive when they divide often, when they have a long dividing future ahead of them, and when they are undifferentiated in form and function. Stem cells of the bone marrow, the intestinal crypts, the basal layer of the skin, and the germinal epithelium of the testis fit all three conditions and respond early. Neurons and mature muscle cells fit none and are among the most resistant. The law has a famous exception: the mature lymphocyte does not divide and is fully differentiated, yet it is the most radiosensitive cell in the body. Lymphocytes die in interphase by apoptosis within hours of a few tenths of a gray, so the falling lymphocyte count in the first one to two days is the earliest laboratory sign of a whole-body exposure. Oocytes are a second exception.

The mitotic index is the fraction of cells in a population that are in mitosis at one moment. A high mitotic index means rapid turnover. Tissues with rapid turnover, such as mucosa, skin, marrow, and gut, express radiation injury within days to weeks, so they are early-responding tissues with a high α/β. Tissues with slow turnover, such as spinal cord, kidney, and lung parenchyma, express injury months to years later, so they are late-responding tissues with a low α/β. The timing of the response follows the turnover rate of the tissue, not the dose.

A typical cultured mammalian cell completes the cycle in about 10 to 24 hours. Mitosis is the shortest phase, about 1 hour. S phase, DNA synthesis, lasts about 6 to 8 hours. G2 lasts about 2 to 4 hours. G1 is the most variable phase, from an hour or two to many hours, and it is the length of G1 that makes one cell type cycle faster than another. Sensitivity follows the phase: cells in M and late G2 are most sensitive, cells in late S are most resistant, and G1 is intermediate, with early G1 relatively resistant when G1 is long. A population irradiated once is therefore enriched in late S survivors, and the redistribution of those survivors into sensitive phases before the next fraction is one of the four Rs.

Radiation damages DNA by two routes. In direct action the charged particle ionizes an atom of the DNA itself. In indirect action the particle ionizes a nearby water molecule, producing free radicals, chiefly the hydroxyl radical, that diffuse a few nanometers and attack the DNA. For low-LET radiation such as x-rays and electrons about two thirds of the DNA damage is indirect and one third is direct. For high-LET radiation such as alpha particles and neutrons the ionization density is so high that direct action dominates. The radical lifetime is on the order of microseconds, and molecular oxygen reacts with the damaged site and makes the damage permanent; this oxygen fixation is the mechanism behind the oxygen enhancement ratio, and it is why the ratio shrinks toward 1 at high LET where direct action does not need oxygen. Sulfhydryl compounds such as amifostine protect by scavenging those radicals. The lethal lesion is the double-strand break. One gray of low-LET radiation produces on the order of a thousand single-strand breaks and about forty double-strand breaks per cell; the single-strand breaks are repaired almost completely, and it is the misrepaired or unrepaired double-strand breaks that produce the chromosome aberrations that kill cells.

Most irradiated mammalian cells die a mitotic death, also called reproductive or clonogenic death. The cell survives the exposure, often completes one or more divisions, and then dies when a dicentric chromosome, a ring, or an acentric fragment makes a later mitosis impossible. This is why the survival curve is measured by the ability to form a colony and why tumors shrink over weeks rather than hours. Apoptosis, programmed cell death, is a different mode: the cell dies in interphase within hours, without attempting division, through a p53-dependent program. It dominates in lymphocytes, germ cells, salivary gland serous cells, and some lymphomas, and it is the reason lymphoid tumors melt quickly under low doses. Senescence, autophagy, and necrosis are the other recognized modes.

Two low-dose phenomena are named often. The bystander effect is damage expressed in unirradiated cells that neighbor irradiated cells, carried by gap junctions and secreted signals, and it matters at doses below about 1 Gy. The adaptive response is the reduced sensitivity to a later large dose after a small priming dose of a few centigray, attributed to induced repair. Both are laboratory observations that complicate the linear no-threshold model at low dose, but the linear no-threshold model remains the basis of radiation protection.

The D10 is the dose that reduces survival to 10 percent along the exponential part of the survival curve. Because one decade of kill is ln 10 = 2.303 times the natural-log slope, D10 = 2.303 × D0, usually rounded to 2.3 × D0. With D0 = 5 Gy, D10 = 2.3 × 5 = 11.5 Gy per decade of kill; with D0 = 1.5 Gy, D10 = 3.45 Gy. Check: three decades of kill with D0 = 1.5 Gy needs about 3 × 3.45 = 10.4 Gy, and ln(1000) × 1.5 = 6.91 × 1.5 = 10.4 Gy agrees.

## Whole-Body and Fetal Effects

**Objectives:** III.3

The LD50/60 is the acute whole-body dose that kills half of an exposed human population within 60 days. Without medical care the bank uses 3 to 4 Gy. With antibiotics, transfusions, and growth factors it rises to about 6 to 7 Gy. Older texts quote an LD50/30 of 3.5 to 4.5 Gy; the 60-day window is used for humans because marrow death comes later than in rodents. The figure is for a single acute exposure to the whole body; fractionated or partial-body exposures are far better tolerated, which is why 12 Gy of total body irradiation in six fractions is survivable with a marrow transplant.

Acute radiation syndrome unfolds in four stages: a prodromal stage of nausea, vomiting, anorexia, and fatigue that begins within hours; a latent stage of apparent well-being; the manifest illness; and recovery or death. The time to vomiting shortens as dose rises, from a few hours at 1 to 2 Gy to under an hour above about 6 Gy, which makes the time to onset a triage clue. The dose bands used in this bank are the thresholds at which each syndrome dominates. The hematopoietic syndrome begins at about 2 to 3 Gy: the marrow stem cells are killed, the counts fall over 2 to 4 weeks, and death from infection and hemorrhage comes at 3 to 8 weeks if the marrow does not recover. The gastrointestinal syndrome begins at about 5 to 12 Gy: the crypt stem cells are killed, the villi are denuded in about a week, and death from fluid loss, electrolyte imbalance, and sepsis comes in 1 to 2 weeks. The cerebrovascular, or central nervous system, syndrome dominates above about 12 Gy and is certain at tens of gray: vascular damage and cerebral edema cause death within 1 to 2 days. Textbooks quote different upper bounds for each band, and the GI band is sometimes written as 10 to 50 Gy; the bank keeps the lower thresholds above because the exam asks which syndrome a given dose produces, and the latent period shrinks and the survival time shortens as dose rises in every version.

Effects on the conceptus depend on the stage of development. During preimplantation, days 1 to 10 after conception, the response is all or none: the embryo either dies and is resorbed or implants and develops normally, because the few cells present are not yet committed. During organogenesis, days 11 to 42, about weeks 2 to 8, the organs are forming and radiation causes malformations and growth retardation, with a threshold near 100 to 200 mGy. During the fetal period, from day 43 onward, malformations are rare but the brain is still proliferating and migrating; the window of weeks 8 to 15 is the most sensitive for intellectual disability, with a smaller effect at weeks 16 to 25 and growth retardation throughout. Childhood cancer risk is a stochastic effect at any stage. The modern threshold statement is that a fetal dose below 100 mGy is not a justification for terminating a pregnancy, because the deterministic effects above have thresholds at or above that dose and the added cancer risk is small. Occupational limits for a declared pregnant worker, 5 mSv for the gestation and the 0.5 mSv per month guidance, are protection rules in the regulatory module and are not these biological thresholds.

## Therapeutic Ratio and Altered Fractionation

**Objectives:** III.3

The therapeutic ratio compares tumor control with normal tissue damage. Plot tumor control probability and normal tissue complication probability against dose; both are sigmoid curves. The ratio is the separation between them, often written as the dose for a given complication probability divided by the dose for the same tumor control probability, so a ratio above 1 means the tumor is controlled before the normal tissue is injured. Everything in planning aims to widen that gap: fractionation and conformal delivery move the complication curve to the right, while sensitizers, oxygen modifiers, and concurrent chemotherapy move the control curve to the left. A radioprotector that protects tumor as much as normal tissue does not change the ratio.

Hyperfractionation uses more fractions of smaller size, about 1.1 to 1.2 Gy given twice daily, in the same overall time, to reach a higher total dose. The rationale is the difference in α/β. Late-responding tissues have a low α/β and are spared strongly by small fractions; tumors and early-responding tissues have a high α/β and are spared much less. Smaller fractions therefore let the total dose rise without raising late effects, and the extra dose is paid for with more acute mucositis. The RTOG head and neck trial of 81.6 Gy in 68 fractions showed better local control than 70 Gy in 35 with no increase in late toxicity. The interval between the two daily fractions must be at least 6 hours so late tissues complete sublethal damage repair; intervals under 4 to 6 hours increased late effects in early trials. Accelerated fractionation is a different idea: the same total dose in a shorter overall time to beat repopulation. Hypofractionation, fewer and larger fractions, is the opposite of hyperfractionation and suits tumors with a low α/β such as prostate cancer and melanoma. A 1.5 to 3 Gy conventional schedule is not hyperfractionation; the term means fractions smaller than the conventional 1.8 to 2 Gy.

Cumulative cord dose for re-irradiation is tracked in biological units, not by adding physical gray. Convert each course to BED, or to EQD2, at the same cord α/β, which this bank takes as 2 to 3 Gy, and sum. A first course of 45 Gy in 25 fractions at α/β = 3 is BED = 45 × (1 + 1.8/3) = 45 × 1.6 = 72 Gy₃, which is EQD2 = 72 / (1 + 2/3) = 43.2 Gy. A retreatment of 20 Gy in 5 fractions is BED = 20 × (1 + 4/3) = 46.7 Gy₃, which is EQD2 = 46.7 / 1.667 = 28 Gy. The cumulative cord exposure is 118.7 Gy₃, or 71.2 Gy EQD2, not the 65 Gy obtained by adding physical doses. The ceiling the physician accepts is a clinical decision from the re-irradiation literature; published analyses accept cumulative cord EQD2 in the 60s of gray when the interval exceeds 6 months and neither course alone was near tolerance, and they credit partial recovery of cord tolerance with time. The bank's rule is the arithmetic: same α/β, sum in BED or EQD2, and name the ceiling and its source before accepting the plan.

## Cell Cycle Checkpoints, Target Models, and Modifiers

**Objectives:** III.3

Mitosis itself has four named sub-phases. In prophase the chromatin condenses into visible chromosomes, the nuclear envelope breaks down, and the spindle forms. In metaphase the chromosomes line up on the equatorial plate; they are at their most compact here, which is why radiation-induced dicentrics and rings are scored on metaphase spreads in cytogenetic dosimetry. In anaphase the sister chromatids are pulled to opposite poles, and in telophase the nuclear envelopes re-form before cytokinesis divides the cytoplasm. The cycle is policed by checkpoints. The G1/S checkpoint, the restriction point, is p53-dependent: a cell with DNA damage arrests in G1 for repair or apoptosis, and tumors with mutant p53 lose this arrest and carry damage into S. The G2/M checkpoint verifies that replication is complete and the DNA undamaged before mitosis begins; after irradiation cells accumulate here, producing the classic G2 block, a mitotic delay of roughly 1 to 2 hours per gray that is seen even in p53-mutant cells. The spindle assembly checkpoint at the metaphase-to-anaphase transition holds the cell until every kinetochore is attached.

Rubin and Casarett classified cell populations by how they divide and differentiate, which ranks their radiosensitivity. Vegetative intermitotic cells, VIM, divide constantly, are undifferentiated, and are short-lived stem cells: basal cells of the epidermis, intestinal crypt cells, erythroblasts, and type A spermatogonia; they are the most sensitive. Differentiating intermitotic cells, DIM, still divide but are already differentiating: myelocytes and spermatocytes; they are sensitive. Multipotential connective tissue cells, MCT, divide irregularly and are intermediate: endothelial cells, fibroblasts, and mesenchymal cells. Reverting postmitotic cells, RPM, do not normally divide but can be recruited after injury: hepatocytes, renal tubular cells, salivary and pancreatic parenchyma; they are relatively resistant. Fixed postmitotic cells, FPM, never divide and are fully differentiated: neurons, muscle fibers, erythrocytes, and spermatozoa; they are the most resistant. The classification restates Bergonié and Tribondeau at the population level. Note that organ tolerance does not follow the parenchymal class: kidney tubular cells are RPM and resistant as cells, yet the kidney has a low tolerance dose because its vascular and stromal compartments fail.

The multi-target model describes the survival curve with a shoulder followed by a straight exponential tail. Its three parameters are D0, the dose that reduces survival by a factor of e along the tail; n, the extrapolation number, where the extrapolated tail meets the survival axis; and Dq, the quasi-threshold dose, where the extrapolated tail crosses a survival of one. They are linked by Dq = D0 × ln(n), so ln(n) = Dq / D0 and n = e raised to Dq / D0. Worked example: with Dq = 2 Gy and D0 = 1.5 Gy, Dq / D0 = 1.333, and n = e^1.333 = 3.8. Check: 1.5 × ln(3.8) = 1.5 × 1.335 = 2.0 Gy. The reverse direction: with n = 4 and D0 = 1.2 Gy, Dq = 1.2 × ln(4) = 1.2 × 1.386 = 1.66 Gy. The usual slip is to use the base-10 logarithm, which would give 1.2 × 0.602 = 0.72 Gy. Mammalian cells typically have D0 of 1 to 2 Gy, n of 2 to 10, and Dq of 1 to 3 Gy. The model predicts zero initial slope and a perfectly straight tail, whereas the linear-quadratic model bends continuously; the linear-quadratic model fits the clinical dose range of 1 to 8 Gy per fraction better and is the one used for fractionation arithmetic.

DNA is the critical target. The double helix carries two sugar-phosphate backbones joined by base pairs: adenine pairs with thymine through two hydrogen bonds and guanine pairs with cytosine through three, so the sequence on one strand fixes the other. A human diploid cell holds about six billion base pairs. The evidence that the nucleus, not the cytoplasm, is the target comes from microbeam experiments in which irradiating the nucleus kills the cell while the same dose to cytoplasm does not, from the tight correlation between chromosome aberrations and cell death, and from sensitization by halogenated pyrimidines such as bromodeoxyuridine and iododeoxyuridine, which substitute for thymidine in DNA and weaken it against breakage.

The oxygen enhancement ratio falls as linear energy transfer rises. For x-rays, gamma rays, and electrons, low-LET radiation at about 0.2 to 2 keV per micrometer, the OER is 2.5 to 3 for doses above a few gray and somewhat lower at low doses. For fast neutrons, intermediate LET of tens of keV per micrometer, the OER is about 1.6. For alpha particles and heavy ions above about 100 keV per micrometer the OER approaches 1, because the dense direct damage no longer needs oxygen to be fixed. Clinical protons have an RBE of 1.1 and an OER essentially that of photons except in the last millimeters of the Bragg peak. RBE peaks at about 100 keV per micrometer and then declines from overkill.

Chemotherapy modifies the radiation response in both directions. The concurrent radiosensitizers are cisplatin, which forms platinum adducts and inhibits repair of double-strand breaks and is the backbone for head and neck, cervix, lung, and bladder cancer; 5-fluorouracil, a thymidylate synthase inhibitor used with radiation for rectal, anal, esophageal, pancreatic, and head and neck cancers; gemcitabine, a nucleoside analog that depletes deoxynucleotide pools and is so potent a sensitizer that concurrent doses must be cut sharply; and hydroxyurea, a ribonucleotide reductase inhibitor that synchronizes cells at the G1/S boundary and was used historically with cervix and head and neck radiation. Mitomycin C adds hypoxic cell cytotoxicity in anal cancer, taxanes block cells in G2/M, and temozolomide is the sensitizer for glioblastoma. The radioprotector is amifostine, WR-2721, a phosphorothioate prodrug that is dephosphorylated by alkaline phosphatase in the capillaries of normal tissue to the free thiol WR-1065, which scavenges free radicals and donates hydrogen to repair DNA radicals. Tumors take up less of it because they are hypoxic, acidic, and low in alkaline phosphatase. It is given intravenously 15 to 30 minutes before each fraction, it is approved to reduce xerostomia in head and neck radiotherapy and to blunt cisplatin nephrotoxicity, and its side effects are nausea and hypotension. It does not raise tumor control; it widens the therapeutic ratio by protecting normal tissue only.

Several drugs raise the risk of radiation pneumonitis when combined with thoracic irradiation. Bleomycin causes pulmonary fibrosis on its own, so a Hodgkin lymphoma patient who has received ABVD and then mediastinal radiation is at particular risk. Gemcitabine should not be given concurrently with thoracic radiation and is hazardous even when given sequentially within weeks of it. Doxorubicin and actinomycin-D produce recall reactions: inflammation flares in the previously irradiated lung or skin when the drug is given weeks to months after the course. Methotrexate, busulfan, the nitrosoureas, and cyclophosphamide also add to lung toxicity. The planning response is to separate these agents in time from thoracic radiation, to tighten the lung dose constraints, and to warn the patient about cough and dyspnea in the weeks after treatment.

Hyperthermia at 42 to 45 degrees Celsius for 30 to 60 minutes is complementary to radiation because it kills exactly the cells that radiation spares. Heat is most lethal to cells in S phase, which are the most radioresistant phase, and to hypoxic, acidic, and nutrient-deprived cells, which are the radioresistant cells of the tumor cord. Heat also inhibits repair of sublethal and potentially lethal damage, so the combination is synergistic, with a thermal enhancement ratio of about 1.5 to 2 when heat follows radiation within a few hours. Cells develop thermotolerance within hours of a heating and keep it for two to three days, so heat is given once or twice a week rather than daily. Above about 43 degrees each additional degree roughly doubles the rate of cell killing. Clinical uses are superficial chest wall recurrences of breast cancer, cervix cancer, and melanoma, where randomized trials showed better local control with the combination.

A pregnant patient who needs radiotherapy is handled by a fixed workflow from AAPM Task Group 36. First, confirm the pregnancy status and gestational age and decide with the physician whether treatment can be deferred or modified. Second, estimate the fetal dose before any treatment is given: the dose outside the field is the sum of internal patient scatter, which dominates near the field edge and cannot be shielded, collimator and head leakage, and scatter from wedges, trays, and blocks; it is read from TG-36 tables as a function of distance from the field edge, field size, and energy, or measured directly with thermoluminescent dosimeters in a phantom at the fetal position. Third, modify the plan: energy below 10 MV to avoid photoneutrons, no physical wedges or trays, smallest fields and tightest collimation, and beams that do not point toward the fetus. Fourth, build the shield: a lead bridge of 4 to 5 cm, about five half-value layers, supported on a frame over the abdomen rather than on the patient, reduces leakage and head scatter by a factor of about three to four. Fifth, verify with dosimeters on the abdomen during the first fraction. The aim is to keep the total fetal dose well under 0.1 Gy, because 0.1 Gy is the lowest dose at which deterministic effects on the conceptus are considered, and the order matters: estimate first, shield second, verify third, since a shield built before the estimate may be in the wrong place or protect against the wrong component.
