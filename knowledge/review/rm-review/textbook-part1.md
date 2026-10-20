# Review of Medical Dosimetry (Amestoy, Springer 2015) — Part 1 coverage report

Scope: book start through PDF page 440 (printed page 424). That is Chapter 1 (Radiation Physics), Chapter 2 (Dose Calculation Methods), Chapter 3 (Treatment Planning), Chapter 4 (Patient Immobilization), Chapter 5 (Brachytherapy) in full, and Chapter 6 (Radiobiology) questions §6.1–6.3 plus the start of §6.4. Chapter 6 answers and the three 155-item practice tests are in Part 2.

Method: every section was read in order; our bank (`knowledge/theory`, `knowledge/questions`, 45 modules, ~1,944 items) was grepped for the key terms and numbers of each section. Facts below are restated in my own words. The source file is copyrighted and stays in `inbox/`.

Format of the book: pure Q&A. Each chapter has a run of question sections followed by matching answer sections. Items are 4-option MCQ, 5-option "I, II, III, IV" multi-truth items (very heavy use, roughly a third of items), matching lists, and calculation items with worked solutions. Difficulty is tagged Level 1–3. Front matter claims an MDCB pass rate near 57%.

Classification key: COVERED = our bank teaches the same facts at the same or better depth. PARTIAL = topic present but specific facts/numbers below are absent. MISSING = topic essentially absent from the bank.

---

## Chapter 1 — Radiation Physics (pp. 1–108, ≈295 questions)

### 1.1 Atomic and nuclear structure, radioactivity (≈56 Q; answers §1.7)
**Covers:** atom/nucleus constituents, masses and rest energies, shells and binding energy, nuclide classification, decay modes, equilibrium, half-life/mean life, historical discoverers.
**Bank status:** PARTIAL (m02, m03 cover structure, classification, decay math, equilibrium well).
**Facts the book has that we lack:**
- 1 amu = 1.66×10⁻²⁷ kg = 931 MeV; proton 938 MeV/c², neutron 939, electron 0.511 (bank has 0.511 and 931 in a few places but no table of nucleon masses in amu: n 1.00866, p 1.00727, e 0.000548).
- 2n² maximum electrons per shell; subshell capacities s2/p6/d10/f14; binding energy of inner shells scales roughly with Z².
- Avogadro's number 6.02×10²³; atoms per gram = N_A/A_w; electrons per gram = N_A·Z/A_w (bank uses electron density conceptually but never the formula).
- Even-even nuclei most stable; odd-odd least.
- Dates: Roentgen 1895, Becquerel 1896, Curies 1898, Bohr model 1913.
- Cs-137 → Ba-137m (2.55 min isomeric transition) as the gamma source.
- Rule of thumb: transient equilibrium reached after ~4 daughter half-lives, secular after ~6; time-to-maximum-daughter formula.
- Effective half-life T_eff = T_p·T_b/(T_p+T_b) (bank mentions effective half-life in 3 files; check that the formula is there).
- Co-60 decay constant 0.1317/yr, mean life 7.57 yr, output loss ≈1.09%/month (bank has ~1%/month).
**Errors/outdated:** valence electrons described as the lowest energy level (should be outermost); gravity stated as 36 times weaker than EM (should be ~10³⁶); Planck constant typo (6.62×10⁻²³).
**Question types:** heavy matching (nuclide ↔ half-life ↔ Γ ↔ energy), many "I–IV" truth items, a few decay calculations. Our m03 has 78 items including decay calculations; we lack matching-style items.

### 1.2 X-ray production and x-ray tubes (≈42 Q; answers §1.8)
**Covers:** thermionic emission, cathode/anode, target materials, focal spot and line-focus principle, bremsstrahlung vs characteristic, heat units, rectification, transmission vs reflection targets.
**Bank status:** PARTIAL (m04 covers production, spectrum, tube design, efficiency; good).
**Facts we lack:**
- Therapy tube target angle ~30° with apparent focal spot 5–7 mm vs diagnostic 6–17° (12° typical) and 0.1–2 mm; apparent focal spot a = A·sin θ.
- Heat units = mA × kVp × s (single-phase).
- Average bremsstrahlung energy ≈ one-third of maximum.
- Rectification concept (half-wave/full-wave) and step-up transformer role — "rectif" absent from the bank.
- Bremsstrahlung yield ∝ Z², efficiency ∝ Z·V (bank has efficiency formula; fine).
**Errors:** none significant.
**Question types:** mostly recall; a few heat-unit arithmetic items. Our m04 has 31 items, no heat-unit items.

### 1.3 Interactions of radiation with matter (≈41 Q; answers §1.9)
**Covers:** coherent, photoelectric, Compton, pair production, photodisintegration; Z and E dependence; charged-particle and neutron interactions.
**Bank status:** COVERED (m06 is thorough: Z³/E³, 1.022 MeV threshold, Compton Z-independence, dominance ranges).
**Facts we lack (minor):**
- Numeric energy windows the book teaches: coherent 1–50 keV; Compton dominant ~150 keV–50 MeV in tissue; 90° Compton-scattered photon can never exceed 0.511 MeV, backscattered ≤0.255 MeV.
- Neutron shielding: hydrogenous materials (paraffin, polyethylene, borated); fat receives ~20% more neutron dose than muscle (hydrogen content).
- Stopping power ∝ z²/v² for heavy charged particles; delta rays (term absent from bank).
**Errors:** none.
**Question types:** recall and I–IV. Our m06 has 25 items; comparable.

### 1.4 Treatment machines: kV units through linacs (≈38 Q; answers §1.10)
**Covers:** Grenz, contact, superficial, orthovoltage, supervoltage, Van de Graaff, betatron, microtron, cyclotron, Co-60, linac; machine energy ranges and SSDs.
**Bank status:** PARTIAL (m07 has a good kV table and linac description; historical machines absent).
**Facts we lack:**
- Full kV-machine table with SSD and treatment depth: contact 40–50 kV at <2 cm SSD treating 1–2 mm; superficial 50–150 kV at 15–20 cm SSD treating ≤5 mm; orthovoltage 150–500 kV at 50 cm SSD treating 2–3 cm; supervoltage 0.5–1 MV (bank has kV and HVL but not SSD/depth columns).
- Van de Graaff (~2 MV electrostatic), betatron (4–45 MeV, low dose rate, small fields, heavy), microtron (4–40 MeV, electrons recirculated through one cavity), cyclotron 15–50 MeV for electrons/protons (bank: 0 hits for Van de Graaff, betatron, microtron).
- Co-60 source diameter 1–2 cm, penumbra trimmers (bank has source size; "trimmer" absent).
**Errors:** orthovoltage treatment depth given inconsistently (3–5 cm in one place, 2–3 cm in another).
**Question types:** recall, matching machine ↔ energy range. Our m07 has 33 items.

### 1.5 Linear accelerator components and beam shaping (≈56 Q; answers §1.11)
**Covers:** modulator, thyratron, klystron/magnetron, waveguide, SF₆, circulator, AFC, electron gun (diode vs triode), standing vs traveling wave, energy switch vs beam loading, bending magnets, target, flattening filter, scattering foil, monitor chamber, jaws, MLC, penumbra formula, field size limits.
**Bank status:** PARTIAL (m07 covers beam-path order, magnetron/klystron, 270° achromatic bend, FFF, monitor chamber, penumbra geometry; engineering detail is thin).
**Facts we lack:**
- Pulsed operation: duty factor ~0.1%; pulse repetition 250–300 Hz via thyratron; ~4 µs beam pulse per 3–4 ms period; ~1 µs waveguide fill time; thyratron hydrogen gas pressure ~0.5 Torr.
- SF₆ gas as dielectric in the RF waveguide; circulator isolates the RF source from reflected power (bank has circulator, 1 file).
- Frequency control: AFC on magnetron (coarse) plus phase shifter (fine).
- Energy change: traveling-wave guides use beam loading; standing-wave guides use an energy switch; standing-wave machines need a gridded (triode) gun.
- Bending-magnet variants: 90° (chromatic, energy-dependent spot), 270° achromatic, 112.5°/slalom (bank has 270° only).
- Monitor chamber must be low-Z and thin to avoid perturbing the beam; two independent chambers.
- Maximum field 40×40 at isocenter; MLC leaf width 0.5–1 cm; penumbra P = s·(SSD + d − SDD)/SDD (bank's m36 has this formula — COVERED there).
- Proton reports: TG-224 (proton machine QA), TG-185 (proton commissioning); TG-140 for photodynamic therapy (odd inclusion).
**Errors:** states linac isocenter at 80 or 100 cm (80 cm is Co-60).
**Question types:** recall with some diagram-matching. Our m07 quiz covers beam order and FFF, not RF engineering.

### 1.6 Dosimeters, units, calibration protocols, personnel monitoring (≈62 Q; answers §1.12)
**Covers:** roentgen, rad/gray, rem/sievert, Ci/Bq, f-factor, free-air and thimble chambers, film (OD, H&D curve), radiochromic film, TLD, OSLD, diodes, calorimetry, Fricke, TG-21 → TG-51, TRS-277 → TRS-398, badge rules.
**Bank status:** PARTIAL (m09, m12, m41, m42 cover units, chambers, Ptp, TG-51 conditions, badge wearing).
**Facts we lack:**
- Exposure (R) is defined only for photons below ~3 MeV.
- Film dosimetry: OD = log₁₀(I₀/I_t); OD 3 = 0.1% transmission; H&D curve regions (toe, linear, shoulder), useful OD range ~0.2–4; film accuracy ±3%; radiochromic Z_eff ≈ 6–6.5, model names HD-810 / MD-55-2, temperature-dependent darkening ("optical density" and "H&D" give 0 hits in the bank).
- Si diode: 3.5 eV per ion pair vs 34 eV in air; silicon ~1800× denser than air hence tiny volumes.
- Absolute standards at NIST/ADCL: calorimeter, free-air chamber, Fricke (ferrous sulfate) dosimeter (Fricke 0 hits).
- Protocol history: TG-21 (1983, cavity-gas, N_gas) replaced by TG-51 (1999, N_D,w, photons at 10 cm depth, 10×10, 100 SSD; electrons referenced at R₅₀); IAEA TRS-277 → TRS-398 (2000). TRS-398 absent.
- Badge rules: wear between neck and waist, control badge kept out of the beam, badge required when a worker could receive 10% of the limit, not worn for one's own medical imaging, open window reads beta; film badge not reliable below ~20 mrem; OSLD (Al₂O₃:C) can be re-read for up to a year; TLD dose = calibration dose × (reading/calibration reading).
**Errors/outdated:** TLD given as the most common personnel badge (OSLD now dominates); no mention of TG-51 addendum (2014); badge-issuance activity thresholds (20 mCi / 5 mCi) are institutional examples presented as rules.
**Question types:** recall, unit conversions, a few TLD-calibration proportions. Our m12 has 26 unit items and m41 has 53 protection items; no film/OD items.

---

## Chapter 2 — Dose Calculation Methods (pp. 109–220, ≈232 questions)

### 2.1 Beam data and dosimetric functions (99 Q; answers §2.8)
**Covers:** algorithm classes, phantom materials, equivalent square, PDD, Mayneord F, TAR, BSF, SAR, SMR, TMR, Clarkson, output factors, wedge effects on depth dose, HVL/TVL, Sc/Sp, light-field vs 50% IDL.
**Bank status:** COVERED for PDD/TAR/TMR/BSF/SAR/Mayneord/Clarkson/equivalent-square/Sc-Sp (m09, m33, m35 are strong). PARTIAL on the items below.
**Facts we lack:**
- SMR (scatter-maximum ratio) definition and its role as the SAD-analog of SAR (0 hits).
- Equivalent circle radius r = (4/√π)·(A/P) ≈ 2.26·A/P.
- Rule that TAR is SSD-independent to within ~2% and that TAR tables are not used above ~3 MV (replaced by TMR/TPR).
- Explicit statement that the flattening filter is tuned for flatness at 10 cm depth, producing horns at d_max (bank mentions horns).
- 8×8 has higher PDD than 12×6 of equal area (equivalent-square intuition item).
- TVL = 2.303/µ alongside HVL = 0.693/µ (bank has 1 file).
- Wedge angle decreases with depth; the universal/motorized/EDW/individualized wedge taxonomy; EDW implemented by moving one jaw at variable dose rate (bank: EDW 2 files, "universal wedge" 0).
**Errors:** an editor's review comment is printed inside the text (around p. 115) — publishing defect, not physics.
**Question types:** many definitional MCQs plus about 25 calculations (PDD→TMR conversions, Mayneord, BSF, equivalent square). Our m35/m09/m33 together have ~150 calculation items; stronger than the book here.

### 2.2 Beam geometry, junctions and CSI (42 Q; answers §2.9)
**Covers:** gap calculation, half-beam block, collimator and couch rotation for CSI, feathering, ICRU dose accuracy goals, patient coordinate system, metric prefixes and unit conversions.
**Bank status:** COVERED for gap, couch/collimator divergence trig, breast tangents (m36 has 123 items). PARTIAL for conventions.
**Facts we lack:**
- ICRU accuracy targets quoted as ±5% dose and 5 mm geometry.
- Patient coordinate convention (+X patient left, +Y superior, +Z anterior) — bank has DICOM mentions; confirm the sign convention is stated.
- Conversion constants 1 in = 2.54 cm, 1 ft = 30.48 cm, °F↔°C (0 hits for 2.54 and Fahrenheit — exam-irrelevant but trivial to add).
- Feathering described as ~1 cm moves repeated 3 times over the course.
**Errors:** "90% of 36 Gy = 2.4 Gy" arithmetic slip; another editor's comment left in the text near p. 156.
**Question types:** gap/angle arithmetic — our bank matches well.

### 2.3 Irregular fields and interpolation (9 Q; answers §2.10)
**Covers:** linear interpolation, effective equivalent square after blocking, sector area, magnification.
**Bank status:** COVERED (m35 interpolation tutorial, m08 magnification).
**Facts we lack:** effective equivalent square = √(ESq² − blocked area) shortcut; sector area ½r²θ for hand Clarkson.
**Errors:** none.

### 2.4 Wedges and wedge factors (16 Q; answers §2.11)
**Covers:** wedge factor use in MU, hinge angle ↔ wedge angle, physical vs dynamic wedges, heel/toe, 15 cm minimum skin clearance for trays.
**Bank status:** COVERED (m34 has wedge-factor tutorial, hinge angle, 40 items).
**Facts we lack:** physical wedge avoided on the medial breast tangent because scatter from the thick end reaches the contralateral breast; wedge-pair hot spot grows with wedge angle and field size.
**Errors (several, significant):** Q9/Q10 treat the wedge factor as the attenuated fraction (a WF of 0.624 is read as 62.4% attenuation; 65% transmission is keyed as WF 0.35) — inverted. Q13 stem says 50° separation but the solution uses 150°. Q4 computes 17.7% transmission but keys 6%. A student must not learn wedge factors from this section.

### 2.5 Electron beam rules of thumb (31 Q; answers §2.12)
**Covers:** depth-energy rules, R_p, R₅₀, lead/Cerrobend thickness, d_max table by photon energy, temperature-pressure correction, f-factor.
**Bank status:** COVERED (m19 Electrons 101 has all the rules with Khan vs Bentel variants; m09 has Ptp).
**Facts we lack:**
- R₅₀ ≈ E/2.33 (bank uses E/2.8, E/3.2, E/4, E/2 — 2.33 appears once).
- Rule that below 10 MeV, 5 mm Pb is a safe universal cutout thickness; add 1 mm Pb margin to E/2.
- d_max table extended to 20 MV 3.5, 25 MV 4, 34 MV 5 cm (bank has Co-60 through 18 MV).
**Errors:** f-factor formula printed with an extra square; bone f-factor of 6.17 cGy/R is unrealistic; 90%-depth rule given as E/3 here but E/4 in Ch 3.
**Question types:** short arithmetic; our m19 has 75 items including these.

### 2.6 Inhomogeneity corrections and weighting (27 Q; answers §2.13)
**Covers:** bone/lung correction per cm by energy, effective depth, densities, beam weighting, entrance/exit dose.
**Bank status:** COVERED for effective depth, densities, weighting (m37, m25). PARTIAL for the per-energy table.
**Facts we lack:**
- Correction-per-cm table: orthovoltage (3 mm Cu HVL) bone −7%, lung +10%/cm; Co-60 bone −3.5%, lung +3.5–5%/cm; 4 MV bone −3%, lung +4%/cm; 10 MV lung +2–2.5%/cm; 6 MV ≈ +3%/cm lung; 20 MV ≈ +2%/cm.
- 3 cm of lung ≈ 1 cm of water (density 0.3); fat 0.92; titanium 4.507 g/cm³ (bank has lung 0.25–0.3, bone 1.85).
- Entrance/exit dose from TMR ratio × inverse square for parallel-opposed pairs (bank covers via m25/m35; confirm worked example).
**Errors:** §2.13 Q2 computes an off-axis ratio inverted (1.17 instead of 0.85). Photon inhomogeneity methods listed only as TAR-ratio and isodose shift; Batho and ETAR are omitted (bank has them).

### 2.7 Junction shifts, renormalization, forgotten wedge (8 Q; answers §2.14)
**Covers:** gap per field = ½L·d/SSD; junction shift at a new depth; renormalizing a plan from 108% to 90%; dose delivered when the wedge is omitted (divide by WF); electron surface dose rises with energy while photon surface dose falls.
**Bank status:** COVERED (m36 gap, m25 normalization, m34 wedge-omitted items exist — 6 hits).
**Facts we lack:** junction-shift scaling formula ΔS′ = ΔS·(d′−d)/d.
**Errors:** none.

---

## Chapter 3 — Treatment Planning (pp. 221–303, 200 questions)

### 3.1 Isodose charts, DVHs, ICRU volumes and reporting (47 Q; answers §3.6)
**Covers:** cumulative vs differential DVH, absolute-volume DVH for OARs, isodose measurement, ICRU 50/62 volumes, reference-point rules, hot spot definition, integral dose, NIST standards.
**Bank status:** COVERED (m19 DVH/volumes sections are detailed; ICRU reference point in 3 files).
**Facts we lack:**
- ICRU reference-point placement rules spelled out: equal parallel-opposed → midpoint; unequal weights → on central axis inside PTV; arcs → center of rotation; >2 beams → beam intersection.
- A reportable maximum must cover ≥2 cm² (older ICRU 50 rule; our bank uses 1.5 cm³ / D2% — modern, fine).
- Ion-chamber size guidance for isodose scanning: <15 mm long, <5 mm inner diameter.
- Integral dose unit (gram-rad / J) — 4 hits only.
- Wedge-pair hot spot sits toward the toes and grows with field size and wedge angle.
**Errors:** says ICRU 50 and 62 were issued in 1978 (actual 1993 and 1999).
**Question types:** recall, I–IV. Our m19 has 75 items; good.

### 3.2 Electron beam planning (46 Q; answers §3.7)
**Covers:** useful energy range, stopping power vs Z, scattering, virtual source, bremsstrahlung tail, flatness/symmetry specs, obliquity, CET, bolus, air gaps, abutments, cutouts and internal shields, electron arc, TSEI.
**Bank status:** COVERED for rules, bolus, abutment, eye shields, TSEB (m19, m24). PARTIAL for specs and shielding numbers.
**Facts we lack:**
- Electron flatness specification: within ±5% over the region inside 2 cm of the field edge at the 95% depth; symmetry 2%.
- Electron backscatter from lead internal shields is 30–70% of the incident dose (1–20 MeV), so a low-Z coating (wax/aluminum) is placed on the patient side; worked example: 9 MeV at 2 cm → ~5 MeV residual → ~2.5 mm Pb (0 hits for backscatter percentage).
- Cutout transmission goal ≤5%; cutout minimum dimension should be ≥ R_p to preserve PDD.
- Electron scattering power ∝ Z²/E², bremsstrahlung ∝ E·Z².
- Electron arc for chest wall; decelerators/degraders (1 hit).
- Pencil-beam algorithm as the standard electron algorithm (older; Monte Carlo now).
**Errors:** electron cones said to need 15 cm from skin (that is the photon-tray rule; cones sit ~5 cm).
**Question types:** recall; a dozen arithmetic items. m19 comparable.

### 3.3 IMRT and inverse planning (25 Q; answers §3.8)
**Covers:** SMLC/DMLC/IMAT definitions, DMLC QA tests, objective functions, simulated annealing vs gradient descent, local vs global minima, fluence-to-leaf sequencing, prescription isodose by modality, VMAT advantages, QA deviation interpretation.
**Bank status:** COVERED (m23 covers step-and-shoot/sliding-window/VMAT/beamlets; m29 optimization).
**Facts we lack:**
- Names of the five classic DMLC QA tests (leaf position, speed, gap, acceleration, transmission).
- Simulated annealing (stochastic, escapes local minima, slower) vs gradient methods (fast, can trap in local minimum) — "local minimum" 0 hits.
- Typical prescription isodose lines by platform: Gamma Knife 50%, CyberKnife ~70%, IMRT 95%, VMAT 90% (bank has GK 50%).
- Uniform ~4% deviation across all IMRT QA fields points to output/calibration, not the plan.
**Errors:** none.

### 3.4 Special procedures: TBI, SRS/SRT, Gamma Knife, CyberKnife, IORT, endocavitary, SIRT, radioiodine (68 Q; answers §3.9)
**Covers:** TBI regimens and setup, SRS/SRT definitions and accuracy, Gamma Knife hardware, CyberKnife hardware and QA, radiobiology snippets (α/β, BED, 4 Rs), IORT, Papillon endocavitary, Y-90 SIRT, I-131.
**Bank status:** PARTIAL (m24 covers TBI, TSEB, SRS/SBRT at concept level; GK/CK hardware, IORT, SIRT, endocavitary are MISSING).
**Facts we lack:**
- TBI specifics: 12 Gy in 2 Gy BID with ≥6 h between fractions; ±10% uniformity goal; lateral technique dose-rate and homogeneity issues; 6 MV acceptable if separation <35 cm at ~300 cm SSD; acrylic spoiler 1–2 cm thick brings surface dose to ≥90%; reference point midplane at umbilicus; low-dose TBI 10–15 fx × 10–15 cGy; half-body 8 Gy single; total nodal 40 Gy/20 (HBI 0 hits).
- SRS/SRT: SRS = 1 fraction, SRT = 2–5; overall accuracy accepted ±1 mm (best systems ~0.2 mm); cone sizes 4–30 mm, ~15 cm long.
- Gamma Knife: 201 Co-60 sources (model 4C), source-focus distance 40.3 cm, 55° tilt, 4/8/14/18 mm helmets, 6 cm tungsten plugs; Perfexion 192 sources with 4/8/16 mm sectors (bank: 4 files mention GK, none of these numbers).
- CyberKnife: 6 MV compact linac, 80 cm SAD, 12 fixed cones 5–60 mm, IRIS variable collimator (no 5 mm), skull tracking to 0.5 mm/0.5°, ~33 DRR pairs per plan, CT 1–1.5 mm slices with 10–15 cm margins, MRI 1–3 mm ≤300 slices, fiducial-to-CT interval ~1 week soft tissue / 24–48 h bone, KUKA 6-DOF robot 0.2 mm repeatability, Multiplan TPS with Monte Carlo option, TG-135 QA report, end-to-end test every ~4 months, daily warm-up 6000/3000 MU plus AQA, E-stop range <5 cm, 12 beams per node, overall precision ~0.5 mm (TG-135 0 hits, IRIS 0 hits).
- α/β values used in the book: cord 2.5, optic structures 2.1, lung 1.6–4.5, skin 10–20 (bank uses 3/10/1.5 generic values).
- IORT: single 10–20 Gy intraoperative dose (4 hits total).
- Endocavitary (Papillon) rectal contact therapy: tumors ≤3 cm, ≤10 cm from anal verge, ~80 Gy in 2–3 fractions of 20–30 Gy two weeks apart, 50 kV at 4 cm SSD (0 hits).
- SIRT: Y-90 microspheres, 50–150 Gy to tumor, whole-liver limit ~30 Gy; Y-90 T½ 64 h pure β with mean range 2.5 mm/max 11 mm; TheraSphere (glass, HCC) vs SIR-Spheres (resin, metastases); lung-shunt fraction from Tc-99m MAA; TG-144 (TG-144 0 hits; Y-90 only as a decay example).
- I-131: T½ 8 d, oral, ≥100 mCi for thyroid cancer; I-123 for SPECT, I-124 for PET (I-123/I-124 0 hits).
- LDR ≤2 Gy/h, HDR >12 Gy/h (bank has).
**Errors/outdated:** Gamma Knife mechanical precision printed as ±3 mm (should be ±0.3 mm); liver blood supply said to be hepatic vein (portal vein); Y-90 delivered via "femoral artery" as a keyed answer (access route, not target vessel); 201-source GK and helmets presented as current; Perfexion described as new, CBCT "in the future" (Icon shipped 2015).
**Question types:** very recall-heavy, device-specific; a few BED sums. Our m24 has 36 items at a more exam-generic level.

### 3.5 Miscellaneous planning (14 Q; answers §3.10)
**Covers:** hot-spot location rules, flattening filter influence, horns, FFF rationale, ion-chamber choice, 95%/≤5%>110% coverage goals.
**Bank status:** COVERED (m07 flattening filters, m19 metrics).
**Facts we lack:** none material.
**Errors:** none.

---

## Chapter 4 — Patient Immobilization and IGRT (pp. 305–320, 35 questions)

### 4.1 Immobilization devices (11 Q; answers §4.4)
**Covers:** alpha cradle, belly board, Vac-Lok, wing board, breast board, Duncan mask for prone CSI, bite block, shoulder straps.
**Bank status:** COVERED (m14 covers each device with reasoning).
**Facts we lack:** Duncan-style prone head mask for CSI; bite-block indexing; "Trendelenburg is not a treatment position" item. Minor.
**Errors:** none.

### 4.2 IGRT systems (15 Q; answers §4.5)
**Covers:** CBCT, MVCT/TomoTherapy, portal imaging, orthogonal kV, CT-on-rails, Calypso, BAT ultrasound, ExacTrac, adaptive RT.
**Bank status:** COVERED (m18, m32, m28; ExacTrac, CBCT, MVCT present).
**Facts we lack:** Calypso = 3 implanted RF transponders giving continuous monitoring (not beam tracking) — 1 hit; TomoTherapy detector is xenon-filled (3 hits); BAT ultrasound as historical prostate localization.
**Errors/outdated:** BAT presented as current; no surface-guidance (SGRT) mention.

### 4.3 Fractionation terms (9 Q; answers §4.6)
**Covers:** hypofractionation (>2 Gy/fx), Canadian breast 42.5/16 at 2.67 Gy, SBRT ≤5 fx at >4 Gy/fx, SRS margins 0–1 mm, lost-mask workflow (re-CT and replan).
**Bank status:** COVERED (m21, m24, m14).
**Facts we lack:** none.
**Errors:** none.

---

## Chapter 5 — Brachytherapy (pp. 321–406, ≈227 questions)

### 5.1 General concepts (19 Q; answers §5.9)
**Covers:** definitions, interstitial/intracavitary/surface/intravascular, LDR vs HDR durations, remote afterloading pros and cons, dose-rate classes (LDR 0.4–2 Gy/h, MDR 2–12, HDR >12), HDR single-source activity 10–20 Ci, orthogonal films and magnification SFD/SAD, stereo-shift method.
**Bank status:** COVERED (m40 opening section matches dose-rate classes and afterloading).
**Facts we lack:** stereo-shift reconstruction method; film magnification = SFD/SAD; MDR range explicitly; HDR source 10 Ci nominal (2 hits).
**Errors:** none.

### 5.2 Radioactive source characteristics (44 Q; answers §5.10)
**Covers:** half-life, Γ, and energy matching tables; decay-rate rules of thumb; radium hazards; needle types; source specification history (mg, mg-Ra-eq, apparent activity, air-kerma strength); well chamber; encapsulation.
**Bank status:** COVERED for half-lives/energies/Γ of Ir, Cs, Co, Ra, I, Pd (m03, m40). PARTIAL for radium-era material.
**Facts we lack:**
- Γ values for Rn-222 (10.15), Au-198 (2.38), I-125 (1.45), Pd-103 (1.48) R·cm²/mCi·h; Ra-226 average energy 0.83 MeV (range 0.18–2.45), Au 0.41 MeV (bank omits I-125 Γ deliberately; Au/Pd/Rn absent).
- Half-lives Rn-222 3.83 d, P-32 14 d, Sr-90 28 y, Y-90 64 h (bank has Sr/Y/P; Rn absent).
- Decay rules of thumb: Ir ≈1%/day, Co ≈1%/month, Cs ≈2.3%/yr, Pd ≈4%/day, Rn ≈18%/day, Au ≈25%/day, I-125 ≈1%/day.
- Radium replaced because it behaves like calcium (bone deposition), high gamma energy, radon leakage; radium needles: uniform, Indian club (one hot end), dumbbell (two hot ends).
- Ir-192 wire is 30% Ir / 70% Pt alloy; I-125 and Pd-103 in laser-welded titanium with anisotropic cold ends; Pd-103 delivers dose faster (shorter T½).
- 1 mg-Ra-eq = 8.25×10⁻⁴ R/h at 1 m; Γ_Ra defined at 1 cm from 1 mg filtered by 0.5 mm Pt.
- Co-60 brachy advantage is high specific activity (small sources).
**Errors:** one matching key lists Ir-192 decay as 1%/yr (should be ~1%/day); Γ for Cs inconsistent across pages (3.1, 3.26, 3.27, 3.28); Ir Γ given as both 4.69 and 4.62.
**Question types:** matching-heavy (5 big matching tables); our m40 has 98 items but no matching format.

### 5.3 Implant systems (20 Q; answers §5.11)
**Covers:** Manchester (Paterson-Parker), Quimby, Memorial, Paris systems; planar vs volume implants; distribution rules; applicator catalogue.
**Bank status:** MISSING (bank mentions Manchester only for point A; Quimby 1 hit, Paris system 0, basal dose 0).
**Facts we lack:**
- Manchester planar: ±10% uniformity; periphery:center split by area — <25 cm² 2/3:1/3, 25–100 cm² 1/2:1/2, >100 cm² 1/3:2/3; needle spacing ≤1 cm; each uncrossed end reduces treated area by 10%; prescribed dose is 10% above the minimum.
- Manchester volume: cylinder 8 parts (belt 4, core 2, each end 1); sphere belt 6/core 2; ≥8 belt needles and ≥4 core; each uncrossed end −7.5%; volume implant needed when thickness >2.5 cm.
- Quimby: uniform activity, nonuniform dose; planar prescribed to the maximum, volume to the minimum. Memorial extends Quimby with 1 cm lattice spacing.
- Paris: uniform linear activity, parallel lines, 8–15 mm spacing, no crossing, basal dose = mean of local minima between sources, reference isodose = 85% of basal dose.
- Fletcher-Suit tandems 15°/30°/45°; Henschke applicator; Heyman capsules; rectal and nasopharyngeal applicators.
**Errors:** none.
**Question types:** definitional plus 5 Manchester distribution calculations in §5.7.

### 5.4 Temporary implant procedures: GYN and eye (39 Q; answers §5.12)
**Covers:** tandem and ovoids, cylinder, Sr-90 pterygium applicator, COMS eye plaque, point A/B definitions and rationale, ICRU 38 bladder/rectum points, lymphatic trapezoid and pelvic wall points, OAR limits, applicator selection, 2 cc volume criterion.
**Bank status:** COVERED for point A/B, ICRU 38 points, cylinder prescription, D2cc (m40). PARTIAL for the rest.
**Facts we lack:**
- Point A historical definition (2 cm above lateral fornix) vs current (2 cm above external os); point A marks where uterine arteries cross ureters; point B = obturator nodes, fixed 5 cm from midline so A and B can be misaligned with a tilted uterus.
- Lymphatic trapezoid (para-aortic, common and external iliac nodes) and pelvic wall point construction on the acetabulum (0 hits).
- Bladder/rectum max preferably ≤80% of point A dose.
- Rectal-point AP-film rule differs between T&O (lower end of intrauterine source) and cylinder (middle of source).
- Largest ovoids and longest tandem that fit give the most uniform distribution; HDR source stops ~4–5 mm short of catheter tip.
- Sr-90 β (via Y-90, ~2.2 MeV max) for pterygium; COMS plaque = gold backing + Silastic seed carrier; I-125/Pd-103 (pterygium 0 hits, COMS 6 hits).
**Errors/outdated:** says GYN HDR has "recently" moved to 3D/DVH — true in 2015; EMBRACE/GEC-ESTRO not named (our bank has them).

### 5.5 Permanent implants (13 Q; answers §5.13)
**Covers:** prostate seed workflow, nuclide choice, surgical approaches, imaging, post-implant dosimetry timing, patient position, pubic-arch interference, preplan contents, cystoscopy, average life.
**Bank status:** PARTIAL (m40 has 145/125 Gy, seed assay, mean life; workflow details absent).
**Facts we lack:**
- Transperineal TRUS-guided approach preferred over retropubic; dorsal lithotomy position; fluoroscopy and ultrasound as intra-op imaging (0 hits for lithotomy/transperineal).
- Post-implant CT at ~1 month (edema resolution); MRI avoided for seeds (artifact); cystoscopy to retrieve seeds in bladder.
- Hormonal downsizing for large gland/pubic-arch interference.
- Pd-103 for faster-growing/high-grade tumors; Au-198 abandoned for exposure reasons.
- Contours for preplan: prostate, urethra, rectum (bladder usually not visible on TRUS).
- Anisotropy cold spots can exceed 50% at seed ends.
**Errors:** none.

### 5.6 Dose delivery, calibration and positional QA (12 Q; answers §5.14)
**Covers:** well chamber in current mode, sweet spot, source identification checks, vendor vs user calibration ±5% rule, dummy vs active source agreement ±1 mm, step sizes (2.5 mm minimum, 40 dwell positions on older Nucletron), applicator checks.
**Bank status:** PARTIAL (m40 well chamber 1 hit, dwell concept yes; QA tolerances deliberately absent).
**Facts we lack:** sweet-spot definition; current-mode (nA) rather than charge; ±5% vendor/user calibration acceptance; dummy/active ±1 mm; 2.5 mm step; source ruler and autoradiograph position checks; marker cable integrity; temporal accuracy within 1 s (TG-56/59 numbers).
**Errors:** none.

### 5.7 Brachytherapy dose calculations (62 Q; answers §5.15)
**Covers:** X = ΓA/d²; mCi↔mg-Ra-eq conversion via Γ ratio; inverse square with filtration; Manchester mg-h table lookups; permanent dose = D₀·1.44·T½; temporary dose = D₀·t_avg·(1−e^(−t/t_avg)); decay forward and backward; survey-meter scale reading; HVL/µ; shielding HVL counts; multi-source point dose from a line-source table with interpolation; air-kerma strength from Γ (×0.876); TRAK.
**Bank status:** COVERED for Γ·A/d², decay, permanent-implant mean life, TG-43, TRAK, HVL (m40, m03, m36). PARTIAL for the mg-Ra-eq family and the finite-time temporary-implant integral.
**Facts we lack:**
- mg-Ra-eq ↔ mCi conversion = activity × Γ_nuclide/8.25 (bank intentionally avoids a universal factor; exam may still ask the historical form).
- Temporary implant delivered dose over a finite time: D = D₀·t_avg·(1 − e^(−t/t_avg)), and solving for removal time (bank uses t = D/Ḋ without the decay integral — fine for HDR, not for multi-day Ir-192 LDR).
- 1 mg-Ra-eq ≈ 7.227 cGy/h air-kerma rate at 1 cm (8.25 × 0.876).
- Survey meter needle × range multiplier item; HVL-count shielding with 50-week work year.
- Line-source (Sievert-type) table interpolation for multi-source point dose.
**Errors:** several numeric inconsistencies (Γ_Ir 4.62 vs 4.69; T½ Ir 73.8 vs 74.2 vs 74.3; Cs Γ 3.1 vs 3.26); Q62 sums 18.75 + 17.30 + 4.85 but writes 4.25 in one line (final 40.30 is right); Q27 labels a Au-198 result as Cs. Methods are sound.
**Question types:** ~55 calculations with full solutions — the most calculation-dense section of the half. Our m40 has ~40 calculation items; comparable in count but different in formalism (TG-43/U vs Γ/mg-Ra-eq).

### 5.8 ICRU and AAPM reports (18 Q; answers §5.16)
**Covers:** ICRU 58 (interstitial reporting: MTD, mean central dose, high-dose volume 150%, uniformity ratios), ICRU 38, ICRU 60, NRC HDR leakage limit, TG-43 components, TG-64, TG-128, TG-129, HDR QA four pillars.
**Bank status:** PARTIAL (TG-43 fully covered; ICRU 58, TG-64, TG-128, TG-129 0 hits).
**Facts we lack:**
- ICRU 58 (1997): minimum target dose at CTV periphery (~90% of prescription in Manchester terms), mean central dose = mean of local minima in the central plane, high-dose volume = tissue ≥150% of MCD, uniformity = MTD/MCD; PTV ≈ CTV for interstitial.
- HDR unit leakage limit 1 mR/h at 10 cm from the safe surface (bank has shielding leakage generally; check this value).
- TG-64 prostate seed implants; TG-128 TRUS QA; TG-129 eye-plaque dosimetry; TG-43 components named (S_K in U = cGy·cm²/h; Λ in cGy/h/U; geometry, radial, anisotropy); I-125 most affected by the radial dose function.
- HDR QA pillars: temporal (≤1 s), dosimetric (decay chart), positional (<1 mm), safety interlocks.
**Errors:** none.

---

## Chapter 6 — Radiobiology, §6.1–6.4 questions only (pp. 407–424, ≈76 questions read; answers in Part 2)

### 6.1 Cellular biology (13 Q)
**Covers:** cell constituents, eukaryotic/somatic/germ cells, mature vs stem cells, tissue definitions, cell-cycle phases and durations, phase sensitivity, direct vs indirect action, free radicals.
**Bank status:** PARTIAL (m21 covers cycle phases and sensitivity; cell biology and direct/indirect action absent — 0 hits for free radical, direct action, eukaryote).
**Facts we lack:** mammalian cell cycle ~10–20 h; indirect action (via water radiolysis → OH• radicals) is the dominant mechanism for low-LET photons, direct action for high-LET; DNA as the principal target.

### 6.2 Cell death (8 Q)
**Covers:** high-LET direct action, indirect-action chain, outcomes (no effect, division delay, apoptosis, reproductive failure, genomic instability, mutation, transformation, bystander, adaptive response), DSB threshold (none), particle penetration, EM radiation.
**Bank status:** MISSING as taught (apoptosis, mitotic death, bystander, adaptive response: 0 hits).
**Facts we lack:** definitions above; double-strand breaks have no dose threshold; alpha stopped by skin, beta by ~cm of tissue, gamma penetrates.

### 6.3 Normal tissue complications (44 Q)
**Covers:** radiation-induced cancers, late effects, lethal/sublethal/potentially lethal damage, somatic vs genetic, stochastic vs deterministic, acute effects, ARS syndromes and doses, fetal stages and effects, 4 Rs, radioprotectors (amifostine, must be present at irradiation), tolerance-dose determinants, TD5/5 and TD50/5 tables, Bergonié–Tribondeau, VIM/DIM/RPM/FPM cell classes, DNA structure and base pairing, mitosis phases, prodromal syndrome, hematopoietic death timing, LD50/30, EM spectrum relations.
**Bank status:** PARTIAL (4 Rs, stochastic/deterministic, QUANTEC present; classical Emami/ARS/fetal/Bergonié material MISSING — TD5/5 1 hit, Emami 1, hematopoietic 0, organogenesis 0, Bergonié 0, amifostine 0, prodromal 0).
**Facts we lack:**
- ARS: hematopoietic (≈2–10 Gy, death in weeks to 2 months), GI (≈10–50 Gy, death in 3–10 days, bloody diarrhea), cerebrovascular (>50 Gy, death in 24–48 h); prodromal phase; LD50/30 or LD50/60 definitions.
- Fetal stages: preimplantation (day 0–10), organogenesis (day 11–42), fetal growth (43–birth); effects depend on dose and stage; abortion consideration at >10 cGy historically.
- Emami TD5/5 examples: liver 30 Gy, stomach 50 Gy, brain 45–50 Gy, kidney 23 Gy, lens 10 Gy; TD50/5: lens 18 Gy, lung 24.5 Gy, bladder/rectum 80 Gy; ovaries TD5/5 2–3 Gy (sterilization), ureters 70 Gy (stricture), oral cavity 60 Gy (mucositis), whole intestine 40 Gy (obstruction/perforation).
- Bergonié–Tribondeau: sensitivity ∝ mitotic rate and ∝ 1/differentiation; VIM (most sensitive) → DIM → RPM → FPM (most resistant); liver, muscle, nerve are RPM/FPM.
- Radioprotectors: amifostine, must be present within ~30 min of irradiation.
- Tissue ordering most-to-least sensitive: gonads, lens, lung, liver, brain.
- DNA bases (purines A/G, pyrimidines T/C; A–T, G–C), mitosis phase descriptions.
**Errors:** TD values are Emami 1991 (dated vs QUANTEC — our bank is current); one option set lists "TD 5/5 50 Gy" twice for different organs (key ambiguity).

### 6.4 Survival curves and models (Q1–11 read)
**Covers:** survival-curve definition, multi-target parameters (n, D₀, D_q), fractionation advantages, hyperfractionation definition, differentiated vs proliferating cells, multi-target formula, LQ as model of choice.
**Bank status:** COVERED (m21 defines D₀, D_q, n, LQ; hyperfractionation term absent — 0 hits).
**Facts we lack:** multi-target survival formula SF = 1 − (1 − e^(−D/D₀))ⁿ and the relation ln n = D_q/D₀; hyperfractionation (>1 fx/day, <1.8 Gy), accelerated fractionation, CHART definitions.
**Errors:** Q7 labels the quasithreshold dose as D₀ (should be D_q).

---

## Question-type comparison

| Book type | Approx share (Ch 1–5) | Our bank |
|---|---|---|
| Single-answer recall MCQ | ~45% | Dominant format; good |
| "I, II, III, IV" multi-truth | ~30% | Rare (≈39 hits for the pattern); worth adding since MDCB uses it |
| Matching lists (nuclide↔value, device↔use) | ~5% | Absent as a format |
| Calculations with worked solutions | ~20% (dense in §2.1, §2.5, §2.7, §5.7) | ~370 calculation stems; stronger and more modern (TG-43, EQD2) |

---

## Summary

1. **Overall book quality: 6/10.** Broad, exam-shaped, and useful for recall drilling, but riddled with numeric inconsistencies, several wrong keys (wedge factor inversion, OAR inversion, GK ±3 mm, ICRU dates, electron cone clearance, liver blood supply) and two editor's comments left in print; a student needs an answer-checker.
2. **Estimated share of this half already in our bank: ~65%.** Chapters 1–3 core physics and calculation methods ≈80% covered; Chapter 4 ≈90%; Chapter 5 ≈50% (classical implant systems, radium-era specification, GYN points beyond A/B, seed workflow are gaps); Chapter 6 (read portion) ≈35% (classical radiobiology is thin in m21).
3. **Top 15 exam-valuable additions (ranked):** (1) Manchester/Paterson-Parker planar and volume distribution rules with the uncrossed-end penalties; (2) Paris system (basal dose, 85% reference isodose, 8–15 mm spacing) and Quimby/Memorial contrasts; (3) mCi↔mg-Ra-eq conversion via Γ ratio and the Γ/half-life/energy tables for Au-198, Rn-222, I-125, Pd-103; (4) finite-time temporary-implant dose integral D₀·t_avg·(1−e^(−t/t_avg)) and solving for removal time; (5) Emami TD5/5–TD50/5 recall set and acute radiation syndromes with dose/time bands; (6) classical radiobiology vocabulary — direct/indirect action, apoptosis vs mitotic death, bystander, adaptive response, Bergonié–Tribondeau and VIM/DIM/RPM/FPM, fetal stages; (7) ICRU 58 interstitial reporting quantities (MTD, MCD, high-dose volume, uniformity ratio) plus TG-64/128/129 names; (8) HDR QA numbers — vendor/user calibration ±5%, dummy/active ±1 mm, 2.5 mm step, 1 s timer, 1 mR/h at 10 cm leakage, sweet spot, source ruler; (9) GYN reference points beyond A/B: lymphatic trapezoid, pelvic wall points, ≤80% of point A for bladder/rectum, historical vs current point A, HDR tip offset 4–5 mm; (10) linac pulse structure and RF engineering (duty factor ~0.1%, 250–300 Hz, thyratron, SF₆, AFC, energy switch vs beam loading, gridded gun, 90°/270°/slalom magnets); (11) kV machine table with SSD and treatment depth plus Van de Graaff/betatron/microtron one-liners; (12) film dosimetry basics — OD definition, H&D curve, radiochromic properties, Fricke/calorimeter as absolute standards, TG-21→TG-51 and TRS-277→TRS-398 history; (13) Gamma Knife and CyberKnife hardware numbers (sources, SFD, collimator sizes, 80 cm SAD, IRIS, tracking accuracy, TG-135, E2E interval); (14) special-procedure facts for SIRT (Y-90 glass vs resin, lung shunt, 30 Gy liver limit, TG-144), IORT single 10–20 Gy, and Papillon endocavitary parameters; (15) permanent-seed workflow (transperineal TRUS, lithotomy, 1-month post-implant CT, cystoscopy, hormonal downsizing) and electron shielding backscatter 30–70% with low-Z coating.
4. **Error list to avoid importing:** wedge factor as attenuation fraction; OAR inverted; GK precision ±3 mm; ICRU 50/62 in 1978; electron cone 15 cm clearance; hepatic vein as liver supply; Ir-192 decays 1%/yr; linac isocenter 80 cm; valence = lowest shell; gravity 36× weaker; multiple Γ and T½ values for the same nuclide.
5. **Dated content:** Emami tables (we use QUANTEC), TLD as default badge (OSLD), BAT ultrasound, 201-source GK/helmets, pencil-beam electrons, no TG-51 addendum, no TG-263 nomenclature, no SGRT, GYN brachy pre-EMBRACE.
6. **Format lesson:** the book's heavy use of I–IV multi-truth and matching items mirrors MDCB style; our bank should add ~50–80 items in those formats, especially nuclide matching and device/report matching.
7. **Calculation lesson:** our bank's calculation set is larger, more modern, and better explained; the book adds only the mg-Ra-eq family, Manchester table lookups, line-source table interpolation and survey-meter/HVL-count shielding items.
8. **Where the book is better:** sheer recall breadth on hardware, radium-era brachytherapy, classical radiobiology, and device-specific SRS platforms.
9. **Where our bank is better:** accuracy, modern references (TG-43U1, TG-101, QUANTEC, GEC-ESTRO, TG-51), worked-example rigor, trap-focused explanations, and calculation depth.
10. **Verdict: complementary, not a replacement.** Use the book as a gap list for recall items (items 1–15 above) and as a source of question-format ideas; do not use it as an answer authority.
