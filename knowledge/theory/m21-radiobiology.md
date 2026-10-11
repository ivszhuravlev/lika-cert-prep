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
- **G1** length varies widely. Early G1 is relatively sensitive; a long G1 holds many cells in a more resistant state.
- **G0** cells are out of cycle until they are recruited.

The four Rs of fractionation:

- **Repair** of sublethal damage between fractions. This is the shoulder. An interval of about 6 hours is the common teaching assumption for substantial repair when a twice-daily schedule is planned. The interval a protocol actually requires is written in that protocol. Confirm it there (head-and-neck BID, total-body irradiation).
- **Repopulation**: surviving cells divide. A gap in treatment gives the tumor time to repopulate. Head and neck cancers are the classic place this hurts, especially after the first few weeks. The basic EQD2 formula does not subtract repopulation. Two schedules with the same EQD2 and very different overall times are not the same biological treatment.
- **Redistribution** (reassortment): cells that survive a fraction were enriched in resistant phases. Given time, they move into sensitive phases before the next fraction.
- **Reoxygenation**: hypoxic cells that survive become better oxygenated as the tumor shrinks and blood flow reaches them. This is a reason fractionation helps kill tumors that started hypoxic.

The oxygen enhancement ratio is the dose required under hypoxia divided by the dose required in air for the same effect. For photons it is about 2.5 to 3. High-LET radiation has an OER closer to 1, because the damage depends less on oxygen.

LET is energy deposited per unit track length. As LET rises, RBE rises, the shoulder shrinks, and the OER falls. Past a peak in LET the RBE falls again because the energy is wasted in overkill of cells that are already dead. Photons and clinical protons sit on the low-LET side. Neutrons sit higher.

Serial and parallel organs are a planning translation of this biology. A serial organ (cord, brainstem, optic pathway) loses function when a small segment is destroyed, so the high-dose end of the DVH dominates. A parallel organ (lung, liver, kidney, parotid) loses function in proportion to the subunit killed, so mean dose and volume dominate. The number you apply is still the one in QUANTEC, TG-101, or the protocol.

**Traps**

- Answering “late S” as the most sensitive phase. Late S is the most resistant. M is the most sensitive.
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
