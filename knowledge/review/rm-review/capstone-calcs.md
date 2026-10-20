# RM Review: Capstone calc sets and practice tests vs. our bank

Source: `inbox/RM Review/` (third-party, copyrighted, gitignored). Text copies in `inbox/text/`.
All numbers below are paraphrased re-statements of problem *types*; no stems are copied.
Coverage marks are against `knowledge/questions/m33*, m35*, m36*, m37*, m40*, m41*` (calc types) and the whole bank (facts), by grep plus a read of every stem in the six calc modules.

Files reviewed (all read in full):

| # | File | Items | Keys? | Style | Domain split (approx.) |
|---|------|-------|-------|-------|------------------------|
| 1 | `CAPSTONE_XXX 2.docx` | ~540 Q→A lines, ~430 unique (many items repeated 2–3×) | Inline one-line answers; a few flagged "?" / "emailed Brent" by the author | Master study sheet grouped by topic (proton, tolerances, SRS, clinical, CT, MRI, isotopes/PET, anatomy, brachy, QA/physics, planning, calcs, units, particles, linac, misc, "still need answered") | ~16% calc (≈75 lines, ≈60 unique), ~84% recall facts; ~45 image-ID items (anatomy, devices, DVHs, PDDs) that have no text |
| 2 | `Capstone Calcs June 2024 with Key.docx` | ~65 worked items | Yes, with formula/steps for most | Calc workbook: prompt → answer → method | ~90% calc; ~10% pre-algebra warm-ups (log, midpoint, slope, Pythagoras, binary) |
| 3 | `Practice Test 1 (Spring 2023).pdf` (Quizlet export) | ~120 MCQ | Yes (answer repeated after options) | 4–5 option MCQ, same pool as file 1 | ~12% calc (≈14), rest facts |
| 4 | `Practice test 2 (2023).pdf` (Quizlet) | ~125 MCQ | Yes | Same pool; several items appear twice with different keys | ~20% calc (≈25), rest facts |
| 5 | `Practice Test 3.pdf` (internally titled "Capstone Practice Test 4", Quizlet) | ~85 MCQ | Yes | a–d MCQ; densities, definitions, TNM, isotopes; matching items | ~5% calc (3 items), ~95% facts |
| 6 | `Practice Test 6.pdf` (Quizlet) | ~95 MCQ | Yes | a–d MCQ, ~20 image-ID items | ~15% calc (≈14), rest facts |
| 7 | `Practice Test 8.docx` | 97 numbered MCQ | **No key** (options only) | 4-option MCQ, ~15 image items | ~10% calc (≈10), rest facts |
| 8 | `MDCB Pract Calcs.pdf` | 68 calc MCQ (one per page) | Yes, answer printed above each stem + OCR-garbled handwritten work | Retired-style MDCB calc questions with tables/diagrams (several diagrams missing in text) | 100% calc |

Overlap: files 3–7 are drawn almost entirely from file 1's pool (same wording, same distractors). File 2 and file 8 are mostly independent of file 1. Unique item estimate across all eight files: **≈590** (≈430 from the master sheet + ≈60 June-2024 calcs + ≈68 MDCB calcs + ≈30 practice-test-only items). Unique calc items: **≈175**, falling into the ≈70 calc types inventoried below.

Key-quality note: the practice tests contradict each other on several items (same stem, different key in PT1 vs PT2 vs master sheet). The master sheet itself carries two different keys for the same problem in two places (gap 0.75 vs 0.70; 0.69 vs 2.8 mR/h). See "Wrong keys" at the end.

---

## 1. Calculation-type inventory

Legend: **C** = COVERED in our bank, **P** = PARTIAL (mechanics present, this variant/twist absent), **M** = MISSING. "Key" column = result of my recomputation (✓ agrees; ✗ disagrees; ~ approximate/convention-dependent; – no key or unverifiable).

### 1a. Photon MU and dose calcs (→ m35)

| # | Calc type | Worked example (paraphrased numbers) | Key | Ours |
|---|-----------|-------------------------------------|-----|------|
| 1 | Isocentric MU, opposed pair with weighting and plan normalization (TMR·Sc·Sp·norm) | 3000 cGy/12 fx, PA 75 %, TMR 0.788, Sc 1.006, Sp 1.004, WF 0.776, norm 115.4 % → 263 MU | ✓ 263 | C |
| 2 | Same, AP/PA total MU, two different TMRs | 4800/20, TMR 0.925/0.8355, Sc 1.03, Sp 1.02, norm 98.5 % → 264 MU (no key given; options include 264) | – (264) | C |
| 3 | Same, 10 MV hip and whole-brain variants | 2700/9, TMR 0.9365/0.899 → 322 MU; 3000/10, TMR 0.876, Sc 1.026, Sp 1.019 → 166 MU/field | – (322, 166) | C |
| 4 | Single small PA boost field MU | 532/28 = 19 cGy, TMR 0.863, Sc 0.985, Sp 0.988, norm 109 % → 21 MU | ✓ | C |
| 5 | AP MU where key applied norm inconsistently | 3200/10, AP 35 %, TMR 0.844, Sc 1.018, Sp 1.0115, norm 96.7 % → key 125 | ✗ (133 dividing by norm, as the same file does elsewhere) | C |
| 6 | SSD MU with PDD and normalization | 200 cGy, d10 PDD 67 %, norm 85 % → 351 MU; 100 cGy, no norm → 149 | ✓ | C |
| 7 | SAD setup with SSD calibration (ISL_cal = ((100+dmax)/100)²) and the reverse | 18X, 150 cGy/field, TMR 0.912, Scp 1.029, norm 95 % → 157 MU | ✓ | C (m35 has SAD 80 / cal 100 and SSD 125 items) |
| 8 | Given dose (dmax dose) from PDD | 60 cGy at 11 cm, PDD 67.1 → 89 cGy; 150 cGy at 65 % → 231 | ✓ | C |
| 9 | Dose to a second depth along a single SSD beam (cord dose via PDD ratio) | 90 cGy at 12 cm (64.1 %) → cord at 6 cm (82.1 %) = 115 cGy | ✓ | C |
| 10 | Cord dose on an isocentric beam: TMR ratio × ISL | 40 Gy at 8 cm iso, cord at 5 cm depth (97 cm from source), TMR 0.939/0.861 → 46.3 Gy | ✓ | C (m33 "calculation point 112 cm" item) |
| 11 | Dose at a second point, same depth, via TMR ratio (SSD change ignored) | 200 cGy × 0.975/0.895 → 218 | ✓ | C |
| 12 | Parallel-opposed: dose at dmax (entrance + exit) from TMR/PDD | 30 cm sep, 100 cGy/field at mid, TMR 0.72/0.525, dmax 2 → 241 cGy; 4 MV 80 SSD POP from PDD table → 64.7 Gy | ✓ | C |
| 13 | Re-prescribing to a lower isodose: new hot spot / isocenter dose | 107 % hot spot, Rx 1.8 × 25 to 95 % → 5068 cGy; 125 cGy to 105 % line → 119 cGy to 100 % | ✓ | C (m25) |
| 14 | Weighted 1 : 0.5 : 0.5 fields, Rx to 95 % → daily iso doses | 180 cGy to 95 % → 95 : 47 : 47 | ✓ | P (renormalization covered; weight splitting not) |
| 15 | Multi-field dmax per beam from weights and 95 % Rx | 180/0.95 × 0.10 → 19 cGy | ✓ | P |
| 16 | Wedge left out of the beam: % dose increase (1/WF − 1) | WF 0.65 → +54 %; WF 0.55 → +82 %; WF 0.528 attenuates 47.2 % | ✓ | C |
| 17 | Wedge omitted for part of the course: average delivered % | WF 0.8 omitted 5 of 10 fx → 112.5 % | ✓ | P (single-fraction omission covered; course averaging not) |
| 18 | Wedge factor left out of the MU calc but wedge used (under-dose) | 180 cGy/day AP/PA, WF 0.617 on AP, 4 days → 582 cGy | ✓ | C |
| 19 | One field of a weighted pair treated without its wedge | 250 cGy, F1 0.7/WF 0.40, F2 0.3/WF 0.55, F2 wedge missed → 311 cGy | ✓ | C |
| 20 | Wedge factor from with/without readings | 0.442/0.625 → 0.707 | ✓ | C |
| 21 | Off-axis ratio from profile readings | 1.045/1.013 → 1.032 | ✓ | C |
| 22 | SMR from TMR − TMR₀ | 0.943 − 0.841 → 0.102 | ✓ | **M** |
| 23 | Interpolation in TMR/PDD tables | implicit in 10, 12 | – | C |
| 24 | Zero-area TMR from μ: e^(−μ(d − dmax)) | μ 0.05 cm⁻¹, dmax 1.5, d 12.5 → 0.577 | ✓ | **M** (m33 gives zero-area TAR, never derives it) |
| 25 | Extended-SSD MU (same dose, new SSD; ISL ± Mayneord) | 230 MU at 100 SSD → ≈330 at 120 SSD | ~ (326–331 depending on PDD update) | C |
| 26 | Treated at SSD when calc'd SAD (or vice-versa): dose/MU error | 20 cm pt, mid-plane: SSD needs +21 % MU; 5 fx at SSD instead of SAD, 7 cm → 13.1 Gy of 15; weekend SSD/SAD mix-up → 660 of 600 cGy | ✓ | **M** as a numeric error scenario (setup-conversion mechanics exist in m35; m42 is conceptual) |
| 27 | Wrong energy delivered: dose ratio from PDDs | 18 MV instead of 6 MV at 5 cm → ≈225 of 200 cGy | ~ (table-dependent) | P (conceptual only in m32/m42) |
| 28 | Dose under a thick block from transmission | 5.5 cm cerrobend, 4000 cGy open → ≈360 cGy | ~ (rule-of-thumb) | P (transmission math covered; block-thickness lookup not) |
| 29 | Skin dose with bolus from PDD table | 1 cm bolus, 3000 cGy to 80 % line, skin at 90 % → 3375 | ✓ | P |
| 30 | MU with a 110 cm SAD, tray/ISL/TMR interpolation | 150 cGy, TMR 0.820, Sc,p 1.030, (100/110)² → key 221 | – (I get 215 with the printed factors; table missing) | C |
| 31 | 1 MU = 1 cGy at reference | → 0.01 Gy | ✓ | C |

### 1b. Electron calcs (→ m35 / m25 / m19)

| # | Calc type | Example | Key | Ours |
|---|-----------|---------|-----|------|
| 32 | Electron MU with cone factor, cutout, virtual-SSD inverse square, % line | 200 cGy to 90 %, SSD 109, VSD 90, CF 1.004, cutout 1.021 → 261 MU | ✓ | C (m35 effective-SSD stand-off item) |
| 33 | Same with 3 Gy to 95 % | → 371 MU | ✗ in two files (364; 448), ✓ in PT2 | C |
| 34 | Electron MU with norm and plain (100/SSD)² | 12E, 300 cGy, CF 1.03, ROF 1.024, norm 90 %, SSD 103 → 335 | ✓ | C |
| 35 | Back-solve the normalization from given MU | 300 cGy, 352 MU, CF 1.03, ROF 1.024, SSD 102.5 → 85 % | ✓ | P |
| 36 | Cutout output from chamber readings ratio | 92.4/98.5 = 0.938; 200 cGy to 90 % → 237 MU | ✓ | C (m42/m44 cutout-factor items) |
| 37 | Energy choice: d90 ≈ E/3.2 with bolus added to depth | 3 cm + 1 cm bolus → ≥12.8 → 15 MeV; d90 5 cm → 16 MeV | ✓ | C (m25) |
| 38 | Energy choice with a structure to spare (R50 or E/2 cutoff) | nodes at 3 cm, cord at 5 cm → 9 MeV; target 0.5–2.5 cm + 0.8 bolus, avoid 4.5 cm → 12 MeV | ✓ | P |
| 39 | Rules of thumb: Rp = E/2, R50 = E/2.4 (Eo ≈ 2.33·R50), d80 = E/2.8, therapeutic = E/4, 2 MeV/cm loss | 15 MeV R50 6.25; 12 MeV d80 4.3; 16 MeV at 4 cm → 8 MeV | ✓ | C for E/2, E/3 (d80), E/4, 2 MeV/cm; **M** for R50 = E/2.4 |
| 40 | Lead thickness for electrons ≈ E/2 mm | 12 MeV → ~6 mm (key 5.6) | ✓ | C |

### 1c. Geometry, gaps, divergence, penumbra (→ m36 / m33 / m08)

| # | Calc type | Example | Key | Ours |
|---|-----------|---------|-----|------|
| 41 | Skin gap, two SSD fields, equal/unequal lengths and SSDs | 22.5 & 37.75 cm at 102/105 SSD, d 7.5 → 2.17; 15 & 18 at 100, d 5 → 0.825; 25 & 15 at 80 SSD, d 6 → 1.50 | ✓ | C |
| 42 | Gap when "collimator setting" is defined at 100 cm but SSD is 120 | 20×20 @100, 10×10 @120, d 5 → 0.75 (if 10 cm projects to 12) or 0.71 (if 10 cm is on skin) | ~ (both keys appear in the same file) | P (worth one item on the definition trap) |
| 43 | Gap for two isocentric (SAD) fields at the match depth | 8×31 & 8×35 SAD, d 6 → 1.98 | ✓ | C |
| 44 | Overlap/gap measured on the far (anterior) skin for SAD spine fields | 25 & 15 cm SAD 100, SSD 94, sep 23 → 3.4 cm | ✓ | P |
| 45 | CSI couch and collimator angles (arctan L/2 / distance) | spine 40 cm & brain 25 cm → 11.3° / 7.1°; spine 38 → 10.8°, brain 18 → 5.1°; spine 39 → 11° | ✓ | C |
| 46 | Opposed tangent gantry angle to align posterior borders | LAO 60°, 18 cm width → RPO 240 − 2·atan(9/100) ≈ 240 − 10° | ✓ | C |
| 47 | Hinge angle for a wedge pair | 30° wedges → 120° | ✓ | C |
| 48 | Field-size projection by distance (light field, film, source length, DRR) | 22 cm @100 → 24.2 @110; 15×15 @140 → 10.7 @100; 40 cm @100 → 200 cm @500 | ✓ | C |
| 49 | Radiographic magnification / true object size / block shift on the tray | 12 cm image, SOD 90, SFD 110 → 9.8; ring 3 → 3.75 → 1.25; 1.5 cm on film @140 → 0.75 cm at tray @70 | ✓ | C (m08) |
| 50 | Collimator setting for a large field at extended distance, with and without 45° collimator rotation (diagonal) | 121.9 cm at 4 m → 30.5 cm; rotated 45° → 21.5 cm | ✓ | **M** |
| 51 | Radius from CAX to the centre of an asymmetric open field | X1 7/X2 5, Y1 2/Y2 10 → √(1²+4²) = 4.1 cm | ✓ | **M** |
| 52 | Geometric penumbra | s 1.5, SSD 70, SDD 49.8, d 7.5 → 0.83 cm | ✓ | C |
| 53 | Equivalent square: 4A/P; circle ≈ 0.89·d; 30 % blocked 10×10 → √(0.7)·10 | 15×25 → 19; 8×40 → 13.3; Ø11 → 9.8; blocked → 8.4–8.5 | ✓ | C (rectangle, blocked); P (circle) |
| 54 | Right-triangle / trig / midpoint / distance / slope / log warm-ups | sin 30 = 4/x → 8; tan 30 = 4/y → 6.9; log 0.00001 = −5 | ✓ | P (m36 trig items; no log/midpoint/slope drills) |

### 1d. Inverse square, attenuation, shielding (→ m33 / m36 / m41)

| # | Calc type | Example | Key | Ours |
|---|-----------|---------|-----|------|
| 55 | Inverse square on dose rate / exposure rate | 800 cGy/min @1 m → 43.3 @4.3 m; 115 @100 → 95 @110; 10 mR/h @10 cm → 2.5 @20 | ✓ | C |
| 56 | Inverse square then multiply by time | 100 mR/h @2 m, 30 min @5 m → 8 mR | ✓ | P |
| 57 | Solve for distance that gives a required dose rate (hemibody) | 250 cGy/min @100 → ≤100 cGy/min at ≥158 cm | ✓ | **M** |
| 58 | Inverse square plus n HVL of shielding | 100 mR/h @0.5 m, 2 HVL, @3 m → 0.69 mR/h | ✓ (and ✗ 2.8 in a second copy) | C |
| 59 | Near-field line source: 1/r not 1/r² | 10 mm source, 100 mR/h @2 mm → 20 @10 mm | ~ (teaching simplification) | P |
| 60 | HVL ↔ μ (0.693/μ) | 11 mm → 0.063 mm⁻¹; 12 cm → 0.058; μ 0.0693 → 10 cm; μ 0.51 → 2-HVL block 2.72 cm | ✓ | C |
| 61 | % attenuated / transmitted after n HVL; 3 TVL vs 6 HVL | 4 HVL → 93.75 %; 5 HVL → 96.87 % | ✓ | C |
| 62 | Fractional HVL/TVL products; thickness to 10 % (3.32 HVL) or 5 % (log₂ 20) | 0.3 TVL × 1.2 HVL → 0.218; HVL 4 in → 13.3 in; Ir-192 HVL 4.8 mm → 2.1 cm | ✓ | P |
| 63 | I = I₀e^(−μx) with μ per mm vs per cm trap | 100 R/min, μ 0.258 mm⁻¹, 3 mm → 46.1 | – (no key; 46.12 is an option) | C |
| 64 | Mass attenuation × density × thickness → % transmission | 2.6 cm²/g × 11.3 g/cm³ × 0.05 cm → 23 % | ✓ | P (μ/ρ conceptual in m04/m06; no numeric) |
| 65 | HVL from two intensities and a thickness; initial intensity behind n HVL | 300→10 over 1.2 cm → 0.24 cm; 100 mR/h behind 25 mm with HVL 5 mm → 3200 | ✓ | P |
| 66 | Workload W (patients × fx × dose), with IMRT factor for leakage | 40 pt × 5 × 180 → 36 000 cGy/wk; W_L = 18 000 + 3 × 18 000 = 72 000 | ✓ | C (W); P (IMRT factor) |
| 67 | Primary barrier B = P d²/(W U T) | P 0.1 mSv/wk, 6.5 m, U 0.23, T 1 → 3.67e-5 | ✗ units (0.1 mSv = 0.01 cGy; result only matches W = 50 000 cGy/wk) | C |
| 68 | Leakage barrier B = 1000·P·d²/(W·T) | → key 0.0042 | ✗ (4.2e-4 with consistent units) | C |
| 69 | Number of TVLs in a primary barrier | 2 TVL ≈ 6 HVL teaching statement | – | C |
| 70 | Dose equivalent with quality factors, mixed fields | 0.1 cGy γ + 0.05 cGy n (Q 20) → 11 mSv; 100 β + 100 α + 20 γ + 30 p → 2420 mrem | ✓ | C (single type); P (summing mixed types) |

### 1e. Radioactivity and brachytherapy (→ m40 / m03)

| # | Calc type | Example | Key | Ours |
|---|-----------|---------|-----|------|
| 71 | Decay by half-lives / exponential; λ = 0.693/T½ | 200 → 25 mCi I-131 → 24 d; 100 mCi, λ 0.115/h, 24 h → 6.33; T½ 2.7 d → λ 0.257; Co-60 λ 0.13/y; Cs-137 25 mCi, 6.5 y → 21.5 | ✓ | C |
| 72 | Decay constant of a specific nuclide from memory | I-125 → key 0.0093/d | ✗ (0.0117/d; 0.0093 is Ir-192) | C |
| 73 | Back-solve A₀, or T½ from two assays | 11 Ci after 5 d, T½ 74 d → 11.5 Ci; 10 → 8 mCi in 24 h → T½ 74.5 h | ✓ (one "2.7 years" should be hours) | P (A₀ ok; T½ from two assays **M**) |
| 74 | Time for two different nuclides to reach equal activity | 10 mCi I-125 vs 25 mCi Pd-103 → key ≈34 d | ~ (I get ≈31.5 d) | **M** |
| 75 | Rescale HDR/applicator treatment time for source decay | 282 s on day 1 → 322 s on day 15; 311 s → 320 s 3 d later; 800 s at 6.67 Ci → 812 s at 6.57 Ci; Sr-90 4.5 cGy/s, 2 y → 233 s for 1000 cGy | ✓ | P (activity decay covered; converting to time is conceptual only) |
| 76 | Effective half-life | Tp 8 d, Tb 0.5 d → 0.47 d | ✓ | C |
| 77 | Permanent implant: total dose = 1.44 · T½ · Ḋ₀; back-solve Ḋ₀; dose after n half-lives | 24 cGy/h, 17 d → 141 Gy; 2.4 cGy/h I-125 → ≈4990 cGy; 12 500 cGy → 6.0 cGy/h; 50 Gy at 50 d (T½ 50) → 75 Gy at 100 d | ✓ | C (total); P (back-solve, fraction-delivered) |
| 78 | Exposure rate from Γ and activity at a distance; Ra-eq source; with patient transmission | 10 mg Ra-eq @2 m → 2 mR/h; 20 mCi Tc-99m, Γ 0.87, 12.5 cm, T 0.2 → 22 mR/h | ✓ (@2 m) / ✗ (@3 m key 9.167 R/h, true 0.92 mR/h) | C; P (transmission factor) |
| 79 | mg-Ra-equivalent conversions (Γ ratio to 8.25); mg-h Ra-eq of a permanent I-125 seed; Γ of Au-198 from its Ra-eq | 25 mCi Cs-137 → 9.88 mg Ra-eq; 1 mCi I-125 (Γ 1.1, T½ 60.2 d) → 277 mg-h; 0.288 × 0.825 → 0.238 | ✓ | **M** |
| 80 | Unit conversions: MBq↔mCi, dps→μCi, rem↔Sv, MeV→eV, °F→°C, Å | 555 MBq → 15 mCi; 5.2e4 dps → 1.4 μCi; 10 rem → 100 mSv | ✓ | C (dps→μCi P) |
| 81 | I-125 lead HVL (0.025 mm) memorization | → 0.002 cm | ✓ | P |

### 1f. Radiobiology, inhomogeneity, dosimetry QA, informatics (→ m21 / m37 / m09 / m27)

| # | Calc type | Example | Key | Ours |
|---|-----------|---------|-----|------|
| 82 | BED = nd(1 + d/αβ); compare two regimens | 6 × 6 Gy → 57.6 Gy₁₀; 10 × 3.4 vs 16 × 2.66 → 72.5 vs 80.3 Gy₃ | ✓ | C |
| 83 | Iso-effective dose per fraction for a new n (quadratic solve) | 5 × 10 Gy αβ 10 in 4 fx → 11.6 Gy; 5 × 7 Gy αβ 3 in 42 fx → 1.75 Gy | ✓ (one file keys 12 Gy) | **M** |
| 84 | EQD2 of a cord dose per fraction | 14 fx × 3 Gy, αβ 3 → 50 Gy | ✓ | C |
| 85 | Water-equivalent (effective) depth with densities | 3 cm bone 1.65 + 10 tissue + 4 lung 0.25 + 1 soft bone 1.1 → 17.05; 2.5 + 11 × 0.2 + 3.5 → 8.2 | ✓ | C |
| 86 | Rule-of-thumb % dose error if lung not corrected (≈ %/cm × cm of lung saved) | 4 cm wall + 7 cm lung, 6 MV → ≈18 % over; 18X, 6 cm lung → 4.5 cm × 2 %/cm = 9 % | ~ | P (TMR-ratio correction covered; %/cm heuristic absent) |
| 87 | Temperature-pressure correction; corrected reading per MU | 24 °C, 737 mmHg → 1.038; 65 °F → 1.017; 101 rdg/100 MU at 25 °C, 770 → 1.007 | ✓ | C (Ptp); P (reading/MU) |
| 88 | Orthovoltage timer: exposure rate × ISL × cGy/R × BSF × PDD | 128 R/min @50, 52 SSD, 0.95, 1.17, 63 % → 4.22 min | ✓ | **M** (timer-error drills exist, not this chain) |
| 89 | Pacemaker/out-of-field dose from a % rule | 0.2 % at 30 cm × 50 Gy → 0.1 Gy | ✓ | P |
| 90 | Binary → decimal | 110111 → 55; 10000101 → 133; 11101 → 29; 1110011 → 115; 1010011 → key 80 | ✗ (83) | C |
| 91 | Image data size (n × matrix² × bits), CD backup count, MRI matrix/slice factor, DRR voxel volume, CT pitch | 1000 × 211² × 9 bit → 4.0e8 bit (key 3.77e10 ✗); 512²/256² × 3 → 12×; 2 × 2 × 5 → 20 mm³; 1.5/1.25 → 1.2 | mixed | C (file size, pitch, voxel); P (CD count) |
| 92 | FMEA risk priority number | 8 × 8 × 5 → 320 | ✓ | C |
| 93 | Wavelength from frequency; λ ∝ 1/f | 3.95e14 Hz → 7.59e-7 m | ✓ | P |
| 94 | Mean photon energy ≈ ⅓ nominal | 25 MV → 8.3; 6 MV → 2 | ✓ | P |

Totals: 94 calc types, of which **C = 56 (60 %)**, **P = 25 (27 %)**, **M = 13 (14 %)**.

---

## 2. Recomputation results

I recomputed ≈110 of the ≈175 unique calcs (every calc in files 1–2 and 8 that had enough data, plus every calc in files 3–7). Agreements are marked ✓ above. Disagreements:

### Wrong keys (calculation)

| # | File | Problem (paraphrased) | Key | Recomputed |
|---|------|------------------------|-----|------------|
| 1 | CAPSTONE_XXX | 9 MeV, 3 Gy to 95 %, SSD 109, VSD 90, CF 1.004, cutout 1.021 | 364 MU | 371 MU |
| 2 | PT1 | same problem | 448 MU | 371 MU (PT2 keys 371 correctly) |
| 3 | CAPSTONE_XXX + PT6 | exposure 3 m from 10 mg Ra-eq | 9.167 R/h | 0.92 mR/h (factor 10⁴; cm² vs m² slip) |
| 4 | CAPSTONE_XXX | binary 1010011 | 80 | 83 |
| 5 | CAPSTONE_XXX | 10 mrad fast neutron × Q 20 | 20 mSv | 2 mSv (used 100 mrad) |
| 6 | CAPSTONE_XXX | AP esophagus MU, norm 96.7 % | 125 | 133 (norm must divide, as the same author does for 115.4 %) |
| 7 | CAPSTONE_XXX | iso-effective 4-fx dose for 5 × 10 Gy, αβ 10 | 12 Gy | 11.6 Gy (PT6 keys 11.6) |
| 8 | CAPSTONE_XXX (2nd copy) | 100 mR/h @0.5 m, 2 HVL, @3 m | 2.8 mR/h | 0.69 mR/h (1st copy correct) |
| 9 | CAPSTONE_XXX | Mayneord 68 % @100 → @110, d 8, 6 MV | 68.1 % | 68.7 % |
| 10 | June 2024 | file size 1000 × 211 × 211 × 9 bit | 3.77e10 | 4.0e8 |
| 11 | June 2024 | leakage B with P 0.1 mSv, W 10⁶ cGy, 6.5 m | 0.0042 | 4.2e-4 (P must be 0.01 cGy); primary-B line has the same unit mix and only matches with W = 50 000 |
| 12 | MDCB Pract Calcs | decay constant of I-125 | 0.0093 | 0.0117 d⁻¹ (0.0093 is Ir-192) |

Unit/wording slips (answer number right, label wrong): June 2024 half-life "2.7 years" (hours); MDCB MRI protocol "smaller by 12" (larger by 12); CAPSTONE_XXX "mean energy of a 9 MeV beam = 3 MeV" (that is the photon ⅓ rule, labelled as electron).

Small or convention-dependent differences (not counted): Mayneord 1.0468 vs 1.044 and 1.0531 vs 1.049–1.052 (dmax choice); I-125/Pd-103 equal-activity 34 d vs 31.5 d; adjacent-field gap 0.75 vs 0.70 (depends on whether "collimator setting" is at 100 cm or on skin); MDCB 110-SAD MU 221 (I get 215 from the printed factors; interpolation table not in the text).

### Wrong keys (facts, noticed while reading)

- PT1: T1 white matter keyed "dark grey" (bright; master sheet says bright).
- PT2: typical effective dose for a CT abdomen/chest keyed 2 mSv (7–10 mSv; other copies say 7–10).
- CAPSTONE_XXX: "highest to lowest energy: F-18, I-125, Pd-103, Cs-137" (Cs-137 662 keV belongs first; PT2 keys it correctly).
- Conflicts between copies: MLC intraleaf transmission 1–2 % (PT3, master) vs 2–3 % (PT1); lung brachy "intraluminal" (PT2) vs "intracavitary" (PT8 option/master); "borated polyurethane" typo for polyethylene (PT1/PT2).

**Count: 12 wrong calculation keys (10 distinct problems), 3 label slips, 3 wrong fact keys, ~4 internal contradictions.** Roughly 1 in 9 of the calc keys I checked is wrong or internally inconsistent; the MDCB set is the cleanest (1 wrong of 68), the master sheet the worst.

---

## 3. Non-calc fact inventory and coverage

Grouped by our module. Mark = coverage in the whole bank (questions + theory).

| Our module | Fact cluster from the Capstone pool | Ours |
|-----------|--------------------------------------|------|
| m02/m06 | isotope/isotone/isobar/isomer; Compton dominant MV; PE ∝ Z³, PP ∝ Z², PP threshold 1.022 MeV / dominant >25 MeV; PE = Compton ≈ 25 keV; 90° Compton max 511 keV; annihilation 2 × 511; neutron heaviest; LET ranking; RBE peaks ~100 keV/μm; indirectly ionizing | C |
| m03 | half-lives (I-131 8 d, Tc-99m 6 h/λ 0.1155, Cs-131 9.7 d), HVL and energy rankings of Co/Cs/Ir/I/Pd/Au/Ra/F-18, Γ for Ra 8.25 and Ir 4.62, mean life 1.44 T½, P-32 polycythemia, Sr-90 eye, Y-90 liver, I-131 100–200 mCi, I-131 release ≤5 mR/h | C except Sr-90 for pterygium (M), I-131 release figure (P) |
| m07 | head component order; primary collimator before FF; klystron/magnetron/thyratron/gun/bending-magnet roles; dose-rate via gun current or PRF; highest beam current 6 MV photons; CyberKnife 6 MV; which machines make photons | C |
| m09/m42 | Ptp reference 22 °C/760; Farmer vs parallel-plate; TG-51 = calibration; star-shot = radiation isocenter; picket fence = leaf position; TG-40 2 mm lasers/gantry iso; TG-142 daily 3 %, monthly 2 %, 1 mm MLC, 2 mm field size, 1° gantry, couch 2 mm/1°, light-rad 2 mm or 1 %, OBI scaling 2 mm, imaging dose baseline; TG-100 risk; TG-53 TPS; TG-36 fetal; TG-108 PET; TG-203 CIED; glow curve; gamma pass <1 | C except star-shot (M), glow/film curve ID (P) |
| m10/m11 | CT resolution 0.5 mm / 0.7 lp/mm; HU ranking; HU ranges (Ca 200–1000, CSF 22–30, blood 55–75); pitch formula; DLP = CTDIvol × length, units mGy·cm; typical CT/PET effective doses (head 2, chest 7, abd/pelvis 10, PET/CT 25, mammo 0.4 mSv); dose-reduction (iterative recon, mAs modulation); CT–ED phantom; partial-volume; PET SUV; PET resolution 4 mm; β⁺ decay; Tl-201 cardiac; attenuation-corrected PET recognition; MRI tesla range, T1/T2/PD appearances (fat, CSF, WM/GM, edema, cyst, blood), Gd shortens T1, shim coils, copper RF shield, Primovist T1 | C for HU, pitch, SUV, densities; **M** for DLP/CTDI and CT effective-dose table; P for MRI tissue-appearance table (6 hits only) |
| m12 | integral dose g·Gy; effective dose mSv; Å; cm⁻¹; quality factors (thermal n 5, fast n 20, e⁻ 1, p 10 old) | C |
| m19/m24/m25 | CI </=/> 1 meaning; CI = Rx vol/PTV; HI (D1–D99)/Rx; inhomogeneity index; conformation number; R50, D2cm (RTOG 0813/0915); 0813 energies 4–10 MV and GTV→PTV 0.5/1.0 cm; 0915 arm 2 = 4 × 12 Gy; RTOG 0631 spine; ICRU 83 IMRT, ICRU 62 ITV; IMRT cost function Σw(Drx − Dplan)²; min 3 MU/segment; integral-dose ranking proton < 3D < IMRT < VMAT; VMAT hot spot ~3–4 % above IMRT; AP/PA hot spot at dmax; e⁻/photon abutment hot spot on photon side; past pointing; Clarkson irregular; algorithm matching (Clarkson 2D photon, convolution 3D photon, pencil beam electron, Sievert brachy); kernels from Monte Carlo; superposition > convolution for divergence/inhomogeneity; TERMA; TBI prescription at umbilicus; gamma-knife 1.25 MeV, ≤4 cm; SRS 1 fx, SRT 3–5; 10 MV for prostate IMRT (neutrons); dose outside field 5 % at 2 cm, 0.2 % at 30 cm; 3-field pelvis wedge statements; vertex field size swaps with 90° couch; lowering table shortens PA field length; which normalization point gives most MU | C for most; P for RTOG 0915 arms / 0813 margins, conformation number, past pointing (M), VMAT-vs-IMRT hot-spot figure (M), out-of-field % rule (P), vertex-field/table-height reasoning (P) |
| m20/m21/m22 | prostate adenocarcinoma; ALL most common paediatric; metastasis sites (breast, Ewing, stomach, pancreas, ovary); first nodes for breast = axillary; TNM NX/Tis/M1; sensitivity vs specificity; stochastic = leukaemia; 4 R's; cell-cycle sensitivity order; α/β prostate 1.5, colon 10; gestation most sensitive 1st trimester, 8–15 wk intellectual disability, embryonic death 100–500 mGy; vertebral levels (hyoid C3, thyroid cartilage C4, laryngopharynx C4–6, trachea C6, SSN T2, carina T4–5, hiatus T10, L1 pylorus/kidney hilum, cord ends L2, umbilicus L3, iliac crest L4); 7 true ribs; rectum 12 cm; parallel vs serial organs | C for anatomy, biology, TNM; P for metastasis-site lists and DCIS/APBI margin |
| m23 | proton energies 30–250 MeV, 30 MeV ocular, RBE 1.1 highest at distal edge, scanning fewest neutrons, 2–4 fields, greater surface dose and (per key) greater lateral penumbra, range uncertainty, cyclotron shielding γ + n; SOBP; neutron PDD shape | C (penumbra claim in the source is itself contested by the author) |
| m31/m41 | pacemaker ≤2 Gy, diodes instant readout; fetal 5 mSv; 10 CFR 20 organ 500 mSv, public 1 mSv; 2 mR in any hour; occupancy ½ exam room, 1/40 parking, 1 work area; design goals 0.1 mSv/wk controlled, 0.02 mSv/wk public; W in cGy/wk at 1 m; U definition; NCRP 151 linac / 147 diagnostic; borated polyethylene for door neutrons; door lead ¾ in with maze / 6 in without; 10 CFR 35 medical use / 71 transport; leak test 6 mo, 0.005 μCi; package wipe 2200 dpm; seed assay 10 %; recordable event 10 % | C except NCRP 147/151 numbers (theory only, P) and door-lead figures (M) |
| m40 | lung brachy intraluminal, sarcoma interstitial; active < physical length; Point A/B; Cs-131 prostate; SAVI most catheters; applicator photo IDs; mg-Ra-eq | C except SAVI/APBI device comparison (P) and mg-Ra-eq (M) |
| m26/m27 | HL7 to billing; HIPAA provisions/identifiers; binary | C for HL7/binary; **M** for HIPAA |
| m34 | MLC intraleaf transmission 1–2 %; scalloped penumbra; collimator rotation between arcs to reduce interleaf leakage; compensator resolution > MLC; wedge-angle on an isodose diagram | C (first two); P (arc collimator trick, compensator statement) |
| m43 | the full tolerance list (lens 10 Gy cataract / 7 Gy max, cochlea 30 mean, optic nerve 54, brainstem 55 to 0.03 cc, parotid 26 mean, lips 20 mean, larynx 66, oesophagus 35 mean, cord 50 / 47 for 20 cm, cauda 60, ribs 50, heart V50 33 %/V25 10 %, liver 25, kidney V20 32 % / 23 Gy, bowel 50, ovaries 5, testes 2, bladder V80 15 %/V50 55 Gy, rectum V50 50 %/V75 15 %, femoral head 50/52, SRS brain V12 5–10 cc, brainstem 12.5, optic 12, cord 13–14, SBRT lung V20 ≤10 %) | C (QUANTEC/RTOG module); P for the single-fraction SRS set (7 hits) |

Non-calc clusters: ≈75 clusters; **C ≈ 55 (73 %)**, **P ≈ 14**, **M ≈ 6** (DLP/CTDI + CT effective doses, HIPAA, star-shot, past pointing, Sr-90 pterygium, door-lead rule, VMAT-vs-IMRT hot-spot figure).

---

## 4. Summary

- **Unique items across the eight files: ≈590** (≈175 calcs in 94 calc types; ≈415 facts in ≈75 clusters; ≈60 image-ID items unusable from text).
- **Coverage in our bank:** calc types 60 % COVERED / 27 % PARTIAL / 14 % MISSING; fact clusters ≈73 % COVERED / 19 % PARTIAL / 8 % MISSING. Weighted by items, roughly **two-thirds of the pool is already fully covered** and another quarter is partially covered.
- **Wrong keys found: 12 calculation keys (10 distinct problems), 3 mislabelled answers, 3 wrong fact keys, ~4 internal contradictions** between copies. The MDCB calc set is reliable; the master sheet and PT1 are not safe to memorise from without re-deriving.

### MISSING calc types worth adding as original items (by our module)

- **m35** — SMR = TMR − TMR₀ (one item); zero-area TMR from μ and dmax (one item); SAD-vs-SSD set-up error as a dose/MU error scenario (two items: "+21 % MU at mid-plane" and "n fractions delivered at the wrong setup"); weighted 1:0.5:0.5 iso split and per-beam dmax after a 95 % Rx (one each); wedge omitted for part of a course (one); electron R50 ≈ E/2.4 (Eo ≈ 2.33·R50) alongside the existing E/2, E/3, E/4 rules (one); back-solving a normalization from a given MU (one).
- **m36** — collimator setting for a large field at extended distance, with the 45° diagonal variant (two); radius from CAX to the centre of an asymmetric open field (one); "collimator setting at 100 cm vs field on skin" gap trap (one); orthovoltage timer chain (exposure rate × ISL × cGy/R × BSF × PDD) (one); mass-attenuation × density × thickness transmission (one); HVL from two intensities and a thickness, and thickness for 5 % with a given HVL (one each); mixed-radiation dose-equivalent sum (one).
- **m33** — solve inverse square for the distance that meets a dose-rate cap (hemibody) (one); inverse square × exposure time (one).
- **m37** — the "% per cm of lung saved" heuristic (≈3–3.5 %/cm at 6 MV, ≈2 %/cm at 18 MV) as a sanity check against the TMR-ratio method (one).
- **m40 / m03** — mg-Ra-equivalent conversions (Γ ratio; mg-h of a permanent seed; Γ from Ra-eq) (two–three); rescaling HDR/applicator treatment time for decay between fractions (two); half-life from two assays (one); time for two nuclides to reach equal activity (one); initial dose-rate back-solve and dose-after-n-half-lives for permanent implants (one each); exposure rate with a patient transmission factor (one).
- **m41** — IMRT factor in the leakage workload (one); unit-consistency item for B (P in Gy vs W in Gy, the exact trap the June key fell into) (one).
- **m21 / m40** — iso-effective dose per fraction for a new fraction number (quadratic solve) (two).

### MISSING / thin facts worth adding

- **m10**: DLP = CTDIvol × scan length (mGy·cm), pitch, and a typical effective-dose table (head 2, chest 7, abd/pelvis 10, PET/CT 25, mammogram 0.4 mSv); MRI tissue-appearance table (T1/T2/PD for fat, CSF, WM/GM, edema, cyst, blood; Gd shortens T1).
- **m26/m27**: HIPAA provisions and protected identifiers.
- **m42**: star-shot / spoke-shot = radiation isocenter; single-fraction SRS constraint set.
- **m25**: past pointing (3D arc), VMAT vs IMRT hot-spot magnitude, out-of-field dose rule (≈5 % at 2 cm, ≈0.2 % at 30 cm), vertex-field size swap and table-height effect on PA field length.
- **m41**: NCRP 151 vs 147 scope; door lead rule of thumb with/without maze.
- **m03**: Sr-90 for pterygium; I-131 inpatient release criterion.

### Verdict for the calculation domain: **complementary, and on balance our bank is better.**

Our six calc modules already drill the core (MU, PDD/TMR/Mayneord, gaps, divergence, inverse square, HVL/TVL, permanent-implant and TG-43 dose, shielding B) more systematically and with correct keys. The Capstone pool adds breadth in exam-flavoured twists — set-up and wedge *error* scenarios, mg-Ra-equivalent arithmetic, decay-rescaled HDR times, extended-distance collimator settings, SMR, zero-area TMR from μ, iso-effective fraction solving — which is where the 13 MISSING and 25 PARTIAL types sit; those are worth writing as original items. The MDCB Pract Calcs file is the single most valuable source here (retired-exam style, 67/68 keys correct). The master sheet and practice tests are useful as a checklist of recall facts but their keys need re-derivation before trusting (≈1 in 9 calc keys wrong).
