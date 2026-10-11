# Module 9 — Radiation Measurement

Original items on kerma, dose, exposure, and the depth-dose ratios.

## KERMA vs. Absorbed Dose

### Q1
Stem: Kerma is:
A. The kinetic energy transferred to charged particles per unit mass
B. The energy absorbed per unit mass at the point of interest, with no further distinction
C. Exposure measured in sievert
D. Activity per unit mass
Answer: A
Objective: I.10
Why: Kerma (kinetic energy released per unit mass) scores the energy handed to charged particles at that point. Absorbed dose scores energy actually imparted, which those charged particles may deposit somewhere else. The sievert is equivalent dose. Activity per mass is specific activity.

### Q2
Stem: For a megavoltage photon beam, kerma is highest at the surface, but absorbed dose peaks at dmax. Why?
A. Secondary electrons travel downstream before they deposit their energy, so electronic equilibrium is not present at the surface.
B. Kerma includes only neutrons.
C. Absorbed dose cannot exceed kerma at any depth, so the curves never cross.
D. The surface dose is higher than dmax for 6 MV in tissue.
Answer: A
Objective: I.10
Why: Photons set electrons in motion, and those electrons carry energy a finite distance. At the surface the electrons have not yet built up, so dose is low while kerma is high. Past dmax, transient equilibrium holds and the dose curve follows kerma, shifted slightly downstream. For 6 MV, dose at the surface is lower than dose at dmax, which is the skin-sparing effect.

### Q3
Stem: Under charged-particle equilibrium, absorbed dose and collision kerma are equal. Electronic equilibrium fails in which situation?
A. A small 15 MV field in lung, where electrons can leave the field laterally
B. The center of a large Co-60 field, well beyond dmax, in uniform water
C. A calibration at the TG-51 depth in a broad beam in water
D. A point on the central axis of a 30 × 30 cm 6 MV field at 10 cm depth in water
Answer: A
Objective: I.10
Why: Lateral electronic disequilibrium is the small-field, high-energy, low-density problem: electrons scatter out of the field and are not replaced. Broad fields in uniform water, past buildup, are the geometry where transient equilibrium is a fair assumption. That includes a standard calibration depth and a large 6 MV field at 10 cm.

### Q4
Stem: Exposure is defined for:
A. Photons in air
B. Neutrons in tissue
C. Any particle, as a synonym for absorbed dose
D. Protons at the Bragg peak
Answer: A
Objective: I.10
Why: Exposure is ionization produced in air by photons (historically up to a few MeV). It is not defined for neutrons or protons, and it is not a synonym for absorbed dose in tissue. The unit is the roentgen or C/kg, not the gray.

### Q5
Stem: The f-factor converts exposure to absorbed dose. In the diagnostic energy range it is larger for bone than for muscle because:
A. Photoelectric absorption raises the energy absorbed in high-Z bone per roentgen
B. Bone has a lower density than air
C. The f-factor is 1.44 for every material
D. Exposure is defined only inside bone
Answer: A
Objective: I.10
Why: Absorbed dose per unit exposure depends on (μen/ρ) of the medium relative to air. At diagnostic energies the photoelectric effect makes that ratio large for bone. At megavoltage energies the f-factor for bone and muscle is much closer because Compton scatter tracks electron density. 1.44 is the mean-life factor, not an f-factor.

## Radiation Measurement

### Q1
Stem: A Bragg–Gray cavity relates the dose in the medium to the dose in a small gas cavity by:
A. The mass stopping-power ratio of medium to gas
B. The mass attenuation coefficient only
C. The decay constant of the wall
D. The Hounsfield number of the gas
Answer: A
Objective: I.10
Why: Under Bragg–Gray conditions the cavity does not disturb the electron fluence, and dose in the medium is the dose in the gas times the stopping-power ratio. Attenuation coefficients convert photon fluence to kerma. They are the wrong ratio for a cavity. Decay constants and HU do not enter the cavity relation.

### Q2
Stem: An in-air output measurement of a Co-60 beam uses a buildup cap. The cap is there to:
A. Establish electronic equilibrium at the chamber so the reading represents the collision kerma at that point
B. Flatten the beam
C. Remove the inverse-square dependence
D. Convert the reading from gray to becquerel
Answer: A
Objective: I.10
Why: Without buildup, the chamber wall is too thin for megavoltage electrons and the reading is low. The cap supplies equilibrium. It does not flatten the beam, cancel inverse square, or change the quantity from dose to activity.

### Q3
Stem: A free-air chamber is a primary standard for exposure. A Farmer-type thimble chamber in a clinic is:
A. A secondary instrument calibrated against a standard
B. A primary standard that does not need a calibration coefficient
C. Used only for neutron surveys
D. Unable to measure photons
Answer: A
Objective: I.10
Why: Clinic ion chambers carry a calibration coefficient from an accredited lab. They are not primary standards. Farmer chambers measure photons (and, with the right setup, electrons). Neutron survey meters are a different detector.

### Q4
Stem: Temperature-pressure correction is applied to an unsealed ion chamber because:
A. The mass of air in the cavity changes with air density, and the reading must be referred to 22 °C and 101.33 kPa (or the lab’s stated reference)
B. The photon energy changes with room temperature
C. Sealed monitor chambers in the linac head need the same daily correction
D. PDD tables are stored at 760 mm Hg only
Answer: A
Objective: I.10
Why: An unsealed cavity contains less air when the room is hot or the pressure is low, so the raw reading changes even if the dose does not. The correction puts the reading back to the calibration atmosphere. Linac monitor chambers are sealed. PDD is a ratio and is not a pressure table.

### Q5
Stem: Which detector statement is correct?
A. A diode is small and sensitive, but its reading is energy dependent and it can accumulate radiation damage.
B. A diode is a primary calorimeter.
C. Thermoluminescent dosimeters report the dose while the beam is on, with no readout step.
D. Radiographic film is independent of energy and processing.
Answer: A
Objective: I.10
Why: Diodes are convenient for patient measurements and small fields, with the stated limitations. A calorimeter measures temperature rise and is a primary dose method, not a diode. TLD stores the signal until it is heated. Film depends on energy, batch, and processing.

## TAR, TPR, TMR and More

### Q1
Stem: Percent depth dose, tissue-air ratio, and tissue-maximum ratio are distinguished by their reference dose. Which pairing is correct?
A. PDD is normalized to dmax at a fixed SSD. TAR is normalized to dose in free space at the same point. TMR is normalized to dmax at the same point.
B. PDD is independent of SSD, and TMR is defined only at a fixed SSD of 80 cm.
C. TAR is normalized to dmax, and TMR is normalized to free space.
D. All three are identical at every depth.
Answer: A
Objective: I.10
Why: PDD = 100 × dose(depth) / dose(dmax) along a fixed-SSD ray, so it changes with SSD. TAR = dose in phantom / dose in free space at the same point, and it does not depend on SSD. TMR = dose at depth / dose at dmax for the same point-to-source distance. Swapping the TAR and TMR denominators is the usual mix-up.

### Q2
Stem: An isocentric plan places the calculation point at the isocenter, 12 cm deep, with the gantry rotating at constant SAD. The depth table that matches this geometry without an extra SSD correction is:
A. TMR or TPR
B. A PDD table measured at 100 cm SSD, used with no Mayneord factor even though the SSD changes with the gantry angle
C. Backscatter factor alone
D. Exposure in roentgen
Answer: A
Objective: I.10
Why: At fixed SAD the inverse-square distance to the point stays constant, which is the TMR/TPR definition. A single SSD PDD table does not describe every gantry angle of an SAD setup. Backscatter factor is only TAR at dmax. Exposure is not a phantom depth-dose ratio.

### Q3
Stem: A fixed-SSD treatment is set up at 110 cm SSD. The only PDD table in the book was measured at 100 cm SSD. Which statement is correct?
A. PDD at the longer SSD is a bit higher. Mayneord’s F factor estimates that change by inverse square alone and does not correct for the change in scatter.
B. PDD does not depend on SSD, so the 100 cm table is exact at 110 cm.
C. TMR must be used, because PDD is undefined above 100 cm.
D. Mayneord’s factor includes a full scatter correction, so it is exact for large fields at low energy.
Answer: A
Objective: I.10
Why: Increasing SSD moves dmax and the depth point farther from the source by different amounts, so the inverse-square penalty at depth is smaller and PDD rises. Mayneord’s F is only that inverse-square ratio. Scatter also changes, and the approximation is poorer for large fields and lower energies. PDD is defined at any SSD.

### Q4
Stem: TMR at dmax equals 1 by definition. TAR at dmax equals the backscatter factor, which for a large Co-60 field is:
A. Greater than 1, because scatter from the phantom adds dose that was not present in free space
B. Exactly 0
C. Equal to the PDD at 10 cm
D. Less than 1, because backscatter removes photons
Answer: A
Objective: I.10
Why: BSF = dose at dmax in phantom / dose in free space at the same point = TAR(dmax). Scatter from surrounding phantom increases the dose, so BSF > 1. It is not zero, not the 10 cm PDD, and backscatter does not reduce the dose at dmax.

### Q5
Stem: If the reference depth used for TPR is exactly dmax, then for the same field-size convention:
A. TPR equals TMR
B. TPR equals PDD
C. TPR equals the inverse square factor only
D. TPR is undefined
Answer: A
Objective: I.10
Why: TPR is dose at depth divided by dose at a reference depth, both at the same distance from the source. Choosing that reference depth to be dmax makes the denominator the TMR denominator, so TPR = TMR. PDD uses a fixed SSD and a different inverse-square relationship. TPR remains defined.

### Q6
Stem: Collimator scatter factor Sc and phantom scatter factor Sp are separated because:
A. Sc follows the jaw opening that the head scatters into the monitor chamber path. Sp follows the tissue volume actually irradiated, including blocks and MLC.
B. Sc is the patient contour and Sp is the half-life.
C. They are always equal, so either field size can be used for both.
D. Sp is measured in air with a buildup cap and Sc is measured at 10 cm depth.
Answer: A
Objective: I.10
Why: Head scatter depends on how far the jaws are open. Phantom scatter depends on the field size at the patient after blocking. Using the jaw field for both, or the blocked field for both, mis-assigns one of the two. The in-air measurement with a buildup cap is Sc (and related output), not Sp. Percent of area blocked is not a full substitute for Sp, because shape and location of the block change the scatter.

## Radiation Measurement Quiz

### Q1
Stem: A fixed-SSD calculation gives 200 cGy at dmax. PDD at the prescription depth is 67%. The dose at that depth is:
A. 134 cGy
B. 200 cGy
C. 299 cGy
D. 67 cGy
Answer: A
Objective: I.10
Why: Dose(depth) = dose(dmax) × PDD/100 = 200 × 0.67 = 134 cGy. 299 cGy divides 200 by 0.67, which inverts the definition. 67 cGy drops the 200 cGy reference. 200 cGy would be correct only at dmax, where PDD is 100%.

### Q2
Stem: An isocentric dose of 150 cGy is delivered at a point where TMR is 0.750. The dose at dmax, at the same distance from the source, is:
A. 200 cGy
B. 112.5 cGy
C. 150 cGy
D. 225 cGy
Answer: A
Objective: I.10
Why: TMR = dose(depth) / dose(dmax), so dose(dmax) = 150 / 0.750 = 200 cGy. 112.5 cGy multiplies 150 × 0.75, which is the depth dose you would get if 150 cGy were already the dmax dose. 225 cGy multiplies by 1.50. Leaving the dose at 150 cGy ignores the TMR.

### Q3
Stem: A candidate uses a TMR of 0.80 in a fixed-SSD extended-distance calculation where the correct tool was the PDD, Mayneord-corrected to the treatment SSD. The mistake is:
A. Using an SAD quantity for an SSD setup
B. Using the half-life where the mean life belongs
C. Confusing photoelectric absorption with Compton scatter
D. Reporting magnification instead of field size
Answer: A
Objective: I.10
Why: TMR already refers to a constant distance from the source to the point. PDD refers to a constant distance from the source to the surface. They are not interchangeable without a conversion. The other options are real exam traps, but they are not this setup error.

### Q4
Stem: Mayneord’s F factor is applied to a PDD. What does it change, and what does it leave out?
A. It changes the inverse-square part of PDD when SSD changes. It leaves scatter uncorrected.
B. It changes only scatter, and it leaves inverse square uncorrected.
C. It converts TMR into activity.
D. It is exact for every field size because scatter is included.
Answer: A
Objective: I.10
Why: F = [(SSD2 + dmax)/(SSD1 + dmax)]^2 × [(SSD1 + d)/(SSD2 + d)]^2. Both factors are distances. There is no scatter term. Calling it exact for large low-energy fields overstates the approximation.

### Q5
Stem: A narrow-beam μ is 0.1155 cm^−1. The half-value layer is:
A. 6.0 cm
B. 8.7 cm
C. 0.080 cm
D. 20 cm
Answer: A
Objective: I.10
Why: HVL = 0.693 / μ = 0.693 / 0.1155 = 6.0 cm. 8.7 cm is the mean free path, 1/0.1155. 0.080 cm is 0.693 × 0.1155, the product instead of the quotient. 20 cm is about a tenth-value layer (2.30 / 0.1155 ≈ 19.9 cm), not a half-value layer.
