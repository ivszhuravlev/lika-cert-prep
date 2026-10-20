# RM Review — MDCB Practice Tests (inbox audit)

Review date: 2026-10-20. Source: nine text extracts in `inbox/text/Practice Exams__*.txt` (third-party, copyrighted, gitignored). Nothing below quotes source wording; every item is paraphrased. Coverage marks come from `rg` sweeps over `knowledge/theory` and `knowledge/questions` (≈390 label/regex probes, then targeted re-checks of every zero- or single-hit probe).

Legend: **COVERED** = fact and its typical calc appear in ≥2 bank files (theory or questions). **PARTIAL** = topic present but the specific fact/number/calc the test wants is absent or appears only once in passing. **MISSING** = no hit under any reasonable pattern.

---

## 1. Per-file statistics

| File | Edition | Tests × items | Total items | Keys | Style (approx.) | Domain split (approx.) |
|---|---|---|---|---|---|---|
| `MDCB PRACTICE TEST 2018_1` | 2018 "Set 1" | Tests 1–4 × 35 | 140 | Yes (letter only) | recall 55 / calc 25 / clinical 20 | physics 25, planning 25, calcs 20, brachy 8, protection 7, QA 5, anat-onc 10 |
| `MDCB PRACTICE TEST 2018_2` | 2018 "Set 2" | Tests 5, 6 × 50 | 100 | Yes | recall 55 / calc 20 / clinical 25 | physics 20, planning 25, calcs 15, brachy 5, protection 5, QA 10, anat-onc 20 (T6 is image-ID heavy, images not in extract) |
| `MDCB PRACTICE TEST 2018_3` | 2018 "Set 3" | Tests 7–10 × 35 | 140 | Yes | recall 60 / calc 25 / clinical 15 | physics 30, planning 20, calcs 20, brachy 8, protection 7, QA 5, anat-onc 10 (T9 has matching items) |
| `MDCB PRACTICE TEST 2018_4` | 2018 "Set 4" | Tests 11, 12 × 50 | 100 | Yes, partial rationales | recall 55 / calc 25 / clinical 20 | physics 25, planning 25, calcs 20, brachy 7, protection 8, QA 7, anat-onc 8 (T11 Q15 needs tables not present) |
| `MDCB PRACTICE TEST 2018_5` | 2018 "Set 5" | Tests 13, 14 × 50 | 100 | Yes | recall 50 / calc 30 / clinical 20 | physics 25, planning 20, calcs 25, brachy 8, protection 7, QA 8, anat-onc 7 |
| `MDCB PRACTICE TEST 2020` | 2020 | 1 × 60 | 60 | Yes, a few rationales | as Tests 13/14 | as Tests 13/14 — ~58 of 60 are reprints |
| `MDCB PRACTICE TEST 2023` | 2023 | 6 short tests (29, 26, 25, 43, 35, 39) | 197 | Yes | as 2018 | reprint of Tests 7, 8, 10, 5, 11, 14 with light edits |
| `PRACTICE TESTS_SET 1` | 2025 | 6 short tests (28, 26, 24, 42, 34, 38) | 192 | Yes | as 2018 | corrected reprint of 2023 (3 fixes, 2 new errors, 1 stray reviewer note) |
| `Test1` | 2005 | Exams 1–4 × 35 | 140 | Yes | recall 45 / calc 35 / clinical 20 | physics 30, planning 20, calcs 30, brachy 10, protection 5, QA 5 — five-option (A–E) and K-type multi-select; many items depend on figures that are not in the extract |
| **Raw total** | | | **≈1169** | | | |

**Unique questions:** the 14 numbered 2018 tests hold ≈580 items with ~25 internal repeats → ≈555 unique. 2020/2023/2025 contribute almost nothing new (≈5 items). The 2005 edition overlaps the 2018 set on ~80 items and adds ≈60 genuinely different ones (older K-type, orthovoltage, Co-60 80-SAD geometry, block-cutter geometry). **Estimated unique pool ≈ 560–620.**

---

## 2. Duplicate map (cross-file)

| Later file | Reprints of |
|---|---|
| 2020 (60 Q) | Test 13 Q1–30 and Test 14 Q1–30, in order; two stems reworded (Q3 "hypofractionation" wording changed but key unchanged; Q14 fundamental unit) |
| 2023 Test 1 | 2018 Test 7 (29 of 35) |
| 2023 Test 2 | 2018 Test 8 (26 of 35) |
| 2023 Test 3 | 2018 Test 10 (25 of 35) |
| 2023 Test 4 | 2018 Test 5 (43 of 50) |
| 2023 second "Test 4" (= Test 5) | 2018 Test 11 (35 of 50) |
| 2023 Test 5 (= Test 6) | 2018 Test 14 (39 of 50) |
| 2025 Tests 1–6 | 2023 Tests 1–6 minus 1 item each, with three key corrections (see §4) |
| 2005 Exams 1–4 | ~80 items re-used (sometimes re-optioned to 4 choices) in 2018 Tests 1, 3, 9, 12, 13 |

Within-2018 repeats: Mayneord factor (T5, T11), penumbra definition (T5, T7, T11), light-field/isodose relation (T13, T14), QUANTEC cord (T2, T7, T13), Sr-90 applicator timer (T1, T13), permanent-implant total dose (T3, T8, T12), neutron mixed-field equivalent dose (T4, T10), CSI collimator/couch angle (T2, T9, T14), gap calc (T1, T6, T12), wedge-factor-omitted (T3, T13), TG-142 kV/SRS tolerance (T6, T14), lens limit (T4, T12, T14).

---

## 3. Fact inventory (paraphrased; coverage against our bank)

Each line: fact or calc type the key teaches → mark → bank module where found (or where it belongs if missing).

### 3.1 Physics fundamentals & radioactivity (m02, m03, m04, m06, m12)

- Decay constant = 0.693 / T½; activity after t = A₀·e^(−λt) → **COVERED** (m03, m36, m40; 17 files)
- Co-60 T½ 5.26 y, λ ≈ 0.13 y⁻¹, output falls ~1 %/month → **COVERED** (m03, m07)
- Cs-137 T½ 30 y; I-125 59.4 d; Ir-192 73.8 d; Pd-103 17 d; Au-198 2.7 d → **COVERED** (m01, m03)
- Permanent-implant total dose = 1.44 · T½ · initial dose rate (mean life) → **COVERED** (m03, m40, m36; 21 files)
- 1 Ci = 3.7×10¹⁰ Bq ≈ 1 mg Ra → **COVERED** (m03, m12)
- mg-Ra-equivalent from activity × Γ ratio → **COVERED** (m40; 4 files)
- Exposure rate = Γ·A/d²; Au-198 Γ derived from Ra-equivalence → **COVERED** (m40, m03)
- Secular / transient equilibrium (Sr-90/Y-90, Mo/Tc) → **COVERED** (m03)
- Decay modes: β⁻, β⁺, EC, IT, internal conversion, Auger; ΔZ/ΔA → **COVERED** (m03)
- Isomeric transition / metastable state → **COVERED** (m03)
- Pair production threshold 1.022 MeV; annihilation 2 × 0.511 → **COVERED** (m06)
- Photoelectric ∝ Z³/E³, dominant kV; Compton ∝ electron density, dominant MV → **COVERED** (m06)
- Coherent (Rayleigh) scatter negligible → **COVERED** (m06)
- Characteristic x-rays and inner-shell binding energy → **COVERED** (m04)
- Bremsstrahlung; x-ray production efficiency rises with Z and kV → **COVERED** (m04)
- Average photon energy ≈ ⅓ of maximum → **COVERED** (m05)
- X-rays vs gamma differ only by origin → **COVERED**
- HVL = 0.693/μ; n HVLs → 1/2ⁿ; 2 HVL for μ = 0.94 cm⁻¹ ≈ 1.47 cm → **COVERED** (m05, m06, m41; 20 files)
- TVL = 3.32 HVL = 2.303/μ → **COVERED** (m41)
- Mass attenuation coefficient μ/ρ → **COVERED** (m06)
- Excitation vs ionization; indirectly ionizing photons/neutrons → **COVERED** (m02, m06)
- Thermionic emission → **COVERED** (m04)
- Proton/neutron rest mass ≈ 938/939 MeV → **COVERED** (m02)
- Metric prefixes (micro 10⁻⁶, milli 10⁻³, centi 10⁻², nano 10⁻⁹) → **COVERED**
- E = hc/λ (Planck relation) numerical → **PARTIAL** (one mention in m02; no worked item)
- Avogadro's number; atoms per gram = N_A / A → **MISSING** (m02)
- Nuclear binding energy / mass defect; strong force holds nucleons, electromagnetic force holds electrons → **MISSING** (m02)
- Radiation weighting factors (photon 1, neutron ~20) and mixed-field equivalent dose calc → **COVERED** (m12, m41; 14 files)
- cGy also used for kerma; exposure-to-dose f-factor → **COVERED** (m12)
- Critical absorption energy / K-edge → **PARTIAL** (m04 one mention)

### 3.2 Beam characteristics, machines, modifiers (m05, m07, m23, m34)

- Linac chain: electron gun, waveguide, klystron/magnetron, bending magnet, target, flattening filter, scattering foil, monitor chamber → **COVERED** (m07; thyratron/modulator specifically **PARTIAL**, 2 passing mentions)
- Cyclotron accelerates heavy charged particles; proton therapeutic energies 150–250 MeV; Bragg peak / SOBP → **COVERED** (m07, m19)
- Betatron / microtron → **MISSING** (m07; historical, low priority)
- Forward-peaked MV x-ray emission → **COVERED** (m04)
- Geometric penumbra = s·(SSD + d − SCD)/SCD; depends on source size, SCD, SSD → **COVERED** (m05, m36; 25 files)
- Physical penumbra = 80–20 % lateral distance → **COVERED** (m05, m19)
- Horns / off-axis ratio / profile flatness & symmetry → **COVERED** (m05, m42)
- Light field edge ≈ 50 % isodose; radiation/light coincidence 2 mm → **MISSING as a stated rule** (light field appears in 13 files, but the 50 % relation is never stated; m05/m42)
- Surface dose decreases with photon energy (skin sparing); increases with field size, trays, obliquity → **COVERED** for energy; **PARTIAL** for field-size dependence (2 passing hits, m05)
- Carbon-fiber couch raises skin dose → **COVERED** (m34)
- Wedge angle definition (isodose tilt at 10 cm); hinge angle = 180 − 2·wedge angle → **COVERED** (m34; 16 files)
- Wedge factor depends on field size and depth; dynamic / EDW; wedge pair isodose shape → **COVERED** (m34)
- Cerrobend / Lipowitz melting point, 5 HVL block ≈ 3–5 % transmission → **COVERED** (m34)
- Tray factor; source-to-tray distance and block divergence → **COVERED** / **PARTIAL** (divergence geometry only once, m34)
- Compensator mounted 15–20 cm off skin; missing-tissue compensation → **COVERED** (m34)
- MLC rounded-leaf / scalloped penumbra; collimator 90° to put leaf motion in the short axis → **COVERED** / **PARTIAL** (collimator-angle trick once, m23)
- Electron rules: dmax ≈ E/4, R₉₀ ≈ E/4, R₈₀ ≈ E/3, Rp ≈ E/2, ~2 MeV/cm → **COVERED** (m05, m19; 12 files)
- Electron surface dose rises with energy; x-ray contamination %; bremsstrahlung tail → **COVERED** (m05, m19)
- Electron lead shield ≈ E/2 mm Pb; internal shields need low-Z coating against backscatter; tungsten eye shields to ~9 MeV → **COVERED** (m34)
- Electron cutout output factor and MU; new cone requires measurement → **COVERED** (m35, m42)
- Electron virtual/effective SSD; air-gap effect on output and penumbra → **COVERED** (m05, m35)
- Electron obliquity shifts dmax shallower → **COVERED** (m19)
- Electron PDD vs field size (small fields lose depth) → **PARTIAL** (one line, m19)
- Skin collimation for electrons → **MISSING** (m34)
- Electron arc therapy → **MISSING** (m24; rare)
- Electron chest wall / lung interface dose; air-cavity (ethmoid) hot spot → **COVERED** / **PARTIAL** (air cavity in 6 files, ethmoid-specific example absent; m37)
- Photon/electron abutment hot and cold; electron junction feathering → **COVERED** (m25, m36)
- Field size scales linearly with distance; magnification = SID/SOD → **COVERED** (m08; 21 files)
- Block-cutter: film distance and tray distance geometry → **MISSING** (m08)
- Block shift via magnification (moving a block on the film vs at tray) → **MISSING** (m08)
- Magnification ring / known-size marker → **MISSING** (m08)
- Isocenter placed anterior/posterior changes projected field size → **PARTIAL** (one item, m08)
- Mechanical vs radiation isocenter; pointer check → **COVERED** (m42)
- Flattening filter / FFF → **COVERED** (m07)
- Tomotherapy, Gamma Knife, SRS cones (4 mm), beamlet/bixel → **COVERED** (m23)
- Step-and-shoot vs sliding window MU/time → **COVERED** (m23)
- Arc past-pointing technique → **MISSING** (m25; dated)
- Rotational therapy contraindications → **COVERED** (m25)

### 3.3 Dose calculation & planning math (m33, m35, m36, m37)

- PDD dependencies (energy, depth, field size, SSD); TMR dependencies (no SSD) → **COVERED** (m35)
- Given dose = tumor dose / PDD; parallel-opposed entrance/exit dose; dose at depth via PDD ratios → **COVERED** (m35; 10 files)
- Mayneord F factor — corrects PDD for SSD change via inverse square → **COVERED** (m35, m45; 19 files)
- Inverse square generally → **COVERED** (33 files)
- TMR = TAR/BSF; BSF = TAR at dmax; TMR replaces TAR because in-air measurement is impractical at MV → **COVERED** (m35)
- SMR (scatter-maximum ratio) definition → **MISSING** (m35)
- Sc (in-air collimator scatter), Sp, Scp → **COVERED** (m35)
- Equivalent square 4A/P; effective field with blocking; elongated-field inaccuracy → **COVERED** / **PARTIAL** (elongated caveat once, m35)
- Clarkson / SAR sector integration → **COVERED** (m36)
- SSD treated at SAD (or vice versa) dose error ≈ ((SSD+d)/SAD)² → **COVERED** (m33, m36)
- Wrong energy delivered: dose ratio via TMR/PDD → **COVERED** (m36)
- Wedge factor omitted → overdose by 1/WF → **COVERED** (m34, m36; 23 files)
- Temperature–pressure correction → **COVERED** (m09)
- Orthovoltage timer calculation with BSF and timer error → **COVERED** (m36)
- Gap calculation ½·L₁·d/SSD₁ + ½·L₂·d/SSD₂ → **COVERED** (m36; 46 files)
- CSI collimator angle arctan(½L/SSD) and couch angle arctan(½L/SAD) → **COVERED** (m36; 6 files)
- Half-beam block / non-divergent junction; junction error vs penumbra → **COVERED** (m25, m36)
- Lateral + supraclav match with cord block; tangent posterior edge non-divergent → **COVERED** (m25)
- Hemibody: SAD extension to cover length, dose-rate at extended distance → **PARTIAL** (extended-distance math present in m36; hemibody as a named procedure absent, m24)
- Effective path length / CET / lung density 0.25–0.3 → **COVERED** (m37; CET named once)
- Isodose shift method → **COVERED** (m37)
- CT number to electron density; HU definition; lung ≈ −750, air −1000 → **COVERED** (m11)
- Window / level arithmetic → **COVERED** (m10)
- Voxel volume calc → **COVERED** (m10, m27)
- Calculation grid size vs speed/accuracy → **COVERED** (m33)
- Algorithm hierarchy: pencil beam < convolution-superposition < Monte Carlo; MC most accurate, slowest; kernels derived by MC → **COVERED** (m33)
- Air cavity loss of electronic equilibrium → **COVERED** (m37)
- Water-equivalent phantom electron density → **COVERED** (m09)
- EQD2 / BED conversions; cord EQD2 → **COVERED** (m21, m43; 21 files)
- Partial treatment / interrupted fraction; missed days → **COVERED** (m42)
- Dose prescription to isodose vs isocenter rescale → **COVERED** (m25)
- Three-field wedge weighting; 4-field box femoral-head weighting → **COVERED** (m25)
- Cord-block fraction counting (how many fractions before block given a limit) → **MISSING as an item type** (arithmetic trivial; m36)
- Integral dose comparison across energies → **COVERED** (m19)
- Delta/differential vs cumulative DVH; bin size → **COVERED** / **PARTIAL** (bin size twice)

### 3.4 Planning concepts, volumes, imaging (m10, m13–m19, m25–m30, m38, m39)

- ICRU 50/62/83 volumes: GTV, CTV, ITV, PTV, treated/irradiated volume, PRV, prescription to volumes, D2/D98/D50 homogeneity → **COVERED** (m19, m13)
- Biological target volume (BTV) → **MISSING** (m19)
- ICRU 24 ±5 % dose-accuracy goal → **MISSING** (m39)
- Organ motion as largest uncertainty; systematic vs random error; TG-76 >5 mm → motion management; slow CT, 4DCT, gating → **COVERED** (m15, m39; slow-CT once)
- Gating not needed for nasopharynx → **COVERED** (m15)
- Prostate motion / fiducials; bladder-filling protocol; belly board; bowel bag → **COVERED** except **MISSING** bowel bag (m22/m25)
- DRR generation; DRR resolution improves with thinner slices → **COVERED** (m16)
- Diagnostic CT limitations (curved top, FOV, no indexing) → **COVERED** (m16)
- CT FOV vs pixel size; partial-volume effect; contrast resolution → **COVERED** / **PARTIAL** (contrast resolution once)
- MRI sequences T1/T2/FLAIR; MRI distortion; prostate volume smaller on MRI than CT → **COVERED** / **PARTIAL** (MRI-vs-CT prostate volume once, m10)
- PET uses; PET in atelectasis → **COVERED**
- Titanium applicators cause CT artifact → **COVERED** (m10)
- Image registration / deformable → **COVERED** (m17, m38)
- IGRT: CBCT dose reduction; portal image contrast is Compton-limited; EPID → **COVERED** (m18)
- Adaptive RT definition; weight change → replan → **COVERED** (m28)
- Autocontouring, autoplanning → **COVERED** (m29, m30)
- Field-in-field; BEV; DVH; EUD; serial vs parallel → **COVERED**
- SBRT: non-coplanar conformality, RTOG 0915 R50/D2cm, prescription IDL 60–90 %, immobilization → **COVERED** (m19, m20); SBRT immobilization as a stand-alone fact **PARTIAL**
- IMRT: leaf motion, dose painting, TG-119-style QA → **COVERED** (m23, m42)
- Breast: tangents, lung included, IMN separate field, posterior edge match, normalization point, surgical clips for boost, contralateral scatter → **COVERED** (m25)
- RTOG breast atlas CTV borders → **MISSING** (m22)
- APBI eligibility; HDR balloon 34 Gy/10 BID → **MISSING** eligibility; **COVERED** dose (m40)
- TBI: lung-limiting, spoiler, compensators; TSEI → **COVERED** (m24)
- H&N 3-field with posterior electrons; electron energy chosen for nodes vs cord; parotid mixed photon/electron → **COVERED** (m25)
- Vertex field; whole-abdomen kidney shielding; Wilms whole-vertebra inclusion; seminoma hockey stick → **COVERED**
- Bladder field superior border → **PARTIAL** (once)
- Retrograde urethrogram to find prostatic apex → **MISSING** (m16/m22; dated)
- Maxillary antrum head position → **MISSING** (m14)
- Pediatric planning considerations (anesthesia, growth plates) → **COVERED** (2 files)
- Pediatric second-malignancy risk → **MISSING** (m21/m41)

### 3.5 Brachytherapy (m40)

- HDR vs LDR advantages; ICRU 38 dose-rate classes → **COVERED**
- Point A (Manchester) definition; TRAK; tandem & ovoid geometry → **COVERED**
- Permanent-implant dose, decay-corrected HDR time, Sr-90 applicator timer → **COVERED**
- I-125 properties (28 keV, HVL ≈ 0.025 mm Pb); Ir-192 HVL in lead (~3–6 mm) → **COVERED** (m03, m40)
- Uveal melanoma plaque 85 Gy; base-of-tongue boost → **COVERED**
- Autoradiography for source uniformity; leak test every 6 months; written directive; NRC medical event → **COVERED** (m40, m41)
- Brachy TPS accuracy; isotropic sources → **COVERED**
- Sievert integral / linear-source tables → **MISSING** (m40; dated)
- Prostate seed pre-plan allowances (extra seeds, needle count) → **MISSING** (m40)
- Source-storage ventilation (radon from radium) → **MISSING** (m41; obsolete)
- Quimby / Paterson-Parker systems → **PARTIAL** (named in 2 files, no rules)

### 3.6 Radiation protection & regulation (m41)

- NCRP 116: occupational 50 mSv/y, cumulative 10 mSv × age, lens 150 mSv, skin/extremities 500 mSv, public 1 mSv (5 mSv infrequent), public lens 15 mSv, embryo 0.5 mSv/month, negligible 0.01 mSv → **COVERED** (m41; negligible-dose once)
- ALARA levels, badge placement, film-badge filters, pocket dosimeter, GM counter for surveys & gas multiplication → **COVERED** / **PARTIAL** (pocket dosimeter once)
- Shielding: workload/use/occupancy, primary/secondary barriers, TVL, maze, neutron door, boronated polyethylene → **COVERED**
- Lead-apron transmission calc → **COVERED** (2 files)
- Neutron production above ~10 MV; prostate IMRT energy choice → **COVERED**
- Radiation area signage; 10 CFR 20 minors → **COVERED**
- Stochastic vs deterministic; LNT; low-dose genetic effects; fetal 8–15 wk mental retardation → **COVERED** / **PARTIAL** (genetic effects once)
- Cataract threshold (modern ~0.5 Gy) → **PARTIAL** (one planning-b item)
- Collective dose (person-Sv) → **MISSING**
- Background radiation ≈ 3 mSv/y → **MISSING**
- Cytogenetic (dicentric) dosimetry → **MISSING**
- HIPAA / privacy; nosocomial infection control → **MISSING** (m01 scope-of-practice)
- Scope of practice / supervision / AAMD documents / charge capture → **COVERED**

### 3.7 QA & standards (m42, m09)

- TG-142 daily output, lasers, door interlock, kV/SRS imaging 1 mm; TG-40; TG-51; TG-21 Ngas; buildup cap; parallel-plate for electrons/surface → **COVERED** (TG-40 and parallel-plate once each → **PARTIAL**)
- ODI daily; monitor-chamber symmetry; isodose agreement 2 %/2 mm; in-vivo diodes; weekly chart check; R&V; checksum → **COVERED** (checksum once)
- TPS acceptance / commissioning → **PARTIAL** (one mention)
- Ion-chamber saturation / recombination → **MISSING** (m09)

### 3.8 Radiobiology (m21)

- LQ model, shoulder, 4 Rs, α/β early vs late, OER, LET/RBE/overkill, cell-cycle sensitivity (M, G2 sensitive; late S resistant), T1 larynx 2.25 Gy/fx → **COVERED**
- Mitosis sub-phases (metaphase etc.) → **PARTIAL** (cell cycle present; mitosis phases not named)
- Mitotic index drives early response → **MISSING**
- Hyperfractionation rationale (late-tissue sparing) and H&N local-control gain → **MISSING** (BID small-cell schedule is present, but the rationale item is not)
- Lymphocytes most radiosensitive; Bergonié–Tribondeau → **MISSING**
- LD50/60 ≈ 3–4 Gy → **PARTIAL** (once)
- Phase I trial = dose escalation → **COVERED**

### 3.9 Anatomy & oncology (m20, m22, m43)

- QUANTEC: cord 50/60/69, kidney V12 < 55 %, optic nerve/chiasm 54–55 (>60 risky), brainstem 54, brain necrosis, rectum V70, lung V20/MLD, liver, parotid mean → **COVERED** (m43)
- Pancreas 4-field; QUANTEC pancreas-region constraints → **COVERED**
- Brain anatomy: clivus, pons, basilar, optic tracts/chiasm, temporal lobe/hippocampus → **COVERED** (m22); corpus callosum / pituitary stalk → **MISSING**
- Fossa of Rosenmüller; foramen lacerum (nasopharynx) → **MISSING** (m22)
- Mandible ramus; seminal vesicles; inguinal node depth; femoral-head contour; brachial plexus → **COVERED**
- Gallbladder → **MISSING** (m22)
- Esophageal survival; pancreatic survival; prostate 5-yr survival; bladder cure rate → **MISSING** (m20; outcome statistics age quickly — low priority)
- Cervix nodal positivity by stage → **PARTIAL** (2 passing)
- Hodgkin, neuroblastoma, Ewing lung mets, glioblastoma prognosis, HPV favorable, small-cell responsive, seminoma radiosensitive, cord compression 8 Gy, bone-met palliation → **COVERED** (Ewing/HPV once)
- Rectal cancer post-op indications → **COVERED**; pre-op RT reduces late SBO → **MISSING**
- Melanoma adjuvant RT indications → **MISSING**
- Parotid surgery as standard → **MISSING**
- Xerostomia mechanism → **PARTIAL** (parotid constraint present, symptom not named)
- Extremity sarcoma strip sparing; Wilms; H&N SCC most common → **COVERED**
- Ependymoma / adult CNS histologies → **MISSING** (m20)

### 3.10 Informatics (m26, m27)

- DICOM, DICOM-RT objects, PACS, bit/byte, binary, gigabyte 2³⁰, RAM/CPU, Unix, network terms (LAN/WAN/FTP once) → **COVERED** / **PARTIAL**

### Coverage tally

| Mark | Probes | Share |
|---|---|---|
| COVERED | ≈318 | 81 % |
| PARTIAL | ≈28 | 7 % |
| MISSING | ≈48 | 12 % |

Weighted by how many test items each fact drives (missing facts are almost all single-question oddballs; covered facts drive the repeated calc families), **≈85 % of the unique questions are answerable from the current bank.**

---

## 4. Suspicious / wrong / outdated keys (28)

| # | Location | Problem |
|---|---|---|
| 1 | T6 Q42 | Output factor is keyed as the backscatter factor; the item describes a relative output factor (Scp). |
| 2 | T6 Q43 | Mitosis phase keyed A; the description (chromosomes aligned on the plate) is metaphase. |
| 3 | T7 Q2 → 2023 T1 / 2025 T1 | QUANTEC item keyed to a kidney statement; the stomach constraint option matches QUANTEC better. |
| 4 | T8 Q12 | SSD-vs-SAD error: key 660 cGy; recomputing gives ≈641 cGy. |
| 5 | T8 Q13 → 2023 T2 Q11 | Two HVLs for μ = 0.94 cm⁻¹ keyed 2.72 cm (that is the μ = 0.51 answer); correct ≈1.47 cm. Fixed in 2025. |
| 6 | T8 Q34 | Gigabyte written as "2 e30" (should be 2³⁰). |
| 7 | T9 Q17 | Prefix matching: 10⁻² paired with micro; 10⁻² is centi, micro is 10⁻⁶. |
| 8 | T9 Q24 | E = hc/λ keyed 1.99×10⁻¹² J; arithmetic gives 1.99×10⁻¹¹ (annotator note agrees). |
| 9 | T9 Q25 | Atoms per gram keyed as N_A × A; should be N_A ÷ A. |
| 10 | T10 Q18 vs T5 Q46 | 6 MeV surface dose 75 % in one test, 80 % in another. |
| 11 | T5 Q38 vs T7/T11 | Penumbra defined 20–90 % in one place, 20–80 % elsewhere. |
| 12 | T11 Q17, Q22 | Stems/options grammatically ambiguous; two options defensible. |
| 13 | T11 Q47 → 2023/2025 | Mayneord factor keyed "corrects PDD" while T5 Q13 keys "inverse square"; both accepted but inconsistent. |
| 14 | T11 Q50 | Ir-192 shielding options unitless; 20.8 mm = 2.1 cm. |
| 15 | T12 Q47 | I-125 decay constant computed with 74.2 d (Ir-192 half-life); should be ≈0.0117 d⁻¹. |
| 16 | T12 Q50 | DRR resolution keyed to "increase mAs"; DRR resolution depends on slice spacing/pixel size, not scan mAs. |
| 17 | T12 Q49 / T4 / T14 | Lens limit keyed 150 mSv — NCRP 116 value, but ICRP 118 (2011) is 20 mSv/y; public lens keyed 50 mSv (2018) and 5 mSv (2025) vs NCRP 15 mSv. |
| 18 | T13 Q33 | Cyclotron keyed as producing electrons for the waveguide; cyclotrons accelerate heavy charged particles. |
| 19 | T13 Q35 → 2023/2025 | "Fastest and most accurate" algorithm keyed Monte Carlo; MC is most accurate, not fastest. 2025 added an option that is now arguably correct but key unchanged. |
| 20 | T14 Q38 | SRS kV-imaging scaling keyed ≤2 mm; TG-142 and the other tests say ≤1 mm. |
| 21 | T14 Q42 vs T12 Q9 | Cataract threshold 500 cGy in one test, 200 cGy in another; modern value ~0.5 Gy. |
| 22 | T14 Q43 → 2023 T5 Q32 | Light field keyed to the 75 % isodose; the 50 % line is standard. Fixed in 2025. |
| 23 | T14 Q45 | Wedge item: two options describe the same effect. |
| 24 | 2020 Q3 | Stem changed to "hypofractionation" but key still points to a conventional H&N regimen. |
| 25 | 2020 Q14 | Fundamental unit of information keyed byte; it is the bit. |
| 26 | 2023 T4 Q31 | Key lists two letters ("B C"). |
| 27 | 2023 T4b Q30 → 2025 T5 Q29 | Standard for image/plan transfer keyed PDF; should be DICOM. |
| 28 | 2025 T3 Q3 | Binding energy keyed to a kinetic-energy option. |

Also noted (outdated rather than wrong): Point A defined relative to the external os (T12 Q44, pre-ICRU 89 convention); esophageal survival figures (T9 Q33); reportable-event threshold edited in 2025 to 20 %; 2025 T6 Q15 contains a stray reviewer comment inside the stem; 2005 E1 Q6 cord-block count lands exactly on the limit (7 fx → 4002 cGy) so the intended answer depends on rounding.

Verified-correct worked keys (spot-checked, all agree): Sr-90 applicator 233 s; 95 % IDL weighting 95:47:47; 2 HVL μ=0.51 → 2.72 cm; CSI angles 7.1°/11.3° and 10.8°/5.1°; T/P 1.007; 18-vs-6 MV error 225 cGy; mg-Ra-eq 277; neutron mixed 11 mSv; I-125 2.4 cGy/h → ≈4987 cGy; Tc-99m 22 mR/h; voxel 20 mm³; EPL 8.2 cm; 3 HVL → 30 mm; cord EQD2 50 Gy; block shift 0.75 cm; gaps 1.5/1.2 cm; Co-60 λ 0.13 y⁻¹; HBI SAD 158 cm; MU 221; T½ 74.5 h; 12,500 cGy → 6 cGy/h; Au-198 Γ 0.238; 2005 block-cutter SFD 104 cm; 80-SAD Co-60 field 12×15 at isocenter; orthovoltage timer 4.22 min; HVL 11 mm; penumbra 0.83 cm; arc MU 142; SAD→SSD +21 %.

---

## 5. Summary

- **Unique questions:** ≈560–620 across ~1169 raw items (2020, 2023 and 2025 are reprints of the 2018 Tests 5, 7, 8, 10, 11, 13, 14; the 2005 edition adds ≈60 older-style items).
- **Estimated coverage by our bank:** ≈85 % of unique questions; 81 % of distinct facts COVERED, 7 % PARTIAL, 12 % MISSING.
- **Suspicious keys:** 28 (5 corrected in the 2025 reprint, 2 new errors introduced there).

### MISSING facts / calc types by module

- **m02-fundamentals:** Avogadro's number and atoms-per-gram calc; nuclear binding energy / mass defect; strong vs electromagnetic force; E = hc/λ worked example (PARTIAL).
- **m05-beam-characteristics / m42:** light-field edge = 50 % isodose (explicit rule); surface dose rising with field size (PARTIAL).
- **m07-treatment-machines:** betatron/microtron (historical); thyratron/modulator role (PARTIAL).
- **m08-magnification:** block-cutter film/tray distance geometry; shifting a block on film vs at tray via magnification; magnification ring/marker.
- **m09-radiation-measurement:** ion-chamber saturation/recombination.
- **m14-positioning:** maxillary-antrum head positioning.
- **m16-simulation / m22:** retrograde urethrogram for prostatic apex (dated).
- **m19-isodose-metrics:** biological target volume.
- **m20-site-oncology:** melanoma adjuvant RT indications; parotid surgery as primary therapy; pre-op rectal RT lowering late SBO; ependymoma/adult CNS histologies; survival statistics (esophagus, pancreas, prostate, bladder — low priority).
- **m21-radiobiology:** hyperfractionation rationale and H&N local-control gain; lymphocytes most radiosensitive / Bergonié–Tribondeau; mitotic index vs early response; mitosis sub-phases (PARTIAL); LD50/60 (PARTIAL).
- **m22-anatomy:** fossa of Rosenmüller, foramen lacerum, corpus callosum, pituitary stalk, gallbladder; RTOG breast atlas CTV borders; bowel bag.
- **m24-special-procedures:** hemibody irradiation as a procedure (extended-SAD math exists); electron arc therapy.
- **m25-planning-methods:** APBI eligibility; arc past-pointing (dated); cord-block fraction-counting item type.
- **m34-beam-modifiers:** skin collimation for electrons; tray-distance block-divergence detail (PARTIAL).
- **m35-pdd-tmr-mu:** SMR definition.
- **m39-uncertainty:** ICRU 24 ±5 % accuracy target.
- **m40-brachytherapy:** Sievert integral / linear-source tables (dated); prostate seed pre-plan allowances; Quimby/Paterson-Parker rules (PARTIAL).
- **m41-radiation-protection:** collective dose (person-Sv); natural background ≈3 mSv/y; cytogenetic dosimetry; HIPAA/privacy and infection control; radium storage ventilation (obsolete); cataract threshold modern value (PARTIAL); negligible individual dose (PARTIAL).

### Verdict vs our m44 set

**Complementary, and on balance our m44 set is better.** The MDCB files are the real exam's register — short recall stems, a steady diet of the same ~15 calc families, and heavy anatomy image-ID (which the text extracts lose). Their weaknesses: ~5 % of keys are wrong or internally inconsistent, protection limits are a decade old, and the 2020–2025 "new" editions are reprints. Our m44 items have fuller rationales, current QUANTEC/TG values, and no key errors found in this sweep, but the MDCB set exposes ~50 small facts we never state (block-cutter geometry, light-field 50 % rule, SMR, Avogadro/binding-energy, radiobiology history, several H&N landmarks). Recommended action: author original items for the MISSING list above (≈40 items, priority m02, m05, m08, m21, m22, m41), and add an "inconsistent sources" note to m41 and m42 for the lens-limit, cataract-threshold, and penumbra-definition drift seen across editions.
