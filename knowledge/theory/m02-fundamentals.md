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
