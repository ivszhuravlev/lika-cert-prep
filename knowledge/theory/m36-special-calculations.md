# Module 36. Special calculations

Original notes for MDCB CMD prep. Objective IV.3 (gap, off-axis, re-treatment, entrance and exit) and the transmission, penumbra, and timer skills tied to I.10 and VI.3.

\(L\) in the gap formula is the field length on the skin. \(d\) in that formula is depth. Source-to-diaphragm distance is SDD, not SSD.

## Gap Calculation Tutorial

**Objectives:** IV.3

**What the exam expects:** Compute the skin gap that makes two adjacent photon field edges meet at a chosen depth. The formula is geometric. It does not remove penumbra, and it is the wrong tool when the match edges are already half-beam blocked.

**Formula**

\[
\mathrm{gap} = \left(\frac{L_1}{2}\right)\left(\frac{d}{\mathrm{SSD}_1}\right) + \left(\frac{L_2}{2}\right)\left(\frac{d}{\mathrm{SSD}_2}\right)
\]

- \(\mathrm{gap}\): separation on the skin between the two light-field edges (cm)
- \(L_1, L_2\): field lengths on the skin, the dimension along the match (cm)
- \(d\): depth at which the geometric edges should meet (cm)
- \(\mathrm{SSD}_1, \mathrm{SSD}_2\): source-to-skin distance of each field (cm)

Each term is the sideways drift of that field’s edge between the skin and depth \(d\). A gap of zero on the skin makes the edges overlap at depth (a hot junction). A gap larger than the formula leaves a cold junction at that depth.

### Worked example

**Given.** Field 1 length \(L_1 = 20\) cm at \(\mathrm{SSD}_1 = 100\) cm. Field 2 length \(L_2 = 18\) cm at \(\mathrm{SSD}_2 = 120\) cm. The geometric edges should meet at depth \(d = 8\) cm.

**Substitute.**

\[
\mathrm{gap} = \left(\frac{20}{2}\right)\left(\frac{8}{100}\right) + \left(\frac{18}{2}\right)\left(\frac{8}{120}\right) = 10 \times 0.080 + 9 \times \frac{8}{120}
\]

**Arithmetic.** \(10 \times 0.080 = 0.80\) cm. \(8/120 = 1/15\), and \(9/15 = 0.60\) cm. Gap \(= 0.80 + 0.60 = 1.40\) cm.

**Check.** \(0.80 + 0.60 = 1.40\). If both SSDs had been 100 cm, the second term would have been \(9 \times 0.080 = 0.72\) cm and the gap would have been 1.52 cm. Using 100 cm for the second field is the usual slip when the stem gives two SSDs.

**Result means.** The light fields on the skin are 1.40 cm apart. At 8 cm depth the geometric edges meet. This is the 50% geometric edge, not a promise of a perfectly uniform dose. Penumbra still feathers both sides of the junction.

**Wrong turns**

- Adding the full field lengths instead of the half-lengths: that doubles the gap.
- A gap of zero because “the fields are adjacent,” which matches them on the skin and overlaps them at depth.
- Using the formula for two half-beam fields whose match borders lie on the central axis. Those borders do not diverge, so the geometric gap is 0. Applying the formula opens a cold strip.
- Using SAD where the field length was defined on the skin, or using a collimator setting at isocenter without converting to the skin length.
- Treating an electron–photon junction with this photon gap. Adjacent electrons have a different surface cold-spot problem; the stem has to say photon edges.

**Traps.** Confirm \(L\) is the length along the match, not the width. Draw SSD, half-length, and depth as similar triangles before substituting.

**Sources.** Khan and Gibbons, adjacent fields and the gap formula.

## Gap Calculation Mini-Quiz

**Skills this quiz checks**

- Identify \(L\) as skin field length and \(d\) as the match depth.
- Compute both half-field contributions, including unequal SSDs.
- Predict a hot junction for a skin gap that is too small and a cold junction for a skin gap that is too large.
- Set the gap to zero when both match edges are central-axis half-beams.

## Couch/Collimator Divergence Tutorial

**Objectives:** IV.3

**What the exam expects:** Compute the angle between the central axis and a field edge, and use that angle as a collimator or couch rotation when the goal is to line one diverging edge up with a nondivergent border.

**Formula**

\[
\theta = \arctan\left(\frac{0.5 \times L}{\mathrm{SAD}}\right)
\]

- \(\theta\): angle from the central axis out to the field edge
- \(L\): field length at isocenter, in the direction being rotated (cm)
- \(\mathrm{SAD}\): source-to-axis distance (cm)
- \(0.5 \times L\): half-field width at isocenter, the opposite side of the right triangle
- \(\mathrm{SAD}\): the adjacent side

For an SSD setup, replace SAD with SSD if \(L\) is the field length on the skin. Half-beam block on the match line puts the edge on the central axis, so \(\theta = 0\) on that border.

### Worked example

**Given.** SAD = 100 cm. Field length at isocenter \(L = 20\) cm. Find the divergence of the field edge from the central axis.

**Substitute.**

\[
\theta = \arctan\left(\frac{0.5 \times 20}{100}\right) = \arctan(0.100)
\]

**Arithmetic.** \(\arctan(0.100) = 5.71^\circ\).

**Check.** \(\tan(5.71^\circ) \approx 0.100\). In radians the angle is about 0.0997, and \(0.0997 \times (180/\pi) \approx 5.71\). A 10 cm half-field at 100 cm is a 1-in-10 slope.

**Result means.** The edge diverges 5.71° from the central axis. The rotation that lays that edge on a nondivergent match line is 5.71°. Which motion carries the angle depends on the border. On a breast tangent the superior–inferior length is a couch kick, not a collimator angle. Leaving that rotation at 0° keeps a diverging overlap or gap against a half-beam neighbor.

**Wrong turns**

- Using the full field length in the arctan: \(\arctan(20/100) = \arctan(0.2) \approx 11.3^\circ\), twice the geometry.
- Reporting the angle in radians on a stem that asks for degrees.
- Applying a nonzero match angle to a half-beam border.
- Using this angle as a wedge angle or a hinge angle (module 34).

**Traps.** Name which border the rotation follows. On a breast tangent the couch kick uses the superior–inferior length and takes the superior border out of the supraclavicular field. A gantry angle, or a half-beam jaw, takes the posterior border out of lung. After the couch kick, the collimator only turns that posterior border parallel to the chest wall. The couch does not set the posterior width.

**Sources.** Khan and Gibbons, beam divergence. Bentel, clinical matching of tangent and supraclavicular fields. The next lesson assigns that match to a couch kick on the field length.

## Couch/Collimator Divergence Mini-Quiz

**Skills this quiz checks**

- Compute \(\arctan((0.5 L)/\mathrm{SAD})\) in degrees and check with tangent.
- Use the half-length, not the full length.
- Assign collimator rotation and couch rotation to different field borders.
- Give 0° when the border is a half-beam central-axis edge.

## Breast Tangent Calculation Tutorial

**Objectives:** IV.3, III.7

**What the exam expects:** For intact-breast tangents matched to a supraclavicular field, compute the couch kick that takes superior-border divergence out of that field. The angle uses the superior–inferior length. State the assumption. Posterior divergence into lung is a gantry angle or a half-beam jaw; the next lesson computes it. After the couch kick, the collimator only turns the posterior border parallel to the chest wall (Bentel). The couch does not set the posterior width.

**Formula**

\[
\theta = \arctan\left(\frac{0.5 \times \text{tangent length}}{\mathrm{SAD}}\right)
\]

- \(\theta\): couch kick
- Tangent length: superior–inferior field length of the tangent at isocenter (cm)
- SAD: source-to-axis distance (cm)

**Assumption.** The supraclavicular field is half-beam blocked inferiorly, so its inferior border is the central axis and does not diverge. The tangent’s superior border does diverge. The couch is kicked so the tangent’s superior edge lies along that nondivergent match line. This matches geometric borders. It is not a calculation of the hot spot in the match, and it assumes the length used is the superior–inferior length at isocenter. The collimator rotation after the kick only puts the posterior border back parallel to the chest wall. That collimator turn is not \(\theta\).

### Worked example

**Given.** Tangent length = 20 cm at SAD = 100 cm.

**Substitute.** \(\theta = \arctan((0.5 \times 20)/100) = \arctan(0.100) = 5.71^\circ\).

**Check.** \(\tan(5.71^\circ) \approx 0.100\). Half-length 10 cm over 100 cm is the same triangle as the previous lesson, applied to the supraclav match.

**Result means.** Set the couch kick near 5.7° so the superior tangent border follows the half-beam supraclavicular border. A couch left at 0° lets that border diverge into or away from the supraclavicular field. This 5.7° is not a collimator angle. A 16 cm posterior width is a gantry angle of about 4.6°, not this couch kick.

**Wrong turns**

- Using the posterior width in the couch-kick formula. That width belongs to the gantry angle, or the divergence is removed with a half-beam jaw.
- Calling 5.7° a collimator rotation. After the kick, the collimator only brings the posterior border parallel to the chest wall.
- Forgetting the half: \(\arctan(20/100)\).
- Applying a skin gap formula and a couch kick to the same supraclav match. Half-beam plus couch kick is one technique. A skin gap is a different technique.
- Khan versus Bentel as if they changed this arctan. They differ on electron coverage rules (module 45). This breast angle is geometry.

**Traps.** Write “half-beam supraclav, diverging superior tangent border” at the top of the solution. If the supraclav is not half-beamed, the assumption is gone and both edges diverge. The couch kick uses the length. It does not set the posterior width.

**Sources.** Bentel, breast technique (couch kick to a half-beam supraclavicular field; collimator then parallels the chest wall). Khan and Gibbons, divergence angle.

## Breast Tangent Calculations

**Objectives:** IV.3

**What the exam expects:** Compute the gantry angle that makes the posterior edges of opposed tangents coplanar, so those edges do not diverge into lung. A half-beam jaw on the posterior border is the other way to remove that divergence. State central lung distance, anterior flash, and SSD and depth when the isocenter is at mid-separation.

**Formula**

\[
\phi = \arctan\left(\frac{0.5 \times W}{\mathrm{SAD}}\right)
\qquad
G_{\mathrm{lateral}} = G_{\mathrm{medial}} + 180^\circ - 2\phi
\]

- \(\phi\): divergence of one posterior edge from the central axis. The gantry uses it. This is not a couch kick.
- \(W\): tangent field width at isocenter, the opening whose posterior edge would otherwise diverge into lung (cm)
- SAD: source-to-axis distance (cm)
- \(G_{\mathrm{medial}}\), \(G_{\mathrm{lateral}}\): medial and lateral gantry angles (degrees)
- \(2\phi\): both posterior edges. The lateral gantry sits \(2\phi\) inside a straight 180° opposition. In this formula \(\phi\) is the \(\theta\) of \(G_{\mathrm{lateral}} = G_{\mathrm{medial}} + 180^\circ - 2\theta\).

**Assumption.** Isocentric tangents. The lateral gantry is set so the posterior edges are coplanar, and geometric divergence no longer carries that border into lung. \(W\) is the posterior-border opening at isocenter. The angle matches a border. It does not compute a lung DVH. The couch kick from the previous lesson uses the superior–inferior length and is a different rotation. After that kick, the collimator only turns the posterior border parallel to the chest wall. The couch does not set the posterior width. A half-beam or asymmetric jaw on the posterior border puts that edge on the central axis, so \(\phi = 0\) and \(G_{\mathrm{lateral}} = G_{\mathrm{medial}} + 180^\circ\).

### Worked example

**Given.** Tangent width \(W = 16\) cm, SAD = 100 cm.

**Substitute.** \(\phi = \arctan((0.5 \times 16)/100) = \arctan(0.080)\).

**Arithmetic.** \(\arctan(0.080) = 4.57^\circ\).

**Check.** \(\tan(4.57^\circ) \approx 0.080\). Half-width 8 cm over 100 cm.

**Result means.** A gantry adjustment of about 4.6° is the divergence of that posterior edge. Using the 20 cm superior–inferior length here would give the couch kick (5.71°) instead of this gantry angle. The couch is not kicked by 4.6°.

### Worked example

**Given.** Medial gantry \(G_{\mathrm{medial}} = 50^\circ\). Posterior width \(W = 20\) cm at SAD = 100 cm. Set the lateral gantry so the posterior edges are coplanar.

**Substitute.** \(\phi = \arctan((0.5 \times 20)/100) = \arctan(0.100) = 5.710593^\circ\). Then \(2\phi = 11.421186^\circ\).

**Arithmetic.** \(G_{\mathrm{lateral}} = 50 + 180 - 11.421186 = 218.578814^\circ\), which rounds to \(218.6^\circ\).

**Check.** A straight opposed pair would be \(50 + 180 = 230^\circ\). The \(11.421186^\circ\) reduction is one \(\phi\) from each posterior edge. \(\tan(5.71^\circ) \approx 0.100\).

**Result means.** Set the lateral gantry to 218.6°. The 5.71° figure is a gantry ingredient here because 20 cm is the posterior width. The same 5.71° on a 20 cm superior–inferior length is the couch kick, and it is not added into this gantry angle.

### Half-beam posterior border

A posterior jaw on the central axis has \(\phi = \arctan(0/\mathrm{SAD}) = 0^\circ\). Then \(G_{\mathrm{lateral}} = G_{\mathrm{medial}} + 180^\circ\). Example: medial gantry 62° gives a lateral gantry of 242°. That posterior border needs no 2φ closure and no couch kick.

### Central lung distance

On the tangent DRR or port, central lung distance is the lung inside the field along the central axis, measured from the posterior border to the chest wall. The usual range is about 2–3 cm. A shorter distance can miss chest wall. A longer distance includes more lung. Central lung distance is a length in centimeters. It is not the gantry angle, not flash, and not a lung DVH.

### Flash

The open beam extends about 1.5–2 cm past the anterior skin so the breast stays inside the field through breathing and small setup changes. Flash is that skin margin. It is not the couch kick and not the central lung distance.

### SSD and depth from separation

For isocentric tangents with the isocenter at mid-separation, depth from skin to isocenter is half the separation, and SSD is SAD minus that depth.

**Given.** Separation = 22 cm. SAD = 100 cm. Isocenter at mid-separation.

**Arithmetic.** Depth \(= 22/2 = 11\) cm. SSD \(= 100 - 11 = 89\) cm.

If the isocenter is not at mid-separation, use the depth along that beam. Half the separation applies only at mid-separation.

**Wrong turns**

- One rotation used for both borders. The couch kick is the superior–inferior length. The gantry angle, or a half-beam jaw, is the posterior width.
- Sign of the gantry closure reversed: \(G_{\mathrm{lateral}} = G_{\mathrm{medial}} + 180^\circ + 2\phi\) sends the posterior edges farther into lung.
- Dropping the 2 and subtracting only one \(\phi\), which still leaves one posterior edge diverging.
- Skipping the gantry closure because a couch kick was already set.
- Treating \(\phi\), central lung distance, or flash as lung dose in gray.
- Using the full separation as the depth. For a 22 cm separation that gives depth 22 cm and SSD \(100 - 22 = 78\) cm.
- Adding depth to SAD. For the same example, \(100 + 11 = 111\) cm is not the SSD.

**Traps.** Label three motions on a sketch: couch = superior match from the length, gantry or half-beam jaw = posterior lung border from the width, collimator after the kick = posterior border parallel to the chest wall. The couch does not set the posterior width.

**Sources.** Bentel, tangent beam geometry (couch kick, then collimator parallel to the chest wall). Khan and Gibbons, \(\arctan\) divergence and coplanar posterior tangent edges.

## Breast Tangent Calculation Mini-Quiz

**Skills this quiz checks**

- Couch kick from tangent length, under the half-beam supraclavicular assumption.
- Gantry angle from tangent width, including lateral = medial + 180° − 2φ for coplanar posterior edges.
- Half-beam posterior border means φ = 0, so the lateral gantry is medial + 180°.
- Central lung distance about 2–3 cm, anterior flash about 1.5–2 cm, and SSD = SAD − (separation / 2) when the isocenter is at mid-separation.
- Half the field dimension over SAD, then arctan, in degrees.
- Refuse to add the couch kick and the gantry angle, or to reuse either as a skin gap.

## Transmission, HVL, Linear Attenuation Coefficient

**Objectives:** I.10, VI.3

**What the exam expects:** Use the narrow-beam exponential, convert between \(\mu\) and HVL, and convert HVL to TVL. Two half-value layers transmit 25%. This is narrow-beam attenuation (scatter not added back). A broad beam needs a buildup factor the stem must give; do not invent one.

**Formulas**

\[
I = I_0 e^{-\mu x}
\qquad
\mathrm{HVL} = \frac{0.693}{\mu}
\qquad
\mathrm{TVL} \approx 3.32 \times \mathrm{HVL}
\]

- \(I_0\): intensity or dose rate with no absorber
- \(I\): intensity transmitted through thickness \(x\)
- \(\mu\): linear attenuation coefficient, per unit thickness
- \(x\): thickness, same length unit as \(\mu\)
- HVL: thickness that cuts the beam in half
- TVL: thickness that transmits 10%
- \(0.693\): \(\ln 2\) to three digits
- \(3.32\): \(\ln(10)/\ln(2) \approx 3.322\), the number of HVLs in one TVL

Transmission through \(n\) HVLs is \((1/2)^n\). Two HVLs: \((1/2)^2 = 0.25\), so 25% is transmitted and 75% is removed.

### Worked example

**Given.** A shield has HVL = 1.2 cm. Incident dose \(I_0 = 100\) cGy. Thickness \(x = 2.4\) cm, which is two HVLs.

**Substitute.** \(\mu = 0.693 / 1.2 = 0.5775\) cm\(^{-1}\). \(n = 2.4 / 1.2 = 2\).

\[
\frac{I}{I_0} = \left(\frac{1}{2}\right)^2 = 0.25
\qquad
I = 100 \times 0.25 = 25 \text{ cGy}
\]

The exponential route: \(\mu x = 0.5775 \times 2.4 = 1.386\), and \(e^{-1.386} \approx 0.250\). The 0.0001 difference from 0.250 is rounding \(\ln 2\) to 0.693. For an exact integer number of HVLs, use \((1/2)^n\).

**TVL.** \(3.32 \times 1.2 = 3.98\) cm. One TVL of this shield would transmit \(100 \times 0.10 = 10\) cGy, not 25 cGy.

**Check.** Two HVLs: 100 → 50 → 25. Three HVLs would transmit 12.5 cGy. That is not one TVL. One TVL is 3.32 HVLs and transmits 10%.

**Result means.** A 2.4 cm shield of this material transmits 25 cGy of the original 100 cGy under narrow-beam conditions.

**Wrong turns**

- Two HVLs transmit 50% (that is one HVL) or 10% (that is one TVL).
- Three HVLs equal one TVL. Three HVLs transmit 12.5%, not 10%.
- \(\mu = 0.693 \times \mathrm{HVL}\) instead of \(0.693/\mathrm{HVL}\).
- Adding broad-beam scatter without a stated buildup factor.
- Mixing cm and mm in \(\mu x\).

**Traps.** “Percent transmitted” and “percent attenuated” add to 100. Two HVLs: 25% transmitted, 75% attenuated.

**Sources.** Khan and Gibbons, HVL, TVL, and exponential attenuation. NCRP 151 uses tenth-value layers for barrier thickness; the conversion factor is the same 3.32.

## Transmission Calculation Tutorial

**Objectives:** I.10, VI.3

**What the exam expects:** A full attenuation problem that starts from \(\mu\) or HVL and ends in transmitted dose, with the integer-HVL result used as the check.

### Worked example

**Given.** \(\mu = 0.0462\) cm\(^{-1}\). Thickness \(x = 30\) cm. Incident dose \(I_0 = 200\) cGy. Narrow beam.

**Formula.** \(I = I_0 e^{-\mu x}\), and \(\mathrm{HVL} = 0.693/\mu\).

**Substitute.**

\[
\mathrm{HVL} = \frac{0.693}{0.0462} = 15.0 \text{ cm}
\]

\[
n = \frac{30}{15} = 2.00 \text{ HVL}
\qquad
I = 200 \times (1/2)^2 = 200 \times 0.25 = 50 \text{ cGy}
\]

**Arithmetic.** \(0.0462 \times 15 = 0.693\), so the HVL is exactly 15.0 cm when 0.693 is the constant in use. \(30/15 = 2\). \(200/4 = 50\).

**Check.** \(\mu x = 0.0462 \times 30 = 1.386\), and \(e^{-1.386} \approx 0.250\), so \(200 \times 0.250 = 50\) cGy. TVL \(\approx 3.32 \times 15.0 = 49.8\) cm. This 30 cm shield is thinner than one TVL, and 50 cGy is 25% of 200 cGy, not 10%.

**Result means.** The shield transmits 50 cGy. Half the thickness (15 cm) would have transmitted 100 cGy. Twice the thickness (60 cm, four HVLs) would transmit \(200 \times (1/16) = 12.5\) cGy.

**Wrong turns**

- Reporting the attenuated dose (150 cGy) when the question asks for transmitted dose.
- Using 0.693 as \(\mu\) itself.
- Linear attenuation: “30 cm is twice 15 cm, so it removes twice 50%,” which wrongly gives zero transmission. Attenuation stacks by halves, not by subtraction of percents.
- A second HVL that is a different thickness. In this narrow-beam monoenergetic model every HVL is 15 cm. A polyenergetic beam hardens; the stem will say so if the second HVL changes.

**Traps.** Decide transmitted versus removed before you touch the calculator. Circle which one the question names.

**Sources.** Khan and Gibbons, exponential attenuation worked numerically.

## Transmission, HVL, Linear Attenuation Coefficient Quiz

**Skills this quiz checks**

- Convert \(\mu\) to HVL with \(0.693/\mu\) and HVL to thickness in number of HVLs.
- Two HVLs transmit 25%. One HVL transmits 50%. One TVL transmits 10%.
- Use \(I = I_0 e^{-\mu x}\) and check an integer number of HVLs with \((1/2)^n\).
- Keep cm and mm consistent, and answer with transmitted dose when that is the question.
- Leave broad-beam scatter out unless a buildup factor is given.

## Geometric Penumbra

**Objectives:** IV.3

**What the exam expects:** Compute geometric penumbra from source size and distances. Separately define physical penumbra as the 80%–20% width at dmax. The two are not the same number.

**Formula**

\[
P = s\,\frac{\mathrm{SSD} + d - \mathrm{SDD}}{\mathrm{SDD}}
\]

- \(P\): geometric penumbra at depth \(d\) (cm)
- \(s\): source size (cm)
- SSD: source-to-skin distance (cm)
- \(d\): depth of the point (cm)
- SDD: source-to-diaphragm (or source-to-collimator) distance (cm)

Physical penumbra is the lateral distance between the 80% and 20% dose points, measured at dmax, as a fraction of the central-axis dose at that depth. Scatter and collimator transmission make the physical penumbra larger than the geometric penumbra. A linac source is small, so geometric penumbra is small; cobalt-60 is where the formula usually changes the answer.

### Worked example

**Given.** Cobalt source size \(s = 2.0\) cm. SSD = 80 cm. Depth \(d = 0.5\) cm (dmax). Source-to-diaphragm distance SDD = 50 cm.

**Substitute.**

\[
P = 2.0 \times \frac{80 + 0.5 - 50}{50} = 2.0 \times \frac{30.5}{50}
\]

**Arithmetic.** \(30.5 / 50 = 0.610\). \(2.0 \times 0.610 = 1.22\) cm.

**Check.** \(2 \times 30.5 = 61\), and \(61/50 = 1.22\).

**Result means.** Geometric penumbra at dmax is 1.22 cm. If a film measurement at dmax shows an 80%–20% width of, for example, 1.6 cm, that 1.6 cm is the physical penumbra. Do not relabel 1.22 cm as the 80–20 width.

**Wrong turns**

- Using SSD in the denominator instead of SDD.
- Dropping the depth: \((80-50)/50 = 0.60\), then \(1.20\) cm, a small but real miss when \(d\) is not tiny.
- Calling geometric penumbra the 80%–20% width. That definition is physical penumbra, at dmax.
- Reading the fraction backwards. Geometric penumbra shrinks when the diaphragm moves closer to the patient, because SDD gets larger: the denominator grows and (SSD + d − SDD) shrinks. A diaphragm closer to the source (smaller SDD) widens geometric penumbra.

**Traps.** SDD is source-to-diaphragm. SSD is source-to-skin. They are both in the formula and they are not interchangeable.

**Sources.** Khan and Gibbons, geometric penumbra. Physical penumbra as the 80%–20% width at dmax is the definition used on these items.

### Off-axis dose

**Objectives:** IV.3

Dose off the central axis at the same depth is the on-axis dose times the off-axis ratio (OAR), also called the off-axis factor.

\[
D_{\text{off}} = D_{\text{axis}} \times \mathrm{OAR}
\]

**Given.** On-axis dose at the depth of interest is 200 cGy. The stem gives OAR = 1.04 at the off-axis point (beam horns).

**Arithmetic.** \(200 \times 1.04 = 208\) cGy.

**Check.** \(208 / 200 = 1.04\).

**Result means.** The off-axis point receives 208 cGy because of the horns, not because of a second MU calculation. An OAR below 1 (near the penumbra) reduces dose. OAR is not a wedge factor and not \(S_c\).

**Wrong turns.** Applying inverse square across the field instead of the OAR the stem gives. Using OAR on a different depth than the table.

## Geometric Penumbra Mini-Quiz

**Skills this quiz checks**

- Compute \(P = s(\mathrm{SSD}+d-\mathrm{SDD})/\mathrm{SDD}\) and name every distance.
- Define physical penumbra as the 80%–20% dose width at dmax.
- Apply an off-axis ratio at the same depth: on-axis dose times OAR.
- Refuse to swap SDD and SSD.

## Timer Setting Tutorial

**Objectives:** I.10, IV.3

**What the exam expects:** For a cobalt-60 treatment, dose follows the effective time, which is the set time plus the timer error (end effect). Find the timer error from two readings, then the dose rate, then the set time for a prescribed dose.

**Formula**

\[
R = \dot{D}\,(t + \tau)
\]

- \(R\): measured dose (cGy)
- \(\dot{D}\): dose rate during the time the source is actually in position (cGy/min)
- \(t\): set time on the timer (min)
- \(\tau\): timer error, or end effect (min). Negative when source transit eats time, which is the usual cobalt case

Two readings solve the two unknowns \(\dot{D}\) and \(\tau\). Dose is never \(\dot{D} \times t\) alone.

### Worked example

**Given.** A 1.00 min setting reads 80 cGy. A 2.00 min setting reads 180 cGy. Find \(\tau\), \(\dot{D}\), and the set time that delivers 200 cGy.

**Substitute.**

\[
\frac{180}{80} = \frac{2 + \tau}{1 + \tau}
\qquad
2.25 = \frac{2 + \tau}{1 + \tau}
\]

**Arithmetic.**

\[
2.25(1 + \tau) = 2 + \tau
\]

\[
2.25 + 2.25\tau = 2 + \tau
\qquad
2.25 - 2 = \tau - 2.25\tau
\qquad
0.25 = -1.25\tau
\]

\[
\tau = \frac{0.25}{-1.25} = -0.20 \text{ min}
\]

From the longer reading: \(180 = \dot{D}(2.00 - 0.20) = \dot{D} \times 1.80\), so \(\dot{D} = 180/1.80 = 100\) cGy/min.

**Check.** Short reading: \(100 \times (1.00 - 0.20) = 80\) cGy. Long reading: \(100 \times 1.80 = 180\) cGy.

**Set time for 200 cGy.** Effective time must be \(200/100 = 2.00\) min.

\[
t + \tau = 2.00
\qquad
t + (-0.20) = 2.00
\qquad
t = 2.20 \text{ min}
\]

**Check.** Effective time \(= 2.20 + (-0.20) = 2.00\) min. Dose \(= 100 \times 2.00 = 200\) cGy. Setting 2.00 min by mistake gives effective time 1.80 min and dose 180 cGy.

**Result means.** The source transit removes 0.20 min from every run. The timer is set 0.20 min longer than the ideal exposure so the patient still receives 200 cGy.

**Wrong turns**

- Ignoring \(\tau\) and setting \(t = \text{dose}/\text{dose rate} = 2.00\) min, which delivers 180 cGy in this example.
- Sign error: subtracting a negative error again, which sets \(t = 1.80\) min and delivers only 160 cGy.
- Using half-life or mean life. Cobalt decay is real over months and is a different correction; this lesson is the end effect on a single treatment.
- Averaging the two dose rates \(80/1\) and \(180/2\) (80 and 90) to get 85 cGy/min. The rates disagree because \(\tau\) is still in both readings. Solve the pair.

**Traps.** Write \(t + \tau\) as the time that multiplies dose rate. Then keep the minus sign on \(\tau\) visible until the last line.

**Sources.** Khan and Gibbons, cobalt timer error (end effect).

## Timer Setting Mini-Quiz

**Skills this quiz checks**

- Set up \(R = \dot{D}(t+\tau)\) from two exposures and solve for a negative end effect.
- Recover dose rate from \((t+\tau)\), not from \(t\) alone.
- Add the end effect back when choosing the set time, and reverse-check both original readings.
- Keep radioactive half-life out of a timer-error item.

## Trigonometry

**Objectives:** IV.3

**What the exam expects:** A right triangle for beam divergence: opposite side is the half-field, adjacent side is SAD or SSD, and the angle is \(\arctan(\mathrm{opposite}/\mathrm{adjacent})\). The same triangle is the breast collimator and couch work above. This lesson also holds the other IV.3 calculations that do not have their own heading: entrance dose, exit dose, and re-treatment.

### Worked example

**Given.** Half-field at isocenter is 7.0 cm. SAD = 100 cm.

**Formula.** \(\theta = \arctan(7/100) = \arctan(0.070)\).

**Arithmetic.** \(\arctan(0.070) = 4.00^\circ\).

**Check.** \(\tan(4.00^\circ) \approx 0.070\). For a small angle, \(\sin(4.00^\circ) \approx 0.0698\) and \(\cos(4.00^\circ) \approx 0.9976\), and \(0.0698^2 + 0.9976^2 \approx 1\).

**Result means.** The field edge sits 4.0° off the central axis. Use degrees on the collimator or couch unless the stem asks for radians.

**Wrong turns.** Full field length as the opposite side. Radians reported as degrees. Sine and tangent swapped for a large angle, where they are not equal.

**Traps.** Write opposite (half-field) and adjacent (SAD or SSD) on the triangle before you take the arctan. The full field length doubles the angle.

**Sources.** Khan and Gibbons for the divergence triangle. The clinical use is the breast match in this module.

### Entrance dose and exit dose

PDD is defined from dmax, so surface (entrance) dose is a separate percent of the dmax dose. The stem gives that percent. Exit dose, if you use the SSD PDD at the exit depth, already includes inverse square and scatter for that SSD, and it still assumes full backscatter beyond the point. The real exit surface has no tissue beyond it, so the PDD estimate is a bit high. Say that assumption in the answer.

**Given.** Dose at dmax (given dose) is 250 cGy. The stem says surface dose is 15% of dmax. Patient separation is 22 cm and PDD at 22 cm is 38%.

**Entrance.** \(0.15 \times 250 = 37.5\) cGy.

**Exit, from the PDD table.** \(0.38 \times 250 = 95\) cGy.

**Check.** \(250 \times 0.15 = 37.5\). \(250 \times 0.40 = 100\), minus \(250 \times 0.02 = 5\), equals 95.

**Result means.** Skin on the entrance side receives about 37.5 cGy. The exit side receives about 95 cGy on the PDD estimate, slightly less in reality because backscatter from tissue beyond the exit is missing.

**Wrong turns.** Using TMR and PDD together for the exit. Taking entrance dose as the given dose. Forgetting the missing-backscatter assumption.

### Re-treatment

Add courses in the same biological unit. Physical gray add only when the fraction size is the same (or you have decided a physical sum is truly what the question asks). Otherwise convert each course to EQD2 and then add. Module 38 is the full argument. The formula is

\[
\mathrm{EQD2} = D \times \frac{d_f + \alpha/\beta}{2 + \alpha/\beta}
\]

- \(D\): total physical dose of that course (Gy)
- \(d_f\): dose per fraction (Gy)
- \(\alpha/\beta\): the value the stem states for that organ (Gy)

**Given.** Cord previously received 45 Gy in 1.8 Gy fractions. A new plan would add 20 Gy in 2.0 Gy fractions. Use \(\alpha/\beta = 2\) Gy for this example only; it is the stem’s value, not a universal cord constant.

**Prior course.** \(45 \times (1.8+2)/(2+2) = 45 \times 3.8/4 = 45 \times 0.95 = 42.75\) Gy EQD2.

**New course.** \(20 \times (2+2)/(2+2) = 20\) Gy EQD2.

**Sum.** \(42.75 + 20 = 62.75\) Gy EQD2. The physical sum is \(45+20 = 65\) Gy.

**Check.** \(45 \times 0.95 = 42.75\). Because the old fractions were smaller than 2 Gy, EQD2 is below the physical dose.

**Result means.** A comparison with a conventional cord limit has to be in one system. Adding 65 Gy of mixed physical dose and then calling it EQD2 overstates this particular sum. Half-life does not belong here. Khan versus Bentel does not change EQD2; using the wrong \(\alpha/\beta\) does.

**Wrong turns.** Adding 45 and 20 and comparing the physical 65 Gy to an EQD2 limit. Using \(\alpha/\beta = 10\) Gy for a late-responding organ when the stem said 2. Forgetting to convert the prior course because “it was already delivered.”

## Extended-Distance and Asymmetric Field Geometry

**Objectives:** IV.3

**What the exam expects:** Three geometry conversions that the gap and divergence lessons above do not cover. (1) A collimator setting is defined at 100 cm; a TBI or hemibody field is defined at the treatment distance, so divide the required length by the distance ratio. (2) When the required setting exceeds the 40 cm jaw limit, rotate the collimator 45° and let the diagonal of the square cover the patient: the side needed is the diagonal divided by \(\sqrt{2}\). (3) With asymmetric jaws the center of the open field is off the central axis; the radius from the axis to the field center is the hypotenuse of the two half-differences. The same 100 cm definition is the trap in a gap calculation: a collimator reading at an extended SSD must be projected to the skin before it goes into the gap formula, although, because the projection and the SSD cancel, the reading divided by 100 gives the same answer as the skin length divided by the SSD.

**Formulas**

\[
\text{setting at 100} = L_{\text{treat}} \times \frac{100}{\mathrm{SPD}}
\qquad
\text{side at } 45^\circ = \frac{\text{diagonal}}{\sqrt{2}}
\qquad
r = \sqrt{\left(\frac{X_1 - X_2}{2}\right)^2 + \left(\frac{Y_1 - Y_2}{2}\right)^2}
\]

- \(L_{\text{treat}}\): field length needed at the treatment distance (cm)
- \(\mathrm{SPD}\): source-to-patient distance where that length is measured (cm)
- diagonal: the projected length at 100 cm that the rotated square must span
- \(X_1, X_2, Y_1, Y_2\): asymmetric jaw positions measured from the central axis (cm); \(X_1 + X_2\) is the field width
- \(r\): distance from the central axis to the center of the open field (cm)

### Worked example: extended distance with and without the diagonal

**Given.** A TBI patient is 180 cm long and is treated at 400 cm from the source.

**Substitute.** Setting at 100 cm \(= 180 \times 100/400 = 45\) cm.

**Arithmetic.** 45 cm exceeds the 40 cm jaw maximum, so rotate the collimator 45°. Side \(= 45/\sqrt{2} = 45/1.414 = 31.8\) cm.

**Check.** A 31.8 cm square has a diagonal of \(31.8 \times 1.414 = 45\) cm at 100 cm, which projects to \(45 \times 4 = 180\) cm at 400 cm. A 150 cm patient at the same distance needs \(150/4 = 37.5\) cm and fits without rotation.

**Result means.** Set 31.8 × 31.8 cm with the collimator at 45°. The corners of the square then extend beyond the patient; the unused corners are not a dose problem in TBI, but the width across the patient at the ends of the diagonal is small, which is why TBI uses the diagonal only when the straight setting will not fit.

### Second pass: radius to the center of an asymmetric field

**Given.** Jaws X1 = 8 cm, X2 = 4 cm, Y1 = 3 cm, Y2 = 11 cm.

**Substitute.** Half-differences: \((8-4)/2 = 2\) cm toward X1, \((11-3)/2 = 4\) cm toward Y2.

**Arithmetic.** \(r = \sqrt{2^2 + 4^2} = \sqrt{20} = 4.47\) cm.

**Check.** The field is 12 × 14 cm; its center is 2 cm off the axis in X and 4 cm in Y, and \(4.47^2 = 20\). Adding the two offsets, 6 cm, is the usual slip.

**Result means.** The off-axis ratio and any point-dose check for the field center must be read 4.47 cm from the central axis, not at the axis.

### Third pass: collimator reading at an extended SSD in a gap

**Given.** Field 1 is 24 cm long on the skin at SSD 100. Field 2 has a collimator reading of 14 cm and is set at SSD 125. Match depth 8 cm.

**Substitute.** Field 2 skin length \(= 14 \times 125/100 = 17.5\) cm. Gap \(= 12 \times 8/100 + 8.75 \times 8/125\).

**Arithmetic.** \(0.96 + 0.56 = 1.52\) cm.

**Check.** The second term is also \(7 \times 8/100 = 0.56\) cm: half the reading over 100 cm. Using 14 cm as if it were already the skin length at SSD 125 gives \(0.96 + 7 \times 8/125 = 1.41\) cm, a gap 1 mm too small.

**Wrong turns**

- Multiplying the patient length by the distance ratio instead of dividing.
- Multiplying by \(\sqrt{2}\) instead of dividing for the rotated square.
- Adding the jaw half-differences instead of taking the hypotenuse, or using the full differences.
- Feeding a collimator reading into the gap formula as a skin length at an SSD other than 100.

**Traps.** Every collimator number is a length at 100 cm until you project it.

**Sources.** Khan and Gibbons, field size definitions and TBI geometry; AAPM Report 17 for TBI technique.

## Orthovoltage Timer Chain

**Objectives:** I.10, IV.3

**What the exam expects:** The timer-error lesson above solved for the end effect. This lesson is the full orthovoltage chain from an in-air exposure rate to a treatment time. The calibration is an exposure rate in R/min at a stated distance. Move it to the treatment SSD with inverse square, convert roentgen to cGy with the f-factor, add backscatter with the BSF to get the surface (dmax) dose rate, then apply PDD to get the dose rate at depth. Time is the prescribed depth dose divided by that rate.

**Formula**

\[
\dot{D}(d) = \dot{X}_{\text{cal}} \left(\frac{d_{\text{cal}}}{\mathrm{SSD}}\right)^2 \times f \times \mathrm{BSF} \times \frac{\mathrm{PDD}}{100}
\qquad
t = \frac{D_{\text{Rx}}}{\dot{D}(d)}
\]

- \(\dot{X}_{\text{cal}}\): in-air exposure rate at the calibration distance \(d_{\text{cal}}\) (R/min)
- \(\mathrm{SSD}\): treatment source-to-skin distance (cm)
- \(f\): roentgen-to-cGy conversion for tissue at this beam quality (cGy/R)
- \(\mathrm{BSF}\): backscatter factor for the applicator size and quality
- \(\mathrm{PDD}\): percent depth dose at the prescription depth
- \(D_{\text{Rx}}\): prescribed dose at depth (cGy)

### Worked example

**Given.** 120 R/min in air at 50 cm. Treatment SSD 55 cm. \(f = 0.94\) cGy/R. BSF = 1.20. PDD at 3 cm = 70%. Prescription 300 cGy at 3 cm.

**Substitute.** \(\dot{D}(3) = 120 \times (50/55)^2 \times 0.94 \times 1.20 \times 0.70\).

**Arithmetic.** \((50/55)^2 = 0.8264\). \(120 \times 0.8264 = 99.17\) R/min. \(\times 0.94 = 93.22\) cGy/min in air. \(\times 1.20 = 111.87\) cGy/min at the surface. \(\times 0.70 = 78.31\) cGy/min at 3 cm. \(t = 300/78.31 = 3.83\) min.

**Check.** \(78.31 \times 3.83 = 300\) cGy. Surface dose during the treatment \(= 111.87 \times 3.83 = 428.6\) cGy, which is also \(300/0.70\).

**Result means.** Set 3.83 min (3 min 50 s), plus any timer-error correction the unit needs. The skin receives 428.6 cGy for 300 cGy at 3 cm, because orthovoltage has no skin sparing and the surface is dmax.

**Wrong turns**

- Dropping inverse square because the applicator "defines the SSD": \(300/(120 \times 0.94 \times 1.20 \times 0.70) = 3.17\) min.
- Leaving BSF out, which gives 4.60 min and overdoses the patient by 20%.
- Dividing by BSF, 5.52 min.
- Treating the roentgen as a cGy.

**Traps.** Write the five factors in order: ISL, f, BSF, PDD, then divide into the prescription. The surface dose is the prescription divided by the PDD.

**Sources.** Khan and Gibbons, orthovoltage dosimetry (exposure, f-factor, BSF).

## Attenuation From Mass Attenuation Coefficient and Two Intensities

**Objectives:** I.10, VI.3

**What the exam expects:** Three turns of the exponential that the HVL lessons above do not ask. (1) The stem gives a mass attenuation coefficient and a density, so the linear coefficient is their product. (2) The stem gives two intensities and the thickness between them, so the HVL is back-solved from the natural log of their ratio. (3) The stem asks for the thickness that transmits 5%, which is \(\log_2 20 = 4.32\) HVL, not 5 HVL and not one TVL.

**Formulas**

\[
\mu = \left(\frac{\mu}{\rho}\right) \rho
\qquad
\mathrm{HVL} = \frac{0.693\, x}{\ln(I_0/I)}
\qquad
n_{\text{HVL}} = \log_2\left(\frac{I_0}{I}\right)
\]

- \(\mu/\rho\): mass attenuation coefficient (cm\(^2\)/g)
- \(\rho\): density (g/cm\(^3\)); the product has units of cm\(^{-1}\)
- \(x\): thickness between the two intensity readings (cm)
- \(n_{\text{HVL}}\): number of half-value layers for a given transmission; 5% needs \(\log_2 20 = 4.32\)

### Worked example: mass attenuation coefficient

**Given.** Lead sheet 0.2 cm thick. \(\mu/\rho = 0.60\) cm\(^2\)/g at this energy. \(\rho = 11.35\) g/cm\(^3\).

**Substitute.** \(\mu = 0.60 \times 11.35 = 6.81\) cm\(^{-1}\). \(\mu x = 6.81 \times 0.2 = 1.362\).

**Arithmetic.** Transmission \(= e^{-1.362} = 0.256\), so 25.6%.

**Check.** HVL \(= 0.693/6.81 = 0.102\) cm, and 0.2 cm is 1.97 HVL; \((1/2)^{1.97} = 0.256\). Forgetting the density, \(e^{-0.60 \times 0.2} = 0.887\), is the usual slip.

**Result means.** The sheet transmits 25.6% and removes 74.4%.

### Second pass: HVL from two readings

**Given.** 250 mR/h falls to 40 mR/h through 1.5 cm of material.

**Substitute.** \(\ln(250/40) = \ln 6.25 = 1.833\). \(\mu = 1.833/1.5 = 1.222\) cm\(^{-1}\).

**Arithmetic.** HVL \(= 0.693/1.222 = 0.567\) cm.

**Check.** 1.5 cm is \(1.5/0.567 = 2.64\) HVL, and \((1/2)^{2.64} = 0.160 = 40/250\).

**Third pass: thickness for 5% transmission.** HVL = 6 mm. \(n = \log_2 20 = 4.32\) HVL, so \(4.32 \times 6 = 25.9\) mm. Check: \((1/2)^{4.32} = 0.050\). Three HVL would transmit 12.5%, five HVL 3.1%, and one TVL (3.32 HVL, 19.9 mm) 10%.

**Wrong turns**

- Using \(\mu/\rho\) as if it were \(\mu\).
- Dividing the thickness by the intensity ratio (linear attenuation) to get the HVL.
- Reading "5%" as five half-value layers.

**Traps.** Check the units on the coefficient. cm\(^2\)/g needs a density; cm\(^{-1}\) does not.

**Sources.** Khan and Gibbons, attenuation coefficients; NCRP 151 for TVL-based barrier arithmetic.

## Mixed-Radiation Dose Equivalent

**Objectives:** VI.3, I.10

**What the exam expects:** When several radiation types contribute absorbed dose at the same point, weight each absorbed dose by its own radiation weighting factor and add. The result is an equivalent dose in sievert (1 cGy × w_R = 1 cSv = 10 mSv). The stem supplies the weighting factors; photons and electrons are 1, alpha particles 20, and neutrons depend on energy (ICRP 103 uses a continuous function that peaks near 20 around 1 MeV), so use the number the stem gives rather than a memorized constant.

**Formula**

\[
H = \sum_i w_{R,i} D_i
\]

- \(D_i\): absorbed dose from radiation type \(i\) (cGy)
- \(w_{R,i}\): radiation weighting factor for that type (dimensionless)
- \(H\): equivalent dose (cSv when \(D\) is in cGy; multiply by 10 for mSv)

### Worked example

**Given.** At a point outside a high-energy treatment room, a survey assigns 0.20 cGy to photons, 0.03 cGy to fast neutrons with \(w_R = 20\), and 0.01 cGy to alpha-emitting contamination with \(w_R = 20\).

**Substitute.** \(H = 0.20 \times 1 + 0.03 \times 20 + 0.01 \times 20\).

**Arithmetic.** \(0.20 + 0.60 + 0.20 = 1.00\) cSv \(= 10\) mSv.

**Check.** The neutron term alone, 0.60 cSv, is three times the photon term even though its absorbed dose is seven times smaller. Summing absorbed doses without weights gives 0.24 cGy, which is 2.4 mSv and is not an equivalent dose.

**Result means.** The equivalent dose is 10 mSv. For a public limit of 1 mSv/yr that is a reportable excess; for an occupational limit of 50 mSv/yr it is a fifth of the annual allowance.

**Wrong turns**

- Adding absorbed doses and calling the sum sievert.
- Applying the neutron factor to every component.
- Dropping the alpha term because its absorbed dose is small.

**Traps.** Write each component on its own line with its factor before adding.

**Sources.** ICRP 103 (radiation weighting factors); 10 CFR 20 for the limits; module 12 for the unit conversions.

## Line Source Versus Point Source

**Objectives:** IV.3, I.10

**What the exam expects:** Inverse square is a point-source law. Close to a line source (a linear brachytherapy source or a long applicator), exposure falls roughly as one over the distance, not one over the distance squared, because the far parts of the line contribute less and less as the point moves away. The usual teaching rule: beyond about twice the active length, treat the line as a point and use inverse square.

**Formulas**

\[
\text{near a line: } \frac{\dot{X}_2}{\dot{X}_1} \approx \frac{r_1}{r_2}
\qquad
\text{far from a line (} r \gtrsim 2L \text{): } \frac{\dot{X}_2}{\dot{X}_1} \approx \left(\frac{r_1}{r_2}\right)^2
\]

- \(r_1, r_2\): perpendicular distances from the source center (cm), both much smaller than the length \(L\) for the near-field rule
- \(L\): active length of the line source (cm)

### Worked example

**Given.** A 10 cm line source reads 120 mR/h at 0.5 cm from its midpoint. Estimate the rate at 2 cm.

**Substitute.** Both distances are far smaller than 10 cm, so use the near-field rule: \(120 \times (0.5/2) = 30\) mR/h.

**Arithmetic.** \(0.5/2 = 0.25\). \(120 \times 0.25 = 30\) mR/h.

**Check.** Inverse square would give \(120 \times 0.0625 = 7.5\) mR/h, a factor of four lower; the 1/r rule is the correct near-field estimate for a long line. At 20 cm or more (twice the 10 cm length) inverse square takes over.

**Result means.** The rate near a long source falls much more slowly than inverse square predicts. For a 4 cm source, inverse square is a fair approximation from about 8 cm outward.

**Wrong turns**

- Using inverse square at a distance much shorter than the source length.
- Applying the 1/r rule beyond twice the source length.
- Using the full length instead of twice the length as the crossover.

**Traps.** Compare the distance to the source length before choosing the rule. TG-43 line-source geometry functions do this exactly; the 1/r and 2L rules are the estimates.

**Sources.** Khan and Gibbons, linear source dose distributions; TG-43U1 line-source geometry factor.

## CSI Angles and the Spine Junction

**Objectives:** IV.3, III.7

**What the exam expects:** In craniospinal irradiation the two rotations use different field lengths. The collimator of the lateral brain fields rotates to match the divergence of the posterior spine field's superior edge, so it uses half the spine field length over the SAD (or SSD). The couch of the lateral brain fields kicks to take the divergence out of the brain fields' inferior edges, so it uses half the brain field length. Both are arctangents. For a long spine that needs two posterior fields, the skin gap between them is set so the geometric edges meet at the anterior surface of the spinal cord: any overlap then falls anterior to the cord in the vertebral body, and the cord itself sits in the matched or slightly cold zone, not in the hot triangle.

**Formulas**

\[
\theta_{\text{coll}} = \arctan\left(\frac{L_{\text{spine}}/2}{\mathrm{SAD}}\right)
\qquad
\theta_{\text{couch}} = \arctan\left(\frac{L_{\text{brain}}/2}{\mathrm{SAD}}\right)
\]

- \(L_{\text{spine}}\): length of the posterior spine field at isocenter (cm)
- \(L_{\text{brain}}\): length of each lateral brain field at isocenter (cm)
- SAD: 100 cm; replace with SSD if the lengths are skin lengths of SSD fields

### Worked example

**Given.** Spine field 36 cm long at isocenter. Lateral brain fields 20 cm long. SAD 100 cm.

**Substitute.** \(\theta_{\text{coll}} = \arctan(18/100)\). \(\theta_{\text{couch}} = \arctan(10/100)\).

**Arithmetic.** \(\arctan(0.18) = 10.2^\circ\). \(\arctan(0.10) = 5.7^\circ\).

**Check.** \(\tan 10.2^\circ = 0.180\), \(\tan 5.7^\circ = 0.100\). Using the full spine length, \(\arctan(0.36) = 19.8^\circ\), doubles the collimator angle.

**Result means.** Rotate the brain-field collimators 10.2° so their inferior edges parallel the spine field's diverging superior edge, and kick the couch 5.7° so the brain fields' inferior edges stop diverging into the spine field. If the spine needs two fields, their gap is calculated to the anterior cord depth.

**Wrong turns**

- Collimator angle from the brain length or couch angle from the spine length.
- Full length in the arctan.
- Matching two spine fields at the skin or at the posterior cord, which puts the cord in the overlap.

**Traps.** Say which field's divergence each rotation removes. The collimator follows the spine field; the couch follows the brain field.

**Sources.** Khan and Gibbons, craniospinal matching; Bentel, CSI technique.

## Density Table and Fahrenheit Temperature Correction

**Objectives:** IV.3, I.10

**What the exam expects:** Two reference tables used inside calculations. The relative density table: lung about 0.25 to 0.33, fat about 0.92 to 0.95, water 1.00, muscle about 1.05, trabecular (soft) bone about 1.1 to 1.2, cortical bone about 1.65 to 1.85. The temperature-pressure correction for an open ion chamber, with the temperature possibly given in Fahrenheit: convert to Celsius first, then to kelvin, before forming the ratio against 22 °C and 760 mmHg.

**Formulas**

\[
T_{\text{C}} = \frac{5}{9}(T_{\text{F}} - 32)
\qquad
P_{TP} = \frac{273.2 + T_{\text{C}}}{273.2 + 22.0} \times \frac{760}{P}
\]

- \(T_{\text{F}}, T_{\text{C}}\): temperature in degrees Fahrenheit and Celsius
- \(P\): pressure in mmHg; 760 mmHg = 101.33 kPa
- \(P_{TP}\): factor that multiplies the raw reading

### Worked example

**Given.** The chamber is at 72 °F and 752 mmHg.

**Substitute.** \(T_{\text{C}} = (72 - 32) \times 5/9 = 40 \times 5/9 = 22.2\) °C. \(P_{TP} = (273.2 + 22.2)/(273.2 + 22.0) \times 760/752\).

**Arithmetic.** \(295.4/295.2 = 1.0007\). \(760/752 = 1.0106\). \(P_{TP} = 1.0007 \times 1.0106 = 1.011\).

**Check.** The room is almost exactly at reference temperature, so the correction is nearly all pressure: 8 mmHg below 760 is about 1.1% less air in the cavity, and the reading must go up by about 1.1%. Using 72 as if it were Celsius gives \(345.2/295.2 \times 1.0106 = 1.18\), an 18% error.

**Result means.** Multiply the raw reading by 1.011.

### Second pass: the density table

**Given.** A plan lists lung 0.30, fat 0.95, muscle 1.05, cortical bone 1.10.

**Reasoning.** Cortical bone at 1.10 is wrong; 1.1 is trabecular or soft bone. Cortical bone is 1.65 to 1.85. The other three are within their usual ranges. In an effective-depth sum (module 37) the slip would shorten 2 cm of cortical bone from about 3.7 cm water-equivalent to 2.2 cm.

**Wrong turns**

- Fahrenheit used directly in the kelvin sum.
- Pressure ratio inverted (P over 760).
- 1.1 assigned to cortical bone, or 0.3 assigned to fat.

**Traps.** Any temperature above 40 in a US stem is probably Fahrenheit. Convert before you add 273.2.

**Sources.** TG-51 for \(P_{TP}\) and the reference conditions; ICRU 44 tissue densities.

## Cord-Block Timing, Sector Areas, and Junction Shifts

**Objectives:** IV.3, III.7

**What the exam expects:** Six pieces of arithmetic that sit around blocks and junctions rather than inside a dose equation. (1) Count the fractions a cord can stay in the field before a block or an off-cord field is required. (2) Compute a sector area inside a Clarkson problem. (3) Count junction shifts and fractions per junction position, and find the largest shift the collimator allows. (4) Reduce a partly blocked field to an effective square. (5) Recognize an orthogonal image pair at non-cardinal angles. (6) Reject a calculation point that sits in a steep gradient.

**Cord-block timing.** Fractions allowed on cord equal the cord limit divided by the cord dose per fraction, rounded down. With 1.8 Gy per fraction, the cord on the 100 percent line, and a 45 Gy limit, \(45/1.8 = 25\) fractions fit exactly and the off-cord fields start at fraction 26. If the cord sits on the 105 percent line the cord dose per fraction is \(1.8 \times 1.05 = 1.89\) Gy, \(45/1.89 = 23.8\), and only 23 full fractions are allowed because 24 would give 45.4 Gy. In a 30-fraction course the remaining \(30 - 25 = 5\) fractions are delivered off-cord, often with an electron strip over the posterior neck. The bank uses the limit stated in the problem; QUANTEC's reference figure is about 50 Gy for a 0.2 percent myelopathy risk, and many departments plan to 45 Gy, so a question will always give its own number.

**Sector area.** A sector of angle \(\theta\) and radius \(r\) has area

\[
A = \frac{\theta}{360}\,\pi r^2
\qquad
\frac{10}{360} \times \pi \times 8.0^2 = 5.59 \text{ cm}^2
\]

Thirty-six such sectors rebuild the full circle of 201 cm², which is the check. In the Clarkson method itself the radius, not the area, drives the lookup: each sector contributes the circular-field scatter-air ratio for its radius weighted by \(\theta/360\), and the sum is the average scatter-air ratio for the irregular field. Arc length, \(\theta/360 \times 2\pi r\), is a length and is never the quantity asked for.

**Junction shifts.** Positions and shifts differ by one: three junction positions require two shifts. A 30-fraction course feathered over three equally weighted positions gives 10 fractions per position, and with 1 cm steps the last position is 2 cm from the first. The collimator sets the ceiling. If the spine field is 36 cm and the jaw opens to 40 cm, the field can grow 4 cm, so three positions allow at most \(4/2 = 2\) cm per step (36, 38, 40 cm). With 37 cm and 1.5 cm steps, \(3/1.5 = 2\) shifts fit (37, 38.5, 40 cm) and a third would need 41.5 cm. Shifting the junction superiorly lengthens the spine field and shortens the cranial field; shifting inferiorly does the reverse, so check which field is near its limit.

**Percent-blocked effective square.** When a fraction \(f\) of a square field of side \(s\) is blocked, the open area is \((1-f)s^2\) and the equal-area square has side

\[
s_{\text{eff}} = s\sqrt{1-f}
\qquad
10\sqrt{0.70} = 8.4 \text{ cm}
\]

Check: \(8.37^2 = 70\) cm², which is 70 percent of 100 cm². This is a phantom-scatter approximation for the TMR or PDD and \(S_p\) lookup; the collimator scatter factor \(S_c\) still follows the open jaw setting, and an irregular blocked shape is better handled by Clarkson. Multiplying the side by \(1-f\) shrinks the area to \((1-f)^2\), 49 percent here, and is the usual error.

**Orthogonal images.** Two projections are orthogonal when their gantry angles differ by 90 degrees in either direction around the circle. Zero and 90, 45 and 135, and 85 and 355 all qualify, because 355 to 85 is 90 degrees going through zero (355 is the same as minus 5). Opposed angles, 0 and 180, give the same projection and no information along the beam axis. The test is \(|\theta_1 - \theta_2|\) equal to 90 or 270.

**Calculation point near a block edge.** An independent MU check is meaningful only where a millimeter of positional uncertainty does not move the dose by more than the agreement tolerance. Isodose spacing of 10 percent per 2 mm near a block edge means 5 percent per millimeter, larger than the 2 to 3 percent expected of a check. TG-114 advises a point in a low-gradient region, well inside the open field and away from inhomogeneities and field edges, where central-axis or off-axis factors describe the dose.

**Common mistakes**

- Rounding 23.8 fractions up to 24 and crossing the cord limit.
- Applying a hot-spot percentage to the tolerance instead of to the fraction dose.
- Counting three shifts for three junction positions.
- Taking 10 percent of a circle for a 10 degree sector instead of 10/360.
- Scaling the field side by the unblocked fraction rather than by its square root.
- Calling 0 and 180 degrees orthogonal.

**Traps.** Cord-block questions sometimes give the total prescription and ask for off-cord fractions, sometimes give the cord percent and ask for on-cord fractions; write both counts down. For junction questions, always list the field lengths at every position and compare each to the collimator limit.

**Sources.** QUANTEC spinal cord summary for the 50 Gy reference; Khan and Gibbons for Clarkson integration and junction feathering; TG-114 for calculation-point selection.
