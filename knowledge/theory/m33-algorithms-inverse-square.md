# Module 33. External beam dose calculation and algorithms

Original notes for MDCB CMD prep (2023 job task analysis). Domain IV, dose calculation methods, is about 13% of the exam.

These lessons use one distance convention on purpose. In the inverse-square work, \(d_1\) and \(d_2\) are distances from the **source** to the point, in centimetres. Depth in tissue is a different quantity and is named when it appears.

## Dose Calculation and Algorithms

**Objectives:** IV.1, IV.6

**What the exam expects:** Name the algorithm family from a short description. Clarkson separates primary and scatter. Pencil beam has weak lateral scatter and is poor in lung. Convolution/superposition (including collapsed cone) moves energy sideways and handles lung better. AAA is an analytical kernel model, stronger than a plain pencil beam and weaker than a transport solution at a hard interface. A grid-based Boltzmann solver (Acuros) and Monte Carlo both transport radiation through heterogeneities. Monte Carlo is the method that best handles interface dose. A coarse dose grid misses a narrow maximum in a serial organ.

### Families

**Correction-based.** Start from measured water data (PDD or TMR, output factors) and multiply corrections: inverse square, Mayneord F, wedge, tray, equivalent square, a heterogeneity ratio. The arithmetic is transparent. There is no electron transport, so lateral scatter and interfaces are only as good as the correction you remembered to apply.

**Clarkson.** Built for irregular fields (blocks, mantles). The tissue-air ratio is split into a primary part and a scatter part:

\[
\mathrm{TAR}(d, r_d) = \mathrm{TAR}(d, 0) + \mathrm{SAR}(d, r_d)
\]

- \(\mathrm{TAR}(d, r_d)\): tissue-air ratio at depth \(d\) for field radius \(r_d\)
- \(\mathrm{TAR}(d, 0)\): zero-area TAR, the primary (no scatter) term
- \(\mathrm{SAR}\): scatter-air ratio, \(\mathrm{TAR}(d, r_d) - \mathrm{TAR}(d, 0)\)

For an irregular outline, the field is cut into angular sectors. Each sector contributes scatter in proportion to its angle:

\[
\mathrm{SAR}_{\text{field}} = \sum_i \mathrm{SAR}(d, r_i)\,\frac{\Delta\theta_i}{2\pi}
\]

- \(r_i\): radius of sector \(i\) out to the field edge
- \(\Delta\theta_i\): sector angle in radians
- \(2\pi\): full circle, so \(\Delta\theta_i / 2\pi\) is the fraction of the circle

Primary and scatter are computed apart, then added. That separation is the fact the item is testing. Clarkson is not a 3D heterogeneity transport model.

**Pencil beam.** The broad beam is a stack of narrow pencils. Heterogeneity is applied mainly along each pencil. Lateral scatter is weak: energy does not move far enough sideways, so the model is poor in lung and at tissue interfaces. It can still look acceptable in a large field of homogeneous water.

**Convolution / superposition, and collapsed cone.** Total energy released in the patient is convolved with a scatter kernel. Superposition stretches that kernel when the density changes, so lateral scatter in lung is much better than with a pencil beam. Collapsed cone is a fast superposition: scatter is transported along a finite set of cone axes. The same limit remains at a sharp interface or inside metal. The kernel is an approximation, not a particle history.

**AAA (anisotropic analytical algorithm).** A clinical analytical model (Varian) with lateral scatter kernels. It is better in lung than a pure pencil beam. It is still an analytical model, so small fields and hard heterogeneities are weaker than Monte Carlo or a Boltzmann solver.

**Grid-based Boltzmann solvers (Acuros).** The linear Boltzmann transport equation is solved on a grid for photons and electrons. Acuros XB is the name items use. Results sit close to Monte Carlo in lung and bone when the material assigned to the voxel is the right material. A wrong density override defeats the transport.

**Monte Carlo.** Particles are followed with random interactions. Of the methods above, Monte Carlo is the one that best handles interface dose: buildup, backscatter from bone or metal, and the lung–soft-tissue boundary. The conditions are enough histories (otherwise the dose is noisy) and the correct material. Speed is a workflow issue, not a reason to accept a pencil beam through lung.

Order to remember when the question is interface dose: Monte Carlo, then a grid-based Boltzmann solver or a good superposition, then AAA, then pencil beam.

**Dose grid.** Dose is stored at voxel centers (or as an average over the voxel, depending on the system). A coarse matrix can step over a narrow peak. Serial organs (cord, optic nerve, brainstem) are judged on a small maximum, so a 4–5 mm grid can report a maximum several gray below the true peak. Stereotactic plans and serial-organ maxima need a fine grid, commonly 1–2 mm. The DVH inherits the miss: a DVH cannot prove that the grid resolved the hot spot, and it cannot show where the hot spot sits.

### Worked example: Clarkson primary and scatter

**Given.** At the depth of interest, \(\mathrm{TAR}(d, 0) = 0.400\). The irregular field is two half-fields: one 180° sector of radius 5 cm with \(\mathrm{SAR} = 0.200\), and one 180° sector of radius 10 cm with \(\mathrm{SAR} = 0.280\).

**Formula.** \(\mathrm{SAR}_{\text{field}} = \sum \mathrm{SAR}(d, r_i)\,(\Delta\theta_i / 2\pi)\), then \(\mathrm{TAR} = \mathrm{TAR}(d, 0) + \mathrm{SAR}_{\text{field}}\).

**Symbols.** Defined above. Each half-field has \(\Delta\theta / 2\pi = \pi / 2\pi = 0.5\).

**Substitute.**

\[
\mathrm{SAR}_{\text{field}} = 0.5(0.200) + 0.5(0.280) = 0.100 + 0.140 = 0.240
\]

\[
\mathrm{TAR} = 0.400 + 0.240 = 0.640
\]

**Check.** \(0.100 + 0.140 = 0.240\). \(0.400 + 0.240 = 0.640\). Removing either sector drops the SAR by that sector’s weighted term only (0.100 or 0.140), which is the point of keeping primary and scatter apart.

**Result means.** The irregular field has TAR 0.640. Of that, 0.400 is primary and 0.240 is scatter. A correction that only scales area does not do this split.

### Worked example: coarse grid and a serial-organ maximum

**Given.** Dose sampled every 2 mm along the cord: 48.0, 51.0, 54.2, 50.5, 47.0 Gy. A 6 mm grid keeps only the first and fourth of those samples (48.0 Gy and 50.5 Gy).

**Arithmetic.** True maximum = 54.2 Gy. Reported maximum = 50.5 Gy. Missed peak = \(54.2 - 50.5 = 3.7\) Gy.

**Check.** \(50.5 + 3.7 = 54.2\).

**Result means.** The plan report says 50.5 Gy. The cord peak is 54.2 Gy. A 50 Gy serial-organ limit can look met on the coarse grid and be exceeded on the fine grid. Module 39 uses this same sampling fact as an uncertainty source.

**Wrong turns**

- Calling pencil beam “fine in lung because the path length was corrected.” Longitudinal correction without lateral scatter is still a pencil beam.
- Swapping Clarkson’s split: SAR is scatter, zero-area TAR is primary.
- Treating AAA or collapsed cone as equivalent to Monte Carlo at a metal–tissue interface.
- Reading a DVH maximum as if grid size were irrelevant.
- Using percent of field area blocked as a stand-in for Clarkson scatter.

**Traps.** Items often describe the algorithm instead of naming it. “Primary and scatter calculated separately, then added” is Clarkson. “Weak lateral scatter, fails in lung” is pencil beam. “Best at interfaces” is Monte Carlo.

**Sources.** Khan and Gibbons, *The Physics of Radiation Therapy* (Clarkson, TAR/SAR). AAPM TG-105 (Monte Carlo in treatment planning). Vendor technical references for AAA and Acuros XB as implementations of the analytical and Boltzmann families above.

## External beam Dose Calculation and Algorithms Quiz

**Skills this quiz checks**

- Match a one-sentence description to correction-based, Clarkson, pencil beam, convolution/superposition or collapsed cone, AAA, Acuros-type Boltzmann, or Monte Carlo.
- State that Monte Carlo handles interface dose best, and that pencil beam is the weak lung model.
- State that Clarkson’s zero-area term is primary and the rest is scatter.
- Explain, with the 3.7 Gy sampling example in mind, why a coarse grid under-reports a narrow serial-organ maximum.
- Reject area-percent blocking as a full scatter correction.

## Inverse Square Tutorial

**Objectives:** I.10, IV.1

**What the exam expects:** Apply inverse square to dose rate (or dose, for a fixed time) when the stem says distance is the only change. Write \(I_1/I_2 = (d_2/d_1)^2\) and solve it in the direction the question asks. The distances are source-to-point distances.

**Formula**

\[
\frac{I_1}{I_2} = \left(\frac{d_2}{d_1}\right)^2
\qquad
I_2 = I_1\left(\frac{d_1}{d_2}\right)^2
\]

- \(I_1\): dose rate (or dose, same irradiation time) at distance \(d_1\)
- \(I_2\): dose rate at distance \(d_2\)
- \(d_1, d_2\): distances from the source, same unit in both places

Attenuation, scatter, and beam modifiers are outside this formula. “Inverse square only” means they are ignored.

### Worked example: dose rate and SAD

**Given.** A unit delivers 400 cGy/min at SAD = 100 cm (the isocenter, 100 cm from the source). Find the dose rate 125 cm from the source. Inverse square only.

**Formula.** \(I_2 = I_1 (d_1/d_2)^2\), with \(I_1 = 400\) cGy/min, \(d_1 = 100\) cm, \(d_2 = 125\) cm.

**Substitute.**

\[
I_2 = 400 \left(\frac{100}{125}\right)^2 = 400 (0.800)^2 = 400 \times 0.640
\]

**Arithmetic.** \(400 \times 0.640 = 256\) cGy/min.

**Check.** The intensity ratio must equal \((d_2/d_1)^2 = (125/100)^2 = 1.5625\). Then \(400 / 1.5625 = 256\). And \(256 \times (125/100)^2 = 256 \times 1.5625 = 400\), which returns the original rate.

**Result means.** Moving from 100 cm to 125 cm drops the dose rate from 400 cGy/min to 256 cGy/min, 64% of the isocenter rate, because \(0.800^2 = 0.640\). The same factor applies to dose if the beam-on time is unchanged.

**Wrong turns**

- Using the ratio once and not squaring it: \(400 \times (100/125) = 320\) cGy/min.
- Inverting the distances: \(400 \times (125/100)^2 = 625\) cGy/min, which is the rate at 80 cm, not at 125 cm.
- Using SSD where the stem gave source-to-point distance, or using depth as \(d\).
- Applying Mayneord F. Mayneord adjusts a percent depth dose between two SSDs. It is an inverse-square correction inside PDD, not the dose-rate-versus-distance problem.
- Changing minutes and distance in the same step without deciding which quantity is \(I\).

**Traps.** SAD is already a source distance. SSD is a source-to-skin distance. A point at depth \(d\) under an SSD setup sits at source distance \(\mathrm{SSD} + d\).

**Sources.** Khan and Gibbons, inverse-square chapter; the MDCB formula list uses the same ratio.

## Inverse Square Calculations

**Objectives:** I.10, IV.1

**What the exam expects:** Compute dose or dose rate at a new source distance, including the case where the stem gives SSD and depth separately so you must add them before squaring.

### Worked example: SSD plus depth is the source distance

**Given.** Dose rate at isocenter (100 cm from the source) is 300 cGy/min. A calculation point has SSD = 80 cm and depth = 10 cm. Inverse square only.

**Formula.** \(I_2 = I_1 (d_1/d_2)^2\).

**Symbols.** \(I_1 = 300\) cGy/min at \(d_1 = 100\) cm. The new source-to-point distance is \(d_2 = \mathrm{SSD} + \text{depth} = 80 + 10 = 90\) cm. Depth alone is not \(d_2\).

**Substitute.**

\[
I_2 = 300 \left(\frac{100}{90}\right)^2 = 300 \left(\frac{10}{9}\right)^2 = 300 \times \frac{100}{81}
\]

**Arithmetic.** \(30000 / 81 = 370.37\) cGy/min. ( \(81 \times 370 = 29970\), remainder 30, and \(30/81 = 0.370\). )

**Check.** \(370.37 \times (90/100)^2 = 370.37 \times 0.81 = 300.0\) cGy/min.

**Result means.** The point is 90 cm from the source, closer than isocenter, so the rate rises from 300 to 370.37 cGy/min. Using 80 cm as the distance would answer a skin point, not the point at 10 cm depth.

### Second pass: dose at a shorter SAD, fixed time

**Given.** 200 cGy is delivered at 100 cm from the source. The same beam-on time is used at 80 cm. Inverse square only.

**Substitute.** \(D_2 = 200 \times (100/80)^2 = 200 \times 1.5625\).

**Arithmetic.** \(200 \times 1.5 = 300\), and \(200 \times 0.0625 = 12.5\), so \(D_2 = 312.5\) cGy.

**Check.** \(312.5 \times (80/100)^2 = 312.5 \times 0.64 = 200\).

**Result means.** For a fixed time, dose tracks dose rate. At 80 cm the dose is 312.5 cGy.

**Wrong turns**

- Stopping at SSD = 80 cm and computing \(300 \times (100/80)^2 = 468.75\) cGy/min for a point that is actually at 90 cm.
- Solving for distance with the square still on: from \(I_1/I_2 = (d_2/d_1)^2\), take the square root before finding \(d\).
- Mixing cGy and Gy (factor of 100) after a correct ratio.
- Half-life or mean life. Nothing in this lesson decays.

**Traps.** Write the two source distances on the page before you square. Label which distance belongs to the known dose rate.

**Sources.** Khan and Gibbons, inverse square applied to SSD geometry.

## Inverse Square Quiz (Beginner)

**Skills this quiz checks**

- Write \(I_1/I_2 = (d_2/d_1)^2\) and name \(d\) as source distance.
- Compute a farther rate (the 100 cm → 125 cm pattern, answer smaller) and a nearer rate (answer larger).
- Square the ratio. The unsquared ratio is the usual wrong choice.
- Keep the unit you were given (cGy/min stays cGy/min).

## Inverse Square Quiz (Advanced)

**Skills this quiz checks**

- Build source distance as SSD + depth before using inverse square.
- Solve the formula for an unknown distance (square root), not only for an unknown dose rate.
- Keep Mayneord F out of a pure dose-rate question. Mayneord changes PDD between two SSDs and does not replace scatter.
- Reverse-check: multiply the new dose rate by the squared distance ratio and recover the original rate.

## Solving Inverse Square for Distance and Time

**Objectives:** I.10, IV.1

**What the exam expects:** Two turns of the same inverse-square ratio that the drills above do not ask. First, the unknown is the distance: a hemibody or total-body protocol caps the dose rate, and you must find how far from the source the midplane has to sit. Second, the unknown is an accumulated exposure: a survey reading is a rate (mR per hour), so after inverse square you still multiply by the time spent, in hours, to get a dose in mR.

**Formulas**

\[
d_2 = d_1 \sqrt{\frac{I_1}{I_2}}
\qquad
X = \dot{X}_1 \left(\frac{d_1}{d_2}\right)^2 \times t
\]

- \(I_1\): known dose rate at distance \(d_1\) from the source
- \(I_2\): the dose rate you are allowed (or want) at the unknown distance \(d_2\)
- \(\dot{X}_1\): exposure rate at \(d_1\), in mR/h
- \(t\): time at \(d_2\), in hours when the rate is per hour
- \(X\): accumulated exposure in mR

The square root is the step people drop. A rate that must fall by a factor of 4 needs twice the distance, not four times.

### Worked example: distance for a dose-rate cap

**Given.** A linac delivers 300 cGy/min at 100 cm from the source. A hemibody protocol requires no more than 80 cGy/min at the midplane. Inverse square only.

**Substitute.** \(d_2 = 100 \sqrt{300/80} = 100 \sqrt{3.75}\).

**Arithmetic.** \(\sqrt{3.75} = 1.9365\). \(d_2 = 193.6\) cm.

**Check.** \(300 \times (100/193.6)^2 = 300 \times 0.2667 = 80.0\) cGy/min. Without the root, \(100 \times 3.75 = 375\) cm would drop the rate to \(300/3.75^2 = 21\) cGy/min, far below the cap.

**Result means.** The midplane must be at least 193.6 cm from the source. Any longer distance is also under the cap; the question asks for the shortest acceptable distance. Attenuation and the lower dose rate that a TBI mode may offer are separate adjustments.

### Second pass: exposure rate times time

**Given.** A survey meter reads 60 mR/h at 1.5 m from an implanted patient. A nurse spends 20 minutes at 3 m. Inverse square only.

**Substitute.** Rate at 3 m \(= 60 \times (1.5/3)^2 = 60 \times 0.25 = 15\) mR/h. Time \(= 20/60 = 0.333\) h.

**Arithmetic.** \(X = 15 \times 0.333 = 5.0\) mR.

**Check.** 15 mR in a full hour, so 5 mR in a third of an hour. Leaving the time in minutes, \(15 \times 20 = 300\), is the usual slip and is 60 times too large.

**Result means.** The nurse accumulates about 5 mR. Convert minutes to hours before multiplying a per-hour rate.

**Wrong turns**

- Solving for distance without the square root.
- Inverting the ratio under the root, which moves the point closer when the rate must fall.
- Multiplying a per-hour rate by minutes.
- Applying inverse square to the time instead of the rate.

**Traps.** Underline the unit of the rate. Then write the two distances and decide which one is unknown before touching the square or the root.

**Sources.** Khan and Gibbons, inverse square; TBI and hemibody dose-rate practice as described in AAPM Report 17 and the TBI technique lesson in module 24.

## Spatially Invariant Kernels

**Objectives:** IV.1

**What the exam expects:** Name the assumption that separates convolution from superposition. A convolution algorithm uses one scatter kernel for every point, so the kernel is spatially invariant. That is only true in a homogeneous water-like patient. Superposition lets the kernel change from point to point by scaling it with the density along each ray (radiological distance), which is why it handles lung and bone better. Collapsed cone is a fast superposition that transports along a fixed set of cone axes.

The kernel itself is the dose spread around a single primary interaction site. It is precomputed by Monte Carlo and stored. The quantity it spreads is TERMA, the total energy released per unit mass by the primary photons (module 35 ties TERMA to the primary and scatter split of a TMR).

### Worked example: which model is in use

**Given.** A planner reads a vendor description: “the same dose-spread array is applied at every voxel, and heterogeneities are handled only by changing the path length to each voxel.”

**Reasoning.** One array everywhere is a spatially invariant kernel, so the engine is a convolution. Changing the path length alters where TERMA is deposited, but the kernel is not rescaled by local density, so lateral scatter in lung is still modeled as if it were water.

**Check.** If the description had said “the kernel is scaled by the density between the interaction site and the dose point,” that would be superposition.

**Result means.** A pure convolution engine is a homogeneous-patient model with a path-length patch. Expect it to overestimate dose inside and just beyond low-density lung for small fields.

**Wrong turns**

- Calling superposition “a convolution with a density override.” The difference is whether the kernel is rescaled, not whether densities are read.
- Saying the kernel is measured. It is calculated by Monte Carlo.
- Confusing TERMA with KERMA. KERMA is energy transferred to charged particles only; TERMA also includes the energy carried off by scattered photons.

**Traps.** “Spatially invariant” is a property of the kernel, not of the dose grid or the beam.

**Sources.** Ahnesjö and Aspradakis, dose calculations for external photon beams (Phys Med Biol 1999); Khan and Gibbons, convolution–superposition.
