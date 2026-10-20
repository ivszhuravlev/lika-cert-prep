# RM Review — "All Short Tests" (third-party PDF) vs our bank

Source: `inbox/text/All Short Tests.pdf.txt` (23,179 lines, ~518 KB, gitignored, copyrighted). Read in full, 2026-10-20.
Everything below is paraphrased; no stems or answer text are reproduced. Coverage was checked by `rg` over `knowledge/theory` + `knowledge/questions` (45 modules, 1,944 items at the time of review).

Important extraction caveat: the answer keys in this PDF were highlighted, not typed. Highlighting did not survive text extraction, so most "Key" copies are byte-identical to the question copies. A typed answer is visible only for the worked-calc sets (opening 63 items, ST 11, 15–17, 206, 222–224, 503, 505, 600), the matching tests (ST 33), and a few commented items. For every other item the correct answer was inferred from physics while reading — treat "wrong key" counts below as a lower bound on the typed keys only.

---

## 1. Structure map and item counts

Roughly half of the file is duplication: the "Board Questions" block appears four times (headers "Board Questions", "Questions for the ARRO Bowl", and two untitled repeats — verified identical by diffing normalized copies; only one typo differs), and every short test appears 2–3 times (question copy + "Key" copy that lacks keys). Unique items are counted once.

| # | Section (lines) | Topic | Unique items | Notes |
|---|---|---|---|---|
| 0 | Untitled worked-calc set (1–717) | Mixed physics/planning calcs with typed answers | 63 | Best part of the file; decay, HVL/TVL, ISL, MU, gap, CSI angle, shielding, BED, stats |
| 1 | Board Questions by module (718–2018; repeats at 2025, 4125, 5427) | Atomic structure → safety, 17 sub-modules | 214 | MCQ, no visible key. Sub-counts: atomic 8, kV x-rays 10, MV x-rays 17, interactions 11, units 10, measurement 18, photon dosimetry 21, electrons 15, CT 10, MRI 10, PET 10, sim/verification 10, IMRT/VMAT 10, brachy 17, protons 10, protection 17, safety 10 |
| 2 | Mineral 1/3/6/8/10 short tests + notes (3335–4121) | Electron ranges; energy choice; α/β; activity magnitudes; equipment/detectors | 41 | Notes pages are fact lists (useful) |
| 3 | Short Tests #1–#17, 30–33 (6724–12760) | General board-style mixes; 11/15/16/17 are calc sets; 33 is matching (regs, shielding, detectors, networking) | 382 | #9 = 23, #10 = 18, 12–14 = 15/16/14, 15–17 = 12 each, rest 20 |
| 4 | Short Tests 101–107 (12761–14330) | Mixed physics + planning | 131 | |
| 5 | Short Tests 201–211 (14331–16930) | Mixed; 206 is a 20-item calc set | 200 | no 209 |
| 6 | ST 221 (reference list), 222, 223, 224 (16781–17207) | 221 = magnitudes cheat-sheet (no items); 222 statistics; 223/224 matching | 38 | |
| 7 | ST 300, 301, 302 (17208–17492) | Surveys; brachy source/device verification; "mag and min" | 30 | |
| 8 | ST 501–508, 511, 519–524, 600 (17493–19780) | Mixed; 503/505/600 are calc sets; 508 imaging; 511 instrumentation; 519 LDR; 520 isodoses; 521 thresholds; 522 QA; 523/524 misc | 210 | |
| 9 | Modules 1&2, 23&24, 25&26, 29&30, 35&36 (19781–20279) | Program-level questions (intro/anatomy/planning/informatics) | 47 | |
| 10 | Vitamin short tests 1–7, 15, 19, 20, 27, 35 + "Board Review" notes (20280–23179) | CT, MRI, PET, shielding, plan review, HDR, detectors, IMRT/VMAT, HDR planning, LDR prostate, brachy sources, ultrasound | 138 | Notes pages are the most content-dense part of the file |

Unique items ≈ **1,494** (≈3,000 printed including duplicates). Of these, ≈ 300 are numeric/calc items, ≈ 120 are matching/true-false, the rest are concept MCQ.

---

## 2. Fact & calc-type inventory with bank coverage

Legend: **C** = covered (theory + ≥1 question), **P** = partial (mentioned in theory only, or one incidental question, or a different variant), **M** = missing from `knowledge/`. Module code = where it would belong in our bank.

### 2.1 Calculation types

| Calc type (as taught by the file) | Module | Cov |
|---|---|---|
| Exponential decay, A = A₀·e^(−0.693·t/T½), forward and solve-for-time; identify isotope from decay over time | m03 | C |
| Effective half-life Teff = Tp·Tb/(Tp+Tb) | m03 | C |
| Mean life 1.44·T½; LDR total dose = 1.44·T½·initial dose rate for permanent implants | m40 | C |
| HDR time scaling: equal dose ⇒ A₁·t₁ = A₂·t₂ after source decay | m40 | P (one question) |
| HVL/TVL attenuation, TVL = 3.32 HVL, combine shielding with inverse square | m06/m41 | C |
| Inverse square: solve for distance at which rate drops to a limit; convert cGy/min at 1 m → mR/hr at distance | m33/m41 | C (distance), P (min→hr unit chain is a frequent trap; one item) |
| Line source: 1/d (not 1/d²) when closer than ~2× active length | m40 | P |
| Point of equal dose rate between two unequal sources | m33 | P |
| Ra-equivalent exposure: 8.25 R·cm²/(mg·h); 10 mg-Ra-eq ≈ 25 mCi Cs-137 | m40 | P (3 hits, no question) |
| Mayneord F for extended SSD, then MU at extended SSD | m35 | C |
| SSD MU with PDD·Sc·Sp·WF·TF·OAR; SAD MU with TMR; reverse (dose from MU) | m35 | C |
| Calibration-geometry correction: SAD-cal machine used at SSD (÷0.971 for 6X dmax 1.5) and SSD-cal used at SAD (÷1.03); 18X dmax 3.3 → 1.067 | m35 | C for 6X; **M for 18X/1.067 variant** |
| Primary-only TMR = TMR − SMR (block-shadow calcs) | m36 | **M** |
| Clarkson sector sum with TAR₀ | m33 | C |
| Equivalent square 4A/P; circle ≈ 0.89·diameter | m33 | C / P (0.89 appears only in two question "Why"s) |
| Missing-wedge or wedge-omitted-for-n-fractions total-dose error | m34 | P |
| Normalization arithmetic (hot spot = 100/normalization %) | m19 | C |
| Effective depth with lung 0.25, soft bone 1.1, hard bone 1.65 | m37 | C for lung; **M for the 1.1 soft-bone value and 3-layer composite** |
| Hetero vs homo rule ≈ 3 %/cm of lung traversed | m37 | **M** |
| Gap calc S = d·(L₁/2SSD₁ + L₂/2SSD₂) | m36 | C |
| CSI collimator angle = atan((L/2)/SSD) for brain fields; couch kick = atan((L/2)/SAD) | m36 | **M (no atan item; bank has couch/collimator logic in prose only)** |
| Parallel-opposed dose at dmax = entrance + exit with ISL | m36 | C |
| Electron MU with cone/cutout factor and virtual-SSD gap ISL | m35/m36 | P (one question, no VSD theory) |
| Electron energy selection: R ≈ E/2, d90 ≈ E/3.2, d80 ≈ E/2.8, therapeutic ≈ E/4, ~2 MeV/cm loss, Pb ≈ E/2 mm | m05/m25 | C |
| Mean electron energy 2.33–2.4·R50 | m09 | C |
| Photon/electron mixed-beam MU weighting by dose fraction | m36 | P |
| Field size projected to another distance (PA jaw to match AP at SAD) | m08 | C |
| BED = n·d·(1+d/(α/β)); iso-effect matching by solving the quadratic for d | m21 | C / C (7 isoeffect items) |
| Shielding: W, U, T; B = P·d²/(W·U·T); leakage B_L = 1000·P·d²/(W·T); IMRT factor in leakage workload | m41 | C / **M for IMRT factor** |
| Dose equivalent with radiation weighting (α 20, n 5–20, photons 1) | m12 | C |
| Ctp = (273.2+T)/295.2 × 760/P (also kPa 101.33; °F→°C) | m09 | C (kPa variant P) |
| CTDIw = ⅓ center + ⅔ periphery; CTDIvol = CTDIw/pitch; DLP; E = k·DLP | m10 | **M** |
| Image file size = rows × cols × bits × slices (bits→bytes→MB) | m26/m27 | **M** |
| Statistics: mean/median/mode; SD intervals 68/95/99.7 %; add uncertainties in quadrature; detector efficiency cpm/dpm | m39 | **M (quadrature, SD)**, P (efficiency, 1 hit) |
| TG-100 RPN = O × S × D; scale 1–1000; >125 flagged | m42 | P (RPN concept present; 125 threshold/range absent) |
| Conformity index, conformation number (van't Riet), HI = (D1−D99)/Rx, R50, D2cm | m19 | C (CI/HI/R50/D2cm), **M (CN)** |
| Magnification SID/SOD; true size from film size | m08 | C |

### 2.2 Fact domains (grouped; representative facts)

**Atomic / interactions / production (m02–m06)** — isotopes/isobars/isotones/isomers; 1 amu; nucleus vs atom size; quarks/leptons; x-ray production efficiency ~1 % kV / tens of % MV; heel effect; average energy ≈ ⅓ kVp; PE ∝ Z³/E³, Compton Z-independent, PP ∝ Z², thresholds 1.022/2.044 MeV; neutron threshold ~10 MV; electron rest mass 511 keV. **C** except quarks/leptons (**M**, irrelevant) and the "characteristic vs brems %" question (**M**, low value).

**Linac engineering (m07)** — klystron vs magnetron, isolator/circulator, SF6 in the guide, traveling vs standing wave, achromatic 270° bend, primary collimator ≈ several TVL, flattening filter designed for a depth of ~10 cm, gun current vs energy vs dose rate, PRF, FFF properties (higher dose rate, lower d10 ≈ 61 % at 6 MV, less head scatter, forward-peaked profile), electron mode uses far lower beam current. **C** for klystron/magnetron/bend/waves; **P** for FFF (theory only) and isolator; **M** for SF6, PRF/gun-current reasoning, primary-collimator thickness, electron-vs-photon beam current.

**Measurement & detectors (m09)** — detector-to-task matching (Farmer for photon cal, parallel-plate for low-energy electrons, micro-chamber/diode/film for small fields, diode arrays for IMRT QA, GM for finding contamination/lost seeds, NaI well counter for swipes, thyroid probe, rem-ball/Bonner for neutrons, dose calibrator for NM activity, re-entrant well chamber for HDR source strength, TLD/OSL for personnel, Gafchromic read ≥24 h); Farmer ~300 V bias; GM dead-time/paralysis; diode temperature/angle/energy dependence; proportional counter α/β discrimination; H&D curve; glow curve; TG-51 chain (kQ, Pion, Ppol, Pgr, dref = 0.6R50−0.1, Pb foil); ADCL every 2 y; survey meter annual cal. **C**: TG-51 chain, TLD/OSL, diode, GM presence, parallel-plate, micro-chambers. **P**: re-entrant well chamber, NaI swipes, neutron detectors, area monitor. **M**: proportional counter, dose calibrator, H&D curve, glow curve, 300 V, "detector matching" as an item type, ADCL 2-year cycle, annual survey-meter cal.

**Photon dosimetry (m09/m35)** — PDD/TMR/TPR/TAR dependencies; TMR(dmax)=1; TMR > PDD at same depth; TMR from PDD via ISL and Sp; Sc from collimator setting, Sp from effective field; WF increases with depth; wedge angle decreases with depth; OAR dependencies; normalization and hot-spot reasoning; POP hot spot grows with separation and falls with energy; dose beyond lung higher when corrected; lateral electronic disequilibrium below ~3–4 cm; square > rectangle output at equal area. **C** nearly all; **P**: "WF grows with depth" (no explicit item), square-vs-rectangle output.

**Electrons (m05/m25)** — rules of thumb above; surface dose rises with energy (≈75 % at 6 MeV → >90 % at 20 MeV); brems tail 1–5 %; isodose bulge (low E) vs constriction (high E); cutout edge hot spots; CET for lung/bone; virtual SSD depends on energy and cone; bolus to shift d90; chest-wall 6–9 MeV. **C** except VSD theory (**P**) and 6 MeV d80 ≈ 2.1 cm worked example (**M**, trivial).

**Imaging — CT (m10/m11)** — HU from μ; window/level and perceived contrast; eye sees ~30–50 grey levels; bit depth → grey levels; pitch definition and dose; helical vs axial; iterative reconstruction 25–40 % dose savings; CTDI/DLP/effective dose; ~0.5–1 mm spatial accuracy, ~0.7 lp/mm; third-generation ring artifacts; bowtie filter; max 140 kVp; iodine contrast; 4DCT data volume; CT-sim room ≈ 1/16" Pb. **C**: HU, window, pitch, 4D, contrast, electron-density curve, artifacts. **P**: grey levels, Pb for CT room. **M**: CTDI/DLP/k-factor, lp/mm figure, iterative-recon savings, ring artifact origin, CT QA phantom metrics, xenon vs solid-state detectors.

**Imaging — MRI (m10)** — hydrogen signal, T1/T2/FLAIR appearance, gadolinium shortens T1, best soft-tissue contrast, distortion at FOV periphery, any-plane acquisition, shim coils, RF (copper) and magnetic (steel) shielding, typical 256 matrix, ~0.3 lp/mm. **C**: T1/T2/FLAIR/Gd/distortion. **M**: shim coils, Faraday/steel shielding, Tesla strengths, matrix/resolution figures.

**Imaging — PET (m10)** — FDG ≈ 10–15 mCi (370–555 MBq), F-18 110 min, 60-min uptake, 511 keV coincidence (electronic collimation), BGO/LSO/GSO crystals, ~4–5 mm resolution, SUV > 2.5 suspicious, positron range, corrections (attenuation, scatter, randoms, dead time), role in N/M staging, cyclotron production, other PET nuclides C-11/N-13/O-15, TG-108 shielding. **C**: 511/coincidence, SUV, F-18, cyclotron, resolution. **P**: FDG activity, uptake time. **M**: other PET nuclides, crystal types, TG-108, PET staging value.

**Imaging — ultrasound (m10)** — 1–20 MHz, speed depends on compressibility and density (~1,500 m/s water), piezoelectric transducer is both emitter and receiver, Fresnel/Fraunhofer zones, dB = 10·log ratio, bioeffects (heating, cavitation), artifacts, uses (PBI/MammoSite check, prostate IGRT, seed volume study), TG-128 QA. **M** almost entirely (only 2 piezo/MHz hits).

**Simulation / IGRT / registration (m14–m18, m32)** — orthogonal pair gives 3 translations; EPID (a-Si) has best isocenter congruence; kV vs MV contrast; CBCT dose; EPID magnification; rigid vs affine vs deformable; 3-point minimum for rigid registration; TG-132. **C** mostly; **P** a-Si/EPID facts; **M** affine definition.

**Planning / IMRT / VMAT (m19, m23, m25)** — ICRU 62 volumes (the file repeatedly writes "ICRP 62"), ITV = CTV + IM, PRV overlap allowed, −5/+7 % historic criterion, serial vs parallel metrics, DVH has no spatial information, dDVH axes, 7–9 beam plateau, ≥15–30° beam separation, avoidance sectors, collimator 15–45° and mirrored, min 3 MU/segment, VMAT modulates gantry speed/dose rate/MLC, 6 MV preferred for IMRT (no neutrons), IMRT factor 2–10 (avg ~4), VMAT typically fewer MU, integral-dose and conformity rankings, hot-spot location inside PTV, brachy and GK heterogeneity (200–300 %), SBRT 60–90 % prescription isodose, SRS size limits and non-coplanar arcs avoiding orbits, FFF for SRS/SBRT. **C** most; **P** beam separation, VMAT vs IMRT; **M** IMRT factor, avoidance sectors, min MU/segment, mirrored collimator, CN, SRS "avoid orbits/more arcs" reasoning.

**Special procedures (m24)** — TBI: 6 MV (or Co-60 historically), Rx at midplane/umbilicus, ~1,200 cGy in 6 fx, 5–10 cGy/min, lung blocks sized for divergence, beam spoiler, in-vivo dosimetry, toxicities (nausea, pneumonitis, cataract, parotitis). TSET: 6 MeV degraded to ~3–4 MeV at the patient, Stanford six dual-fields with CAX above/below, dmax < 1.3 cm, brems midplane dose ~1 %, eye/nail shields, toxicities (erythema, nail loss, counts). IORT: electrons/orthovoltage/eBT; lucite cones; bevelled cones shift penumbra; eBT needs no isotope. Electron arc: velocity effect pushes dmax deeper, Pb ≈ E/2 + 1 mm, arc extended 10–15° past borders, 4–8 cm field width, isocenter at equal depth. **C** basic TBI/TSET/IORT existence (4–14 hits). **M** essentially all the specific numbers above (TBI energy/dose rate/toxicities, TSET degraded energy/brems/shields, IORT cones/bevel/eBT advantages, every electron-arc fact).

**Brachy — general & HDR (m40)** — source table (Ir-192 380 keV/74 d; Cs-137 662 keV/30 y; I-125 28 keV/60 d; Pd-103 21 keV/17 d; Cs-131 30 keV/9.7 d; Co-60 1.25 MeV/5.26 y; Ru-106 β/1 y; Ra-226 α/1,600 y, abandoned for radon leakage); HDR source ≈ 10 Ci, ~4 × 0.8 mm, exchanged quarterly, 1 mm positioning tolerance, TG-43 (Λ, g(r), F(r,θ), G), air-kerma strength unit U; dwell-time patterns (ends longer); vaginal cylinder tip anisotropy and Rx at surface/5 mm; T&O Point A (2 up, 2 over), Point B, pear shape, tip dwell reductions for bladder/bowel; bronchial applicator Rx at 1 cm; PBI balloon: PTV_eval 1 cm rind minus skin/chest wall, 34 Gy/10 fx BID, ≈200 % at balloon surface, multi-lumen for skin sparing; HDR QA (dummy/check cable, autoradiograph, applicator integrity, area monitor, survey before/after, physician + QMP present, two independent barriers, emergency retract/crank); therapy isotopes (Sr-90 pterygium, Y-90 liver, Ra-223 bone, Sr-89/Sm-153 bone, I-131 100–200 mCi thyroid ablation, P-32 polycythemia/craniopharyngioma); Syed/template, interstitial sarcoma/breast. **C**: source table, TG-43, Point A/B, cylinder, T&O, QA procedures, Y-90, Ru-106, Ra-223, P-32, Au-198. **P**: HDR exchange/10 Ci (8 hits), 1 mm tolerance, dwell patterns. **M**: Sr-90 pterygium, Sr-89/Sm-153, I-131 therapy activities, PBI balloon numbers (rind, 34 Gy BID, 200 % surface, multi-lumen), HDR source dimensions, T&O tip-dwell reduction rationale.

**Brachy — LDR prostate workflow (m40)** — I-125/Pd-103/Cs-131 (Cs-131 shortest half-life = highest dose rate); ~0.3 mCi/seed; 60–120 seeds (depends on volume, activity, isotope); order ~10 % extra; assay a 10 % sample (third-party vendor assay acceptable); TRUS volume study with 5 mm slices and full bladder; PTV = prostate + 5 mm except 0 mm posteriorly; peripheral loading; needles loaded anterior-first to avoid US shadowing; Mick applicator vs strands; C-arm/US verification in OR; cystoscopy to remove bladder seeds; GM survey for lost seeds; CT post-plan same day and ~30 days (ABS); evaluate V100/V150/V200/D90, urethra < 150 %, rectal dose; base is hardest to cover; patient release exposure ~µR/hr level; I-125 Rx 144–145 Gy, Pd-103 110–125 Gy. **C**: isotopes, 144 Gy, Mick/strands, V-metrics, lost seeds (partial). **P**: post-plan timing (2 hits), 10 % extra/assay (5 hits, mixed), release survey, urethra (theory only). **M**: seed count range, PTV margin rule with 0 mm posterior, needle-order rationale, urethra < 150 % as an item, base-coverage difficulty, third-party assay, full-bladder/5-mm TRUS protocol.

**Protons (m07/m23)** — RBE 1.1 (higher at distal edge), most inhomogeneity-sensitive modality, HU→RSP conversion, range uncertainty, passive scatter makes more neutrons than scanning, lower surface dose than photons only with modulation, penumbra grows with depth, robust optimization, ocular 60–70 MeV. **C** almost all; **P** ocular energies.

**Radiobiology (m21)** — α/β early ≈ 10, late ≈ 3, prostate ≈ 1.5; α non-repairable/β repairable; survival-curve parameters D0 (37 %), Dq, n; cell-cycle sensitivity (M/G2 sensitive, late S resistant); OER; LET for max RBE ≈ 100 keV/µm; LD50/30 ≈ 3.5–4.5 Gy; ARS syndromes; fetal stages (preimplantation death, organogenesis 2–8 wk malformations, 8–15 wk cognitive); cataract threshold ≈ 0.5 Gy; therapeutic ratio; melanoma radioresistance; TD5/5. **C**: α/β, LQ, cell cycle, OER, LET, ARS, stochastic/deterministic. **P**: LD50 (1 hit), fetal stages (9 hits, no item), cataract (3), α/β repair interpretation. **M**: therapeutic ratio, melanoma radioresistance, TD5/5 vocabulary (QUANTEC is present).

**Clinical oncology & anatomy (m20, m22)** — typical dose list (prostate 78–80 Gy, H&N 70, lung 60–66, breast 50 + 10–16, SBRT lung 48–60, pelvis 45, PBI 34–38.5, WBRT 30, SRS mets 12–24 single, 8 Gy single palliative, TN SRS 70–90 Gy, I-125 prostate 144, Pd 110–125); TNM conventions (T0/Tx/Tis/N0/Nx); NSCLC vs SCLC; metastatic routes (melanoma hematogenous, thyroid → lung/bone); pediatric tumors (Wilms, rhabdoid, medulloblastoma CSI late effects); landmarks (carina T4–5, heart apex, pancreas L1–2, colon segments/flexures, hilum contents, anal lymphatics incl. inguinal, corpus callosum). **C**: most doses, landmarks, CSI. **P**: heart apex, pancreas level, sarcoma imaging. **M**: TN SRS dose, TNM-code definitions, melanoma spread, Wilms/rhabdoid, colon flexures, corpus callosum.

**Radiation protection & regulations (m41)** — 10 CFR 20 limits (50 mSv TEDE, 150 lens, 500 extremity/skin, 1 mSv public, 5 mSv fetus/0.5 per month, 2 mrem in any hour), 10 CFR 35 (written directive, medical event 20 %/50 %/wrong site, NRC notice next calendar day + 15-day written report, AU/QMP presence, leak test ≤ 185 Bq every 6 mo, surveys), 10 CFR 19 (worker notices/rights), 10 CFR 71/DOT (transport index = mR/hr at 1 m; White I/Yellow II/III labels), NCRP 151 (P 0.02/0.1 mSv/wk, U, T incl. 1/40 parking, leakage 0.1 %, IMRT factor, 6 TVL ≈ 8 ft concrete primary, ≈ 3 ft secondary, mazed door ≈ ¾" Pb, mazeless ≈ 6" Pb + BPE with BPE on the vault side, capture-gamma 2.2 MeV), NCRP 147 (diagnostic), TG-108 (PET), NCRP 49 (legacy), BEIR/LNT, background ≈ 3.1 mSv natural / 6.2 total, swipe action 2,200 dpm (220 ALARA), typical exposure magnitudes (console < 2 mR/hr; bedside LDR Cs patient ~100 mR/hr at 1 m; I-131 release ≤ 7 mR/hr at 1 m; seed patient ~0.1 mR/hr; cath-lab staff highest occupational), survey practice (6 MV: ion chamber + GM; ≥10 MV add neutron meter; NM daily meter + weekly wipes), Hiroshima/LSS as risk basis, dosimetry badge issuance (likely > 10 % of limit). **C**: 10 CFR 20/35 core, NCRP 151 basics, leak test, medical event, I-131 release, ALARA. **P**: parking 1/40 worked example, BPE ordering, secondary thickness, swipe limits, background split, console/bedside magnitudes. **M**: 10 CFR 19, transport index/labels, NCRP 147, TG-108, BEIR/LSS, IMRT factor, cath-lab magnitude, NM survey cadence, 2 mrem/hr figure as item.

**QA (m42)** — TG-142 tolerances (output 3 % daily/2 % monthly/1 % annual; lasers 1 mm SRS/1.5–2 mm; field size 2 mm; MLC 1 mm IMRT; flatness/symmetry 1 % baseline; gantry/collimator 1°; kV/MV imaging dose annual), picket fence, star/spoke shot, Winston-Lutz, dynamic-wedge monthly check, TG-53 → MPPG 5a (2 % CAX, 2 mm penumbra, 3–5 % out-of-field), TG-106 commissioning, TG-119 IMRT commissioning, TG-100 (FMEA, fault tree, RPN 1–1000, >125, human error most common root cause), TG-203 CIED (CT scatter seconds, 2 Gy/5 Gy tiers, in-vivo if < 10 cm), RO-ILS, IMRT QA before first fraction, high-gradient failures, gamma 3 %/3 mm, HDR source commissioning. **C**: TG-142 core, Winston-Lutz, gamma, TG-203, TG-100 concept, HDR QA. **P**: picket fence, MLC 1 mm, TG-53/TG-119, RPN specifics. **M**: star/spoke shot, dynamic-wedge cadence, MPPG 5a by name, fault tree, RPN range/threshold, "human error" root-cause fact.

**Informatics (m26/m27)** — DICOM meaning, matrix sizes (MRI 256, CT 512, DR 2048), bit depth → grey levels, file-size arithmetic, KB/MB/GB/TB, 4D data volume, archiving, data mining/benchmarking. **C**: DICOM, matrix sizes, bit depth. **M**: file-size calc, 4D data-volume estimate. Network definitions (DSL/FTP/HTTP/bus/router) are **M and irrelevant**.

### 2.3 Coverage tally

Inventory rows (facts + calc types, deduplicated): **≈ 310**. Covered ≈ 200 (**65 %**), partial ≈ 52 (**17 %**), missing ≈ 58 (**19 %**). Weighted by how often the file tests a fact, item-level coverage is higher (≈ 72 %) because the file re-asks the same decay/ISL/MU/HVL/BED families many times and those are all covered.

---

## 3. Re-computation of numeric answers

Checked 80+ typed answers; 73 reproduce. Representative verified sample (file section → quantity → my result):

| # | Section | Quantity | My result | Key |
|---|---|---|---|---|
| 1 | Opening set Q10 | Decay of a 60-mCi-class source over ~2 half-lives | 8.9 mCi | ✓ |
| 2 | Q11 | Co-60 after 2 y from 155 Ci | 119.5 Ci | ✓ |
| 3 | Q13 | Time for Cs-137 to reach ¼ | 120 y | ✓ |
| 4 | Q14/Q15 | Exposure through 2 HVL / at half distance | 39 mR/hr; 1,600 mR/hr | ✓ |
| 5 | Q17 | HVL thickness in inches for a given attenuation | 43.8 in | ✓ |
| 6 | Q22/Q23 | ISL factor; OAR interpolation | 0.9875; 1.013 | ✓ |
| 7 | Q25/Q26 | SSD and SAD MU | 146 MU; 132 MU | ✓ |
| 8 | Q30 | Gap between two SSD fields | 2.45 cm | ✓ |
| 9 | Q31 | CSI collimator angle | 10.2° | ✓ |
| 10 | Q36/Q37 | HDR time scaling; LDR total dose | 0.476 d; 133 Gy | ✓ |
| 11 | Q44–Q47 | Workload 500 & 1,600 Gy/wk; B = 2.9×10⁻⁵; leakage B 0.0067 | ✓ |
| 12 | Q48–Q50 | Dose equivalent 2,040 mrem; BED 80.64; BED pair 68.4/93.6 | ✓ |
| 13 | Q52/Q54/Q55 | CI 1.1; R50 4.55; RPN 90 | ✓ |
| 14 | Q56/Q58/Q59 | Ctp 1.011; TVL 10.05 cm; 13.5 % | ✓ |
| 15 | ST 11 | 142.5 cGy/min; 4.77 m; 25.7 eq-sq; 1.028; 71.4 %; 40,000/100,000 Gy·wk workloads; 80 mR/hr; 142 MU; 274 MU; 47 cGy/hr | ✓ |
| 16 | ST 15–17 | 0.04; 1.44 R/hr; 60 Gy; 2.5; 1.28 R/hr; 0.12 cGy/hr; 160 R/hr | ✓ |
| 17 | ST 206 | 221 MU; 24.2; (−4,−4); 4.47 m; 41.4/58.6 cm split; MF 1.055; 13.7 mR/hr; 16 MeV; 9 MeV; 27,000/81,000; BED 48; 2.22 Gy; Ctp 1.020; 0.993; ÷0.971; ÷1.067 | ✓ |
| 18 | ST 222 Q8 | Quadrature sum of three uncertainties | 3.7 mm | ✓ |
| 19 | ST 503 Q2–5, 7, 9, 10 | 2.0 cm; 205 MU; 0.607 R/hr; 22.4/77.6 cm; 4,000 mR/hr; 16 h; 144 vs 129.5 cGy | ✓ |
| 20 | ST 505 Q1, 2, 7–10 | 3.3 Gy; Ir-192 identified; 257.4 cGy; 60 %; 9.9°; ≈ 256–262 MU | ✓ |

### Wrong or unreproducible typed keys (7)

| # | Section | Problem | Correct value |
|---|---|---|---|
| 1 | ST 503 Q1 | PDD at 10 cm moved from 100 to 150 SSD; key 83.2 % | Mayneord F = 1.053 → **84.2 %** |
| 2 | ST 503 Q6 | Effective depth of tissue/hard bone/lung/tissue stack; key 9.3 cm | 2 + 1.65 + 1 + 3 = **7.65 cm** |
| 3 | ST 503 Q8 | Leakage workload; key 162,500 cGy/wk ignores the stated daily IMRT QA runs | ≈ **182,500** with QA included |
| 4 | ST 505 Q4 | Distance where 800 cGy/min at 1 m falls to 2 mR/hr; key 632 m forgets min→hr | 48,000 R/hr → **≈ 4,900 m** |
| 5 | ST 505 Q5 | 18X SAD MU (TMR, Sc, Sp, WF 0.5, 95 % norm, SSD-calibrated); key 464 | file's own convention gives **≈ 422 MU**; 464 is not reproducible |
| 6 | ST 33 Q16–20 | Matching key swaps FTP and router | FTP = file transfer; router = network routing |
| 7 | Opening set Q19 | Reports the ISL factor (0.0016) as the answer | 20 × 0.0016 = **0.032 mR/hr** |

Stem/formula typos (not key errors): ST 16 Q11 prints (1 + 1.8/10) but multiplies with α/β = 3 (answer 80.6 is right); opening set Q32 stem says a "29×29" matrix but computes 512×512×9 bits; "E/1/5" typo in one board-question copy.

Content error repeated throughout: the file attributes GTV/CTV/ITV/PTV definitions to "ICRP 62" — the correct reference is **ICRU 62**. Our bank uses ICRU 62 (15 hits) — keep it that way.

---

## 4. Outdated content (flag; do not import as-is)

- Conventional simulator and image-intensifier chain questions (several per block) — CT-sim era; keep only the magnification/divergence logic.
- TDF/NSD tables, Co-60 teletherapy heads (~9,000 Ci), "201-source" Gamma Knife (Icon has 192), NCRP 49 shielding — historical.
- "GM calibrated annually" and "film badges with H&D curves" — still true in places but OSL/TLD and electronic dosimeters are the exam-relevant answer.
- TG-53 cited as the TPS QA standard (superseded by MPPG 5.a, which the file does mention once); TG-142 cited without TG-198 (its implementation guide).
- 10 CFR 20 figures are current but presented in rem/mrem only; add SI equivalents when writing our items.
- "HDR source ≤ 10 Ci" and "dwell < 1 s deleted" are site conventions, not regulations.
- "ICRP 62" misnomer (see above).
- Dose list uses older breast (50 + 10) and WBRT (30/10) habits; hypofractionated breast (40–42.5 Gy) and 20 Gy/5 WBRT are missing.

## 5. Irrelevant to MDCB (skip)

- Pure arithmetic/CS drills: binary↔decimal, logarithm identities, midpoint/distance formulas, angles in polygons, trig definitions (cotangent etc.), ohm/ampere/coulomb/joule/hertz unit trivia, Snell's law, Planck's constant, parallel-resistance formula, conduction/convection, KB/TB conversions, DSL/FTP/HTTP/bus/router definitions (~60 items across ST 12–14, 33, 223–224, Module 29&30 blocks).
- Quarks/leptons, atomic/nuclear diameters, Hiroshima trivia beyond "LSS is the risk basis".
- Vendor minutiae (MammoSite brand workflow, Picture-of-the-day style items).

---

## 6. Summary

- **Total unique items:** ≈ 1,494 (≈ 3,000 printed with duplicates; the board-question block appears 4×, every short test 2–3×).
- **Bank coverage of the fact/calc inventory:** ≈ 65 % covered, 17 % partial, 19 % missing; item-weighted ≈ 72 % covered. Roughly 4 % of items are arithmetic/network trivia not worth covering.
- **Wrong typed keys found:** 7 (plus 3 stem typos and one systematic ICRP/ICRU misnomer). Most MCQ keys are not visible in the extraction, so the real error rate is unknown but the worked sets are generally reliable.

### MISSING facts / calc types worth adding as original items, by module

- **m03** — Cs-131 9.7 d as the fastest-delivering prostate seed; therapy activity magnitudes (I-131 100–200 mCi ablation; Sr-89/Sm-153 for bone pain; check source ~10 µCi; blood irradiator ~kCi class).
- **m07** — SF6 in the waveguide; dose rate ∝ gun current × PRF at fixed energy; FFF facts (6 MV d10 ≈ 61 %, higher dose rate, less head scatter); electron mode uses far lower beam current; primary collimator ≈ several TVL.
- **m09** — detector-to-task matching set (proportional counter α/β discrimination; dose calibrator; NaI well counter for swipes; thyroid probe; rem-ball); Farmer ~300 V; H&D and glow curves; counting efficiency cpm/dpm; ADCL 2-year chamber calibration; annual survey-meter calibration.
- **m10/m11** — CTDIw/CTDIvol/DLP/effective-dose chain; CT ≈ 0.7 lp/mm, MRI ≈ 0.3, PET 4–5 mm; iterative recon 25–40 % dose cut; third-gen ring artifacts; MRI shim coils, copper RF shield vs steel magnetic shield, field strengths; PET nuclides C-11/N-13/O-15, crystal types, 60-min uptake, 15 mCi FDG, TG-108; **ultrasound block** (1–20 MHz, ~1,540 m/s, piezo transducer, Fresnel/Fraunhofer, bioeffects, TG-128, uses in PBI/prostate).
- **m17** — rigid vs affine vs deformable definitions.
- **m19** — conformation number (van't Riet) alongside RTOG CI; dDVH axes.
- **m20** — trigeminal-neuralgia SRS 70–90 Gy; TNM code definitions (T0/Tx/Tis/Nx); melanoma hematogenous spread; Wilms/rhabdoid pediatrics; hypofractionated breast/WBRT current schedules.
- **m21** — therapeutic ratio definition; LD50/30 ≈ 3.5–4.5 Gy; fetal-stage effects (preimplantation / 2–8 wk / 8–15 wk); α non-repairable vs β repairable; melanoma radioresistance; TD5/5 vocabulary.
- **m22** — colon segments and flexures; hilum contents; corpus callosum; heart apex level.
- **m23** — IMRT factor (2–10, ~4) and its shielding use; min ~3 MU/segment; avoidance sectors; mirrored collimator angles in VMAT; VMAT vs IMRT hot-spot/MU behaviour.
- **m24** — TBI numbers (6 MV, 1,200 cGy/6 fx, 5–10 cGy/min, midplane Rx, lung blocks, spoiler, toxicities); TSET numbers (6 MeV → 3–4 MeV, dual fields, dmax < 1.3 cm, ~1 % brems midplane, eye/nail shields); IORT (lucite cones, bevel effect, eBT advantages); electron arc (velocity effect, Pb E/2 + 1 mm, 10–15° over-travel, 4–8 cm width).
- **m26/m27** — image file-size arithmetic (matrix × bits × slices → MB); 4D data-volume estimate.
- **m35/m36** — 18X SSD↔SAD correction (1.067 with dmax 3.3); primary TMR = TMR − SMR under blocks; CSI collimator angle atan((L/2)/SSD) as a numeric item; photon/electron mixed-beam MU weighting; "wedge omitted for n fractions" error.
- **m37** — ≈ 3 %/cm lung rule; three-layer effective depth with soft bone 1.1 and hard bone 1.65; expected 5–30 % hetero/homo spread.
- **m39** — SD intervals 68/95/99.7 %; quadrature addition; mean/median/mode; correlation r vs r².
- **m40** — LDR prostate workflow (60–120 seeds, 0.3 mCi, 10 % assay/third-party, 10 % over-order, 5-mm TRUS with full bladder, PTV +5 mm/0 posterior, anterior-first needle order, urethra < 150 %, post-plan ~30 d, base under-coverage); PBI balloon (1-cm PTV_eval rind, 34 Gy/10 BID, ~200 % at surface, multi-lumen skin sparing); HDR source ≈ 4 × 0.8 mm and 1 mm positioning; T&O tip-dwell reduction rationale; Sr-90 pterygium; Ra-eq exposure 8.25 R·cm²/mg·h as a numeric item; HDR A₁t₁ = A₂t₂ scaling.
- **m41** — 10 CFR 19 worker notices; 10 CFR 71/DOT transport index and White I/Yellow II/III labels; NCRP 147 scope; TG-108; BEIR/LSS as risk basis; 2 mrem-in-any-hour; cath-lab/console/bedside exposure magnitudes; NM survey cadence (daily meter, weekly wipes); swipe 2,200/220 dpm as item; door construction (¾" Pb with maze, 6" Pb + BPE without, BPE facing the vault).
- **m42** — star/spoke shot; dynamic-wedge monthly check; MPPG 5.a by name; TG-100 fault tree, RPN 1–1000 with >125 action, human error as top root cause; survey practice at ≥10 MV (add neutron meter).

### Verdict

**Complementary.** The file is weaker than our bank on rigor (keys lost in extraction, 7 wrong typed keys, some legacy content, ~60 arithmetic/network items, heavy duplication) and on explanation quality (no "why" text). It is stronger than our bank on breadth of practice facts — special procedures (TBI/TSET/IORT/electron arc), detector-to-task matching, LDR prostate and PBI workflow, exposure/activity "magnitude" cheat-sheets, ultrasound, CT dose metrics, and the regulatory corners (10 CFR 19/71, NCRP 147, TG-108). Use it as a checklist for the ~58 missing facts above and for the three missing calc variants (18X 1.067, primary TMR − SMR, CSI atan), not as a source of items.
