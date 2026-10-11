# Module 3. Radioactivity

Original notes. Half-lives in this module are the values candidates are expected to recall.

## Radioactivity

**MDCB:** I.1, I.7, I.10

**What the exam expects**

You treat radioactivity as a nuclear process with a constant probability per nucleus, independent of chemistry, temperature, and pressure at any level this exam tests. You distinguish activity (decays per time) from the number of atoms left, and you know they fall by the same fraction. You know which emissions change Z and A, because the next lessons compute activity only after the mode is identified.

**Core facts**

An unstable nucleus has a fixed probability of decaying in the next small time interval. That probability does not depend on how long the nucleus has already existed. For a large number of nuclei the result is exponential loss.

Activity A is the number of decays per unit time. It is not the number of particles emitted if one decay produces more than one photon, and it is not dose rate. Dose rate depends on activity, energy per decay, distance, and what the tissue absorbs.

The same exponential that reduces the number of nuclei reduces the activity, because A = λN and λ is constant for that nuclide. After one half-life both N and A are half. The emitted radiation’s energy spectrum does not soften the way an x-ray beam softens. A cobalt source at the end of a half-life is half as active and still emits 1.17 and 1.33 MeV photons.

Specific activity is activity per unit mass. For a carrier-free radionuclide it is proportional to λ, so a shorter half-life means a higher specific activity. That is why an Ir-192 HDR source can be physically small at high activity, and a Cs-137 source of similar activity is larger. Ir-192 is recalled at 73.8 days and Cs-137 at 30 years.

Nothing in ordinary chemical processing restarts a half-life. Eluting a generator separates daughter atoms; it does not change λ of either species.

**Formulas**

A = λN

- A: activity, decays per unit time (Bq if time is in seconds)
- λ: decay constant, per unit time
- N: number of radioactive nuclei of that species present

Specific activity of a pure radionuclide is proportional to λ / (atomic mass). Comparing two pure sources, the activity per gram scales as 1/(T½ × atomic mass).

**Traps**

Reporting remaining atoms as remaining dose without a decay calculation. Treating filtration or a change in chemical compound as a change in half-life. Using exposure rate and activity as if they were the same number.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.1, I.7, I.10.

## Decay Constant

**MDCB:** I.7, I.10

**What the exam expects**

Given a half-life, you compute λ in a stated time unit and use it in an exponential. You do not confuse λ with the half-life, with 0.693 itself, or with mean life.

**Core facts**

λ is the fraction of remaining nuclei that decay per unit time, for a constant fractional rate. A large λ means a short half-life. λ and T½ are reciprocals scaled by ln(2), not by 1.

ln(2) = 0.693 is the value used on this exam. Mean life is the reciprocal of λ, so mean life is longer than half-life: τ = 1/λ = T½ / 0.693 = 1.443 T½. The factor 1.443 belongs to mean life. The factor 0.693 belongs in the numerator of λ.

**Formulas**

λ = ln(2) / T½ = 0.693 / T½

- λ: decay constant
- T½: half-life
- ln(2): 0.693 on this exam

τ = 1/λ = 1.443 T½

- τ: mean life

**Worked example**

Given: Co-60 half-life is the recall value 5.26 years. Find λ per year and λ per month.

Formula: λ = 0.693 / T½

Substitution per year: λ = 0.693 / 5.26

Arithmetic: 5.26 × 0.1317 = 0.6927, remainder 0.0003, so λ = 0.13175 per year.

Substitution per month: T½ = 5.26 × 12 = 63.12 months. λ = 0.693 / 63.12 = 0.01098 per month.

Meaning: about 1.1% of the remaining Co-60 atoms decay each month. The output of a teletherapy source falls by that fraction per month if nothing else changes. The precise one-month remaining fraction is exp(−0.01098) = 0.9891, which is a 1.09% loss, not a flat 0.01098 subtracted from 1 in a sloppy way. For one month the two are almost the same (0.9890 versus 0.9890). Over many months you must use the exponential, not 1.09% × (number of months) subtracted from 1.

Check of the monthly loss: exp(−0.01098) = 0.9891. Activity remaining after one month is 98.91% of the starting activity.

Usual wrong turn: λ = 0.693 × 5.26 = 3.65 per year. That number is larger than 1 and would predict that the source vanishes in a fraction of a year. The other common miss is to use λ = 1/5.26 = 0.190 per year, which drops the 0.693 and makes every later activity too low.

**Traps**

Unit of λ left blank, then multiplied by a time in the wrong unit. Using 0.693 as λ for every nuclide. Rounding 0.693 to 0.7 inside a long decay and then treating the result as exact; for exam arithmetic, 0.693 is the constant to use.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*.

## Activity

**MDCB:** I.7, I.10, V.1

**What the exam expects**

You compute activity at a later time from a stated assay, and you convert that activity between curies and becquerels when the stem asks. You keep activity distinct from dose rate. Two sources with the same activity can have very different dose rates if the energy per decay differs.

**Core facts**

The SI unit of activity is the becquerel: 1 Bq = 1 decay per second. The older unit is the curie: 1 Ci = 3.7×10^10 Bq exactly by definition. Useful shortcuts: 1 mCi = 37 MBq, and 1 Ci = 37 GBq.

Activity falls as A = A0 exp(−λt) whether or not anyone is in the room. An assay has a date and a time. HDR and implant items are often a decay from the assay to the treatment time, nothing more.

A = λN connects the macroscopic activity to the atom count. A small λ (long half-life) means many atoms are required to produce 1 Bq.

**Formulas**

A = A0 exp(−λt)

- A: activity at time t
- A0: activity at t = 0 (the assay)
- λ: decay constant in the same time unit as t
- t: elapsed time

A = λN

- N: number of radioactive nuclei

1 Ci = 3.7×10^10 Bq

**Worked example**

Given: a sample of I-131 contains N = 1.00×10^12 radioactive nuclei. The recall half-life is 8 days. Find the activity in Bq and in mCi.

Formula: λ = 0.693 / T½, then A = λN.

Substitution: T½ = 8 × 24 × 3600 = 691200 seconds. λ = 0.693 / 691200 = 1.003×10^−6 per second.

Arithmetic: A = (1.003×10^−6) × (1.00×10^12) = 1.003×10^6 Bq = 1.003 MBq.

In mCi: 1 mCi = 3.7×10^7 Bq, so A = 1.003×10^6 / 3.7×10^7 = 0.0271 mCi.

Meaning: about a million decays per second, which is only a few hundredths of a millicurie. Activity in becquerels looks large next to activity in millicuries because the becquerel is one decay per second.

Usual wrong turn: forgetting to convert 8 days into seconds before multiplying by N, which produces an “activity” of 0.693/8 × 10^12 = 8.7×10^10 per day and then calling that number becquerels. The becquerel is per second. Another miss is 1 mCi = 3.7×10^10 Bq, which is the curie, and makes this sample look a thousand times weaker.

**Traps**

Decay applied to dose rate when the stem already gave a dose rate that includes a different reference date. Using calendar days and a half-life in hours in the same exponent. Reporting remaining activity as a percent and then failing to multiply by A0.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Curie definition as used in that text. Public blueprint I.10.

## Half-Life and Mean Life

**MDCB:** I.7, I.10, V.6

**What the exam expects**

You find activity after an integer or a fractional number of half-lives. You compute mean life as 1.443 T½. For a permanent implant you multiply the initial dose rate by the mean life, not by the half-life. Given two assays, you can solve for the half-life.

**Core facts**

Half-life is the time for activity, and for the number of nuclei, to fall by half. It is not half the time the source is dangerous, and it is not the time until the source is gone.

Remaining fraction after n half-lives is 1/2^n:

| Half-lives | Fraction left |
| --- | --- |
| 1 | 0.50 |
| 2 | 0.25 |
| 3 | 0.125 |
| 4 | 0.0625 |
| 5 | 0.03125 |
| 10 | about 0.001 (1/1024) |

Mean life τ = 1/λ = 1.443 T½. It is the average lifetime of a nucleus. In a permanent implant the source is left in place for complete decay, and the total dose equals the initial dose rate times the mean life. Exam arithmetic often rounds 1.443 to 1.44. When a stem says 1.44, use 1.44: the Cs-137 mean life is 43.2 years. When a stem says 1.443, use 1.443: that mean life is 43.3 years. Do not mix the two in one item.

Effective half-life applies when biologic excretion and physical decay both remove activity from an organ:

1/Te = 1/Tp + 1/Tb, so Te = Tp Tb / (Tp + Tb).

Te is shorter than both Tp and Tb. Implant sources sealed in seeds do not have a biologic half-life. Unsealed I-131 and P-32 do.

**Formulas**

A = A0 / 2^n, with n = t / T½

τ = 1.443 T½

Total dose for complete decay = Ḋ0 × τ = Ḋ0 × 1.443 × T½

- Ḋ0: dose rate at the start, in dose per time
- T½ and τ: in that same time unit

Te = Tp Tb / (Tp + Tb)

- Te: effective half-life
- Tp: physical half-life
- Tb: biologic half-life

From two assays: λ = ln(A0 / A) / t, then T½ = 0.693 / λ.

**Worked example**

Given: Cs-137, recall half-life 30 years. Assay today is 100 mCi. Find the activity 15 years later. Then find the mean life.

Formula: n = t / T½, A = A0 / 2^n, τ = 1.443 T½.

Substitution: n = 15 / 30 = 0.50. A = 100 / 2^0.50.

Arithmetic: 2^0.50 = √2 = 1.414. A = 100 / 1.414 = 70.7 mCi. Equivalently, one square-root of one-half: 100 × 0.707 = 70.7 mCi.

Mean life: τ = 1.443 × 30 = 43.3 years.

Meaning: halfway to one half-life is not a 25% loss. Half a half-life leaves about 71% of the activity. The mean life, 43 years, is longer than the 30-year half-life. A permanent-implant total-dose calculation that used 30 years instead of 43.3 years would be low by a factor of 1.443.

Usual wrong turn: 15/30 = 1/2, so activity is 50 mCi. That treats “half the half-life” as “half the activity.” The other miss on this same stem is a linear drop: 100 × (1 − 15/30) = 50 mCi, same wrong number, different reason. For the mean-life factor, using 0.693 × 30 = 20.8 years puts the 0.693 on the wrong side of the fraction.

**Traps**

Integer half-life arithmetic used on a fractional interval. Mean life and half-life swapped inside a permanent-implant total dose. Effective half-life replaced by the average of Tp and Tb. For the numbers above, an average of a physical half-life and a biologic half-life is not Te. Te is the product divided by the sum.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.7 and the permanent-implant relation sampled on the public skills list (initial dose rate × 1.44 × half-life; this set uses 1.443).

## Radioactive Equilibrium

**MDCB:** I.1, I.7, I.10

**What the exam expects**

You state the condition for secular equilibrium and for transient equilibrium, you name a therapy pair for each, and you compute the equilibrium activity ratio when half-lives are given. You know when no equilibrium exists.

**Core facts**

Equilibrium is about a parent decaying into a radioactive daughter.

Secular equilibrium: the parent half-life is vastly longer than the daughter half-life. After several daughter half-lives, daughter activity equals parent activity. The pair then decays, if you can see it decay at all, with the parent half-life. Therapy pair to recall: Sr-90 (28.8 y) and Y-90 (64 h). Historical pair: Ra-226 (1600 y) in equilibrium with its daughters. The useful betas from a Sr-90 eye applicator are the Y-90 betas; the source is stored long enough that secular equilibrium has been reached.

Transient equilibrium: the parent is longer-lived than the daughter, but not vastly longer. The daughter activity rises above the parent activity and then the daughter appears to decay with the parent half-life. The activity ratio approaches λ2/(λ2 − λ1), which is greater than 1. The generator pair is Mo-99 to Tc-99m. Tc-99m half-life is the recall value 6 h. Use 66 h for Mo-99 in the example below; confirm that parent half-life in Khan.

No equilibrium: if the daughter half-life is longer than the parent half-life, the daughter grows in and later decays with its own half-life after the parent is gone. The daughter activity does not lock to the parent.

Branching matters. If only a fraction f of parent decays feed the daughter, multiply the ideal ratio by f. For Mo-99 to Tc-99m, f is about 0.87. Confirm the branching fraction in Khan.

The time of maximum daughter activity, starting from a pure parent, is

t_max = ln(λ2 / λ1) / (λ2 − λ1).

**Formulas**

Pure parent at t = 0, branching fraction 1:

A2(t) = A1(0) × [λ2 / (λ2 − λ1)] × [exp(−λ1 t) − exp(−λ2 t)]

- subscript 1: parent
- subscript 2: daughter
- λ: decay constant of that species

Secular, after the daughter has grown in: A2 = A1.

Transient, at late times: A2 / A1 = λ2 / (λ2 − λ1).

With branching fraction f: multiply A2 by f.

**Worked example**

Given: Mo-99 half-life 66 h (confirm in Khan), Tc-99m recall half-life 6 h, branching ignored first (f = 1). Find the transient-equilibrium activity ratio and the time of maximum Tc-99m activity.

Formula: λ = 0.693 / T½. Ratio = λ2 / (λ2 − λ1). t_max = ln(λ2/λ1) / (λ2 − λ1).

Substitution:

λ2 = 0.693 / 6 = 0.1155 per hour

λ1 = 0.693 / 66 = 0.01050 per hour

λ2 − λ1 = 0.1050 per hour

Ratio = 0.1155 / 0.1050 = 1.100

λ2/λ1 = 11.0. ln(11.0) = 2.398. t_max = 2.398 / 0.1050 = 22.8 h.

With f = 0.87: equilibrium activity of Tc-99m is about 0.87 × 1.100 = 0.96 times the Mo-99 activity.

Meaning: at transient equilibrium the daughter activity is slightly higher than the parent activity if every parent decay feeds the daughter, and close to the parent activity once the real branching fraction is included. The useful elution time is on the order of a day after a fresh elution, not many daughter half-lives later in the secular sense. Sr-90/Y-90 is the contrasting case: the ratio goes to 1.00, not to 1.10.

Usual wrong turn: using A2/A1 = λ1/λ2, which is 6/66 = 0.091 and describes a different approximation. Or calling Mo/Tc secular because “the generator is in equilibrium.” The half-lives are within a factor of about ten, which is transient. Secular is the Sr-90 case, where the parent half-life is thousands of times the daughter half-life (28.8 years versus 64 hours).

**Traps**

Secular ratio quoted as greater than 1. Transient pair expected to show equal activities. Equilibrium claimed for a daughter that outlives the parent. Forgetting branching and reporting Tc-99m activity as 1.10 × Mo-99 on a stem that gives a branching fraction.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Confirm the Mo-99 half-life and branching fraction in Khan. Recall half-lives for Y-90, Sr-90, and Tc-99m are the exam set listed in the next lesson.

## Modes of Radioactive Decay

**MDCB:** I.1

**What the exam expects**

For alpha, beta minus, beta plus, electron capture, gamma, isomeric transition, and internal conversion, you state what happens to Z and A and what leaves the nucleus. You know the positron threshold is 1.022 MeV, that beta particles have a continuous spectrum up to Emax, and that gammas are discrete. You know annihilation produces two 0.511 MeV photons.

**Core facts**

Alpha decay. The nucleus emits a helium-4 nucleus (2 protons, 2 neutrons). A decreases by 4. Z decreases by 2. Alphas are monoenergetic for a given transition, high LET, and stopped by a sheet of paper or the outer dead layer of skin. They are an internal hazard, not an external-beam modality.

Beta minus. A neutron becomes a proton. The nucleus emits an electron and an antineutrino. A is unchanged. Z increases by 1. The electron and antineutrino share the energy, so the beta spectrum is continuous from near zero up to Emax. The average beta energy is about Emax/3. Parent and daughter are isobars.

Beta plus. A proton becomes a neutron. The nucleus emits a positron and a neutrino. A is unchanged. Z decreases by 1. The nuclear mass must fall by at least 1.022 MeV, two electron rest energies, or positron emission is impossible. The positron slows and annihilates with an electron, producing two 0.511 MeV photons emitted in opposite directions. F-18 (110 min) is the PET case.

Electron capture. The nucleus captures an orbital electron. A proton becomes a neutron. A is unchanged. Z decreases by 1. A neutrino leaves. No charged particle has to be created, so electron capture can occur when the decay energy is below 1.022 MeV. The atomic vacancy produces characteristic x-rays or Auger electrons. I-125 and Pd-103 decay by electron capture. Electron capture and beta plus can compete when both are energetically allowed.

Gamma emission and isomeric transition. The nucleus drops from an excited state and emits a photon. Z and A are unchanged. If the excited state is long-lived, the state is metastable and the transition is an isomeric transition (Tc-99m, 6 h, 140 keV). Gamma energies are discrete lines.

Internal conversion. The nuclear excitation energy is handed to an orbital electron, which is ejected. No gamma is emitted in that event. Z and A are unchanged. The vacancy then yields characteristic x-rays or Auger electrons. Internal conversion competes with gamma emission. It is not beta decay: the electron was an orbital electron, and Z does not change.

**Formulas**

Changes to remember, not a rate formula:

| Mode | ΔA | ΔZ | What is emitted |
| --- | --- | --- | --- |
| Alpha | −4 | −2 | He-4 nucleus |
| Beta minus | 0 | +1 | electron + antineutrino |
| Beta plus | 0 | −1 | positron + neutrino |
| Electron capture | 0 | −1 | neutrino (plus atomic x-ray or Auger) |
| Gamma or isomeric transition | 0 | 0 | photon |
| Internal conversion | 0 | 0 | orbital electron |

Positron threshold: decay energy at least 2 × 0.511 MeV = 1.022 MeV.

Annihilation: two photons, 0.511 MeV each, 180 degrees apart in the rest frame.

**Traps**

Alpha written as ΔA = −2. Beta written as a change in A. Positron threshold written as 0.511 MeV. Annihilation written as one 1.022 MeV photon. Internal conversion classified as beta minus because an electron was detected. Characteristic x-rays from electron capture classified as gammas. Average beta energy set equal to Emax; the spectrum is continuous and the mean is about one-third of the endpoint.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.1.

## Common Radioisotopes

**MDCB:** I.7, V.1

**What the exam expects**

You recall the half-life and the kind of emission for each therapy and imaging nuclide on the standard list. You use the correct one in a decay problem. You know which sources are pure beta, which are photon sources for brachytherapy, and which are diagnostic only.

**Core facts**

These half-lives are the values candidates are expected to recall:

| Nuclide | Half-life to recall | Mode and emission to recall |
| --- | --- | --- |
| Co-60 | 5.26 y | β−, gammas 1.17 and 1.33 MeV (mean 1.25 MeV) |
| Cs-137 | 30 y | β− to Ba-137m, gamma 0.662 MeV |
| Ir-192 | 73.8 d | β−, complex gammas, mean energy about 0.38 MeV |
| I-125 | 59.4 d | electron capture, photons about 28 keV |
| Pd-103 | 17 d | electron capture, photons about 21 keV |
| Au-198 | 2.7 d | β−, gamma 0.412 MeV |
| Ra-226 | 1600 y | α, gammas from daughters |
| I-131 | 8 d | β−, gamma 364 keV |
| P-32 | 14.3 d | pure β−, Emax 1.71 MeV |
| Sr-90 | 28.8 y | pure β− to Y-90 |
| Y-90 | 64 h | pure β−, Emax 2.28 MeV |
| Tc-99m | 6 h | isomeric transition, 140 keV |
| F-18 | 110 min | β+, annihilation photons 0.511 MeV |

Co-60 is a teletherapy gamma source. Because λ per month is 0.01098 (see the decay-constant example), output falls about 1.09% per month. A source whose output is 120 cGy/min today is about 120 × 0.989 = 118.7 cGy/min in one month. The machine uses a timer. There is no monitor unit.

Cs-137 replaced radium for many LDR gynecologic sources. Half-life 30 y means a source is still near its original activity over a single implant, and a decay correction over a few days is negligible. Over 30 years the activity is half.

Ir-192 is the HDR workhorse. Half-life 73.8 days means a source exchanged several times a year, and a decay correction from assay to treatment is routine. Mean photon energy is a few hundred keV, so room shielding is concrete and the door is a real design problem. Confirm a published exposure-rate constant in Khan rather than memorizing an unstated Γ.

I-125 (59.4 d) and Pd-103 (17 d) are permanent prostate seed sources. Both are electron-capture, low-energy photon sources. Mean life of I-125 is 1.443 × 59.4 = 85.7 days. Mean life of Pd-103 is 1.443 × 17 = 24.5 days. For the same total dose, the shorter mean life requires a higher initial dose rate. Ratio of mean lives: 85.7 / 24.5 = 3.50. Pd-103 starts about 3.5 times hotter than I-125 for the same total dose, before any prescription difference is applied.

Au-198, 2.7 days, has been used as gold grains. A week is 7 / 2.7 = 2.59 half-lives, so about 17% of the activity remains (2^−2.59 ≈ 0.17).

Ra-226, 1600 y, is historical. Filtered radium (0.5 mm platinum) is the source behind the old exposure-rate constant 8.25 R·cm²/(mg·h). Activity was stated in mg-Ra eq. You will see it in older calculation stems. Secular equilibrium with daughters is assumed for an unvented source.

I-131, 8 days, is unsealed thyroid therapy, beta plus a 364 keV gamma. The gamma is why the patient is a radiation precaution for other people. P-32, 14.3 days, is a pure beta emitter (Emax 1.71 MeV). There is no gamma to image. Shield a beta emitter with plastic. High-Z shielding produces bremsstrahlung.

Sr-90, 28.8 y, is a pure beta emitter in secular equilibrium with Y-90, 64 h, Emax 2.28 MeV. Ophthalmic applicators use that Y-90 beta. Y-90 microspheres are the daughter nuclide used alone, not in equilibrium, for radioembolization. Y-90 maximum range in tissue is about a centimeter; confirm the range figure in Khan before using it as more than a scale.

Tc-99m, 6 h, 140 keV, is diagnostic, from a Mo-99 generator (transient equilibrium). It is not a therapy source. F-18, 110 min, is the PET positron emitter. A delay of one half-life, 110 minutes, halves the administered activity. A delay of 55 minutes leaves 70.7%, not 50%.

**Formulas**

Monthly Co-60 factor from the recall half-life:

T½ = 5.26 × 12 = 63.12 months

λ = 0.693 / 63.12 = 0.01098 per month

Remaining fraction after one month = exp(−0.01098) = 0.989

Mean lives used above: τ = 1.443 T½.

**Worked example**

Given: Co-60 output measured today as 120 cGy/min. Recall half-life 5.26 y. Find the output in one month from decay alone.

Formula: remaining fraction = exp(−0.693 t / T½), with t and T½ in months.

Substitution: t = 1, T½ = 63.12 months. Exponent = −0.693/63.12 = −0.01098.

Arithmetic: exp(−0.01098) = 0.9891. Output = 120 × 0.9891 = 118.7 cGy/min.

Meaning: the monthly correction is about 1%, not the 5.26-year half-life misread as 5% per month.

Usual wrong turn: 120 × (1 − 0.0526) = 113.7 cGy/min, which uses the yearly half-life number as a monthly percent. Or adding 1% because “the source decays and the time must increase,” and then raising the output number instead of lowering it. Output falls. Treatment time rises if the prescription is unchanged.

**Traps**

Ir-192 half-life quoted in hours or as 74 years. Cs-137 and Cs-131 swapped; the recall value on this list for cesium therapy sources of the older LDR type is Cs-137 at 30 y. I-125 and I-131 swapped: 59.4 days versus 8 days, keV photons versus a 364 keV gamma plus beta. P-32 or Y-90 assigned a gamma because “all therapy sources have one.” F-18 half-life used as 110 hours. Pd-103 used as 17 hours.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, for emission energies, the filtered-radium exposure-rate constant, and ranges. Half-lives listed above are the recall set for this exam. Public blueprint I.7.

## Radioactivity Calculation Tutorial

**MDCB:** I.7, I.10, V.6

**What the exam expects**

A stem gives an assay and a later time, or an initial dose rate for a permanent seed, and you finish the number. This lesson chains the pieces the earlier lessons separated: λ, exponential activity, integer half-life as a check, mean life, and total dose.

**Core facts**

Do the steps in the same order every time.

1. Write the recall half-life and convert t into that unit.
2. Compute λ = 0.693 / T½ and write the unit (per day, per hour).
3. Compute λt. It is dimensionless.
4. Compute exp(−λt), or 2^(−t/T½). They are the same number if 0.693 and ln(2) are handled consistently.
5. Multiply by A0.
6. If the question is total dose from complete decay, stop using the exponential. Use dose rate × 1.443 × T½, with the dose rate and the half-life in matching time units.

**Formulas**

λ = 0.693 / T½

A = A0 exp(−λt) = A0 × 2^(−t/T½)

τ = 1.443 T½

D∞ = Ḋ0 × τ

**Worked example**

Given: a permanent Pd-103 seed. Recall half-life 17.0 days. Assay activity 2.00 mCi. Initial dose rate at the point of interest 5.00 cGy/h. The implant is permanent.

Find (a) λ per day, (b) activity after 10.0 days, (c) mean life in hours, (d) total dose at the point.

(a) Formula: λ = 0.693 / T½

Substitution: λ = 0.693 / 17.0 = 0.04076 per day.

(b) Formula: A = A0 exp(−λt)

Substitution: λt = 0.04076 × 10.0 = 0.4076. A = 2.00 × exp(−0.4076).

Arithmetic: exp(−0.4) = 0.6703. exp(−0.0076) = 0.9924. Product = 0.6703 × 0.9924 = 0.6652. A = 2.00 × 0.6652 = 1.33 mCi.

Check with half-lives: n = 10/17 = 0.588. 2^−0.588 = 0.665. Same remaining fraction. Activity 1.33 mCi.

(c) Formula: τ = 1.443 × T½, then convert days to hours.

Substitution: τ = 1.443 × 17.0 = 24.53 days. Hours: 24.53 × 24 = 588.7 h.

Arithmetic check: 1.443 × 10 = 14.43, 1.443 × 7 = 10.10, sum 24.53 days. 24 × 24 = 576, 0.53 × 24 = 12.7, sum 588.7 h.

(d) Formula: D∞ = Ḋ0 × τ

Substitution: D∞ = 5.00 cGy/h × 588.7 h = 2944 cGy = 29.44 Gy.

Alternative: 17.0 days × 24 h/day = 408 h. 5.00 × 408 = 2040 cGy if someone multiplies by the half-life only. 2040 × 1.443 = 2944 cGy. Same result.

Meaning: after 10 days a 17-day source still holds two-thirds of its activity, not half. The permanent implant delivers 2944 cGy at this point because the dose rate keeps falling for several mean lives, and the integral of an exponential is the starting rate times the mean life. Using the half-life alone (2040 cGy) is 31% low.

Usual wrong turn: λ = 0.693 × 17 = 11.8 per day, then exp(−118) is zero and the seed is “gone” by day 10. Or t = 10 days with λ computed per hour (0.04076/24) so λt is 24 times too small and the activity barely moves. Or total dose = 5 cGy/h × 17 h, mixing the 17-day half-life with an hour. Or total dose = 5 × 408 = 2040 cGy, the half-life integral, which is the error the 1.443 factor exists to prevent.

**Traps**

Checking the exponential against 2^(−n) and “fixing” a correct exponential because the two differed in the third digit from rounding 0.693. Stopping at activity when the question asked for dose. Applying the permanent-implant mean-life formula to a temporary HDR dwell, which is removed after minutes and does not decay in place for a mean life.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Recall half-life Pd-103 = 17 d.

## Radioactivity Quiz

This quiz checks decay mode against the change in Z and A, the positron threshold 1.022 MeV, annihilation as two 0.511 MeV photons, continuous beta spectra versus discrete gammas, and electron capture versus beta plus. It also checks which nuclide on the recall list is a pure beta emitter, which is an electron-capture seed, and which equilibrium (secular Sr-90/Y-90 versus transient Mo-99/Tc-99m) applies. The traps are ΔA = −2 for alpha, a 0.511 MeV pair threshold, I-125 assigned the I-131 half-life, and a secular ratio of λ2/(λ2−λ1) instead of 1.

## Radioactive Decay Calculation Mini-Quiz

This quiz checks λ = 0.693/T½, A = A0 exp(−λt) with matching time units, fractional half-lives (half of one half-life leaves about 71%, not 50%), mean life = 1.443 T½, and permanent-implant total dose = initial dose rate × mean life. The traps are multiplying by 0.693 instead of dividing, using the half-life where the mean life belongs (answer low by 1.443), converting curies with 3.7×10^10 in the wrong direction, and mixing hours and days in one exponent.
