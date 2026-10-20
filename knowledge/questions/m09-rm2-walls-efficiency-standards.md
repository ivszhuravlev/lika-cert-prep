# Module 9. Radiation Measurement

Original items. Chamber wall and cap materials, converting a count rate to an activity through counting efficiency, TG-51 and its international counterpart, and Fricke chemical dosimetry.

## Chamber Walls, Counting Efficiency, Protocols and Chemical Dosimetry

### Q1
Stem: Which material is used as the build-up cap and phantom for a Farmer chamber but is not used as the collecting wall because it is an electrical insulator?
A. Graphite
B. C-552 air-equivalent plastic
C. A-150 tissue-equivalent plastic
D. PMMA (acrylic)
Answer: D
Objective: I.10
Why: PMMA is nearly water-equivalent and cheap, so it is the standard cap and solid-phantom material, but the wall of an ionization chamber must conduct to define the collecting field, and acrylic does not unless it is coated. Graphite is the classic conductive Farmer wall. C-552 is a conductive air-equivalent plastic used for walls and electrodes. A-150 is a conductive tissue-equivalent plastic chosen when the hydrogen content matters, as in neutron and proton dosimetry.

### Q2
Stem: A wipe is counted on a pancake probe with 20% counting efficiency. The gross reading is 480 counts per minute and the background is 40 counts per minute. What is the removable activity on the wipe?
A. 88 dpm
B. 2,400 dpm
C. 2,200 dpm
D. 11,000 dpm
Answer: C
Objective: VII.3
Why: Net count rate = 480 − 40 = 440 cpm; activity = net cpm / efficiency = 440 / 0.20 = 2,200 dpm, which is 36.7 Bq or about 0.001 µCi and sits exactly at the removable-contamination trigger for a received package (2,200 dpm per 100 cm²). Check: 2,200 × 0.20 = 440. 88 dpm multiplies by the efficiency instead of dividing. 2,400 dpm forgets to subtract background. 11,000 dpm is the sealed-source leak-test limit (0.005 µCi), a different number.

### Q3
Stem: Which protocol is the international equivalent of AAPM TG-51 for reference dosimetry of megavoltage beams?
A. IAEA TRS-277, based on an air-kerma calibration factor
B. IAEA TRS-398, based on an absorbed-dose-to-water calibration factor
C. AAPM TG-21, based on a cavity-gas calibration factor
D. AAPM TG-61, based on an air-kerma calibration at kilovoltage energies
Answer: B
Objective: VII.3
Why: TRS-398 and TG-51 share the ND,w formalism and the kQ beam-quality correction, differing mainly in the photon quality specifier (TPR20,10 versus %dd(10)x) and in the extra kilovoltage, proton and ion chapters of TRS-398; they agree within about 1%. TRS-277 and TG-21 are the superseded air-kerma-based generation. TG-61 is the AAPM kilovoltage protocol, not a megavoltage counterpart.

### Q4
Stem: The Fricke dosimeter measures absorbed dose by:
A. Oxidation of ferrous to ferric ions in an acidic solution, read by ultraviolet absorbance
B. Thermally stimulated light emission from lithium fluoride crystals
C. Polymerization of a dye in a radiochromic film that darkens on exposure
D. Ionization of air in a cavity bounded by a graphite wall
Answer: A
Objective: I.10
Why: Fricke dosimetry is the classic chemical dosimeter: radiation converts Fe²⁺ to Fe³⁺ in ferrous sulfate solution with a yield of about 15.5 ions per 100 eV, and the ferric concentration is read spectrophotometrically at 304 nm. It is water-equivalent and absolute but useful only from roughly 40 to 400 Gy, so it served as a standard rather than a clinical tool. Option B is TLD, option C is radiochromic film, option D is an ionization chamber.

### Q5
Stem: Why is the build-up cap removed when a Farmer chamber is placed at 10 cm depth in a water phantom for a TG-51 output measurement?
A. The cap would short the collecting electrode to the wall under water
B. The phantom already provides charged-particle equilibrium, and the cap would add an unwanted material perturbation
C. The cap is only needed for electron beams, not photon beams
D. TG-51 requires the measurement to be made in air with the cap on
Answer: B
Objective: I.10
Why: The cap exists to supply build-up for in-air measurements at megavoltage energies; in a phantom the surrounding water does that job, and an acrylic cap would introduce a non-water material next to the cavity that the protocol does not correct for. The cap is an insulator, so it does not short anything. Electron beams in TG-51 are also measured in water without a cap. TG-51 is an in-phantom protocol by design.
