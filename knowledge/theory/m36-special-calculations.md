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
