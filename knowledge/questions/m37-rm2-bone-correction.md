# Module 37. Corrections for Tissue Inhomogeneities and Density Overrides

Original items. Magnitude of the bone correction by energy, the electron-density ratio method, bone paired with the lung rule, and dose inside bone.

## Bone Corrections by Energy

### Q1
Stem: A 6 MV beam crosses 3.0 cm of cortical bone with a relative electron density of 1.65 before reaching a point. Using the rule of 3.5 percent per centimeter of extra water-equivalent path, about how does the dose at that point compare with a homogeneous water calculation?
A. About 10.5 percent lower
B. About 7 percent lower
C. About 17 percent lower
D. About 7 percent higher
Answer: B
Objective: IV.4
Why: The extra water-equivalent path is 3.0 × (1.65 − 1.00) = 1.95 cm, and 1.95 × 3.5 = 6.8, about 7 percent less dose beyond the bone. Check: the slab is 3.0 × 1.65 = 4.95 cm of water, which is 1.95 cm more than its physical thickness. Multiplying the full 3.0 cm by 3.5 percent gives 10.5 percent and forgets that bone is only 0.65 cm of extra water per centimeter. Using the whole 4.95 cm gives 17 percent and counts the slab's own thickness twice. A 7 percent increase treats bone like lung; bone attenuates more than water, so the dose beyond it falls.

### Q2
Stem: The same 2 cm slab of cortical bone lies in the path of four different photon beams. Beyond which beam is the percentage dose reduction per centimeter of bone the largest?
A. 18 MV
B. 10 MV
C. 6 MV
D. Cobalt-60
Answer: D
Objective: IV.4
Why: The bone correction is the extra water-equivalent path times the beam's attenuation per centimeter of water, and the less penetrating beam loses more per centimeter: with the bank's figures that is about 0.65 × 4.5 to 5 ≈ 3 percent per cm of bone at cobalt-60, about 0.65 × 3.5 ≈ 2.3 percent at 6 MV, and about 0.65 × 2 ≈ 1.3 percent at 18 MV. The 18 MV beam has the smallest correction, not the largest. Ten MV and 6 MV fall between the extremes.

### Q3
Stem: A CT density table lists cortical bone at a physical density of 1.85 g per cc, but a hand correction for a 6 MV beam uses a relative electron density of 1.65 instead. Why is the lower number correct for the megavoltage correction?
A. Compton interactions dominate at megavoltage energies and scale with electron density; bone has fewer electrons per gram than water, so its electron density relative to water is about 1.65 even though its mass density ratio is about 1.85
B. Bone's high atomic number makes photoelectric absorption dominate, and 1.65 is the photoelectric correction factor
C. Planning systems cannot store densities above 1.7
D. 1.65 is the density of spongy bone, which is what vertebral bodies contain
Answer: A
Objective: I.9
Why: Megavoltage attenuation in tissue is Compton attenuation, which depends on electrons per unit volume; bone's low hydrogen content gives it fewer electrons per gram than water, so the electron-density ratio is below the mass-density ratio. For a 2 cm slab, 1.85 adds 1.7 cm of water and 1.65 adds 1.3 cm, a 0.4 cm difference that at 3.5 percent per cm is a 1.4 percent overcorrection if the wrong ratio is used. Photoelectric absorption is an orthovoltage effect and is not described by either ratio. Planning systems store any density; the limit is fictional. Spongy bone is about 1.1, not 1.65.

### Q4
Stem: A 6 MV ray to a mediastinal point crosses 2.0 cm of cortical bone at relative electron density 1.65 and 4.0 cm of lung at density 0.25, with the rest soft tissue. Using 3.5 percent per centimeter of water-equivalent path change, how does the dose at the point compare with a homogeneous water calculation?
A. About 10.5 percent higher
B. About 4.5 percent lower
C. About 6 percent higher
D. About 6 percent lower
Answer: C
Objective: IV.4
Why: Bone adds 2.0 × 0.65 = 1.3 cm of water and lung removes 4.0 × 0.75 = 3.0 cm, so the ray is net 1.7 cm shorter in water-equivalent terms and the point receives about 1.7 × 3.5 = 5.95, roughly 6 percent, more dose. Check: 1.3 − 3.0 = −1.7 cm. Ignoring the bone gives 3.0 × 3.5 = 10.5 percent, too high. Counting only the bone gives 1.3 × 3.5 ≈ 4.5 percent lower and forgets the lung. Six percent lower has the right magnitude but the wrong sign; the lung wins on this ray.

### Q5
Stem: A 6 MV beam passes through a vertebral body. Compared with soft tissue at the same depth, how does the absorbed dose within the bone mineral itself compare, and how does that compare with an orthovoltage beam?
A. Much higher at 6 MV because of photoelectric absorption, and about equal at orthovoltage
B. Identical at both energies because dose is defined per unit mass
C. Higher at 6 MV because bone is denser than soft tissue
D. Slightly lower at 6 MV, because Compton dose per gram follows electrons per gram and bone has fewer; several times higher at orthovoltage, where photoelectric absorption in calcium dominates
Answer: D
Objective: IV.4
Why: At megavoltage energies the dose to bone mineral is about 0.96 of the dose to water at the same point because the Compton energy absorbed per gram scales with electrons per gram, while the soft tissue inside the bone receives a few percent extra from electrons set in motion in the mineral. At orthovoltage energies the photoelectric cross-section of calcium raises the bone dose to several times the soft-tissue dose, which is the historical reason kilovoltage therapy was limited near bone. Photoelectric dominance is the orthovoltage behavior, not the megavoltage one. Density alone does not raise dose per gram.
