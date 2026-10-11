# Module 34. Effects of beam modifying devices

Original notes for MDCB CMD prep. Objectives IV.2 and III.7: wedges, bolus, partial transmission, compensators, and MLCs.

Calibration sentence used whenever an MU is computed in this module: the machine is calibrated to **1.0 cGy/MU at dmax, 10×10 cm², SAD 100 cm**, unless a worked example says the reading was measured at a different point.

## Wedges

**Objectives:** IV.2, III.7

**What the exam expects:** Define the wedge factor as a dose ratio at the same MU. Use a physical wedge, a dynamic wedge, or an enhanced dynamic wedge as a beam modifier that tilts the isodose. If the wedge is in the beam and the wedge factor was left out of the MU calculation, the patient is underdosed by about that factor. Know the opposite mistake as a distractor: factor used in the MU, wedge never inserted, patient overdosed.

A wedge tilts the isodose curves toward the thick side (the hot side of the distribution is the thin side of the wedge). The wedge angle is the tilt of a chosen isodose curve (often near 10 cm depth), not the angle of the metal. Physical wedges change beam quality slightly and need a measured factor. Dynamic and enhanced dynamic wedges create the tilt by jaw motion; they still need a wedge factor in the MU.

Other modifiers in the same objective, in one pass:

- **Bolus** sits on the skin, pulls dmax toward the surface, and raises skin dose. It is tissue-equivalent thickness, not a wedge.
- **Partial transmission blocks** and **compensators** reduce dose by a measured transmission. A compensator also shapes the distribution for missing tissue or a sloping surface. A compensator is not a density override.
- **MLCs** shape the aperture. Leaf transmission is small and is not zero. Detail is in the MLC lesson below.
- A megavoltage block or tray is kept on the order of 20 cm from the skin so contaminant electrons scatter and are absorbed in air before they reach the patient.
- The wedge transmission used for dose is the one the planning system expects. A factor measured in air is not the same number as a factor measured in phantom at depth.
- A larger gap from an electron cutout to the skin lowers output, so the monitor units for the same dose go up. Oblique electron incidence from an air gap that is not filled moves dmax toward the surface.

**Formula**

\[
\mathrm{WF} = \frac{\text{dose with the wedge in the beam}}{\text{dose with the beam open}}
\]

at the **same MU**, same energy, same field, same point. WF is less than 1. In an MU formula it belongs in the denominator.

### Worked example: wedge in the beam, factor left out of the MU

**Given.** Prescription to the calculation point is 200 cGy. The point is the calibration point, so the open-beam output is 1.0 cGy/MU. Every other factor (TMR or PDD, Sc, Sp, tray, inverse square) equals 1 in this stem. The physical wedge is in the beam. Its wedge factor is 0.600. The planner computes MU with no wedge factor.

**Formula.** With the factor included,

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times \mathrm{WF}}
\]

- \(D\): dose wanted at the point (cGy)
- \(\dot{D}_{\mathrm{cal}}\): 1.0 cGy/MU at dmax, 10×10, SAD 100
- \(\mathrm{WF}\): 0.600

**What was actually calculated.** The factor was omitted, so \(\mathrm{MU} = 200 / 1.0 = 200\) MU.

**Dose delivered.** The wedge is physically in the beam, so each MU still produces only 0.600 cGy at the point:

\[
\text{Dose} = 200 \times 1.0 \times 0.600 = 120 \text{ cGy}
\]

**Check.** \(200 \times 0.6 = 120\). The ratio delivered/prescribed is \(120/200 = 0.60\), which is the wedge factor.

**Correct MU, for comparison.** \(200 / 0.600 = 333.3\) MU. Then \(333.3 \times 0.600 = 200\) cGy.

**Result means.** The patient receives 120 cGy instead of 200 cGy. Delivered dose is about the wedge factor times the intended dose (here exactly 0.60). The shortfall is 80 cGy, which is 40% of the prescription. The sentence to keep: wedge in the beam, factor left out of the MU, underdose by about that factor.

**Wrong turns**

- Reversing the direction and saying the patient is overdosed. Overdose is the other setup: WF was used, so 333.3 MU were set, and the wedge was **not** inserted. Delivered dose is then \(333.3 \times 1.0 = 333\) cGy, and \(333/200 = 1/0.60\).
- Putting WF in the numerator of the MU.
- Using a wedge factor measured at a different energy, field size, or depth than the beam you are calculating.
- Treating the nominal wedge angle (15°, 30°, 45°, 60°) as the wedge factor. The factor is a measured dose ratio, often near 0.6 for a steep wedge, and the stem gives it.
- Mixing this SSD/open-output story with a TMR taken from a different calibration.

**Traps.** Read the stem for two independent facts: is the wedge in the tray or the plan, and was WF in the MU. Both must be known before you decide underdose or overdose.

**Sources.** Khan and Gibbons, wedge filters and MU. Clinical wedge factors are measured, not computed from the wedge angle.

## Wedge Factor Calculation Tutorial

**Objectives:** IV.2

**What the exam expects:** Compute WF from two doses at the same MU, then use that WF in an MU calculation at a stated calibration.

### Worked example

**Given.** At the same point, 100 MU open delivers 98.0 cGy. The same 100 MU with the wedge delivers 58.8 cGy. Later, a prescription of 180 cGy is required at the calibration point, where open output is 1.0 cGy/MU (dmax, 10×10, SAD 100). The wedge will be in the beam. No other modifier.

**Formula.** \(\mathrm{WF} = D_{\text{wedge}} / D_{\text{open}}\) at the same MU.

\[
\mathrm{MU} = \frac{D}{\dot{D}_{\mathrm{cal}} \times \mathrm{WF}}
\]

**Symbols.** \(D_{\text{wedge}} = 58.8\) cGy, \(D_{\text{open}} = 98.0\) cGy, both for 100 MU. \(D = 180\) cGy. \(\dot{D}_{\mathrm{cal}} = 1.0\) cGy/MU.

**Substitute.**

\[
\mathrm{WF} = \frac{58.8}{98.0} = 0.600
\]

\[
\mathrm{MU} = \frac{180}{1.0 \times 0.600} = \frac{180}{0.600} = 300
\]

**Arithmetic.** \(98.0 \times 0.6 = 58.8\), so the ratio is exactly 0.600. \(180 / 0.6 = 300\).

**Check.** Delivered dose \(= 300 \times 1.0 \times 0.600 = 180\) cGy. The measurement ratio uses equal MU; if the wedged reading had been taken at a different MU, scale both readings to the same MU before dividing.

**Result means.** The wedge transmits 60% of the open dose. The plan needs 300 MU, not 180 MU, to reach 180 cGy with the wedge in place.

**Wrong turns**

- Dividing open by wedged: \(98/58.8 = 1.667\), which is \(1/\mathrm{WF}\), and then multiplying MU by 0.6 instead of dividing.
- Forgetting the wedge after measuring it (the underdose case in the previous lesson): 180 MU would deliver \(180 \times 0.6 = 108\) cGy.
- Using PDD in this calibration-point example. The point is already at dmax under the stated calibration, so the depth factor is 1. Adding a TMR and a PDD together double-counts depth.
- Changing field size and keeping a wedge factor that was measured for a different jaw setting. Large-field wedge factors can differ; use the factor the stem associates with the field.

**Traps.** “Same MU” is part of the definition. A wedge left in during an output check that was supposed to be open makes the output look low by about WF.

**Sources.** Khan and Gibbons, wedge transmission factor.

## Wedge and Hinge Angle

**Objectives:** IV.2, III.7

**What the exam expects:** Convert hinge angle to wedge angle for a symmetric wedged pair, and the reverse. Keep wedge angle (isodose tilt) separate from the slope of the metal.

**Formula**

\[
\text{wedge angle} = 90^\circ - \frac{\text{hinge angle}}{2}
\]

- Hinge angle: angle between the central axes of the two beams
- Wedge angle: tilt of the isodose curve produced by each wedge in a symmetric pair

The formula assumes a symmetric pair: both wedges the same angle, both beams aiming to flatten one region.

### Worked example

**Given.** Two beams form a hinge of 120°.

**Substitute.** Wedge angle \(= 90 - (120/2) = 90 - 60 = 30^\circ\).

**Check with the standard pairs.**

- Hinge 90°: wedge angle \(= 90 - 45 = 45^\circ\).
- Hinge 60°: wedge angle \(= 90 - 30 = 60^\circ\).

Rearrangement: hinge \(= 2(90 - \text{wedge angle})\). For a 30° wedge, hinge \(= 2(60) = 120^\circ\), which matches the given.

**Result means.** A 120° hinge calls for a pair of 30° wedges if the goal is the classic uniform wedged-pair distribution. A 60° wedge on that hinge would over-tilt the isodoses.

**Wrong turns**

- Wedge angle \(=\) hinge/2 (that gives 60° for this hinge).
- Wedge angle \(= 180 - \text{hinge}\) (that gives 60° as well, for a different reason).
- Using the formula for a single wedged field with an open field. The relation is for a wedged pair.
- Reading “60° wedge” as WF = 0.60. Some steep wedges do have factors near 0.6, and that coincidence is not a rule.

**Traps.** Draw the two central axes and mark the hinge before you halve it. A quick sketch stops the 180° complement error.

**Sources.** Khan and Gibbons, wedge-pair geometry.

## MLCs

**Objectives:** IV.2, III.7

**What the exam expects:** MLC leaves shape the aperture and replace many blocks. Transmission through a leaf is small, on the order of 1–2% for a typical 6 MV mid-leaf measurement, and interleaf leakage is higher than mid-leaf transmission. Rounded leaf ends need a dosimetric leaf-gap parameter so the light field and the radiation edge agree. Tongue-and-groove design reduces interleaf leakage and can leave a cold stripe where adjacent segments do not overlap the same way. None of that is a wedge factor.

**Formula for a transmission estimate**

\[
D_{\text{through leaf}} = D_{\text{open}} \times T_{\text{leaf}}
\]

- \(D_{\text{open}}\): dose at the point if that region were open (cGy)
- \(T_{\text{leaf}}\): mid-leaf transmission, a fraction (0.015 is 1.5%)
- \(D_{\text{through leaf}}\): dose under the leaf

### Worked example

**Given.** A region blocked by an MLC would receive 200 cGy if it were open. Mid-leaf transmission is 1.5% (0.015).

**Substitute.** \(D = 200 \times 0.015 = 3.0\) cGy.

**Check.** \(200 \times 0.01 = 2.0\), and \(200 \times 0.005 = 1.0\), so \(2.0 + 1.0 = 3.0\).

**Result means.** The “blocked” region still gets about 3 cGy from mid-leaf transmission, 1.5% of the open dose. It is not a zero-dose block. Interleaf leakage would be higher than this mid-leaf figure. A Cerrobend block is thicker in intent; do not reuse an MLC transmission number as a block transmission.

**Wrong turns**

- Treating MLC transmission as a wedge factor and dividing the whole-field MU by 0.015.
- Ignoring tongue-and-groove cold stripes when two segments abut along a leaf side.
- Forgetting that a rounded leaf end shifts the radiation edge. The commissioned leaf gap fixes that in the planning system; a wrong gap shows up as a systematic dose error on modulated plans.
- Using jaw transmission and leaf transmission as if they were the same number.

**Traps.** Partial transmission blocks in a stem are a stated transmission (for example 50%), measured or specified. MLC mid-leaf transmission is the small percent above. Read which device is in the beam.

Bolus and compensators do not use the hinge-angle formula. Bolus thickness is chosen to bring the surface to a stated depth (often so that dmax falls on or near the skin). A compensator’s transmission is measured or calculated from its thickness and linear attenuation, the same exponential as in module 36, and it sits in the beam to replace missing tissue.

**Sources.** Khan and Gibbons, beam modification. AAPM MLC commissioning guidance (leaf transmission, leaf gap, tongue and groove) as used in TG-142 era machine QA.

## Beam Modifying Devices Quiz

**Skills this quiz checks**

- Compute WF from two equal-MU doses and place WF in the MU denominator.
- Predict underdose when the wedge is in the beam and WF was omitted (delivered/prescribed ≈ WF; the 0.6 case delivers 60% of the prescription).
- Predict overdose when WF was included and the wedge was not inserted (delivered/prescribed ≈ 1/WF).
- Convert hinge angle to wedge angle with \(90^\circ - \text{hinge}/2\), and recover the 45°/90° and 60°/60° pairs.
- Estimate dose under an MLC from a stated transmission, and keep that transmission far below a wedge factor.
- Separate bolus (skin dose, dmax shift), compensator (missing tissue), and partial transmission (a stated fraction) from a wedge.
