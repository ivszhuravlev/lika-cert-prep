# Module 41. Radiation Protection

Original items. Written for the RM Review porting wave; gaps in transport rules, source and waste regulations, NCRP 147/151 design numbers, and background dose.

## Transport of Radioactive Material: DOT Labels, Transport Index, and Package Types

### Q1
Stem: A survey meter held 1 m from the surface of a package containing a gamma emitter reads 1.23 mR/h. What transport index goes on the label?
A. 0.13
B. 1.3
C. 1.2
D. 12.3
Answer: B
Objective: VI.2
Why: The transport index is the highest dose rate at 1 m in mrem/h, and the mR/h gamma reading is taken as mrem/h, rounded up to the next tenth: 1.23 becomes 1.3. Rounding down to 1.2 breaks the round-up rule. 0.13 divides by ten for no reason, and 12.3 multiplies by ten. Check: a TI of 1.3 is above 1, so this package is Yellow-III regardless of its surface reading.

### Q2
Stem: A package surface reads 35 mR/h and the reading 1 m from the surface is 0.9 mR/h. Which DOT label is correct?
A. White-I
B. Out of limits for ordinary transport
C. Yellow-II
D. Yellow-III
Answer: C
Objective: VI.1
Why: Yellow-II requires a surface reading of at most 50 mrem/h and a transport index above 0 and at most 1; 35 and 0.9 satisfy both. White-I would need a surface reading of at most 0.5 mrem/h and nothing measurable at 1 m. Yellow-III begins when the TI passes 1 or the surface passes 50 mrem/h. Out of limits means a surface reading above 200 mrem/h or a TI above 10, which this package is nowhere near.

### Q3
Stem: Treating a small package as a point source, a reading of 3.6 mR/h is taken at 50 cm from its surface. What transport index does the inverse-square estimate give for the 1 m reading?
A. 0.9
B. 1.8
C. 3.6
D. 7.2
Answer: A
Objective: VI.2
Why: Doubling the distance from 0.5 m to 1 m divides the dose rate by four: 3.6 / 4 = 0.9 mR/h, so the TI is 0.9. Dividing by two (1.8) uses the distance ratio instead of its square. Reporting 3.6 ignores the distance change, and 7.2 moves the wrong way. Check: 0.9 × 4 = 3.6, and 0.9 is already a tenth so no round-up changes it. A real shipper measures at 1 m rather than estimating, but the arithmetic shows why a surface or half-metre reading is not the TI.

### Q4
Stem: A sealed-source package arrives with a surface reading of 120 mR/h and a labelled transport index of 4.0. Which label should it carry?
A. White-I, because the source is sealed
B. Yellow-II, because the surface is under 200 mR/h
C. Yellow-III
D. It may not be shipped by ordinary carrier
Answer: C
Objective: VI.1
Why: Yellow-III covers a surface reading of at most 200 mrem/h together with a TI above 1 and at most 10; 120 and 4.0 fit. Being sealed has nothing to do with the label category. Yellow-II stops at 50 mrem/h on the surface and a TI of 1, and 120 exceeds the first while 4.0 exceeds the second. The package is within ordinary transport limits because the surface is under 200 mrem/h and the TI is under 10.

### Q5
Stem: In the shipping tables, what does the quantity A1 for a radionuclide represent?
A. The largest activity of special-form (sealed, non-dispersible) material allowed in a Type A package
B. The largest surface dose rate allowed on a Type A package
C. The largest transport index allowed on a Type A package
D. The largest activity of dispersible material allowed in a Type A package
Answer: A
Objective: VI.1
Why: A1 is the Type A activity limit for special-form material, which is a sealed source that cannot disperse. The limit for normal-form, dispersible material such as a liquid is A2, which is never larger than A1. Surface dose rate and transport index are label quantities measured on the package, not tabulated activity limits. Above A1 or A2 the shipment needs a Type B package.

### Q6
Stem: A replacement HDR source of 10 Ci of Ir-192 is shipped to a clinic. The A1 value for Ir-192 is about 27 Ci. Which package type does the shipment require?
A. Type B, because any source above 1 Ci is Type B
B. Type A, because 10 Ci is below the Ir-192 A1 value
C. An excepted package, because the source is sealed
D. Type C, because the source is for medical use
Answer: B
Objective: VI.1
Why: A sealed source is special form, so it is compared with A1, and 10 Ci is below 27 Ci, which permits a Type A package. There is no universal 1 Ci line; each nuclide has its own A1. An excepted or limited-quantity package applies only to a small fraction of A1, far below 10 Ci. There is no Type C category in clinical shipping, and medical use does not change the package type.

### Q7
Stem: What distinguishes a Type B package from a Type A package?
A. Type B carries only liquids
B. Type B is used whenever the transport index exceeds 1
C. Type B is any package with a Yellow-III label
D. Type B holds more than A1 or A2 and must survive accident tests such as a 9 m drop, a fire, and immersion
Answer: D
Objective: VI.1
Why: A Type B package is required when the contents exceed A1 (special form) or A2 (normal form), and its design is tested against accident conditions and certified by the NRC under 10 CFR 71. Type A is tested only against normal transport conditions such as a short drop, water spray, and stacking. Package type is decided by activity, not by physical form alone, and not by the label or the TI, which describe external dose rate. A Gamma Knife Co-60 reload of thousands of curies is the clinical example of Type B.

### Q8
Stem: Under 10 CFR 20.1906, when a labelled radioactive package is delivered during working hours, within what time must the licensee survey its surface and wipe it for removable contamination?
A. Within 3 hours of receipt
B. Within 24 hours of receipt
C. Before the next scheduled leak test
D. Only if the transport index is above 1
Answer: A
Objective: VI.2
Why: The receipt survey is due within 3 hours when the package arrives during normal working hours, and within 3 hours of the start of the next working day if it arrives after hours. Twenty-four hours is too long. The leak test is a routine on the clinic's own sealed sources and has nothing to do with package receipt. The survey is required for every labelled package, not only those with a measurable TI, and findings above the surface or contamination limits are reported to the carrier and the regulator.

## Sealed Sources, Contamination, Waste, and Patient Release Rules

### Q1
Stem: A semi-annual leak-test wipe of a Cs-137 tube counts out to 0.003 microcuries of removable activity. What is that in becquerels, and does the source pass?
A. 111 Bq, and it passes
B. 111 Bq, and it fails
C. 3,000 Bq, and it fails
D. 11.1 Bq, and it passes
Answer: A
Objective: VI.2
Why: One microcurie is 37,000 Bq, so 0.003 × 37,000 = 111 Bq, which is below the 185 Bq (0.005 microcurie) limit, so the source passes. Calling 111 Bq a failure compares it with the wrong side of the limit. 3,000 Bq treats 0.003 as if one microcurie were a million becquerels. 11.1 Bq drops a factor of ten. Check: the limit itself is 0.005 × 37,000 = 185 Bq, and 111 is about 60 percent of it.

### Q2
Stem: The removable-contamination trigger used for a received package is 2,200 disintegrations per minute per 100 square centimetres for beta-gamma emitters. What is that in becquerels per 100 square centimetres?
A. 2,200 Bq
B. 36.7 Bq
C. 132,000 Bq
D. 22 Bq
Answer: B
Objective: VI.2
Why: One becquerel is one disintegration per second, so 2,200 per minute is 2,200 / 60 = 36.7 Bq per 100 square centimetres, which is 0.37 Bq per square centimetre. 2,200 Bq forgets the minute-to-second conversion. 132,000 multiplies by 60 instead of dividing. 22 is the dpm per square centimetre figure, not becquerels. Check: 36.7 × 60 = 2,200.

### Q3
Stem: Contaminated gloves and vials from an I-131 therapy are held for decay-in-storage. With a half-life of 8.0 days, about how long is the ten-half-life holding time before the survey?
A. 8 days
B. 40 days
C. 80 days
D. 120 days
Answer: C
Objective: VI.1
Why: Ten half-lives is 10 × 8.0 = 80 days, after which about 1/1,024, or 0.1 percent, of the activity remains. Eight days is one half-life (50 percent left) and 40 days is five (about 3 percent left). One hundred twenty days is the longest half-life a nuclide may have to qualify for decay-in-storage at all, not a holding time. Check: 2 to the tenth power is 1,024. The bag is released by a survey that reads background with the meter unshielded, not by the calendar alone.

### Q4
Stem: What finally allows a decay-in-storage bag to go out as ordinary waste?
A. Reaching the date written on the bag
B. A wipe test under 185 Bq
C. A written directive from the authorized user
D. An unshielded survey that reads no higher than background, after which the radiation labels are removed or defaced
Answer: D
Objective: VI.1
Why: 10 CFR 35.92 releases decay-in-storage waste on a survey, taken with an appropriate meter and no shielding between the meter and the waste, showing nothing above background, followed by removal of the labels. The date is a planning estimate from the ten-half-life rule, not the release criterion. A 185 Bq wipe is the sealed-source leak-test limit and does not apply to open waste. A written directive is a prescription document for a therapy, not a waste step.

### Q5
Stem: A patient retains 33 mCi of I-131. Using an exposure-rate constant of 2.2 R per hour at 1 cm per mCi, what is the exposure rate at 1 m?
A. 0.73 mR/h
B. 7.3 mR/h
C. 73 mR/h
D. 726 mR/h
Answer: B
Objective: VI.2
Why: Exposure rate is the constant times activity divided by the distance squared: 2.2 × 33 / 100 squared = 72.6 / 10,000 = 0.00726 R/h, which is 7.3 mR/h. 0.73 and 73 are off by a factor of ten in each direction from a slipped decimal. 726 mR/h divides by 100 instead of 100 squared. Check: 7.3 mR/h at 1 m is the published dose-rate release value that matches the 33 mCi activity value for I-131, which is why both appear as teaching numbers.

### Q6
Stem: After I-131 therapy a patient reads 6.0 mR/h at 1 m. Take the effective half-life as the 8.0 day physical half-life, an occupancy factor of 0.25 for the household member, and 1 mR as 0.01 mSv. Estimate the total dose to that person and the release decision under 10 CFR 35.75.
A. 4.1 mSv, release with written instructions
B. 2.9 mSv, release with no instructions needed
C. 16.6 mSv, keep the patient
D. 41 mSv, keep the patient
Answer: A
Objective: VI.1
Why: Total dose is the initial rate times the mean life times occupancy: 1.44 × 8.0 × 24 = 276.5 hours, times 0.25 is 69.1 hours, times 6.0 mR/h is 415 mR, which is 4.1 mSv, under the 5 mSv limit, and above 1 mSv so written instructions are required. 2.9 mSv uses the half-life instead of the mean life (6 × 8 × 24 × 0.25 = 288 mR) and also wrongly skips the instructions. 16.6 mSv forgets the occupancy factor (6 × 276.5 = 1,659 mR). 41 mSv is a decimal slip. Check: 69.1 × 6 = 414.7.

### Q7
Stem: Which subject is governed by 10 CFR Part 19?
A. Transport labels and the transport index
B. Occupational and public dose limits
C. Sealed-source leak-test limits
D. Notices to workers, instruction about radiation risks, and the worker's right to dose reports and to speak with inspectors
Answer: D
Objective: VI.1
Why: Part 19 covers posting of the NRC notice to employees, keeping the license and regulations available, instructing workers on risks and ALARA and the right to declare a pregnancy, providing dose reports on request, and the right to request an inspection. Transport is Part 71 and the DOT rules. Dose limits are Part 20. Leak tests are Part 35 for medical licensees. Part 19 sets no numeric dose limit of its own.

### Q8
Stem: Why did a radium source safe require ventilation to the outdoors, a requirement that does not apply to an Ir-192 or Cs-137 safe?
A. Radium emits neutrons that activate the air in the safe
B. Ra-226 decays to radon gas, so a leaking needle fills the safe with radon and its daughters
C. Radium needles heat the safe and need cooling air
D. Radium gives off ozone through ionization of the air
Answer: B
Objective: VI.1
Why: Radium-226 decays to radon-222, a noble gas, so any leak released radon and its alpha-emitting daughters into the storage area; ventilation and a radon-emanation leak test were therefore required. Radium is not a neutron source and does not activate air. The heat from a few milligrams of radium is negligible. Ozone from ionization is a trivial effect and not the reason. The fact is historical; it is a distractor key on current exams because Ir-192 and Cs-137 decay to solids.

## NCRP 147 versus 151: Design Goals, Occupancy, Workloads, Doors, and Neutrons

### Q1
Stem: A radiation-oncology department is building a CT simulator room. Which shielding report applies to that room?
A. NCRP 151, because the room is in a therapy department
B. NCRP 147, because it is a kilovoltage imaging room
C. AAPM TG-108, because the scanner produces annihilation photons
D. NCRP 49, the current report for all medical rooms
Answer: B
Objective: VI.3
Why: NCRP 147 covers structural shielding for medical x-ray imaging, including CT, regardless of which department owns the scanner. NCRP 151 covers megavoltage therapy vaults; a CT simulator is not one. TG-108 is PET and PET/CT shielding, where the 511 keV photons come from the patient. NCRP 49 is the 1976 predecessor of both and is a legacy citation.

### Q2
Stem: Under NCRP 151, which pair gives the weekly shielding design goals for a controlled area and an uncontrolled area?
A. 0.1 mSv per week controlled and 0.02 mSv per week uncontrolled
B. 1 mSv per week controlled and 0.1 mSv per week uncontrolled
C. 0.02 mSv per week controlled and 0.1 mSv per week uncontrolled
D. 0.02 mSv in any hour for both
Answer: A
Objective: VI.3
Why: Controlled areas are designed to 0.1 mSv per week, about 5 mSv a year, and uncontrolled areas to 0.02 mSv per week, about 1 mSv a year, the public limit. One millisievert per week would be 50 mSv a year for the controlled area, the whole occupational limit. Option C swaps the two. The 0.02 mSv in any hour figure is the 10 CFR 20.1301 hourly cap for unrestricted areas, a separate check and not the weekly P.

### Q3
Stem: A primary barrier faces an unattended parking lot. Design goal 0.02 mSv per week, distance 6 m, workload 1,000 Gy per week at 1 m, use factor one quarter, occupancy 1/40, and a TVL of 35 cm for this concrete. How thick must the barrier be?
A. 148 cm
B. 194 cm
C. 138 cm
D. 159 cm
Answer: C
Objective: VI.3
Why: Convert the workload to 1,000,000 mSv per week so the units match P. Transmission B = 0.02 × 36 / (1,000,000 × 0.25 × 0.025) = 0.72 / 6,250 = 0.000115. The number of TVLs is log base ten of 1 / 0.000115, which is log of 8,680, or 3.94, and 3.94 × 35 = 138 cm. Using T = 1 instead of 1/40 gives B = 0.0000029, 5.54 TVL, and 194 cm. Using T = 1/20 gives 148 cm, and dropping the use factor (U = 1) gives 159 cm. Check: 10 to the 3.94 is about 8,700.

### Q4
Stem: A secondary wall is sized for head leakage in a controlled area. Design goal 0.1 mSv per week, distance 4 m, primary workload 400 Gy per week at 1 m, all IMRT with an IMRT factor of 4, leakage 0.1 percent, use factor 1, occupancy 1, leakage TVL 30 cm. What thickness does the leakage term require?
A. 72 cm
B. 90 cm
C. 120 cm
D. 180 cm
Answer: B
Objective: VI.3
Why: Leakage workload is 400 × 4 = 1,600 Gy per week; the leakage source at 1 m is 0.001 × 1,600 = 1.6 Gy per week, which is 1,600 mSv per week. B = 0.1 × 16 / 1,600 = 1.6 / 1,600 = 0.001, exactly 3 TVL, so 3 × 30 = 90 cm. Forgetting the IMRT factor gives B = 1.6 / 400 = 0.004, which is 2.4 TVL and 72 cm. 120 cm would be 4 TVL and 180 cm would be 6 TVL, neither of which the numbers produce. Check: 10 to the minus 3 is 0.001.

### Q5
Stem: When a vault is redesigned for an IMRT program, the IMRT factor multiplies which shielding term?
A. The primary-barrier workload only
B. Both the primary workload and the patient-scatter term
C. The leakage workload only
D. The occupancy factor of every adjacent room
Answer: C
Objective: VI.3
Why: IMRT delivers the same isocenter dose with several times the monitor units, and head leakage follows monitor units, so the leakage workload is the primary workload times the IMRT factor. The primary barrier sees the useful-beam dose at isocenter, which the IMRT factor does not change. Patient scatter also scales with the dose delivered to the patient, not with monitor units. Occupancy describes who is behind the wall and is untouched by the treatment technique.

### Q6
Stem: In the NCRP 151 occupancy table, which location carries an occupancy factor of 1/40?
A. A staff corridor
B. A receptionist desk
C. A public toilet
D. An unattended parking lot or an outdoor area with only transient traffic
Answer: D
Objective: VI.3
Why: The lowest tabulated occupancy, 1/40, belongs to unattended parking, outdoor areas with transient traffic, stairways, and janitor closets. Staff corridors are 1/5. A receptionist desk, offices, and nurse stations are fully occupied at 1. Public toilets, vending areas, and unattended waiting rooms are 1/20. Occupancy is a property of the protected point, not of the treatment room.

### Q7
Stem: A direct door is being built for an 18 MV vault. How are the borated polyethylene and the lead arranged, and why?
A. Borated polyethylene on the vault side to slow and capture neutrons, with lead outside it to absorb the capture gamma rays
B. Lead on the vault side to stop the neutrons, with polyethylene outside for the gamma rays
C. Lead only, because concrete walls already remove all neutrons
D. Polyethylene only, because the capture gamma rays are below 100 keV
Answer: A
Objective: VI.3
Why: Hydrogen in the polyethylene thermalizes the neutrons and the boron captures them with a 0.48 MeV gamma, so the polyethylene faces the vault; lead then sits outside to attenuate those capture gammas and the 2.2 MeV hydrogen-capture gammas from the walls. Lead is a poor neutron shield, so putting it first does nothing for the neutrons and places the capture gammas outside the gamma shield. Concrete reduces neutron fluence but a maze-less door at 18 MV still faces a large neutron component. The capture gammas are hundreds of keV to 2.2 MeV, so a polyethylene-only door would leak them.

### Q8
Stem: Which AAPM report addresses shielding for a PET/CT suite, and what makes that room different from a diagnostic x-ray room?
A. TG-142, because the scanner is checked daily
B. NCRP 147, because PET is an imaging modality
C. TG-51, because dose is calibrated in water
D. TG-108, because the 511 keV annihilation photons are far more penetrating than diagnostic x-rays and the injected patient is the source
Answer: D
Objective: VI.3
Why: TG-108 covers PET and PET/CT shielding; the source is the patient in the uptake room and the scanner room, and 511 keV photons need about a centimetre and a half of lead per tenth-value layer rather than the millimetre or so that stops diagnostic x-rays. NCRP 147 is kilovoltage imaging shielding and its transmission data do not apply to 511 keV. TG-142 is linac QA and TG-51 is beam calibration; neither is a shielding document.

## Background Radiation, Collective Dose, Biodosimetry, and Privacy

### Q1
Stem: According to NCRP Report 160, what is the average total annual effective dose to a person in the United States, and roughly how much of it is natural background?
A. About 3.1 mSv total, of which about 1 mSv is natural
B. About 1 mSv total, all of it natural
C. About 50 mSv total, of which 6.2 mSv is medical
D. About 6.2 mSv total, of which about 3.1 mSv is natural
Answer: D
Objective: VI.1
Why: NCRP 160 puts the total at about 6.2 mSv a year, split roughly in half between natural background (3.1 mSv, dominated by radon) and medical exposure (about 3 mSv, half of it CT). The older 3 mSv figure is the natural component alone, or a pre-CT-era total. One millisievert is the annual public limit from licensed operations, not background. Fifty millisieverts is the occupational limit.

### Q2
Stem: A department has 250 badged workers whose annual effective doses average 1.2 mSv. What is the collective effective dose?
A. 0.30 person-Sv
B. 300 person-Sv
C. 1.2 person-Sv
D. 208 person-Sv
Answer: A
Objective: VI.1
Why: Collective dose is the sum of individual doses: 250 × 1.2 mSv = 300 person-mSv, which is 0.30 person-Sv. Three hundred person-Sv forgets the millisievert-to-sievert conversion. 1.2 is the mean individual dose, not the collective dose. 208 divides 250 by 1.2 for no reason. Check: 0.30 person-Sv / 250 people = 0.0012 Sv = 1.2 mSv per person.

### Q3
Stem: Taking a chest radiograph as 0.1 mSv and an abdomen CT as 8 mSv, about how many chest radiographs equal one abdomen CT?
A. 8
B. 80
C. 800
D. 0.8
Answer: B
Objective: VI.1
Why: 8 / 0.1 = 80 chest radiographs per abdomen CT. Eight treats the chest film as 1 mSv, which is ten times too high. Eight hundred treats it as 0.01 mSv. 0.8 inverts the ratio. Check: 80 × 0.1 = 8. The same CT is about three years of natural background at 3.1 mSv a year and about one sixth of the 50 mSv occupational limit.

### Q4
Stem: A worker was exposed in an accident without a dosimeter. Which measurement estimates the whole-body dose from the worker's own body?
A. Reading the OSL badge of a nearby colleague
B. A thyroid uptake count
C. The frequency of dicentric chromosomes in cultured blood lymphocytes, read against a calibration curve
D. A skin-erythema score at 24 hours
Answer: C
Objective: VI.1
Why: Cytogenetic dosimetry counts dicentric chromosomes, which have two centromeres and are produced by misrepair of radiation-induced breaks; their yield rises with dose and detects acute whole-body doses down to roughly 0.1 to 0.2 Gy. A colleague's badge records the colleague's exposure. A thyroid count measures internal iodine, not external whole-body dose. Skin erythema appears only above several grey, days later, and reflects local skin dose, not whole-body dose.

### Q5
Stem: Which of these is a HIPAA problem even though the clinical content is correct?
A. Sending a plan to the treating physician for approval inside the record-and-verify system
B. Showing a de-identified DVH, with name and medical record number removed, at a teaching conference
C. Billing the payer for the planning charge
D. Texting a screenshot of the plan, with the patient's name visible, to a colleague's personal phone for an opinion
Answer: D
Objective: VI.1
Why: A named screenshot on a personal phone discloses protected health information outside the safeguards of the Security Rule and beyond the minimum necessary, so it is a Privacy and Security Rule problem regardless of clinical intent. Use within treatment, payment, and health-care operations is permitted without authorization, which covers physician approval in the clinical system and billing. A properly de-identified teaching example is no longer PHI. The rule protects identifiable information, not the dose numbers themselves.

### Q6
Stem: Which single source contributes the most to natural background dose in the United States?
A. Cosmic rays at sea level
B. Terrestrial gamma rays from soil and building materials
C. Radon and thoron decay products inhaled indoors
D. Potassium-40 inside the body
Answer: C
Objective: VI.1
Why: Radon and thoron account for roughly 2 mSv of the 3.1 mSv natural component in NCRP 160, about two thirds of natural background and about a third of the 6.2 mSv total. Cosmic, terrestrial, and internal emitters each contribute a few tenths of a millisievert. Radon dose is delivered by alpha particles to the bronchial epithelium, which is why its equivalent dose to lung is large relative to the effective dose.
