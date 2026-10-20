# Module 21. Radiobiology

Original items. Round 2 from the RM Review gap list: mitosis sub-phases and checkpoints, the Rubin-Casarett classes, multi-target model arithmetic, DNA as target, OER versus LET, chemical modifiers, and the fetal-dose workflow.

## Cell Cycle Checkpoints, Target Models, and Modifiers

### Q1
Stem: Chromosome aberrations for biological dosimetry are scored on spreads in which the chromosomes are lined up on the equatorial plate and maximally condensed. Which sub-phase of mitosis is this?
A. Prophase
B. Metaphase
C. Anaphase
D. Telophase
Answer: B
Objective: III.3
Why: In metaphase the chromosomes are aligned on the equatorial plate and are at their most compact, so dicentrics and rings are counted on metaphase spreads. Prophase is condensation and breakdown of the nuclear envelope. Anaphase is the separation of sister chromatids to the poles, and telophase is re-formation of the nuclear envelopes before cytokinesis.

### Q2
Stem: A population of tumor cells with mutant p53 is irradiated. In which phase do the cells accumulate afterward, and why?
A. In G1, because the restriction point arrests damaged cells
B. In S, because replication cannot start with damaged DNA
C. In anaphase, because the spindle checkpoint fails
D. In G2, because the G2/M checkpoint still arrests damaged cells even when p53 is lost
Answer: D
Objective: III.3
Why: The G2/M checkpoint verifies that DNA is replicated and undamaged before mitosis and is largely p53-independent, so irradiated cells accumulate there in the classic G2 block of roughly 1 to 2 hours per gray. The G1/S arrest is p53-dependent and is lost in p53-mutant tumors, so those cells do not stop in G1. Cells do not arrest in S or anaphase as the primary radiation response.

### Q3
Stem: In the Rubin-Casarett classification, which population is the most radiosensitive, and which cells belong to it?
A. Vegetative intermitotic cells, such as intestinal crypt cells, basal epidermal cells, and erythroblasts
B. Fixed postmitotic cells, such as neurons and muscle fibers
C. Reverting postmitotic cells, such as hepatocytes and renal tubular cells
D. Multipotential connective tissue cells, such as fibroblasts and endothelium
Answer: A
Objective: III.3
Why: Vegetative intermitotic cells divide constantly, are undifferentiated, and are short-lived stem cells, which makes them the most sensitive class; crypt cells, basal cells, erythroblasts, and type A spermatogonia belong here. Fixed postmitotic cells never divide and are the most resistant. Reverting postmitotic cells are relatively resistant, and multipotential connective tissue cells are intermediate.

### Q4
Stem: Which Rubin-Casarett class is the least radiosensitive, and what is its defining property?
A. Differentiating intermitotic cells, because they are already specializing
B. Vegetative intermitotic cells, because they are short-lived
C. Fixed postmitotic cells, because they never divide and are fully differentiated
D. Reverting postmitotic cells, because they divide only after injury
Answer: C
Objective: III.3
Why: Fixed postmitotic cells such as neurons, muscle fibers, erythrocytes, and spermatozoa never divide and are fully differentiated, so they are the most resistant class. Reverting postmitotic cells such as hepatocytes are relatively resistant but can be recruited to divide and are one step more sensitive. Differentiating intermitotic cells are sensitive, and vegetative intermitotic cells are the most sensitive of all.

### Q5
Stem: A survival curve fitted with the multi-target model has a quasi-threshold dose of 2 Gy and a D0 of 1.5 Gy. What is the extrapolation number?
A. 1.3
B. 2.1
C. 3.8
D. 7.4
Answer: C
Objective: III.3
Why: The parameters are linked by Dq = D0 × ln(n), so ln(n) = 2 / 1.5 = 1.333 and n = e^1.333 = 3.8. Check: 1.5 × ln(3.8) = 1.5 × 1.335 = 2.0 Gy. The value 1.3 is the ratio Dq / D0 left without exponentiating. The value 2.1 is e raised to the inverted ratio 0.75, and 7.4 is e raised to 2, the quasi-threshold in gray with the D0 forgotten.

### Q6
Stem: A cell line has an extrapolation number of 4 and a D0 of 1.2 Gy on the multi-target model. What is the quasi-threshold dose?
A. 4.8 Gy
B. 1.66 Gy
C. 0.72 Gy
D. 0.30 Gy
Answer: B
Objective: III.3
Why: Dq = D0 × ln(n) = 1.2 × ln(4) = 1.2 × 1.386 = 1.66 Gy. Check: ln(n) = 1.66 / 1.2 = 1.386 and e^1.386 = 4.0. The value 4.8 Gy multiplies n by D0 without the logarithm. The value 0.72 Gy uses the base-10 logarithm of 4, which is 0.602. The value 0.30 Gy divides D0 by n.

### Q7
Stem: Which statement about the base pairs of the DNA target is correct?
A. Adenine pairs with guanine and thymine with cytosine
B. Adenine pairs with cytosine through three hydrogen bonds
C. Guanine pairs with thymine through two hydrogen bonds
D. Adenine pairs with thymine through two hydrogen bonds, and guanine with cytosine through three
Answer: D
Objective: III.3
Why: Adenine pairs with thymine with two hydrogen bonds and guanine pairs with cytosine with three, so the sequence on one strand fixes the complementary strand and the two sugar-phosphate backbones run antiparallel. Purine-to-purine pairing such as adenine with guanine does not occur in the double helix. The other combinations are not complementary pairs. The halogenated pyrimidines that sensitize cells substitute specifically for thymidine.

### Q8
Stem: What is the approximate oxygen enhancement ratio for fast neutrons, and how does it compare with photons and with alpha particles?
A. About 1.6, between the 2.5 to 3 of photons and the value near 1 for alpha particles
B. About 3, the same as photons, because neutrons are uncharged
C. About 1, the same as alpha particles, because both are high LET
D. About 5, higher than photons, because neutrons produce recoil protons
Answer: A
Objective: III.3
Why: The OER falls as linear energy transfer rises: 2.5 to 3 for low-LET x-rays, gamma rays, and electrons; about 1.6 for fast neutrons of intermediate LET; and about 1 for alpha particles and heavy ions above roughly 100 keV per micrometer, where dense direct damage no longer needs oxygen fixation. Neutrons are uncharged but deposit dose through recoil protons of intermediate LET, so they sit in the middle, not at either extreme, and no radiation has an OER above the photon value.

### Q9
Stem: Which agent in the following list is a radioprotector rather than a radiosensitizer, and what is its mechanism?
A. Cisplatin, which forms platinum adducts and blocks double-strand break repair
B. Gemcitabine, which depletes deoxynucleotide pools
C. Amifostine, a thiol prodrug activated by alkaline phosphatase in normal tissue that scavenges free radicals
D. Hydroxyurea, which inhibits ribonucleotide reductase and synchronizes cells at G1/S
Answer: C
Objective: III.3
Why: Amifostine, WR-2721, is dephosphorylated in normal tissue capillaries to the free thiol WR-1065, which scavenges radicals and donates hydrogen to DNA radicals; tumors take up less because they are hypoxic, acidic, and low in alkaline phosphatase. It is given 15 to 30 minutes before each fraction to reduce xerostomia. Cisplatin, gemcitabine, and hydroxyurea are all concurrent radiosensitizers, as is 5-fluorouracil.

### Q10
Stem: A Hodgkin lymphoma patient completed chemotherapy and is scheduled for mediastinal radiation. Which of the following drug groups most raises the risk of radiation pneumonitis?
A. Vincristine and prednisone
B. Bleomycin, gemcitabine, doxorubicin, and actinomycin-D
C. Rituximab and dexamethasone
D. Tamoxifen and leucovorin
Answer: B
Objective: III.3
Why: Bleomycin causes pulmonary fibrosis on its own and compounds pneumonitis after mediastinal radiation; gemcitabine is a potent sensitizer that should not be given concurrently with or shortly after thoracic radiation; doxorubicin and actinomycin-D produce recall reactions in previously irradiated lung and skin. Vincristine, prednisone, rituximab, dexamethasone, tamoxifen, and leucovorin do not add meaningfully to lung toxicity.

### Q11
Stem: Why does hyperthermia at 42 to 45 degrees Celsius complement radiotherapy rather than merely duplicate it?
A. Heat is most lethal to cells in mitosis, the same cells radiation kills best
B. Heat reoxygenates the tumor, so it only works on well-oxygenated cells
C. Heat raises the oxygen enhancement ratio and sensitizes only aerobic cells
D. Heat kills S-phase cells and hypoxic, acidic, nutrient-deprived cells, which are the radioresistant populations, and inhibits repair of sublethal damage
Answer: D
Objective: III.3
Why: Heat is most lethal to S-phase cells, the most radioresistant phase, and to hypoxic, acidic, and poorly nourished cells in the tumor cord, which radiation spares; it also blocks repair of sublethal and potentially lethal damage, giving a thermal enhancement ratio of about 1.5 to 2 when heat follows radiation within hours. Mitotic cells are radiation's best targets, not heat's special targets. Heat does not act through oxygen and does not raise the OER.

### Q12
Stem: A pregnant patient needs radiotherapy to the head and neck. Which sequence of physics steps is correct, and what is the fetal dose goal?
A. Estimate the fetal dose from tables or phantom measurement, then design the lead shield and plan modifications, then verify with dosimeters on the abdomen; keep the fetal dose well under 0.1 Gy
B. Build a lead bridge first, then estimate the dose at the first fraction; keep the fetal dose under 1 Gy
C. Omit shielding because head and neck fields are far from the fetus; keep the fetal dose under 0.5 Gy
D. Use physical wedges and 18 MV beams to shorten the course; keep the fetal dose under 0.2 Gy
Answer: A
Objective: III.3
Why: Task Group 36 orders the work as estimate, then modify and shield, then verify: the out-of-field dose is read from TG-36 tables or measured in a phantom, the plan is changed to energy below 10 MV, no physical wedges or trays, tight collimation and beams away from the fetus, a 4 to 5 cm lead bridge on a frame cuts leakage and head scatter by a factor of three to four, and dosimeters on the abdomen confirm the result. The goal is a total well under 0.1 Gy, the lowest dose at which deterministic effects on the conceptus are considered. Shielding before estimating risks protecting against the wrong component, and 18 MV adds photoneutrons.
