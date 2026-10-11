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
