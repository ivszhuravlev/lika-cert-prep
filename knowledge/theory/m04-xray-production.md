# Module 4. Production of X-rays

Original notes for MDCB Domain I.

## X-Ray Production

**MDCB:** I.2

**What the exam expects**

You explain where bremsstrahlung and characteristic x-rays come from, what is different about their spectra, and why almost all of the electron energy at diagnostic and orthovoltage potentials becomes heat. You know production efficiency rises with Z and with electron energy, which is why megavoltage targets convert a much larger share of electron energy into photons than a 100 kV tube does.

**Core facts**

Electrons are boiled off a filament (thermionic emission), accelerated through a potential difference, and stopped in a high-Z target. Two photon processes follow.

Bremsstrahlung. The electron is deflected in the nuclear Coulomb field and loses kinetic energy as a photon. The photon can carry any energy from near zero up to the full electron kinetic energy. The spectrum is continuous. The endpoint energy in keV equals the tube potential in kV (Duane–Hunt). Radiative yield rises with Z of the target and with electron energy.

Characteristic x-rays. The incoming electron ejects an inner-shell electron. An outer electron fills the vacancy. The photon energy is the difference between the two shell binding energies, so the spectrum is discrete lines (Kα, Kβ). For tungsten the K-shell binding energy is about 69.5 keV. A tube operated below about 70 kV produces no tungsten K characteristic x-rays. Running at 100 kV does. The lines sit on top of the bremsstrahlung continuum.

At 100 kV in tungsten, well under 1% of the electron kinetic energy becomes x-rays. The rest is heat in the anode. That is why targets are tungsten (Z = 74, melting point about 3400°C) and why therapy tubes care about anode heat. At megavoltage energies the bremsstrahlung efficiency is much higher; a linac target is a transmission target, not a diagnostic anode, and heat is still a design limit.

Intensity of the continuous beam increases with tube current (mA), with time, and approximately with Z and with the square of kVp. mA changes quantity only. kVp changes quantity and quality. Filtration changes both, by removing low-energy photons.

**Formulas**

Endpoint: Emax (keV) = tube potential (kV). Equivalently λmin (Å) = 12.4 / kVp.

Efficiency of x-ray production, the relation given in Khan:

η = 9×10^−10 × Z × V

- η: fraction of electron kinetic energy converted to x-rays
- Z: atomic number of the target
- V: tube voltage in volts

Confirm the prefactor in Khan before treating it as more precise than this working formula. The scaling, proportional to Z and to voltage, is the exam point.

**Worked example**

Given: tungsten target, Z = 74, tube voltage 100 kV. Estimate the bremsstrahlung production efficiency with the Khan prefactor.

Formula: η = 9×10^−10 × Z × V, with V in volts.

Substitution: V = 100 kV = 1.00×10^5 V. η = 9×10^−10 × 74 × 1.00×10^5.

Arithmetic: 74 × 1.00×10^5 = 7.4×10^6. 9×10^−10 × 7.4×10^6 = 6.7×10^−3. η = 0.0067 = 0.67%.

Meaning: about 99.3% of the electron energy heats the anode. Characteristic production is extra only if kVp exceeds the K-edge; it does at 100 kV, and it is still a minority of the energy.

Usual wrong turn: inserting 100 instead of 100000 for V, which yields 6.7×10^−6 and makes the efficiency look a thousand times worse. Or inserting V in kV into a formula whose constant assumes volts. The other miss is claiming a useful characteristic yield at 60 kV in tungsten. 60 keV electrons cannot eject a K-shell electron bound by about 70 keV.

**Traps**

Bremsstrahlung described as discrete. Characteristic x-rays described as a continuum. Efficiency treated as independent of Z, which would make a copper target as good a producer as tungsten. Heat load ignored because “the beam is off most of the time.”

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.2.

## X-Ray Energy Spectrum

**MDCB:** I.2, I.3

**What the exam expects**

You sketch a filtered bremsstrahlung spectrum: zero below a minimum wavelength, a continuous hump, characteristic lines if kVp exceeds the K-edge, and a low-energy cutoff from filtration. You state how kVp, mA, and added filtration each move that curve. You compute λmin.

**Core facts**

Unfiltered bremsstrahlung intensity rises from the endpoint toward lower energy. Inherent filtration (glass, oil, beryllium window, housing) and added filtration (aluminum, copper) absorb the lowest energies first. The beam that leaves the housing is harder than the beam born in the target: higher average energy, lower total fluence, higher HVL.

Rules the exam uses:

- Raise mA or mAs: the whole spectrum scales up. Shape and endpoint stay. Quality is unchanged. Quantity rises in proportion to mAs.
- Raise kVp: endpoint energy rises, average energy rises, and quantity rises faster than the kVp ratio (about as kVp squared in the usual approximation). Quality and quantity both change.
- Add filtration: low-energy photons drop out, average energy and HVL rise, quantity falls. This is beam hardening.
- For a polyenergetic beam the second HVL is thicker than the first, because the beam that survives the first HVL is harder. Homogeneity coefficient = first HVL / second HVL. It is 1 for a monoenergetic beam and less than 1 for a hardened polyenergetic beam.
- A lightly filtered diagnostic spectrum has an average energy on the order of one-third of kVp. Confirm a specific average in Khan. Do not use one-third as an endpoint law. The endpoint is the full kVp.

Kramers’ thin description of the unfiltered continuum: intensity at energy E is proportional to Z × (Emax − E). Filtration multiplies that shape by an energy-dependent transmission. You are not asked to redraw Kramers from memory. You are asked what filtration does to the low-energy end.

Co-60 is not this spectrum. Co-60 emits two discrete gammas, 1.17 and 1.33 MeV. It has no kVp and no heel effect.

**Formulas**

Duane–Hunt: λmin (Å) = 12.4 / kVp

- λmin: shortest wavelength in the spectrum
- kVp: peak tube voltage in kilovolts
- 12.4: hc expressed so the answer is in angstroms when energy is in keV

Emax (keV) = kVp, for the maximum photon energy.

Homogeneity coefficient = HVL1 / HVL2.

**Worked example**

Given: a tube operated at 120 kVp. Find the minimum wavelength and the maximum photon energy. Then interpret a measured HVL1 = 1.5 mm Cu and HVL2 = 2.5 mm Cu. (Those HVL numbers are given for the arithmetic; they are not a universal 120 kVp result.)

Formula: λmin = 12.4 / kVp. Emax = kVp in keV. HC = HVL1 / HVL2.

Substitution: λmin = 12.4 / 120. Emax = 120 keV. HC = 1.5 / 2.5.

Arithmetic: λmin = 0.103 Å. HC = 0.60.

Meaning: no photon in this beam has a wavelength shorter than 0.103 Å or an energy above 120 keV, no matter how much filtration you add. Filtration can only remove photons, not raise the endpoint. HC = 0.60 means the second half-value layer is thicker than the first, so the beam is polyenergetic and hardened. A monoenergetic source would have given HC = 1.

Usual wrong turn: λmin = 12.4 × 120, a huge wavelength, which also makes the student think filtration creates higher-energy photons. Or HC = HVL2/HVL1 = 1.67 and a claim that a larger coefficient means a dirtier beam. The coefficient used here is first over second, and closer to 1 means more homogeneous.

**Traps**

mA described as changing quality. kVp described as quantity only. Filtration described as raising Emax. HVL1 = HVL2 offered as proof of heavy filtration; equal HVLs mean the beam is not hardening, which means it is already effectively monoenergetic. Characteristic lines drawn on a 50 kV tungsten spectrum.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.2 and I.3.

## X-Ray Tube

**MDCB:** I.2, I.5

**What the exam expects**

You name the parts that produce the beam and you know which knob changes which parameter. You can apply the line-focus principle and state the direction of the heel effect. You know why superficial tubes use a beryllium window and added filtration, and why the treatment is timed rather than counted in monitor units.

**Core facts**

Cathode: filament plus focusing cup. Filament current heats the wire and sets the number of electrons available (tube current, mA). The focusing cup shapes the electron stream onto the target.

Anode: tungsten target embedded in a copper block on therapy tubes. The target is angled. Actual focal spot is the area struck by electrons. Effective focal spot, as seen from the central axis of the beam, is smaller: line-focus principle. A small effective spot keeps geometric penumbra smaller. A large actual spot spreads heat.

Heel effect: photons produced in the target must escape through the anode face. On the anode side of the field they travel through more target material and are attenuated more. Intensity is higher on the cathode side of the field. For a superficial treatment this can be used deliberately, or it can produce an unwanted gradient. Diagnostic tubes show the same effect.

Envelope: vacuum, so electrons are not scattered by air before the target. Window: glass on many tubes; beryllium on superficial and Grenz-ray tubes because low-energy photons would not survive glass. Added filtration (aluminum for superficial, copper plus aluminum for higher kV) is placed after the window to set the HVL the prescription assumes.

Housing: lead-lined, leakage limit applies, oil or water cooling. A hooded anode on orthovoltage tubes reduces extrafocal radiation from electrons that bounce off the target and hit other metal.

Generators: single-phase, three-phase, and high-frequency. Less voltage ripple means a higher average photon energy and a higher output for the same kVp setting. High-frequency supplies are the modern default.

Space charge: at low kVp, not every electron boiled off the filament reaches the anode. Tube current then depends on kVp. In saturation, every emitted electron is pulled across and mA is controlled by filament temperature alone.

The patient dose from a kV unit is tube output × time, corrected by an end effect (timer error) if the shutter or the kV waveform does not turn on cleanly. There is no transmission ion chamber defining a monitor unit the way a linac does.

Heat units accumulate in the anode and the housing. A single exposure’s heat is proportional to kVp × mA × time, with a waveform factor greater than 1 for three-phase and high-frequency supplies (confirm the factor in Khan). The exam point is that heat, not only the prescription, limits how long a kV unit can run.

**Formulas**

Line focus: effective focal-spot length = actual length × sin(θ)

- θ: anode angle, the angle between the target face and the central axis of the useful beam

Exposure with a timer error, when dose is proportional to (set time + δ):

R1 / R2 = (t1 + δ) / (t2 + δ)

- R: reading (dose or exposure) for a set time t
- δ: end effect, in the same time unit. Solve for δ from two exposures. δ can be negative.

**Worked example**

Given: two shutter timings on an orthovoltage unit. A 1.00 min setting delivers 80 cGy. A 2.00 min setting delivers 180 cGy. The dose is proportional to (set time + δ). Find δ. Then find the timer setting that delivers a true 1.00 min of beam.

Formula: R1/R2 = (t1 + δ) / (t2 + δ)

Substitution: 80/180 = (1 + δ) / (2 + δ)

Arithmetic: 80(2 + δ) = 180(1 + δ). 160 + 80δ = 180 + 180δ. 160 − 180 = 180δ − 80δ. −20 = 100δ. δ = −0.20 min.

Interpretation of the sign: delivered beam-on time = set time − 0.20 min. To get 1.00 min of beam, set time = 1.20 min.

Check: at set time 1.20, effective time = 1.00. At the measured points, effective times are 0.80 min and 1.80 min. Ratio of doses should be 1.80/0.80 = 2.25. Measured ratio 180/80 = 2.25. Consistent.

Meaning: the timer setting is not the beam-on time. Here every exposure is short by 0.2 min, so a prescription calculated as dose / nominal dose rate underestimates the setting.

Usual wrong turn: average the two dose rates (80 cGy/min and 90 cGy/min) and pick one. Or set δ = +0.20 min and subtract it, giving a 0.80 min setting that delivers only 0.60 min of beam. The sign comes out of the algebra; do not assume the shutter error is always added.

**Traps**

Heel effect reversed (intensity higher on the anode side). Line focus written as actual × cos(θ) without a drawing; the effective length along the anode-cathode axis is actual × sin(θ) for the usual definition of θ. Beryllium window replaced with lead. Filament current described as setting kVp. A claim that added filtration increases output.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.2 and I.5 (superficial and orthovoltage units).

## Mass Attenuation Coefficient

**MDCB:** I.3, I.4, I.10

**What the exam expects**

You use I = I0 exp(−μx) for a narrow beam, convert between μ and HVL, and convert between the linear coefficient and the mass coefficient with density. You know why the mass coefficient, not the linear coefficient, is what you look up in a table, and why a narrow-beam μ underestimates transmission once scatter is present.

**Core facts**

The linear attenuation coefficient μ is the probability per unit distance that a photon is removed from a narrow beam. Removed means absorbed or scattered out of the beam. Unit: per length, often cm^−1. μ depends on photon energy and on the material, including the material’s density.

The mass attenuation coefficient μ/ρ has unit area per mass (cm²/g). It does not change if you compress the material. Tables are published as μ/ρ. Recover the linear coefficient with μ = (μ/ρ) × ρ.

Half-value layer is the thickness that cuts the narrow-beam intensity in half. Tenth-value layer cuts it to one-tenth. For a monoenergetic narrow beam, every successive HVL is equal. For a polyenergetic beam, later HVLs are larger (beam hardening), which is why HVL1 and HVL2 were different in the spectrum lesson.

Mass energy-transfer coefficient μ_tr/ρ is the part of μ/ρ that hands energy to charged particles. Kerma uses it. Mass energy-absorption coefficient μ_en/ρ subtracts the energy those charged particles later lose as bremsstrahlung. Absorbed dose under charged-particle equilibrium tracks μ_en/ρ. At diagnostic energies in tissue the two are almost the same. At high Z and high energy they are not, because radiative losses grow.

Narrow beam: a small detector far away sees only photons that never interacted. Broad beam: scatter from the phantom or the wall can reach the detector. Transmission is higher than the narrow-beam exponential. Shielding calculations put that extra into a buildup factor. Using a narrow-beam μ for a broad beam overestimates the shielding.

Coherent scatter, photoelectric absorption, Compton scatter, and pair production each contribute a partial coefficient. μ is their sum. Which term wins is the subject of module 6.

**Formulas**

I = I0 exp(−μx)

- I: intensity or fluence on the far side of a narrow beam
- I0: intensity with no absorber
- μ: linear attenuation coefficient
- x: thickness, same length unit as in μ

HVL = 0.693 / μ

TVL = 2.30 / μ = 3.32 HVL

μ = (μ/ρ) × ρ

- μ/ρ: mass attenuation coefficient
- ρ: physical density

Number of HVLs = x / HVL. Transmission = (1/2)^(x/HVL) for a monoenergetic narrow beam.

**Worked example**

Given: a monoenergetic narrow beam has μ = 0.0693 cm^−1 in water of density 1.00 g/cm³. Find the HVL, the transmission through 20 cm of water, and the linear coefficient if that same water is only a thought-experiment at density 2.00 g/cm³ with the same μ/ρ.

Formula: HVL = 0.693 / μ. Transmission = exp(−μx). μ = (μ/ρ) ρ.

Substitution: HVL = 0.693 / 0.0693. x = 20 cm. μ/ρ = 0.0693 cm²/g at unit density.

Arithmetic: HVL = 10.0 cm. μx = 0.0693 × 20 = 1.386 = 2 × 0.693. Transmission = exp(−1.386) = (1/2)^2 = 0.25.

At ρ = 2.00 g/cm³, μ = 0.0693 × 2 = 0.1386 cm^−1. HVL = 5.0 cm of the dense material. The mass thickness of one HVL is still 10 g/cm².

Meaning: 20 cm of unit-density water is two half-value layers, so one-quarter of the narrow-beam photons remain. Doubling density doubles μ and halves the physical HVL. It does not change μ/ρ.

Usual wrong turn: transmission = μx = 1.386, reported as “137% transmitted,” which treats the exponent as the answer. Or HVL = μ / 0.693, inverting the formula, HVL = 0.10 cm, absurd for this μ. Or multiplying μ/ρ by 20 cm and forgetting density, then calling the result dimensionless. μ/ρ × thickness is dimensionless only when thickness is a mass thickness in g/cm².

**Traps**

Using the exponential for a broad beam inside a patient and expecting it to equal dose. Dose includes scatter and buildup; the exponential is photon removal from the primary. Quoting μ in cm²/g. That unit is μ/ρ. Assuming HVL1 equals HVL2 for a 120 kV beam. Changing density and changing μ/ρ with it.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.3, I.4, I.10.

## X-Ray Tube Design Mini-Quiz

This quiz checks cathode versus anode, what mA changes versus what kVp changes, the line-focus relation between actual and effective focal spot, the heel effect (higher intensity on the cathode side), why a beryllium window is used for soft beams, and why characteristic tungsten K x-rays are absent below about 70 kV. The traps are reversing the heel effect, using filtration to raise the endpoint energy, and treating timer setting as beam-on time when an end effect is in the stem.

## Production of X-Rays Quiz

This quiz checks bremsstrahlung as a continuum with endpoint equal to kVp, characteristic radiation as discrete shell differences, production efficiency rising with Z and tube voltage, λmin = 12.4/kVp, and HVL1 versus HVL2 for a polyenergetic beam. The traps are a discrete bremsstrahlung spectrum, an efficiency formula fed with kV when it expects volts, homogeneity coefficient inverted, and mA described as a quality control.

## Generator Rectification and What Filtration Changes

**Objectives:** I.2, I.4

The high-voltage generator decides how steady the tube potential is, and the filtration decides what leaves the tube. Items on these two topics are recall with a direction of change attached, so learn the direction for each quantity.

Rectification converts the alternating supply into a potential that always drives electrons from cathode to anode. Half-wave rectification on single-phase power uses only one half of each cycle, so the tube is idle half the time and the potential falls to zero 60 times a second. Full-wave rectification flips the negative half-cycle, giving 120 pulses per second but still a potential that drops to zero between pulses, so the ripple is 100% for both single-phase schemes. Three-phase six-pulse generators overlap three waveforms and the potential never drops below about 87% of the peak (ripple about 13%); twelve-pulse three-phase holds it above about 96% (ripple about 4%). High-frequency generators convert the supply to several kilohertz, rectify and smooth it, and deliver a nearly constant potential with ripple under about 2%; they are small, light, and are what modern CT scanners, simulators and portable units use. Ripple is defined as (Vmax − Vmin)/Vmax. Less ripple means the tube spends more of the exposure near the set kVp, so for the same kVp and mAs the beam has a higher mean energy, a higher output, and a slightly higher HVL, and a shorter exposure time is needed for the same mAs.

Filtration removes the low-energy part of the spectrum that would be absorbed in the patient without reaching the detector. Inherent filtration is the glass or metal envelope, the insulating oil and the window, typically 0.5 to 1 mm aluminum equivalent; added filtration is deliberate aluminum or copper sheet; the total must be at least 2.5 mm Al equivalent above 70 kVp under 21 CFR 1020.30. Adding filtration lowers the number of photons at every energy but removes proportionally more of the soft photons, so the mean energy rises and the HVL increases (beam hardening). The maximum photon energy does not move, because it is set by the kVp. The characteristic lines do not move either, because their energies are fixed by the tungsten shell structure (K-alpha about 59 keV, K-beta about 67 keV); their heights fall along with the rest of the spectrum. Clinically, more filtration means lower patient entrance skin dose, lower subject contrast because the harder beam is less differentially attenuated, and a longer exposure or higher mA to restore detector signal. A lightly filtered diagnostic beam has a mean energy of about one-third of the peak; a heavily filtered or high-kV beam drifts toward about one-half.

Efficiency of bremsstrahlung production rises with target atomic number and with tube potential (roughly 9 × 10⁻¹⁰ × Z × V in volts, as used earlier in this module). At 100 kV in tungsten this is well under 1%, and the remaining 99% of the electron energy appears as heat in the anode, which is the whole reason for rotating anodes, tungsten-rhenium targets and heat-unit ratings. At linac energies the picture inverts: at 6 MV roughly 30 to 50% of the electron energy becomes x-rays, and at 20 MV well over half, so a linac target is thin, water-cooled and does not need to rotate, and the engineering problem becomes the forward-peaked intensity that the flattening filter has to level.

**Traps**

Ripple stated as 50% for full-wave single-phase (it is 100%, only the pulse rate doubles). Filtration said to lower the maximum energy or shift the characteristic lines. Filtration said to increase contrast. Efficiency said to fall with voltage. Rotating anode described as improving efficiency rather than heat handling.

**Sources**

Bushberg, *The Essential Physics of Medical Imaging*, x-ray production and generator chapters. Khan and Gibbons, *The Physics of Radiation Therapy*, production of x-rays chapter. 21 CFR 1020.30 for minimum total filtration.
