# Module 2. Fundamentals

Original notes. Objective domain: MDCB I, Radiation Physics.

## Fundamental Radiation Concepts

**MDCB:** I.3, I.4, I.10

**What the exam expects**

You separate ionizing from non-ionizing, directly ionizing from indirectly ionizing, and a point-source intensity change from a change in energy. You use the inverse-square law with the distances the stem actually gives. You know that a photon has energy and no charge, and that a charged particle loses energy continuously along a track.

**Core facts**

Ionizing radiation has enough energy per event to eject an electron from an atom. In tissue the relevant agents are photons, electrons, protons, heavier charged ions, and neutrons.

Directly ionizing radiation is charged: electrons, positrons, protons, alpha particles, heavy ions. The particle’s electric field knocks electrons out of atoms along the track. Indirectly ionizing radiation is uncharged: photons and neutrons. They transfer energy by setting charged particles in motion (photoelectrons, Compton electrons, recoil protons), and those charged particles deliver the dose.

Excitation raises an electron to a higher orbital state and does not produce an ion pair. Ionization removes the electron. Dose is energy imparted per unit mass. It is not the same quantity as exposure, kerma, or activity.

Electromagnetic radiation used in therapy (x-rays and gamma rays) has no rest mass and no charge, travels at c in vacuum, and is attenuated exponentially. Charged particles have a finite range. Neutrons are uncharged and are not exponentially “stopped” the way alphas are; they scatter, especially from hydrogen.

A point source in a non-absorbing geometry spreads the same emission over the surface of a sphere. Area grows as r^2, so intensity and dose rate fall as 1/r^2. Tissue attenuation is a separate factor. Inverse square does not include attenuation, and attenuation does not replace inverse square.

**Formulas**

Inverse square, same source, no attenuation change:

Ḋ2 / Ḋ1 = (r1 / r2)^2

- Ḋ1, Ḋ2: dose rates at distances r1 and r2 from the source
- r: distance from the source to the point of interest, same unit in both places

Photon energy and wavelength are related by E = hν and c = λν. The numeric form used on these exams is in the wavelength lesson: E(keV) = 12.4 / λ(Å).

**Worked example**

Given: a point source produces 100 cGy/min at 100 cm. Find the dose rate at 80 cm and at 120 cm. Ignore attenuation.

Formula: Ḋ2 = Ḋ1 × (r1 / r2)^2

Substitution at 80 cm: Ḋ2 = 100 × (100 / 80)^2

Arithmetic: 100/80 = 1.25. 1.25^2 = 1.5625. Ḋ2 = 156.25 cGy/min.

Substitution at 120 cm: Ḋ2 = 100 × (100 / 120)^2 = 100 × (5/6)^2 = 100 × 0.69444 = 69.4 cGy/min.

Meaning: moving closer raises dose rate by the square of the distance ratio. Moving from 100 cm to 80 cm is a 25% distance cut and a 56% dose-rate increase, not a 25% increase.

Usual wrong turn: using r2/r1, which swaps the answers (64 cGy/min at 80 cm). Or using a linear ratio, 100 × (100/80) = 125 cGy/min.

**Traps**

Calling neutrons or photons directly ionizing. Applying inverse square across a change in depth in tissue and forgetting that attenuation and scatter also changed. Using diameter when the given distances are radii, or mixing SSD and SAD without deciding which distance the inverse-square term actually uses.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public MDCB blueprint, objectives I.3 and I.10.

## Atomic Structure

**MDCB:** I.1, I.4

**What the exam expects**

You read Z, A, and N correctly and you know which particles sit in the nucleus. You know the scale of energies: electron binding is eV to keV, nuclear energies are MeV, and the electron rest energy is 0.511 MeV. That 0.511 MeV number is used again for annihilation, pair production, and Compton scatter.

**Core facts**

The nucleus contains protons and neutrons (nucleons). Electrons occupy shells. Chemical identity is Z, the proton number. Mass number A is protons plus neutrons. Neutron number N = A − Z.

A neutral atom has Z electrons. Removing one electron produces a positive ion. Shell labels start at K (principal quantum number 1), then L, M. K-shell binding is the largest. Binding energies in tissue atoms are well under 1 keV. The K-shell binding energy of tungsten is about 70 keV, which is why a diagnostic tube must be run above about 70 kV before tungsten K characteristic x-rays appear.

Rest energies to recall: electron 0.511 MeV, proton about 938 MeV, neutron about 940 MeV. One atomic mass unit is about 931 MeV. Confirm a more precise mass-table value in Khan if a stem asks for one.

The mass of a nucleus is less than the mass of its separated nucleons. The difference is the binding energy. Nuclear binding is MeV per nucleon. That is why gamma rays from nuclear de-excitation are MeV-scale, while characteristic x-rays from electron shells are keV-scale.

An atom is ionized when an electron is removed. The same atom can emit a characteristic x-ray or an Auger electron when the vacancy is filled. Those are atomic emissions. Gamma rays leave the nucleus.

**Formulas**

N = A − Z

- Z: atomic number, number of protons
- A: mass number, nucleons
- N: neutron number

Photon energy from a shell transition equals the difference in electron binding energies. A nuclear gamma energy equals the difference between two nuclear levels.

**Traps**

Setting A equal to Z. Counting electrons as nucleons. Quoting the electron rest energy as 511 keV and then using 511 MeV in a Compton or pair calculation. Treating a characteristic x-ray as a gamma ray; the exam uses the origin (shell versus nucleus) to classify the emission.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*.

## Classification of Atoms

**MDCB:** I.1, I.7

**What the exam expects**

Given two nuclides, you say whether they are isotopes, isobars, isotones, or isomers. You identify a metastable state, because Tc-99m is an isomer and I-125 and Pd-103 are different isotopes from I-131. Decay mode follows from which number changes, and that is the next module. This lesson is the classification the decay questions assume.

**Core facts**

Isotopes: same Z, different A. Same element, different neutron number. Co-59 and Co-60. I-125 and I-131. C-12 and C-14.

Isobars: same A, different Z. Different elements, same number of nucleons. Beta decay connects isobars, because beta decay changes Z by 1 and leaves A unchanged. Sr-90 and Y-90 are isobars. Mo-99 and Tc-99 are isobars.

Isotones: same N, different Z (and therefore different A). Same neutron count.

Isomers: same Z and same A, different nuclear energy state. The metastable state is marked “m”. Tc-99m and Tc-99 are isomers. The decay between them is an isomeric transition, a gamma (or internal conversion), and Z and A do not change. Internal conversion can be followed by Auger electron emission.

A radionuclide is an unstable nuclear species. A radiopharmaceutical is that nuclide in a chemical form. The exam half-life list is a list of nuclides, not of compounds.

Stable versus radioactive is a property of the nucleus, not of the electron shells. Chemical binding does not change the half-life at any level this exam cares about.

**Traps**

Calling Tc-99m an isotope of Tc-99. It is the same isotope’s metastable isomer; both have Z = 43 and A = 99. Calling Sr-90 and Y-90 isotopes of each other. They are different elements. Swapping isotone and isobar. Remember: isotope, same proton number; isobar, same A; isotone, same neutron number; isomer, same nucleus, different energy.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint objective I.1 (decay types assume this classification) and I.7.

## Fundamentals Mini-Quiz

This quiz checks whether you can assign Z, A, and N, separate isotope from isobar from isotone from isomer, and separate directly ionizing charged particles from indirectly ionizing photons and neutrons. It also checks a one-step inverse-square ratio. The traps are equating A with Z, calling Tc-99m a different element, calling neutrons directly ionizing, and inverting the distance ratio so the closer point gets the lower dose rate.

## Mass Defect and Binding Energy

**Objectives:** I.1, I.4

**What the exam expects**

You explain why a nucleus weighs less than its parts, convert that missing mass into energy with the 931.5 MeV per atomic mass unit figure, and name the force that holds the nucleus together. You also carry a few constants in your head: the electron is about 1/1836 of a proton mass, and 1 eV is 1.6 × 10^−19 J.

**Core facts**

Add up the masses of the free protons and neutrons that make a nucleus and the sum is larger than the measured nuclear mass. The shortfall is the mass defect. By E = mc^2 the defect is the binding energy that was released when the nucleons came together, and it is the energy you would have to supply to pull them apart again. One atomic mass unit (1 u = 1.66 × 10^−27 kg) is equivalent to about 931.5 MeV.

Binding energy per nucleon is the useful comparison number. It rises steeply through the light nuclei, peaks near 8.8 MeV per nucleon around iron and nickel (A about 56–62), and declines slowly toward uranium. Fission of a heavy nucleus and fusion of light nuclei both move toward the peak and release energy. Typical binding is several MeV per nucleon, which is why nuclear gamma rays and decay energies are MeV while chemical and electron-shell energies are eV to keV.

The strong nuclear force binds nucleons. It is attractive between any two nucleons, is far stronger than the electrostatic repulsion between protons, but acts only over about 10^−15 m, roughly one nucleon diameter. The electromagnetic force binds the orbital electrons to the nucleus and is what shell binding energies describe. Gravity is irrelevant at this scale. Heavy nuclei need extra neutrons because the strong force saturates while proton repulsion keeps adding up across the whole nucleus.

Constants to recall: electron rest mass 9.11 × 10^−31 kg, which is 1/1836 of the proton mass (proton 1.673 × 10^−27 kg, neutron slightly heavier at 1.675 × 10^−27 kg). Electron charge 1.602 × 10^−19 C. One electron-volt is the kinetic energy gained by one electron charge across one volt, so 1 eV = 1.602 × 10^−19 J, 1 keV = 1.6 × 10^−16 J, 1 MeV = 1.6 × 10^−13 J. Dose in gray is joules per kilogram, so a MeV-scale deposition must be converted to joules before it becomes a dose.

**Formulas**

Mass defect: Δm = Z × m_p + N × m_n − M_nucleus

Binding energy: BE = Δm × 931.5 MeV/u

Binding energy per nucleon: BE / A

**Worked example**

Given: a helium-4 nucleus has a measured mass of 4.0015 u. A free proton is 1.00728 u and a free neutron is 1.00866 u. Find the mass defect, total binding energy, and binding energy per nucleon.

Formula: Δm = 2 m_p + 2 m_n − M. BE = Δm × 931.5.

Substitution: 2 × 1.00728 + 2 × 1.00866 = 2.01456 + 2.01732 = 4.03188 u. Δm = 4.03188 − 4.0015 = 0.0304 u.

Arithmetic: BE = 0.0304 × 931.5 = 28.3 MeV. Per nucleon: 28.3 / 4 = 7.1 MeV.

Meaning: a 0.75% mass loss is 28 MeV of binding, about two million times the binding of a hydrogen electron (13.6 eV). That gap is the whole reason nuclear and atomic emissions are easy to tell apart by energy.

Usual wrong turn: reporting the total 28.3 MeV when the stem asked per nucleon, or multiplying by 511 keV (the electron rest energy) instead of 931.5 MeV per u.

**Traps**

Describing the mass defect as the mass of the emitted electrons. Saying the nucleus is held together by the electromagnetic force. Quoting the electron as 1/1836 of a neutron and then treating proton and neutron masses as very different; they differ by about 0.1%. Mixing 1.6 × 10^−19 (joules per eV, or coulombs per electron) with 1.66 × 10^−27 (kilograms per u).

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, atomic and nuclear structure chapter. Public blueprint I.1 and I.4.

## Avogadro, Planck and the Electromagnetic Spectrum

**Objectives:** I.1, I.2, I.3

**What the exam expects**

You turn grams into numbers of atoms and electrons with Avogadro's number, you use the Planck relation in both directions, and you order the electromagnetic spectrum from radio waves to gamma rays without hesitation.

**Core facts**

Avogadro's number, 6.022 × 10^23, is the number of atoms in one gram-atomic mass. Atoms per gram of an element = 6.022 × 10^23 / A, where A is the atomic (or molecular) mass in grams per mole. Electrons per gram = atoms per gram × Z (or the total electrons per molecule for a compound). Because Z/A is about 0.5 for most light elements and about 1 for hydrogen, hydrogen-rich materials (water, fat) have more electrons per gram than muscle or bone. Compton interactions scale with electrons per gram, which is why fat has a slightly higher electron density per gram than muscle even though its physical density is lower, and why electron density per cubic centimeter (what the dose engine wants) is electrons per gram times physical density.

Water: molecular mass 18, ten electrons per molecule. Electrons per gram = 6.022 × 10^23 × 10 / 18 = 3.34 × 10^23. Electron density of water per cubic centimeter is the same number because the density is 1 g/cm^3. The planning system's relative electron density table is referenced to this value.

Planck's relation: E = hν, with h = 6.626 × 10^−34 J·s = 4.136 × 10^−15 eV·s. Combined with c = λν this gives E = hc/λ, and in exam units E (keV) = 12.4 / λ (Å), equivalently λ (nm) = 1.24 / E (keV). Energy rises with frequency and falls with wavelength.

Electromagnetic spectrum in order of increasing frequency and energy (decreasing wavelength): radio, microwave, infrared, visible (about 700 nm red to 400 nm violet), ultraviolet, x-rays, gamma rays. The ionizing boundary is in the ultraviolet, roughly 10–12 eV, which is the ionization energy of oxygen and hydrogen in tissue. Linac microwaves at about 3 GHz have photon energies of a few tens of micro-electron-volts, so RF leakage is a heating hazard, never an ionization hazard. X-rays and gamma rays overlap in energy; the name follows origin (electron shell or bremsstrahlung versus nucleus), not energy.

**Formulas**

Atoms per gram = N_A / A

Electrons per gram = N_A × Z / A

E = hν = hc/λ; E (keV) = 12.4 / λ (Å)

**Worked example**

Given: a linac waveguide runs at 3.0 GHz. Find the photon energy of that RF in electron-volts and the wavelength.

Formula: E = hν with h = 4.136 × 10^−15 eV·s. λ = c/ν.

Substitution: E = 4.136 × 10^−15 × 3.0 × 10^9. λ = 3.0 × 10^8 / 3.0 × 10^9.

Arithmetic: E = 1.24 × 10^−5 eV, about 12 micro-electron-volts. λ = 0.10 m = 10 cm.

Meaning: the RF that accelerates electrons to 6 MeV carries about a hundred-thousandth of an electron-volt per photon and cannot ionize anything. The 10 cm wavelength is why S-band accelerator cavities are a few centimeters across.

Second example: a 1.24 MeV gamma ray. λ (Å) = 12.4 / 1240 keV = 0.010 Å = 1.0 × 10^−12 m. Check: 12.4 / 0.010 = 1240 keV.

Usual wrong turn: using h in J·s and forgetting to divide by 1.6 × 10^−19 to reach eV, which leaves 2 × 10^−24 "eV" that is really joules. Or using 12.4 with wavelength in nanometers instead of angstroms, a factor-of-ten error.

**Traps**

Multiplying by Avogadro's number instead of dividing when asked for atoms per gram. Forgetting the Z factor for electrons. Ordering the spectrum by wavelength and calling it energy order (they run opposite ways). Claiming microwaves or visible light are ionizing. Assigning x-ray versus gamma by energy.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Attix for electron densities. Public blueprint I.1, I.2 and I.3.
