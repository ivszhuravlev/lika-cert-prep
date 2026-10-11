# Module 41. Radiation protection

Original notes for MDCB CMD prep. Domain VI is about 9% of the exam. Objectives VI.1, VI.2, and VI.3. Detectors as objects are in module 42; this module is the limit, the badge, and the barrier.

The public lesson title says “NRCP.” The council is the National Council on Radiation Protection and Measurements, **NCRP**. An item that says “according to NCRP” wants **NCRP Report 116**, not a later ICRP number.

## ALARA and maximum permissible dose equivalent based on NRCP recommendations, regulatory guidelines

**Objectives:** VI.1, VI.2

**What the exam expects:** Quote NCRP 116 limits from memory, separate them from the later ICRP lens limit, apply a stated radiation weighting factor, and state the linear no-threshold model in one sentence. ALARA is a practice, not a second set of numbers.

**ALARA.** As low as reasonably achievable, with economic and social factors taken into account. The table below is a ceiling. A reading under the ceiling can still be a failure of ALARA if a simple shield or a step back would have lowered it.

**NCRP 116 limits to recall**

| Person | Quantity | Limit |
| --- | --- | --- |
| Occupational | Effective dose | 50 mSv in a year |
| Occupational | Lens of the eye | 150 mSv in a year |
| Occupational | Skin or extremity | 500 mSv in a year |
| Public | Effective dose | 1 mSv in a year |
| Public | Lens of the eye | 15 mSv in a year |
| Public | Skin or extremity | 50 mSv in a year |
| Embryo/fetus, after declaration | Equivalent dose | 0.5 mSv in a month |
| Embryo/fetus, NRC gestation | Equivalent dose | 5 mSv over the gestation |

NCRP also offers a cumulative occupational guidance of \(10\,\mathrm{mSv} \times \text{age in years}\). That is guidance over a career. It does not replace the 50 mSv annual effective-dose limit.

**ICRP and the lens.** ICRP later lowered the occupational lens limit (20 mSv in a year, averaged, in the 2011 tissue-reactions statement). When the stem says “according to NCRP,” the lens answer is **150 mSv in a year**. The ICRP figure is the distractor.

**LNT.** The linear no-threshold model treats the probability of stochastic effects (cancer, heritable effects) as proportional to dose, with no dose at which that probability is taken to be exactly zero. Deterministic effects (skin injury, cataract, marrow suppression) do have thresholds. Dose limits are regulatory ceilings on top of ALARA, not a claim that 49 mSv is “safe” and 51 mSv is the first dangerous sievert.

**Radiation weighting factors \(w_R\)** used in this course:

| Radiation | \(w_R\) |
| --- | --- |
| Photons, electrons | 1 |
| Protons | 2 |
| Alpha particles | 20 |
| Neutrons | energy-dependent, up to 20 |

Older ICRP 60 tables list protons at 5. If the stem names a report, use that report’s table. These notes use 2 for protons. Neutron items that omit the energy are incomplete; the worked example states \(w_R\).

Equivalent dose (rem if absorbed dose is in rad, or Sv if absorbed dose is in Gy):

\[
H = \sum w_R D
\]

For these numbers, 1 rad = 1 cGy and 1 rem = 1 cSv = 10 mSv.

**Area signs (regulatory, 10 CFR 20), because items pair them with the NCRP table**

- Caution, radiation area: more than 0.05 mSv in 1 hour at 30 cm (5 mrem/h).
- Caution, high radiation area: more than 1 mSv in 1 hour at 30 cm (100 mrem/h).
- Grave danger, very high radiation area: more than 5 Gy in 1 hour at 1 m.

### Worked example

**Given.** A person receives 0.10 cGy from photons (\(w_R = 1\)) and 0.05 cGy from neutrons. The stem states the neutron \(w_R = 10\).

**Formula.** \(H = w_R D\) for each component, then add.

**Substitute.**

\[
H_{\gamma} = 0.10 \times 1 = 0.10 \text{ rem}
\qquad
H_n = 0.05 \times 10 = 0.50 \text{ rem}
\]

**Arithmetic.** \(0.10 + 0.50 = 0.60\) rem \(= 6.0\) mSv, because 1 rem = 10 mSv.

**Check.** In SI: \(0.10\) cGy \(= 0.0010\) Gy, times \(w_R = 1\), is 1.0 mSv. Neutron absorbed dose \(0.05\) cGy \(= 0.00050\) Gy, times 10, is 5.0 mSv. Total 6.0 mSv.

**Result means.** The equivalent dose is 6 mSv, not the 0.15 cGy absorbed-dose sum. Against NCRP 116, 6 mSv is well under the 50 mSv occupational effective-dose limit and is six times the 1 mSv public effective-dose limit, so the same number is a different conclusion for a worker and for a member of the public. It is not a lens dose unless the stem says the dose was to the lens.

**Wrong turns**

- Adding 0.10 + 0.05 = 0.15 cGy and calling it the equivalent dose.
- Using \(w_R = 20\) for every neutron. Twenty is the top of the neutron table and the alpha factor.
- Using the ICRP lens limit of 20 mSv when the stem says NCRP (NCRP lens is 150 mSv).
- Using 50 mSv as the public effective limit (that is the occupational effective limit; the public effective limit is 1 mSv).
- Treating LNT as a deterministic threshold.

**Traps.** Write “occupational or public” and “effective, lens, or skin” before you pick a row. Then apply \(w_R\) only to equivalent dose, not to a raw exposure reading.

**Sources.** NCRP Report 116 for the limit table and LNT as used in U.S. guidance. ICRP 103 for \(w_R\) (protons 2) and the later ICRP lens statement. 10 CFR 20 for the area-sign definitions and for the 5 mSv gestation limit.

## Radiation Monitoring for Personnel and Patients

**Objectives:** VI.2, VI.1

**What the exam expects:** Who is badged, what a declared pregnancy changes, and which limit is monthly versus gestation. Personnel monitors (OSL, TLD, film) integrate dose for the worker. Pocket dosimeters and electronic dosimeters give an immediate reading. Area monitors and survey meters watch rooms and patients; they are not a substitute for a fetal badge. Patient in-vivo diodes are dose to the patient, covered with the instruments in module 42.

A declared pregnancy is a written declaration. After that declaration the NCRP recommendation is 0.5 mSv to the embryo in a month, kept uniform, and the NRC gestation limit is 5 mSv. A fetal monitor is worn so the reading estimates the embryo, not the collar.

### Worked example

**Given.** After a written declaration, the fetal badge for the month reads 0.80 mSv. NCRP monthly recommendation: 0.5 mSv. NRC gestation limit: 5 mSv.

**Arithmetic.** \(0.80 - 0.50 = 0.30\) mSv over the monthly recommendation. \(0.80 < 5\), so this single month does not by itself exceed the NRC gestation cap. Five more months at 0.80 mSv would be \(6 \times 0.80 = 4.80\) mSv, still under 5 mSv, but every one of those months would break the 0.5 mSv recommendation. Six months at 0.80 is 4.80; a seventh month would be \(7 \times 0.80 = 5.60\) mSv and would pass the NRC gestation limit as well.

**Check.** \(0.80 - 0.50 = 0.30\). \(6 \times 0.80 = 4.80\). \(4.80 + 0.80 = 5.60\).

**Result means.** The month fails the NCRP 0.5 mSv recommendation by 0.30 mSv. Work restrictions are a radiation-safety decision at that point. The NRC 5 mSv figure is the whole gestation, not a license to bunch the dose into one month.

**Wrong turns**

- Comparing 0.80 mSv to the 50 mSv occupational limit and calling the month acceptable. The fetal recommendation is the row that applies after declaration.
- Using 0.5 mSv as the entire gestation (that is the monthly figure; the gestation figure in NRC rules is 5 mSv).
- Forgetting that the declaration is written. An unstated pregnancy is still protected by ALARA; the specific 0.5 mSv monthly recommendation is tied to the declaration.
- Badge on the collar reported as the fetal dose without a stated conversion.

**Traps.** Two fetal numbers live side by side: 0.5 mSv in a month (NCRP, after declaration) and 5 mSv over the gestation (NRC). Name which one you compared.

**Sources.** NCRP Report 116 (embryo/fetus). 10 CFR 20.1208 (5 mSv gestation). Personnel dosimeter types as used in clinical radiation safety programs.

## Treatment Vault Shielding Requirements

**Objectives:** VI.3, I.10

**What the exam expects:** A primary barrier intercepts the useful beam. A secondary barrier does not; it shields head leakage and patient scatter. Workload, use factor, and occupancy enter the primary transmission formula. Thickness then comes from the number of tenth-value layers and the TVL the stem gives for that energy and that concrete. HVL and TVL arithmetic is module 36.

**Formula (primary barrier)**

\[
B = \frac{P\, d^2}{W\, U\, T}
\]

- \(B\): transmission required of the barrier (a fraction)
- \(P\): design dose limit behind the barrier, per week, same dose unit as \(W\)
- \(d\): distance from the source (or the target) to the point being protected, in meters when \(W\) is specified at 1 m
- \(W\): workload, dose per week at 1 m from the source
- \(U\): use factor, the fraction of the workload aimed at this barrier
- \(T\): occupancy factor, the fraction of time a person is at the protected point

Number of TVLs and thickness:

\[
n = \log_{10}(1/B)
\qquad
\text{thickness} = n \times \mathrm{TVL}
\]

Leakage radiation is present whenever the beam is on, so the leakage use factor is 1. Patient scatter depends on field size and angle. Both are secondary. The scatter equation in NCRP 151 carries a scatter fraction this lesson does not invent; if the stem gives that fraction, treat it as given. The worked numbers below are the primary-barrier formula only.

A controlled area is often designed to 0.1 mSv in a week (about 5 mSv in a year). An uncontrolled area is often designed to 0.02 mSv in a week (about 1 mSv in a year). Use the \(P\) the stem prints.

### Worked example

**Given.** Primary barrier. \(P = 0.0001\) Gy/week (0.1 mSv/week, a controlled-area design goal). Distance \(d = 4\) m. Workload \(W = 400\) Gy/week at 1 m. Use factor \(U = 0.25\) (this cardinal wall). Occupancy \(T = 1\). The stem gives TVL = 30 cm for this beam in this concrete. That 30 cm is a given for the arithmetic, not a universal linac TVL.

**Substitute.**

\[
B = \frac{0.0001 \times 4^2}{400 \times 0.25 \times 1} = \frac{0.0001 \times 16}{100}
\]

**Arithmetic.** \(400 \times 0.25 = 100\). \(0.0001 \times 16 = 0.0016\). \(B = 0.0016/100 = 1.6 \times 10^{-5}\).

\[
n = \log_{10}\left(\frac{1}{1.6 \times 10^{-5}}\right) = \log_{10}(62500) = 4.796
\]

\[
\text{thickness} = 4.796 \times 30 = 144 \text{ cm}
\]

**Check.** \(1 / 1.6 \times 10^{-5} = 6.25 \times 10^{4} = 62500\). \(\log_{10}(62500) = \log_{10}(6.25) + 4\). \(\log_{10}(6.25) \approx 0.796\), so \(n = 4.796\). \(4.796 \times 30 = 143.9\) cm, which is 144 cm to three figures. \(WUT = 100\) Gy/week aimed at a fully occupied wall; \(P d^2 = 0.0016\); the ratio is \(1.6 \times 10^{-5}\).

**Result means.** This primary wall may transmit no more than \(1.6 \times 10^{-5}\) of the useful beam. At the stated TVL of 30 cm, the concrete is about 144 cm thick, just under 5 TVLs. A secondary wall looking at the same room does not use \(U = 0.25\) for leakage; leakage uses \(U = 1\) and a much smaller workload (the head-leakage fraction of \(W\)).

**Wrong turns**

- Forgetting to square \(d\): \(0.0001 \times 4 / 100 = 4 \times 10^{-6}\), too small by a factor of 4, and the wall comes out thinner than the design allows.
- Using \(U = 1\) on a primary wall whose use factor is 1/4, which makes \(B\) four times smaller and the wall thicker than the formula requires. The opposite error, \(U = 0.25\) on leakage, under-shields a secondary barrier.
- Taking \(T\) from memory when the stem gives it. Full occupancy is \(T = 1\). Partial occupancy comes from the NCRP table in the stem (corridors and toilets are less than 1). This example states \(T = 1\).
- Designing an uncontrolled corridor to 0.1 mSv/week. That \(P\) is the controlled-area scale; the public-area scale is tighter (0.02 mSv/week if the annual public goal is 1 mSv).
- Confusing HVL with TVL when converting \(B\) to concrete. \(n\) above is in TVLs because the log is base 10. In HVLs the count would be \(\ln(1/B)/0.693\), about \(3.32\) times larger, and the thickness is that count times the HVL, not times the TVL.

**Traps.** Label the barrier primary or secondary before you pick \(U\). Write the unit of \(d\) next to the unit of \(W\). Meters with a workload at 1 m is the usual pair.

**Sources.** NCRP Report 151, structural shielding design for megavoltage rooms (primary versus secondary, \(W\), \(U\), \(T\)). NCRP Report 116 sets the public and occupational limits that justify the weekly \(P\). Module 36 for HVL and TVL.

## Radiation Protection and Personnel Monitoring Quiz

**Skills this quiz checks**

- Recall NCRP 116: occupational 50, 150, and 500 mSv/year (effective, lens, skin/extremity); public 1 and 15 mSv/year (effective, lens); embryo 0.5 mSv in a month after declaration; NRC gestation 5 mSv.
- Choose 150 mSv for the lens when the stem says NCRP, and recognize the later ICRP lens limit as a different report.
- Apply a stated \(w_R\), including neutrons that are not automatically 20, and convert rem to mSv.
- State LNT for stochastic risk and ALARA as a practice under the ceiling.
- Identify radiation-area and high-radiation-area signs at 0.05 mSv/h and 1 mSv/h at 30 cm.
- Compute primary-barrier \(B = P d^2 / (WUT)\), square the distance, and keep leakage at use factor 1.
