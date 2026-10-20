# Review of Medical Dosimetry (Amestoy, Springer 2015) — part 2 coverage report

Scope: the book from the page-441 marker to the end (Ch. 6 §6.5 onward through Ch. 14 and the reference list). Source text lives in the gitignored `inbox/` folder and is copyrighted; this report paraphrases and lists values only. Coverage was judged by grepping `knowledge/theory/` and `knowledge/questions/` for the book's key terms and numbers.

Book structure in this range: every chapter is a Q&A review. Questions are numbered, many use the old "I, II, III, IV → pick the combination letter" format, and the answer key (often with a one-line rationale) follows each question block. Three 155-item practice tests close the book.

Classification key: **COVERED** = our bank states the same facts and tests them; **PARTIAL** = topic present but the book has facts/numbers we lack; **MISSING** = topic absent from the bank.

---

## Ch. 6 (tail), §6.5–6.14 — Radiobiology quizzes

**Covers:** survival-curve parameters, α/β and BED arithmetic, OER/LET, cell-cycle timing, chemo–radiation interactions, hyperthermia, acute radiation syndromes, fetal effects, Emami TD5/5 tolerance table, cell-type radiosensitivity classes.

**Classification:** PARTIAL. Our m21 has D0/Dq/n, LQ, α/β, BED/EQD2 (16+ files), OER, the four Rs, cell-cycle sensitivity. Missing almost everything in whole-body effects, fetal windows, tolerance-dose tables, and chemo/hyperthermia modifiers.

**Facts the book has and we lack:**
- D10 = 2.3 × D0 (D0 of 5 Gy → 11.5 Gy per decade of kill). The bank mentions D10 in 6 files but never the 2.3 factor with a worked value.
- Cell-cycle durations: whole cycle 10–20 h; S 6–8 h; G2 2–4 h; G1 ~8 h (most variable); M < 1 h.
- About two-thirds of low-LET damage is indirect (OH· radical); high-LET damage is mostly direct.
- OER by radiation: x-rays 2–3.5, neutrons ~1.5, alpha ~1; OER falls as LET rises (we state this qualitatively but have no neutron/alpha values).
- Minimum interfraction interval > 6 h; RTOG hyperfractionation data showed worse late effects with intervals < 4 h.
- Drug–RT modifiers: hydroxyurea synchronizes cells in late G1/S boundary; methotrexate inhibits repair; fludarabine slows the cycle; cisplatin kills radioresistant cells. Radioprotectors (amifostine) must be given within ~30 min of RT.
- Hyperthermia: 42–45 °C, S-phase and hypoxic cells are heat-sensitive (complementary to RT), CEM43 concept.
- Acute radiation syndromes: 1–10 Gy hematopoietic (death 3–8 weeks, bone-marrow transplant useful 8–10 Gy), 10–100 Gy GI (death 3–10 days), > 100 Gy CNS (death 24–48 h). LD50/60 for humans 3–4 Gy without support.
- Fetal stages: preimplantation days 1–10 (all-or-none), organogenesis days 11–42 (malformations), fetal growth day 43 onward (CNS/growth retardation). Modern threshold: fetal dose below 100 mGy is not grounds for termination.
- Emami TD5/5 (whole organ unless noted): liver 30, stomach 50, whole brain 45, kidney 23 (book prints 50 — see errors), lung 17.5 (TD50/5 24.5), lens 10 (TD50 18), testes 1–2 (sterility), ovaries 2–3 (TD50 6–12), bladder 65, rectum 60 (TD50 80), ureter 70, oral mucosa 60 (TD50 75), small intestine 40 (TD50 55), spinal cord 47 (20 cm). Our m43 is QUANTEC-only; no Emami numbers at all.
- Radiosensitivity classes (Rubin–Casarett): VIM (stem cells, most sensitive) → DIM → multipotential connective → RPM → FPM (neurons, muscle; least sensitive).
- Bergonié–Tribondeau law named.
- Dose perspective: a chest x-ray ~0.1 mSv vs US background 6.2 mSv/yr → about 6 days of background.

**Wrong / outdated:**
- BED example for 70 × 1.2 Gy uses a total of 86.4 Gy instead of 84 Gy; the printed BEDs (96.8 Gy10, 121 Gy3) should be ≈ 94.1 and 117.6.
- Kidney TD5/5 printed as 50 Gy; Emami is 23 Gy whole-organ.
- Cataract threshold stated as ~10 Gy fractionated / 2 Gy single. ICRP 2011 put the threshold at ~0.5 Gy.
- "Hyperfractionation" is used loosely for 1.5–3 Gy/fx conventional schedules in one item.
- Abortion-consideration threshold given as > 10 cGy in one place and 100 mGy elsewhere (inconsistent; 100 mGy is current).
- Typo labelling the quasithreshold dose as D0.

**Questions:** ~45 items. Format: definition recall + a few BED/OER/D10 arithmetic items. Our m21 quiz has similar LQ/BED calculations; we have nothing on syndromes, fetal windows, or TD5/5 recall.

---

## Ch. 7 — Radiation Safety

**Covers:** dose-equivalent quantities and quality factors, NCRP/NRC/agreement-state roles, occupational and public limits, ALARA/investigational levels, HDR and teletherapy license requirements (QMP), source leak tests and storage, patient release, radiopharmaceutical safety (I-131, Y-90), NCRP 151 shielding (P, W, U, T, TVL, neutrons, mazes), DOT shipping (TI, A1/A2, package types, labels), and detector physics (GM, proportional, ion chamber, OSL/TLD, MOSFET, bubble, neutron detectors).

**Classification:** PARTIAL. m41 covers NCRP 116 limits (correctly, including the public lens 15 mSv), the 10 mSv × age guidance, declared pregnancy, ALARA, badges, workload/use/occupancy, TVL, photoneutrons, and a medical-event item. The regulatory-procedure half (QMP details, leak-test numbers, release criteria, shipping) and detector-physics details are thin or absent.

**Facts the book has and we lack:**
- Quality factors: photons/electrons 1; thermal neutrons 5; fast neutrons, protons, alpha 20 (we have "radiation weighting" in 6 files; thermal-neutron 5 is present, alpha/fast-neutron 20 appears but not as a table).
- Radon ≈ 24 mSv/yr equivalent dose to bronchial epithelium; largest natural-background contributor.
- ALARA investigational level I ≈ 10% of the annual limit (5 mSv), level II ≈ 30%. m41 deliberately leaves these unquantified.
- HDR licence (10 CFR 35): written directive, two independent patient identifiers, physician and physicist physically present during treatment, daily pre-treatment checks, records kept 3 years, annual QMP review (expand to a full year if a medical event is found), QMP changes reported to NRC within 30 days.
- Teletherapy: full calibration if a spot check differs > 5% or after source change, otherwise annually; monthly spot checks; head leakage ≤ 2 mrem/h average and 10 mrem/h maximum at 1 m with beam off; full inspection/servicing at ≤ 5-year intervals.
- Sealed-source leak test: ≤ 0.005 µCi (185 Bq) removable, every 6 months; storage areas surveyed weekly; radium sources also tested by immersion. Our bank has "leak test" in 4 files and the 185 Bq value in 2, but not the interval or survey cadence.
- Visitor rules for brachy inpatients: ≥ 6 ft from the bed, over 18, no pregnant visitors, time-limited.
- Decay-in-storage: hold ≥ 10 half-lives, survey at background, deface labels, then ordinary waste.
- Thyroid bioassay within 72 h after handling volatile I-131 (NaI probe).
- HDR unit leakage limit: ≤ 1 mR/h at 10 cm with source shielded (Test III item).
- NCRP 151 shielding goals: P = 0.1 mSv/week controlled, 0.02 mSv/week uncontrolled; B = P d² / (W U T); scatter term scales with (F/400)/a; leakage taken as 0.1% of primary; U = 1/4 per wall; T = 1 (offices), 1/4 (corridors), 1/8–1/16 (restrooms), 1/40 (closets). Densities: concrete 2.35, steel 7.8, lead 11.3, polyethylene 0.9 g/cm³. Neutron production above ~10 MV; borated-polyethylene door; maze > 5 m; neutron TVL in air ≈ 4–5 m along a maze. IMRT raises leakage workload 3–5× (≈ one extra HVL on secondary barriers). m41 has the primary-barrier formula and TVL, but no P values, T table, IMRT factor, or maze/neutron numbers.
- Rule of thumb: ~3 TVLs for a wall meeting ALARA investigational level I (Test II item).
- PET/CT rooms: 511 keV; typical 2.5 cm (1 in) lead equivalent walls; ~15% of the injected dose is voided; PET patient at 1 m is ~50 µSv/h early.
- DOT (49 CFR): Transport Index = mrem/h at 1 m (range 1–10 on labels; passenger aircraft ≤ 3 per package). Labels: White-I (< 0.5 mrem/h surface), Yellow-II (TI ≤ 1), Yellow-III (TI ≤ 10). Package classes: strong-tight < 0.001 A1 (limited quantity), Type A up to 1 A1, Type B 1–3000 A1; no Type C. A1 values: Ir-192 27 Ci, I-125 540 Ci, Co-60 10.8 Ci. A Gamma Knife reload (~6600 Ci Co-60) requires Type B. Our bank has zero on TI, labels, or A1.
- Detectors: GM dead time ~100–300 µs and saturation in pulsed linac beams; ion chamber plateau ~300 V, GM region ~1000 V; proportional counters with BF3/10B or 3He for neutrons; bubble detectors (superheated drops, reset by recompression); OSL (Al2O3:C, re-readable); LiF TLD glow peaks 4–5 used for dose; MOSFET threshold-voltage shift; well chamber for brachy strength; G value = molecules per 100 eV. m09/m42 cover chamber vs diode vs TLD vs survey meter functionally; proportional, well, MOSFET, bubble and dead-time details are absent.
- Patient release from radiopharmaceutical therapy: current NRC criterion is ≤ 5 mSv TEDE to any other individual (NUREG-1556 tables); book still quotes the pre-1997 30 mCi / 5 mrem/h-at-1-m rule.

**Wrong / outdated:**
- Public lens limit stated as 50 mSv (NCRP 116: 15 mSv).
- Patient release stated as < 5 mrem/h at 1 m (pre-1997; now 5 mSv TEDE to others).
- "I-131 and P-32 treat thyroid cancer" — P-32 is wrong (Test II/III items correctly key I-131 alone).
- Badge exchange stated monthly in one item and ≤ 3 months in another; Test III key says OSL every 2 months. No consistent cadence; monthly or quarterly is the normal practice.
- Occupational lens 150 mSv is the NCRP 116 figure; the book never mentions the ICRP 20 mSv/yr revision. (m41 handles this distinction well.)
- NRC "misadministration" terminology used; the regulatory term since 2002 is "medical event."

**Questions:** ≈ 190 items across nine quizzes — the largest Q bank of any chapter. Mostly limit recall and regulatory procedure, ~15 shielding/TI/decay calculations. Our m41 quiz has barrier-transmission and limit items but nothing on shipping, licence procedure, or detector regions.

---

## Ch. 8 — Quality Assurance

**Covers:** accreditation (JCAHO), staffing ratios, acceptance vs commissioning, TG-40/142/51 tolerances, mechanical tests (star shot, light/radiation coincidence, ODI, couch sag), beam tests (flatness/symmetry/energy), daily/monthly/annual cadence, simulator and CT-sim QA, brachy source calibration, chamber calibration intervals, Ptp correction, IMRT QA (gamma, Las Vegas, picket fence).

**Classification:** PARTIAL (closer to COVERED on linac tolerances). m42 has TG-142 cadence and tolerances, picket fence, Winston–Lutz, gamma, CT-sim HU/laser constancy, detector-selection logic, Ptp. Missing: historical/organizational facts, staffing, several specific tests and intervals.

**Facts the book has and we lack:**
- ISCRO "Blue Book" staffing: 1 dosimetrist per 300 patients/yr, 1 physicist per 400, 1 radiation oncologist per 200–250.
- Acceptance testing is the vendor-contract step (specs written by the physicist); commissioning generates clinical beam data for the TPS.
- Star-shot tests for collimator, gantry, and couch isocentricity; isocenter sphere ≤ 1 mm radius for SRS, 2 mm otherwise (m42 has the number but not the test name).
- Split-field (half-beam) junction test for asymmetric jaws.
- Light/radiation coincidence ±2 mm or 1% of field side (m42 lists 2 mm only).
- Energy constancy via PDD at 10 cm, 10 × 10, 100 SSD, ±1%; chamber diameter < 3 mm for profile scans.
- Flatness checked at maximum field size, 10 cm depth and dmax, principal axes and diagonals. TG-40 historical tolerances: flatness 3%, symmetry 2% at 10 cm; TG-142 uses 1% from baseline.
- Co-60 output constancy monthly ±2%; electron energies checked ≥ 2×/week when photons are daily (older TG-40 practice).
- Simulator: tube leakage ≤ 0.1 R/h at 1 m, kVp ±5%, mA linearity.
- Ion chamber and electrometer recalibrated at an ADCL every 2 years; survey meters annually.
- Brachy: a vendor-supplied I-125 calibration may be accepted if within 5% of the user's; well chamber should be calibrated with the same isotope; disagreement > 5% triggers vendor recalibration.
- Las Vegas phantom for EPID contrast/resolution.
- MU linearity and interrupted-delivery (beam-hold) tests.
- "Golden" beam data acceptable if within ~2% of measured.
- History: the roentgen was adopted in 1928; free-air chamber is the primary standard below ~3 MeV; parallel-plate chambers recommended < 10 MeV and required < 6 MeV for electrons.
- Ctp worked value: 22 °C and 750 mmHg → 1.0133.

**Wrong / outdated:**
- Ctp formula printed without the inner parentheses (looks like 273 + t/295).
- Answer numbering in §8.6 is offset by one (answers 5–14 vs questions 4–13); §8.7 has two "9"s.
- "JCAHO" (now The Joint Commission); TG-40 cited as the current standard alongside TG-142.
- Daily output tolerance 3% and monthly 2% match TG-142; the book's 1% flatness/symmetry is TG-142 but is presented next to TG-40's 3%/2% without distinguishing them.

**Questions:** ≈ 100 items; recall of tolerances/intervals plus a handful of Ctp and gamma items. Our m42 quiz tests tolerance recall and instrument choice similarly; no staffing, interval-of-calibration, or test-name items.

---

## Ch. 9 — Computer Basics

**Covers:** bits/bytes, storage units, image matrix sizes and bit depth per modality, file-size arithmetic, PACS, networking terms (TCP/IP, FTP, SQL, DSL, router, LAN).

**Classification:** PARTIAL. m27 has bytes/kilobyte (1024), PACS, ASCII, 12-bit/4096 once, 512 matrix once, DICOM thoroughly.

**Facts the book has and we lack:**
- Matrix/bit depth table: CT 512 × 512 × 12-bit (2 bytes/pixel, ~0.5 MB/slice, 100 slices ≈ 50 MB); MRI 256 × 256; nuclear medicine 128 × 128; digital radiography 2048 × 2048 ≈ 8 MB; ultrasound 8-bit.
- Byte ladder: KB = 1,024, MB = 1,048,576, GB = 1,073,741,824.
- Binary conversion (12 = 1100), ASCII 256 codes, TCP/IP, FTP, SQL, DSL, router as LAN hub.

**Wrong:** the answer text for the binary-conversion item computes 11 instead of 12.

**Questions:** 38 items, definitional. m27 mini-quiz is comparable in style; the book is heavier on raw IT vocabulary than the current exam.

---

## Ch. 10 — Professional Issues, Ethics, Law, MDCB

**Covers:** ethics principles and practitioner–patient models, informed consent, negligence and intentional torts, legal doctrines, incident reports, chart corrections, HIPAA, patient rights, living wills, AAMD and MDCB structure, certification eligibility, CE requirements, scope of practice, performance standards, CARE bill, professional organizations.

**Classification:** MISSING (except scope of practice and incident reporting). The bank has zero hits for beneficence, autonomy, informed consent, negligence, malpractice, HIPAA (PHI appears 10× but only as a DICOM/record concept), living will, or JRCERT. m42 covers AAMD scope of practice and RO-ILS/medical-event reporting.

**Facts the book has and we lack:**
- Ethics principles: beneficence, nonmaleficence, autonomy, justice, veracity, fidelity, confidentiality.
- Veatch models: engineering, priestly (paternal), collegial, contractual, covenant; "analytical" as the reasoning method.
- Informed consent elements; competency age 18; consent may be withdrawn.
- Negligence: duty, breach, causation, damages (4 elements). Intentional torts: battery (touching without consent), assault (threat), false imprisonment (restraint without order), defamation (libel written, slander spoken), invasion of privacy.
- Doctrines: res ipsa loquitur, respondeat superior, standard of care, statute of limitations.
- Incident reports are not part of the chart; corrections are single-line strike-through, initialled and dated, never obliterated.
- HIPAA (1996): civil penalties $100–$50,000 per violation, $1.5 M annual cap; criminal up to $250,000 and 10 years.
- Living will / durable power of attorney / DNR distinctions.
- AAMD: board with six regional directors; MDCB mission and exam ownership; Scope of Practice adopted March 13, 2001; performance standards in professional, quality, and clinical domains.
- CE: 50 credits per 5-year cycle (the bank mentions CE in 2 files; confirm the current MDCB figure is stated).

**Wrong / outdated:**
- MDCB eligibility routes I–III (RT(T) + experience, bachelor's + OJT) — since 2017 the only route is graduation from a JRCERT-accredited dosimetry program.
- CARE bill presented as pending; never enacted.
- ACMP listed as a current organization (merged into AAPM, 2013). JCAHO (now TJC) and ASTRO name used in its old form.
- "Misadministration" vs "medical event" as above.

**Questions:** 49 items, pure recall. Our bank has none of this question type. The exam blueprint gives professional/ethics a small weight, so this is a low-cost, low-yield gap.

---

## Ch. 11 — Radiation Oncology by Site

**Covers:** CNS (gliomas, meningioma, pituitary, pineal, medulloblastoma/CSI), head and neck subsites, eye, salivary, thyroid, breast, thorax (esophagus, lung, thymoma, lymphoma), abdomen (pancreas, stomach, liver, kidney), pelvis (bladder, prostate, testis, penis, gyn sites, rectum, anus), spine, pediatrics, hematologic, benign disease, skin, sarcoma, lab values for contrast.

**Classification:** PARTIAL. m20 covers regimens, intent, and planning problems for the major sites (brain, H&N, breast, lung, prostate, rectum, cervix, etc.) and m22 covers anatomy and nodal levels. The book's epidemiology/percentage facts, classic field borders, and the less common sites (eye, pediatric solid tumors, benign disease, myeloma, sarcoma) are largely absent.

**Facts the book has and we lack (selected, with values):**
- CNS: gliomas ~50% of primary brain tumors, meningioma ~20%, pituitary ~15%; CSI junction feathered every ~10 Gy; lower spine border S2–S3 (thecal sac); pineal region ~1 cm posterior and 3 cm superior to the EAM; pituitary wedged pair with heels anterior.
- H&N: hypopharynx subsites — pyriform sinus ~65%, postcricoid ~20%, posterior wall ~15%; doses RT alone 65–70 Gy, postop 60–66 Gy, preop 45–50 Gy. Subglottis begins ~5 mm below the cords; T1 glottic fields 4 × 4 to 6 × 6 cm from thyroid notch to cricoid. Nasal cavity/sinus tumors are bimodal (10–20, 50–60 yr), M:F 2:1. Nasopharynx: ~90% epidermoid/undifferentiated; bone is the commonest distant site. Oral cavity LDR 4.5–5 Gy/h (historic); allow 8–10 days after dental extraction. Xerostomia in ~75% of conventional H&N courses. Thyroid cancer ~1–1.5% of all cancers.
- Eye: uveal melanoma enucleated if > 15 mm diameter or > 10 mm thick (COMS plaque otherwise); retinoblastoma — Reese–Ellsworth grouping, I-125 plaques, ~40% hereditary, one-third bilateral.
- Breast: quadrant distribution UOQ ~48%, UIQ ~15%, LOQ ~11%, LIQ ~6%, central ~17%; IDC > 80%; BRCA1 on 17q21, BRCA2 on 13q12-13. Classic tangent borders: superior at the clavicular head, inferior 2–3 cm below the inframammary fold, medial 1 cm across midline, lateral 2 cm beyond palpable tissue. SCV field prescribed at 3 cm depth, 45–50 Gy, gantry angled 10–15° to spare the cord; PAB calculated 2 cm below mid-clavicle; monoisocentric match is the common technique. IMN coverage considered for inner-quadrant/central primaries with positive nodes. (m20 has breast dose regimens and SCV/PAB appear in 15 and 4 files; the quadrant/BRCA/border numbers are absent.)
- Thorax: esophagus ~25 cm long, C7–T11; AJCC regions cervical (C7–T2 / 15–18 cm from incisors), upper T3–T4, middle T5–T8, lower T9–T11; SCC favours the middle third (40–50%), adenocarcinoma arises from Barrett's distally; carina at T5. Lung: cough ~75%, hemoptysis ~57%, smoking in ~85%; SVC syndrome 80% from bronchogenic carcinoma. Thymoma ~20% of mediastinal masses.
- Abdomen: pancreas at L1–L2, head 75%, adenocarcinoma 80%; head fields include the duodenal loop and about half the right kidney, body/tail fields spare two-thirds of the left kidney. Gastric cancer 90–95% adenocarcinoma. Kidneys from the 11th rib to L3, move up to 4 cm with breathing, right lower; left-kidney drainage goes to para-aortics; RCC metastasizes to lung 75%. Ureter tumours favour the distal third.
- Pelvis: anal canal 3–4 cm, SCC ~80%; rectum ~15 cm from S3 with three valves; bladder TCC ~92%, smoking in 30–40%; penile SCC; testis lymphatics cross right→left; germ-cell tumours 95%, ages 15–35; endometrial is the commonest gyn cancer, bleeding 70–80% presenting; ovarian epithelial 85–90%; cervix SCC ~90%, lung mets ~21%, para-aortic nodes ~11% (early stage), FIGO staging, Point A definition, tandem/ovoid or ring, longest tandem and largest ovoids that fit; vagina — posterior upper third commonest, epidermoid 90%, LDR 75–80 Gy total.
- Spine/CNS palliation: 31 nerve-pair levels, cord ends L1–L2, fields 2 vertebral bodies above and below, width 4–8 cm.
- Lymphoma: Hodgkin — cervical presentation > 80%, mediastinal ~50%, Ann Arbor staging, nodular sclerosis commonest, B symptoms, mantle/inverted-Y/Waldeyer field definitions and blocks (m20 mentions mantle/inverted-Y in 6 files; Ann Arbor absent).
- Pediatrics: neuroblastoma adrenal 30–40%, > 70% metastatic at diagnosis; Wilms — lung mets, RT within ~10 days of nephrectomy; osteosarcoma distal femur/proximal tibia, Enneking staging; Ewing femur diaphysis, pelvic primaries worst; ALL commonest pediatric malignancy; AML > 40 yr; CLL > 50 yr (Rai/Binet); low-grade glioma ~40% of pediatric CNS; medulloblastoma CSI + posterior fossa boost.
- Myeloma: bone pain ~68%, hypercalcemia ~50%, hemibody RT relieves pain in 80–90% within 48 h; commonest primary bone malignancy in adults.
- Benign: keloid RT within 24 h of excision (~12–15 Gy); heterotopic ossification after hip arthroplasty (~30% without prophylaxis) 7 Gy × 1 or 10 Gy in 4–5 fx within 72 h; pterygium beta plaque; plantar wart ~10 Gy; AVM radiosurgery; trigeminal neuralgia radiosurgery; Graves ophthalmopathy ~20 Gy/10.
- Skin: BCC > SCC in incidence; prescribe electrons to the 80–90% IDL; Kaposi margin 1.5–2 cm; eyelid lesions.
- Sarcoma: thigh commonest, lung mets, MFH/UPS historically ~40%.
- Contrast labs: BUN 10–20 mg/dL, creatinine 0.5–1.1 (F) / 0.6–1.2 (M) mg/dL; AFP for HCC. (m13/m16 have creatinine/BUN in 7 files; metformin hold and allergy prep absent.)

**Wrong / outdated:**
- "Larynx is the commonest H&N cancer" — oral cavity/oropharynx are now; HPV-oropharynx not mentioned.
- Eyelid BCC/SCC "RT is the treatment of choice" — surgery first in current practice.
- States the splenic flexure is attached to the liver and the hepatic flexure to the spleen (reversed).
- "Mediastinal lymphomas are in the middle compartment" — anterior is typical.
- Breast: axillary/SCV RT "for ≥ 2 positive nodes" and the adjuvant-chemo wording are garbled/outdated; LDR brachy for oral cavity and vagina reflects 1990s practice; no SBRT, no IMRT for H&N, no hypofractionated breast/prostate.
- Chemo lists (e.g., for testis/lymphoma) reflect 1990s regimens.

**Questions:** ≈ 250 items — heaviest chapter. Mostly epidemiology percentages, anatomy borders, and classic field definitions; almost no plan-evaluation or technique-choice items. Our m20 quiz asks regimen/intent/planning-problem items instead. The exam-readiness review already flagged site-technique depth as our biggest hole, so the book's border/landmark material is useful raw material even though its percentages are low-yield.

---

## Ch. 12 — Anatomy (CT slice labelling)

**Covers:** ~45 labelled axial CT images from skull base to pelvis; the text extract contains only the label lists (brainstem, cochlea, parotid, brachial plexus, IMN chain, aortic arch, pancreas head/body/tail, seminal vesicles, penile bulb, etc.).

**Classification:** cannot assess from text — the chapter is image-based. m22 has an anatomy list and nodal levels but the exam-readiness review already notes we have no unlabeled-slice items. The book's structure list is a useful checklist of which structures get labelled on an axial CT at each level (e.g., cochlea, brachial plexus, penile bulb) if the parent decides to add image items from an open dataset.

**Questions:** ~45 image items; none reproducible here.

---

## Ch. 13 — Imaging

**Covers:** CT principles (HU, FBP, kVp/mAs/slice/FOV trade-offs, DRR), MRI physics (Larmor, T1/T2, TR/TE, sequences, contrast agents, safety), ultrasound (frequency, impedance, piezoelectrics, speed of sound, modes), nuclear medicine (Te, gamma camera, collimators, common isotopes), PET (F-18, resolution limits, detectors).

**Classification:** PARTIAL. m10/m11 cover HU scale with calculation, CT acquisition parameters, T1 vs T2 "what is bright," FLAIR/DWI, pacemaker/MRI safety, ultrasound 1540 m/s with a worked depth calc, F-18 110 min, 511 keV coincidence, SUV caveats. Missing: MRI physics vocabulary, ultrasound engineering numbers, nuclear-medicine instrumentation, PET resolution physics.

**Facts the book has and we lack:**
- Spatial resolution by modality: CT and MRI ~1 mm; PET 3–7 mm; planar NM 5–10 mm. The eye distinguishes only ~30–90 gray levels, hence windowing.
- Tissue HU reference: fat ≈ −100, muscle +40 (35–50), lung ≈ −700, bone +1000 (m11 gives ranges; the book gives single anchor values and the H = 1000(μ−μw)/μw definition; m11 has the formula).
- CT acquisition: kVp 80–140 (120 typical); thinner slices raise noise and improve spatial resolution/reduce partial volume; mAs ↑ → noise ↓; FOV ↓ → pixel ↓; filtered back projection; tube-current modulation; flat couch and large bore for simulation.
- MRI: only nuclei with odd nucleon counts are MR-active; Larmor frequency ∝ B0 (≈ 42.6 MHz/T for ¹H); RF pulse applied perpendicular to B0; T1 (spin–lattice) > T2 (spin–spin); gradients for slice select, frequency and phase encode; spin-echo 90°–180°; T1W = short TR/short TE, T2W = long/long, PD = long TR/short TE; clinical 0.5–3 T (7 T research); gadolinium (T1-shortening), manganese and perfluorocarbon agents; contraindications (pacemaker, aneurysm clips, cochlear implants, ferromagnetic foreign bodies; pregnancy caution).
- Ultrasound: 1–20 MHz (higher frequency = better resolution, less penetration); Z = ρ·v; piezoelectric materials (PZT, barium titanate, lead metaniobate); attenuation ~0.5 dB/cm/MHz; speed 1540 m/s tissue, 330 air, 1450 fat, 4080 bone; A/B/M modes; convex probe gives a sector image.
- Nuclear medicine: Te = Tp·Tb/(Tp+Tb) (bank has it in 3 files); mean life 1.44 T½; Tc-99m in ~80% of studies; cyclotron nuclides Tl-201, Ga-67, I-123, In-111 vs generator Tc-99m; bladder is the hot organ on FDG/bone scans; parallel-hole/pinhole/converging collimators.
- PET: F-18 110 min from a cyclotron, positron end-point 0.63 MeV, ~2 mm range; uptake 40–60 min before scan; BGO/LSO/LYSO detectors; resolution limits = positron range, 180° non-colinearity (~0.25°), detector size; practical limit ~2 mm (micro-PET ~1 mm); CT-based attenuation correction.

**Wrong / outdated:** nothing substantive; "transverse tomography" and film-based DRR workflow are historic. One answer key prints air −100 / bone +100 (typo).

**Questions:** ≈ 100 items, mostly definitional with one or two HU/Te calculations. Our m10/m11 quizzes are calculation-heavier (HU from μ, US depth, F-18 decay) and lighter on MRI/NM vocabulary.

---

## Ch. 14 — Practice Tests I, II, III (+ answer keys)

**Covers:** three 155-item mixed tests mimicking the MDCB length. Content is ~70% recycled from the chapter quizzes; ~30% calculations; Tests II/III add CyberKnife/Gamma Knife/tomotherapy/Calypso/IMRT-optimization items and a handful of particle-physics items (quarks, neutrinos, mesons) that are off-blueprint.

**Classification:** PARTIAL on calculations (our m35/m36/m40/m44 cover the same families), MISSING on format and some topics.

**Calculation families present (book value → our status):**
- Equivalent square 20 × 14 → 16.5 (COVERED, m35).
- Electron MU with cutout output and IDL: 250/(1.07 × 0.9) → 260 MU (COVERED).
- Electron rules of thumb: Rp ≈ E/2 cm, R90 ≈ E/4 (Bentel) or E/3.2 (Khan), R50 ≈ E/2.33, lead cutout mm ≈ E/2, Cerrobend 20% thicker than lead (COVERED; m19 already distinguishes Khan vs Bentel; the R50 = E/2.33 rule is absent).
- Ctp 21 °C / 772 mmHg → 0.980; 22 °C / 750 → 1.013 (COVERED, m09/m42).
- HVL/attenuation: 15 mm with 2.5 mm HVL → 1.56%; μ = 0.693/HVL; 10 HVLs → (0.5)^10 (COVERED, m05/m06).
- Wedge: WF 0.35/0.70 = 0.5; MU 300/0.64 = 469; hinge angle = 180 − 2θ (45° wedges → 90°); wedge angle = 90 − hinge/2 (COVERED, m34).
- Inverse square: Co-60 120 × (80/100)² = 76.8; dose-rate change 100→120 cm = 0.694; ODI misread 100 vs 115 SSD → 250 × (100/115)² = 189 cGy (COVERED, m33; the ODI-error framing is a nice variant we lack).
- Parallel-opposed MU with tray: 100/(1.089 × 0.863 × 0.98) = 109 MU per field (COVERED).
- Weighted fields: 2:1 of 250 → 167/83; 3:2:1 of 200 → 100/67/33; 3:1 of 180 → 135/45 (COVERED).
- Mayneord F 110→120 SSD at 15 cm depth → +1.6% (COVERED, m35).
- Field size projection: 20 × 25 at 70 SSD → 27 × 34 at 95 SSD; 110 × 150 mm at 100 SSD → 179 × 245 mm at 63.5 cm depth; 1 cm bolus does not change the field at depth (COVERED, m08).
- Renormalization: 108% hot spot renormalized to 90% → 120% (COVERED, m19).
- Forgotten wedge: 244 MU at WF 0.82 → 222 cGy delivered (COVERED concept; m42 record-and-verify).
- TMR unchanged when SSD changes (COVERED trap, m35).
- Geometric penumbra 1.5 × (100−75)/75 = 0.5 cm (COVERED, m36).
- CSI collimator angle arctan(20/100) = 11.3°; couch angle for 20 cm field at 93 SSD; gap and skin-gap calcs (COVERED, m36).
- Lung equivalent path 1 cm tissue ≈ 3 cm lung; titanium hip EPL 5 + 3×(~1.5–2) + 7 (COVERED, m37).
- Exposure rate constant Ra-226 8.25; I-125 Γ 1.46 → mg-Ra-eq conversion (PARTIAL: Γ values present in 7 files; mg-Ra-eq-hr conversion absent).
- I-125 permanent implant removed early: 70 Gy prescribed, 78 days in, Tavg 85.7 d → D = 70(1 − e^(−78/85.7)) ≈ 41.9 Gy (PARTIAL: m40 has total-dose formula; "removed early" variant absent).
- Ir-192 temporary implant: 15 Gy at 0.6 Gy/h → 25 h (COVERED, m40).
- Ir-192 decay to 99.5% → 0.53 d; Au-198 15 mCi after 20 d → 0.09 mCi; Te 7 h & 14 h → 4.67 h; Ir-192 A1 shipping (COVERED except shipping).
- Arc MU: 180/0.570 = 316; arc time 150/(80.5 × 0.55) = 3.39 min (COVERED, m36).
- D10 = 2.3 × D0 (MISSING, see Ch. 6).
- Sievert-table line-source dose to a point from three sources (Test III Q129) → 60.3 cGy/h (MISSING: no Sievert/along-away table items in m40).
- Multi-source brachy "away/along" table and Fig-based DVH/isodose reading (MISSING in text form).

**Non-calculation topics in the tests that we lack:** CyberKnife specifics (80 cm SAD, 12 fixed cones 5–60 mm, Iris collimator, 45° orthogonal kV imagers, 6D skull / Xsight spine / fiducial / Synchrony tracking, 6-DOF robotic couch, node-and-path delivery, Monte Carlo/ray-trace planning, TG-135 daily QA); Gamma Knife (201 Co-60 sources, 4 helmets 4–18 mm, ~6600 Ci reload, 50% IDL prescription); tomotherapy ring gantry 6 MV; Calypso transponders; BAT ultrasound; IMRT optimization vocabulary (cost function, global minimum, simulated annealing, fluence → leaf sequencing → MU); SMLC/DMLC/IMAT delivery modes; typical normalization IDLs (GK 50%, CK 70%, IMRT 95%, VMAT 90%); IORT 10–20 Gy single fraction; low-dose TBI 10–15 cGy × 10–15; endorectal cone technique; klystron/magnetron/thyratron/circulator functions; microtron; electron scattering-power dependence (Z², 1/E²); bremsstrahlung tail source; ICRU dose-specification points and ±5% target uniformity goal; treated vs irradiated volume; Veatch/ethics items.

**Wrong / questionable in the tests:**
- Test III Q134: "dose to kill 90%" keyed as 115 Gy ("10 decades"); 90% kill is one decade → 11.5 Gy.
- Test III Q126: 30 mCi-min of I-125 → keyed 318.5 mg-Ra-eq-hr; minutes → hours should divide by 60 (≈ 0.088 mg-Ra-eq-hr), not multiply.
- Test II Q143: asks for Au-198 activity after 20 days using its "half-value layer 2.5" — means half-life 2.7 d.
- Test II Q105: MU formula multiplies the SAD output factor by BSF as well as TMR; with an SAD-calibrated output in phantom the BSF should not appear (keyed 162 instead of 167 MU).
- Test II Q54 key gives a factor of 0.986 while the keyed answer is a 1.6% increase (the answer letter is right, the rationale is not).
- Test I transmission item (2.5 cm of a 10-mm-HVL material) has no option near the correct ~18%.
- Test II Q2 / IIA key repeats the Ctp formula typo; Test III Q154 key prints air −100 / bone +100.
- Test III Q28 keys the thyratron's hydrogen as an "insulator"; the gas is there to be ionized and conduct.
- Test II Q39/Q128/Q131 are opinion-style items (reasons for hypofractionation's return, whether adaptive replanning fixes setup error, IMRT vs 3D-CRT outcomes) with debatable keys.
- Test III Q136 keys OSL exchange "every 2 months," conflicting with Ch. 7.
- Particle-physics items (quark interactions, neutrino flavours, meson composition, relativistic KE) are not on the MDCB blueprint.

**Questions:** 3 × 155 = 465 items with letter keys and sparse rationales. Our bank has ~280 practice-test items across m44 with full rationales. Format difference: the book's "I, II, III, IV" combination items (0 in our bank) and CyberKnife-heavy content are not representative of the current single-best-answer MDCB exam, but the rule-of-thumb and error-scenario calculations are close to exam style.

---

## Summary (10 lines)

1. **Book quality: 5/10.** Broad, exam-shaped Q&A with ~1,000 items, but written to 1990s–2000s practice, dense with typos, arithmetic slips, and keyed errors (≈ 20 found in this half), and padded with off-blueprint CyberKnife/particle-physics items.
2. **Already in our bank: ≈ 55–60%** of the content in this half — nearly all calculation families, TG-142/TG-51 tolerances, NCRP 116 limits, HU/PET/US basics, and major-site regimens; what's missing is mostly recall tables and regulatory procedure.
3. Weakest coverage in our bank vs the book: professional/ethics/law (essentially 0%), DOT shipping and licence procedure (~10%), Emami tolerances and whole-body/fetal radiobiology (~15%), site epidemiology and classic field borders (~30%), MRI/NM physics vocabulary (~30%).
4. **Top 15 additions (exam value order):** (1) Emami TD5/5–TD50/5 table for ~15 organs; (2) acute radiation syndromes with dose bands and LD50 3–4 Gy; (3) fetal stages (d1–10 / 11–42 / 43+) and the 100 mGy counselling threshold; (4) D10 = 2.3 D0 and cell-cycle phase durations; (5) NCRP 151 design goals P = 0.1/0.02 mSv/wk, T table, leakage 0.1%, IMRT factor, neutron/maze rules; (6) DOT TI, label categories, Type A/B limits, A1 for Ir-192/I-125/Co-60; (7) HDR/teletherapy licence numbers (leak ≤ 185 Bq every 6 mo, 2/10 mrem/h head leakage, 5% spot-check trigger, 3-yr records, 30-day QMP reporting); (8) NRC patient-release 5 mSv rule and 10-half-life decay-in-storage; (9) detector regions and quirks (GM dead time, proportional/BF3, well chamber, MOSFET, OSL re-read, TLD glow peaks); (10) classic breast tangent/SCV/PAB borders and depth, esophagus AJCC regions, pancreas/kidney field anatomy; (11) ISCRO staffing ratios, ADCL 2-yr chamber / 1-yr survey-meter intervals, star-shot and split-field test names; (12) MRI sequence/parameter table (TR/TE, T1/T2 meanings, Larmor, gradients) and US numbers (Z = ρv, 0.5 dB/cm/MHz, 1–20 MHz); (13) NM/PET instrumentation (Te, 1.44 T½, resolution limits, collimators, cyclotron vs generator nuclides); (14) ethics/legal vocabulary (4 elements of negligence, intentional torts, res ipsa, respondeat superior, HIPAA penalties, consent) plus current MDCB eligibility (JRCERT) and CE cycle; (15) SRS/SBRT platform facts (CK 80 cm SAD, cones, tracking modes; GK sources/helmets/50% IDL; tomotherapy; Calypso) and IMRT-optimization vocabulary.
5. New calculation variants worth adding: early-removed permanent implant dose, mg-Ra-eq conversion, Sievert along/away table dose-to-point, ODI-misread dose error, forgotten-wedge delivered dose, D10 from D0.
6. **Better than our bank:** sheer item volume for drill (≈ 1,000 keyed items), systematic regulatory/safety procedure coverage, and site-by-site anatomy/border recall.
7. **Worse than our bank:** accuracy (keyed errors, inconsistent numbers), currency (pre-2017 MDCB routes, pre-1997 release rule, no QUANTEC/TG-101/hypofractionation/HPV), rationale depth (one line or none vs our worked examples), and question format (combination items, opinion items, off-blueprint physics).
8. **Complementary:** use the book as a recall-fact mine for m21, m41, m42, m20, m10 and as a checklist of CT structures for m22; keep our bank as the source of truth for calculations and current standards.
9. Do not import any book statement without checking against the current standard; the specific errors to avoid are listed per chapter above (BED arithmetic, kidney TD5/5, lens/cataract thresholds, public lens 50 mSv, P-32 thyroid, release criterion, badge cadence, MDCB routes, flexure anatomy, Test III Q126/Q134 keys).
10. Nothing from `inbox/` has been copied into `knowledge/`; this report is paraphrase and values only and is the only new file.
