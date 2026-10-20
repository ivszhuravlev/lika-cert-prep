# Module 41. Radiation protection

Original notes for MDCB CMD prep. Domain VI is about 9% of the exam. Objectives VI.1, VI.2, and VI.3. Detectors as objects are in module 42; this module is the limit, the badge, and the barrier.

The public lesson title says “NRCP.” The council is the National Council on Radiation Protection and Measurements, **NCRP**. An item that says “according to NCRP” wants **NCRP Report 116**, not a later ICRP number.

## ALARA and maximum permissible dose equivalent based on NRCP recommendations, regulatory guidelines

**Objectives:** VI.1, VI.2

**What the exam expects:** Quote NCRP 116 limits from memory, separate them from the later ICRP lens limit, and match 10 CFR 20.1201, 20.1207, and 20.1301. Apply a stated radiation weighting factor, and state the linear no-threshold model in one sentence. ALARA is a practice under the ceiling. Investigational levels I and II are local thresholds. This lesson does not give them a universal millisievert value.

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

**NRC adult and minor limits.** 10 CFR 20.1201 uses the same three adult ceilings. The regulatory names are total effective dose equivalent (TEDE), lens dose equivalent, and the 500 mSv organ, skin, and extremity limits. 10 CFR 20.1207 sets the annual occupational dose for a minor at 10 percent of each adult limit.

| Rule | Person | Quantity | Limit |
| --- | --- | --- | --- |
| 10 CFR 20.1201 | Adult | TEDE | 50 mSv in a year |
| 10 CFR 20.1201 | Adult | Lens of the eye | 150 mSv in a year |
| 10 CFR 20.1201 | Adult | Skin, extremity, or any organ other than the lens | 500 mSv in a year |
| 10 CFR 20.1207 | Minor | Each adult limit above | 10 percent of that limit |

The minor arithmetic is \(0.10 \times 50 = 5\) mSv TEDE, \(0.10 \times 150 = 15\) mSv to the lens, and \(0.10 \times 500 = 50\) mSv to skin, extremity, or organ. Skin and extremity use the shallow-dose equivalent. The organ figure is the sum of the deep-dose equivalent and the committed dose equivalent to that organ. The lens stays on its own row.

**Public dose, 10 CFR 20.1301.** A member of the public is limited to 1 mSv TEDE in a year, the same annual effective-dose figure as NCRP 116, and to 0.02 mSv (2 mrem) in any one hour from external sources in an unrestricted area. A reading of 0.03 mSv in one hour is over that hourly cap by \(0.03 - 0.02 = 0.01\) mSv. A reading of 0.015 mSv in one hour is under it by \(0.02 - 0.015 = 0.005\) mSv.

The hourly cap is a dose in one hour. The uncontrolled-area shielding goal later in this lesson is 0.02 mSv in a week. Fifty weeks at that weekly goal is \(50 \times 0.02 = 1.0\) mSv, which is why the weekly goal lines up with the annual public limit. The NCRP public lens row (15 mSv) and public skin row (50 mSv) stay in the NCRP table above.

**ALARA investigational levels.** A radiation protection program may set two investigational levels below the regulatory ceiling. Level I is the lower local threshold and starts a review of how the dose was received. Level II is the higher local threshold and starts a formal investigation, often written to the radiation safety committee. The millisievert values are whatever that program wrote down. Crossing level I is a local review. It is not, by itself, an exceedance of the 50 mSv TEDE limit.

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
- Assigning the adult 50 mSv TEDE limit to a minor. Ten percent of 50 mSv is 5 mSv.
- Reading 0.02 mSv in any one hour as 0.02 mSv in a week, or as 1 mSv in any one hour.
- Quoting one millisievert number for ALARA level I at every clinic. Level I and level II are local.
- Treating LNT as a deterministic threshold.

**Traps.** Write “occupational or public” and “effective, lens, or skin” before you pick a row. Then apply \(w_R\) only to equivalent dose, not to a raw exposure reading.

**Sources.** NCRP Report 116 for the limit table and LNT as used in U.S. guidance. ICRP 103 for \(w_R\) (protons 2) and the later ICRP lens statement. 10 CFR 20.1201 and 20.1207 for the adult and minor occupational limits, 10 CFR 20.1301 for the public annual and hourly limits, and 10 CFR 20 for the area-sign definitions and the 5 mSv gestation limit.

## Radiation Monitoring for Personnel and Patients

**Objectives:** VI.2, VI.1

**What the exam expects:** Who is badged under 10 CFR 20.1502, what a declared pregnancy changes, and which number is a monthly recommendation, a gestation limit, or a monitoring trigger. Personnel monitors (OSL, TLD, film) integrate dose for the worker. Pocket dosimeters and electronic dosimeters give an immediate reading. Area monitors and survey meters watch rooms and patients; they are not a substitute for a fetal badge. Patient in-vivo diodes are dose to the patient, covered with the instruments in module 42.

**Who is monitored, 10 CFR 20.1502.** The decision is prospective: monitor the person who is likely to exceed a trigger. For external dose the triggers in this lesson are:

- An adult likely to exceed 10 percent of a 10 CFR 20.1201 limit. Ten percent of the 50 mSv TEDE limit is \(0.10 \times 50 = 5\) mSv.
- A minor likely to exceed 1 mSv deep dose in a year.
- A declared-pregnant worker likely to exceed 1 mSv deep dose during the pregnancy.
- Any person who will enter a high radiation area. The same sentence of the rule covers a very high radiation area. Entry requires monitoring even when the adult’s expected TEDE is under 5 mSv.

The 5 mSv adult figure is a monitoring threshold. It is the same arithmetic as the minor’s annual TEDE limit, and it is the same number of millisieverts as the NRC gestation limit, but the three sentences do different jobs. The 1 mSv minor and declared-pregnant figures are monitoring triggers. They are not the minor TEDE limit (5 mSv) and they are not the NCRP monthly embryo recommendation (0.5 mSv).

A declared pregnancy is a written declaration. After that declaration the NCRP recommendation is 0.5 mSv to the embryo in a month, kept uniform, and the NRC gestation limit is 5 mSv. A fetal monitor is worn so the reading estimates the embryo, not the collar.

### Worked example

**Given.** Four external-dose estimates. None of them is a lens dose.

1. Adult, likely TEDE 6 mSv in the year, no entry into a high radiation area.
2. Adult, likely TEDE 3 mSv in the year, must enter a high radiation area.
3. Minor, likely deep dose 1.4 mSv in the year.
4. Declared-pregnant worker, likely deep dose 1.8 mSv over the pregnancy. Her adult TEDE estimate is 4 mSv. She will not enter a high radiation area.

**Arithmetic.** Adult TEDE trigger: \(0.10 \times 50 = 5\) mSv. Person 1: \(6 - 5 = 1\) mSv over that trigger, so monitor. Person 2: \(5 - 3 = 2\) mSv under the 5 mSv trigger. High-radiation-area entry still requires a monitor. Person 3: \(1.4 - 1.0 = 0.4\) mSv over the 1 mSv minor trigger, so monitor. Person 4: \(1.8 - 1.0 = 0.8\) mSv over the declared-pregnant trigger, so monitor. Her adult estimate is \(5 - 4 = 1\) mSv under the adult 5 mSv trigger, which does not cancel the pregnancy trigger.

**Check.** \(0.10 \times 50 = 5\). \(6 > 5\). \(3 < 5\). \(1.4 > 1\). \(1.8 > 1\). \(4 < 5\).

**Result means.** Badge person 1 because 6 mSv exceeds 5 mSv. Badge person 2 because of the high radiation area. Badge person 3 because 1.4 mSv exceeds 1 mSv. Badge person 4 because 1.8 mSv exceeds 1 mSv. An adult estimate of 4 mSv does not remove person 4 from monitoring.

**Wrong turns**

- Waiting until 50 mSv is already on the badge. The rule asks whether the person is likely to exceed the trigger.
- Using 5 mSv as the deep-dose monitoring trigger for a minor or a declared pregnancy. That trigger is 1 mSv.
- Treating “under the 5 mSv gestation cap” as “no fetal monitor.” The cap and the 1 mSv monitoring trigger are different sentences.

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

**HDR room, pointer only.** Two room facts belong with personnel protection. The HDR door interlock retracts the source if the door opens. After the fraction, an in-room survey of the patient confirms the source is back in the safe. The console “retracted” indication is not that survey. Source decay, dwell time, and the emergency crank are module 40.

**Traps.** Two fetal dose numbers live side by side: 0.5 mSv in a month (NCRP, after declaration) and 5 mSv over the gestation (NRC). Beside them, 10 CFR 20.1502 asks whether a declared-pregnant worker is likely to exceed 1 mSv. Name which sentence you compared. The adult badge threshold of 5 mSv is 10 percent of 50 mSv. It is not a fourth name for the gestation limit.

**Sources.** NCRP Report 116 (embryo/fetus). 10 CFR 20.1208 (5 mSv gestation). 10 CFR 20.1502 (who must be monitored). 10 CFR 35 for the HDR door interlock and the post-treatment survey, with the worked survey in module 40. Personnel dosimeter types as used in clinical radiation safety programs.

## Treatment Vault Shielding Requirements

**Objectives:** VI.3, I.10

**What the exam expects:** A primary barrier intercepts the useful beam. A secondary barrier does not. It shields head leakage and patient scatter as separate terms. Leakage at 1 m is 0.1 percent of the useful beam, and its use factor is 1. Workload, use factor, and occupancy enter the primary transmission formula. Thickness then comes from the number of tenth-value layers and the TVL for that energy and that concrete. Use the TVL the stem gives. If the stem gives none, ordinary concrete is about 35 cm at 6 MV and about 45 cm at 18 MV. HVL and TVL arithmetic is module 36.

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

**Secondary barrier.** A secondary barrier is not struck by the useful beam. It is sized for two separate contributions: head leakage and patient scatter. A maze is arranged so the door is one of these barriers. The door sees leakage and scatter.

Head leakage at 1 m is 0.1 percent of the useful beam. As a fraction that is 0.001. The leakage workload at 1 m is \(0.001 \times W\), with \(W\) the useful-beam workload at 1 m. Leakage is present whenever the beam is on, so the leakage use factor is \(U = 1\). The leakage transmission uses the primary formula with those two substitutions:

\[
B = \frac{P\, d^2}{(0.001\, W)\, (1)\, T}
\]

Patient scatter is not inside that 0.001. Scatter depends on energy, field size, and angle. NCRP 151 carries a scatter fraction for that term. This lesson does not assign a universal scatter fraction. If the stem gives the fraction, use it as given, and keep it as its own term. Do not account for scatter by changing the leakage use factor from 1 to 0.25.

The first worked example is the primary-barrier formula only. The second is the leakage term only.

A controlled area is often designed to 0.1 mSv in a week (about 5 mSv in a year). An uncontrolled area is often designed to 0.02 mSv in a week. Fifty weeks at that weekly goal is \(50 \times 0.02 = 1.0\) mSv, the annual public limit. That weekly 0.02 mSv is not the 10 CFR 20.1301 cap of 0.02 mSv in any one hour. Use the \(P\) the stem prints.

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

**Result means.** This primary wall may transmit no more than \(1.6 \times 10^{-5}\) of the useful beam. At the stated TVL of 30 cm, the concrete is about 144 cm thick, just under 5 TVLs. That 30 cm is the TVL this example was given. It is not the 6 MV teaching value below. A secondary wall looking at the same room does not use \(U = 0.25\) for leakage. Leakage uses \(U = 1\) and a workload of 0.1 percent of \(W\). The next example does that arithmetic.

**Wrong turns**

- Forgetting to square \(d\): \(0.0001 \times 4 / 100 = 4 \times 10^{-6}\), too small by a factor of 4, and the wall comes out thinner than the design allows.
- Using \(U = 1\) on a primary wall whose use factor is 1/4, which makes \(B\) four times smaller and the wall thicker than the formula requires. The opposite error, \(U = 0.25\) on leakage, under-shields a secondary barrier.
- Taking \(T\) from memory when the stem gives it. Full occupancy is \(T = 1\). Partial occupancy comes from the NCRP table in the stem (corridors and toilets are less than 1). This example states \(T = 1\).
- Designing an uncontrolled corridor to 0.1 mSv/week. That \(P\) is the controlled-area scale; the public-area scale is tighter (0.02 mSv/week if the annual public goal is 1 mSv).
- Confusing HVL with TVL when converting \(B\) to concrete. \(n\) above is in TVLs because the log is base 10. In HVLs the count would be \(\ln(1/B)/0.693\), about \(3.32\) times larger, and the thickness is that count times the HVL, not times the TVL.

### Worked example

**Given.** Leakage term only, same room as the primary example. \(P = 0.0001\) Gy/week, \(d = 4\) m, useful-beam \(W = 400\) Gy/week at 1 m, \(T = 1\). Head leakage at 1 m is 0.1 percent of the useful beam, so the leakage workload is \(0.001 \times W\). Leakage use factor \(U = 1\). Patient scatter is not in these numbers. For thickness, use the 6 MV teaching TVL in ordinary concrete, 35 cm, not the 30 cm the primary example was given.

**Substitute.** Leakage workload \(= 0.001 \times 400 = 0.4\) Gy/week.

\[
B = \frac{0.0001 \times 4^2}{0.4 \times 1 \times 1} = \frac{0.0001 \times 16}{0.4}
\]

**Arithmetic.** \(0.0001 \times 16 = 0.0016\). \(B = 0.0016 / 0.4 = 0.004\).

\[
n = \log_{10}(1/0.004) = \log_{10}(250) = 2.40
\]

\[
\text{thickness} = 2.40 \times 35 = 84 \text{ cm}
\]

**Check.** \(0.4 \times 0.004 = 0.0016\). The primary example, with \(U = 0.25\), had denominator \(400 \times 0.25 = 100\) and \(B = 1.6 \times 10^{-5}\). The ratio of those denominators is \(100 / 0.4 = 250\), and \(1.6 \times 10^{-5} \times 250 = 0.004\). \(10^{2.40} \approx 251\), and \(1/251 \approx 0.004\).

**Result means.** This leakage term may transmit 0.004. At 35 cm per tenth-value layer that is about 84 cm of ordinary concrete, near 2.4 TVL. The primary wall in the same room had to reach \(1.6 \times 10^{-5}\), about 250 times less transmission, because the useful beam is not the 0.1 percent leakage workload. Patient scatter is still a separate term and can add concrete. This 84 cm is not a finished secondary barrier.

**Wrong turns**

- Using 0.1 instead of 0.001. That is 10 percent, one hundred times the leakage fraction, and the workload becomes 40 Gy/week instead of 0.4.
- Putting \(U = 0.25\) on leakage. The denominator becomes \(0.4 \times 0.25 = 0.1\), \(B = 0.0016/0.1 = 0.016\), and the wall is thinner than the leakage term requires.
- Stopping at 84 cm and calling scatter finished. The scatter fraction was never used.
- Replacing 35 cm with the primary example’s 30 cm when the problem did not give 30 cm. \(2.40 \times 30 = 72\) cm uses the wrong TVL.

**Concrete TVL and density.** When the stem prints a TVL, use that TVL. When it does not, the teaching values for ordinary concrete are:

| Beam | Teaching TVL | Range used here |
| --- | --- | --- |
| 6 MV | about 35 cm | 34–37 cm |
| 18 MV | about 45 cm | 44–45 cm |

Ordinary concrete in this note is about 2.35 g/cm³. Lead is about 11.3 g/cm³. The teaching TVLs already belong to that concrete. A lead thickness is not the concrete TVL rescaled by \(2.35/11.3\) unless a problem asks for that comparison. These notes do not make that conversion. The 30 cm used in the primary example remains a given for that example.

**Traps.** Label the barrier primary or secondary before you pick \(U\). Write the unit of \(d\) next to the unit of \(W\). Meters with a workload at 1 m is the usual pair. For a secondary wall, write leakage and scatter on two lines before you compute either one.

**Sources.** NCRP Report 151, structural shielding design for megavoltage rooms (primary versus secondary, leakage of 0.1 percent at 1 m, \(W\), \(U\), \(T\), concrete near 2.35 g/cm³). NCRP Report 116 sets the public and occupational limits that justify the weekly \(P\). Module 36 for HVL and TVL. The 35 cm and 45 cm figures are the teaching values for items that do not supply a TVL.

## Radiation Protection and Personnel Monitoring Quiz

**Skills this quiz checks**

- Recall NCRP 116: occupational 50, 150, and 500 mSv/year (effective, lens, skin/extremity); public 1 and 15 mSv/year (effective, lens); embryo 0.5 mSv in a month after declaration; NRC gestation 5 mSv.
- Match 10 CFR 20.1201: adult 50 mSv TEDE, 150 mSv lens, 500 mSv skin, extremity, or organ. A minor is 10 percent of each (5, 15, and 50 mSv) under 10 CFR 20.1207.
- Match 10 CFR 20.1301: public 1 mSv in a year and 0.02 mSv in any one hour. Keep that hour separate from 0.02 mSv in a week.
- Choose 150 mSv for the lens when the stem says NCRP, and recognize the later ICRP lens limit as a different report.
- Apply a stated \(w_R\), including neutrons that are not automatically 20, and convert rem to mSv.
- State LNT for stochastic risk and ALARA as a practice under the ceiling. Treat investigational levels I and II as local, with no universal millisievert value in this lesson.
- Identify radiation-area and high-radiation-area signs at 0.05 mSv/h and 1 mSv/h at 30 cm.
- Apply 10 CFR 20.1502: badge an adult likely to exceed 5 mSv TEDE (10 percent of 50), a minor or declared-pregnant worker likely to exceed 1 mSv, and anyone entering a high radiation area.
- Name the HDR door interlock and the post-treatment in-room survey. Leave dwell time and the emergency crank in module 40.
- Compute primary-barrier \(B = P d^2 / (WUT)\), square the distance, and keep leakage at 0.1 percent of the useful beam with use factor 1. Keep patient scatter as a separate term.
- Use a stem TVL when it is given. Otherwise ordinary concrete is about 35 cm at 6 MV (34–37 cm) and about 45 cm at 18 MV (44–45 cm), at about 2.35 g/cm³.

## Transport of Radioactive Material: DOT Labels, Transport Index, and Package Types

**Objectives:** VI.1, VI.2

**What the exam expects:** Read a package label, compute a transport index from a 1 m reading, and say whether a shipment needs a Type A or Type B package. The rules are the Department of Transportation hazardous-materials regulations (49 CFR 173) and the NRC packaging rule (10 CFR 71); the clinic meets them mostly on the receiving end, under 10 CFR 20.1906.

**Transport index.** The transport index (TI) is the maximum dose rate 1 m from any external surface of the package, in mrem per hour, with the measured value rounded up to the next tenth. A gamma reading in mR per hour is taken as mrem per hour for this purpose. A reading of 1.23 mR/h at 1 m therefore gives a TI of 1.3, not 1.2. A surface reading or a half-metre reading is never the TI; a point-source inverse-square estimate from a closer distance only shows why (doubling the distance divides the rate by four).

**Label categories.** Three labels, chosen by the surface dose rate and the TI together, with the more restrictive of the two deciding:

- White-I: surface at most 0.5 mrem/h and no measurable dose rate at 1 m (TI 0).
- Yellow-II: surface at most 50 mrem/h and TI above 0 but at most 1.
- Yellow-III: surface at most 200 mrem/h and TI above 1 but at most 10.

Above 200 mrem/h on the surface or a TI above 10, the package may not go by ordinary carrier and must move under exclusive-use arrangements. Whether the source is sealed has nothing to do with the label; the label describes the external radiation field.

**Activity limits and package types.** The shipping tables give two activity limits per nuclide. A1 is the Type A limit for special-form material, which is a sealed, non-dispersible source. A2 is the Type A limit for normal-form, dispersible material such as a liquid or powder, and A2 is never larger than A1. A shipment at or below the relevant limit can travel in a Type A package, which is tested against normal transport conditions (a short drop, water spray, stacking, penetration). Above A1 or A2 the shipment requires a Type B package, which is designed to survive accident conditions (a 9 m drop onto an unyielding surface, a puncture test, a 30 minute fire, immersion) and is certified by the NRC under 10 CFR 71. An excepted or limited-quantity package holds only a small fraction of A1 or A2. A 10 Ci Ir-192 HDR source, well under the roughly 27 Ci A1 for Ir-192, travels Type A; a Gamma Knife Co-60 reload of thousands of curies travels Type B. There is no "Type C" in clinical shipping, and medical use does not change the package type.

**Receipt survey.** Under 10 CFR 20.1906 the licensee monitors a labelled package for surface dose rate and for removable contamination (a wipe) within 3 hours of receipt when it arrives during working hours, and within 3 hours of the start of the next working day when it arrives after hours. The survey applies to every labelled package, not only those with a measurable TI. A surface reading above 200 mrem/h, a 1 m reading above 10 mrem/h, or removable contamination above the limit is reported to the carrier and to the NRC.

**Traps.** Round the TI up. Pick the label from both the surface reading and the TI. Compare a sealed source with A1 and a liquid with A2. Three hours for the receipt survey.

**Sources.** 49 CFR 173 (DOT labels, TI, A1 and A2), 10 CFR 71 (Type A and Type B package certification), 10 CFR 20.1906 (receipt survey). The A1 value for Ir-192 is the teaching value this bank uses.

## Sealed Sources, Contamination, Waste, and Patient Release Rules

**Objectives:** VI.1, VI.2

**What the exam expects:** Convert between microcuries, becquerels, and disintegrations per minute for the leak-test and contamination limits; run the decay-in-storage clock; estimate the dose to a household member from an I-131 patient and apply the 10 CFR 35.75 release rule; place 10 CFR Part 19 among the NRC parts.

**Leak tests.** Sealed sources are wipe-tested for removable activity at intervals of up to six months (10 CFR 35.67). The limit is 0.005 microcurie, which is 185 Bq. One microcurie is 37,000 Bq, so a wipe of 0.003 microcurie is 111 Bq and passes. A source that fails is withdrawn from use, stored or returned, and reported to the NRC within five days. Sources that emit only beta or gamma below a small activity threshold, and sources in storage, are exempt from the routine test.

**Package contamination.** The removable-contamination trigger for a received package is 2,200 disintegrations per minute per 100 square centimetres for beta and gamma emitters (220 dpm per 100 square centimetres for alpha). One becquerel is one disintegration per second, so 2,200 dpm is 2,200 / 60 = 36.7 Bq per 100 square centimetres, about 0.37 Bq per square centimetre. Forgetting the minute-to-second conversion leaves 2,200; multiplying by 60 gives 132,000, which is wrong in the other direction.

**Decay-in-storage.** Under 10 CFR 35.92 a medical licensee may hold waste containing a nuclide with a physical half-life under 120 days until it has decayed. The planning rule is ten half-lives, after which about 1/1,024 of the activity (0.1 percent) remains; for I-131 at 8.0 days that is 80 days. The release criterion is a survey, not the calendar: the bag is monitored with an appropriate meter and no shielding between the meter and the waste, and it may go out as ordinary waste only when the reading is indistinguishable from background, after which the radiation labels are removed or defaced. The 120 day figure is the eligibility cut-off for the nuclide, not a holding time. The 185 Bq wipe limit is a sealed-source rule and does not apply to open waste.

**Patient release.** 10 CFR 35.75 lets a licensee release a patient when the total effective dose to any other individual is not likely to exceed 5 mSv (0.5 rem); written instructions are required when that dose could exceed 1 mSv, and a record is kept when the dose to a breast-feeding infant or child could exceed 1 mSv. NUREG-1556 provides activity-based and dose-rate-based release columns, and for I-131 the matching teaching values are 33 mCi retained activity and 7 mR/h at 1 m. The exposure rate at 1 m follows from the exposure-rate constant: for I-131 at 2.2 R per hour at 1 cm per mCi, 33 mCi gives 2.2 × 33 / 10,000 = 0.00726 R/h, about 7.3 mR/h, which is why the two columns agree. A patient-specific estimate integrates the dose rate over the retention: total dose is the initial dose rate at 1 m times the mean life (1.44 times the effective half-life) times an occupancy factor (0.25 is the usual value for a household member), with the result converted at 1 mR to about 0.01 mSv. Using the half-life instead of the mean life undercounts by about 30 percent; dropping the occupancy factor overcounts by four.

**10 CFR Part 19.** Part 19 is "Notices, Instructions and Reports to Workers; Inspection and Investigations." It requires posting the NRC Form 3 notice to employees, keeping the licence, regulations, and operating procedures available, instructing workers on the risks of radiation and on ALARA, telling a worker of the right to declare a pregnancy, providing dose reports on request and at termination, and protecting the right to request an inspection and to speak with inspectors. It sets no dose limit of its own. Dose limits are Part 20, medical use is Part 35, packaging is Part 71, and labels are DOT rules.

**Radium, historically.** Ra-226 decays to radon-222, a noble gas, so a leaking radium needle filled its storage safe with radon and its alpha-emitting daughters. Radium safes therefore required ventilation to the outdoors and the leak test was a radon-emanation test. Ir-192 and Cs-137 decay to solids and need neither. The fact survives on exams as a distractor key.

**Traps.** 185 Bq equals 0.005 microcurie. 2,200 dpm is 36.7 Bq. Ten half-lives for planning, a background survey for release. Mean life, not half-life, in the release-dose estimate. Part 19 is worker rights, not dose limits.

**Sources.** 10 CFR 35.67 (leak tests), 10 CFR 35.92 (decay-in-storage), 10 CFR 35.75 and NUREG-1556 Volume 9 Appendix U (patient release), 10 CFR 19, 10 CFR 20.1906 and 49 CFR 173.443 (package contamination).

## NCRP 147 versus 151: Design Goals, Occupancy, Workloads, Doors, and Neutrons

**Objectives:** VI.3

**What the exam expects:** Know which shielding report covers which room, quote the two weekly design goals, pick the occupancy factor for a named location, apply the IMRT factor to the right term, lay out a neutron door, and run the primary and leakage barrier formulas with the workload in the same units as the design goal. The vault-shielding lesson above has the formulas; this lesson adds the report boundaries and the table values.

**Which report.** NCRP Report 151 (2005) covers structural shielding for megavoltage photon and electron therapy facilities: linacs, Co-60, and the vaults that hold them. NCRP Report 147 (2004) covers medical x-ray imaging rooms, including CT, and it applies to a CT simulator even when the scanner sits inside a radiation-oncology department, because the shielding problem is kilovoltage scatter and leakage. AAPM TG-108 covers PET and PET/CT, where the source is the injected patient in the uptake room and the scanner room, and the 511 keV annihilation photons need about 1.5 cm of lead per tenth-value layer rather than the millimetre or so that stops diagnostic x-rays; NCRP 147 transmission data do not apply to 511 keV. NCRP Report 49 (1976) is the predecessor of both 147 and 151 and is a legacy citation.

**Design goals.** NCRP 151 and 147 use the same shielding design goals P: 0.1 mSv per week for a controlled area, which is about 5 mSv a year and a fraction of the occupational limit, and 0.02 mSv per week for an uncontrolled area, about 1 mSv a year, the public limit. The 0.02 mSv in any one hour figure from 10 CFR 20.1301 is a separate check on the hourly rate in an unrestricted area, not the weekly P; NCRP 151 handles it through the time-averaged dose-rate check.

**Occupancy.** The occupancy factor T describes the protected point, not the treatment room. The NCRP 151 teaching values: offices, nurse stations, receptionist desks, control rooms, and occupied work areas are 1; patient examination and treatment rooms are 1/2; corridors, staff lounges, and employee rest rooms are 1/5; corridor doors are 1/8; public toilets, vending areas, storage rooms, and unattended waiting rooms are 1/20; outdoor areas with transient traffic, unattended parking, stairways, and janitor closets are 1/40. Attended parking lots are also often taken at 1/40; a parking lot with an attendant booth is designed for the attendant at 1.

**Workload and the IMRT factor.** W is the weekly dose at 1 m from the target, in Gy per week; when P is in mSv, W is converted so that the units match (1 Gy is taken as 1,000 mSv for photons). IMRT delivers the same isocenter dose with several times the monitor units, and head leakage follows monitor units, so the leakage workload is the primary workload times the IMRT factor (commonly 2 to 10, with 3 to 5 typical for conventional IMRT). The primary barrier sees the useful-beam dose at isocenter, which the IMRT factor does not change, and patient scatter also scales with dose to the patient rather than with monitor units. The use factor U is 1 for leakage and scatter and a fraction (a quarter for each of four cardinal gantry angles) for the primary barrier.

**Doors and neutrons.** Above about 10 MV, photoneutrons from the head and the vault become a shielding term. A maze lowers the neutron and capture-gamma fluence at the door; a direct (maze-less) door at 15 to 18 MV must shield neutrons itself. The layered door puts borated polyethylene on the vault side, because hydrogen thermalizes the neutrons and boron captures them with a 0.48 MeV gamma, and lead outside the polyethylene to attenuate those capture gammas and the 2.2 MeV hydrogen-capture gammas from the concrete. Lead first does nothing for the neutrons and leaves the capture gammas outside the gamma shield. Steel in a wall shortens the photon TVL but does little for neutrons; polyethylene and concrete do that work.

**Traps.** NCRP 151 for the vault, 147 for the CT simulator, TG-108 for PET. 0.1 and 0.02 mSv per week. 1/40 is the parking lot. The IMRT factor multiplies leakage only. Polyethylene inside, lead outside.

**Sources.** NCRP Report 151 (design goals, occupancy table, IMRT factor, neutron and door guidance), NCRP Report 147 (imaging rooms including CT), AAPM TG-108 (PET/CT), 10 CFR 20.1301 (hourly check).

## Background Radiation, Collective Dose, Biodosimetry, and Privacy

**Objectives:** VI.1

**What the exam expects:** Quote the NCRP 160 background numbers, compute a collective dose and convert its units, compare a diagnostic dose with background, name the laboratory test that estimates an unbadged whole-body dose, and recognize a HIPAA problem in an otherwise correct clinical act.

**NCRP 160.** NCRP Report 160 (2009) puts the average annual effective dose to a resident of the United States at about 6.2 mSv, split roughly in half between natural background (about 3.1 mSv) and medical exposure (about 3.0 mSv, half of it CT). Radon and thoron decay products inhaled indoors contribute about 2 mSv of the natural half, two thirds of natural background and about a third of the total; cosmic rays, terrestrial gamma rays, and internal emitters such as potassium-40 each contribute a few tenths of a millisievert. The older "3 mSv" figure is the natural component alone or a pre-CT-era total. The public limit of 1 mSv a year applies to licensed operations and has nothing to do with background. Radon dose is delivered by alpha particles to the bronchial epithelium, which is why its equivalent dose to lung is much larger than its contribution to effective dose.

**Collective dose.** Collective effective dose is the sum of individual effective doses over a group, in person-sievert. Two hundred fifty workers averaging 1.2 mSv give 250 × 1.2 = 300 person-mSv, which is 0.30 person-Sv. Dividing back gives the mean dose per person. The mean individual dose and the collective dose are different quantities with different units, and the millisievert-to-sievert conversion is where items go wrong.

**Comparisons.** Teaching values: a chest radiograph about 0.1 mSv, an abdomen or pelvis CT about 8 to 10 mSv, so one abdomen CT is about 80 chest radiographs, about three years of natural background at 3.1 mSv a year, and about one sixth of the 50 mSv occupational limit.

**Biodosimetry.** When a worker is exposed in an accident without a dosimeter, cytogenetic dosimetry estimates the acute whole-body dose from the worker's own blood: lymphocytes are cultured and the frequency of dicentric chromosomes (two centromeres, produced by misrepair of radiation-induced breaks) is read against a laboratory calibration curve. The method detects acute whole-body doses down to roughly 0.1 to 0.2 Gy. A colleague's badge measures the colleague. A thyroid count measures internal iodine. Skin erythema appears only above several grey, days later, and reflects local skin dose. Lymphocyte count depletion over the first days is the clinical triage indicator for higher doses, not the laboratory estimate.

**Privacy.** HIPAA's Privacy Rule protects individually identifiable health information (PHI) and permits use and disclosure without patient authorization for treatment, payment, and health-care operations, under a minimum-necessary standard; the Security Rule requires administrative, physical, and technical safeguards for electronic PHI. Plan approval inside the record-and-verify system and billing the payer are permitted uses. A properly de-identified teaching example (name, record number, dates, and the other identifiers removed) is no longer PHI. A screenshot with the patient's name sent to a personal phone outside the clinic's safeguards is a Privacy and Security Rule violation regardless of clinical intent. The dose numbers themselves are not protected; the identifiers are.

**Traps.** 6.2 mSv total, 3.1 natural, radon about 2. Person-sievert, not sievert. Dicentrics for whole-body dose. HIPAA protects identifiers, and treatment, payment, and operations are permitted uses.

**Sources.** NCRP Report 160 (2009) for background and medical dose; ICRP and IAEA biodosimetry guidance for the dicentric assay; 45 CFR Parts 160 and 164 (HIPAA Privacy and Security Rules).

## Magnitude Ladders: Out-of-Field Dose, ALARA Levels, Exposure Rates, Shielding, and QA Errors

**Objectives:** VI.1, VI.2, VI.3

**What the exam expects:** Order-of-magnitude recall. The item gives a distance, a room, a staff group, or a planning error and asks which figure belongs to it, or gives a course dose and a distance and asks for an estimate. Nobody expects three significant figures; the test is whether you place the number on the right rung. Alongside the ladders sit four regulatory facts that the earlier lessons left out: the model-program ALARA levels, how often the radiation safety committee meets, the iodine bioassay window, and the nuclear-medicine survey cadence.

**Out-of-field (peripheral) dose ladder.** Expressed as a fraction of the central-axis dose at depth, the dose outside a megavoltage field falls from about 5 percent at 2 cm beyond the field edge (penumbra tail plus patient scatter), to about 1 percent at 10 cm, to about 0.2 to 0.5 percent at 30 cm, where head leakage (at most 0.1 percent of the useful beam by regulation, measured at 1 m) and collimator scatter set the floor. Higher energies, larger fields, and wedges or more monitor units (IMRT) raise the far rungs; a lead bridge or a thicker-walled head lowers them. The same ladder gives the device dose for a pacemaker (module 31) and the fetal dose for a pregnant patient (AAPM TG-36).

**Fetal-dose worked estimate.** Given: 50 Gy course, uterus 30 cm from the field edge, unshielded peripheral fraction about 0.3 percent. Unshielded estimate: \(50 \times 0.003 = 0.15\) Gy, inside the 0.1 to 0.25 Gy band that 0.2 to 0.5 percent predicts. A lead bridge over the abdomen typically cuts the peripheral dose by a factor of 2 to 4: \(0.15 / 3 = 0.05\) Gy. Check: \(0.05 \times 3 = 0.15\). Result means: the shielded estimate lands in the 0.05 to 0.1 Gy region where TG-36 expects shielding, careful field choice, and a documented risk discussion; it is not a prohibition. Doses well above that band, and especially above about 0.5 Gy, are where deterministic risks (growth retardation, mental retardation in weeks 8 to 15) begin to dominate the discussion.

**ALARA investigational levels and the committee.** The earlier lesson says each licensee writes its own levels, and that stays true. The figures most programs copy come from the NRC model program (Regulatory Guide 8.18 for medical institutions): Level I is about 10 percent of the applicable quarterly limit and Level II about 30 percent. With a quarterly whole-body limit of 12.5 mSv (a quarter of 50 mSv), Level I is \(0.10 \times 12.5 = 1.25\) mSv and Level II is \(0.30 \times 12.5 = 3.75\) mSv per quarter. Crossing Level I: the RSO reviews how the dose was received and records the finding; crossing Level II: the RSO investigates and takes corrective action to lower future dose. Both are reviewed by the radiation safety committee, which 10 CFR 35.24 requires to meet at least quarterly. When a stem names Reg Guide 8.18 or "the model program," answer 10 and 30 percent of the quarterly limit; when it says "the clinic's program," the clinic's numbers govern.

**Declared pregnancy can be withdrawn.** The declaration is voluntary and written (10 CFR 20.1003, 20.1208). The worker may withdraw it in writing at any time; after withdrawal the 5 mSv gestation limit and the 0.5 mSv monthly recommendation stop applying and the adult limits return. Neither the RSO nor a physician decides for her.

**Thyroid bioassay.** After handling large quantities of volatile I-131 or I-125 in open form (therapy capsule preparation, a spill, a broken vial), Regulatory Guide 8.20 asks for a thyroid probe count between about 6 hours (so the iodine has reached the gland) and 72 hours (before the 8 day physical half-life and biological clearance erase the signal). A whole-body count is for nuclides that distribute generally; iodine is counted at the neck.

**Nuclear-medicine survey cadence (10 CFR 35.70).** A meter survey of preparation and administration areas at the end of each day of use for radiopharmaceuticals that need a written directive, and a wipe survey for removable contamination weekly. The meter finds spills and misplaced sources; the wipe finds contamination too diffuse to see on a meter. Quarterly is the sealed-source inventory; semi-annual is the leak test.

**Occupational dose ladder, highest first.** Interventional radiologists and cath-lab staff (standing beside the patient during fluoroscopy; several millisieverts a year at the collar, more under heavy loads), then nuclear-medicine and PET technologists (the injected patient is an unshielded source; a few millisieverts), then diagnostic radiographers, and radiation therapists last (outside a shielded vault; usually under 1 mSv, near background). Nobody in routine practice approaches 50 mSv, which is why ALARA levels live in low single-digit millisieverts.

**Patient exposure-rate ladder.** Beside a freshly dosed 100 to 150 mCi I-131 patient, on the order of 100 mR/h; at 1 m, about 20 to 30 mR/h at first (the 2.2 R per hour per mCi at 1 cm constant gives \(2.2 \times 150 / 10{,}000 = 33\) mR/h); the visitor line is placed where the rate has fallen to about 1 to 2 mR/h. A permanent prostate seed implant (I-125 or Pd-103) reads about 0.1 mR/h at 1 m through the pelvis at discharge. Natural background is about 0.01 to 0.02 mR/h. The ladder spans four orders of magnitude, and dose rate always falls with distance even when the patient is the source.

**Shielding-thickness ladder.** Linac primary barrier about 2 to 2.5 m of ordinary concrete (6 to 18 MV, busy workload), secondary barrier about 1 m, HDR Ir-192 vault about 0.5 to 0.6 m of concrete, CT simulator about 1.5 mm of lead in the walls, PET uptake and scan rooms 3 to 25 mm of lead depending on workload and distance (511 keV photons have a lead tenth-value layer of about 1.5 cm), and a high-energy vault door of lead over borated polyethylene (polyethylene on the vault side to thermalize and capture neutrons, lead outside it for the capture gamma rays). Mixing up the linac and HDR rungs, or the CT and PET rungs, is the usual distractor.

**Three-tier sign wording.** "Caution, Radiation Area": more than 0.05 mSv (5 mrem) in one hour at 30 cm. "Caution" or "Danger, High Radiation Area": more than 1 mSv (100 mrem) in one hour at 30 cm. "Grave Danger, Very High Radiation Area": more than 5 Gy (500 rad) absorbed dose in one hour at 1 m. The top tier changes both the quantity (gray, not sievert) and the distance (1 m, not 30 cm), and only the top tier uses "Grave Danger."

**QA error-magnitude ladder.** Largest first. Normalising to the 50 percent isodose when the prescription meant 100 percent: doubles the dose (100 percent). A wedge computed into the MU but left out of the beam: dose high by \(1 / \mathrm{WF}\), from about 25 percent (WF 0.80) to 300 percent (WF 0.25); the reverse error (wedge in the beam, factor omitted) gives a dose low by the factor itself, for example 40 percent low at WF 0.60. Lung heterogeneity correction on versus off: 5 to 30 percent at the target, depending on energy and path length. A 1 cm SSD error at a nominal 100 cm: inverse square, \((100/101)^2 = 0.98\), about 2 percent. Check for the wedge case: \(1 / 0.60 = 1.667\), and \(1.667 \times 0.60 = 1.0\).

**Wrong turns**

- Using the 2 cm figure (about 5 percent) at 30 cm, which inflates a fetal estimate tenfold, or the 30 cm figure at 2 cm.
- Applying the 10 and 30 percent ALARA fractions to the annual 50 mSv instead of the quarterly 12.5 mSv.
- Reading the very-high-radiation-area sign as "1 mSv at 30 cm with stronger words"; it is 5 Gy at 1 m.
- Putting the thick lead on the CT room and the thin lead on the PET room.
- Treating a 1 cm SSD error as a 10 percent event; at 100 cm it is about 2 percent (at a 20 cm orthovoltage SSD it would be about 10 percent, module 7).

**Traps.** Read the distance and the quantity on every sign and ladder: 30 cm versus 1 m, sievert versus gray, quarterly versus annual, central-axis percent versus absolute dose. For a wedge error, decide first whether the wedge was in the beam or in the calculation.

**Sources.** AAPM TG-36 (fetal dose) and TG-203 (implanted devices) for peripheral dose; NRC Regulatory Guides 8.18 (ALARA for medical institutions), 8.20 (iodine bioassay), and 10 CFR 20.1003, 20.1208, 20.1902, 35.24, 35.70; NCRP 151, NCRP 147, and AAPM TG-108 for the shielding rungs; NCRP 160 and UNSCEAR occupational summaries for the staff-dose ladder; Khan and Gibbons for the wedge, normalisation, and inverse-square arithmetic.
