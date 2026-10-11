# Module 6. Interaction of Radiation with Matter

Original notes for MDCB objective I.4.

## Interaction of Photons with Matter

**MDCB:** I.4

**What the exam expects**

You name coherent scatter, photoelectric absorption, Compton scatter, and pair production. You state the Z and energy dependence the exam uses, the products of each interaction, and which process dominates in soft tissue at therapy energies. You know the pair-production threshold is 1.022 MeV and that it is still not the dominant process in tissue at ordinary linac energies.

**Core facts**

The linear attenuation coefficient is the sum of the partial coefficients for the processes below. “Removed from the beam” and “energy absorbed locally” are different. Compton scatter removes a photon from the primary and puts a lower-energy photon somewhere else. Photoelectric absorption, when the characteristic x-ray is also absorbed, hands essentially the whole photon energy to charged particles nearby.

Coherent (Rayleigh) scatter. The photon scatters off the atom as a whole. The photon energy is unchanged. The angle is small. There is no ionization and no local energy deposition from the scatter itself. The probability rises with Z and falls with energy. In tissue at therapy energies it is negligible for dose. It is a small contributor to reduced contrast on a diagnostic image.

Photoelectric absorption. The photon is absorbed. A bound electron is ejected. Kinetic energy of that electron = photon energy − binding energy. The vacancy is filled with a characteristic x-ray or an Auger electron. In tissue the binding energy is negligible and the electron gets almost the whole photon energy. In high-Z material the characteristic photon can escape and carry energy away. The atomic attenuation goes approximately as Z^3 / E^3. That is the dependence this exam uses. Some tables fit a slightly different exponent; if you remember one relation, remember Z^3/E^3. Photoelectric absorption dominates at low energy and high Z: bone and contrast on a CT scanner, lead at diagnostic energies, and iodine. It is why a CT number of bone is not a pure density measurement.

Compton scatter. The photon strikes a loosely bound electron, which you treat as free. The photon scatters with reduced energy. The electron takes the difference. The probability per electron is independent of Z. Per gram, it is nearly the same for all materials except hydrogen, because Z/A is about 1/2 for everything heavier than hydrogen. This is the dominant photon interaction in soft tissue from a few tens of keV through the therapy megavoltage range, up to energies of order 25 MeV. Confirm a precise crossover energy in Khan. The exam statement is: Compton dominates in tissue at therapy energies. That is why megavoltage dose tracks electron density, not Z^3, and why a missing tissue-density correction still matters while a photoelectric f-factor usually does not.

Pair production. In the nuclear field the photon disappears and creates an electron and a positron. Threshold is 2 × 0.511 MeV = 1.022 MeV. Any energy above 1.022 MeV is shared as kinetic energy of the pair. The positron later annihilates and produces two 0.511 MeV photons. The probability rises with energy above threshold and goes approximately as Z^2. Triplet production in the field of an electron has a threshold of 2.044 MeV and is uncommon. Pair production is allowed at 6 MV and is still a minority of interactions in soft tissue there. It becomes an important share of the coefficient only at much higher energy, and earlier in high-Z absorbers than in water.

Photonuclear absorption. Above roughly 10 MeV a photon can knock a neutron out of the nucleus. This is the source of linac neutrons. It is not one of the four dose-dominating interactions in tissue, and it is the reason high-energy beams have a neutron shielding problem.

Where each wins, as recall statements: photoelectric at low E and high Z; Compton in tissue at therapy energies; pair production only above 1.022 MeV and dominant in tissue only at very high energy; coherent scatter negligible for therapy dose.

**Formulas**

Photoelectric, exam form: τ ∝ Z^3 / E^3

Compton: probability per electron independent of Z; per gram, roughly independent of Z.

Pair production: threshold 1.022 MeV; κ ∝ Z^2 above threshold.

Energy of a photoelectron: KE = hν − BE

- hν: photon energy
- BE: binding energy of the shell that was emptied

**Traps**

Compton assigned a Z^3 dependence. Photoelectric assigned as the dominant interaction at 6 MV in muscle. Pair production allowed at 0.511 MeV. Coherent scatter assigned a large local dose. Pair production described as the main event at 6 MV because “the energy is above threshold.” Threshold is permission to occur, not dominance. Dominance in tissue at 6–18 MV is still Compton.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.4.

## Energy of Photons

**MDCB:** I.4, I.10

**What the exam expects**

You compute the energy of a Compton-scattered photon at a stated angle and the energy given to the electron. You compute the kinetic energy left after pair production. You can say, for a given interaction, whether the energy is absorbed locally, carried off as a scattered photon, or both.

**Core facts**

A photon’s energy is hν. In tissue at therapy energies that quantum is usually Compton-scattered one or more times and then photoelectrically absorbed when its energy has fallen.

Compton relations the exam uses, with the electron rest energy 0.511 MeV:

- At 0 degrees the scattered photon keeps all the energy.
- At 90 degrees, E′ = E / (1 + α).
- At 180 degrees, E′ = E / (1 + 2α). This is the lowest energy the scattered photon can have. The electron then has its maximum energy (the Compton edge).
- Side scatter and backscatter from a patient are still hundreds of keV when the incident photon was 1 MeV. That is a shielding fact as well as a dosimetry fact.

As the incident energy rises, even a 180-degree photon cannot fall below about 0.255 MeV. High-energy scatter is forward. Low-energy scatter is more isotropic, which is why orthovoltage backscatter factors are larger than megavoltage backscatter factors.

Pair production of a photon of energy E leaves (E − 1.022) MeV of kinetic energy to share between the electron and the positron. The two annihilation photons are a separate 1.022 MeV that may escape the local volume. Do not count the threshold energy as kinetic energy, and do not forget that the annihilation photons exist.

Photoelectric kinetic energy is hν − BE. In soft tissue at 100 keV, BE is a rounding error. In lead or iodine it is not.

**Formulas**

α = E / 0.511, with E in MeV

E′ = E / [1 + α (1 − cos θ)]

- E′: scattered photon energy
- E: incident photon energy
- θ: photon scatter angle
- α: incident energy in units of the electron rest energy

Electron kinetic energy = E − E′

At θ = 90°, E′ = E / (1 + α)

At θ = 180°, E′ = E / (1 + 2α)

Pair kinetic energy shared = E − 1.022 MeV, only if E > 1.022 MeV.

**Worked example**

Given: a 1.00 MeV photon Compton-scatters. Find the scattered photon energy and the electron kinetic energy at 90° and at 180°.

Formula: α = E / 0.511. E′(90°) = E / (1 + α). E′(180°) = E / (1 + 2α). Electron energy = E − E′.

Substitution: α = 1.00 / 0.511 = 1.957.

At 90°: E′ = 1.00 / (1 + 1.957) = 1.00 / 2.957 = 0.338 MeV. Electron = 1.00 − 0.338 = 0.662 MeV.

At 180°: E′ = 1.00 / (1 + 3.914) = 1.00 / 4.914 = 0.204 MeV. Electron = 1.00 − 0.204 = 0.796 MeV.

Meaning: a right-angle scatter from a 1 MeV photon still leaves the room with about 340 keV. Most of the energy at 180° does go to the electron, but clinical scatter is not all at 180°. The photon that scatters at 90° keeps about a third of the incident energy. Shielding and in-room dose from scatter have to be designed for that photon, not for a fully absorbed quantum.

Usual wrong turn: E′ = E × cos θ, which gives 0 at 90° and −1 MeV at 180°. Or α = 0.511 / E, inverting the definition, which for this problem produces α = 0.511 and a 90° photon of 1/1.511 = 0.662 MeV. That swaps the photon and electron answers at 90°. Another miss: setting the 180° electron energy equal to E, as if the backscattered photon carried nothing.

**Traps**

Rest energy written 511 MeV inside α. Scatter angle taken as the electron angle; θ in this formula is the photon’s angle. Pair threshold subtracted twice, once for “creation” and again for annihilation, so a 10 MeV photon is left with 10 − 2.044 of kinetic energy. The kinetic energy available at creation is E − 1.022. The annihilation photons are created later, when the positron is already at rest.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.4.

## Wavelength and Frequency Tutorial

**MDCB:** I.4, I.10

**What the exam expects**

You convert photon energy to wavelength and to frequency with hc = 12.4 keV·Å and c = 3.00×10^8 m/s. You recognize 0.511 MeV, the annihilation and rest energy, as the photon whose wavelength equals the electron Compton wavelength scale used in scatter formulas.

**Core facts**

Energy and frequency are proportional. Energy and wavelength are inversely proportional. A higher-energy photon has a shorter wavelength and a higher frequency.

The working constant on this exam is 12.4 keV·Å. It is hc. If you remember Duane–Hunt, you already remember this constant: λmin (Å) = 12.4 / kVp because Emax in keV equals kVp.

The Compton wavelength of the electron is h/(mc) = 12.4 / 511 Å = 0.0243 Å. You do not need a second constant. A 511 keV photon has that wavelength.

Frequency follows from c = λν once λ is in meters. 1 Å = 10^−10 m.

**Formulas**

E (keV) = 12.4 / λ (Å)

λ (Å) = 12.4 / E (keV)

c = λν

- c: 3.00×10^8 m/s
- λ: wavelength in meters when you solve for ν
- ν: frequency in hertz
- E: photon energy

**Worked example**

Given: an annihilation photon, E = 511 keV. Find the wavelength in angstroms and the frequency. Then repeat the wavelength for a Co-60 mean energy of 1.25 MeV.

Formula: λ (Å) = 12.4 / E (keV). Convert λ to meters. ν = c / λ.

Example 1 substitution: E = 511 keV. λ = 12.4 / 511.

Arithmetic: 511 × 0.024 = 12.264. Remainder 0.136. 0.136/511 = 0.000266. λ = 0.0243 Å.

In meters: 0.0243 × 10^−10 m = 2.43×10^−12 m.

ν = 3.00×10^8 / 2.43×10^−12 = (3.00 / 2.43) × 10^20 = 1.23×10^20 Hz.

Example 2: E = 1.25 MeV = 1250 keV. λ = 12.4 / 1250 = 0.00992 Å.

Check: 1250 × 0.00992 = 12.4 exactly.

Meaning: the 511 keV annihilation photon and the wavelength shift constant in Compton theory are the same scale, 0.0243 Å. A 1.25 MeV cobalt photon is shorter in wavelength by 1250/511 ≈ 2.45, and 0.0243/2.45 ≈ 0.0099 Å, which matches.

Usual wrong turn: λ = 12.4 × 511, or E in MeV inserted into the keV form, λ = 12.4 / 0.511 = 24.3 Å, one thousand times too long. Or ν = c × λ, which for the annihilation photon gives an absurdly small frequency. Or converting angstroms with 10^−8 m (that is an obsolete “Ångström vs cm” slip); 1 Å = 10^−10 m.

**Traps**

hc taken as 12.4 MeV·Å, which collapses every wavelength by 1000. Frequency asked and the candidate stops at wavelength. A scatter problem that gives wavelength shift Δλ = 0.0243(1 − cos θ) Å and a candidate who adds that shift in nanometers. Keep angstroms until the last step.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*.

## Interaction of Photons with Matter Quiz

This quiz checks which interaction dominates for a stated energy and Z, the Z^3/E^3 photoelectric dependence, Compton’s near-independence of Z per gram, the 1.022 MeV pair threshold, and a numeric Compton scatter at 90° or 180°. The traps are using Compton for a 30 keV photon in bone, using photoelectric for 6 MV in tissue, setting the pair threshold at 0.511 MeV, and inverting α = E/0.511.
