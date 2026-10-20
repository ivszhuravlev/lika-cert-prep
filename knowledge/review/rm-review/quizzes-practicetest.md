# RM Review — "All Quizzes" and "AllPracticeTest" coverage report

Scope: two third-party review packets found in `inbox/RM Review/` (text extracted to `inbox/text/All Quizzes.pdf.txt`, ~180 KB, 8,137 lines, 251 PDF pages; and `inbox/text/AllPracticeTest.pdf.txt`, ~277 KB, 13,257 lines, 309 PDF pages). Both are instructor-made board-review handouts (the "Vitamin / Mineral" board-review series), not retired MDCB items. Source files are copyrighted, stay in `inbox/` (gitignored) and nothing below quotes them; every fact is restated.

Method: both text files were read end to end in order. Each quiz/test section was identified and counted (duplicates detected with `diff`). Every item whose answer teaches a concrete fact or calc type was restated and the bank (`knowledge/theory`, `knowledge/questions`, 45 modules, ~1,944 items) was grepped for the term or number. At least 20 numeric answers from each file were recomputed by hand.

Classification key: COVERED = bank teaches the same fact at equal or better depth. PARTIAL = topic present but the specific number/term is absent or appears once in passing. MISSING = fact or calc type essentially absent from the bank.

A warning that affects both files: the answer keys were marked by highlighting/bolding in the original PDF. Text extraction dropped that formatting, so every "Key" section in the text is a verbatim copy of the question block with no answer letter visible. For the quizzes the "Vitamin"/"Mineral" reference pages that follow each quiz supply the intended answers. For the practice tests the only visible answers are (a) the 63 worked calcs, (b) a notes appendix after Test 1, (c) the matching-item blanks in Test 4 key, and (d) a few stray parenthetical tags (for example "RTOG 822", "RTOG 0225") left next to the intended option. Everything else had to be answered independently.

---

## File 1 — "All Quizzes" (quizzes + Vitamin/Mineral reference pages)

### Structure and counts

45 distinct quizzes, ~515 unique items; ~577 printed because Quiz 1 appears twice and Quizzes 18–22 are reprinted verbatim as Quizzes 118–122. About 25 reference pages ("Vitamin n" / "Mineral n") follow the quizzes and carry the facts. Style: short 4-option MCQ (many True/False and 2-option items), one short-answer quiz (brachy sources), one image-identification quiz (brachy applicators, images lost in extraction). No calculations except Quiz 116 (magnification). Items are shallow recall; the reference pages are the real content.

| Quiz | Topic | Items | Key in text? |
|---|---|---|---|
| 1 | Magnitudes (activities, exposures, shielding thickness, clinical doses) | 10 | key block present, letter lost; reference page gives values |
| 2 | HDR | 10 | same |
| 3 | Shielding | 10 | same |
| 4 | Linac QA (TG-142) | 14 | same + summary page |
| 4b | Brachy sources (short answer) | 12 | yes, written answers |
| 5 | Equipment usage (detectors) | 10 | same + summary page |
| V5 | Plan review short test (CI, DVH, hot spots, R50, D2cm, V20) | 10 | same + reference page |
| 8 | Linac parts | 20 | same + Mineral 51 |
| 8b | TG-100 | 12 | same + Mineral 62 |
| 10 | Dose algorithms | 12 | same + Minerals 63, 73 |
| 11 | Linac film tests | 10 | same + Mineral 16 |
| 12 | Neutron shielding | 8 | same + Mineral 21 |
| 13 | TG-142 | 10 | same + Mineral 31 |
| 14 | Threshold energies | 9 | same + Mineral 32 |
| 15 | Surface dose | 9 | same + reference page |
| 16 | Brachy implant types | 10 | same + list |
| 17 | Staging | 12 | same + Minerals 65, 82 (long ACS-style staging essay) |
| 18/118 | IMRT and VMAT | 10 | same + Vitamin 15 |
| 19/119 | HDR planning and process | 9 | same + Vitamin 19 |
| 20/120 | Radiation units | 14 | same + Vitamin 17 |
| 21/121 | Ultrasound | 10 | same + Vitamin 35 |
| 22/122 | FF and FFF | 9 | same + Vitamin 51 |
| 23 | Brachy applicators (image ID) | 9 | same + Vitamin 34 (images lost) |
| 23b | Regulations | 14 | same + Vitamin 24 |
| 24 | LDR prostate | 10 | same + Vitamin 20 |
| 25 | PET | 10 | same + Vitamin 3 |
| 26 | MRI | 10 | same + Vitamin 2 |
| 27 | CT | 12 | same + Vitamin 1 |
| 101 | CT | 15 | key block, letter lost |
| 102 | MRI | 10 | same |
| 103 | PET | 10 | same |
| 104 | Shielding | 15 | same |
| 105 | Plan review | 13 | no key |
| 106 | HDR | 17 | no key |
| 107 | Instrumentation | 16 (printed twice as 1–16 and 17–32) | no key |
| 108 | Pacemakers (TG-203 "new" + "old") | 14 | no key |
| 109 | Data sets / informatics | 10 | no key |
| 110 | Dose outside the field | 10 | no key |
| 111, 112 | SBRT | 10 + 10 | no key |
| 113, 114 | SRS | 12 + 10 | no key |
| 116 | Magnification / minification (calcs) | 11 | no key |
| 117 | Units | 20 | no key |
| 118 | Elementary particles | 7 | no key |

### Fact and calc-type inventory — File 1

Status is against our bank. Values are the ones the handout teaches, restated.

**Magnitudes and clinical doses (Quiz 1, reference page) — mostly m03, m12, m40, m41**
- FDG PET dose ≈ 15 mCi (555 MBq); F-18 half-life ≈ 110 min — MISSING (555 MBq / 15 mCi nowhere in bank; 110 min present).
- Wipe/leak test limit 0.005 µCi (185 Bq) — COVERED (m40, m41).
- Gamma Knife is Co-60, ~6,600 Ci total — COVERED.
- Ir-192 HDR source ≈ 10 Ci; Co-60 teletherapy ≈ 9,000 Ci; Cs-137 blood irradiator ≈ 50 Ci; Cs-137 LDR T&O ≈ 170 mCi (≈70 mg Ra-eq); I-131 ablation ≈ 150 mCi; prostate seed ≈ 0.3 mCi — PARTIAL (10 Ci and 0.3 mCi present; the rest of the order-of-magnitude ladder absent).
- Personnel exposure ladder (cardiac cath ≈ 1,500 mR/yr, PET tech ≈ 500, nuc med ≈ 400, x-ray tech ≈ 300, therapist ≈ 0) — MISSING; low exam value.
- Exposure rates near patients: bedside Cs-137 or I-131 patient ≈ 100 mR/h; unrestricted-area guideline < 2 mR/h in any hour; prostate seed patient ≈ 100 µR/h at 1 m — PARTIAL (2 mR/h rule present in m41; others absent).
- I-131 inpatient release ≈ 5–7 mR/h at 1 m — MISSING and OUTDATED (bank correctly uses the 10 CFR 35.75 dose-based 5 mSv criterion).
- Shielding thickness ladder: linac primary ≈ 8 ft concrete, secondary ≈ 3 ft, HDR suite ≈ 2 ft, CT/diagnostic rooms ≈ 1/16 in Pb, PET 1/8–1 in Pb, door with maze ≈ 3/4 in Pb + 4 in borated poly, door without maze ≈ 6 in Pb + 14 in BPE — PARTIAL (primary 8 ft concrete and 1/16 in Pb appear; BPE door numbers absent).
- Magnitude-of-error ladder: missing wedge 25–300%; normalizing to the 50% field edge ≈ 200%; calibrating at 10 cm vs dmax for 6X ≈ 50% (67 vs 100); heterogeneity on/off 5–30% (lung ≈ 2–3 %/cm); 1 cm SSD error ≈ 3–7%; omitting the TG-51 Pb foil ≈ 0.2% — PARTIAL (missed-wedge and SSD-error calcs covered in m36; the "2–3 %/cm of lung" rule and the Pb-foil magnitude are MISSING).
- Clinical dose ladder: I-125 seed 144–145 Gy; Pd-103 110–125 Gy; trigeminal SRS 90 Gy; prostate IMRT 80 Gy; H&N 70 Gy; lung 66 Gy; breast 60–66 Gy with boost; lung SBRT 48–60 Gy; whole pelvis 45 Gy; PBI 34 Gy/10 fx BID; LDR gyn 30 Gy; WBRT 30 Gy; SRS mets 12–30 Gy; single-fraction bone met 8 Gy — COVERED except PBI 34 Gy/10 BID (PARTIAL, 340 cGy mentioned once) and trigeminal 90 Gy (MISSING).

**HDR (Quizzes 2, 19, 106; Vitamins 6, 19, 34) — m40, m42**
- Ir-192: ~380 keV average, 74-day half-life, ~10 Ci new, source ≈ 3.5–4 mm × <1 mm, anisotropy (self-attenuation) visible on isodoses — COVERED.
- HDR QA: source position accuracy 1 mm; calibration quarterly and at every source exchange and after major repair; well-type (re-entrant) ion chamber for calibration; daily interlocks, room GM monitor, positioning; dwell-time linearity check; patient survey before and after; emergency-procedure drills annually; two independent patient-ID methods; two levels of security for the source — PARTIAL (1 mm, quarterly, survey, and medical-event concepts covered; "re-entrant chamber" named once; dwell linearity, annual drills, 2-level security MISSING).
- Lung (endobronchial) dose prescribed 1 cm from catheter; end dwells carry the longest times — PARTIAL (dwell-weighting idea present, lung specifics MISSING).
- Vaginal cylinder Rx at surface or 5 mm — COVERED (m40 has 7 Gy × 3 at 0.5 cm).
- Point A = 2 cm up, 2 cm lateral; largest ovoid preferred; ring has no anterior/posterior shielding and is easier to place; Syed template for extensive gyn disease; Freiburg flap and Leipzig applicator for skin — Point A COVERED; ovoid size, ring shielding, Syed, Freiburg/Leipzig all MISSING.
- PBI balloon devices (MammoSite single/4-lumen, Contura 5-lumen, SAVI strut device): target is a 1 cm shell around the balloon ("PTV_eval"), 34 Gy in 10 fractions BID, balloon-surface dose ≈ 200%, multi-lumen spares skin — MISSING entirely (no APBI/balloon brachytherapy in the bank).
- Treatment-time scaling with decay: t2 = t1 × A1/A2; Ir-192 loses ≈ 1 %/day so a 10-day delay adds ≈ 10% time — COVERED (m40 Q on decay-corrected dwell time; m03).
- Air-kerma strength unit 1 U = 1 µGy·m²/h = 1 cGy·cm²/h — COVERED.
- Planning methods: manual, dose-point optimization, volume optimization, graphical optimization; some centers delete dwells < 1 s — MISSING (graphical optimization never named).
- HDR prostate kept < 120% centrally to spare urethra; HDR gives fewer urethral hot spots than LDR — MISSING.
- Typical HDR prescriptions quoted: T&O 7 Gy × 4; lung 5 Gy × 3; esophagus 8 Gy × 2; PBI 3.4 Gy × 10 — PARTIAL (T&O covered; others absent).

**Shielding and neutrons (Quizzes 3, 12, 14, 104; Minerals 21, 32) — m41, m06**
- Linac neutrons arise in the head (target, flattening filter, collimators), practically only above ~10 MV (threshold ≈ 8 MeV in high-Z, material dependent); 6X none, 10X a few, 15X/18X many; electrons produce far fewer — COVERED (13 files).
- NCRP 151 for linac vaults, NCRP 147 for diagnostic/CT rooms — NCRP 151 COVERED; NCRP 147 MISSING.
- Borated polyethylene (≈5% boron) on the linac side of the door; neutron capture in hydrogen yields a 2.2 MeV gamma so lead goes on the outer side; 4 in with maze, 10–14 in without — PARTIAL (BPE named once; thicknesses and 2.2 MeV capture gamma MISSING).
- Concrete chosen for cost; densities Pb 11.3, concrete 2.35, water 1.0 g/cm³ (steel 7.8–8.0) — COVERED.
- Primary barrier ≈ 6 TVL; head leakage 0.1% at 1 m; use factor 0.25 for primary walls, 1 for leakage; design goals P = 0.02 mSv/wk unrestricted (1 mSv/yr) and 0.1 mSv/wk restricted (5 mSv/yr); W in cGy/wk, U and T dimensionless — COVERED (m41 has P, U, T, W, leakage; TVL count PARTIAL).
- Pair production threshold 1.022 MeV; triplet 2.044 MeV; photoelectric/Compton threshold is just the binding energy; β+ decay needs 1.022 MeV excess — COVERED (triplet PARTIAL, one mention).

**Linac QA and film tests (Quizzes 4, 11, 13; TG-142 summaries; Mineral 16, 31) — m42**
- TG-142 cadence: daily output 3%, monthly output 2%, annual TG-51 1%; lasers 2 mm (3D) / 1.5 mm (IMRT) / 1 mm (SRS-SBRT); monthly gantry-collimator-couch angle 1°; field size 2 mm (symmetric) / 1 mm (asymmetric); MLC 2 mm (3D) / 1 mm (IMRT); picket fence weekly; flatness and symmetry 1% from baseline; dynamic wedge factor monthly; imaging uniformity, registration, scaling, contrast, resolution monthly; imaging dose annually; "baseline" = commissioning values — COVERED (14 files on TG-142; 1.5 mm IMRT laser and weekly picket fence present).
- Film types: XTL localization 1–10 cGy, XV verification 10–100 cGy, EDR2 for IMRT 10–500 cGy, radiochromic needs no processing and should be read ≥24 h after exposure — PARTIAL (EDR/XV and radiochromic named; dynamic ranges and 24 h wait MISSING).
- Star shot tests collimator (and couch) radiation-isocenter; spoke shot tests gantry; Winston-Lutz checks radiation vs mechanical isocenter for SRS — Winston-Lutz COVERED; star/spoke shot MISSING.

**Detectors and instrumentation (Quizzes 5, 107; summary page) — m09**
- Farmer 0.6 cc (or 0.3 cc) for photons; parallel-plate for low-energy electrons; well-type chamber for HDR/LDR sources; dose calibrator for nuc med doses; NaI well scintillator for wipes (≈30,000× more sensitive than an ion chamber); GM to find lost seeds and leaks; hand-held ion chamber for area surveys; rem-ball (moderated proportional counter) for neutrons; proportional counter discriminates alpha from beta; diode arrays for IMRT QA; point detectors = diode, micro-chamber, film; NaI scintillators in gamma cameras, thyroid probes, hand-held meters; personal dosimeters film, TLD, OSL; IROC phantoms use TLD (≈5%) or OSL (≈3%) — PARTIAL (Farmer, parallel-plate, GM, OSL, diodes covered; rem-ball, proportional counter, NaI well counter, IROC MISSING).
- Diode problems: energy, angular, temperature dependence; GM saturates at high rates; most common TLD is LiF; TLD glow curve = light vs temperature; film H&D curve = OD vs log exposure; film is energy dependent at kV — PARTIAL (LiF and diode properties covered; glow curve and H&D curve MISSING).
- Amorphous-silicon flat panels for EPID and OBI; EPID for IMRT QA needs a dose-calibration curve; OBI kV tube 90–140 kVp — MISSING (a-Si never named).

**Plan review metrics (Vitamin 5, Quiz 105) — m19**
- CI = Rx-isodose volume / PTV volume; CI > 1 means dose spills outside, CI < 1 means part of the target is uncovered; Conformation Number = (TV covered)² / (TV × irradiated volume); Homogeneity Index = (D1% − D99%)/Rx; Inhomogeneity Index = (max − min)/mean; ICRU 83 HI = (D2% − D98%)/D50% — CI COVERED (10 files); conformation number MISSING; HI PARTIAL (one mention).
- DVH axes (cumulative: % or absolute volume vs dose; differential: frequency of voxels vs dose); DVH cannot show where a hot spot is; global max = single voxel (often reported to 0.03 cc) — COVERED (bank uses 0.035 cm³).
- Typical hot spots: 3D 105–107%, IMRT 107–110%, VMAT ≈ 110%, SBRT 120–130% (Rx often to 60–80% line), Gamma Knife 200% (Rx to 50%), brachy 300–400% — PARTIAL (SBRT/GK normalization concept present; the full ladder not stated).
- R50 = 50% isodose volume / PTV volume; D2cm = max dose 2 cm from PTV (RTOG 0813/0915); lung V20 ≤ 37% (conventional) and ≤ 10% (SBRT) — COVERED.
- Acceptable target DVH example: ≥95% PTV at 100%, ≥99% at 95%, <10% above 107% — PARTIAL.

**Linac components (Quiz 8, Mineral 51) — m07, m23**
- 3 GHz (S-band), 10 cm wavelength; RF driver only with klystron; klystron is a linear amplifier for high-energy machines, magnetron a circular oscillator for low-energy; RF waveguide filled with SF6 insulating gas and rectangular; accelerating guide evacuated, traveling or standing wave; electron gun diode or triode (grid); isolator/circulator protects the klystron from reflected power; steering coils around the guide; bending magnets 90° (chromatic), 270° (achromatic), slalom 45/45/112.5 (achromatic); target W or Au, 30–50% efficient at MV; primary collimator ≈ 3 TVL (0.1%); flattening filter per energy, hardens the beam; two transmission dose chambers monitor output, flatness, symmetry, dose/pulse; jaws tungsten ≈ 0.5% transmission; MLC tungsten, intraleaf 1–2%, interleaf 2–4%, rounded ends keep penumbra constant; EPID/OBI a-Si; cooling: water for target, oil for klystron, fans for electronics; modulator = PFN + thyratron — PARTIAL: magnetron, klystron, achromatic 270°, interleaf/intraleaf leakage, circulator COVERED; SF6, 3 GHz/10 cm, steering coils, PFN/thyratron, triode gun, slalom magnet, jaw 0.5%, a-Si panel, cooling MISSING.

**TG-100 (Quiz 8b, Mineral 62) — m42**
- RPN = O × S × D, each 1–10, range 1–1000, RPN > 125 flagged; FMEA finds weak controls, fault tree traces root causes left (failure) to right (causes); process map; most IMRT failures are human (≈35%), then lack of procedures and training (≈15% each) — PARTIAL (RPN and FMEA present; fault tree and the failure-cause percentages MISSING).

**Dose algorithms (Quiz 10, Minerals 63, 73) — m33, m37**
- TERMA vs KERMA; dose = TERMA convolved with a Monte Carlo-derived kernel; convolution is spatially invariant (homogeneous assumption); superposition scales kernels by density (radiological distance) and handles heterogeneity and divergence; collapsed-cone is faster (M×N not N³); halving grid spacing multiplies calculation time ≈ 8× (2³); pencil beam is 2D and not acceptable for lung SBRT; Monte Carlo most accurate; TAR₀/TMR₀ are zero-field primary; Clarkson TAR = TAR₀ + SAR; AAA and Acuros grouped with superposition; brachy algorithms: along-and-away, TG-43, Boltzmann solvers, MC; protons: pencil beam, MC; robust optimization is an optimizer not a dose engine — COVERED (kernel, superposition, CCC, MC, Clarkson, zero-area TAR, grid size all present); TERMA by name and "spatially invariant" wording MISSING.
- Handout error: lists AAA as "deterministic." AAA is a convolution-superposition pencil-kernel model; Acuros XB is the deterministic (LBTE) solver. The bank has this right.

**Surface dose (Quiz 15) — m05, m34**
- Photons: surface dose falls with energy (handout quotes Co-60 ≈ 40%+, 6X ≈ 30%+, 18X ≈ 20%+ for open large fields), rises with bolus, spoiler, obliquity, smaller SSD; sources are head electron contamination and Compton electrons in tissue. Electrons: surface dose rises with energy (6E ≈ 75%, 9E ≈ 80%, 20E ≈ 93%), bolus, obliquity; bolus shifts the PDD so surface dose can be read off the curve — COVERED (17 files). The photon percentages quoted are at the high end (textbook 10×10 values are ≈ 15–20% for 6X, ≈ 10–15% for 18X).

**Brachy implant classification and sources (Quizzes 4b, 16, 23) — m40**
- Interstitial (prostate, sarcoma, base of tongue, Syed, breast needles, brain); intracavitary (T&O, cylinder, balloon PBI); intraluminal (esophagus, bronchus, bile duct, nasopharynx); surface (skin, chest wall, nose) — PARTIAL (interstitial/intracavitary used; "intraluminal" and the classification exercise MISSING).
- Source-to-use map: Ir-192 for HDR/Syed; Cs-137 for LDR T&O; I-125/Pd-103/Cs-131 seeds; Y-90 liver mets; I-131 thyroid; P-32 polycythemia vera; Ru-106 eye plaque; Ra-223 bone mets from prostate; Sr-90 pterygium — COVERED (all nuclides present).

**Staging (Quiz 17, Minerals 65, 82) — m20**
- TNM notation (TX, T0, Tis, T1–4, NX, N0–3, M0/M1), clinical vs pathological (c/p), y for post-neoadjuvant, r for recurrence, stage grouping I–IV, grade, FIGO for gyn, no formal TNM for most brain tumors; neoadjuvant = before surgery — MISSING (no TNM primer in the bank; m20 is site oncology). The handout's generic "N1 ipsilateral local, N2 ipsilateral distant, N3 contralateral" is an oversimplification; N categories are site-specific.

**IMRT / VMAT (Quizzes 18, Vitamin 15) — m25**
- 6X (or 10X) preferred: no neutrons, smaller penumbra; 5–9 beams, avoid parallel-opposed, ≥10–15° separation; step-and-shoot minimum ≈ 3 MU/segment (end effect); sliding window faster; IMRT factor 3–10 (avg ≈ 4) more MU; compensator IMRT has finer resolution and fewer MU but wrong-compensator risk; VMAT modulates MLC, dose rate, gantry speed; 2–4 arcs, full/partial, coplanar/non-coplanar, avoidance sectors (> 30°), collimator 15–45° and mirrored between arcs to smear interleaf leakage; VMAT more efficient and conformal — PARTIAL (sliding window, step-and-shoot, compensators, 3 MU covered; IMRT factor, avoidance sectors, collimator-offset rationale MISSING).
- Contestable claim: VMAT has higher integral dose than IMRT. Integral dose is similar; VMAT spreads low dose but reduces MU. Treat as opinion.

**Radiation units (Quizzes 20, 117; Vitamin 17) — m12**
- 1 Ci = 3.7×10¹⁰ dps = 10⁶ µCi; Bq = dps; dps→dpm ×60; R = C/kg measured in air; 1 Gy = 100 rad; f ≈ 0.876 R→rad in air (1 R ≈ 1 rad for safety work); H = D × Q with Q = 1 (photon/electron), 5 (thermal n), 10 (protons of unknown energy), 20 (fast n, alpha) per 10 CFR 20; 1 Sv = 100 rem; fundamental units: dose J/kg, exposure C/kg, activity s⁻¹, capacitance farad, resistance ohm, current ampere, frequency Hz; 555 MBq = 15 mCi — COVERED except the 555 MBq/15 mCi pair (MISSING) and SI electrical units (MISSING, low value). The Q = 10 for protons and 5 for thermal neutrons are the 10 CFR 20 regulatory values, not ICRP 103 (wR = 2 for protons) — exam-relevant but mark as regulatory.

**Ultrasound (Quiz 21, Vitamin 35) — m10**
- 1–20 MHz; speed depends on compressibility and density, ≈ 1,497 m/s in water (≈1,540 m/s soft tissue), higher in metal than air; piezoelectric transducer transmits and receives; attenuation by scatter, absorption, reflection; Fresnel (near) zone used for imaging, higher frequency gives longer near zone and narrower beam; artifacts (reverberation, shadowing, side lobe, mirror); bioeffects heating and cavitation; uses: prostate IGRT, TRUS for seed volume study and implant, balloon-PBI verification; TG-128 for prostate US QA — PARTIAL (speed and TRUS covered; Fresnel/Fraunhofer, cavitation, TG-128 MISSING; low exam weight).

**FF and FFF (Quiz 22, Vitamin 51) — m05, m34**
- Electrons have no flattening filter; one FF per photon energy, located after the primary collimator, hardens the beam, gives horns at shallow depth; Tomotherapy has none; FFF dose rate up to ≈ 2,400 MU/min, peaked symmetric profile, softer spectrum (6X FF ≈ 67% at d10 vs 6X FFF ≈ 61–63%), suited to SBRT — PARTIAL (FFF, 67% covered; 2,400 MU/min and FFF PDD number MISSING).

**Regulations (Quiz 23b, Vitamin 24) — m41**
- Agreement states regulate under state law; NRC governs byproduct material only, states govern x-ray machines/linacs; 10 CFR 19 worker rights, Part 20 dose limits/surveys/signage/contamination, Part 35 medical use (medical-event definitions, 24 h phone and 15 day written report), Part 71 transport (White I, Yellow II, Yellow III labels; Transport Index = mR/h at 1 m); contamination 2,200 dpm/100 cm² beta-gamma on packages; leak test < 0.005 µCi every 6 months; source inventory quarterly; waste decay-in-storage 10 half-lives; storage area survey quarterly; HDR two security barriers — PARTIAL: Agreement states, Part 20, Part 35, medical event, 15 days, 6-month leak test, 0.005 µCi COVERED; Part 19, Part 71, Transport Index, package labels, 2,200 dpm, 10 half-lives, quarterly inventory MISSING.

**LDR prostate (Quiz 24, Vitamin 20) — m40**
- I-125/Pd-103/Cs-131 ≈ 0.3 mCi per seed, 60–120 seeds; TRUS at 5 mm; pre-plan on US, order ≈ 10% extra; assay a 10% sample or rely on third-party assay; Mick applicator or strands; cystoscopy for bladder seeds; GM survey for lost seeds; CT post-plan same day and at ≈ 30 days (ABS); PTV = prostate + 5 mm except 0 mm posteriorly; peripheral loading to spare urethra (< 150%); evaluate V100, V150, V200, D90, rectal dose; base often underdosed — PARTIAL (D90, post-implant concept, seed activity covered; 10% assay, 5 mm margin rule, peripheral loading, V150/V200, Mick, 30-day post-plan MISSING).

**PET (Quizzes 25, 103; Vitamin 3) — m10**
- β+ decay, 511 keV pair, isotopes C-11, N-13, O-15, F-18 (110 min), FDG 15 mCi/555 MBq, 60 min uptake, void before scan, 30–60 min scan; electronic (coincidence) collimation, 10–100× more sensitive than SPECT; BGO/GSO/LSO crystals; resolution ≈ 4–5 mm; corrections for dead time, attenuation, scatter; SUV = ROI concentration / (injected activity / body mass), > 2.5 suspicious; normal uptake brain, heart, liver, kidney, bladder; better for N and M than T staging; artifacts from metal, motion, contrast, truncation via CT attenuation map; F-18 made in a cyclotron; waste held ~10 half-lives (~20 h) — PARTIAL (β+, 511 keV, coincidence, 110 min, SUV, NM staging covered; crystals, 555 MBq, cyclotron, 2.5 threshold, uptake protocol MISSING).
- Handout error: coincidence window quoted as "12 µs"; real windows are ≈ 6–12 ns.

**MRI (Quizzes 26, 102; Vitamin 2) — m10, m17**
- Images H (also F, Na, P); 0.5–3 T; shim coils for uniformity, phased-array/quadrature coils for SNR; steel plates shield the magnet, copper mesh (Faraday cage) shields RF; safety: missile effect, pacemakers, heating, acoustic noise, quench and oxygen displacement, pregnancy caution; resolution ≈ 0.3 lp/mm, spatial accuracy 1–2 mm, geometric distortion worst at the periphery; artifacts chemical shift, wrap-around, zipper, motion; T1: fat and white matter bright, CSF dark; T2: CSF and edema bright; FLAIR = T2 with CSF nulled; Gd shortens T1 and brightens on T1; no ionizing dose; MRI tends to over/under-estimate prostate volume vs CT (handout answers "underestimate" relative to CT) — PARTIAL (T1/T2/FLAIR contrast, Gd, distortion covered; shim, Faraday cage, quench, Tesla range, 0.3 lp/mm MISSING).

**CT (Quizzes 27, 101; Vitamin 1) — m10, m11**
- 3rd generation rotate-rotate with ring artifacts, 4th generation fixed detector ring; HU = 1000(µt − µw)/µw, unitless, based on linear attenuation; fat ≈ −100, organs 30–60, thyroid ≈ 80, metal ≈ 3000; iodine contrast; spatial accuracy ≈ 0.5 mm, resolution ≈ 0.7 lp/mm; more dose → better SNR; CTDI (single slice), CTDIw = ⅓ center + ⅔ periphery, DLP = CTDIvol × length, effective dose = DLP × k, in mSv; pitch = table travel per rotation / beam width, pitch > 1 lowers dose, 1.2 acceptable; FBP vs iterative (less noise, 25–40% less dose); partial volume reduced by thin slices; streak/photon starvation from inadequate technique; HU-to-density curve bilinear because of photoelectric effect in bone; dose reduction via AEC, mA modulation, kV modulation, avoidance angles, iterative recon; monthly QA uniformity, scaling, registration, contrast, resolution; annual dose; external lasers more accurate than internal; scouts not for brachy planning — PARTIAL (HU, pitch, bilinear curve, streak artifacts, HU of tissues COVERED; CTDI/CTDIw/DLP/effective-dose chain, iterative reconstruction, ring artifact, 0.7 lp/mm, AEC, thyroid HU MISSING).
- Handout error: Quiz 27 Q3 implies DLP = effective dose × length; DLP = CTDIvol × length.

**Pacemakers / CIEDs (Quiz 108) — m31**
- TG-203: risk tiers low (< 2 Gy, not pacing dependent), medium (2–5 Gy or pacing dependent), high (> 5 Gy or neutron-producing beam > 10 MV, protons); keep cumulative device dose < 2 Gy where possible; keep device ≥ 3–5 cm from field edge; use measurements rather than TPS if within ~3 cm of field edge; avoid prolonged direct CT exposure (≈ 3 s rule); check MR-conditional status; older "ICP 2 Gy / ICD 1 Gy" tolerances — COVERED (m31, 14 files).

**Data sets / informatics (Quiz 109) — m26, m27**
- Voxel is 3D; eye distinguishes ≈ 30 grey levels; max dose commonly to 0.03 cc; MRI 256², CT 512², DR 2048²; CT/MRI 2 bytes per pixel (12-bit data); 10 bits = 1,024 levels; TB = 10⁶ MB; 4DCT ≈ 10 phases; calc time scales with grid — COVERED (bit depth, bytes, 4DCT, voxel all present).

**Dose outside the field (Quiz 110) — m41, m06**
- Field edge = 50%; ≈ 5% at 2 cm, ≈ 1% at 10 cm, ≈ 0.2% at 30 cm, ≈ 0.1% at 100 cm (leakage floor); patient scatter dominates near the field, head leakage far away; physical wedge raises out-of-field dose; TPS does not include neutron dose for 18X — PARTIAL (leakage 0.1% and 50% edge covered; the distance ladder MISSING).

**SBRT / SRS (Quizzes 111–114) — m24, m32, m43**
- SBRT sites prostate, lung, liver, spine; heterogeneity correction required; TG-101, RTOG 0813 (central) and 0915 (peripheral); grid ≤ 2 mm; avoid 15X/18X; max dose should sit inside the PTV (ideally GTV); tumor ≤ 5 cm; central tumors riskier; CI < 1.2; GTV = CTV; ITV + 5 mm uniform PTV (or 5 mm axial / 10 mm S-I without 4D); skin = outer 5 mm; brachial plexus contoured C5–T2; ribs contoured within a few cm; avoid skin overlap of beams; 4DCT or breath-hold motion management; patient selection (no distant mets, prior RT, pregnancy) — COVERED (TG-101, 0813/0915, R50, D2cm, V20, grid, ITV all present).
- SRS: Gamma Knife Co-60, 0.3 mm accuracy, internal collimation (Perfexion), max lesion ≈ 3–4 cm, Rx to 50% → 200% hot spot; linac SRS lasers 1 mm, cones give tighter penumbra than MLC, micro-MLC ≈ 2.5–3 mm leaves; fields < 3–4 cm lack lateral equilibrium; frameless masks acceptable; IGRT to ≈ 1 mm; avoid eye entry and metal couch rails; image inferior to C1; multiple mets raise integral dose; a 1 cm beam is ≈ 10 mm at 50%, a 5 mm beam is < 2 mm wide at 95%; film has best resolution for small fields, then diodes/micro-chambers — COVERED (Winston-Lutz, 1 mm, small-field CPE, V12 present); 0.3 mm GK accuracy and cone sizes PARTIAL.

**Magnification / minification calcs (Quiz 116) — m08**
- SOD/SID definitions; M = SID/SOD; minification = 1/M; conventional simulator M ≈ 1.4; object size = measured/M; field scales linearly with distance (30×20 at 100 cm → 105×70 at 350 cm); 40×40 at 45° collimator gives 56.6 cm diagonal, so 156 cm needs 276 cm; isocentric AP/PA skin field sizes = iso size × (100 − d)/100 — COVERED (m08 has 86 magnification hits; the 45°-diagonal TBI-style distance calc PARTIAL).

**Elementary particles (Quiz 118) — not an exam topic**
- Quarks, leptons, bosons, atom 10⁻¹⁰ m, nucleus 10⁻¹⁴–10⁻¹⁵ m, electron 10⁻¹⁸ m — MISSING and exam-irrelevant.

### Recomputed answers — File 1
Only Quiz 116 contains arithmetic. All 5 numeric items check: 14/1.4 = 10 cm; 30×20 → 105×70 at 3.5 m; 156/56.57 × 100 = 276 cm (option 2.77 m); AP skin field 10 × 92/100 = 9.2 cm; PA 10 × 84/100 = 8.4 cm. No wrong keys, but Quiz 104 asks the density of steel with options 1.00/2.36/4.40/11.30 — no option is correct (steel ≈ 7.8–8.0 g/cm³).

### Outdated or exam-irrelevant content — File 1
- I-131 release at "< 5–7 mR/h at 1 m": pre-1997 criterion; current rule is dose-based (10 CFR 35.75, 5 mSv to any individual).
- Quality factors 10 (proton) and 5 (thermal neutron): 10 CFR 20 values; ICRP 103 uses wR = 2 for protons. Keep as regulatory.
- "Deterministic = AAA": wrong (Acuros XB is deterministic).
- PET coincidence window "12 µs": should be nanoseconds.
- Quiz 27 Q3 DLP definition inverted.
- Personnel exposure ladder, elementary particles, ultrasound Fresnel/Fraunhofer and cavitation, MRI quench procedures: not MDCB content.
- Old pacemaker tolerances (ICP 2 Gy / ICD 1 Gy) are superseded by TG-203 tiers; the handout correctly labels them "old."
- Film dosimetry (XV, EDR2 dynamic ranges) is largely obsolete; keep only radiochromic.

---

## File 2 — "AllPracticeTest" (calcs inventory + topic bank + four practice tests)

### Structure and counts

| Section | Lines | Items | Keys |
|---|---|---|---|
| Calcs self-assessment (63 calc prompts with worked answers) | 1–700 | 63 (≈52 with numeric answers; #24–28 and a few definitions left blank) | yes, worked |
| Commentary on 2013/2014 MDCB practice-test items (mag block shift, HVL from µ, PDD ratio, bolus taper, iso shift, MRI T1 for fusion, vertex field size, head-leakage film, TMR via e^−µx, BED→total dose) | 700–1050 | 11 solution notes | yes |
| Calculation inventory (methods for the same 63 calc types, with formula "vitamins") | 1050–1650 | 63 method entries | n/a |
| Topic bank (23 topic headings, 4-option MCQ) | 1650–3510, reprinted 3516–5377 | 293 unique | key copy present, letters lost |
| Practice Test 1 (150 Q) + notes appendix | 5378–7790 | 150 | key copy identical; 6 items annotated |
| Practice Test 2 (150 Q) | 7791–10252 | 150 | key copy identical, letters lost |
| Practice Test 3 (100 Q) | 10253–11766 | 100 | key copy identical; a few parenthetical protocol tags survive |
| Practice Test 4 (100 Q) | 11767–13257 | 100 | key copy identical; matching answers survive (Q1–5, 26–30, 73–76) |

Unique items ≈ 63 + 293 + 500 = 856 (plus 63 method notes and 11 commentary notes). Topic-bank headings and counts: fundamental physics 10, atomic/nuclear 8, kV production 10, MV production 17, interactions 11, units 10, measurement/calibration 18, photon dosimetry 21, electron dosimetry 15, CT 10, MRI 10, PET 10, simulation/verification 10, informatics 12, prescribing/reporting 14, IMRT/VMAT 8, special procedures 18, brachytherapy 17, protons 10, SRS/SBRT 17, QA 10, protection/shielding 17, safety/TG-100 10.

Style: Tests 1 and 2 share ≈ 60 items (same stems, sometimes reordered options); Test 3 and 4 reuse ≈ 40 more. Roughly 35 items are image-identification (anatomy on CT/MR, linac components, detectors, DVH shapes, isodose plots) whose images did not survive extraction. About 45 items across the four tests are calculations. The rest is recall at MDCB level. Several stems are sloppy (see wrong/ambiguous list).

### Fact and calc-type inventory — File 2

**Calc types in the self-assessment inventory (63) and where our bank stands**
- Binary → base 10; midpoint and distance between points; log10 of powers of ten; sin/cos/tan and Pythagoras; degrees in circle/triangle/sector — COVERED (m27 binary; trig used in m14/m16), sector/pie arithmetic MISSING (trivial).
- Decay: A = A₀e^(−0.693t/T½); solve for A₀, for T½ (via ln), for time to 25% (two half-lives) — COVERED (m03).
- Attenuation: I = I₀e^(−µx); µ = 0.693/HVL; HVL from two intensities; TVL = 3.32 HVL; transmission through mixed TVL+HVL stacks, fractional TVL (0.1^0.5 = 0.316); attenuated = 1 − transmitted — COVERED (m36, m41).
- Line source (1/d) vs point source (1/d²) exposure scaling, with "point-source rule valid beyond ≈ 2× source length" — PARTIAL (inverse square covered; line-source 1/d approximation MISSING).
- OAR = off-axis reading / CAX reading at the same depth — COVERED.
- PDD at extended SSD (Mayneord); MU for SAD/SSD with TMR/PDD, Sc, Sp, WF, norm; calibration-geometry ISL (SAD-calibrated, SSD setup: divide by (100/101.5)² = 0.971 for 6X) — COVERED (m35, 19 Mayneord hits).
- Air-gap dose: D2 = D1 × TMR2/TMR1 (same depth, different SSD) — COVERED.
- Parallel-opposed dmax dose = entrance + exit contributions via TMR ratios and ISL — COVERED.
- SMR = TMR − TMR₀ — MISSING by name (SAR covered).
- Gap calc for SSD/SSD and SAD/SAD fields: gap = Σ (L/2)(d/SSD) — COVERED (46 "gap" hits).
- CSI collimator twist = tan⁻¹((L/2)/SAD) ≈ 11° for 40 cm spine at 100 cm; "0.57 rule" shortcut (angle ≈ 0.57 × half-length at 100 cm) — COVERED (17 hits, 0.57 rule present).
- Image file size = images × pixels × bits; bits vs bytes; transfer time = size/speed; 10-bit depth needs 2 bytes — COVERED (m27).
- HDR time scaling with decay (Ir ≈ 1%/day) — COVERED.
- Exposure from mg Ra-eq: X = A × Γ / d² with Γ(Ra) = 8.25 R·cm²/(mg·h); unit traps (m vs cm) — COVERED (m40, m45).
- Air-kerma unit U — COVERED.
- Effective half-life — COVERED (3 files).
- Permanent-implant total dose = 1.44 × T½ × 24 × initial dose rate — COVERED (m45 worked item).
- Electron MU = D / (cone factor × cutout factor × ISL × norm), ISL = ((VSD + dm)/(VSD + dm + gap))², gap = SSD − 100 — COVERED (17 cone/cutout hits, VSD 4 hits).
- Electron rules: Rp ≈ E/2, d90 ≈ E/3.2, d80 ≈ E/2.8, therapeutic range ≈ E/4, mean energy ≈ 2.33–2.4 × R50, ≈ 2 MeV/cm loss, Pb thickness ≈ E/2 mm — COVERED.
- Workload: W_primary = patients/day × 5 × dose/fraction (no IMRT factor); W_leakage adds the IMRT factor to the IMRT fraction — PARTIAL (workload present; IMRT-factor split MISSING).
- Barrier transmission B = P d²/(W U T) with P in mSv (or mGy)/wk and W converted ×10 from cGy to mGy; leakage B_L = 1000 P d²/(W T); expected magnitudes (primary 10⁻⁵–10⁻⁶, leakage 10⁻²–10⁻³) — COVERED (m41 worked example).
- Dose equivalent sum = Σ D × Q — COVERED.
- BED = nd(1 + d/(α/β)); compare regimens; solve for dose/fraction by trial or quadratic — COVERED (m21, 12 BED and 19 EQD2 hits).
- CI, D2cm, R50 definitions; RPN = O × S × D — COVERED.
- CTP correction with °F → °C conversion — PARTIAL (one hit; worth a drill).
- Along-and-away table method for LDR sources (shrink each source to a point, look up cGy/h per mg, multiply by strength, sum) — PARTIAL (5 "along" hits; a worked tabular item MISSING).
- Effective (radiological) depth with density factors (lung 0.25–0.33, fat 0.95, water 1.0, muscle 1.05, soft bone 1.1, hard bone 1.65–1.85) and dose difference ≈ 3%/cm of radiological depth difference — PARTIAL (effective depth 1 hit; 3%/cm rule MISSING).
- Equivalent square 4A/P; circle → square ≈ 0.89 × diameter — COVERED (14 hits).
- Missed-wedge dose = delivered/WF — COVERED (m36).
- CTDIw, DLP, effective dose formulas — MISSING.

**Topic-bank and practice-test facts (restated; grouped by our module)**

m02 fundamentals / m12 units: farad, henry, N/m², e = 1.602×10⁻¹⁹ C, c = 3×10⁸ m/s, Planck J·s, mₑ = 9.11×10⁻³¹ kg, V = IR, E = hν, °C = 5/9(°F − 32), Angstrom = wavelength unit, EM spectrum ordering by frequency/wavelength, 1 amu = 1.66×10⁻²⁷ kg, atom 10⁻¹⁰ m, nucleus 10⁻¹⁴–10⁻¹⁵ m, quarks/leptons — mostly MISSING (constants and SI electrical units never appear; Angstrom covered). Low exam weight except isotope/isotone/isobar/isomer (COVERED, 4 files) and the °F→°C conversion (PARTIAL).

m04 kV production: CT x-rays are bremsstrahlung + characteristic; yield rises with Z and kVp; kV efficiency ≈ 1%; mAs does not change max energy; heel effect (more output on cathode side); 120 kVp average ≈ 40 keV; ≈ 80–90% bremsstrahlung at 120 kVp; spectrum shapes with filtration; image intensifier parts (input phosphor, photocathode, output phosphor) in conventional simulators — COVERED except image-intensifier anatomy (MISSING; obsolete).

m07 / m23 MV production: isolator protects klystron; SF6 insulates the RF guide; klystron for 18 MV; traveling guide longer, standing guide fixed-frequency with side-coupled cavities; achromatic magnet keeps energy uniform; primary collimator ≈ 3 TVL; MV bremsstrahlung efficiency ≈ 40%; FF designed to flatten at 10 cm; energy raised by longer guide or more RF power; dose rate by PRF or gun current; electron-mode beam current far lower than photon mode; leakage 0.1%; MV beam more forward-peaked than kV; modulator = PFN + thyratron; 6 MV average ≈ 2 MeV (≈ ⅓ of max; 25 MV ≈ 8.3 MeV); CyberKnife 6 MV; linac gives the highest photon dose rate among Co-60, Van de Graaff, betatron, cyclotron; pulsed microwaves from magnetron or klystron — PARTIAL (magnetron/klystron/achromatic/leakage/⅓ rule covered; SF6, guide types, PFN/thyratron, beam current, FF depth MISSING).

m06 interactions: PE ∝ Z³/E³; Compton Z-independent, dominant ≈ 25 keV–25 MeV in water; PE = Compton near 25–30 keV in water; PP ∝ Z², threshold 1.022 MeV, dominant > ≈ 25 MeV; annihilation photons mostly Compton; 1.022 MeV photon still mostly Compton; 90° Compton photon ≤ 511 keV, 180° ≤ 255 keV; µ in cm⁻¹, µ/ρ in cm²/g; mass stopping power MeV·cm²/g; LET keV/µm; RBE peaks near 100 keV/µm; photons are indirectly ionizing; MV therapy is Compton-dominated — COVERED (m06 thorough; 255/511 keV present in 2 files).

m09 measurement / TG-51: Farmer at ≈ 300 V; GM not for dose or dose rate, long dead time; diodes energy/angle/temperature dependent; proportional counter separates alpha from beta; radiochromic read ≥ 24 h; H&D curve; LiF TLD; glow curve; neutron detectors (rem-ball, "snoopy," gold foils); well chamber for HDR; NaI for wipes; a-Si for EPID/OBI; TG-51 photons at 10 cm with %dd(10)x and Pb foil to remove electron contamination, kQ relates Co-60 calibration to the beam quality, raw reading × P_TP × P_ion × P_pol (× P_elec); electrons at dref with P_gr = 1 for parallel-plate; chamber recalibrated at an ADCL every 2 years — PARTIAL (TG-51 chain, kQ, Pb foil, dref, P_gr covered thinly in 1–3 files; glow curve, H&D, rem-ball, NaI, a-Si, 2-year ADCL MISSING).

m35 / m33 photon dosimetry: TMR₀ = zero-area primary; TMR(dmax) = 1; TMR depends on energy, field size, depth but not SSD; PDD depends on all four; orthovoltage surface ≈ 100%; 18 MV d10 ≈ 80%, 6 MV ≈ 67%; Mayneord accounts for PDD rising with SSD; TMR = PDD × ISL × Sp ratio; Sp from phantom (= Scp/Sc), Sc in air; WF depends on energy, field size, depth; OAR on energy, off-axis distance, depth; 80% normalization → 125% hot spot; wedge angle shrinks with depth; P/O 6 MV hot spots at dmax near the periphery, growing with separation; heterogeneity correction lowers dose just upstream of lung slightly and raises it downstream; 4 cm chest wall + 7 cm lung at 6 MV ≈ 15–18% overdose if uncorrected; < 4 cm fields lack lateral equilibrium; FFF PDD lower, profile peaked; BSF = Ddmax/Dair; TAR = Dd/Dair; SAR = Dscatter/Dair; TMR = Dd/Ddmax SAD; TPR = Dd/Dref; PDD = Dd/Ddmax SSD; Clarkson for irregular fields; dose kernels from Monte Carlo; TERMA; superposition better for divergence and heterogeneity; dose-rate change with SSD by inverse square (115 cGy/min at 100 → 95 at 110) — COVERED (all definitions and factor dependencies present).
- Handout item to watch: "P/O hot spots increase with energy" offered as part of an all-of-the-above; hot spots decrease with energy. Our bank has this right.

m05 / m34 electrons: 2 MeV/cm; 16 MeV at 4 cm ≈ 8 MeV; range 20 MeV ≈ 10 cm; d90 16 MeV ≈ 5 cm; d80 12 MeV ≈ 4.3 cm; mean energy 2.33 R50; bremsstrahlung ≈ 1% at 6 MeV; Pb ≈ E/2 mm; d90–d20 gradient widens with energy; virtual source from head/cone scatter; high-energy 90% line pinches in, low-energy bulges out; electron–photon abutment hot spot lands on the photon side (bulge); surface dose up with obliquity/energy/bolus; cone factor depends on energy and cone, cutout factor on energy, cone, cutout size/shape; energy choice for 3 cm depth + 1 cm bolus at 90% — COVERED (m05/m34 and m45 have all rules).

m10 / m11 imaging: narrower window → more contrast; HU from µ; pitch 1.3 lowers dose; CTDIvol/DLP/effective dose; dose-reduction methods; CT ≈ 0.6–0.7 lp/mm, ≈ 0.5 mm accuracy; thyroid ≈ 80 HU; 9 bits = 512 levels; iterative recon; ring artifact 3rd gen; typical effective doses head CT ≈ 2 mSv, chest ≈ 7, abdomen/pelvis ≈ 10, PET/CT ≈ 10–25, mammogram ≈ 0.4 mSv; MRI shim/steel/copper mesh/H/periphery distortion/0.3 lp/mm/T1-T2-FLAIR/Gd; fat-suppressed Gd T1 best for H&N fusion; Primovist (hepatobiliary Gd) on T1; PET 555 MBq, 110 min, electronic collimation, corrections, N-13 (not N-11), SUV, N/M staging, BGO/LSO/GSO, 10–100× SPECT, 511 keV; transmission (attenuation) image recognition; kV vs MV CT trade-offs; MV cone-beam images in the treatment beam; kVCT ≈ 0.5 mm — PARTIAL (HU, pitch, T1/T2, Gd, SUV, kV/MV covered; CTDI/DLP, exam effective doses, lp/mm values, shim/RF shield MISSING).

m26 / m27 informatics: TB = 10¹² bytes; 100-slice CT ≈ 50 MB (512² × 2 B); 100-slice MRI ≈ 12 MB; DR 2048²; DICOM, PACS, HTTP, HL7 (R&V to billing); HIPAA five rules (privacy, transaction/code set, security, identifiers, enforcement) and what HIPAA does not do; informatics definition; ML needs adequate, accurate data and defined metrics — COVERED except HIPAA (MISSING) and HTTP (irrelevant).

m19 / m25 prescribing and IMRT: ITV = CTV + internal margin; PTV adds set-up margin; ICRU 62 for notation, ICRU 83 for IMRT reporting; the four indices; DVH shows no spatial location; lung/parotid parallel, cord/brainstem/optic nerve serial; recognizing GK/IMRT/VMAT/proton/brachy DVH shapes; VMAT advantages; > 7–9 IMRT beams no gain; ≥ 10° beam separation; VMAT modulates gantry, dose rate, MLC; 6 vs 15 MV; IMRT factor 3–10, avg ≈ 4; arcs > 90°, coplanar or not; IMRT cost function Σ w(Dplan − Drx)²; segmentation = leaf-sequencing a fluence map; Tomotherapy disadvantage MVCT contrast — COVERED except IMRT factor (MISSING) and DVH-shape recognition items (PARTIAL; images).

m24 special procedures: TBI spoiler raises skin dose; Rx at umbilicus mid-depth; 6–18 MV photons; lung blocks; nausea/diarrhea/pneumonitis; TSET 6 MeV, dmax pulled toward the surface by scatter, midplane dose from bremsstrahlung, nail loss and erythema, Stanford 12-field with superior-field axes above the orbits? (handout treats as geometry recall); IORT with orthovoltage, electrons, or electronic brachy; lucite cones collimate and cut bremsstrahlung; beveled cone penumbra; electronic brachy advantages (no isotope, staff may stay, mobile); electron arc: deeper dmax, isocenter at a depth equal for all angles, Pb ≈ E/2 + 1 mm, arc extends beyond field edges; past pointing (3D arc therapy); proton RBE 1.1, highest at distal edge, varies with energy/depth; scanning produces fewest neutrons; proton safety = neutrons and activation gammas; heterogeneities matter more; no exit dose; surface dose slightly higher than 6 MV; penumbra slightly larger at depth; integral dose ranking (protons lowest; handout ranks VMAT highest — contestable); ocular protons ≈ 70 MeV; SOBP — COVERED for TBI/TSET/IORT/protons/SOBP/RBE (4–12 files); electron arc, past pointing, ocular proton energy MISSING.

m40 brachytherapy: Ra-226 abandoned for radon leakage; Cs-137 gyn strengths in mg Ra-eq; 0.3 mCi seeds; 10 Ci HDR; 1 mm; quarterly calibration; PBI 34 Gy/10 BID; I-131 150 mCi; Y-90 liver, P-32 polycythemia, Ra-223 bone; 1/d² valid beyond ≈ 2× source length; Point A where uterine artery crosses the ureter, Point B at pelvic sidewall/obturator nodes; ring unshielded; post-plan at ≈ 30 days; seed assay options; Cs-131 for prostate; SAVI has the most catheters; sarcoma interstitial, lung intraluminal; P-32 not a permanent implant source; Γ: Co-60 13.07, Ra-226 8.25, Ir-192 4.6–4.7, I-125 1.48 R·cm²/(mCi·h); 25 mCi Cs-137 ≈ 9.9 mg Ra-eq (3.26/8.25); active vs physical length (active shorter); mean life = 1.44 T½; "recordable event" 10% (obsolete) — COVERED except SAVI/Contura/MammoSite (MISSING), 2× source-length rule (MISSING), recordable-event threshold (MISSING and outdated), 30-day post-plan (PARTIAL).

m43 / m20 constraints and oncology (RTOG/QUANTEC numbers the tests use): testes ≤ 1–2 Gy (ambiguous); small bowel 45–50 Gy; whole liver ≈ 30 Gy mean; kidney V20 < 32% (bilateral), mean < 18–23 Gy; rectum V50 < 50%, V75 < 15%; bladder V80 < 15%; parotid mean ≤ 26 Gy bilateral, ≤ 20 Gy single; larynx Dmax 66 Gy (QUANTEC necrosis); optic nerve 54 Gy; brainstem 54 Gy (60 Gy to 0.03 cc); femoral head 50 Gy; heart V25 < 10%, V50 ≈ 33% (RTOG lung); SRS single fraction: cord 13–14 Gy, optic apparatus 8–10 Gy, brainstem 12.5–15 Gy, brain V12 < 5–10 cc; pacemaker < 2 Gy; ovary sterilization ≈ 5–10 Gy; rib fracture risk ≈ 50 Gy; α/β colon 10, prostate 1.5; four Rs; cell-cycle sensitivity (M/G2 most, late S least); stochastic (leukemia) vs deterministic; fetal limit 5 mSv (0.5 mSv/month), 1st trimester most sensitive; common prostate histology adenocarcinoma; most common childhood cancer ALL; Ewing mets to lung; breast mets bone/lung/liver/brain, first nodes axillary; stomach/pancreas/ovary mets liver-lung-peritoneum; anatomy levels: cord ends L1–L2, carina T4–T5, hyoid C3, suprasternal notch T2, pylorus L1, right renal hilum L1–L2, laryngopharynx C4–C6, brachial plexus C5–T1, rectum ≈ 12 cm beginning at S3/anal verge, 7 true rib pairs; Tc-99m 6 h (λ 0.115/h), I-131 8.06 d, Tl-201 for cardiac — COVERED for QUANTEC/TG-101/anatomy levels/α-β/four Rs (13, 10, 12+ files); MISSING: testes/ovary doses, Ewing, true ribs, Tis/TNM notation, exam-specific effective doses; PARTIAL: metastasis-site lists (1 file), cell-cycle ranking (2 files).

m42 QA / m41 protection / TG-100 (test versions): output constancy daily; TG-51 annual 1%; picket fence weekly; SRS lasers 1 mm; kV imaging dose annually; chamber calibration every 2 years; TG-40 gantry isocenter 2 mm and sim lasers 2 mm; TG-142 couch 2 mm/1° for IMRT, monthly MLC 1 mm (IMRT), field size 2 mm, gantry 1°, light-radiation 2 mm or 1% per side, imaging scaling ≤ 1–2 mm, imaging dose "within baseline"; TG-36 fetal dose, TG-53 TPS QA, TG-108 PET shielding, TG-132 registration, TG-203 CIEDs; IMRT factor meaning; P unrestricted 0.02 mSv/wk, restricted 0.1 mSv/wk; U = 1 for secondary; T nurse station 1, exam room 1/2, parking lot 1/40; W cGy/wk; TVL = 3.32 HVL; 15 MV concrete TVL ≈ 16 in, 6 MV lead TVL ≈ 2 in; neutrons above ≈ 10 MV, shield at ≥ 10–15 MV; BPE in doors; occupational 50 mSv/yr, extremities 500 mSv, public 1 mSv, organ 0.5 Sv, fetus 5 mSv; leak tests semi-annual; Transport Index mR/h at 1 m; 2 mR/h in any hour; wipe 0.005 µCi; contamination 2,200 dpm; RPN components, > 125 threshold, human error dominant, FTA as propagation diagram; random vs systematic error — COVERED except TG-108, TG-40 numbers, 2-year ADCL, Transport Index, 2,200 dpm, T for parking lot, TVL inch values (MISSING or PARTIAL).

### Recomputed answers — File 2 (sample of 48; wrong or unresolvable items listed first)

Wrong, no correct option, or internally inconsistent (7):
1. Test 1 Q62 (electron MU, 3 Gy to 95%, SSD 109, VSD 90, 9 MeV, CF 1.004, cutout 1.021): ISL = (92/101)² = 0.830; MU = 300/(1.004 × 1.021 × 0.95 × 0.830) = 371. Options 448/459/399/420 — none correct. The handout's own appendix says the key is wrong. (Test 2 Q76 reissues it with 371 as an option.)
2. Test 3 Q97 (exposure 3 m from 10 mg Ra-eq): 10 × 8.25 / 300² = 9.2×10⁻⁴ R/h ≈ 0.92 mR/h. Options 3.06/9.17/27.5/30.6 R/h are all 10⁴ too large (9.17 R/h would be at 3 cm). Unit error in the options.
3. Test 1 Q135 as printed: the stem's inline arithmetic "200/(1 × 1 × 0.085 × 0.67) = 149 MU" is a transcription error; the correct 200/(0.67 × 0.85) = 351 MU is option a. The appendix acknowledges this.
4. Calcs #32 (file size): stem says 1,000 images at 210 × 210, 10-bit; the worked answer uses 1,024 × 1,024 (1.05×10¹⁰ bits). With 210² the answer is 4.4×10⁸ bits. Inconsistent stem/answer.
5. Calcs #54: "R50" defined as the depth of 50% dose, inside a block of SBRT plan-review definitions. That is the electron R50; the SBRT R50 is the 50% isodose volume / PTV volume (stated correctly elsewhere in the same file).
6. Test 4 Q42: asks for the "linear attenuation coefficient" and the intended answer is ln2/T½ — that is the decay constant. Q51 calls 1.44 × T½ the "average half life" — that is the mean life.
7. Quiz 104 (File 1) steel density: no correct option (see above).

Nearest-option only (exact value falls between options) (3):
8. Test 1 Q43 / Test 2 Q64 Mayneord, 6X, d 11, SSD 102 → 137: [(138.5/103.5) × (113/148)]² = 1.044. Nearest option 1.0468 (0.3% off); the others are far.
9. Test 3 Q70 Mayneord, 10X, d 12, 100 → 140: with dmax 2.5 cm, 1.049; with dmax 2.0, 1.0525. Nearest option 1.0531.
10. Test 3 Q17 (when 10 mCi I-125 equals 25 mCi Pd-103): ln 2.5 / [0.693(1/17 − 1/59.4)] = 31.5 d. Nearest option 34 d (8% off).

Ambiguous by construction (4):
11. Test 2 Q5/Q66 gap, 20×20 at SSD 100 and "collimator 10×10" at SSD 120, depth 5: if the 10×10 is the collimator setting, the surface field is 12 cm and gap = 10 × 5/100 + 6 × 5/120 = 0.75 (option b). If 10 cm is the skin field, gap = 0.5 + 0.208 = 0.71 (option c). Both are options; the stem wording points to 0.75.
12. Test 1 Q126 / Test 2 Q84 (electron energy for 3 cm depth + 1 cm bolus at 90%): 4 cm × 3.2 = 12.8 MeV. A 12 MeV beam has d90 ≈ 3.75 cm, which does not reach 4 cm; strictly 15 MeV is needed. The intended rule-of-thumb answer is 12 MeV.
13. Test 1 Q108 / Test 2 Q141 (IMRT cost function): options Σw(Drx − Dplan)² and Σw(Dplan − Drx)² are mathematically identical, so two options are correct.
14. Test 1 Q144 / Test 2 Q82 muscle density: options 1.04 and 1.06 are both within quoted ranges (ICRU 1.05).
15. Test 1 Q12: "average energy of a 9 MeV beam" — the ⅓ rule applies to photon spectra, not electron beams; Test 2 Q100 fixes the stem to "9 MV x-ray" (3 MeV).
16. Test 2 Q44/Q129 ocular protons: standard is ≈ 60–70 MeV; options 30/100/150/250 contain no standard value (100 MeV is the intended choice).

Verified correct (34): decay 100 → 84.1 mCi over 6 mo with T½ 2 y; A₀ = 10.88 Ci for Ir-192 9 d earlier; T½ = 5.8 h from 3 → 2.1 mCi in 3 h; Cs-137 to 25% = 60 y; 3 HVL → 12.5 mR/h; 2 HVL back-calculation → 40 mR/h; HVL 2.27 cm from 500 → 200 in 3 cm; TVL = 3.32 × 3.2 in = 10.6 in; line vs point source 8 and 3.2 mR/h; 3 TVL + 1 HVL = 5×10⁻⁴; 0.5 TVL + 2 HVL = 0.079; 1 TVL + 1 HVL attenuates 95%; OAR 0.822/0.811 = 1.014; SMR 0.932 − 0.881 = 0.051; gap 1.625 cm for 30 and 35 cm fields at 5 cm depth; CSI twist tan⁻¹(20/100) = 11.3°; HDR time 210 s → ≈ 220 s after 5 d; 25 mg Ra-eq at 5 m = 0.000825 R/h; T_eff = 48 × 2/50 = 1.92 h; electron MU 300/(1.022 × 0.683 × 0.85) = 506; d90 → 9.6 MeV, d80 → 14 MeV, R50 = 12/2.4 = 5 cm; W_p = 40,000 cGy/wk, W_L = 100,000 cGy/wk; B = 3.7×10⁻⁵ (P 0.1 mSv/wk, d 6.5 m, W 500,000 mSv/wk, U 0.23); H = 610 mrem; BED₃ (50 × 1.1) = 75.2; BED₁.₅ 252 vs 182; RPN 54; CTP (65 °F, 741 mmHg) = 1.013; effective depth 8.0 cm; 6 cm lung-equivalent shortfall ≈ 18%; 4A/P of 7 × 37 = 11.8; 0.89 × 8 = 7.1; 2014 commentary: µ 0.94 → HVL 0.737, 2 HVL 1.47 cm; 90 × 82.1/64.1 = 115 cGy; √(1² + 6²) = 6.1 cm; e^(−0.05 × 11) = 0.577; Test 1: 16 MeV − 2 × 4 = 8 MeV; 555 MBq = 15 mCi; binary 110111 = 55; 15/2.4 = 6.25; 1/0.55 − 1 = 82%; 5 HVL → 96.9%; 20/3.2 = 6.25; CTP (24.6 °C, 739.25) = 1.037; gap 0.827 + 1.348 = 2.17; 9/2.8 = 3.2; norm 300/(352 × 1.03 × 1.024 × 0.952) = 85%; 100 × (2/5)² × 0.5 h = 8 mR; λ(Tc) = 0.115/h; 9.5 MeV = 9.5×10⁶ eV; Test 2: 4A/P 15 × 25 = 18.75; CTP (24 °C, 737) = 1.038; 19/(0.863 × 0.985 × 0.988 × 1.09) = 21 MU; 0.693/11 = 0.063/mm; 100e^(−0.115 × 24) = 6.33 mCi; 115 × (100/110)² = 95; 800/4.3² = 43.3; 200/(1.004 × 1.021 × 0.90 × 0.830) = 261; 11101 = 29; 1/0.65 − 1 = 54%; 0.693/12 = 0.058; 0.375 + 0.45 = 0.825; 12/2.8 = 4.3; 10000101 = 133; PA T-spine 187.5/(0.788 × 1.006 × 1.004 × 0.776 × 1.154) = 263; Test 3: 25 × 3.26/8.25 = 9.88; 30/40 fields at 8 cm → 2.8; 4 HVL → 93.75%; BED₁₀ match 5 × 10 Gy in 4 fx → 11.6 Gy/fx; 18 − 8 = 10 MeV; 100/0.67 = 149; 300/(1.03 × 1.024 × 0.9 × 0.943) = 335; Test 4: 0.693/2.7 = 0.257/d.

Wrong-key count: 7 items with no correct option or an internally wrong worked answer; 3 nearest-option-only; 6 ambiguous by construction. The quizzes file has 1 (steel density). Keys themselves are not visible in the text, so the count reflects recomputation against the options rather than against a stated letter.

### Outdated or exam-irrelevant content — File 2
- "Recordable event = 10%" (Tests 1 and 4): pre-2002 10 CFR 35 term. Current medical-event thresholds are 20% of total dose, 50% of a fractional dose, or 0.5 Sv to an organ; "recordable event" no longer exists.
- Quality factor 10 for protons: regulatory (10 CFR 20); ICRP 103 wR = 2.
- Film-based QA (XV/EDR2, head-leakage film wrap), image intensifiers, Van de Graaff/betatron comparisons: historical.
- "Past pointing" in 3D arc therapy: rarely examined.
- Electron arc therapy items (dmax shift, E/2 + 1 mm lead, isocenter depth): legacy technique, low yield.
- HTTP, informatics definition, machine-learning data-quality item: filler.
- Fundamental-constant items (farad, henry, Planck units, electron mass): not on the MDCB content outline.
- Elementary-particle items: not exam content.
- NCRP 151 TVL inch values and door thickness ladders: dosimetrists are asked concepts (P, U, T, W, TVL count), not inch tables.

---

## Overlap between the two files and with MDCB domains

Internal overlap: the quizzes and the practice tests were written by the same instructor and share about 150 facts verbatim (TG-142 numbers, TG-100 RPN, shielding P/U/T/W, detectors by task, HDR QA, Point A/B, SBRT R50/D2cm/V20, PET/MRI/CT trivia, 4A/P, Mayneord, electron rules, BED). Tests 1 and 2 share ≈ 40% of stems; Tests 3 and 4 recycle another ≈ 40 from Tests 1–2 plus ≈ 35 image-ID items.

Domain weighting (both files combined, ≈ 1,370 unique items):
- Physics / machines / interactions / units: ≈ 30% — heaviest. Linac anatomy depth exceeds MDCB needs.
- QA / safety / TG documents: ≈ 15% — TG-142, TG-100, TG-51, TG-203 well drilled.
- Protection / shielding / regulations: ≈ 12% — good coverage of P/U/T/W, 10 CFR parts, NCRP references.
- Calculations: ≈ 10% (63 inventory + ≈ 45 test calcs) — MU, gap, Mayneord, BED, decay, attenuation, electron rules, shielding B, exposure from Γ.
- Brachytherapy: ≈ 10% — strongest on HDR process, PBI devices, LDR prostate workflow, applicator ID.
- Imaging (CT/MR/PET/US): ≈ 10% — more detail than MDCB asks (lp/mm, crystals, CTDI chain).
- Plan evaluation / IMRT / SBRT / SRS: ≈ 8% — indices and protocol numbers.
- Anatomy / oncology / constraints: ≈ 5% — mostly in the practice tests (vertebral levels, metastasis patterns, QUANTEC/RTOG numbers, image ID).
Compared to the MDCB outline the packet under-weights treatment planning technique (beam arrangement, wedges, field matching rationale, immobilization, simulation, IGRT decision-making) and clinical oncology, and over-weights machine hardware, imaging physics, and regulatory trivia.

---

## Summary

- Total items: File 1 ≈ 515 unique quiz items (≈ 577 printed) across 45 quizzes plus ≈ 25 reference pages; File 2 ≈ 856 unique items (63 worked calcs, 293 topic-bank MCQ, four tests of 150/150/100/100) plus 63 method notes and 11 commentary notes. Combined ≈ 1,370 unique items; every answer key in the text is a verbatim copy with the marked letter lost, so only the worked calcs, the Test 1 appendix, and the Test 4 matching blanks carry visible answers.
- Coverage by our bank (counted over the ≈ 190 distinct facts/calc types in the inventory above): ≈ 58% COVERED, ≈ 24% PARTIAL, ≈ 18% MISSING. Weighted by item count (because the tests repeat the covered facts many times) roughly 70% of the items would be answerable from our bank today.
- Wrong keys: File 2 has 7 items with no correct option or an internally wrong worked answer, 3 where only a nearest option exists, and 6 ambiguous-by-construction items; File 1 has 1 (steel density). 48 numeric answers were recomputed in File 2 and 5 in File 1.

MISSING facts and calc types worth adding as original items, by module:
- m03 radioactivity: 555 MBq ↔ 15 mCi conversion drill; activity order-of-magnitude ladder (GK 6,600 Ci, HDR 10 Ci, I-131 150 mCi, FDG 15 mCi, seed 0.3 mCi, check source 10 µCi, wipe limit 0.005 µCi); time for two activities to become equal.
- m04/m07 machines: SF6 in the RF guide; 3 GHz / 10 cm; traveling vs standing wave guides; PFN + thyratron modulator; triode gun; steering coils; jaw transmission ≈ 0.5%; a-Si flat panel; photon-mode vs electron-mode beam current; flattening filter designed for 10 cm; FFF dose rate ≈ 2,400 MU/min and FFF d10 ≈ 61–63%.
- m09 measurement: rem-ball / proportional counter for neutrons and alpha-beta discrimination; NaI well counter for wipes (why not an ion chamber); TLD glow curve and film H&D curve; radiochromic 24 h read; chamber recalibration every 2 years; IROC phantom TLD/OSL.
- m10/m11 imaging: CTDI → CTDIw (⅓ center + ⅔ periphery) → DLP = CTDIvol × L → E = k × DLP chain, with units (mGy, mGy·cm, mSv); typical exam effective doses (head CT 2, chest 7, abdomen-pelvis 10, PET/CT 10–25, mammogram 0.4 mSv); iterative reconstruction (less noise, 25–40% less dose); ring artifact = 3rd-generation detector fault; CT ≈ 0.7 lp/mm vs MRI ≈ 0.3 lp/mm; AEC/mA modulation; thyroid ≈ 80 HU; PET crystals (BGO/LSO/GSO), SUV > 2.5, uptake protocol; MRI shim coils, steel magnet shield vs copper RF shield, quench, 0.5–3 T.
- m12 units: dps → dpm; f-factor 0.876 vs "1 R ≈ 1 rad"; SI base definitions table (optional).
- m19 plan evaluation: conformation number and inhomogeneity index alongside CI/HI; hot-spot ladder by technique (3D 105–107%, IMRT ≈ 110%, SBRT 120–130%, GK 200%, brachy 300–400%); acceptable target DVH triplet (95% at 100%, 99% at 95%, < 10% at 107%).
- m20 oncology: generic TNM primer (TX/T0/Tis, NX/N0–3, M0/M1, c/p/y/r prefixes, stage grouping, FIGO, grade); neoadjuvant definition; common metastasis-site lists (breast, stomach, pancreas, ovary, Ewing); vertebral-level anatomy set (hyoid C3, notch T2, carina T4–5, pylorus L1, renal hilum L1–2, cord end L1–2, laryngopharynx C4–6); 7 true rib pairs.
- m25 IMRT/VMAT: IMRT factor (3–10, avg 4) and why it enters W_leakage only; avoidance sectors; collimator offset between arcs to smear interleaf leakage; compensator IMRT trade-offs.
- m33/m37 algorithms: TERMA by name; "spatially invariant" wording for convolution; CCC cost M×N vs N³; AAA vs Acuros (deterministic) distinction as a trap item.
- m36 special calcs: SMR = TMR − TMR₀; line-source 1/d vs point-source 1/d² and the 2× source-length rule; "3%/cm of radiological-depth difference" lung rule with a worked hetero-vs-homo item; effective depth with the density table (lung 0.25–0.33, fat 0.95, muscle 1.05, soft bone 1.1, cortical bone 1.65–1.85); CTP with °F input; along-and-away tabular LDR calc; 45°-collimator diagonal distance calc.
- m40 brachytherapy: balloon/strut APBI (MammoSite, Contura, SAVI; 1 cm PTV_eval shell; 34 Gy/10 BID; 200% at balloon surface; multi-lumen skin sparing); Syed template; Freiburg flap and Leipzig surface applicators; ring vs ovoid shielding; HDR planning methods incl. graphical optimization; dwell-linearity QA, annual emergency drills, two-level security; LDR prostate workflow (10% assay, 10% overage, 5 mm TRUS slices, prostate + 5 mm/0 mm posterior PTV, peripheral loading, urethra < 150%, V100/V150/V200/D90, 30-day post-plan, Mick vs strands); endobronchial Rx at 1 cm; HDR prostate central < 120%; current medical-event thresholds as the replacement for "recordable event."
- m41 protection/regulations: 10 CFR Part 19 (worker rights) and Part 71 (transport; Transport Index mR/h at 1 m; White I / Yellow II / Yellow III); 2,200 dpm/100 cm² package contamination; decay-in-storage 10 half-lives; quarterly source inventory; NCRP 147 vs 151; BPE on the linac side of the door with Pb outside (2.2 MeV capture gamma); W_primary vs W_leakage with IMRT factor; occupancy factors for exam room (½) and parking lot (1/40); out-of-field dose ladder (≈ 5% at 2 cm, 1% at 10 cm, 0.2% at 30 cm, 0.1% at 1 m).
- m42 QA: star shot (collimator) vs spoke shot (gantry) vs Winston-Lutz; TG-40 legacy numbers still asked (gantry isocenter 2 mm, sim lasers 2 mm); TG-108 PET shielding, TG-53 TPS QA; fault-tree analysis and TG-100 failure-cause percentages; HIPAA five rules.
- m43 constraints: testes and ovary dose thresholds; rib-fracture threshold; whole-liver 30 Gy mean; heart V50 ≈ 33% (RTOG lung).
- m44/m45: a 6X "surface-dose vs energy" ladder item and a photon-vs-electron abutment hot-spot item (bulge toward photon side).

Verdict: complementary, and on balance weaker than our bank. The packet's strengths are its calculation inventory (63 types, every one of which our bank already drills, often with more care about units and geometry), its HDR/APBI/LDR-prostate workflow detail, and its regulatory and imaging-physics trivia, which fill real gaps listed above. Its weaknesses are a 7-item wrong-key rate plus several sloppy stems, heavy repetition (Tests 1–4 reuse ≈ 40% of stems), no visible answer letters in the extracted text, several outdated items (recordable event, mR/h release, Q = 10 for protons presented as physics), and an over-weighting of hardware and imaging trivia relative to the MDCB outline's planning and clinical content. Use it as a checklist for the MISSING list above, not as a question source.
