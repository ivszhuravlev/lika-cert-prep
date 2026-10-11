# Module 35. PDD, TMR, and MU calculations

Original notes for MDCB CMD prep. Objectives IV.1 and IV.3.

Two formulas in this module are never mixed in one line. An SSD calculation uses percent depth dose. An SAD calculation uses TMR. Mayneord F corrects inverse square inside a PDD only. It does not correct scatter.

**Calibration used for every MU example below:** 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm. That means 1 MU delivers 1.0 cGy when dmax of a 10×10 field sits 100 cm from the source.

## Interpolation Tutorial (No Formula)

**Objectives:** IV.3

**What the exam expects:** The lesson title means there is no new named physics quantity. The skill is linear interpolation between two rows of a PDD, TMR, or output table. Do not extrapolate far past the table and call it the same operation.

The arithmetic is

\[
y = y_1 + \frac{x - x_1}{x_2 - x_1}(y_2 - y_1)
\]

- \(x\): the depth or field size you need
- \(x_1, x_2\): the neighboring table entries, with \(x_1 < x < x_2\)
- \(y_1, y_2\): the table values at \(x_1\) and \(x_2\)
- \(y\): the interpolated value

### Worked example

**Given.** A PDD table lists 67.5% at 10.0 cm and 64.3% at 11.0 cm. Find PDD at 10.4 cm. Same field, same SSD, so the only change is depth.

**Substitute.**

\[
\frac{10.4 - 10.0}{11.0 - 10.0} = 0.40
\]

\[
y = 67.5 + 0.40(64.3 - 67.5) = 67.5 + 0.40(-3.2)
\]

**Arithmetic.** \(0.40 \times 3.2 = 1.28\). \(67.5 - 1.28 = 66.22\%\).

**Check.** The point is 40% of the way from 10.0 to 11.0, so it should be 40% of the way from 67.5 to 64.3. Distance still to go: \(64.3\) is \(66.22 - 64.3 = 1.92\) below the answer, and \(1.28 + 1.92 = 3.20\), the full drop. At a fraction of 0 the result is 67.5. At a fraction of 1 the result is 64.3.

**Result means.** Use 66.22% for depth 10.4 cm. Quoting 67.5% or 64.3% ignores the table step the stem paid for.

**Wrong turns**

- Scaling by depth ratio: \((10.4/11) \times 64.3\), which is not interpolation.
- Averaging 67.5 and 64.3 to get 65.9 when the depth is not midway.
- Interpolating field size on a table whose rows are depth, or the reverse.
- Extrapolating to 14 cm from the 10 and 11 cm rows. PDD is not linear over long stretches; ask for another table row.

**Traps.** Write the fraction \((x-x_1)/(x_2-x_1)\) first and confirm it is between 0 and 1. A fraction outside that range means you are extrapolating.

**Sources.** Standard table use in Khan and Gibbons. The public curriculum names this lesson “no formula” because the operation is arithmetic, not a new dosimetry symbol.

## PDD and TMR Calculation Tutorial

**Objectives:** IV.1, IV.3, I.10

**What the exam expects:** Define PDD and TMR so they cannot be swapped. Apply Mayneord F to move a PDD from one SSD to another, and state that F corrects inverse square only, not scatter.

**Definitions**

\[
\mathrm{PDD}(d) = 100 \times \frac{D(d)}{D(d_{\max})}
\]

at a **fixed SSD**. The field size for a PDD table is conventionally the field on the skin. PDD already contains inverse square from dmax down to depth \(d\), plus attenuation and scatter.

\[
\mathrm{TMR}(d, r_d) = \frac{D(d)}{D(d_{\max})}
\]

at a **fixed source-to-point distance**. The field size \(r_d\) is the field at the point. Moving from dmax to depth does not change the distance from the source, so inverse square is not inside the TMR. Scatter and attenuation are.

Related names, so the stems stay distinct:

- TPR uses a reference depth in the denominator instead of dmax.
- TAR uses dose in free space (air) in the denominator. Clarkson splits TAR into primary and scatter (module 33).

**Mayneord F**

\[
F = \left(\frac{\mathrm{SSD}_2 + d_m}{\mathrm{SSD}_1 + d_m}\right)^2 \left(\frac{\mathrm{SSD}_1 + d}{\mathrm{SSD}_2 + d}\right)^2
\]

\[
\mathrm{PDD}(\mathrm{SSD}_2) = \mathrm{PDD}(\mathrm{SSD}_1) \times F
\]

- \(\mathrm{SSD}_1\): SSD of the table PDD
- \(\mathrm{SSD}_2\): SSD you are treating at
- \(d_m\): depth of dmax
- \(d\): depth of the point
- \(F\): inverse-square-only factor

The first bracket compares the two dmax locations (farther dmax, slightly higher dose relative to a fixed source output). The second compares the two points at depth. Together they adjust the inverse-square piece already inside the PDD. Scatter still belongs to the original SSD. Extended SSD also changes the field size on the skin if the collimator is unchanged; Mayneord does not fix that either.

### Worked example: Mayneord F

**Given.** PDD at depth 10 cm, SSD 100 cm, is 67.0%. \(d_m = 1.5\) cm. Estimate PDD at the same depth for SSD 110 cm.

**Substitute.**

\[
F = \left(\frac{110 + 1.5}{100 + 1.5}\right)^2 \left(\frac{100 + 10}{110 + 10}\right)^2 = \left(\frac{111.5}{101.5}\right)^2 \left(\frac{110}{120}\right)^2
\]

**Arithmetic.**

- \(111.5 / 101.5 = 1.09852\), and \(1.09852^2 = 1.20675\)
- \(110 / 120 = 0.916667\), and \(0.916667^2 = 0.840278\)
- \(F = 1.20675 \times 0.840278 = 1.0140\)
- \(\mathrm{PDD}(110) = 67.0 \times 1.0140 = 67.94\%\)

**Check.** \(67 \times 0.014 = 0.938\), and \(67 + 0.938 = 67.938\), which rounds to 67.94. If the squares are dropped, \(1.09852 \times 0.916667 \approx 1.007\), and \(67 \times 1.007 \approx 67.5\). That lower answer is the usual distractor.

**Result means.** At a longer SSD the PDD rises slightly, from 67.0% to 67.9%, because the inverse-square falloff between dmax and 10 cm depth is gentler when both points are farther from the source. Scatter was not corrected. A real measurement at SSD 110 cm will not match 67.94% exactly.

**Wrong turns**

- Inverting either bracket, which produces \(1/F \approx 0.986\) and a PDD near 66.1%.
- Calling F a scatter correction.
- Applying F to a TMR. TMR is already an SAD quantity.
- Using SAD in place of SSD, or using depth \(d\) in the dmax bracket.
- Mixing this PDD with a TMR in one MU formula (next lessons).

**Traps.** Identify which SSD is the table SSD (\(\mathrm{SSD}_1\)) before you write the fraction. Extended SSD is \(\mathrm{SSD}_2\).

**Sources.** Khan and Gibbons, Mayneord factor. The derivation is inverse square between dmax and depth; Khan states the scatter limitation explicitly.

## PDD and TMR Calculations

**Objectives:** IV.1, IV.3

**What the exam expects:** Convert tumor dose to dose at dmax with PDD (“given dose”), and convert dose at dmax to dose at depth with TMR. The two calculations can share numbers and still be different setups.

**Given-dose formula (SSD, PDD only)**

\[
D(d_{\max}) = \frac{D_{\text{tumor}}}{\mathrm{PDD}/100}
\]

- \(D_{\text{tumor}}\): dose at depth (cGy)
- \(\mathrm{PDD}\): percent depth dose at that depth, for that field and SSD
- \(D(d_{\max})\): given dose, the dose at dmax

**TMR formula (SAD only)**

\[
D(d) = D(d_{\max}) \times \mathrm{TMR}(d, r_d)
\]

- \(D(d_{\max})\): dose at dmax on the same ray, same source-to-point distance, same field size at the point
- \(\mathrm{TMR}\): a fraction, not a percent, unless you divide the table’s percent by 100 yourself

### Worked example: given dose from PDD

**Given.** The tumor is to receive 200 cGy at a depth where PDD = 80.0%. SSD setup.

**Substitute.** \(D(d_{\max}) = 200 / 0.80 = 250\) cGy.

**Check.** \(250 \times 0.80 = 200\) cGy at the tumor. If someone multiplies instead, \(200 \times 0.80 = 160\) cGy, which is the tumor dose you would get from a given dose of 200 cGy, the reverse question.

**Result means.** “Given dose” here is 250 cGy at dmax. The tumor, at 80% of dmax, receives 200 cGy. The prescription point is the tumor, not dmax, unless the stem says the prescription is to dmax.

### Worked example: dose at depth from TMR

**Given.** On an SAD setup, dose at dmax at the isocenter distance is 250 cGy. TMR at the tumor depth is 0.800. Field size in the TMR is the field at the point.

**Substitute.** \(D(d) = 250 \times 0.800 = 200\) cGy.

**Check.** \(200 / 250 = 0.800\).

**Result means.** The number 200 cGy matches the previous example on purpose. The setups do not match. The PDD case fixed the SSD and included inverse square inside the 80%. The TMR case fixed the source-to-point distance. You cannot lift 80% out of a PDD table and call it a TMR of 0.800 for the same patient.

**Wrong turns**

- Multiplying tumor dose by PDD/100 when the question asks for given dose.
- Leaving PDD as 80 instead of 0.80, which makes given dose \(200/80 = 2.5\) cGy.
- Using a TMR looked up at the skin field size. TMR field size is at the calculation point.
- Applying Mayneord to the TMR example.
- Treating a full-phantom PDD ratio as an exit dose. That product is the dose at depth \(d\). The true exit surface has less backscatter than the phantom, so the exit dose is lower.

**Traps.** Underline “given dose,” “tumor dose,” “dmax,” and “depth” in the stem. Those four nouns decide whether you divide or multiply.

**Sources.** Khan and Gibbons, definitions of PDD, TMR, and given dose.

## PDD and TMR Quiz

**Skills this quiz checks**

- Interpolate between table rows and show the fraction is between 0 and 1.
- Compute Mayneord F with both brackets squared, then multiply the original PDD.
- State that Mayneord corrects inverse square only, not scatter, and that it is not applied to TMR.
- Turn tumor dose into given dose by dividing by PDD/100, and turn dmax dose into depth dose by multiplying by TMR.
- Refuse a setup that puts PDD and TMR in the same formula.

## Equivalent Square

**Objectives:** IV.3

**What the exam expects:** Convert a rectangular open field to an equivalent square with either form of Sterling’s formula, and explain why “percent of the field blocked” is not that calculation.

**Formula**

\[
\text{equivalent square side} = \frac{2ab}{a+b} = \frac{4A}{P}
\]

- \(a, b\): rectangle sides, same unit
- \(A = ab\): area
- \(P = 2(a+b)\): perimeter
- The result is the side of the square that has about the same scatter

Look up PDD, TMR, and phantom scatter at this side. Very long, narrow fields stretch the approximation.

### Worked example

**Given.** An open field is 10 cm × 15 cm.

**Substitute.**

\[
\frac{2 \times 10 \times 15}{10 + 15} = \frac{300}{25} = 12.0 \text{ cm}
\]

\[
A = 150,\quad P = 2(10+15) = 50,\quad \frac{4A}{P} = \frac{600}{50} = 12.0 \text{ cm}
\]

**Check.** Both forms agree at 12.0 cm. The arithmetic mean \((10+15)/2 = 12.5\) cm is the nearby distractor. The square root of the area, \(\sqrt{150} \approx 12.25\) cm, is the other one.

**Result means.** For scatter quantities, read the 12 cm × 12 cm row, not the 10 cm row and not the 15 cm row.

A long field, 4 cm × 20 cm, gives \(2 \times 4 \times 20 / (4+20) = 160/24 = 6.67\) cm. Sterling still returns a number; the approximation is poorer because the field is far from square. The exam still wants the formula.

**Wrong turns**

- Percent blocked used as a side length. A 10×10 field with 25% of its area blocked is not a 7.5 cm square (\(10 \times 0.75\)) and not an 8.7 cm square (\(\sqrt{75}\)). Block shape and position change scatter. An irregular or blocked field is a Clarkson problem (primary and scatter separated), not an equivalent-square problem.
- Using the equivalent square for collimator scatter when the jaws are a different size from the blocked opening. Jaws set collimator scatter. The opening at the patient sets phantom scatter.
- Forgetting that both formulas must be fed the field size at the distance the table expects (skin for many PDD tables, isocenter for TMR).

**Traps.** If the two forms disagree, the perimeter was computed as \(a+b\) instead of \(2(a+b)\). \(4A/(a+b)\) is twice the correct side.

**Sources.** Khan and Gibbons, equivalent squares (Sterling; Day’s rectangular approximation is the \(2ab/(a+b)\) form).

## Equivalent Square Calculation Mini-Quiz

**Skills this quiz checks**

- Evaluate \(2ab/(a+b)\) and \(4A/P\) and show they match.
- Reject the arithmetic mean and the square root of area when those numbers are close.
- Reject a percent-blocked shortcut and send an irregular field to Clarkson.
- Name which field size (jaws versus treated opening, skin versus isocenter) the table needs.

## Everything you need to know about MUs

**Objectives:** IV.3, IV.1, IV.2

**What the exam expects:** Write an SSD formula that contains PDD and an SAD formula that contains TMR. Do not put both depth quantities in one formula. State the calibration in the same breath as the number. Put wedge, tray, scatter, and inverse-square factors in the denominator.

**Calibration for every example in this lesson:** 1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm.

**SSD form (PDD). No TMR in this formula.**

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times S_c(r_c) \times S_p(r_d) \times (\mathrm{PDD}/100) \times \mathrm{WF} \times \mathrm{TF} \times \mathrm{ISF}}
\]

\[
\mathrm{ISF} = \left(\frac{\mathrm{SAD}}{\mathrm{SSD} + d_m}\right)^2
\]

- \(D\): dose wanted at depth (cGy)
- \(\dot{D}_{\mathrm{cal}}\): 1.0 cGy/MU at the calibration condition above
- \(S_c(r_c)\): collimator (head) scatter for the jaw equivalent square \(r_c\)
- \(S_p(r_d)\): phantom scatter for the treated field size the PDD table uses
- \(\mathrm{PDD}\): percent depth dose at the point, for that field and SSD
- \(\mathrm{WF}, \mathrm{TF}\): wedge factor and tray factor (1 if absent)
- \(\mathrm{ISF}\): moves the calibration from SAD 100 cm to the actual location of dmax, which is at \(\mathrm{SSD} + d_m\)
- \(d_m\): depth of maximum dose

**SAD form (TMR). No PDD in this formula.**

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times S_c(r_c) \times S_p(r_d) \times \mathrm{TMR}(d, r_d) \times \mathrm{WF} \times \mathrm{TF} \times (\mathrm{SAD}/\mathrm{SPD})^2}
\]

- \(\mathrm{TMR}(d, r_d)\): tissue-maximum ratio at depth \(d\) for the field size at the point
- \(\mathrm{SPD}\): source-to-point distance
- \(\mathrm{SAD}\): 100 cm in this calibration
- If the point is at isocenter, \(\mathrm{SPD} = \mathrm{SAD}\) and the inverse-square term is 1

\(S_c\) follows the jaws. \(S_p\) and TMR (or PDD) follow the field that actually irradiates the phantom, including blocks. A stem that gives every factor as 1 is telling you the point is at calibration conditions except for the factor it wants you to use.

### Worked example: SSD, PDD, inverse square equal to 1

**Given.** SSD setup. \(\mathrm{SSD} + d_m = 100\) cm, so dmax is exactly at the calibration distance (for example SSD = 98.5 cm and \(d_m = 1.5\) cm). Field 10×10, so \(S_c = S_p = 1\). Open beam, \(\mathrm{WF} = \mathrm{TF} = 1\). PDD at the tumor depth is 70.0%. Tumor dose \(D = 210\) cGy.

**Substitute.** \(\mathrm{ISF} = (100/100)^2 = 1\).

\[
\mathrm{MU} = \frac{210}{1.0 \times 1 \times 1 \times 0.700 \times 1 \times 1 \times 1} = \frac{210}{0.700}
\]

**Arithmetic.** \(210 / 0.70 = 300\) MU.

**Check.** \(300 \times 1.0 \times 0.700 = 210\) cGy.

**Result means.** 300 MU delivers 210 cGy at depth when 70% of the dmax dose reaches that depth and dmax itself is at the calibration distance. The given dose at dmax is \(210/0.70 = 300\) cGy, and at 1.0 cGy/MU that is 300 MU, the same answer from the given-dose route.

### Worked example: SAD, TMR

**Given.** The point is at isocenter, \(\mathrm{SPD} = 100\) cm. \(S_c = S_p = \mathrm{WF} = \mathrm{TF} = 1\). TMR = 0.800. Dose \(D = 200\) cGy. Same calibration, 1.0 cGy/MU at dmax, 10×10, SAD 100.

**Substitute.** \((\mathrm{SAD}/\mathrm{SPD})^2 = 1\).

\[
\mathrm{MU} = \frac{200}{1.0 \times 0.800} = 250 \text{ MU}
\]

**Check.** \(250 \times 0.800 = 200\) cGy.

**Result means.** Because the point is at the calibration distance, MU is simply dose divided by TMR. There is no PDD in this line. Using the 70% PDD from the SSD example here would be a different patient setup.

### Worked example: SAD with a 0.6 wedge factor

**Given.** Isocenter point, all scatter and tray factors = 1, inverse square = 1, same calibration. TMR = 0.750. WF = 0.600. The wedge is in the beam. \(D = 180\) cGy.

**Substitute.**

\[
\mathrm{MU} = \frac{180}{0.750 \times 0.600} = \frac{180}{0.450} = 400 \text{ MU}
\]

**Check.** \(400 \times 0.750 \times 0.600 = 400 \times 0.450 = 180\) cGy.

**If the factor is omitted.** MU would be calculated as \(180/0.750 = 240\). With the wedge still in the beam the dose is \(240 \times 0.750 \times 0.600 = 108\) cGy. And \(108/180 = 0.60\). Same underdose rule as module 34.

**Wrong turns**

- PDD in a TMR formula, or TMR in a PDD formula.
- WF multiplied into the numerator, or omitted while the wedge stays in the beam.
- ISF upside down: \((( \mathrm{SSD}+d_m)/\mathrm{SAD})^2\) makes MU too small when the patient dmax is farther than 100 cm.
- \(S_c\) looked up at the blocked field, or TMR looked up at the jaw field. Jaws set \(S_c\). The patient opening sets \(S_p\) and TMR.
- A Mayneord correction stacked on top of a TMR.
- Khan versus Bentel electron rules used to pick an energy, then that energy’s photon PDD used by mistake. Electron output is a measured cutout factor (module 42), not this photon MU.

**Traps.** Copy the calibration sentence onto the page before any division: “1.0 cGy/MU at dmax, 10×10, SAD 100.” Then write either PDD or TMR, not both. If \(\mathrm{SSD}+d_m\) is not 100 cm, ISF is not 1. For SSD = 100 cm and \(d_m = 1.5\) cm, \(\mathrm{ISF} = (100/101.5)^2 = 0.9707\). A 67.0% PDD and a 200 cGy tumor dose then give

\[
\mathrm{MU} = \frac{200}{0.670 \times 0.9707} = \frac{200}{0.6504} = 307.5
\]

Check: \(307.5 \times 0.6504 \approx 200\) cGy. Leaving ISF out of that particular setup yields \(200/0.670 = 298.5\) MU, about 3% low on the MU and therefore about 3% low on dose once the real inverse square is included. Many stems choose geometry so the factor is 1. Read it.

**Sources.** Khan and Gibbons, MU calculations for SSD and SAD. Equivalent-square and wedge-factor chapters supply \(S_p\) field size and WF.

## MU Calc Quiz

**Skills this quiz checks**

- State the calibration (1.0 cGy/MU at dmax, 10×10, SAD 100) and then compute an SSD MU with PDD and an SAD MU with TMR.
- Keep ISF equal to 1 only when dmax or the calculation point is actually 100 cm from the source.
- Place WF in the denominator and reproduce the underdose when it is omitted (delivered/prescribed = WF).
- Assign jaws to \(S_c\) and the treated opening to \(S_p\) and TMR.
- Show a reverse check: MU × output × depth factor × WF equals the prescribed dose.
