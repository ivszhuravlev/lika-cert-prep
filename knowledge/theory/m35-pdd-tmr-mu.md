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

## Scatter-Maximum Ratio and Zero-Area TMR

**Objectives:** IV.1, IV.3

**What the exam expects:** Split a TMR into its primary and scatter parts the way Clarkson splits a TAR (module 33). The zero-area TMR, written TMR(d, 0), is the primary-only term: the TMR a field would have if it were shrunk to nothing, so no phantom scatter reaches the point. The scatter-maximum ratio, SMR, is what the finite field adds. Items ask for SMR from two TMRs, for the scatter dose at a point, and for TMR(d, 0) derived from an effective attenuation coefficient.

**Formulas**

\[
\mathrm{SMR}(d, r_d) = \mathrm{TMR}(d, r_d) - \mathrm{TMR}(d, 0)
\qquad
\mathrm{TMR}(d, 0) = e^{-\mu_{\text{eff}} (d - d_{\max})}
\]

- \(\mathrm{TMR}(d, r_d)\): tissue-maximum ratio at depth \(d\) for field size \(r_d\) at the point
- \(\mathrm{TMR}(d, 0)\): zero-area (primary-only) TMR
- \(\mathrm{SMR}\): scatter-maximum ratio, the scatter part of the TMR
- \(\mu_{\text{eff}}\): effective linear attenuation coefficient of the beam in water (cm\(^{-1}\))
- \(d - d_{\max}\): the attenuating thickness between dmax and the point. The exponential starts at dmax, not at the surface, because TMR is 1.000 at dmax by definition

Dose at the point splits the same way: primary dose is the dmax dose times TMR(d, 0), scatter dose is the dmax dose times SMR, and they add to the full dose. In the convolution picture, TERMA is the energy released by the primary photons and the kernel spreads it; TERMA is not KERMA (KERMA counts only energy handed to charged particles). The vendor trap in this area: AAA is an analytical convolution-type model, and Acuros XB is a deterministic solution of the linear Boltzmann transport equation. Neither is Monte Carlo, and only Acuros transports radiation through the voxel materials.

### Worked example: SMR and the scatter dose

**Given.** For a 10 MV beam at 10 cm depth, TMR for the 15×15 field at the point is 0.812 and the zero-area TMR is 0.705. The dose at dmax on this ray is 240 cGy.

**Substitute.** \(\mathrm{SMR} = 0.812 - 0.705 = 0.107\).

**Arithmetic.** Total dose \(= 240 \times 0.812 = 194.9\) cGy. Primary \(= 240 \times 0.705 = 169.2\) cGy. Scatter \(= 240 \times 0.107 = 25.7\) cGy.

**Check.** \(169.2 + 25.7 = 194.9\) cGy, equal to the total. The scatter share is \(0.107/0.812 = 13\%\) of the dose at the point.

**Result means.** Of the 194.9 cGy at 10 cm, 169.2 cGy arrives as primary and 25.7 cGy as phantom scatter from the 15×15 field. A block that shadows the point but leaves the rest of the field open removes the 169.2 cGy of primary while leaving most of the 25.7 cGy of scatter.

### Second pass: zero-area TMR from the attenuation coefficient

**Given.** \(\mu_{\text{eff}} = 0.045\) cm\(^{-1}\), \(d_{\max} = 2.5\) cm, depth \(d = 14\) cm.

**Substitute.** \(\mathrm{TMR}(14, 0) = e^{-0.045 (14 - 2.5)} = e^{-0.045 \times 11.5} = e^{-0.5175}\).

**Arithmetic.** \(e^{-0.5175} = 0.596\).

**Check.** \(\ln(0.596) = -0.5175\), and \(0.5175/0.045 = 11.5\) cm. Starting the exponential at the surface instead of dmax, \(e^{-0.045 \times 14} = 0.533\), is the usual slip.

**Result means.** A pencil of primary photons loses about 40% of its intensity between dmax and 14 cm. Any TMR for a real field at 14 cm must be larger than 0.596, because scatter adds to it.

**Wrong turns**

- SMR as a ratio of the two TMRs, or as 1 minus the TMR.
- Exponential measured from the surface instead of from dmax.
- Linear attenuation, \(1 - \mu x\), in place of the exponential.
- Calling AAA a Monte Carlo code, or calling Acuros a kernel model.

**Traps.** TMR(d, 0) is a primary quantity for the beam; it does not depend on field size. SMR does.

**Sources.** Khan and Gibbons, SMR and the zero-area TMR; Clarkson method; vendor documentation for AAA and Acuros XB.

## SSD and SAD Setup Errors as Delivered Dose

**Objectives:** IV.3, IV.1

**What the exam expects:** Turn a set-up mix-up into a delivered-dose number. Three patterns recur. (1) The MU were computed with the wrong calibration geometry: the unit is calibrated 1 cGy/MU at dmax under an SSD set-up, but the MU assumed 1 cGy/MU at dmax 100 cm from the source. (2) An isocentric plan was set up at SSD = 100 cm, so the calculation point moved from 100 cm to 100 + depth from the source. (3) The question is how many more MU an SSD set-up needs than an SAD set-up for the same midplane point.

**Formulas**

\[
\text{output at 100 cm} = \dot{D}_{\mathrm{cal}} \left(\frac{100 + d_{\max}}{100}\right)^2
\qquad
\frac{D_{\text{delivered}}}{D_{\text{planned}}} = \left(\frac{100}{100 + d}\right)^2
\]

- \(\dot{D}_{\mathrm{cal}}\): 1 cGy/MU at dmax when dmax sits at 100 + dmax cm from the source (SSD calibration)
- \(d_{\max}\): 3.3 cm for the 18 MV example, so the factor is \((103.3/100)^2 = 1.067\); for 6 MV with dmax 1.5 cm it is \((101.5/100)^2 = 1.030\)
- \(d\): depth of the planned isocentric point; after an SSD set-up it is 100 + d from the source
- Inverse square only; the small change in field size and TMR is ignored unless the stem gives tables

### Worked example: 18 MV calibrated at SSD, MU computed as SAD

**Given.** An 18 MV unit is calibrated to 1.000 cGy/MU at dmax (3.3 cm) with the phantom surface at 100 cm. The MU for a 200 cGy isocentric fraction were computed as if the unit gave 1.000 cGy/MU at dmax placed 100 cm from the source.

**Substitute.** Real output with dmax at 100 cm \(= 1.000 \times (103.3/100)^2 = 1.067\) cGy/MU.

**Arithmetic.** Delivered \(= 200 \times 1.067 = 213.4\) cGy.

**Check.** \(1.033^2 = 1.0671\). \(200 \times 0.0671 = 13.4\), and \(200 + 13.4 = 213.4\). The error is 6.7% high.

**Result means.** The patient received 213.4 cGy instead of 200 cGy. The 6 MV version of the same slip is 3.0% high. The direction reverses if the calibration were SAD and the MU assumed SSD.

### Second pass: isocentric plan set up at SSD 100

**Given.** The isocentric point is at 6 cm depth, 250 cGy per fraction. Four fractions were set up with the skin at 100 cm instead of the isocenter.

**Substitute.** The point is at 106 cm. Per fraction \(= 250 \times (100/106)^2 = 250 \times 0.890 = 222.5\) cGy.

**Arithmetic.** Four fractions \(= 4 \times 222.5 = 890\) cGy of the planned 1000 cGy.

**Check.** \((100/106)^2 = 0.8900\), an 11.0% underdose; \(1000 \times 0.890 = 890\) cGy.

**Result means.** The four fractions delivered 890 cGy. The remaining fractions, or a corrected re-plan, must make up 110 cGy.

**Third pass: MU penalty for SSD at midplane.** Separation 24 cm, midplane 12 cm. SAD: point at 100 cm. SSD 100: point at 112 cm. The SSD set-up needs \((112/100)^2 = 1.254\) times the MU, 25.4% more, for the same midplane dose (inverse square only).

**Wrong turns**

- Dividing by 1.067 when the true output is higher, or using the unsquared 1.033.
- Treating the point as 100 cm from the source in both set-ups.
- Using the separation (24 cm) instead of the midplane depth (12 cm) in the distance.

**Traps.** Write the source-to-point distance for the planned and the delivered geometry on two lines before squaring.

**Sources.** Khan and Gibbons, SSD and SAD calibration conventions; TG-51 reference geometry.

## Weighted Isocentric Fields and Back-Solved Normalization

**Objectives:** IV.3

**What the exam expects:** Two bookkeeping skills. First, when a prescription is written to an isodose line (95%) and the beams carry weights at isocenter, find each beam's isocenter dose: raise the prescription to the 100% isocenter dose, then split it by weight. Second, when a wedge was left out for only part of a course, average the delivered fractions. Third, when the MU and all factors are known but the normalization line is not, divide to recover it.

**Formulas**

\[
D_{\text{iso}} = \frac{D_{\text{Rx}}}{\text{line}/100}
\qquad
D_{\text{beam}} = D_{\text{iso}} \frac{w_{\text{beam}}}{\sum w}
\qquad
\text{line} = \frac{D_{\text{Rx}}}{\mathrm{MU} \times \text{output} \times \prod \text{factors}}
\]

- \(D_{\text{Rx}}\): prescribed dose to the isodose line
- \(\text{line}\): the prescription isodose (95%) or, in the back-solve, the normalization isodose
- \(w\): isocenter weights, for example 1 : 0.5 : 0.5, which sum to 2.0
- \(\prod \text{factors}\): cone or collimator factor, cutout or phantom scatter, inverse square to the effective SSD, wedge or tray

### Worked example: 1 : 0.5 : 0.5 after a 95% prescription

**Given.** 180 cGy per fraction is prescribed to the 95% line. Three isocentric beams are weighted 1 : 0.5 : 0.5 at isocenter.

**Substitute.** \(D_{\text{iso}} = 180/0.95 = 189.5\) cGy. Sum of weights \(= 2.0\).

**Arithmetic.** Anterior beam \(= 189.5 \times 1/2 = 94.7\) cGy. Each lateral \(= 189.5 \times 0.5/2 = 47.4\) cGy.

**Check.** \(94.7 + 47.4 + 47.4 = 189.5\) cGy, and \(189.5 \times 0.95 = 180\) cGy at the 95% line.

**Result means.** Each lateral delivers 47.4 cGy at isocenter, not 45 cGy; the 95% prescription raised every beam by 1/0.95.

### Second pass: wedge omitted for part of the course

**Given.** 50 Gy in 20 fractions through a wedged field, wedge factor 0.75. The wedge was left out of the beam in 4 fractions; the MU were not changed.

**Substitute.** Wedged fraction \(= 2.5\) Gy. Unwedged fraction \(= 2.5/0.75 = 3.333\) Gy.

**Arithmetic.** Total \(= 16 \times 2.5 + 4 \times 3.333 = 40 + 13.33 = 53.3\) Gy, which is 106.7% of the prescription.

**Check.** The excess is \(4 \times (3.333 - 2.5) = 3.33\) Gy. Omitting the wedge in every fraction would give \(50/0.75 = 66.7\) Gy.

**Third pass: back-solving a normalization.** An electron field delivered 296 MU for 250 cGy prescribed to the normalization line. Cone factor 1.02, cutout factor 0.975, SSD 103 cm with a 100 cm nominal distance, output 1 cGy/MU. Inverse square \((100/103)^2 = 0.9426\). Line \(= 250/(296 \times 1.02 \times 0.975 \times 0.9426) = 250/277.5 = 0.901\), the 90% line. Check: \(296 \times 0.9375 = 277.5\) cGy at dmax on the axis, and 90% of that is 250 cGy.

**Wrong turns**

- Splitting 180 cGy by weight without first raising it to the isocenter dose.
- Multiplying the omitted-wedge fractions by the wedge factor instead of dividing.
- Inverse square the wrong way round in the back-solve, which drops the line to 80%.

**Traps.** Weights are isocenter weights unless the stem says dmax weights. The sum of weights is the divisor; it is not always 1.

**Sources.** Khan and Gibbons, isocentric weighting and normalization; module 34 for the wedge-omitted rule.

## Electron Range Rules Inside a Calculation

**Objectives:** IV.3

**What the exam expects:** The depth rules for electrons are used as numbers inside a problem, not only recited. The mean energy at the surface comes from the measured half-value depth: \(E_0 \approx 2.33 \times R_{50}\), which is the same as \(R_{50} \approx E/2.33\) (some texts round to E/2.4). The practical range is \(R_p \approx E/2\). The 90% and 80% depths follow whichever rule the stem names (Khan E/3.2 and E/2.8; Bentel E/4 and E/3, modules 19 and 25). Energy falls about 2 MeV per centimeter of water.

**Formulas**

\[
E_0 \approx 2.33 \, R_{50}
\qquad
R_{50} \approx \frac{E}{2.33}
\qquad
R_p \approx \frac{E}{2}
\]

- \(E_0\): mean electron energy at the phantom surface (MeV)
- \(R_{50}\): depth of the 50% dose on the central axis (cm of water)
- \(R_p\): practical range, where the falloff meets the bremsstrahlung tail (cm)

### Worked example: energy from a measured R50

**Given.** A commissioning scan puts the 50% depth at 5.6 cm.

**Substitute.** \(E_0 = 2.33 \times 5.6\).

**Arithmetic.** \(2.33 \times 5.6 = 13.0\) MeV.

**Check.** \(13.0/2.33 = 5.58\) cm. The nominal energy is likely 12 or 13 MeV, since nominal and mean surface energy differ by a few percent.

**Result means.** The beam behaves like a 13 MeV beam. Its practical range is near \(13/2 = 6.5\) cm.

### Second pass: where a structure sits in the falloff

**Given.** A 12 MeV beam. A critical structure is at 5.5 cm depth.

**Reasoning.** \(R_{50} = 12/2.33 = 5.2\) cm. \(R_p = 12/2 = 6\) cm. The structure at 5.5 cm is deeper than the 50% depth and shallower than the practical range, so it is in the steep falloff: well under 50% of the maximum, but still real electron dose, not just bremsstrahlung.

**Check.** Bentel's 90% depth is \(12/4 = 3\) cm, so 5.5 cm is nowhere near the therapeutic depth either. To push the structure past \(R_p\) you would need \(E/2 < 5.5\), that is, a beam of 11 MeV or less, while still covering the target.

**Wrong turns**

- \(E_0 = R_{50}/2.33\) or \(2 \times R_{50}\).
- Treating a point just inside \(R_p\) as if it received zero dose.
- Reporting \(R_p\) as the therapeutic depth.

**Traps.** Write the three depths (90%, 50%, \(R_p\)) in order on the page. A structure between \(R_{50}\) and \(R_p\) is in the falloff.

**Sources.** Khan and Gibbons; TG-25 and TG-70 for \(E_0 = 2.33 R_{50}\).
