# Module 9. Radiation Measurement

Original notes for MDCB objectives I.10 and the dose-ratio portion of dose calculation. TAR, TMR, TPR, PDD, BSF, Sc, and Sp are different ratios. They are not renamed copies of one curve.

## KERMA vs. Absorbed Dose

**MDCB:** I.10, I.4

**What the exam expects**

You define kerma and absorbed dose and you describe how the two curves sit in a megavoltage phantom. Kerma is maximum at the surface and falls with depth. Dose is low at the surface, rises through buildup to dmax, then falls. You know when dose equals collision kerma (charged-particle equilibrium) and why that equality fails in the buildup region and at a tissue–lung edge.

**Core facts**

Kerma is the kinetic energy transferred to charged particles per unit mass. It is a photon (or neutron) event score. The energy has been handed to electrons. It has not necessarily been absorbed yet. Those electrons travel.

Collision kerma excludes energy the charged particles later lose as bremsstrahlung. Absorbed dose tracks collision kerma when the electrons that start in a small mass are matched by electrons that stop there. That condition is charged-particle equilibrium.

Absorbed dose is the energy imparted per unit mass. It is what the prescription states. Unit gray, or cGy. Dose includes whatever the charged particles actually deposit in that mass, regardless of where they were set in motion.

In a megavoltage photon beam entering water:

- Primary photon fluence, and therefore kerma, is highest at the surface and decreases with depth because of attenuation and inverse square.
- Electrons are set in motion mostly in the forward direction. At the surface there are few electrons arriving from upstream. Dose is low. This is skin sparing.
- Dose rises over a depth comparable to the electron range until transient equilibrium. That depth is dmax. Approximate values: Co-60 about 0.5 cm, 6 MV about 1.5 cm, 10 MV about 2.5 cm, 18 MV about 3.5 cm. Confirm for the machine in Khan.
- Beyond dmax, dose and collision kerma both fall. Dose at a point matches collision kerma a short distance upstream, by about the electron range. The dose curve is the kerma curve shifted downstream.

Buildup is not attenuation. Attenuation would make the surface dose the highest. The surface dose is low because the electrons have not arrived yet. Bolus, a tray, obliquity, and couch material fill that buildup region with electrons or with scattering material and raise skin dose.

Electronic disequilibrium returns at a lung interface and in a small high-energy field. Electrons leave a small mass and are not replaced. Collision kerma can stay high while dose falls. An equivalent-path correction does not model that. It is why lung dose at 15 MV in a small field is not a simple density scaling.

Exposure is ionization in air, not kerma and not dose. Under equilibrium, exposure, air kerma, and dose to air are convertible. The conversion is in the units module (about 0.876 rad in air per roentgen).

**Formulas**

K = Ψ (μ_tr / ρ)

K_c = Ψ (μ_en / ρ)

- K: kerma
- K_c: collision kerma
- Ψ: photon energy fluence
- μ_tr/ρ: mass energy-transfer coefficient
- μ_en/ρ: mass energy-absorption coefficient

Under charged-particle equilibrium, absorbed dose equals collision kerma. In the buildup region that equality does not hold.

**Traps**

Kerma and dose drawn as the same curve from the surface. Dose described as maximum at the surface for 6 MV. Buildup described as the filter “absorbing” the beam so less dose arrives at the skin. Equilibrium assumed inside lung for a 3×3 cm 15 MV field.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.10 and I.4.

## Radiation Measurement

**MDCB:** I.10, VII.3

**What the exam expects**

You know what an ion chamber measures, why a buildup cap exists, and how to correct an unsealed chamber for temperature and pressure. You can name the other detectors only well enough to say what they are for. Full QA tolerances are a later domain. This lesson is the measurement physics those tolerances assume.

**Core facts**

Exposure is charge liberated per mass of air. The standard is a free-air chamber. A practical thimble chamber is calibrated against that chain and, under TG-51, carries an absorbed-dose-to-water factor N_D,w.

Bragg–Gray cavity theory: dose to the medium equals dose to the gas in a small cavity times the ratio of mass collision stopping powers (medium to gas), with perturbation factors because real cavities are not ideal. You will not be asked to evaluate the Spencer–Attix integral. You will be asked why the chamber wall and the gas matter, and why an electron beam uses a parallel-plate chamber.

TG-51 gives absorbed dose to water from a corrected chamber reading, N_D,w, and a quality conversion k_Q. Photon quality is TPR20,10. Electron quality is R50. Confirm the factor list in TG-51 rather than reconstructing the protocol from memory. The exam point here is that the linac’s monitor unit becomes a gray only after this calibration, under a stated field size, depth, and SSD or SAD.

Ptp corrects an unsealed chamber because the mass of air in the cavity changes. Reference conditions in TG-51 are 22°C and 101.33 kPa (760 mmHg). If the room is warmer, or the pressure is lower, fewer molecules are in the cavity, the reading is low, and Ptp is greater than 1.

Pion corrects for ions that recombine before they are collected. It is larger when the dose per pulse is large. Ppol corrects for a reading that changes when the bias polarity is flipped. These are not weather corrections.

A buildup cap, or a miniphantom, puts the chamber at equilibrium when you measure in air (collimator scatter, exposure). The cap thickness is about dmax. The cap must be fully covered by the field or the reading is not the in-air quantity you think it is.

Other detectors, at the level this module needs:

- Farmer (thimble) chamber: photon calibration in water.
- Parallel-plate chamber: electrons and surface dose, where a cylindrical cavity perturbs the gradient.
- Diode: real-time, small, angle and energy dependent. Not a substitute for a calibrated chamber when you are defining output.
- TLD and OSLD: integrating, small, read after the irradiation.
- Radiochromic film: two-dimensional relative dose.
- Geiger counter: sensitive, saturates and loses counts in a pulsed linac beam. It is not the instrument for linac output.
- Ion-chamber survey meter: dose rate around a source or a patient, if it is designed for that rate.

The f-factor converts roentgen to rad in a medium under equilibrium: about 0.876 rad/R in air, and near 0.97 rad/R in muscle in the Compton range. Bone at orthovoltage is several times higher because of the photoelectric effect. Confirm a table value in Khan before using a specific bone f-factor.

**Formulas**

Ptp = [(273.2 + T) / (273.2 + T0)] × (P0 / P)

- T: local temperature in °C
- T0: 22°C for TG-51
- P: local pressure
- P0: 760 mmHg if P is in mmHg
- The first ratio uses kelvin. The second ratio is reference pressure over local pressure.

If T > T0 or P < P0, then Ptp > 1.

**Worked example**

Given: an unsealed chamber is used at 24.0°C and 750 mmHg. TG-51 reference is 22.0°C and 760 mmHg. Find Ptp.

Formula: Ptp = [(273.2 + T) / (273.2 + 22)] × (760 / P)

Substitution: T = 24.0. P = 750. Ptp = (297.2 / 295.2) × (760 / 750)

Arithmetic: 297.2 / 295.2 = 1.0068. 760/750 = 1.0133. Product = 1.0068 × 1.0133 = 1.020.

Meaning: the raw reading is about 2% low. Multiply the reading by 1.020 before applying N_D,w. Ignoring Ptp understates dose by that 2%.

Usual wrong turn: (273.2 + 22) / (273.2 + 24) × (750/760) = 0.980, which inverts both ratios and “corrects” in the wrong direction, making a low reading lower. Or using 24/22 = 1.09 as if the Celsius numbers were absolute temperature. A 2°C error is about 2/295, under 1%, not 9%.

**Traps**

Ptp applied to a sealed linac monitor chamber that has already defined the MU. Buildup cap left off an in-air measurement at 6 MV, so the chamber is still in buildup and the reading is not “dose in free space.” Geiger counter used to measure linac output. f-factor for bone at 250 kV reused at 6 MV.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-51 for reference conditions, N_D,w, and k_Q. Public blueprint I.10.

## TAR, TPR, TMR and More

**MDCB:** I.10, IV.1

**What the exam expects**

You define each ratio, you state what is held constant, and you know which ones depend on SSD. You can convert TAR to TMR with the backscatter factor, and Sc,p to Sp with Sc. You know Mayneord’s factor is an inverse-square correction only.

**Core facts**

Percent depth dose, PDD. Dose at depth d on the central axis, divided by dose at dmax, times 100, for a fixed SSD. The field size is stated at the surface. PDD rises with energy, with field size (more phantom scatter), and with SSD. PDD falls with depth. Because the definition fixes SSD, a 100 cm PDD table is the wrong table for an 80 cm SSD setup unless you correct it.

PDD(d) = 100 × D(d) / D(dmax), same SSD, same field.

Tissue-air ratio, TAR. Dose at depth d in a phantom, divided by the dose in free space at the same point, for the same field size measured at that depth. The source-to-point distance is the same in both measurements, so inverse square cancels. TAR does not depend on SSD. It was the workhorse for Co-60 isocentric treatments. TAR at dmax is the backscatter factor.

Backscatter factor, BSF. Also called the peak scatter factor when dmax is not on the surface. Dose at dmax in the phantom divided by dose at the same point in free space (buildup cap, same collimator opening). BSF increases with field size. The increase is large at orthovoltage, modest at Co-60, and close to 1 at high megavoltage because scatter is forward and the “back” scatter is small. BSF = TAR(dmax). BSF is not TMR. TMR at dmax is 1 by definition.

Tissue-maximum ratio, TMR. Dose at depth d divided by dose at dmax, same field size at the point of interest, same source-to-point distance. TMR does not depend on SSD. TMR(dmax) = 1. TMR(d) = TAR(d) / BSF = TAR(d) / TAR(dmax). SAD monitor-unit calculations use TMR (or TPR) because the isocenter stays put and the surface moves.

Tissue-phantom ratio, TPR. The same idea as TMR, except the reference depth is a chosen depth d_ref, not necessarily dmax. TMR is the special case d_ref = dmax. TG-51’s photon quality index is a TPR: dose at 20 cm over dose at 10 cm, 10×10 cm², which is TPR20,10. Confirm the exact setup in TG-51.

Scatter-air ratio, SAR. TAR(d, r) − TAR(d, 0). The zero-area TAR is primary only. SAR is the scatter part. Clarkson integration, a later calculation, uses SAR so an irregular field can be built from sectors. Knowing the definition now keeps Clarkson from looking like a new kind of PDD.

Collimator scatter factor, Sc. Also called the in-air output ratio. Reading in air (buildup cap or miniphantom) for a collimator setting, divided by the same reading for the reference collimator, usually 10×10 cm², at the same distance. Sc accounts for head scatter, including how much of the flattening filter the jaws expose. Sc does not include phantom scatter. A custom block downstream of the jaws does not change the jaw setting, so it does not change Sc the way opening the jaws does. AAPM TG-74 is the measurement reference for Sc. TG-71 is the monitor-unit reference.

Phantom scatter factor, Sp. The change in dose at the reference depth that comes from phantom scatter alone. In practice Sp(r) = Sc,p(r) / Sc(r). The field size that enters Sp is the field size incident on the phantom (blocked field), not the jaw setting, when those differ.

Total scatter factor, Sc,p. Dose at the reference depth in phantom for field r, divided by dose at the same depth for the reference field, same SSD. Sc,p = Sc × Sp. This is the “output factor” people mean when they say the 20×20 puts out more per MU than the 10×10. Part of that increase is the head (Sc). Part is the phantom (Sp).

Mayneord F converts PDD from one SSD to another using inverse square only. It does not correct the change in scatter. When SSD increases, F is slightly above 1 at depth and the corrected PDD is a little high compared with measurement. The exam statement: Mayneord is an inverse-square correction only.

Which field size goes where, the usual miss:

- PDD: field size at the surface.
- TAR, TMR, TPR: field size at the depth of the point.
- Sc: collimator setting, projected to the isocenter.
- Sp: blocked field on the patient.

Percent of the field area that is blocked is not Sp. Scatter is not linear with area. Equivalent square, 2ab/(a+b) for a rectangle, is a later module. Do not invent Sp by multiplying the open-field Sp by the percent open area.

**Formulas**

PDD(d, r, SSD) = 100 × D_d / D_dmax

TAR(d, r_d) = D_d / D_free space

BSF(r) = TAR(dmax, r)

TMR(d, r_d) = D_d / D_dmax = TAR(d, r_d) / BSF

TPR(d, d_ref, r_d) = D_d / D_dref

Sc,p(r) = Sc(r) × Sp(r)

Sp(r) = Sc,p(r) / Sc(r)

Mayneord:

F = [(SSD2 + dmax) / (SSD1 + dmax)]^2 × [(SSD1 + d) / (SSD2 + d)]^2

PDD2 = PDD1 × F

- d: depth of the point
- dmax: depth of maximum dose
- SSD1, SSD2: the two source-to-surface distances
- r: field size at the surface for PDD
- r_d: field size at depth for TAR, TMR, TPR
- F: Mayneord factor, inverse square only

**Worked example**

Three separate substitutions. They are not one patient.

1. PDD. Given D(dmax) = 180 cGy and D(10 cm) = 120 cGy at the same SSD. PDD = 100 × 120/180 = 66.7%.

2. TAR to TMR. Given TAR(10 cm, 10×10) = 0.712 and BSF = TAR(dmax) = 1.036. TMR = 0.712 / 1.036 = 0.687. TMR is less than TAR because the denominator of TMR is the phantom dose at dmax, which includes backscatter, while the denominator of TAR is free-space dose.

3. Scatter factors. Given Sc,p(15×15) = 1.041 and Sc(15×15) = 1.018. Sp = 1.041 / 1.018 = 1.023. Check: 1.018 × 1.023 = 1.041.

4. Mayneord. Given 6 MV, dmax = 1.5 cm, d = 10 cm, SSD1 = 100 cm, SSD2 = 110 cm, PDD1 = 67.0%.

F = [(110 + 1.5)/(100 + 1.5)]^2 × [(100 + 10)/(110 + 10)]^2
= (111.5/101.5)^2 × (110/120)^2

111.5/101.5 = 1.0985, squared = 1.207.
110/120 = 0.9167, squared = 0.8403.
F = 1.207 × 0.8403 = 1.014.

PDD2 = 67.0 × 1.014 = 67.9%.

Meaning: moving from 100 to 110 cm SSD raises the 10 cm PDD by about one percentage point, from inverse square alone. TMR for the same energy and field does not get this correction. TMR was built so SSD would cancel. Applying Mayneord to a TMR is a double correction.

Usual wrong turn: TMR = TAR × BSF = 0.712 × 1.036 = 0.738, multiplying instead of dividing. Or Sp = Sc,p × Sc = 1.060, which is greater than the total scatter and cannot be a factor inside it. Or Mayneord with the depth term inverted, [(SSD2 + d)/(SSD1 + d)]^2, which for this problem gives (120/110)^2 in the second term and F below 1, so the PDD falls when SSD rises. PDD at depth rises slightly when SSD rises.

**Traps**

PDD treated as independent of SSD. TMR treated as dependent on SSD. BSF set equal to TMR(dmax); TMR(dmax) is 1 and BSF is TAR(dmax), which is a few percent above 1 at Co-60. Sc measured in a big water phantom; that measurement is Sc,p if it is at dmax in full scatter. Zero-area field and blocked field treated as the same idea. Mayneord described as a scatter correction.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-71 for Sc, Sp, and Sc,p in monitor-unit calculations. AAPM TG-74 for in-air output ratio. AAPM TG-51 for TPR20,10. Public blueprint I.10.

## Radiation Measurement Quiz

This quiz checks kerma versus dose in the buildup region, Ptp greater than 1 when the air is warm or the pressure is low, and the definitions of PDD, TAR, TMR, TPR, BSF, Sc, and Sp. The traps are making TMR depend on SSD, setting BSF equal to 1 at every energy, obtaining Sp by multiplying Sc,p by Sc, applying Mayneord to a TMR, and using a narrow-beam attenuation factor as if it were PDD.
