# DoseGrid course (OCR screenshots) and "Picture Day" slide deck vs. our bank

Sources (third-party, copyrighted, gitignored): `inbox/RM Review/DOSE GRID.pdf` (420 screenshot pages, OCR text ≈15,100 lines) and `inbox/RM Review/Picture+Day+Sun.pptx` (≈1,290 lines of slide text). Both were read in full, in order. Everything below is restated in my own words; no course text, stems, or answer keys are copied, and nothing from `inbox/` has been written into `knowledge/`.

Method: for each DoseGrid lesson I recorded the facts, tables and worked examples it teaches and counted its mini-quiz/quiz items, then grepped `knowledge/theory/mNN-*.md` and `knowledge/questions/mNN-*.md` for the same terms and numbers (and, for every candidate gap, the whole bank, since several facts live in a different module than the course puts them). Classification: **COVERED** = same facts at equal or better depth; **PARTIAL** = topic present but the listed facts/numbers are absent; **MISSING** = topic essentially absent.

The course is a lesson → mini-quiz → section-quiz sequence. Our module titles follow the lesson titles 1:1, so the mapping is direct. Quiz counts below are the number of items visible in the OCR (a few image-only items may be under-counted).

---

## Lesson-by-lesson

### Introduction / Formula sheet / Study tips → m01
**Teaches:** the exam content matrix with domain weights (I 16%, II 8%, III 40%, IV 15%, V 6%, VI 7%, VII 8% in the 2018 version the course uses), a one-page formula sheet (inverse square, couch and collimator angle tangents, opposed-tangent gantry formula, wedge angle = 90 − hinge/2, BED/EQD2, exponential transmission with μ = 0.693/HVL, barrier W·U·T, electron R₈₀ ≈ E/2.8, R₉₀ ≈ E/3.2, R₅₀ ≈ E/2.33, electron virtual-SSD inverse square with gap term, electron MU formula, unit equivalences, Planck relation, T/P correction, TAR = TMR × BSF, Gp = s(SSD + d − SDD)/SDD, SSD and SAD MU set-ups, 6 MV ≈ 3.5 %/cm, pixel = FOV/matrix, kV output ∝ kVp²·mAs), dmax tables (electrons 6/9/12/15/18 MeV ≈ 1.4/2.2/2.9/2.9/2.9 cm; photons 4/6/10/18 MV = 1/1.5/2.5/3.5 cm; Co-60 0.5 cm), mean life 1.44 T½, an isotope table, a window/level table, the HU scale, OER and HI definitions. Study tips: time per question, flag-and-return, calculator habits.
**Quiz:** none.
**Status:** COVERED for formulas (every formula appears in m33/m35/m36/m21/m40/m41). PARTIAL for the matrix: m01 cites the newer 2023 matrix (Physics 14 %), which is correct and better than the course, but the per-domain percentages are listed in one line only and no item tests them. Low priority—the exam does not ask about its own blueprint.
**Flag:** course matrix is the 2018 one; ours is newer.

### Fundamentals of Physics → m02
**Teaches:** atomic structure, electron ≈ 1/1800 proton mass, A/Z notation, amu, electrons per gram = N_A·Z/A, E = mc², 0.511 MeV, mass defect/binding energy, 2n² shell rule, four fundamental forces ranked by strength, isotopes/isotones/isobars/isomers.
**Quiz:** 6.
**Status:** PARTIAL. Nuclide classification, 0.511 MeV, 2n² (one question) are present. **Missing:** mass defect and binding energy per nucleon; the electron/proton mass ratio (~1/1836); electrons-per-gram formula and why fat has more electrons per gram than bone (bank uses electron density conceptually, m06 hints at it, no formula); the four forces ordering (strong > EM > weak > gravity).

### Radioactivity + Decay calculations → m03
**Teaches:** Becquerel 1896, λ and A = A₀e^(−λt), 1 Ci = 3.7×10¹⁰ Bq, half life vs mean life (1.44), specific activity, transient vs secular equilibrium, decay-mode table (α for Z > 82, β⁻, β⁺, EC, IC, isomeric), β average ≈ ⅓ max, Co-60 1.17/1.33 MeV, isotope table (Pd-103 17 d/21 keV, I-125 60 d/35 keV, Ir-192 74 d/380 keV, Cs-137 30 y/662 keV, Co-60 5.26 y/1.25 MeV, Ra-226 1622 y), Co-60 output-after-N-years worked example, Sr-90 eye-applicator timing problem, "equal activity I-125 vs Pd-103—which has more atoms" problem.
**Quiz:** 7 + 5.
**Status:** COVERED. m03 is 510 theory lines/78 questions, richer than the course (effective half life, equilibrium math, multiple decay-correction problems). Only trivia absent: discovery year 1896, α emission being typical of Z > 82, and the Ra-226 average photon energy (the course's ~0.83 MeV figure; our m35 mentions 830 keV once in passing).

### X-ray production + Tube design → m04
**Teaches:** brems vs characteristic, efficiency ≈ 9×10⁻¹⁰·Z·V, Auger electrons, critical absorption energy, mean energy ≈ ⅓ peak, output ∝ kVp²·mAs, target tungsten (Z 74, mp ≈ 3400 °C), rotating anode, line-focus principle, anode heel effect, focusing cup, dual focal spots, filament/high-voltage circuits, μ and μ/ρ.
**Quiz:** 5 + 11.
**Status:** COVERED (efficiency formula, melting point, line focus, heel effect all present). **Missing:** rotating anode (why: heat loading) is never named—one sentence.

### Characteristics of radiation → m05
**Teaches:** EM vs particulate, x vs γ by origin, 1 eV = 1.6×10⁻¹⁹ J, ionizing threshold, EM spectrum order, neutrons as indirectly ionizing and shielded with hydrogenous/borated material, neutron production above ~8–10 MV and why 15 MV IMRT is avoided, ICRP-60-style radiation weighting factors (photons/electrons 1, neutrons 5–20 by energy, α 20).
**Quiz:** 6.
**Status:** COVERED for weighting factors, neutron shielding, photoneutron threshold. **Missing:** the eV→joule conversion; EM-spectrum ordering (radio → microwave → IR → visible → UV → x/γ); the "IMRT at 15 MV multiplies neutron dose because of MU" argument is only implicit.
**Flag:** course uses the old neutron weighting-factor steps (5/10/20/10/5); ICRP-103 uses a continuous function. Ours is fine either way.

### Interactions of radiation with matter → m06
**Teaches:** coherent, photoelectric (∝ Z³/E³), Compton (dominant ~25 keV–25 MeV, electron scatter 0–90°, 90° scatter → 0.511 MeV cap, backscatter → 0.256 MeV cap), pair (1.022 MeV threshold), triplet (2.04), photodisintegration (> ~10 MV), E = hν with frequency→wavelength examples (3 GHz → 10 cm), SI prefixes, mCi→MBq conversions, fat vs bone electrons per gram, f-factor, muscle receives ≈ 99 % of water dose (so a 100 cGy water calc ≈ 101 MU to muscle in the course's example).
**Quiz:** 20.
**Status:** COVERED for all interaction physics, including triplet and the 0.256/0.511 limits. **Missing:** photodisintegration as the named fifth interaction (the neutron-production consequence is covered in m05/m41 but the word never appears); Planck's constant and an E = hν numeric example; the water-to-muscle 0.99 correction as an MU adjustment.

### Treatment machines → m07
**Teaches:** linac component tour, magnetron vs klystron, traveling vs standing wave guides and the circulator, 90°/270° bending, photon-mode vs electron-mode components (target, flattening filter vs scattering foils), filter flattens at 10 cm depth and produces horns at shallow depth, FFF properties (higher dose rate, softer spectrum, shallower dmax, no horns), kV-therapy table (Grenz < 20 kV; contact 40–50 kV at < 2 cm SSD; superficial 50–150 kV at 15–20 cm; orthovoltage 150–500 kV at 50 cm), Co-60 dmax 0.5 cm and 80 cm SSD, source sticking, flattening filter removes up to ~90 % of central-axis fluence, beam current higher for photon mode than electron mode and higher for 6 MV than 15 MV, bending-magnet current changes with energy.
**Quiz:** 20.
**Status:** COVERED for components, FFF, kV table, circulator, carousel. **Missing:** traveling vs standing wave distinction (name, length, where the circulator fits); the "~90 % attenuation by the filter" and electron-gun/beam-current facts (which the course quizzes); thyratron/modulator/PFN (appears only in m19 by accident).

### Magnification → m08
**Teaches:** similar triangles, MF = image/object = SID/SOD, electron cutout size at extended SSD, TBI distance needed to cover a patient (170 cm patient in a 40 cm field at 100 cm → 425 cm), block-tray-to-isocenter scaling.
**Quiz:** 6.
**Status:** COVERED (m08 has 20 questions on exactly this). **Missing:** the TBI "distance to fit the patient" variant and the electron-cutout-at-extended-SSD variant—both are one-line applications of the same ratio.

### Radiation measurement → m09
**Teaches:** kerma vs absorbed dose, exposure (R, C/kg), f-factor, TG-51 overview, beam-quality specifiers (PDD(10)x and R₅₀; kV by HVL in mm Al/Cu), T/P correction, sealed monitor chambers, P_ion/P_pol/P_elec/M_raw, TAR/TPR (TPR₂₀,₁₀, 5 cm reference)/TMR/SMR, narrow-beam geometry for HVL.
**Quiz:** 15.
**Status:** COVERED, except **scatter-maximum ratio (SMR)** is never defined, and the HVL-in-mm-Al/Cu beam-quality convention for kV units is only in m04/m07 rather than m09. Free-air chamber and parallel-plate chambers are present.

### Imaging modalities (CT, MRI, PET, US) → m10
**Teaches:** CT as a matrix of μ, HU formula, DRR/BEV, thinner slices → better DRRs, flat top/bore size/artifacts/BB placement, "fast facts" (CT overestimates prostate volume vs MRI; 2–10 mm slices; HU→density curve depends on kVp and filtration not mAs), fluoroscopic sim, CT-on-rails, MRI (Larmor precession, TR/TE table—long TR + short TE = proton density, short/short = T1, long/long = T2; T1/T2/FLAIR brightness table; 1.5–3 T; nuclei with even N and Z do not image; 256–512 matrix; Gamma Knife planning on MRI), PET (511 keV, ~4 mm resolution, ~10 mCi FDG, ~1–4 cGy, bladder wall highest dose, SUV), ultrasound (piezoelectric, acoustic impedance, 1–20 MHz).
**Quiz:** 10.
**Status:** PARTIAL. HU, T1/T2/FLAIR brightness, PET 511 keV/SUV/4 mm, piezoelectric, 4DCT are present. **Missing:** the TR/TE → weighting table; Larmor/field strength (tesla) and "proton density" weighting; CT overestimates prostate volume by ~30 % vs MRI (both sources teach this; it is a classic exam fact); CT-on-rails and conventional fluoro simulators as named devices; ultrasound frequency range; PET patient dose ~1–4 cGy. DRR and BEV are only in questions, not theory.
**Flag:** course says CT matrices are 1024×1024; 512×512 is the standard planning-CT matrix.

### HU scale → m11
**Teaches:** cheese-phantom HU→density calibration; scale: air −1000, lung ≈ −750 (range −950 to −500), fat ≈ −100 to −50, water 0, muscle ≈ +40, soft tissue ≈ +100, bone +700 to > +2000.
**Quiz:** 5.
**Status:** COVERED.

### Units → m12
**Teaches:** SI prefixes, unit conversion table (Gy/rad, Sv/rem, R, Ci/Bq, 1 mCi = 37 MBq), mg-Ra-eq.
**Quiz:** 10.
**Status:** COVERED.
**Flag:** course equates 1 Gy with 100 R; strictly 1 R ≈ 0.876 cGy in air / ≈ 0.95–0.97 cGy in tissue. Ours states the approximation correctly.

### Acquisition of patient data → m13
**Teaches:** phantom vs patient; historical contouring tools (lead wire, calipers, pantograph, conventional simulator with fluoro); contour-correction methods (effective SSD, TAR/TMR ratio, isodose shift); inhomogeneity-correction principles.
**Quiz:** 3.
**Status:** COVERED for corrections (effective SSD, TAR ratio, isodose shift, Batho/ETAR present). **Missing:** the legacy contouring hardware (lead wire, solder wire, calipers, pantograph) and the scout/topogram term—trivia, but the course quizzes it.

### Patient positioning → m14
**Teaches:** SAD vs SSD set-ups, avoid thick pads (attenuation/surface-dose build-up), rigid thermoplastic masks, supine default, prone breast indications, feet-first set-ups.
**Quiz:** 3.
**Status:** COVERED (prone breast, feet-first, mask rationale). **Missing:** the "avoid thick mattress under the beam" immobilization-attenuation point (the only related text is in m34 bolus/skin-dose material).

### Motion management → m15
**Teaches:** TG-76, ≥ 5 mm motion as the threshold for management, 4DCT (~1500 slices sorted into 10 phases), prospective vs retrospective gating, ITV, tracking systems (floor-mounted fluoro, ExacTrac, CyberKnife 6-DOF robot, Calypso beacons, MR-guided), ≥ 3 fiducials for 6-DOF registration.
**Quiz:** 4.
**Status:** PARTIAL. 4DCT, ITV, gating, breath-hold, Calypso, TG-76 are present. **Missing:** the 5 mm "manage motion above this" threshold; prospective vs retrospective gating vocabulary (the words appear only in m41/m44 in other contexts); ExacTrac as a named system; "at least three fiducials" for rotation (present only in m18/m31/m32).
**Flag:** course cites TG-40 for gating QA; TG-76 (and TG-142) are the right references.

### Simulation → m16
**Teaches:** user origin and shifts, urethrogram to locate prostate apex, MRI/PET fusion for target definition.
**Quiz:** 2.
**Status:** COVERED. **Missing:** urethrogram (retrograde contrast to mark the apex) — one fact.

### Image registration / segmentation → m17
**Teaches:** segmentation = contouring, rigid (6-DOF) vs deformable, common modality pairings, Velocity as a DIR product.
**Quiz:** 2.
**Status:** COVERED (rigid vs deformable, Dice/Hausdorff, MIM/Velocity named in other modules). "Segmentation" as a synonym appears only in m30—add a sentence.

### IGRT → m18
**Teaches:** kV vs MV planar, 6 MV images better than 15 MV, CBCT reconstruction by filtered back-projection, half-fan/bowtie for large FOV, MV-CBCT vs kV-CBCT, TomoTherapy MVCT, ultrasound/TRUS, ExacTrac, CyberKnife, Calypso, MR-guided.
**Quiz:** 4.
**Status:** COVERED for modality comparisons and MR-linac. **Missing:** FBP, half-fan/bowtie filter, flat-panel detector as terms; ExacTrac; TRUS for prostate IGRT.
**Flag:** course states MV imaging has better soft-tissue contrast than kV—wrong (kV photoelectric contrast wins; MV has less artifact from metal).

### Isodose, electrons, protons, dose metrics → m19
**Teaches:** *Electrons*: Rp, bremsstrahlung tail 0.5–3 %, R₉₀/R₈₀/R₅₀ rules, R₈₅ "therapeutic range", cones and cone factors, cutout dimension ≥ E/2 cm, cerrobend composition, virtual SSD and gap-factor worked example, dmax table, 2 MeV/cm, surface dose rises with energy, dual scattering foils, obliquity, hot spot on the photon side of an abutment, bolus, lead E/2 mm, eye shields, electron arc, electrons vs superficial x-rays, air-cavity hot spots; quiz items include "maximum LET at ~22 MeV/cm" and "90 % at E/3". *Protons*: Bragg peak, cyclotron vs synchrotron, RBE 1.1 (variable at the distal edge), range uncertainty ~2.5–3.5 % + mm, passive scattering vs PBS, algorithms, IMPT, entrance 70–90 % vs photon ~60 %. *Isodose/metrics*: horns, Gp formula, physical penumbra 80–20 (course uses 90–20), field size at 50 %, Clarkson, ±2 % TPS accuracy, ICRU volumes, differential vs cumulative DVH, HI = (D2 − D98)/D50, CI, D0.03cc, coverage, NTCP/gEUD.
**Quiz:** 18 + 8 + 10.
**Status:** COVERED and richer than the course for electrons (m19 is 511 lines/75 Q; our R₉₀/R₈₀ notation differs but the rules are there), protons and metrics. **Missing:** R₈₅ "therapeutic range" terminology; cyclotron vs synchrotron (only m07 mentions them in passing); IMPT by name; electron arc therapy; Clarkson sector integration in m19 (present elsewhere); NTCP/TCP acronyms (gEUD present).

### Site-specific oncology → m20
**Teaches:** a long run of site notes: incidence/prognostic factors, brain (GBM 60/30, WBRT 30/10, SRS), spine, pediatrics (medulloblastoma CSI 23.4/36 + 54, Wilms, neuroblastoma, leukemia CNS), H&N sub-sites (oral tongue, floor of mouth, retromolar trigone, Ohngren's line/maxillary sinus, nasopharynx, larynx, HPV), skin (melanoma ABCDE, Merkel), lymphoma (Hodgkin subtypes, B symptoms, Reed-Sternberg), lung (SVC syndrome, SCLC PCI), breast (invasive ductal most common, BRCA, field borders), esophagus (~25 cm, Barrett, histology by third), pancreas (uncinate, Whipple), liver (HCC), kidney, bladder, prostate (LDR seed doses 145/115 Gy mono; EBRT 45–50 nodes/54–56 vesicles/72–80 prostate), testis (hockey-stick/dog-leg), colorectal, gyn (point A, ovary CA-125), bone (osteosarcoma, Ewing t(11;22), myeloma), soft-tissue sarcoma, anal canal; hyperfractionation.
**Quiz:** 16.
**Status:** PARTIAL—two different strengths. Our m20 is a dose-regimen recognition module (97 Q) and is deeper than the course on prescriptions, regimen traps, OARs and techniques (SIB math, prostate bed, bladder preservation, Wilms/neuroblastoma, vulva/vagina, AVM, liver SBRT, meningioma, pituitary). The course is broader on **clinical oncology trivia**, which our bank lacks almost entirely: epidemiology/prognostic factors; H&N sub-site anatomy (Ohngren's line, retromolar trigone, floor of mouth, maxillary sinus); HPV as a favorable prognostic factor (one question only); melanoma ABCDE/Merkel cell; Hodgkin subtypes/B symptoms; SVC syndrome as an emergency; invasive ductal carcinoma/BRCA; esophageal length ~25 cm and Barrett's; uncinate process/Whipple; hockey-stick field for seminoma; LDR prostate monotherapy doses in the oncology context (present in m40); bone/soft-tissue sarcoma histologies (Ewing translocation, osteosarcoma age peak, myeloma); hyperfractionation definitions.
**Flags:** fetal exposure limit printed as "10 Gy" (should be cGy); "145 Gy I-131" for prostate (I-125); a penile-cancer paragraph duplicating the testicular text.

### Radiobiology → m21
**Teaches:** survival curve (Dq, D₀ = dose to 37 %, n), Bergonié–Tribondeau law, cell-cycle sensitivity (M/G2 most, late S least), 4 Rs, OER ≈ 2.5–3, fetal windows (3–12 weeks organogenesis), BED/EQD2 with a cord re-irradiation worked example (α/β 3; 50.4/28 → BED ≈ 80.7; cumulative cord BED limit ~150) and an EQD2 example (42 Gy at 3 Gy/fx → 50.4 Gy EQD2).
**Quiz:** 8.
**Status:** COVERED and richer (328 lines; EQD2 appears 49×; LET/RBE/LQ well treated). **Missing:** Bergonié–Tribondeau by name; the cord re-irradiation cumulative-BED worked example (the bank does cord EQD2 in m25/m43 but not a cumulative BED ≈ 150 Gy₃ rule); DSB as the lethal lesion by name; fetal 3–12 week window stated only once.

### Anatomy → m22
**Teaches:** structure identification checklist; brachial plexus C5–T1; carina T4–T5; seminal vesicles posterior-superior to prostate; lymphatic maps (H&N levels, Waldeyer's ring, axillary levels I–III by pectoralis minor, pelvic and para-aortic chains, celiac/porta hepatis).
**Quiz:** 15 (mostly image-based).
**Status:** COVERED (m22 247 lines/60 Q, including levels, Sappey/pectoralis minor, IMN, carina). **Missing:** Waldeyer's ring; thoracic duct; lacrimal gland as an OAR. Image-identification items cannot be reproduced in a text bank.

### Delivery systems (IMRT/VMAT) → m23
**Teaches:** VMAT (fewer MU than fixed-field IMRT, variable dose rate/gantry speed, beam-hold), jaw tracking, conformal arc, step-and-shoot vs sliding window, optimizer families (gradient descent, simulated annealing, direct aperture optimization), leaf sequencing.
**Quiz:** 7.
**Status:** PARTIAL. VMAT, step-and-shoot/sliding window, leaf sequencing, dose-rate modulation present. **Missing:** jaw tracking (purpose: reduce MLC leakage); optimizer names (gradient vs stochastic/simulated annealing vs DAO)—the course has a quiz item on this; "VMAT typically uses fewer MU than IMRT" as an explicit statement.

### Special procedures (TBI, TSEB, SRS) → m24
**Teaches:** TBI (±10 % uniformity, compensators, 1–2 cm acrylic spoiler to bring surface ≥ 90 %, lung as limiting organ, < 35 cm separation at ≥ 300 cm SSD lets 6 MV work, 5–10 cGy/min at midplane, 0.6 cc Farmer in a 40 cm phantom for calibration, in vivo TLD/diode ±5 %, verify first ~20 patients), TSEB (±20° dual-angle, mycosis fungoides, Stanford 6-position), SRS (±1 mm, prescribe to 50–80 % isodose, TG-101 grid ≤ 2 mm, TG-142 tolerances 1 mm for SRS vs 2 mm standard, cones vs MLC, non-coplanar arcs).
**Quiz:** 8.
**Status:** COVERED for TBI/TSEB/SRS concepts (12 Gy/6–8 fx, lung blocks, spoiler, Stanford, frame/frameless, cones). **Missing numbers:** TBI dose-rate band 5–10 (to ~20) cGy/min; the "< 35 cm separation at ≥ 3 m → 6 MV is enough" rule; ±10 % uniformity target; in-vivo ±5 % acceptance; SRS prescription isodose 50–80 % (present in m19/m45, not m24); TG-142 SRS 1 mm vs 2 mm isocenter tolerance; TG-101 ≤ 2 mm grid.

### Planning methods → m25
**Teaches:** energy selection (course: "< 12 MV for lung"), breast separation > 25 cm → consider higher energy or mixed, lung build-up loss, normalization math (200 cGy / 0.90 = 222 cGy to the max), beam weighting, mono- vs dual-isocenter breast, IMN mini-tangent, hockey-stick, off-cord AP/PA at 45 Gy for lung, 3D H&N, postage-stamp larynx, parotid electron/photon mix, surface dose vs field size/tray, integral dose, exit dose at 15 MV.
**Quiz:** 2 + 15.
**Status:** COVERED for normalization, weighting, half-beam block, breast match, 110 %, separation (in questions). **Missing:** IMN mini-tangent/wide-tangent technique; hockey-stick (seminoma) field; off-cord oblique at 45 Gy as a named 3D lung technique; postage-stamp larynx fields (only in questions); surface dose increases with field size, tray, obliquity (not stated in m25; m34 bolus section is the nearest).
**Flag:** "< 12 MV lung" is an odd cut-off; the usual teaching is ≤ 10 MV (6 MV preferred) because of lateral electron disequilibrium.

### DICOM → m26
**Teaches:** DICOM-RT objects (RTSTRUCT, RTPLAN, RTDOSE, RTIMAGE), PACS, HL7 vs DICOM, transfer failures.
**Quiz:** 3.
**Status:** COVERED (m26 richer—17 Q).

### Computer systems → m27
**Teaches:** bit/byte/pixel/voxel, LAN/MAN/WAN, MIPS, ROM/RAM, parallel processing, off-site backups, Unix-based TPS history (Pinnacle), scripting.
**Quiz:** 4.
**Status:** COVERED. Missing only MIPS and "parallel processing" vocabulary—trivia.

### Adaptive RT → m28 (no quiz) — COVERED; our m28 has online/offline adaptation, triggers (weight loss, bladder filling), CBCT-dose caveats are the only item not stated.

### Autoplanning → m29 (no quiz) — COVERED (KBP/RapidPlan, templates, MCO/Pareto, model libraries; 13 Q).

### Autocontouring → m30 (quiz 1) — COVERED and richer (atlas vs deep learning, Dice/Hausdorff, review workflow).

### Implanted devices → m31
**Teaches:** pacemaker < 2 Gy per TG-34, prefer ≤ 6 MV (no neutrons), dependent vs non-dependent patients.
**Quiz:** 2.
**Status:** COVERED and newer—m31 teaches TG-203 risk categories (2/5 Gy, neutron tier) alongside TG-34.
**Flag:** course teaches only TG-34 (1994); TG-203 (2019) replaced it.

### IGRT limitations → m32
**Teaches:** systematic vs random error with examples (laser miscalibration, couch sag, contouring = systematic; daily bladder filling = random), ≥ 3 fiducials, fiducial migration, pitch/roll/yaw.
**Quiz:** 3.
**Status:** COVERED (systematic/random, residual error, fiducials, 6-DOF, van Herk present). **Missing:** the worked list of which real errors are systematic vs random (laser/couch-sag/delineation examples), and fiducial migration as a limitation.

### Algorithms and inverse square → m33
**Teaches:** algorithm tiers (Monte Carlo at top; Acuros/collapsed-cone/AAA; pencil beam over-predicts dose in lung; hand calculation at the bottom), mass-energy-absorption coefficient, inverse square beginner (10 Q) and advanced problems (TBI at 3 m beyond isocenter → 1/16; AP at 95 SSD; 90 → 110 cm SSD MU change; calibration at SSD vs SAD ≈ 3 % difference).
**Quiz:** 7 + 10 + 7.
**Status:** COVERED (63 inverse-square questions, all algorithm families, lung pencil-beam issue present). **Missing:** the "SSD vs SAD calibration ~3 %" variant; μ_en/ρ as the link from fluence to dose (only m04/m09 mention it).

### Beam modifiers → m34
**Teaches:** wedge angle defined at 10 cm depth, wedge ≥ 15–20 cm from skin, beam hardening, wedge (transmission) factor, dynamic vs physical vs universal wedge, 3-field wedged-pair example (229 cGy), wedge = 90 − hinge/2, tongue-and-groove 3–4 % under-dose, transmission: jaws < 0.1 %, MLC 1.5–3 %, blocks 4–5 %; divergent blocks give the sharpest penumbra; bolus, compensators, partial-transmission blocks.
**Quiz:** 13.
**Status:** COVERED (wedge factors 31×, hinge, EDW, T&G, transmission values). **Missing:** the explicit "wedge angle is specified at 10 cm" and "keep the wedge ≥ 15 cm from skin" statements; "focused blocks have the sharpest penumbra, MLC the widest" comparison; EDW wedge factor depends strongly on field size while physical wedge factor varies little.

### PDD / TMR / MU calculations → m35
**Teaches:** interpolation, PDD vs TMR definitions, Mayneord F, equivalent square 2ab/(a + b), Sc/Sp/Scp, tray and wedge factors, inverse-square/SAD factor, off-axis ratio, electron MU.
**Quiz:** 6 + 3 + 9.
**Status:** COVERED and richer (369 lines/67 Q). Only vocabulary gap: Scp as the "total scatter/output factor" name (bank uses Sc and Sp separately).

### Special calculations (gap, angles, transmission, Gp, timer) → m36
**Teaches:** gap = ½L₁·d/SSD₁ + ½L₂·d/SSD₂, couch/collimator angle tangents for CSI, opposed-tangent gantry formula, exponential transmission/HVL/TVL, Gp mini-set, Co-60 timer and end-effect, trig refresher.
**Quiz:** 3 + 2 + 2 + 4 + 1 + 8.
**Status:** COVERED and much richer (589 lines/123 Q—our strongest calc module).

### Inhomogeneity → m37
**Teaches:** overrides (streak artifacts, wires, contrast, dental), lung ≈ ⅓ water density, 6 MV ≈ 3.5 %/cm, effective path length.
**Quiz:** 5.
**Status:** COVERED (overrides, EPL, Batho/ETAR). **Missing:** the "≈ 3.5 %/cm for 6 MV, lower for higher energy" rule of thumb in m37 (it is in the m01 formula sheet of the course; our bank states per-cm attenuation nowhere); "lung ≈ ⅓ density" phrasing (we use 0.25–0.3 g/cc, fine).

### Deformable dose accumulation → m38 (no quiz) — COVERED; add that accumulated dose carries DIR uncertainty and should be treated as approximate.

### Uncertainty → m39 (no quiz)
**Teaches:** ±5 % overall accuracy goal and a component table (calibration, TPS, set-up…) combining in quadrature to ≈ 5.6 %.
**Status:** PARTIAL. m39 has 50 lines on grid size/voxel effects but **does not state the ICRU ±5 % goal or a quadrature budget**. Add both.

### Brachytherapy → m40
**Teaches:** radium needle specs (active vs physical length, 0.66/0.33 mg/cm full/half intensity, Indian club/dumbbell), autoradiographs, isotropy, Γ_Ra = 8.25 R·cm²/(mg·h), mg-Ra-eq worked example, apparent activity, air-kerma strength, Paterson-Parker/Quimby/Paris systems, HDR defined ≥ 20 cGy/min (12 Gy/h), Ir-192 HDR ~10 Ci, 0.3–0.6 mm source, LDR prostate doses (table mislabelled HDR), implant types incl. intravascular 15–20 Gy, Manchester points A/B/bladder/rectal, Mobius3D-type second check within 5 %, NCRP 40, semi-annual leak test, NRC HDR licensing, post-source-exchange tests, transport labels (White-I < 0.5 mrem/h surface; Yellow-II ≤ 50 mrem/h surface, TI ≤ 1; Yellow-III > 50), calc quiz (Au-198 Γ 0.238–0.247; permanent-implant total dose = 1.44·T½·Ṙ₀; Ir-192 1 mCi ≈ 0.568 mg-Ra-eq; LDR 0.2 cGy/h × 5 days; exposure rate at 2 m from 150 mCi Cs-137).
**Quiz:** 14 + 6.
**Status:** COVERED and richer (490 lines/98 Q; Sk, apparent activity, Γ 8.25, point A/B, Manchester, written directive, leak tests, source-exchange QA, permanent implant total dose all present). **Missing:** Quimby and Paris systems by name; radium needle linear-intensity specs (0.66/0.33 mg/cm) and active vs physical length; intravascular brachytherapy (15–20 Gy for restenosis); intraluminal (esophagus/bronchus) applicators; DOT transport label categories and the transport index; Sr-90/Y-90 eye applicators (present only as an isotope in m03); electronic brachytherapy (~50 kV); accelerated partial-breast balloon/multi-lumen 34 Gy/10 fx BID.

### Radiation protection → m41
**Teaches:** stochastic vs deterministic, acute radiation syndromes (hematopoietic 2–3 Gy, GI 5–12 Gy, CNS > 12 Gy), LD50/60 ≈ 3–4 Gy, background ~3 mSv (quiz says ~6 mSv incl. medical, NCRP 160), NCRP 116 table (50 mSv/yr; 150 lens; 500 skin/extremity; cumulative 10 mSv × age; public 1 mSv continuous/5 mSv infrequent; students 1 mSv; embryo 5 mSv total/0.5 mSv per month; NIRL 0.01 mSv), badges, declared pregnancy, NRC/10 CFR 35, medical event criteria (20 % total dose or 50 % fraction; 0.05 Sv effective/0.5 Sv organ), controlled 0.1 mSv/wk vs uncontrolled 0.02 mSv/wk, W·U·T, neutrons above 10 MV, IMRT leakage multiplier.
**Quiz:** 17.
**Status:** COVERED for limits, barriers, signs, ALARA, NRC roles, pregnancy. **Missing:** ARS dose bands and LD50/60; NCRP 160 (6.2 mSv) as the background figure; medical-event criteria in m41 (they live in m40/m42—cross-reference); "infrequent public 5 mSv"; film-badge construction/filters.

### QA / standard of care → m42
**Teaches:** TPS commissioning, TG-40 tolerance table (daily output 3 %/lasers 2 mm; monthly 2 %; annual 2 %, isocenter 2 mm), weekly chart checks, R&V (MOSAIQ/ARIA), two patient identifiers, medical events, picket fence, Winston-Lutz, star shot, AAMD scope, detector zoo (free-air, thimble/Farmer 0.6 cc, parallel-plate for electrons ≤ ~10 MeV, diodes, film, TLD, OSLD, GM), well-chamber 2-year calibration, TG-176, FMEA/RPN, RO-ILS, near miss, Swiss-cheese model, TG-66 CT-sim table (water 0 ± 5 HU, 1 mm geometry), CBCT daily/monthly.
**Quiz:** 13 + 16.
**Status:** COVERED and richer (389 lines/106 Q; TG-142, TG-100, RO-ILS, FMEA, TG-66, Winston-Lutz, picket fence, detectors). **Missing:** star-shot test; "two patient identifiers" as a safety rule; Swiss-cheese model by name; parallel-plate chamber in m42 (only m09); TG-176 (only m16).
**Flags:** course quiz keys "annual output accuracy 5 %" (TG-142: 1 %); TG-40 table is superseded by TG-142 (daily 3 %, monthly 2 %, annual 1 %).

### QUANTEC and densities → m43
**Teaches:** QUANTEC table (brain, brainstem 54/59, optics 55, cord 50/60/69, cochlea 45, parotid mean 25/39 or 20, constrictors 50, larynx 66/44/V50 < 27 %, lung V20 ≤ 30 %/mean 7–27, esophagus mean < 34, heart V25 < 10 %, pericardium mean 26/V30 < 46 %, liver 30–32/42/28/36, kidney 15–18/28/V12 < 55 %…, stomach D100 < 45, bladder 65/V65 < 50 %/V70 < 35 %, rectum V50–V75, penile bulb), SRS limits (brain V12 < 5–10 cc, brainstem 12.5, optics 12, cord 13/20, cochlea 14), densities (lung 0.3, fat 0.91, muscle/blood 1.05, bone 1.65).
**Quiz:** 4.
**Status:** COVERED (164 lines/55 Q; every value above is present except brain V12 < 5–10 cc for single-fraction SRS).

### Practice tests → m44 — separate documents (reviewed in `capstone-calcs.md`/`textbook-part2.md`).

### Bonus → m45
**Teaches:** six mixed calcs, clinical-trial phases, binary conversion, a 50-item "radiation therapy concepts" quiz.
**Status:** COVERED (m45 has trial phases, binary, 32 Q).

---

## Course errors / outdated items worth knowing

1. Fetal limit printed as "10 Gy" (should be ~10 cGy / 0.1 Gy). 2. "145 Gy I-131" prostate monotherapy (I-125). 3. Penile cancer section repeats the testis text. 4. "MV has better soft-tissue contrast than kV" (reversed). 5. TG-40 cited for respiratory-gating QA (TG-76/TG-142). 6. Lead-HVL quiz item keyed to one option while the explanation computes a different one. 7. ICRP-60 neutron weighting steps; TG-34 for pacemakers (TG-203); TG-40 QA table (TG-142). 8. "< 12 MV for lung" (≤ 10 MV, prefer 6). 9. "1024×1024 CT matrix" (512). 10. Prostate seed table labelled HDR though it is LDR, and the Pd-103 boost value (90 Gy) differs from the ABS 100 Gy convention. 11. Background 3 mSv in lesson vs ~6 mSv in quiz (NCRP 160: 6.2 incl. medical). 12. QA quiz keys annual output tolerance 5 % (1 %). 13. Ra-226 average photon energy given as 883 keV (usually quoted ~830 keV). 14. "1 Gy = 100 R" stated as an identity. 15. Proton weighting factor ambiguity (listed as a range).

---

## The "Picture Day" pptx

A bootcamp slide deck (~122 slides) of equipment and detector photographs with short bullet captions—no narrative text. Topics: linac subsystems (modulator/PFN/thyratron, 50–1000 pps, 2–5 µs pulses, magnetron vs klystron, SF₆ waveguides, traveling vs standing wave, 270° achromatic/slalom magnets, flattening filter materials, MLC transmission figures), beam data (6X vs 18X penumbra ~7 vs 8 mm; electron rules E₀ = 2.4·R₅₀, old vs new R₈₀/R₉₀ rules; mean photon energy ≈ ⅓ nominal; FFF PDD(10) ~67 → 61 % at 6X and ~80 → 73 % at 18X), brachy hardware (Cs-137 tubes, Ir-192 HDR source, Sr-90/Y-90 pterygium applicator, I-125/Pd-103/Cs-131 seeds, balloon and multi-lumen APBI with 34 Gy/10 fx and the 1 cm PTV_eval minus 5 mm skin rule, T&O and cylinder prescriptions, Freiburg flap, electronic brachy ~50 kV), imaging (CT overestimates prostate ~30 % vs MRI; T1/T2/Gd; PET SUV; fusion), DVH examples, and radiation-safety hardware (posting thresholds: Radiation Area 5 mrem/h or 100 mrem in 5 days, High Radiation Area 100 mrem/h at 30 cm; RAM labels; GM ~3300 cpm per mR/h; rem-ball; badge/TLD/OSL ranges; Farmer 0.6 cc ≈ 0.2 nC/cGy; micro-chamber 0.009 cc; parallel-plate 0.06 cc; re-entrant chamber ~245 cc with 2-year calibration; dose-calibrator QA; diode arrays; radiochromic film 0.02–8 Gy read at ~660 nm; TLD glow curve; H&D curve; gas-detector regions).

**Usefulness:** moderate as a checklist of hardware numbers, low as a teaching source (the slides are captions for pictures we cannot see). The numeric items worth harvesting (FFF PDD(10) shift, 6X/18X penumbra, detector volumes and sensitivities, APBI 34 Gy/10 fx, posting thresholds, GM calibration) are listed in the top-20 below where they also appear in the course. Our bank already has the posting thresholds (m41) and most detector types (m09/m42); it lacks the specific chamber volumes/sensitivities, the FFF PDD values and the APBI prescription.

---

## Summary

### Estimated coverage
Weighting each lesson by its quiz-item count (≈ 480 items incl. mini-quizzes), about **82–85 %** of the DoseGrid course's testable content is already in our bank at equal or greater depth. The residual is concentrated in four places: clinical-oncology trivia (m20), imaging-device vocabulary (m10/m15/m18), named brachytherapy systems/transport labels (m40), and a handful of rules-of-thumb numbers (m24, m37, m39).

### Top 20 MISSING facts worth adding (grouped by module)

**m02 Fundamentals**
1. Mass defect/binding energy per nucleon; electron ≈ 1/1836 proton mass; electrons per gram = N_A·Z/A (hydrogen-rich tissue has more electrons per gram than bone).

**m05 / m06 Characteristics & interactions**
2. 1 eV = 1.6×10⁻¹⁹ J; EM-spectrum order; photodisintegration named as the fifth interaction (threshold ~8–10 MeV, source of neutrons).
3. Planck relation E = hν with h = 6.63×10⁻³⁴ J·s and one worked frequency/wavelength example.

**m07 Treatment machines**
4. Traveling vs standing-wave guides (standing wave shorter, needs a circulator/isolator); flattening filter removes up to ~90 % of central fluence; gun current higher in photon mode and at lower photon energy.

**m10 Imaging**
5. MRI TR/TE → weighting table (short/short T1; long/long T2; long TR/short TE proton density), Larmor precession, 1.5–3 T.
6. CT overestimates prostate volume ~30 % relative to MRI; standard 512×512 matrix; PET effective dose ~1–4 cGy with the bladder wall highest; ultrasound 1–20 MHz.

**m15 / m18 Motion & IGRT**
7. ≥ 5 mm respiratory excursion as the TG-76 threshold for motion management; prospective vs retrospective gating/binning.
8. CBCT vocabulary: filtered back-projection, half-fan with bowtie filter for large FOV, flat-panel detector; ExacTrac and TRUS as named systems.

**m20 Oncology (clinical trivia block)**
9. H&N sub-sites: Ohngren's line (maxillary sinus prognosis), retromolar trigone, floor of mouth/oral tongue drainage to levels I–II; HPV-positive oropharynx has better prognosis.
10. Hodgkin subtypes (nodular sclerosis most common), B symptoms, Reed-Sternberg cell; SVC syndrome as an oncologic emergency.
11. Breast: invasive ductal most common histology, BRCA1/2; esophagus ~25 cm long, Barrett's → adenocarcinoma in lower third, squamous in upper/middle; pancreas uncinate process/Whipple.
12. Seminoma hockey-stick (dog-leg) para-aortic + ipsilateral iliac field ~20–25 Gy; bone/soft-tissue sarcoma histology (Ewing t(11;22), osteosarcoma teen peak, myeloma).

**m21 Radiobiology**
13. Bergonié–Tribondeau law by name; cumulative cord BED (α/β 3) re-irradiation worked example with a ~150 Gy₃ ceiling.

**m23 Delivery systems**
14. Jaw tracking (reduces MLC leakage); optimizer families—gradient descent vs simulated annealing vs direct aperture optimization; VMAT uses fewer MU than fixed-field IMRT.

**m24 Special procedures**
15. TBI numbers: 5–10 cGy/min midplane dose rate, ±10 % uniformity, in-vivo ±5 %, "< 35 cm separation at ≥ 3 m → 6 MV suffices"; SRS: TG-142 isocenter 1 mm (SRS) vs 2 mm, TG-101 grid ≤ 2 mm, prescribe to 50–80 % isodose.

**m25 Planning methods**
16. IMN wide/mini-tangent technique; off-cord oblique boost at ~45 Gy for AP/PA lung; surface dose rises with field size, tray and obliquity.

**m37 / m39 Inhomogeneity & uncertainty**
17. ~3.5 %/cm attenuation rule for 6 MV (less at higher energy); ICRU ±5 % overall accuracy goal with a quadrature budget (~5.6 % when components are summed).

**m40 Brachytherapy**
18. Paterson-Parker vs Quimby vs Paris systems (uniform vs non-uniform loading, where the dose is specified); radium needle linear intensity 0.66/0.33 mg/cm, active vs physical length.
19. DOT transport labels (White-I ≤ 0.5 mrem/h surface; Yellow-II ≤ 50 mrem/h, TI ≤ 1; Yellow-III > 50), intravascular (15–20 Gy) and intraluminal applications, Sr-90/Y-90 eye applicators, electronic brachytherapy ~50 kV, APBI balloon/multi-lumen 34 Gy/10 fx BID.

**m41 / m42 Protection & QA**
20. Acute radiation syndromes (hematopoietic 2–3 Gy, GI 5–12 Gy, CNS > 12 Gy), LD50/60 ≈ 3–4 Gy, NCRP 160 background 6.2 mSv; star-shot test, two-identifier rule, Swiss-cheese model, parallel-plate chamber for low-energy electrons, chamber specs (Farmer 0.6 cc ≈ 0.2 nC/cGy, micro 0.01 cc, re-entrant ~245 cc).

### Lessons where our bank is richer than the course
m03 Radioactivity (effective half-life, equilibrium math, many decay calcs), m19 electrons/protons/metrics (511 lines/75 Q), m21 Radiobiology (EQD2 depth), m24 TBI/TSEB technique narrative, m26 DICOM, m29/m30 autoplanning/autocontouring (course has essentially no quiz), m31 implanted devices (TG-203 vs the course's TG-34), m33 inverse square (63 Q), m35 MU calcs, m36 special calcs (123 Q vs the course's ~22), m40 brachytherapy (Sk, TG-43 vocabulary, written directive, QA), m42 QA (TG-142/TG-100/RO-ILS vs the course's TG-40), m43 QUANTEC (full table with SRS limits), and the regimen side of m20 (SIB math, prostate bed, bladder preservation, pediatrics, gyn, SBRT).

### Verdict
**Complementary, with our bank ahead overall.** The DoseGrid course is a slide-style survey: broad, memorisable, light on calculation depth, and carrying a dozen factual or outdated errors (listed above). Our bank is deeper in every calculation module, in QA/protection/brachy regulation, and in dose-regimen recognition. The course is better only at (a) clinical-oncology background facts, (b) imaging and IGRT device vocabulary, and (c) a set of rules-of-thumb numbers it repeats across lessons (3.5 %/cm, 5 mm motion, 5–10 cGy/min TBI, 50–80 % SRS isodose, ±5 % accuracy). Adding the 20 items above would close essentially all of the residual gap; none of them requires copying course wording. The pptx adds nothing beyond a few detector/FFF numbers already folded into item 20.
