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

## Matching the Detector to the Task

**Objectives:** I.10, VII.3

**What the exam expects**

You pick the right instrument for a stated job and you can say why the other instruments fail at that job. The exam does not ask you to operate the device. It asks which one belongs in the water tank, which one belongs at the vault door, which one belongs in the hot lab, and which one goes in the mail to Houston.

**Core facts**

A Farmer-type cylindrical chamber has a collecting volume of about 0.6 cm³ and an active length of a little over 2 cm. It is the reference-dosimetry chamber: TG-51 output calibration in water for photon beams and for electron beams above about 10 MeV, where the beam is flat across its length. Its weakness is size. In a field smaller than about 3 × 3 cm the chamber spans the penumbra and averages over the dose falloff, so the reading is low. Sensitivity scales with volume, so the Farmer gives a large, stable signal at a bias of about 300 V, which puts it on the saturation plateau of the gas-filled detector curve. Raising the bias toward about 1000 V would move a gas detector into the Geiger region, where every event gives the same pulse and dose information is lost.

Small-field and stereotactic work uses a micro-chamber of about 0.01 to 0.02 cm³, a shielded or unshielded diode, a plastic scintillator, or a diamond detector. These are point detectors: small enough that the dose is nearly uniform across the sensitive volume. The trade is a small signal, a larger leakage fraction, and for diodes an energy, temperature and angular dependence that must be corrected. TG-155 and the IAEA TRS-483 code of practice give the detector-specific small-field correction factors; the exam point is that a 0.6 cm³ chamber is the wrong instrument for a 1 × 1 cm field and a diode is the wrong instrument for defining reference output.

A parallel-plate (plane-parallel) chamber has a thin entrance window and a small plate separation. It is the chamber for electron beams below about 10 MeV, where the dose gradient along the beam is steep and a cylindrical cavity would perturb the fluence. It is also the chamber for surface dose and buildup-region measurements, because the effective point of measurement sits at the inner face of the window. Under TG-51 the gradient correction for a parallel-plate chamber is 1, which is one reason it is preferred for low-energy electrons.

A well-type (re-entrant) chamber surrounds the source with gas. The common HDR and LDR well chamber has a collecting volume of roughly 245 cm³, which gives it the sensitivity to assay a single low-dose-rate seed and the geometry to be insensitive to small source-position errors near the sweet spot. It measures the air-kerma strength Sk of a brachytherapy source against an ADCL calibration for that source model. A Farmer chamber in air at a measured distance is the old method and is now a cross-check only. The nuclear-medicine dose calibrator is the same idea, a pressurized well chamber calibrated per radionuclide in activity units.

A Geiger–Müller counter is the instrument for finding radiation, not for measuring dose. It is very sensitive, cheap, and rugged, so it is used to search for a lost seed, to check a package or a patient for contamination, and to confirm that an HDR source has retracted. It has a dead time of about 100 to 300 microseconds, so it saturates at high count rates, and in a pulsed linac beam it can read almost nothing while the dose rate is high. Its reading is energy dependent unless the probe is compensated. A GM is never the instrument for linac output.

An ion-chamber survey meter (a large, often pressurized, air chamber) reads exposure rate or air-kerma rate for area surveys around a brachytherapy patient, an HDR vault door, or a package. It is the right instrument when the number must be in mR/h or mSv/h with reasonable energy independence.

A proportional counter runs at a bias between the ionization plateau and the Geiger region, so the pulse height is proportional to the energy deposited. That lets it discriminate alpha from beta events in a contamination counter. Filled with boron trifluoride (BF3) or helium-3, it detects thermal neutrons through the boron-10 or helium-3 capture reaction. Surrounded by a polyethylene moderating sphere it becomes the rem-ball (rem-meter, Bonner sphere), which is the standard neutron survey meter outside the door of a vault running photon beams above 10 MV. A bubble detector (superheated drops in a gel) is a passive personal neutron dosimeter that is read by counting bubbles and reset by recompression. Activation foils (gold, indium) are the laboratory method.

A thallium-activated sodium iodide, NaI(Tl), scintillator is the detector for wipe tests of sealed sources and for low-level counting. A wipe that must be reported at 0.005 µCi (185 Bq) is about 11,000 disintegrations per minute; a well-shaped NaI counter detects that in seconds, while an ion chamber cannot see it at all. NaI crystals are also the detector in gamma cameras and thyroid probes.

Two-dimensional and array detectors do relative dosimetry. Diode or small-chamber arrays (planar or cylindrical) are the standard patient-specific IMRT and VMAT QA device, compared with the plan by a gamma analysis. Radiochromic film gives the highest spatial resolution for small-field profiles and for brachytherapy checks. The amorphous silicon (a-Si) flat panel is the EPID and the kV imager, and it can also serve as a 2D dosimeter.

The measurement chain is traceable. The clinic's reference chamber and electrometer are calibrated at an Accredited Dosimetry Calibration Laboratory (ADCL), traceable to NIST, and TG-51 states the interval as every two years, with a constancy check against a Sr-90 check source or a redundant chamber in between. Survey meters used for regulatory surveys are calibrated annually and after any repair, with a daily battery and check-source response before use. The independent audit is IROC Houston: a mailed optical or thermoluminescent dosimeter (OSLD, formerly TLD) is irradiated to a stated dose and the institution's output must agree within about 5%, and anthropomorphic phantoms (head-and-neck, lung, prostate) carry TLD and film for end-to-end IMRT and SBRT credentialing.

**Formulas**

GM dead-time correction, non-paralyzable model: true rate n = m / (1 − m τ), where m is the observed count rate and τ the dead time. Fraction of counts lost ≈ m τ.

**Worked example**

Given: a GM probe with 100 microsecond dead time reads 2,000 counts per second. Find the true rate and the fraction lost.

Substitution: m τ = 2,000 × 100 × 10^−6 = 0.20. n = 2,000 / (1 − 0.20) = 2,000 / 0.80 = 2,500 counts per second.

Meaning: the meter is already losing one count in five at a modest rate. At 10,000 counts per second the product m τ would be 1.0 and the simple formula fails; the tube is paralyzed and can read low or zero. That is why a GM reads nothing useful in a linac beam and why a dose-rate survey of an HDR source uses an ion chamber.

**Traps**

GM used for linac output or for an HDR dose-rate survey. Farmer chamber used to define the output of a 1 × 1 cm cone. Diode used as the reference detector for TG-51. Well chamber described as a photon-beam calibration device. Wipe test read with an ion chamber. Rem-ball described as a photon survey meter. Chamber calibration described as annual or as "once at purchase."

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, dosimeters chapter. AAPM TG-51 and its 2014 addendum (calibration interval, chamber choice). AAPM TG-155 and IAEA TRS-483 (small-field detectors). AAPM TG-56 and TG-40 (well chamber for Sk). 10 CFR 20 and 35 (survey-meter calibration). IROC Houston credentialing program.

## Chamber Corrections and Passive Dosimeters

**Objectives:** I.10, VII.3

**What the exam expects**

You can compute the recombination and polarity corrections from two readings each, you know which direction each moves the dose, and you can describe how TLD, OSL, MOSFET, radiographic film and radiochromic film store and release their signal. The temperature–pressure correction is in the lesson above and is not repeated here.

**Core facts**

The TG-51 photon chain is: dose to water equals the raw electrometer reading, times Ptp, Pion, Ppol and Pelec, times the quality conversion factor kQ, times the absorbed-dose-to-water calibration coefficient N_D,w. Each P factor is a small multiplicative correction near 1. Ptp is the only one that changes day to day. Pion and Ppol are measured at commissioning and checked at the annual calibration; kQ comes from the TG-51 table for the chamber model and the measured %dd(10)x or TPR20,10; N_D,w comes from the ADCL certificate for Co-60.

Pion corrects for ions that recombine before they reach the electrode. In a pulsed linac beam the charge density per pulse drives recombination, so Pion grows with dose per pulse: it is larger for FFF beams, for high dose-rate electron beams and at short SSD. TG-51 measures it by the two-voltage method: take the reading at the normal bias V_H (about 300 V) and at half that bias V_L, and Pion at V_H equals (1 − V_H/V_L) divided by (M_H/M_L − V_H/V_L). Pion is always slightly greater than 1; a Pion above 1.05 means the chamber or bias is unsuitable for that beam. Lowering the bias collects fewer ions, so the lower-voltage reading is the smaller one.

Ppol corrects for the fact that the reading changes a little when the sign of the bias is reversed, because of charge deposited in the stem and cable and asymmetric collection. It is the average of the magnitudes of the two readings divided by the reading at the polarity actually used in the clinic: Ppol = |M+ − M−| / (2 M), where M is the reading, with its sign, at the working polarity. Ppol is normally within 1% of 1 for a Farmer in photons and can be larger for parallel-plate chambers in low-energy electrons. Pelec is the electrometer calibration factor, 1.000 when the chamber and electrometer were calibrated together.

Thermoluminescent dosimeters store dose as electrons trapped in crystal defects. The clinical material is lithium fluoride doped with magnesium and titanium (LiF:Mg,Ti, TLD-100), chosen because its effective atomic number of about 8.2 is close to tissue. Heating the chip releases the trapped electrons as light, and the plot of light output against temperature is the glow curve. The low-temperature peaks fade in hours and are discarded; the dosimetric signal is the high-temperature peak 5 near 210 °C (often integrated with peak 4). TLD is destructive: reading empties the traps, and the chip must be annealed (a standard cycle is 400 °C for one hour followed by 100 °C for two hours, with a short 100 °C pre-read anneal to clean out the shallow traps) before reuse. TLD is linear up to a few gray, supralinear above that, and good to about 3 to 5% with a batch calibration. It is the classic in-vivo and mailed-audit detector and the material in older personnel badges.

Optically stimulated luminescence dosimeters use carbon-doped aluminium oxide (Al2O3:C). The trapped charge is released by a light pulse instead of heat, and only a small fraction of the traps empties on each read, so an OSLD can be read repeatedly. It is cleared by prolonged light exposure (bleaching), has a fast readout and a modest energy dependence at kV energies because its effective atomic number is higher than tissue. OSL is now the dominant badge technology and the IROC mailed-output detector.

A MOSFET dosimeter is a small transistor whose threshold voltage shifts in proportion to the dose absorbed in its gate oxide. It gives an immediate reading, is tiny and can be placed on the skin or in a catheter, but it has a finite life (the total shift is limited), a temperature and energy dependence, and a calibration that drifts with accumulated dose. It is an in-vivo and intracavitary tool, not a calibration tool. Diodes are similar in role: instant reading, no bias, with energy, temperature, dose-rate and angular dependence and a sensitivity that falls with accumulated dose.

Radiographic (silver-halide) film records dose as optical density after chemical processing. The sensitometric or H&D (Hurter–Driffield) curve plots optical density against the logarithm of exposure: a toe, a straight-line region whose slope is the gamma (contrast), and a shoulder where the film saturates. Film is over-responsive to low-energy scatter because of silver, so it exaggerates dose outside the field and at depth. Radiochromic film (Gafchromic) darkens by polymerization without any processing, is close to tissue equivalent, has little energy dependence, is insensitive to room light, and is read with a flatbed scanner after a stabilisation time of about 24 hours for absolute dosimetry (the density keeps rising for several hours after exposure). Its resolution is sub-millimetre, which is why it is the small-field and brachytherapy film. Neither film is the instrument for defining output.

**Formulas**

Pion(V_H) = (1 − V_H/V_L) / (M_H/M_L − V_H/V_L), two-voltage method with V_H/V_L = 2.

Ppol = |M+ − M−| / (2 M_raw), where M_raw is the signed reading at the working polarity.

Dose to water = M_raw × Ptp × Pion × Ppol × Pelec × kQ × N_D,w.

**Worked example**

Given: a Farmer chamber reads 20.10 nC at 300 V and 20.00 nC at 150 V in a 6 MV beam. At 300 V, the reading with reversed polarity has magnitude 20.00 nC. Ptp is 1.020, Pelec is 1.000, kQ is 0.992, N_D,w is 5.00 cGy per nC. Find Pion, Ppol and the dose.

Pion: M_H/M_L = 20.10 / 20.00 = 1.005. Pion = (1 − 2) / (1.005 − 2) = (−1) / (−0.995) = 1.005.

Ppol: (20.10 + 20.00) / (2 × 20.10) = 40.10 / 40.20 = 0.9975.

Corrected charge: 20.10 × 1.020 × 1.005 × 0.9975 = 20.10 × 1.0225 = 20.55 nC. Dose = 20.55 × 0.992 × 5.00 = 101.9 cGy.

Meaning: recombination added half a percent, polarity removed a quarter of a percent, and the weather added two percent. Each is small; together they are the difference between a passing and a failing 2% annual tolerance. Check: the corrections multiply to 1.0225, so the dose is 2.25% above the uncorrected 99.7 cGy.

Usual wrong turn: Pion = M_L / M_H = 0.995, which corrects the wrong way. Or Ppol computed as M+ / M− = 1.005. Or using 300/150 = 2 as a correction factor by itself.

**Traps**

Pion below 1. Pion measured by changing temperature instead of bias. Glow curve attributed to OSL. TLD described as re-readable or OSL as destructive. Radiochromic film read immediately after exposure for an absolute dose. Film gamma confused with gamma analysis of an IMRT QA. MOSFET used for TG-51 output.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, dosimeters and film chapters. AAPM TG-51 (Pion, Ppol, Pelec, kQ) and the TG-51 addendum. AAPM TG-191 (TLD and OSLD clinical use). AAPM TG-55 and TG-235 (radiochromic film).

## Chamber Walls, Counting Efficiency, Protocols and Chemical Dosimetry

**Objectives:** I.10, VII.3

Four loose ends from the measurement lesson: what the chamber is made of and why, how a contamination count is turned into an activity, which protocol is the international twin of TG-51, and the one chemical dosimeter the exam still names.

Chamber walls and build-up caps. A cavity chamber works by Bragg-Gray theory, which assumes the electrons crossing the air cavity come from the surrounding medium, so the wall should be as close to water or air as possible in its atomic composition. Graphite (pure carbon, Z = 6) is the classic Farmer wall; it is conductive, stable and close to air in effective Z (6 versus 7.6). C-552 is a conductive plastic formulated to be air-equivalent, used for the wall and the central electrode of many thimble and parallel-plate chambers. A-150 is a conductive tissue-equivalent plastic (mostly carbon and hydrogen, with the hydrogen content of muscle) used in chambers for neutron and proton work where the hydrogen matters. PMMA (acrylic, Lucite, Perspex) is nearly water-equivalent and inexpensive, so it is the usual build-up cap and phantom material, but it is an insulator and is not used as the collecting wall without a conductive coating. Aluminum appears as the central electrode in the original Farmer design and contributes a small but known perturbation. The build-up cap is used for in-air measurements at megavoltage energies to provide charged-particle equilibrium; it is removed for in-phantom TG-51 measurements, where the phantom provides the build-up, and it is matched to the beam energy (about 0.5 g/cm² for Co-60, more at higher MV).

From counts to activity. A survey instrument or a wipe counter reports counts per minute (cpm). Activity is disintegrations per minute (dpm), and the two are related by the counting efficiency, the fraction of decays the detector actually registers: dpm = net cpm divided by efficiency, where net cpm is the gross count rate minus the background count rate. Efficiency depends on geometry (a well counter sees nearly 4π, a pancake probe above a wipe sees less than 2π), on the window and the radiation type (alphas and soft betas are stopped by any window; gammas pass through a thin detector), and on the energy. Typical numbers are 30 to 50% for a well counter with Cs-137, 5 to 20% for a pancake GM over a beta wipe, and under 1% for a GM tube counting gammas. Worked example: a package wipe reads 480 cpm with 40 cpm background on a counter with 20% efficiency. Net = 480 − 40 = 440 cpm. dpm = 440 / 0.20 = 2,200 dpm. Check: 2,200 × 0.20 = 440 cpm, the net reading. In other units 2,200 dpm is 2,200 / 60 = 36.7 Bq, or 2,200 / (2.22 × 10⁶ dpm per µCi) = 0.001 µCi. That is exactly the removable-contamination trigger for a received package of beta-gamma emitters, 2,200 dpm per 100 cm² (10 CFR 20.1906 and 49 CFR 173.443), so this wipe sits right at the limit. Keep that number separate from the sealed-source leak-test limit, which is 0.005 µCi = 185 Bq = about 11,000 dpm of removable activity (10 CFR 35.67), five times higher. The common wrong turns are multiplying by efficiency (giving 88 dpm), forgetting to subtract background (2,400 dpm), confusing the two limits, and converting 2,200 dpm to 2,200 Bq.

Protocols. AAPM TG-51 (1999, addendum 2014) is the North American absorbed-dose-to-water protocol for photon and electron beams from Co-60 to 50 MV, built on an ND,w calibration traceable to NIST and the beam quality specifier %dd(10)x. IAEA TRS-398 (2000, revised 2024) is the international counterpart: the same ND,w formalism and kQ concept, traceable to the BIPM, with TPR20,10 as the photon beam quality specifier and R50 for electrons, and with additional chapters for kilovoltage, proton and heavy-ion beams. The two agree to within about 1% for the same chamber in the same beam. Their predecessors, TG-21 and TRS-277, were air-kerma-based (Nx, Ngas) protocols and are no longer used for clinical reference dosimetry. TG-61 is the AAPM kilovoltage protocol, and TG-25/TG-70 cover clinical electron dosimetry beyond the reference point.

Fricke dosimetry. The Fricke dosimeter is an air-saturated solution of ferrous sulfate in dilute sulfuric acid; radiation oxidizes Fe²⁺ to Fe³⁺ with a radiation chemical yield G of about 15.5 ions per 100 eV (1.6 µmol per joule) at megavoltage energies, and the Fe³⁺ concentration is read by ultraviolet absorbance at 304 nm. It is water-equivalent, absolute (no calibration against another dosimeter), linear from about 40 to 400 Gy, and independent of dose rate, which made it a primary standard for absorbed dose and the reference against which early chamber protocols were checked. It is too insensitive for clinical doses of 2 Gy and is destroyed by reading, so today it appears on the exam as the classic chemical dosimeter, and in the clinic as the chemistry behind Fricke gel and polymer gel 3D dosimeters.

**Traps**

PMMA quoted as a conductive wall material. Build-up cap left on in the phantom. cpm multiplied by efficiency. Background forgotten. TRS-398 called an air-kerma protocol or a kilovoltage-only protocol. TG-21 used as the current reference protocol. Fricke described as a solid-state or film dosimeter, or as sensitive enough for a 2 Gy check.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, measurement of absorbed dose chapter. AAPM TG-51 and addendum; IAEA TRS-398. Attix, *Introduction to Radiological Physics and Radiation Dosimetry*, chemical dosimetry chapter. NRC Regulatory Guides 8.23 and 10.8 for contamination levels.
