# RM Review: DoseGrid practice exams, RAPHEX 2023, Potholes, QUANTEC/Isotope sheets, Reminders, Study Tips

Source: `inbox/RM Review/` (third-party, copyrighted, gitignored). Text copies in `inbox/text/`.
Everything below is a paraphrased re-statement of problem *types* and *facts*; no stems, options, or explanations are copied.
Coverage marks are against the whole `knowledge/theory` + `knowledge/questions` bank by grep (ripgrep, case-insensitive, with synonym patterns), plus a full read of `theory/m43-*`, `theory/m40-*`, `theory/m03-*` for the two tables.

Marks: **C** = COVERED (fact or calc type present with the right value/direction), **P** = PARTIAL (topic present, this specific number/rule/twist absent or stated only vaguely), **M** = MISSING.

Files reviewed (all read in full; the two image-only PDFs were rendered and read as images):

| # | File | Items | Keys? | Style | Notes on OCR |
|---|------|-------|-------|-------|--------------|
| 1 | `Dose Grid Practice Exams.pdf` (90 pages of screenshots) | **155 unique MCQ**. "Practice Exam 1" = 155 items, no answers. "Practice Exam 2" = the **same 155 items reshuffled**, with the course's post-submission feedback showing on about 90 of them | Partial: ~90/155 have a visible key or a worked solution (feedback panel or handwritten work), ~65 have none; almost all of those 65 are single-fact recall and the key is obvious | 4-option MCQ, "choose only ONE best answer"; 6 image-ID anatomy items (sinuses, ventricles, skull bones, thalamus) whose images are not in the text; two 6 MV data tables (PDD/TMR/Sc/Sp for 5×5…25×25) attached to the MU items | Two-column page layout interleaves stems; options OCR-garbled but recoverable |
| 2 | `Raphex exam 2023.pdf` (therapy section) + `Raphex Answers 2023.pdf` | **140 MCQ** (T1–T140), 4–5 options | Yes, all 140, with a short rationale each | ACR/RAMPS-style physics exam written for radiation oncology residents and physicists | ~8 stems lose one or more options to OCR (T14, T15, T20, T47, T61, T79, T117, T124, T137); the answer file supplies the fact in every case except T117 |
| 3 | `Dos Boards Potholes DD 10192022.docx.pdf` | **237 numbered pitfalls** (many with a–l sub-bullets), plus pointers to the author's "Vitamin/Mineral" handouts | n/a (statements, not questions) | Instructor's "fill in the holes" list, roughly in curriculum order | Word-per-line OCR; collapsed to lines for reading |
| 4 | `Quantec.pdf` | One department OAR-constraint spreadsheet: **~70 constraint rows** × 8 dose-per-fraction columns (1.5, 1.8, **2.0**, 2.2, 2.5, 3, 4, 5 Gy/fx). Yellow column = 2 Gy/fx base values; green rows = the sheet's own QUANTEC lines; white rows = department (RTOG-style) lines | n/a | Table image; read from the rendered PNG, the OCR text is column-scrambled | |
| 5 | `Isotopes.pdf` | 7 brachy nuclides × (half-life, energy, Γ, HVL in Pb) | n/a | One-page ARC "Brachy Source Page" | Clean |
| 6 | `Reminders for Review for the Final Exam.pdf` | 14 "updated in our field" reminders | n/a | Instructor bullets | Clean |
| 7 | `Study Tips.docx` | 2 lines | n/a | | Clean |

---

## 1. DoseGrid practice exam (155 items)

### 1.1 Counts, keys, domain split

- 155 unique items; the second exam is a reshuffle of the first, so the file contains **155**, not 310, distinct questions.
- Keys: visible for ~90 (58%); none for ~65. Where the feedback panel appears, it includes a 2–6 line rationale, sometimes with a mnemonic.
- 30 items are numeric calculations (19%); 6 are image-ID anatomy (4%); the remaining 119 are single-fact recall or one-step reasoning.
- Approximate MDCB-domain split (own classification): I Physics/machines/measurement 45 (29%) · II Localization/imaging/sim 12 (8%) · III Planning incl. site oncology, anatomy, radiobiology 55 (35%) · IV Dose calc 22 (14%) · V Brachy 9 (6%) · VI Protection 6 (4%) · VII QA/IT/regulatory 6 (4%). Compared with the MDCB blueprint (III = 42%, IV = 13%) this exam is light on planning depth (most "planning" items are one-liner clinical facts) and has no DVH-reading, no plan-comparison, and no slice-based items beyond the six anatomy pictures.

### 1.2 Fact and calc-type inventory, with coverage

Numbers are the exam's values, restated. "Our" = what the bank says when it differs.

**Calculation types (30)**

| # | Calc type (values restated) | Key shown? | Mark | Where / note |
|---|---|---|---|---|
| 1 | Identify nuclide from decay constant 0.00936 d⁻¹ → T½ ≈ 74 d → Ir-192 | yes | C | m03 |
| 2 | Dose at a deeper point on the same SAD beam from a TMR ratio (0.862/0.949) **times** an inverse-square (100/103)² → 171 cGy | yes | C | m35 does TMR ratios; the extra inverse-square step is defensible only if the 7 cm point is read as 3 cm beyond isocenter; the stem does not say so. Note as ambiguous, not wrong |
| 3 | Skin gap for two 30 cm fields matched at 8 cm depth, 100 SSD: 2 × (15 × 8/100) = 2.4 cm | yes | C | m36 |
| 4 | Exposure rate Γ·A/d²: 1.9 R cm²/mCi h × 200 mCi / 300² → ~4 mR/h | yes | C | m40 |
| 5 | Lead for 12 MeV electrons: E/2 mm → 6 mm | yes | C | m19, m45 |
| 6 | Lead to reduce to 20% with HVL 3.8 mm: log₂5 = 2.32 HVL → 8.8 mm | yes | C | m36, m41 |
| 7 | CSI: collimator angle = atan(½ spine length/100), couch = atan(½ brain-field length/100) → 7.4° / 3.4° | yes | **M** | `craniospinal` appears in m19/m20/m36/m44 but no item computes the two angles |
| 8 | AP/PA midplane 200 cGy, separation 20, AP set at 95 SSD (iso at 105) → AP half × (100/105)² → 191 cGy; same type with 300 cGy, sep 22, 90 SSD → 297 cGy | yes | C | m35/m44 (wrong-SSD set-up error) |
| 9 | Hot spot 300 cGy at 100% renormalized to 90% → 333 cGy | yes | P | renormalization concept present (m19/m25); this exact arithmetic twist not drilled |
| 10 | Isocentric MU with Sc (collimator 15×15) and Sp (MLC-shaped 10×10), TMR at 8 cm → 234 MU | yes | C | m35 |
| 11 | Opposed tangent angle: 180 + 57 − 2·atan(12/100) → 223° | yes | C | m36 (tangent geometry) |
| 12 | Permanent implant total dose = 1.44 × T½ × Ḋ₀ (17 d, 0.5 cGy/h → 294 cGy; 30 d → 518 cGy) | yes | C | m03, m40 |
| 13 | Cerrobend transmission 2^(−1.27/1.6) = 0.58 → 42% attenuated | yes | C | m36, m41 |
| 14 | Electron MU from a cutout/cone ion-chamber ratio (92/99.5) and 88% IDL → ~307–309 MU | yes | C | m35, m42. The source multiplies by 0.92 instead of 92/99.5 = 0.925 (307 MU); nearest option is still 309 |
| 15 | 6 HVL on 150 cGy/min → 2.34 cGy/min | yes | C | m36 |
| 16 | Wedge omitted on one treatment: 0.6/0.4 weighting, WF 0.70 in the PA → 180 + 120/0.70 = 351 cGy | yes | C | m34, m42 |
| 17 | Port-film block shift scaled by tray/film distance 75/127 × 2.5 → 1.5 cm | yes | C | m08 |
| 18 | Equivalent square 12×20 → 15×15 (2ab/(a+b)) | yes | C | m35 |
| 19 | POP at 80 SSD, 60 Gy midplane, 20 cm diameter: Ddmax per field = 30/0.636; entrance 100% + exit at 18.8 cm (interpolated PDD 37.2%) → 64.7 Gy | yes | C | m35 (entrance+exit), interpolation drill |
| 20 | Hinge angle from wedge angle 20° → 140° | yes | C | m34 |
| 21 | 21 mCi → 777 MBq | yes | C | m03, m12 |
| 22 | Cs-137 30 mCi after 7 y → 25.5 mCi | yes | C | m03 |
| 23 | mg-Ra-eq from Γ ratio: 3 mCi × 4.69/8.25 → 1.7 | yes | C | m40 |
| 24 | Single-field SSD MU with PDD, equivalent square 8×10 → 8.9, 180 cGy at 8 cm | no | C | m35 |
| 25 | Exposure rate from a radium-equivalent strength (0.241 mgRaEq/mCi × 0.825 R m²/Ci h, 100 mCi, 2 m → 0.005 R/h) | yes | C | m40 (Ra constant route) |
| 26 | Split 300 cGy by weights 30:90:40 → 56.3 / 168.7 / 75 | no | C | m25 (weighting) |
| 27 | Geometric penumbra s(SSD + d − SDD)/SDD with s = 2, SDD = 20, d = 3 → 8.3 cm | yes | C | m07, m36 |
| 28 | Orthovoltage timer: R/min × f × BSF × inverse square (50/55)², dose at dmax = 180/0.63, then add 24 s timer error → 2.8 min | yes | C | m36 (orthovoltage/timer error) |
| 29 | Right-triangle side from 40° and 5 cm (x = 5/tan 40) | yes | C | m36 trig |
| 30 | Linac RF 3000 MHz → λ = 10 cm | yes | P | wavelength = c/f is in m02/m06; the linac-specific 3 GHz/10 cm number is not stated |

**Fact items (119 non-image + 6 image)** grouped by module:

| Module | Fact (restated) | Key shown? | Mark |
|---|---|---|---|
| m02/m03 | Isotopes share Z; isobars share A; same Z → same protons and electrons; secular vs transient equilibrium wording; gamma rays are not particulate; Compton photon can scatter at any angle (electron 0–90° only); E = hf, longer λ = lower E; electron capture nuclides | mixed | C |
| m03/m40 | I-125 T½ 60 d; I-125 photon "energy 35 keV" | yes | P — bank uses ~28 keV mean (35 keV is the top photon line); add a note that both numbers appear on tests |
| m04 | Halving kV cuts tube output most (output ∝ kV²); bremsstrahlung = radiative electron–nucleus collision; "critical absorption energy" as the threshold for characteristic emission | partly | C / P (the exact phrase "critical absorption energy" is not used; binding energy is) |
| m05/m06 | Photoelectric gives bone contrast; Compton independent of Z; kerma > dose before dmax; microwaves non-ionizing; horns from the flattening filter | yes | C |
| m07 | FFF beam has lower mean energy (and not "flatter"); monitor chamber watches symmetry/flatness; linac head ion chamber; Winston–Lutz = mechanical vs radiation isocenter; cones vs MLC for SRS → sharper penumbra; geometric penumbra falls as SDD rises; tongue-and-groove reduces interleaf leakage | yes | C except **cones-vs-MLC penumbra (M)** |
| m09 | Thimble-wall properties (air-equivalent, thick enough for CPE; it is *not* a low-energy filter); free-air chamber = delicate standards-lab instrument; parallel-plate for surface/build-up and low-energy electrons; T–P factor > 1 when P < 760 mmHg and T > 22 °C; solid-water matched on electron density; TAR = TMR × BSF | mixed | P (thimble wall list and the T–P direction are not spelled out; the rest C) |
| m10/m11/m18 | MV CBCT tolerant of metal streaks; TG-66 uniformity ±5 HU; HU of muscle ≈ +40; HU linear with μ but not with electron density (Z-dependence of photoelectric); PET fused for lung GTV; Gamma Knife plans on MRI; CT **over**estimates prostate size vs MRI; surface-guidance fails when the surface is covered | mixed | C except **CT-overestimates-prostate (M)** and surface-obstruction (P) |
| m12/m41 | Gy/Sv SI pair; extremity 500 mSv/y; shielding uses W, U, T, d (not patient count); borated polyethylene for neutrons; stochastic = cancer; random error = daily bladder filling; personnel badge properties | mixed | C except badge-properties item (P) |
| m13/m16 | Contour acquisition methods (CT, lead wire, pantograph, calipers); scan that cuts off lung most affects **mean** lung dose; electron density drives heterogeneity correction; calcification needs no override (artifact, wire, contrast do) | yes | **M** (pantograph/lead wire), P (lung cut-off), C, **M** (calcification stays) |
| m19/m25 | Volume nesting GTV<CTV<ITV<PTV<treated<irradiated; wedge angle = isodose tilt; differential DVH shows volume in a dose bin; Clarkson for irregular fields; feathering a junction; photon–electron match hot spot on the photon side; electron obliquity pulls dmax toward the surface; 9 MeV lower surface dose than 16 MeV; Rp ≈ E/2 (10 MeV → 5 cm); electron tail = bremsstrahlung; bigger cutout-to-skin gap → more MU; energy for 90% at 4 cm | mixed | C; the 90%-depth rule is **P** (see wrong-keys list) |
| m20/m22 | Pylorus connects stomach to duodenum; prostate = adenocarcinoma; seminoma hockey-stick field; base-of-tongue organ preservation; sarcoma: spare a skin strip; SCLC gets PCI; small cell most radiosensitive lung histology; seminoma most radiosensitive of the listed; skin cancer most common US cancer; colorectal → liver; esophagus primary-RT 5-year survival; most common childhood CNS tumour; liver is its own dose-limiting organ; off-cord technique at 45 Gy; six image-ID items (paranasal sinuses ×2, maxillary antrum/cribriform plate, 4th ventricle/cerebellum, thalamus/hippocampus) | mixed | **M**: pylorus, prostate histology, hockey stick, base of tongue, skin-cancer rank, colorectal-liver, esophagus survival, all 6 image items. C: sarcoma, PCI, small cell, off-cord, liver. P: seminoma radiosensitivity, childhood CNS (bank names medulloblastoma) |
| m21 | D₀ = dose for 37% survival; M/G2 most sensitive; Bergonié–Tribondeau; LD50/60 ≈ 3–4 Gy; CNS syndrome > 12 Gy; proton RBE 1.1 | mixed | C, C, **M**, **M**, **M**, C |
| m23/m24 | TBI dose rate (5–10 cGy/min); beam spoiler → ≥ 90% surface; TSET boost sites (perineum, soles, palms) vs fingernails; SBRT favours non-coplanar beams; full-arc VMAT has the worst clearance problem; pencil beam least suited to lung SBRT; Monte Carlo most accurate for electrons; mid-course 15 MV → 6 MV machine change needs a recalculation/replan | mixed | P (no TBI dose-rate number), C, P, C, C, C, C, **M** |
| m26/m27 | DICOM expansion; LAN; ROM | mixed | C, P (networks mentioned, LAN not defined), **M** |
| m30 | Auto-segmentation goal = less inter-user variation | no | C |
| m31 | TG-34 pacemaker < 2 Gy total; avoid 18 MV near a device | yes | C (bank uses TG-203 tiers) |
| m33/m34/m35 | Mayneord corrects PDD for SSD; TMR depends on field size, energy, depth only; SAD→SSD raises MU and SSD→SAD lowers it; extended 110 SSD raises MU on both fields without changing dose; physical wedge works at any collimator angle (EDW does not); physical wedges historically avoided for breast because of scatter to the contralateral breast; equivalent square least accurate for 4×20; compensator/tray ≥ 15–20 cm from skin to keep skin sparing | mixed | C, C, C, C, P, P, C, **P** (skin-sparing reason present, the 15–20 cm distance number absent) |
| m37 | Lung path 3 cm tissue + 9 cm lung: turning heterogeneity correction off | yes | C but the bank's direction is the opposite of this key, see 1.3 |
| m40 | Point A definition; active length vs physical length; esophagus/bronchus = intraluminal; I-125 monotherapy 145 Gy (stem says "HDR"); HDR calibration traceable to NIST | mixed | C, **M** (active/physical length), P, C, C |
| m42/m43 | Daily output ±3%; near-miss definition; AAMD as the dosimetry society; QUANTEC cochlea mean 45; QUANTEC lung V20 < 30%; **QUANTEC spinal-cord single-fraction SRS limit 13 Gy**; compact bone ≈ 1.65 g/cc | mixed | C, C, C, C, C, **M** (m43 has TG-101 14 Gy point max but not the QUANTEC 13 Gy / 20 Gy-in-3 line), C with a value conflict (bank 1.85) |
| m44 | Acute radiation syndromes table (hematopoietic 2–3 Gy months; GI 5–12 Gy ~1 week; CNS > 12 Gy ~1 day) | yes | **M** |

Tally for DoseGrid: **C 110 · P 19 · M 26** → 71% covered, 83% covered-or-partial.

### 1.3 Keys that look wrong or shaky (DoseGrid)

1. **Heterogeneity correction turned off on a 3 cm tissue + 9 cm lung path → key "underdose".** A homogeneous calculation assumes 12 cm of water, over-estimates attenuation, and asks for more MU than the lung path needs; delivering those MU **over**doses the target distal to lung (lateral-equilibrium loss aside). The bank (`theory/m37`, `questions/m37`) already states that the uncorrected calc *underestimates* dose beyond lung, i.e. the opposite direction from this key. Treat the DoseGrid key as **wrong** (or at best a confusion between "calculated dose is low" and "patient is underdosed").
2. **Electron energy for the 90% line at 4 cm → key 12 MeV, justified with "R90 = E/2.8".** E/2.8 is the usual 80% rule; the 90% rules in circulation are E/3.2 (Khan) or E/4 (Bentel). With either 90% rule 12 MeV reaches 3.0–3.75 cm, i.e. short of 4 cm; 16 MeV is the energy that covers 4 cm. Our `theory/m45` already teaches both author conventions and lands on 16 MeV for a Khan-style stem. Flag as **questionable**; the "Reminders" file from the same instructor set explicitly says d90 = E/3.2 and d80 = E/2.8, contradicting this DoseGrid rationale.
3. **I-125 photon energy → key 35 keV.** Bank recall is ~28 keV (mean); 35.5 keV is the highest line. Not wrong, but inconsistent with the bank's number; worth a one-line note in m03/m40 that both appear.
4. **"Prostate HDR using I-125" → 145 Gy.** Value is right for I-125 LDR monotherapy; the stem mislabels a permanent LDR seed implant as HDR.
5. **Bergonié–Tribondeau → "long mitotic cycle".** The law says a long mitotic *future* (many divisions ahead), not a long cycle. Wording error in both stem and key.
6. Electron cutout MU (item 14 above): rationale divides by 0.92 instead of 0.925; answer unaffected.
7. Deeper-point TMR calc (item 2): the inverse-square step is only right if the 7 cm point lies beyond isocenter; the stem is silent. Ambiguous rather than wrong.

Wrong-key count for DoseGrid: **1 wrong, 4 questionable/wording, 2 ambiguous.**

---

## 2. RAPHEX 2023 therapy section (140 items)

### 2.1 Counts, keys, domain split

- 140 items, all keyed with rationale. 5-option format (A–E) for most.
- Calculation items: 18 (13%). Everything else is one-step reasoning or recall, but the recall is physicist-grade (quantities, detectors, task-group numbers).
- Domain split (own count): atomic/nuclear/EM basics 12 · x-ray tubes & linac components 8 · interactions & dosimetric quantities 10 · detectors/measurement 13 · photon beam physics & MU 19 · electrons 7 · devices/QA/TG-142 8 · informatics/AI 3 · protection & regulations 7 · imaging physics & IGRT 18 · planning/IMRT/motion 15 · special procedures (TBI, TSET, IORT, SRS) 9 · brachytherapy 13 · protons 6 · safety culture (FMEA, medical events, secondary calcs) 3. Roughly MDCB-domain: I 55 · II 18 · III 25 · IV 12 · V 13 · VI 7 · VII 10.

### 2.2 Inventory with coverage and dosimetrist relevance

"Phys" = physicist-level, not something the CMD exam blueprint asks; skip for the dosimetrist bank.

| T# | Fact / calc (restated) | Mark | Phys? | Note |
|---|---|---|---|---|
| 1 | λ = c/f (500 kHz → 600 m) | C | | m02/m06 |
| 2 | KE = ½mv² | — | **Phys** | general mechanics |
| 3 | Sievert = SI unit of equivalent dose | C | | |
| 4 | Fully ionized hydrogen = proton | C | | |
| 5 | Mass excess 0.001281 amu × 931 MeV → endoergic 1.19 MeV | — | **Phys** | |
| 6 | β⁻ emits electron + antineutrino | C | | m03 |
| 7 | β⁺ and electron capture compete | C | | m03 |
| 8 | β decay mediated by the weak force | — | **Phys** | |
| 9 | Beam quality: HVL (kV), mean energy (Co/Cs), PDD or TPR₂₀,₁₀ (linac) | C | | m05/m07 |
| 10 | Bremsstrahlung becomes forward-peaked at MV energies → transmission target | C | | m07 |
| 11 | Added filtration: mean energy up, fluence down | C | | m04 |
| 12 | Max photon energy = kVp; peaks = characteristic lines | C | | m04 |
| 13 | Focusing cup is on the cathode, negative | C | | m04 |
| 14 | Anode cooling (stem lost) | C | | m04 |
| 15 | Secondary position readouts → interlock when primary/secondary disagree | C | | m07/m42 |
| 16 | Rounded leaf end keeps penumbra constant across leaf travel | C | | m34 |
| 17 | Scattering foil is in the electron path only | C | | m07 |
| 18 | Microwave waveguide accelerates the electrons | C | | m07 |
| 19 | ODI reads SSD | C | | |
| 20 | Couch rotation about the vertical axis = yaw (6DoF couch) | C | | m32; the RAPHEX rationale's "rotation around the coronal plane" phrasing is loose, the key is fine |
| 21 | Beam hardening: HVL₂ > HVL₁ | C | | m04/m05 |
| 22 | Photoelectric = photon fully absorbed, electron ejected | C | | |
| 23 | Minimum Compton-scattered photon energy 0.256 MeV (back-scatter) | C | Phys-ish | m06 has it |
| 24 | Pair production threshold 1.022 MeV | C | | m03/m06 |
| 25 | Protons are directly ionizing | C | | |
| 26 | Narrow-beam geometry measures primary only | C | | |
| 27 | HU 1000 ⇒ μ = 2 μ_water | C | | m11 |
| 28 | Inverse square | C | | |
| 29 | Exposure/KERMA/TERMA are defined for uncharged particles; dose for both | C | | m09 |
| 30 | KERMA definition | C | | |
| 31 | Fluence = particles through a sphere's cross-section | C | Phys-ish | |
| 32 | Diode signal ≫ ion chamber (Si density ~1900× air, W ≈ 3.5 eV) | P | **Phys** | diodes covered; the two numbers are not |
| 33 | 0.03 cc chamber: better resolution, more noise | P | **Phys** | |
| 34 | MV phantom material must match electron density | C | | m37/m43 |
| 35 | TLD emits light on heating | C | | m09 |
| 36 | FFF dose-per-pulse raises P_ion (TG-51) | P | **Phys** | |
| 37 | MOSFET for in-vivo electron skin dose | **M** | **Phys** | |
| 38 | Free-air chamber needs a uniform collecting field | P | **Phys** | |
| 39 | Guard electrode defines the active volume / cuts leakage | **M** | **Phys** | |
| 40 | OSLD is the one without immediate readout | C | | m09/m42 |
| 41 | CSI: cranial collimator angle uses the **spine** field length; spine couch angle uses the **cranial** field length | **M** | | not in m36 |
| 42 | Two spine fields should intersect **anterior** to the cord | **M** | | |
| 43 | Geometric penumbra shrinks when SDD grows | C | | |
| 44 | Inverse-square affects PDD but not TMR | C | | m09/m13 |
| 45 | Isocentric MU with 4A/P equivalent square (6×12 → 8), Sc·Sp·TMR → 235 MU | C | | m35 |
| 46 | Adding MLC blocking: Sc unchanged, Sp falls | C | | m09 |
| 47 | (stem lost) | — | | |
| 48 | FFF surface dose is higher than flattened; TPS surface dose inaccurate; higher energy → lower surface dose; surface dose rises with field size | **M** (FFF part) | | rest C in m05/m07 |
| 49 | FFF 6 MV PDD₁₀ ≈ 3% lower than flattened | P | | m07 says "FFF is not harder"; no number |
| 50 | Mayneord at 135 SSD, 6 cm: ≈ +2% | C | | m33 |
| 51 | Lung is the site where heterogeneity correction changes MU most | P | | implied in m37, not stated as a comparison |
| 52 | 15 MV TMR ≈ 2.5%/cm; 3 cm extra depth on one of four box fields → ≈ 2% low at iso | **M** | | the %-per-cm rule is used for other things in m13/m19 but not as a TMR-error estimate |
| 53 | Skin flash = margin beyond skin for breathing/set-up | C | | m13/m25 |
| 54 | Wedge angle = angle between a specified isodose and the perpendicular to the CAX (10 cm) | C | | m34 |
| 55 | Energy up → dmax deeper, PDD₁₀ higher | C | | m07 |
| 56 | 25×25 defined at iso (5 cm depth) → 20×20 collimator setting at 120 SSD | C | | m02/m33 (field-size scaling to 100 cm) |
| 57 | Algorithm accuracy ranking: equivalent-TAR < pencil-beam < convolution/superposition < Monte Carlo | P | | m33/m37 rank MC and PB; ETAR/Batho not named |
| 58 | Flatness = (Dmax − Dmin)/(Dmax + Dmin) × 100 over central 80% | C | Phys-ish | m19 |
| 59 | Out-of-field dose: patient scatter near the edge, head leakage far away (TG-158) | P | **Phys** | m31 touches it |
| 60 | d90 ≈ E/3.2 → 12 MeV for 3.75 cm | P | | bank uses E/4 (Khan-style wording in m45) and E/3.2 only as "the other author"; see DoseGrid key 2 |
| 61 | CET for bone 1.5: 3 cm tissue + 2 cm bone = 5 cm geometric range for 12 MeV (6 cm water) | C | | m37 (CET) |
| 62 | Obliquity: dmax shallower, faster fall-off | C | | |
| 63 | Patient tissue is the smallest contributor to electron x-ray contamination | C | | m19 |
| 64 | Electron MU = dose / (IDL fraction × output × cone-cutout factor) → 466 | C | | m35/m42 |
| 65 | Electron effective-SSD gap correction (87/88)² → −2% | C | | m19/m35 |
| 66 | < 10 MV preferred near a pacemaker because ≥ 15 MV makes neutrons | C | | m05/m31 |
| 67 | TG-203: non-dependent patient, 6 MV, 2–5 Gy = medium risk | C | | m31 |
| 68 | TG-142: imaging/treatment isocenter coincidence checked **daily** (≤ 2 mm; 1 mm SRS) | C | | m18/m42 |
| 69 | TG-142: output measured **in water** annually (TG-51); monthly constancy otherwise | C | | m42 |
| 70 | TG-142: flatness/symmetry monthly | C | | m42 |
| 71 | Jaw mechanical accuracy underlies star shots, light/rad, jaw-WL, steering | — | **Phys** | |
| 72 | TG-201 data path: sim → TPS → TMS (R&V) → delivery | C | | m42 |
| 73 | The TMS does not hold the diagnostic contouring studies | C | | m42 |
| 74 | Machine learning = pattern-learning without explicit programming | **M** | | m29/m30 do not name ML/AI |
| 75 | Geiger–Müller region on the gas-detector curve (~1000–1400 V) | C | **Phys** | m09 |
| 76 | Neutron door: a few inches of polyethylene; > 10 MV only; longer maze helps | C | | m05/m41 |
| 77 | NCRP 102: badge anyone likely to exceed 10% of the limit | C | | m42/m43 |
| 78 | Lead apron pays off for fluoroscopy, not Cs-137 or seed implants | C | | m40/m41 |
| 79 | Use factor for leakage = 1 | C | | m41 |
| 80 | LNT underlies protection standards | C | | m41 |
| 81 | Ultrasound: higher frequency → less penetration, better axial resolution | C | | m10 |
| 82 | MRI signal = hydrogen nuclei | C | | m10 |
| 83 | PET images 511 keV annihilation photons | C | | |
| 84 | Planning CT needs a measured HU-to-density curve per scanner | C | | m11/m37 |
| 85 | TG-132: rigid (6 DoF) < affine (+scale/shear) < deformable (per-voxel vectors) | C | | m17 |
| 86 | DIR appropriate: PET/CT to sim-CT in H&N; not MRI↔CT, not pre/post prosthesis, not intracranial | C | | m17 |
| 87 | Doubling pixel size: low-contrast resolution up, high-contrast down | **M** | **Phys** | |
| 88 | Metal artifact reduction software | C | | |
| 89 | Dual-energy CT acquisition methods | **M** | **Phys** | |
| 90 | Aliasing from under-sampling | **M** | **Phys** | |
| 91 | Lung window/level for low-HU targets | C | | m10/m16 |
| 92 | DVH cannot show where the hot spot is | C | | m19 |
| 93 | V20 = 25% means 25% of lung gets ≥ 20 Gy | C | | |
| 94 | IGRT is what shrinks the ITV→PTV margin (not IMRT, 4DCT, energy) | P | | m18 mentions; not as a contrast with IMRT/4DCT |
| 95 | ITV at the diaphragm: contour every phase, MIP under-estimates | C | | m15 |
| 96 | CBCT covers the sup/inf range in one rotation; more scatter, worse HU | P | | m18 covers scatter/HU; one-rotation geometry not said |
| 97 | Planar kV cannot align a soft-tissue/soft-tissue interface | C | | m18/m32 |
| 98 | TG-180: kV CBCT organ dose ≈ 0.5–5 cGy per scan | C | | m18/m32 |
| 99 | Optical surface imaging cannot localize deep targets | C | | |
| 100 | Daily CBCT is not intrafraction motion management | C | | m32 |
| 101 | Gamma 3%/3 mm, 10% threshold: 98% of evaluated points have γ < 1 | C | | m42 |
| 102 | DCA vs VMAT: both move MLC; only VMAT is inverse-optimized IMRT | P | | m23 one line |
| 103 | Intensity map = fluence per beamlet | C | | m23/m25 |
| 104 | Over-modulation lowers the PSQA pass rate (and raises MU, time, neutrons, wear) | P | | m42 complexity hints |
| 105 | Objective function has no term for HU-artifact compensation | C | | m25 |
| 106 | A wrong CTV→PTV margin is not something PSQA can catch | C | | m42 |
| 107 | Step-and-shoot pauses the beam between segments | C | | m23 |
| 108 | EPID advantage over chamber arrays = spatial resolution; disadvantages energy/field-size dependence | P | | EPID mentioned (m08/m18/m24), not compared with arrays |
| 109 | AP/PA TBI prescribed at the umbilicus | C | | m24 |
| 110 | Most homogeneous TBI = 15 MV AP/PA (smaller, more uniform separation) | **M** | | m24 has no AP/PA-vs-lateral comparison |
| 111 | F-18 is cyclotron-made; I-125, Cs-137, Co-60, Ir-192 reactor-made | C | | m07 |
| 112 | TSET x-ray contamination peaks on the CAX, hence beams angled above/below | **M** | | m24 has the angled-beam set-up but not the reason |
| 113 | IORT does not use MV photon linacs | C | | m24 |
| 114 | SRS cones lengthen SDD → smaller geometric penumbra | **M** | | (also DoseGrid) |
| 115 | Detector too big for a small field: output factor low, penumbra wide | P | **Phys** | m24/m39 volume averaging |
| 116 | SRS is less homogeneous, more conformal than fractionated IMRT | C | | m24 |
| 117 | 20 Gy to the 60% line → max 33.3 Gy | P | | m24 states "centre ≈ 2× at the 50% line"; no division drill |
| 118 | CI < 1 (options lost; key is the "PIV smaller than target" reading) | C | | m19/m24; cannot verify the lettered key |
| 119 | Larger HDR cylinder lowers the surface hot spot for a 5 mm prescription | C | | m40 |
| 120 | Pressurized sealed ion-chamber survey meters: more sensitive, no T–P correction, need a check source | **M** | **Phys** | |
| 121 | Pd-103 shortest half-life of the five | C | | |
| 122 | Transport index = mrem/h at 1 m from the package | **M** | | |
| 123 | Lower seed strength → more seeds, longer procedure, same precautions | **M** | | |
| 124 | Manchester (Paterson–Parker) uses non-uniform loading for uniform dose; Quimby/Paris uniform loading | **M** | | the bank's "Manchester" is point A only |
| 125 | I-125 anisotropy varies more with angle than Ir-192 because its low-energy photons are absorbed in the capsule | P | | anisotropy function defined in m40; no nuclide comparison |
| 126 | g(r) is the TG-43 term for attenuation/scatter along the transverse axis | C | | m40 |
| 127 | 15 Ci Ir-192, 2 m, 10 s → ≈ 5 mR | C | | m40 Γ route |
| 128 | 600 → 30 μR/h is 1.30 TVL of patient attenuation | C | | m41 (TVL) |
| 129 | 15 Ci replacing 10 Ci: log₂(1.5) = 0.59 HVL × 0.6 cm → 0.35 cm more lead | C | | m41 HVL calc type |
| 130 | Activity (not apparent activity, not S_K) ignores encapsulation | C | | m40 |
| 131 | TG-43 assumes water; no heterogeneity | C | | m40 |
| 132 | NRC HDR daily source-position check ±1 mm | **M** | | m40 has no positional tolerance |
| 133 | TG-59: the physician removes the applicator in an emergency | **M** | | m40 names TG-59 but not the role |
| 134 | Proton RBE is highest at the distal Bragg-peak edge | C | | m19/m21 |
| 135 | Pediatric proton benefit = no exit dose | C | | m19 |
| 136 | 3 Gy physical × 1.1 → 3.3 Gy(RBE) | C | | m19 |
| 137 | Range modulator wheel builds the SOBP (passive scattering) | C | | m19 |
| 138 | Range uncertainty ≈ 2.5–4% of range → distal overshoot | C | | m19/m25 |
| 139 | A secondary calc catches a beam-model error, not output/MLC/jaw/motion errors | P | | m42 covers secondary checks; scope-of-detection statement absent |
| 140 | NRC medical event: referring physician notified unless harmful | C | | m42 |
| 141 | TG-100 FMEA O/S/D indices ≈ logarithmic | C (FMEA) / P (log scale) | Phys-ish | m42 |

(The exam has 140 items; T47 is lost to OCR and T141 above is the last item, numbered 140 in the exam.)

Tally for RAPHEX: **C 107 · P 14 · M 19** → 76% covered. Of the 19 missing, 6 are physicist-only (T37, T39, T87, T89, T90, T120); **13 missing items are dosimetrist-relevant** (T41, T42, T48, T52, T74, T110, T112, T114, T122, T123, T124, T132, T133).

Physicist-level items not worth adding (22): T2, T5, T8, T23, T31, T32, T33, T36, T37, T38, T39, T58, T59, T71, T75, T87, T89, T90, T115, T120, T141, and the T14 anode-cooling detail.

### 2.3 RAPHEX keys that look wrong

None of the 140 keys is wrong on the physics. Two rationales are loosely worded: T20 (yaw described as rotation "around the coronal plane"; the key, yaw, is right) and T69 (says output "in water" is annual, which is the TG-51 absolute calibration; monthly output constancy is separate, the key matches the question's wording). T117's options are lost to OCR, so the lettered key cannot be checked.

---

## 3. Potholes list (237 pitfalls)

One line per numbered pitfall, restated; mark says whether the bank's theory or a "Why" already warns about it. Grouped by the list's own order.

**Atomic / nuclear / units (1–22)**
1–2. Mass and energy interchange, E = mc². **M** (not stated anywhere; low value).
3. Mass defect: nucleon masses exceed the C-12 mass; the difference is binding energy. **M**.
4. Shell capacity 2n² (K2 L8 M18 N32). P (m02 mentions shells, not the formula).
5. Four forces; weak force drives decay. **M**.
6–7. Decay is random per nucleus, predictable in bulk. C (m03).
8. Decay modes list (α, β⁻, β⁺, γ, EC, IT; the list also puts photodisintegration here, which is an interaction, not a decay). C (m03), with the bank correctly keeping photodisintegration in interactions (m06).
9–12. Proton-rich → β⁺/EC; neutron-rich → β⁻. P (m03 states what each mode does to Z; the "which way is the nucleus off" rule appears only in a question Why).
13. Photodisintegration: high-energy photon knocks out a neutron. C (m05/m06).
14. Old vs SI unit table (Ci/Bq, R/C kg⁻¹, rad/Gy, rem/Sv). C (m12).
15. 1 Ci = 3.7 × 10¹⁰ Bq. C.
16. 1 Bq = 2.7 × 10⁻¹¹ Ci. **M** (only the forward factor is given).
17. Mean life = 1.44 T½. C.
18. Specific activity = activity per mass. C (m03).
19. "6X" = 6 MV; max 6 MeV; mean ≈ 2 MeV (one third). P (m04 states the one-third rule; not applied to 6 MV explicitly).
20. "6E" = 6 MeV electrons, essentially monoenergetic at the surface. C (m07/m19).
21–22. μ in cm⁻¹; μ/ρ in cm²/g. **M** (units never spelled out).

**X-ray production and radiation types (23–47)**
23. Line-focus principle: angled target, smaller apparent focal spot, better resolution. C (m04).
24. Tube vacuum; a breach arcs, no beam. P (m04 mentions vacuum).
25. Characteristic = discrete, competes with Auger; bremsstrahlung = continuous, mean ≈ ⅓ max; filtration leaves max energy and K-edge unchanged. C (m04, m02).
26–27. Discrete vs continuous spectra. C.
28–29. More filtration: lower surface dose, lower contrast (imaging). **M** as an imaging statement (m04 covers hardening only).
30. X-rays vs gammas differ by origin only. C (m02).
31–33. Particulate (mass, charge) vs EM. C.
34. 1 eV = 1.6 × 10⁻¹⁹ J. **M**.
35–36. Ionizing (x, γ, far UV) vs non-ionizing (microwaves). C.
37. EM spectrum order; high frequency = short wavelength. C.
38–39. Directly ionizing (charged) vs indirectly (photons, neutrons). C (m02/m05).
40–41. Neutrons: high weighting factor, energy-dependent, via recoil protons. C (m05/m12).
42–45. E = hν, Planck's constant, c = λν, linac 3 GHz ↔ 10 cm. C except the linac 10 cm number (P).
46. Four photon interactions. C.
47. Coherent scatter deposits no energy. C (m06).

**Densities, f-factor, linac operation (48–61)**
48. Density table: lung 0.25–0.33, fat 0.95, water 1, breast 1.02, muscle 1.05, blood 1.06, soft bone 1.10, hard bone 1.60. P — m43 has lung/fat/water/muscle/bone but with fat 0.92, bone 1.85 and no breast/blood/spongy-bone rows.
49. "Fat has higher electron density than muscle" → higher dose; CT separates fat well. **M**, and the statement is only true per gram (more hydrogen), not per cm³; worth a careful line in m11/m37 rather than a copy.
50–51. Dose = exposure × f; f depends on material and energy. C (m09/m12).
52. Dose per roentgen is higher in bone (low energies). C (m05/m09).
53–56. What sets linac energy (guide length, RF power/frequency, current) vs dose rate (gun current, pulse-rate); beam current higher for photons than electrons. **M** (m07 has components, not these control relationships).
57–58. X-ray yield depends on Z and E; ≈ 1% at kV, ≈ 40% at MV. C (m04 gives efficiency).
59. FFF: peaked profile, slightly shallower dmax, lower PDD. P (m07 covers peaked and "not harder"; no PDD/dmax statement).
60–61. Photon-beam contamination is electrons; electron-beam contamination is bremsstrahlung (from head, foils, applicator; rises with energy). C (m05/m07/m19).

**Imaging: CT, MRI, PET, US (62–92)**
62. DRR quality improves with thinner slices. C (m10/m13).
63. Pointers to the author's CT/MRI/PET/US handouts. n/a.
64. CT over-estimates prostate size (vs MRI). **M**.
65. HU depends on kV and filtration, not mAs. C (m11).
66–67. HU linear with μ, not with electron density. C (m11/m17).
68. CT matrix 512², newer 1024². C (m27).
69. CT-on-rails: in-room CT, not part of the linac, couch transfers. C (m18).
70–71. MRI: no dose, best soft tissue; distortion at the periphery, slow, worse spatial resolution, poor bone, proton density not electron density. C (m10/m17).
72. MRI avoided in the first 12 weeks of pregnancy. **M**.
73–75. T1 = anatomy; T2 = disease burden; FLAIR = T2 with fluid nulled, good for CTV. C (m10).
76–78. Brain mets: CE-T1 and FLAIR; prostate mpMRI (T2, DWI, DCE, spectroscopy); uterus on T2. P (m10 names CE-T1/T2; mpMRI components and uterus-T2 not stated).
79–80. Contrast set by TR/TE; T1 short/short, T2 long/long, PD long/short. C (m10).
81. MRI matrix 256², newer 512². **M**.
82. Higher field strength → more distortion. **M**.
83. Appearance table (CSF dark on T1, bright on T2, dark on FLAIR; fat bright on T1; edema bright on T2/FLAIR). P (m10 has CSF/fat lines, not the full grid).
84. Even–even nuclei give no MR signal (no net spin). P (m10: hydrogen spin).
85–88. PET: 10–15 mCi FDG, 15 mCi = 555 MBq, 511 keV, patient dose on the order of 1–4 cGy. P (511 keV C; activity/dose numbers M).
89–92. Ultrasound: 1–20 MHz, piezoelectric, reflections at large impedance steps (tissue–air, tissue–bone), good conductors blood/muscle/water/fat. P (m10 has frequency and impedance in one line).

**Simulation, motion, IGRT, registration (93–112)**
93. Separation methods: CT, conventional sim, lead wire, calipers, pantograph. **M** for the manual methods (bank is CT-only).
94. Set-up pointers: SAD vs SSD, mark iso at sim, rigid immobilization, no pads, level the patient, supine vs prone. P (m14 covers immobilization; "no pads/level" not said).
95–96. TG-76; manage motion when excursion > 5 mm. C (m15/m16).
97–98. Time as the 4th dimension; ITV = CTV + internal margin. C (m15/m19).
99. Prospective (one phase) vs retrospective (all phases) 4DCT. P (named in m41/m44 only).
100. Gating: smaller target volume, longer treatment. C (m15).
101. Tracking systems: CyberKnife floor tubes/ceiling panels, EM beacons, fluoroscopy, ExacTrac, MR. P (m15 lists them; CyberKnife geometry detail absent).
102–103. Prostate base superior, apex inferior; urethrogram marks the apex. P (m22 anatomy; urethrogram M).
104. Localization aids: contrast CT, Gd-T1 MRI, PET/CT fusion. C.
105–108. Segmentation vs registration; rigid = 3 translations + rotations, deformable adds stretch/shrink. C (m17).
109. Pointer. n/a.
110. EPID (a-Si), kV planar, kV CBCT, MV CBCT. C (m18/m41).
111–112. CBCT full-fan vs half-fan (larger FOV), bow-tie filter. C (m22/m18).

**Electrons (113–129)**
113–114. Cutout output depends on energy, cone, cutout size and shape; cutout should be at least ≈ E/2 cm wide. C / P (rule of thumb not stated as E/2 cm).
115. Electron–electron matching: angle apart or shift the junction; electron–photon: hot spot on the photon side. C (m19/m25).
116. Lead on skin: hot spot just inside the shield edge, teardrop shape. C (m19/m24).
117. Virtual/effective SSD < 100 cm; worst at low energy and small fields. P (m19 one line).
118. Electrons vs superficial x-rays: surface dose 100% vs 75–93%, electrons have a finite range, superficial gives more bone dose. P (m07).
119–120. R50 specifies the beam; E₀ = 2.4 × R50 (older 2.33). C (m09/m24).
121–122. Energy rules; what energy with/without bolus. C (m19/m45).
123. Small cutout: dmax shallower, Rp unchanged. C (m19).
124. Rp ≈ E/2. C.
125. Proton RBE 1.1, rises at the distal edge. C.
126. Electrons lose ≈ 2 MeV/cm; LET rises at track end. C.
127. Cutout < 4 cm → no lateral equilibrium → measure. P (m42 measure-small-cutouts; 4 cm / E/2 thresholds absent).
128. Electron hot spots: photon side of a match, beside skin lead, along the ethmoid air interface, bolus shifts dmax, obliquity adds side scatter. P (first two C; ethmoid air-interface in m20 only).
129. Lead: E/2 mm; electron arcs E/2 + 1 mm. C / **M** (arc rule).

**Protons (130–134)**
130. Robust optimization: CTV, no PTV; range + set-up uncertainty. C (m19/m25).
131. Photons use HU→electron density; protons HU→relative stopping power; range uncertainty 2.5–4%. C (m19).
132. Robust optimization is not a dose algorithm; PB/CS/MC exist for protons. P.
133. Passive scattering (apertures, compensators, more neutrons) vs pencil-beam scanning (fewer neutrons, IMPT, magnets). C (m19).
134. Proton surface dose slightly higher than photons. C (m07).

**Beam metrics, DVH, statistics (135–143)**
135–137. PDD, profiles, penumbra; geometric penumbra formula; penumbra defined 90–20 (older 80–20). C (both widths appear in the bank).
138–140. CI, R50 (gradient), D2cm, V20, HI (> 1 = less homogeneous). C (m19/m24).
141. Mean, median, mode. **M** (not defined).
142–143. Cumulative vs differential DVH; neither shows hot-spot location. C (m19).

**Radiobiology (144–152)**
144–147. Survival curve: D₀ (37%), Dq (shoulder width), shoulder = repair, LQ. C (m21).
148. EQD2 formula. C.
149–150. Conceptus: most sensitive overall in the first ~12 days (all-or-none), malformations 3–12 weeks. **M** (m41 has fetal dose limits, not the windows).
151–152. OER definition and a 12 Gy / OER 4 → 3 Gy example. C (m21).

**IMRT / VMAT / special procedures (153–167)**
153–156. Modulate = change; IMRT modulates MLC; VMAT also gantry speed and dose rate; step-and-shoot vs sliding window. C (m23).
157. Optimizers: gradient search, simulated annealing, direct aperture optimization. **M** (m25 has cost function; algorithms not named).
158–160. Cost function (penalty vs iterations), minimize penalty, leaf sequencer turns fluence into segments. C (m23/m25).
161. VMAT vs IMRT: more conformal, hotter hot spot, more integral dose (the second two are debatable). P (m23 states conformity and low-dose bath).
162. TBI: hot spot < 110%, ±10% uniformity, ion-chamber commissioning, TLD in vivo. P (m24 lists in-vivo dosimetry; the two numbers absent).
163. TSET: extended distance, beams 20° above/below horizontal, CAX above head/below knees, x-ray dose highest on CAX, 6-field Stanford, shield eyes and nails. P (m24 has Stanford six positions; the angle/CAX reasoning and nail shields absent).
164. SRS/SBRT: grid ≤ 2 mm (TG-101), IGRT ≤ 1 mm (TG-142). C (m33/m39/m42).
165. More beams → more conformity, hotter hot spot (accepted), coverage first. **M** as a stated trade-off.
166–167. SRS normalization 50–90% to spare OARs. P (m24 Gamma Knife 50% line).

**Informatics, automation, errors, set-up (168–182)**
168–170. DICOM expansion; DICOM-RT objects (image, structure, plan, dose). C (m26).
171. IT glossary: bit, byte, pixel, voxel, RAM, ROM, LAN/MAN/WAN, MIPS. P (pixel/voxel C; RAM/ROM/LAN/WAN/MIPS M).
172. Adaptive RT pointer. n/a (m28 exists).
173–174. Auto-contouring and auto-planning: quality up, variation down, throughput up, cost down. C (m29/m30).
175–178. Normal distribution; ±1 SD 68%, ±2 SD 95%, ±3 SD 99.7% (list says 99%); variance plots. P (m35 one mention).
179–180. Random (fraction-to-fraction, bladder) vs systematic (all fractions: delineation, wrong iso, calibration). C (m17/m18/m32).
181. Fiducials: at least 3, 4 better, may migrate. C (m18/m31/m32).
182. Pitch/roll/yaw axes — the list assigns pitch to the sup-inf axis and roll to the left-right axis, which is **swapped** relative to the usual convention (roll = about the long axis, pitch = about the lateral axis, yaw = about the vertical). Bank m23/m32 use the standard convention. Mark C for the bank; flag the source.

**Dose calculation and algorithms (183–196)**
183–184. Dose = J/kg; dose uses μ_en/ρ. C (m09).
185–189. Slower = more accurate; Monte Carlo tracks histories from random numbers; convolution = TERMA ⊗ kernel; tier table MC / superposition-CC-Acuros / pencil beam / hand calc. P (m33/m37 cover MC and PB; TERMA-kernel wording and the four-tier table absent).
190. Pencil beam not for IMRT or small lung lesions (over-predicts periphery). C (m33/m37).
191. Dynamic wedge: jaw sweep, toe/heel dwell, field-size-dependent WF, less peripheral scatter, more MU than open, any angle, limits (min field, min MU, orientation vs MLC). P (m34 has the basics).
192. Wedge angle = 90 − hinge/2. C (m34).
193. Tangents pointer. n/a.
194–196. Uncertainty adds in quadrature (1,2,3% → 3.7%); 5% overall goal; component table. C (m39/m25).

**Brachytherapy and radiation safety (197–215)**
197. Radium loading patterns: uniform, club, dumbbell. **M**.
198–199. HDR / applicator pointers. n/a.
200. HDR: ~10 Ci single source, outpatient, less staff dose, two independent security measures, interlock so HDR and x-ray cannot both run. P (10 Ci and single source C; security/interlock details M).
201. HDR QA: commissioning scope; daily interlocks/area monitor/source position; quarterly calibration/timer/positioning/applicators. C (m40/m42).
202. LDR QA: commissioning, source receipt, per-patient. P.
203. Two patient identifiers. **M**.
204. Surveys before and after any implant. C (m40).
205. LDR safety: ALARA; time/distance/shielding; forceps; lead pigs; quarterly inventory; semi-annual leak test with a well/NaI counter; threshold given as "< 0.05 µCi". C for the practices; the threshold in the source is **off by 10×** — the regulatory limit is 0.005 µCi (185 Bq), which is what m40 teaches.
206. Exposure limits pointer. n/a (m41).
207. Protection standards rest on LNT. C (m41).
208–210. Stochastic (probability, no threshold, cancer) vs deterministic (severity, threshold, erythema/cataract/blood). C (m41).
211. Declared pregnancy: not pregnant until declared; two badges; monthly reading; may un-declare. C (m41/m44).
212–214. NRC regulates byproduct material, not x-rays; agreement vs non-agreement states. C (m40/m41).
215. Facility program: ALARA, RSC meets quarterly, RSO. C (m40/m42).

**Machine QA, detectors, imaging QA (216–237)**
216–217. TG-40 old, TG-142 current. C (m42).
218. Tongue-and-groove under-dose; keep leaves together; TPS models it poorly. C (m23/m34).
219. Picket fence: weekly per TG-142; visual plus software. P (m42 names picket fence; cadence absent).
220. Winston–Lutz: SRS; mechanical vs radiation iso. C.
221. Star shot for collimator/gantry/couch rotation about iso, film. **M**.
222–224. AAMD scope of practice, practice standards, MDCB handbook links. C (m42/m30 and official/).
225. Good chamber: high collection efficiency, no energy/polarity/recombination/stem/leakage dependence. P (m09 mentions polarity and stem).
226. Parallel-plate for low-energy electrons (6 MeV), point detector. C (m09).
227. GM: sensitive, energy-dependent, long dead time, paralysis. C (m23/m09).
228. Diodes: small, instant, no bias; energy/temperature/angle dependence, damage over time. C (m09/m42).
229. Radiochromic film: no processing, best resolution, low energy dependence, light-insensitive, 10 min relative / 24 h absolute. P (named in m09/m42; properties list absent).
230. TLD: LiF, glow-curve 5th peak, read next day, environment-sensitive. P (m09 "integrating, read later").
231. OSL: more sensitive and stable than TLD, read after ~1 h. P.
232. Delivery limits: collisions, jaw/MLC travel, extended SSD outside TPS validity, long beam-on vs motion. C (m23/m42/m15).
233–235. Imaging-QA test families; TG-66 CT-sim: daily water 0 ± 5 HU, monthly 4–5 materials, annual electron-density phantom, spatial integrity 1 mm, uniformity monthly, contrast/resolution annual. C (m42; m10/m11 for the 5 HU line).
236. IGRT QA pointer to TG-142. C.
237. Density overrides: dental and hip artifacts, rectal contrast, wire markers. C (m11/m13/m37/m39).

Potholes tally (237 numbered items, 9 are pointers): **C 128 · P 56 · M 44** → 56% of the warnings already appear in theory or a Why; 80% at least partially. Source errors found: leak-test threshold 0.05 µCi (should be 0.005), pitch/roll axes swapped, "fat has higher electron density than muscle" stated without the per-gram qualifier, ±3 SD given as 99% (99.7%), photodisintegration filed under decay modes.

---

## 4. QUANTEC sheet vs `theory/m43`

The sheet is a department template: the 2 Gy/fx column holds the constraints; the other seven columns are LQ-rescaled versions for 1.5–5 Gy/fx (the bank has EQD2 in m21/m25 and does not need such a table). Green rows are labelled as QUANTEC on the sheet; white rows are the department's own (RTOG-era) numbers. Comparison of the 2 Gy/fx column, row by row:

| Site / structure | Sheet (2 Gy/fx) | m43 | Verdict |
|---|---|---|---|
| Optic chiasm/nerves | Dmax 54 (dept) · **55 (QUANTEC)** | < 55 Gy | agrees |
| Inner ears | Dmax 40 (dept) | no row (cochlea mean 45 only) | dept-only; optional |
| Brainstem | Dmax 54 | whole organ < 54 | agrees |
| Eyes (globe/retina) | Dmax 20 (dept) | no row | **missing** (not a QUANTEC row; RTOG H&N templates use 45–50 for retina, so the sheet's 20 Gy looks like a local choice) |
| Lens | Dmax 3 (dept) | no row | **missing**; note the same instructor's "Reminders" says lens tolerance 5 Gy and threshold ~1 Gy. Worth one line in m43: lens is Emami/local, 3–10 Gy depending on source, not QUANTEC |
| Whole brain | Dmax 60 | Dmax < 60 | agrees |
| Cochlea | **mean < 45 (QUANTEC)** | mean ≤ 45 | agrees |
| Spinal cord | Dmax 45 (dept) · **50 (QUANTEC)** · cord + 5 mm PRV 50 | Dmax 50 | agrees; **PRV (cord + 5 mm, "always"; 7–10 mm when feasible) concept missing** from m43 |
| Parotid unilateral | mean < 26 and V30 < 50% (dept) · **mean < 20 (QUANTEC)** | spare one gland to mean < 20 | agrees |
| Parotid bilateral | **mean < 25 (QUANTEC)** | mean < 25 | agrees |
| Mandible | V60 < 15%, V70 < 1%, Dmax 75 (dept) | no row | **missing** (RTOG-style; common exam item "mandible Dmax 70") |
| Larynx | V50 < 33% (dept) · **V50 < 27%, Dmax 66, mean < 44 (QUANTEC)** | mean < 44 or V50 < 27%; Dmax < 66 | agrees |
| Pharyngeal constrictors | **mean < 50 (QUANTEC)** | the "mean < 50 for aspiration" line is filed under larynx | **partial**: QUANTEC has both a larynx mean < 50 (aspiration) and a constrictor mean < 50 (dysphagia/aspiration) row; add the constrictor row |
| Lungs (bilateral) | mean < 20, V5 < 50%, V10 < 45%, V20 < 35% (dept) · **V20 < 30% (QUANTEC)** | V20 ≤ 30% and mean 20 | agrees; V5/V10 are dept extras |
| Esophagus | mean < 35, V55 < 30% (dept) · **mean < 34, V35 < 50%, V50 < 40%, V70 < 20% (QUANTEC)** | same four QUANTEC numbers | agrees |
| Heart | V30 < 50% (dept) | V30 < 46% (pericardium) and V25 < 10% | dept row is looser; no change |
| Pericardium | **mean < 26, V30 < 46% (QUANTEC)** | same | agrees |
| Brachial plexus | Dmax 60 (dept) | TG-101 stereotactic cells only | **missing** a conventional-fractionation plexus line (60–66 Gy, RTOG) |
| Breast: ipsilateral lung | "V5 < 25%" and V20 < 10% as printed | no breast-specific rows | the printed V5 < 25% is implausible for tangents (RTOG 1005 uses V20 < 15%, V10 < 35%, V5 < 50%); likely a transcription slip on the sheet. **Breast/chest-wall template rows are missing** in m43 (lung V20 ~15–25%, heart V25 < 5–10%, mean heart < 4–5 Gy) |
| Breast: heart | V25 < 5% (breast), V25 < 9% (chest wall) | V25 < 10% cardiac-mortality line | close |
| Chest wall: ipsilateral lung | V20 < 25% | no row | missing as above |
| Abdomen: liver | mean < 28, V30 < 70% (dept) | mean < 30–32 (QUANTEC) | agrees in spirit; dept stricter |
| Kidney unilateral | V20 < 75% (dept) | no unilateral row | optional |
| Kidneys bilateral | **mean < 15, V12 < 55%, V20 < 32%, V23 < 30%, V28 < 20% (QUANTEC)** | mean < 15–18, V12 < 55% | **partial**: add V20 < 32%, V23 < 30%, V28 < 20% |
| Stomach | V45 < 50% (dept) · **D100 < 45 (QUANTEC)** | D100 < 45 | agrees |
| Duodenum | V45 < 30% (dept) | "QUANTEC gives no duodenum row" | consistent (dept-only) |
| Small bowel | V45 < 75% (dept) · **V15 < 120 cc (QUANTEC)** | V15 < 120 cc loops; V45 < 195 cc bag | agrees |
| Large bowel | V45 < 50% (dept) | no row | dept-only |
| Prostate: rectum | V45 < 50%, V70 < 15% (dept) · **V50 < 50, V60 < 35, V65 < 25, V70 < 20, V75 < 15 (QUANTEC)** | same five | agrees |
| Bladder | V45 < 50%, V70 < 15% (dept) · **V65 < 50, V70 < 35, V75 < 25, V80 < 15 (QUANTEC)** | same four | agrees |
| Small bowel / large bowel (pelvis) | V50 < 5%, V60 < 5% (dept) | — | dept-only |
| Femoral heads | V50 < 5% | no row | **missing** (RTOG 0126 style femoral head V50 < 5% / Dmax 50 is a frequent exam item) |
| Pubic bone | V70 < 25% | no row | dept-only |
| Penile bulb | **mean dose to 95% of the bulb < 50 (QUANTEC)** | same wording | agrees |
| PTV rows | ≥ 95% at Rx for PTV60/46/70/66/50/50.4/75.6 | — | n/a |

Result: **0 value conflicts** between the sheet's QUANTEC (green) rows and m43. **Missing in m43**: cord PRV concept, pharyngeal constrictors, kidney V20/V23/V28, mandible, conventional brachial plexus, femoral heads, lens/eye, breast/chest-wall lung-and-heart template rows (8 gaps, all RTOG/department-style rather than QUANTEC proper; the first three are QUANTEC-adjacent and should be added).

---

## 5. Isotope sheet vs `theory/m03` and `theory/m40`

| Nuclide | Sheet: T½ · E (MeV) · Γ (R cm²/mCi h) · HVL Pb (mm) | Bank (m03/m40) | Discrepancy / gap |
|---|---|---|---|
| Ra-226 | 1604 y · 0.830 · 8.25 (per mg) · 8 | 1600 y · "gammas from daughters" · 8.25 per mg · no HVL | add mean energy ≈ 0.83 MeV and HVL ≈ 8 mm (teaching values) |
| Cs-137 | 30.0 y · 0.662 · 3.28 · 5.5 | 30 y · 0.662 · 3.26 · **6.5** | Γ 3.28 vs 3.26 (both appear in texts; 3.26 is Khan). **HVL 5.5 vs 6.5 mm**: Khan's table gives 5.5; the bank's 6.5 should be re-checked and probably changed to "about 5.5–6.5" |
| Co-60 | 5.26 y · 1.17/1.33 · 13.07 · 11 | 5.26 y · same · 13.07 (13.1) · **12** | HVL 11 vs 12 mm, both are common teaching values; harmonize to "about 11–12" |
| Au-198 | 2.7 d · 0.412 · 2.38 · 2.5 | 2.7 d · 0.412 · none · none | add Γ 2.38 and HVL 2.5 mm (low priority, historical) |
| Ir-192 | 74.0 d · 0.380 · **4.66** · **2.5** | 73.8 d · ~0.38 · **4.69** · "3–6 mm" | Γ 4.66 vs 4.69 (Khan 4.69; keep 4.69, note 4.66 exists). HVL: the sheet's 2.5 mm is Khan's narrow-beam value; the bank's "3–6" should say "about 2.5–3 mm narrow beam, up to ~6 mm broad beam" |
| I-125 | 60.2 d · 0.028 · 1.46 · 0.025 | 59.4 d · ~28 keV · "use the stem" · 0.025 | agrees; bank deliberately memorizes no Γ for I-125 (fine, DoseGrid uses other values) |
| Pd-103 | 17.0 d · 0.021 · 1.48 · 0.008 | 17 d · ~21 keV · none · none | add HVL ≈ 0.008 mm (completes the seed pair) |

Sheet rows missing from the bank: none. Bank nuclides absent from the sheet (I-131, P-32, Sr/Y-90, Tc-99m, F-18, Cs-131, Ru-106) are a superset, which is fine. Real discrepancies: **2** (Cs-137 HVL, Ir-192 HVL wording); minor Γ rounding: 2.

---

## 6. Reminders and Study Tips

**Reminders for the final exam.** Fourteen one-line "what changed" notes from the course instructor, mostly useful as a tie-breaker list for items where old and new numbers both circulate: penumbra defined 90–20 rather than 80–20; MLC tolerance intra-leaf 1% / inter-leaf 2–3%; electron d90 = E/3.2 and d80 = E/2.8 (not E/4 and E/3); E₀ = 2.4 R50 (not 2.33); IMRT beam separation 10–15°; pacemaker threshold moving from 2 Gy to a 5 Gy high-risk tier and "any neutron-producing beam" (TG-203); electron eye shields only for 6 and 9 MeV; CT spatial accuracy 0.5 mm (MRI 1 mm); iterative reconstruction replacing filtered back-projection; constraints from RTOG/QUANTEC rather than Emami; swipe-test action level 2200 dpm; lung V20 history (37% → 20–30%, SBRT V20 < 10%); cord "49–50 Gy" rather than 45; lens threshold ~1 Gy with 5 Gy tolerance. The bank already carries the new value for penumbra, pacemaker tiers, QUANTEC-over-Emami, cord 50 Gy, R50 and the electron rules (as "author-dependent" in m45). Gaps worth a line each: the MLC 1%/2–3% tolerances, the 0.5 mm CT spatial-accuracy figure, iterative reconstruction, the 2200 dpm swipe level, eye-shield energies, and a lens entry. Two cautions: the "old vs new" framing is this instructor's opinion, not an MDCB statement, and the electron rule it endorses (E/3.2) contradicts the DoseGrid rationale (E/2.8 for 90%) in the same folder — the bank's "state which author's rule you are using" approach in m45 is the safer position.

**Study Tips.** Two lines: study more, and remember borated polyethylene (for neutron shielding). The second is already in m05/m41. No further content; not a source.

---

## 7. Summary

- **Items reviewed:** DoseGrid 155 unique MCQ (30 calc, 6 image-ID; keys visible for ~90) + RAPHEX 2023 therapy 140 MCQ (all keyed) = **295 question items**; plus 237 Potholes pitfalls, ~70 constraint rows, 7 isotope rows, 14 reminders.
- **Coverage of question items:** DoseGrid 110 C / 19 P / 26 M (71% covered); RAPHEX 107 C / 14 P / 19 M (76%); combined **217/295 = 74% covered, 85% covered-or-partial**. Potholes: 128 C / 56 P / 44 M (56% fully warned about, 80% at least partially). QUANTEC sheet: 0 conflicts, 8 absent rows. Isotope sheet: 2 real discrepancies (Cs-137 HVL 5.5 vs 6.5 mm; Ir-192 HVL "3–6" vs 2.5 mm narrow-beam), 2 Γ rounding differences.
- **Wrong keys:** DoseGrid **1 wrong** (heterogeneity-off on a lung path keyed "underdose"; bank m37 already has the correct direction), 4 questionable (90%-depth rule E/2.8 → 12 MeV; I-125 "35 keV"; "HDR with I-125"; "long mitotic cycle"), 2 ambiguous stems. RAPHEX **0 wrong**, 2 loose rationales, 1 unverifiable (T117). Potholes source errors: leak-test 0.05 µCi (should be 0.005), pitch/roll swapped, fat-vs-muscle electron-density claim, ±3 SD = 99%.
- **MISSING facts and calc types worth adding, by module:**
  - m03/m40: I-125 "35 keV max vs ~28 keV mean" note; active vs physical length of a source; Manchester/Paterson–Parker non-uniform loading vs Quimby/Paris uniform; radium loading patterns (uniform/club/dumbbell); lower seed strength → more seeds; I-125 anisotropy stronger than Ir-192 (capsule absorption); transport index (mrem/h at 1 m); NRC HDR source-position tolerance ±1 mm; TG-59 roles (physician removes applicator); Γ/HVL for Ra-226, Au-198, Pd-103; fix Cs-137 HVL (5.5) and Ir-192 HVL wording.
  - m07/m23/m24: SRS cones lengthen SDD → smaller penumbra; FFF has higher surface dose and ~3% lower PDD₁₀; TBI 15 MV AP/PA is the most homogeneous arrangement; TBI dose-rate band (5–10 cGy/min) and hot-spot < 110%; TSET x-ray contamination peaks on the CAX (why beams are angled); linac 3 GHz ↔ 10 cm; which knobs set energy vs dose rate.
  - m09/m42: thimble-wall property list; T–P factor > 1 when P < 760 and T > 22; star shot; picket fence weekly; chamber "good properties" list; radiochromic/TLD/OSL property lines; MLC tolerance 1%/2–3%; CT spatial accuracy 0.5 mm; iterative reconstruction; swipe 2200 dpm.
  - m11/m13/m16: CT over-estimates prostate size; calcification stays, artifact/wire/contrast get overridden; manual contour methods (lead wire, pantograph, calipers); fat-vs-muscle electron density per gram vs per cm³; MRI first-trimester caution; field strength ↔ distortion.
  - m19/m25/m36: **CSI collimator/couch angle calc** (collimator from spine length, couch from cranial length) and spine fields meeting anterior to the cord; renormalization 100% → 90% hot-spot arithmetic; TMR ≈ 2.5%/cm error estimate for a wrong depth; algorithm ranking including equivalent-TAR; electron arc lead E/2 + 1 mm; optimizer names (gradient, simulated annealing, DAO); "more beams → conformity up, hot spot up" trade-off; IGRT (not IMRT/4DCT) is what shrinks ITV→PTV.
  - m20/m22: pylorus, prostate adenocarcinoma, hockey-stick seminoma field, base-of-tongue organ preservation, skin cancer as most common US cancer, colorectal → liver, esophagus survival, mid-course machine/energy change → replan, and the six cross-sectional anatomy images (sinuses, ventricles, thalamus/hippocampus) — the audit already flagged image items as the biggest anatomy gap.
  - m21/m41: Bergonié–Tribondeau wording (undifferentiated, mitotically active, long mitotic future); LD50/60 ≈ 3.5–4 Gy; acute radiation syndromes (hematopoietic 2–3 Gy/months, GI 5–12 Gy/~1 week, CNS > 12 Gy/~1 day); conceptus sensitivity windows; 1 Bq = 2.7 × 10⁻¹¹ Ci; 1 eV = 1.6 × 10⁻¹⁹ J; units of μ and μ/ρ; mean/median/mode; ±1/2/3 SD.
  - m26/m27/m29: ROM/RAM/LAN/WAN/MIPS glossary; machine learning definition; DCA vs VMAT; over-modulation ↔ PSQA pass rate; EPID vs array trade-offs.
  - m43: **QUANTEC cord 13 Gy single fraction / 20 Gy in 3** (currently only TG-101 14 Gy); cord PRV + 5 mm; pharyngeal constrictors mean < 50; kidney V20 < 32% / V23 < 30% / V28 < 20%; mandible (V70 < 1%, Dmax 75); conventional brachial plexus 60–66; femoral heads V50 < 5%; lens (3–10 Gy, source-dependent) and eye rows; breast/chest-wall lung V20 and heart V25/mean rows; compact-bone density note (1.6–1.85 range across sources).
- **Verdict: complementary.** The DoseGrid exam is a reasonable 155-item dress rehearsal in the right format but is shallower than the bank on planning, calc variety, and constraints, and it carries one wrong key and one wrong electron rule; its main value is 26 missing recall facts (mostly oncology/anatomy one-liners and the QUANTEC 13 Gy cord line) and the CSI-angle calc type. RAPHEX is above the dosimetrist level on about a sixth of its items but is cleanly keyed and gives 13 worth-adding facts (CSI geometry, FFF surface/PDD, TBI arrangement, brachy systems and NRC/TG-59 specifics). Potholes is a useful checklist whose warnings the bank already states for 80% of items, with four source errors to avoid copying. The QUANTEC sheet confirms every m43 QUANTEC value and points at the RTOG-style rows m43 lacks; the isotope sheet is consistent apart from the Cs-137 and Ir-192 lead-HVL numbers, which should be corrected in m03.
