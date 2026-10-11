# Module 44. Practice test

Original notes for MDCB CMD prep. The items in this file are original drills. They are not retired MDCB items, and they are not copied from a commercial question bank. Use them to practice the arithmetic in modules 33–43. A score on this set is not a scaled exam score.

## The Format

**Objectives:** all domains, exam mechanics

**What the exam expects:** You know the clock, the item count, the performance-based items, and the domain weights before you sit down, so a hard calculation does not steal the time that belongs to a short memory item.

The CMD exam, from the public handbook and the 2023 job-task blueprint:

- **155 items**, a few of them unscored pilots mixed in, so the scored total is slightly under 155.
- **3 hours 50 minutes** (230 minutes). About \(230/155 \approx 1.48\) minutes per item, roughly **90 seconds**.
- English only, U.S. practice.
- Most items are multiple choice. A small number are **performance-based in ProKnow**: plan evaluation, isodose display, DVH, anatomy, beam arrangement, contouring. Those items want you to look at a plan, not to type a formula.
- Domain weights, and the approximate item counts \(155 \times\) weight:

| Domain | Weight | About how many of the 155 | Where these notes live |
| --- | --- | --- | --- |
| I Radiation physics | 14% | 22 | modules 2–12, plus transmission and units in 36 |
| II Localization | 8% | 12 | modules 13–18 and 32, plus DIR in 38 |
| III Treatment planning | 42% | 65 | modules 19–31 and QUANTEC in 43 |
| IV Dose calculation | 13% | 20 | modules 33–39 |
| V Brachytherapy | 5% | 8 | module 40 |
| VI Radiation protection | 9% | 14 | module 41 |
| VII QA and standard of care | 9% | 14 | module 42 |

\(0.14+0.08+0.42+0.13+0.05+0.09+0.09 = 1.00\), and the approximate counts \(22+12+65+20+8+14+14 = 155\). Pilots and rounding mean a given form will not hit these integers exactly.

**How to use an original practice set**

1. Cover the solutions. Closed notes. Time yourself at about 90 seconds per item for a sprint, or untimed when the goal is the arithmetic rather than the clock.
2. On every calculation, write the given data, the formula, the symbol definitions, the substitution, the arithmetic, a reverse check, and one sentence on what the number means. That is the same shape as the worked examples in modules 33–43.
3. Grade the setup, not only the final choice. An inverted wedge (underdose versus overdose) is a miss even if a later arithmetic slip lands on a familiar number.
4. The same day, redo any miss in the theory file it came from. Do not memorize this set’s answers. The next form will change the SSD and the wedge factor.
5. After the sprint, sort misses by domain weight. A repeated planning miss (42%) outranks a repeated bonus-module miss. A repeated MU or gap miss still matters because those items are fast points inside the 13% dose-calculation domain if the setup is clean, and they are lost entirely if PDD and TMR get mixed.

**What a ProKnow item is asking.** You will see a plan, not a formula sheet. Typical jobs: read a DVH against a stated constraint, name a hot spot on an isodose colorwash, identify an organ on an axial slice, or judge whether a beam arrangement includes a wedge or a half-beam. Grid size, contour quality, and algorithm still limit what that picture proves (module 39). The original sets below are paper calculations so you can practice the arithmetic the performance items will not walk through for you.

**Sources.** MDCB CMD exam handbook (time, language, item count, ProKnow) and the 2023 test-specifications matrix (domain weights).

## Practice Exam 1

**Objectives:** IV.1–IV.3, IV.6, V.6, VI.1, I.10

**What the exam expects:** A written setup on every item: given data, formula, substitution, arithmetic, a reverse check, and one sentence on what the number means. These items are original. They are not a retired form.

**Sources.** The worked examples in modules 33–36, 40, and 41. Khan and Gibbons for the underlying formulas.

Fifteen original items. Calibration, whenever an MU is required: **1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm.** Solutions start after the last item.

1. A cobalt beam delivers 240 cGy/min at SAD 100 cm. Inverse square only: what is the dose rate 80 cm from the source?

2. A PDD at SSD 100 cm, depth 10 cm, is 67.5%. Depth of dmax is 1.5 cm. Estimate the PDD at SSD 120 cm with Mayneord F. What does F not correct?

3. Open field 8 cm × 12 cm. Equivalent square side, by both \(2ab/(a+b)\) and \(4A/P\).

4. PDD is 73.2% at 8.0 cm and 67.2% at 10.0 cm. Interpolate to 9.0 cm.

5. Prescription 180 cGy at the calibration point. Open output 1.0 cGy/MU. Wedge factor 0.65. The wedge is in the beam and the factor was omitted from the MU. What dose is delivered, and what is delivered/prescribed?

6. Two photon fields on the skin, lengths 24 cm and 12 cm, both at SSD 100 cm. Skin gap so the geometric edges meet at 5.0 cm depth.

7. Breast tangent length 24 cm at SAD 100 cm. Couch kick so the superior border follows a half-beam supraclavicular field. State the assumption.

8. A shield is exactly two HVLs thick. Incident dose 80 cGy. Transmitted dose?

9. Geometric penumbra. Source size 1.0 cm, SSD 100 cm, depth 1.5 cm, source-to-diaphragm 50 cm. Also name the 80%–20% width at dmax.

10. Cobalt timer. 0.50 min reads 45 cGy. 1.50 min reads 165 cGy. Find the timer error, the dose rate, and the set time for 240 cGy.

11. SAD MU. Point at isocenter. Dose 180 cGy. TMR 0.750. \(S_c = S_p = \mathrm{WF} = \mathrm{TF} = 1\). Same calibration as the header.

12. SSD MU. Dose 180 cGy. PDD 60%. \(\mathrm{SSD}+d_m = 100\) cm so the inverse-square factor is 1. All other factors 1. Same calibration. Which depth quantity is forbidden in this formula?

13. Permanent I-125 implant. Initial dose rate 4.0 cGy/h. Half-life 59.4 days. Total dose after complete decay, using 1.443.

14. Cs-137 exposure rate. \(\Gamma = 3.26\) R cm² mCi⁻¹ h⁻¹, activity 20 mCi, distance 50 cm.

15. Equivalent dose. 0.10 cGy of photons (\(w_R = 1\)) and 0.05 cGy of neutrons at a stated \(w_R = 10\). Report rem and mSv.

### Solutions

**1. Inverse square**

Given: \(I_1 = 240\) cGy/min at \(d_1 = 100\) cm. Find \(I_2\) at \(d_2 = 80\) cm.

Formula: \(I_2 = I_1 (d_1/d_2)^2\). Distances are from the source.

Substitute: \(I_2 = 240 \times (100/80)^2 = 240 \times 1.5625\).

Arithmetic: \(240 \times 1.5 = 360\), \(240 \times 0.0625 = 15\), total **375 cGy/min**.

Check: \(375 \times (80/100)^2 = 375 \times 0.64 = 240\).

Meaning: the point is closer than isocenter, so the rate rises. The unsquared wrong turn is \(240 \times 1.25 = 300\). The inverted wrong turn is \(240 \times 0.64 = 153.6\), which is the rate at 125 cm, not at 80 cm.

**2. Mayneord**

Given: \(\mathrm{PDD}_1 = 67.5\%\), \(\mathrm{SSD}_1 = 100\), \(\mathrm{SSD}_2 = 120\), \(d_m = 1.5\), \(d = 10\), all cm.

Formula: \(F = [( \mathrm{SSD}_2+d_m)/(\mathrm{SSD}_1+d_m)]^2 \times [( \mathrm{SSD}_1+d)/(\mathrm{SSD}_2+d)]^2\).

Substitute: \(F = (121.5/101.5)^2 \times (110/130)^2\).

Arithmetic: \(121.5/101.5 = 1.19704\), squared \(= 1.43291\). \(110/130 = 0.846154\), squared \(= 0.71598\). \(F = 1.43291 \times 0.71598 = 1.0259\). New PDD \(= 67.5 \times 1.0259 = 69.25\%\).

Check: \(67.5 \times 0.0259 \approx 1.75\), and \(67.5 + 1.75 = 69.25\).

Meaning: extended SSD raises PDD slightly, from 67.5% to 69.25%. **F corrects inverse square only, not scatter.** Dropping the squares gives about \(1.197 \times 0.846 \approx 1.013\) and a PDD near 68.4%, the usual distractor. Do not apply F to a TMR.

**3. Equivalent square**

\(2 \times 8 \times 12 / (8+12) = 192/20 = 9.6\) cm.

Area \(= 96\), perimeter \(= 2(8+12) = 40\), \(4A/P = 384/40 = 9.6\) cm.

Check: both forms match. The arithmetic mean 10 cm and \(\sqrt{96} \approx 9.8\) cm are the nearby wrong answers. A percent-blocked shortcut is not this formula.

Meaning: look up scatter quantities on the 9.6 cm square row.

**4. Interpolation**

Fraction \(= (9.0-8.0)/(10.0-8.0) = 0.50\).

PDD \(= 73.2 + 0.50(67.2-73.2) = 73.2 - 3.0 = 70.2\%\).

Check: the midpoint of 73.2 and 67.2 is \((73.2+67.2)/2 = 70.2\).

Meaning: use 70.2% at 9 cm. Averaging is legal here only because the depth is midway.

**5. Wedge omitted**

Given: calibration 1.0 cGy/MU at dmax, 10×10, SAD 100. \(D = 180\) cGy. WF = 0.65. Wedge physically in the beam. MU calculated as \(180/1.0 = 180\).

Delivered \(= 180 \times 0.65 = 117\) cGy. Ratio \(= 117/180 = 0.65\).

Check: \(180 \times 0.65 = 117\).

Meaning: the patient receives 65% of the prescription, an underdose by about the wedge factor. The overdose distractor is the other story: factor included (MU \(= 180/0.65 = 276.9\)) and wedge not inserted, which would deliver about 277 cGy.

**6. Gap**

Formula: \(\mathrm{gap} = (L_1/2)(d/\mathrm{SSD}_1) + (L_2/2)(d/\mathrm{SSD}_2)\). \(L\) is the field length on the skin.

Substitute: \((24/2)(5/100) + (12/2)(5/100) = 12 \times 0.05 + 6 \times 0.05 = 0.60 + 0.30 = 0.90\) cm.

Check: \(0.60+0.30 = 0.90\).

Meaning: light fields are 0.90 cm apart on the skin so the geometric edges meet at 5 cm. A zero gap overlaps at depth. Half-beam match borders would have used gap 0 instead of this formula.

**7. Breast couch kick**

\(\theta = \arctan((0.5 \times 24)/100) = \arctan(0.12) = 6.84^\circ\).

Check: \(\tan(6.84^\circ) \approx 0.12\).

Assumption: the supraclavicular field is half-beam blocked inferiorly, so its inferior border does not diverge, and the tangent length is the superior–inferior opening at isocenter. The couch kick uses this 24 cm length. The posterior border is a gantry or half-beam adjustment. This matches borders. It is not a lung DVH.

**8. Two HVLs**

Transmission through 2 HVL \(= (1/2)^2 = 0.25\). \(I = 80 \times 0.25 = 20\) cGy.

Check: 80 → 40 → 20.

Meaning: 20 cGy transmitted, 60 cGy removed. One TVL would have transmitted 8 cGy (10%), which is the distractor if someone treats two HVLs as a tenth-value layer. Three HVLs would transmit 10 cGy (12.5%), still not one TVL.

**9. Penumbra**

\(P = s(\mathrm{SSD}+d-\mathrm{SDD})/\mathrm{SDD} = 1.0 \times (100+1.5-50)/50 = 51.5/50 = 1.03\) cm.

Check: \(51.5/50 = 1.03\).

Meaning: geometric penumbra at that depth is 1.03 cm. The **physical** penumbra is the 80%–20% dose width at dmax, a measured width, not this formula. SDD in the denominator is source-to-diaphragm, not SSD.

**10. Timer**

Formula: \(R = \dot{D}(t+\tau)\).

\(165/45 = 11/3 = (1.50+\tau)/(0.50+\tau)\).

\(3(1.50+\tau) = 11(0.50+\tau)\) → \(4.50 + 3\tau = 5.50 + 11\tau\) → \(-1 = 8\tau\) → \(\tau = -0.125\) min.

\(\dot{D} = 45 / (0.50-0.125) = 45/0.375 = 120\) cGy/min.

Effective time for 240 cGy \(= 240/120 = 2.00\) min. Set time \(= 2.00 - (-0.125) = 2.125\) min.

Check: \(120 \times (2.125-0.125) = 240\). Second reading: \(120 \times (1.50-0.125) = 120 \times 1.375 = 165\).

Meaning: transit removes 0.125 min from every run, so the timer is set longer than the ideal 2.00 min. Setting 2.00 min delivers \(120 \times 1.875 = 225\) cGy. Half-life does not belong in this solution.

**11. SAD MU**

Formula (no PDD): \(\mathrm{MU} = D / (\dot{D}_{\mathrm{cal}} \times \mathrm{TMR})\), with the inverse-square term equal to 1 at isocenter.

Calibration: 1.0 cGy/MU at dmax, 10×10, SAD 100.

\(\mathrm{MU} = 180 / 0.750 = 240\).

Check: \(240 \times 0.750 = 180\) cGy.

Meaning: 240 MU. Putting the 60% PDD from item 12 into this SAD setup is the mix the formula forbids.

**12. SSD MU**

Formula (no TMR): \(\mathrm{MU} = D / (\dot{D}_{\mathrm{cal}} \times \mathrm{PDD}/100 \times \mathrm{ISF})\).

ISF \(= 1\) because dmax is at 100 cm. \(\mathrm{MU} = 180 / 0.60 = 300\).

Check: \(300 \times 0.60 = 180\) cGy.

Meaning: 300 MU. **TMR is the depth quantity forbidden in this formula.** PDD is forbidden in item 11. Same dose, different MU, because 60% and 0.750 are not the same setup.

**13. Permanent implant**

\(T_{1/2} = 59.4 \times 24 = 1425.6\) h.

Mean life \(= 1.443 \times 1425.6 = 2057.1\) h.

\(D = 4.0 \times 2057.1 = 8228.6\) cGy.

Check: \(1.443 \times 1400 = 2020.2\), \(1.443 \times 25.6 = 36.94\), sum 2057.14, times 4 is 8228.6.

Meaning: complete decay delivers about 82.3 Gy. Omitting 1.443 leaves \(4 \times 1425.6 = 5702\) cGy, the half-life mistake. This factor is not used on an HDR dwell of a few minutes.

**14. Exposure rate**

\(X = \Gamma A / d^2 = 3.26 \times 20 / 50^2 = 65.2 / 2500 = 0.02608\) R/h \(= 26.1\) mR/h.

Check: \(50^2 = 2500\), \(3.26 \times 20 = 65.2\), \(65.2/2500 = 0.02608\).

Meaning: about 26.1 mR/h at 50 cm. Forgetting the square gives \(65.2/50 = 1.304\) R/h. Using Ir-192’s 4.69 in place of 3.26 is the wrong nuclide. Distance must be in centimetres because \(\Gamma\) is in cm².

**15. Equivalent dose**

\(H = 0.10 \times 1 + 0.05 \times 10 = 0.10 + 0.50 = 0.60\) rem \(= 6.0\) mSv.

Check: 0.10 rem = 1 mSv and 0.50 rem = 5 mSv.

Meaning: 6 mSv equivalent dose. The absorbed-dose sum 0.15 cGy is the distractor that drops \(w_R\). Neutron \(w_R\) is 10 because the stem said so, not because every neutron is 20.

## Practice Exam 2

**Objectives:** IV.3–IV.6, III.8, V.6, VI.1, VI.3, VII.5, VII.8, VII.9

**What the exam expects:** The same written setup as Practice Exam 1, now across heterogeneity, EQD2, QUANTEC, grid size, shielding, cutout factor, and deliverability. Original items, not a retired form.

**Sources.** Modules 37–43 and 45. QUANTEC 2010 summaries and TG-142 tolerances as stated in those notes.

Another fifteen original items. Same calibration sentence when an MU appears: **1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm.**

1. Tumor dose 180 cGy. PDD at the tumor is 75%. What is the given dose at dmax?

2. Hinge angle between two wedged beams is 100°. Wedge angle for a symmetric pair?

3. A ray crosses 2.0 cm soft tissue (density 1.00), 10.0 cm lung (density 0.25), and 1.0 cm soft tissue. Water-equivalent depth and physical depth.

4. Prior course: 46 Gy in 2 Gy fractions to an organ with \(\alpha/\beta = 3\) Gy. New course, already mapped by DIR: 5 fractions of 4 Gy. Biological sum in EQD2, and the physical sum.

5. TG-43 at the reference point, all relative functions equal to 1. \(S_K = 5000\) U, \(\Lambda = 1.12\) cGy h⁻¹ U⁻¹. Dose rate?

6. A radiation worker has 20 mSv effective dose this year. How much remains under the NCRP 116 annual occupational effective limit? Which number is the ICRP lens distractor doing in this item? (It does not belong.)

7. Daily output reads 1.028 cGy/MU against a 1.000 baseline. Percent difference, and how it sits against the daily 3% and monthly 2% windows.

8. Conventional lung DVH: V20 = 34%, mean lung dose 18 Gy. Apply the QUANTEC pair (V20 ≤ 30%, mean 20 Gy associated with about 20% pneumonitis). These are 2010 summary estimates, not a prescription.

9. Contrast 4.0 cm thick is assigned density 1.30. Urine is density 1.00. Extra water-equivalent thickness, and the override.

10. Cord samples every 2 mm: 48.0, 51.0, 54.2, 50.5, 47.0 Gy. A 6 mm grid keeps only 48.0 and 50.5. Reported maximum, true maximum, and the miss.

11. Convert 45 to binary. Convert binary 1101 to decimal. Convert 0.625 to binary.

12. Clarkson. TAR at the field is 0.820. Zero-area TAR is 0.450. What is the scatter-air ratio, and which term is primary?

13. Primary barrier. \(P = 1.0 \times 10^{-4}\) Gy/week, \(d = 5\) m, \(W = 500\) Gy/week at 1 m, \(U = 0.25\), \(T = 1\). Transmission \(B\).

14. Electron cutout factor measured as 0.880. Open-cone calibration 1.0 cGy/MU at dmax. Dose wanted at dmax: 200 cGy. MU with the factor, and dose if the factor is omitted while the cutout is in the beam.

15. One VMAT arc, 360°, 900 MU. Maximum gantry speed 6°/s. Maximum dose rate 600 MU/min. What gantry speed lets the arc deliver 900 MU, and why 6°/s is not enough?

### Solutions

**1. Given dose**

\(D(d_{\max}) = 180 / 0.75 = 240\) cGy.

Check: \(240 \times 0.75 = 180\).

Meaning: dmax must receive 240 cGy for the tumor to receive 180 cGy at 75% PDD. Multiplying \(180 \times 0.75 = 135\) answers the reverse question. TMR does not enter.

**2. Hinge**

Wedge angle \(= 90 - (100/2) = 90 - 50 = 40^\circ\).

Check: hinge \(= 2(90-40) = 100^\circ\).

Meaning: a symmetric pair with a 100° hinge uses 40° wedges. Wedge angle = hinge/2 gives the distractor 50°.

**3. Effective depth**

\(d_{\mathrm{eff}} = 2.0(1) + 10.0(0.25) + 1.0(1) = 2 + 2.5 + 1 = 5.5\) cm.

Physical depth \(= 13.0\) cm.

Check: \(10 \times 0.25 = 2.5\), and \(13.0 - 5.5 = 7.5\), which is the lung’s “missing” water \(10-2.5\).

Meaning: look up a path-length correction at 5.5 cm of water, not at 13 cm. A pencil beam can do this longitudinal step and still fail the lateral scatter in lung. Monte Carlo is the interface method. Override nothing here: the stem already gave lung density 0.25.

**4. EQD2**

Old course is already 2 Gy per fraction, so EQD2 = 46 Gy.

New: \(D = 20\) Gy, \(d_f = 4\). \(\mathrm{EQD2} = 20 \times (4+3)/(2+3) = 20 \times 7/5 = 28\) Gy.

Biological sum \(= 46+28 = 74\) Gy EQD2. Physical sum \(= 46+20 = 66\) Gy.

Check: \(20 \times 1.4 = 28\). \(74-66 = 8\).

Meaning: after DIR, the biological accumulation is 74 Gy EQD2. Adding 66 Gy of physical dose understates it for \(\alpha/\beta = 3\). If the anatomies were never deformed onto one frame, do not add the grids at all. Weight loss would break the sum even with a DIR.

**5. TG-43**

\(\dot{D} = 5000 \times 1.12 \times 1 \times 1 \times 1 = 5600\) cGy/h.

Check: \(5000 \times 1.12 = 5600\).

Meaning: 56 Gy/h at the reference point for this strength. Moving to 2 cm on a point-source geometry multiplies by \((1/2)^2 = 0.25\) before \(g(r)\) and \(F\). Leaving the square off is the usual geometry miss.

**6. NCRP remaining**

Limit 50 mSv effective in a year. Remaining \(= 50-20 = 30\) mSv.

Check: \(20+30 = 50\).

Meaning: 30 mSv of occupational effective dose remains under NCRP 116. The public limit of 1 mSv is the wrong row. The later ICRP occupational lens limit (20 mSv) is not this item: the quantity in the stem is effective dose, the report is NCRP, and the lens NCRP number would have been 150 mSv anyway.

**7. Output window**

\((1.028-1.000)/1.000 = 2.8\%\).

Check: \(1.028-1 = 0.028\).

Meaning: inside the daily constancy window of about 3%, outside the monthly window of about 2%. Name which check you are doing. The annual TG-51 comparison is about 1%, so 2.8% would fail that one too. The door interlock is a separate daily pass/fail and is not measured in cGy/MU.

**8. QUANTEC lung**

V20 of 34% is above 30%. Mean dose 18 Gy is below 20 Gy.

Meaning: the pair is not satisfied. The 2010 summary associates V20 ≤ 30% and mean dose 20 Gy with about a 20% pneumonitis risk; this plan’s V20 is the failing limb. One passing limb does not clear the pair. This is not a prescription for a named patient.

**9. Contrast override**

Extra path \(= 4.0(1.30-1.00) = 1.2\) cm.

Check: \(4 \times 1.3 = 5.2\), and \(5.2-4.0 = 1.2\).

Meaning: override the contrast contour to density 1.00. Contrast is not tissue. Leaving 1.30 in the plan over-attenuates and underestimates dose beyond the bladder.

**10. Dose grid**

True maximum 54.2 Gy. Reported maximum 50.5 Gy. Miss \(= 3.7\) Gy.

Check: \(50.5+3.7 = 54.2\).

Meaning: a coarse grid under-reports a narrow cord peak. The DVH will confidently display 50.5 Gy and will not show that the peak was skipped. Recalculate on a finer grid.

**11. Binary**

45: divide by 2 and read remainders upward. \(45=22\times2+1\), \(22=11\times2+0\), \(11=5\times2+1\), \(5=2\times2+1\), \(2=1\times2+0\), \(1=0\times2+1\). Binary **101101**.

Check: \(32+8+4+1 = 45\).

1101 binary \(= 8+4+1 = 13\) decimal.

0.625: \(0.625\times2 = 1.25\) → 1; \(0.25\times2 = 0.50\) → 0; \(0.50\times2 = 1.00\) → 1. Binary **0.101**.

Check: \(1/2 + 0/4 + 1/8 = 0.625\).

**12. Clarkson**

SAR \(= 0.820 - 0.450 = 0.370\).

Check: \(0.450+0.370 = 0.820\).

Meaning: primary is the zero-area TAR, 0.450. Scatter is 0.370. Clarkson keeps them apart and integrates scatter over sectors. Percent of area blocked does not do that split.

**13. Barrier**

\(B = P d^2 / (WUT) = (1.0\times10^{-4})(25) / (500 \times 0.25 \times 1)\).

\(WUT = 125\). \(P d^2 = 0.0025\). \(B = 0.0025/125 = 2.0 \times 10^{-5}\).

Check: \(125 \times 2.0 \times 10^{-5} = 0.0025\).

Meaning: the primary wall must transmit no more than \(2.0\times10^{-5}\) of the useful beam. Forgetting \(d^2\) uses 5 instead of 25 and is low by a factor of 5. Leakage on a secondary barrier would use use-factor 1, not 0.25.

**14. Cutout**

Calibration stated: 1.0 cGy/MU at dmax for the open cone.

MU \(= 200/(1.0\times0.880) = 227.3\).

Check: \(227.27 \times 0.880 = 200\).

If the factor is omitted and the cutout is still in the beam: dose \(= 200 \times 0.880 = 176\) cGy, ratio 0.880.

Meaning: measure small-field electron cutouts. The omitted-factor underdose is the same pattern as a wedge left out of the MU.

**15. Deliverability**

At 6°/s, 360° takes 60 s and 600 MU/min can deliver only 600 MU. The plan needs 900 MU, which takes \(900/600 = 1.5\) min = 90 s. Gantry speed \(= 360/90 = 4.0\)°/s.

Check: \(4\times90 = 360\). \(600 \times 1.5 = 900\).

Meaning: the arc is deliverable only if the gantry slows to 4°/s and the leaves can follow. Maximum gantry speed cannot carry 900 MU at a 600 MU/min ceiling. Collision and carriage travel are separate holds even when this speed works.
