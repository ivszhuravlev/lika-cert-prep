# RM Review — independent verifier: what the plan missed

Method. Read plan.md and all 8 reports; extracted every MISSING/PARTIAL item; checked each against
plan.md and against the worktree `knowledge/` (ripgrep, review folder excluded) at the time of this
pass (worktree then held 24 `*-rm-*` question files plus appended theory; it is still being written,
so a few items below may be landing as this is read). Independently read in full: MDCB Practice Test
Set 2023 (Tests 1–5), MDCB Pract Calcs, Potholes, Reminders; sampled ~260 lines at 4–5 places each in
All Short Tests, All Quizzes, AllPracticeTest, DOSE GRID. Roughly 330 testable facts were probed.
Everything below is paraphrased; no source wording is reproduced.

Legend: (dated) = appears in sources but reflects superseded practice; include only as a distractor
or with a "historical" tag. (low) = single-source, low exam yield.

## (a) Report-MISSING/PARTIAL facts absent from BOTH plan.md and the worktree

### m01 Introduction / professional
- m01: Legal and ethical vocabulary that appears in the review materials — negligence, tort, informed consent, living will / advance directive, scope-of-practice reference documents (AAMD scope and practice standards), JRCERT as the program accreditor; plan has only HIPAA.

### m03 Radioactivity / sources
- m03: Activity "order of magnitude" ladder — teletherapy Co-60 ~10 kCi; Gamma Knife ~6 kCi; blood irradiator Cs-137 tens of Ci; HDR Ir-192 ~10 Ci; LDR tandem/ovoid Cs-137 ~100–200 mCi; I-131 ablation ~100–150 mCi; FDG ~15 mCi; I-125 seed ~0.3–0.5 mCi; check source ~10 µCi; wipe limit 0.005 µCi.
- m03: Radiopharmaceuticals for painful bone metastases — Ra-223 (alpha), Sr-89 and Sm-153 (beta); bank lists Ra-223 only as a half-life entry.
- m03: Choice of decay mode from the N/Z balance — neutron-rich nuclides decay β−, proton-rich decay β+ or electron capture.

### m04 X-ray production
- m04: Rectification / generator type (half-wave, full-wave, three-phase, high-frequency) and its effect on ripple and output.
- m04: Changing filtration leaves the maximum photon energy and the characteristic lines unchanged; added filtration lowers surface dose but also lowers image contrast.
- m04: Rules of thumb — mean bremsstrahlung energy ≈ one-third of the peak; x-ray production efficiency ~1% at diagnostic kV versus tens of percent (sources quote ~40%) at megavoltage.

### m06 Interactions
- m06: Delta rays (energetic secondary electrons knocked out by a primary charged particle).

### m07 Treatment machines
- m07: Beam steering coils (radial/transverse position and angle) in the drift/bending section and their role in symmetry.
- m07: Among clinical photon machines the linac gives the highest dose rate (vs Co-60, betatron, Van de Graaff).

### m09 Measurement
- m09: Thimble-chamber wall materials and build-up caps (graphite, C-552 air-equivalent plastic, A-150, PMMA).
- m09: Counting efficiency — converting counts per minute to disintegrations per minute for wipe tests.
- m09: IAEA TRS-398 as the international counterpart of TG-51; Fricke (ferrous sulphate) chemical dosimetry as a named absolute method.

### m10 Imaging
- m10: MRI is generally avoided in the first trimester (first ~12 weeks) by convention, not because of a proven effect.
- m10: Basic pulse-sequence names — spin echo (90°/180°), gradient echo, inversion recovery; multiparametric prostate MRI = T2 + diffusion + dynamic contrast.
- m10: SUV defined as tissue concentration divided by (injected activity / body mass).

### m13 Patient data
- m13: Manual contour-acquisition tools — lead/solder wire, calipers, pantograph — and that calipers are still the check on CT separations.
- m13: Iodinated contrast precautions — renal function (creatinine/eGFR), metformin hold, prior reaction; relevance to sim scheduling.

### m14 / m16 Positioning and simulation
- m14: Positioning aids — head-rest sizes / chin-extension masks, avoidance of thick soft pads under the patient for reproducibility. (low)
- m16: Retrograde urethrogram marks the prostatic apex; base is superior, apex inferior. (dated for apex localization, still asked)

### m15 / m18 Motion and IGRT
- m15: Prospective vs retrospective 4D-CT acquisition (one phase vs all phases binned afterwards); gating lengthens treatment time.
- m18: Named tracking systems — CyberKnife with floor-mounted kV tubes and ceiling detectors; ExacTrac (floor tubes, ceiling panels, infrared); electromagnetic beacons (three transponders, prostate more than lung).

### m19 Isodose metrics / electrons
- m19: Electron flatness/symmetry specification (reference plane near the 95% depth, symmetry as the difference between mirror points; TG-142 tolerances in the 3% class).
- m19: Inhomogeneity index Dmax/Dmin and the typical hot-spot ladder by technique (3D ≤107–110%, IMRT/VMAT ~110–115%, SRS/SBRT 125–200% accepted).
- m19: Electron cut-out lateral-equilibrium rule — field width should be at least about E/2 cm (or ≥ Rp); smaller cut-outs lower output, pull dmax toward the surface and need measurement.
- m19: Lead on the skin produces a hot spot medial to the lead edge (tear-drop shape); electron hot spots at air-cavity interfaces (ethmoid/nasal region).
- m19: Virtual SSD is shorter than the nominal 100 cm, with the largest deviation at low energy and small cone.

### m20 Site oncology
- m20: Benign-disease radiotherapy indications (keloid, heterotopic ossification, Graves ophthalmopathy, gynecomastia); only pterygium is present.
- m20: Wilms tumour flank RT is started within about 10 days of nephrectomy; dental extractions are done 10–14 days before head-and-neck RT to allow healing.
- m20: Uveal melanoma — plaque or protons for medium tumours, enucleation for very large tumours (roughly >10 mm thick or >15–16 mm diameter).
- m20: Breast cancer arises in the upper outer quadrant in about half of cases (~45–50%).
- m20: Interstitial brachytherapy boost of the base of tongue preserves swallowing function.
- m20: Lip cancer — lower lip predominates; small lesions are cured equally by surgery or RT; oral tongue is the most common oral-cavity subsite, floor of mouth second; intraoral electron cone (6–12 MeV) boost is given before the large fields so the patient tolerates the cone before mucositis.
- m20: Maxillary sinus accounts for the large majority (~70%) of paranasal-sinus cancers.
- m20: CNS early-delayed reaction (somnolence syndrome) at 1–12 weeks, peaking around week 3, self-limited. (low)
- m20: Hereditary syndromes raising childhood cancer risk — Li-Fraumeni (p53), Down syndrome (leukaemia). (low)
- m20: Supraglottic larynx drains early to levels II–III bilaterally, in contrast to glottic T1 which takes no elective nodes (glottic part present).

### m21 Radiobiology
- m21: Mitosis sub-phases (prophase, metaphase, anaphase, telophase) and where the checkpoint sits.
- m21: Rubin–Casarett cell-population classes (vegetative intermitotic most sensitive → fixed post-mitotic least).
- m21: Multi-target model relation ln(n) = Dq/D0 and the extrapolation number.
- m21: DNA bases (A–T, G–C) as the target of direct action.
- m21: OER falls with LET — ~2.5–3 for photons, ~1.5–1.6 for fast neutrons, ~1 for alpha/heavy ions.
- m21: Radiosensitizing chemotherapy agents (cisplatin, 5-FU, hydroxyurea, methotrexate, fludarabine, gemcitabine) versus protectors (amifostine).
- m21: Hyperthermia 42–45 °C acts synergistically, especially on S-phase and hypoxic cells. (low)
- m21: Chemotherapy agents that raise pneumonitis risk when combined with thoracic RT (bleomycin, gemcitabine, actinomycin-D, doxorubicin recall).

### m22 Anatomy
- m22: Cardiac apex at about the left 5th intercostal space in the midclavicular line; the right atrium forms the right heart border.
- m22: Adult rectum length ~12 cm (sources also quote 12–15 cm). (low)

### m23 Delivery systems
- m23: The classic set of dynamic-MLC QA tests (leaf speed, leaf acceleration/deceleration, positional accuracy/gap, dose-rate stability, interrupt test).
- m23: Dynamic conformal arc vs VMAT (DCA conforms aperture only, no fluence modulation or dose-rate change).
- m23: Sliding-window is more time-efficient than step-and-shoot; IMRT beam entry/exit angles kept ≥10–15° apart to avoid opposed beams.
- m23: Compensator-based (solid) IMRT — finer spatial resolution, fewer MU and less leakage than MLC IMRT, with the risk of mounting the wrong compensator.
- m23: Quadratic objective — penalty = Σ weight × (D_plan − D_goal)² over voxels. (low)

### m25 Planning methods
- m25: VMAT vs fixed-field IMRT — VMAT is usually more conformal with fewer MU but tends to be less homogeneous (higher internal hot spot) and gives a larger low-dose bath (the "fewer MU" part is in plan; the hot-spot/homogeneity trade-off is not).
- m25: A physical wedge on the medial tangent raises scatter dose to the contralateral breast; prefer dynamic wedge or field-in-field medially.
- m25: Vertex (non-coplanar) field requires checking couch/table height and gantry clearance; a bladder field's superior border near L5/S1 limits small bowel. (dated)
- m25: Multiple beams improve target homogeneity and tumour/normal-tissue ratio; more beams raise conformity but also the internal maximum and spread penumbra (partly present for SRS; not stated generally).
- m25: Partially delivered IMRT fraction (machine fault mid-treatment) — estimate delivered dose, do not simply repeat, decide the make-up with the physician.

### m34 Beam modifiers
- m34: Wedge taxonomy — individual physical, universal/motorized (upper) wedge, dynamic/virtual wedge; dynamic-wedge factor depends on field size (opposite to a physical wedge), has minimum field-size and MU limits, less scatter outside the field.
- m34: Skin collimation for electrons sharpens penumbra when the cone is far from the skin.

### m35 PDD / TMR / MU
- m35: Equivalent circle/square conversions — square of a circle ≈ 0.886 × diameter (or radius ≈ 0.56 × side), equivalent square of a circle via 4A/P.
- m35: A 1 cm depth error changes TMR by roughly 2–3% at 6 MV; depth-error → dose-error rule.
- m35: Electron cut-out factor from the ratio of chamber readings cut-out/open cone, then into the MU equation.
- m35: SSD vs SAD technique for the same midplane dose — SSD setup needs more MU by ((SAD + d)/SAD)² (≈21% for a 20 cm diameter); and the mirror case, dose delivered when a plan is set up at the wrong distance (worktree has only the 18X 1.067 case).
- m35: Parallel-opposed pair — dmax dose = entrance + exit contributions from the PDD table; the dmax/midplane ratio rises with thickness and falls with energy (e.g., two beams each 93% at the far dmax give 186%).

### m36 Special calculations
- m36: Cord-block timing — count how many fractions the cord may stay in the field before the block/off-cord change given tolerance and fraction dose.
- m36: Sector area (θ/360 × πr²) in Clarkson-type problems; junction-shift formula (shift distance per move and how many moves fit in the field).
- m36: "Percent blocked" field — effective side ≈ open side × √(unblocked fraction) (10 cm with 30% blocked → ≈8.4 cm). (note: worktree says percent-blocked is an incomplete scatter correction; the calculation type itself is absent)
- m36: Orthogonal images are 90° apart (e.g., 85° and 355° qualify). (low)

### m37 Inhomogeneity
- m37: Bone correction magnitude by energy (a few % per cm of cortical bone at MV, larger at Co-60/low MV), to pair with the lung 3–3.5%/cm rule already in plan.

### m40 Brachytherapy
- m40: Exposure-rate calculation for a patient containing a radionuclide with an average body transmission factor (Γ × A / d² × transmission).
- m40: Manchester-style dose limits — bladder and rectum points kept ≤ ~80% (bladder) / ~70–80% (rectum) of the point-A dose.
- m40: Use the largest ovoids and the longest tandem the anatomy allows (better depth dose, lower mucosal dose).
- m40: Ring applicator is unshielded (vs shielded Fletcher ovoids); Fletcher-Suit tandem angles 15°/30°/45°; Henschke and Heyman applicators by name.
- m40: Radium-era source loadings — uniform, Indian club (one end heavier), dumbbell (both ends heavier).
- m40: HDR QA — timer/dwell-time linearity and end-effect test; two independent security measures on the HDR room/source; interlock preventing the imaging x-ray unit and the HDR from running together.
- m40: Eye-plaque construction — gold backing/shell (COMS) holds I-125 or Pd-103 seeds; Ru-106 is the beta alternative (Ru-106 present).
- m40: Prostate seed candidacy — pubic-arch interference and hormonal downsizing of large glands before implant.
- m40: Stereo-shift (and orthogonal) films for seed/source reconstruction. (dated)
- m40: Anisotropy is more pronounced for low-energy seeds (I-125, Pd-103) than for Ir-192; survey-meter range multiplier reading (×1/×10/×100 scale). (low)
- m40: Classification of implants by type with examples — interstitial (prostate, base of tongue, sarcoma, Syed), intracavitary (tandem/ovoid, cylinder, nasopharynx, balloon APBI), intraluminal (oesophagus, bronchus, bile duct), surface (skin, chest wall); endoluminal dwell weighting is higher at the catheter ends.
- m40: Brachytherapy TPS commissioning/annual check against published TG-43 tables (per-point agreement within ~2%, overall accuracy ~5%); source-strength unit consistency and anisotropy check.

### m41 Radiation protection
- m41: Out-of-field dose ladder — roughly 5% of the central dose at 2 cm from the edge, ~1% at 10 cm, ~0.2–0.5% at 30 cm (for fetal-dose estimates).
- m41: ALARA investigational levels — Level I ~10% and Level II ~30% of the applicable quarterly limit; radiation-safety committee meets quarterly; a worker may un-declare a pregnancy.
- m41: Thyroid bioassay after I-131 handling (within ~72 h), and when a bioassay is required.
- m41: BEIR reports / Japanese Life Span Study as the basis of the risk coefficients. (low)
- m41: Nuclear-medicine survey cadence — meter survey daily, wipe tests weekly.
- m41: Occupational-exposure ladder by job — interventional/cardiac-cath staff highest (~1–1.5 rem/y), nuclear-medicine and PET techs next, radiation therapists near background.
- m41: Exposure-rate ladder from patients — I-131 or Cs-137 bedside ~100 mR/h; visitor line ~1–2 mR/h; prostate-seed patient ~0.1 mR/h; background ~0.02 mR/h; contact with an HDR source thousands of R/h.
- m41: Shielding "magnitude" ladder — linac primary ~2.5 m (8 ft) concrete, secondary ~1 m (3 ft), HDR suite ~0.6 m (2 ft), CT/diagnostic rooms ~1.5 mm (1/16") Pb, PET ~3–25 mm Pb, linac door lead + borated polyethylene, portable Cs-137 bedside shield ~2 cm Pb.
- m41: Film-badge filters indicate beam quality (penetration) from differential darkening. (low)
- m41: Teletherapy head leakage 2 mrem/h at 1 m with 10 mrem/h at 5 cm from the housing, 5% spot check (dated).

### m42 QA / standard of care
- m42: TG-100 finding that communication/human error is the leading cause of events (RPN process present; this conclusion is not).
- m42: EPID/portal image quality phantom (Las Vegas) and monthly imaging-QA items by name.
- m42: Any new electron cone or applicator requires its output to be measured, not assumed.
- m42: DVH accuracy depends on bin size/dose grid; coarser calculation grid speeds the calculation (grid-vs-accuracy present, bin size not).
- m42: CBCT dose reduction by collimating the kV field/FOV to the region of interest and matching technique to task.

### m43 Constraints
- m43: Gonadal thresholds — testes: temporary sterility ~0.15–1 Gy, permanent ~3.5–6 Gy; ovaries: permanent sterility ~5–10 Gy (age dependent), hormonal loss.
- m43: Rib fracture risk rises above ~50 Gy conventional (and the SBRT chest-wall rows).
- m43: Single-fraction SRS brainstem maximum (~12.5–15 Gy, TG-101 15 Gy) — bank has cord and optic single-fraction points but not the brainstem row.
- m43: Lung SBRT V20 < 10% (RTOG 0236/0813 style) alongside the conventional V20 ≤ 30–37%.

### m44 Formats
- m44: The MDCB retired sets also use "which statement is TRUE/NOT a role" and image-identification stems alongside I–IV; nothing to add beyond plan, noted for balance.

## (b) Facts found in my own source reading, absent from both plan and worktree (not already listed in (a))

- m05: Superficial/orthovoltage vs electrons for skin — superficial gives ~100% surface dose and higher bone dose; electrons give 75–95% surface dose, a finite range sparing deep tissue, and a higher dose rate.
- m05: Electron surface dose increases with energy (≈75% at 6 MeV → ≈95% at 18 MeV) and with obliquity and bolus; a megavoltage photon beam's surface dose falls with energy. (first half present; the energy ladder values are not)
- m06: Compton recoil electrons are emitted only in the forward hemisphere (0–90°), while the scattered photon can go in any direction; maximum backscattered photon energy 255 keV at 180° is present.
- m07: Photon modes produce far more neutrons than electron modes of the same nominal energy; threshold region ~8–10 MV.
- m10: Reconstructed voxel volume = pixel² × slice thickness (e.g., 2 × 2 × 5 mm = 20 mm³); DRR quality improves with thinner slices (second half present).
- m10: Narrowing the window width increases displayed contrast; typical lung window (level ≈ −400/−600, width ≈ 1500); window/level does not change stored HU (last part present).
- m10: HU of water constancy ±5 HU and spatial-integrity check of ~1 mm are the TG-66 daily/monthly items (HU present; length accuracy not).
- m19: Penumbra definitions — bank uses 80–20%; the review package's "updated" sheet uses 90–20%; items should state which definition is meant.
- m19: Therapeutic electron depth is the 80–90% line, and the useful rule set E/3.2 (d90), E/2.8 (d80), E/2 (Rp) is present; add E/4 as the older "therapeutic range" so a stem using it is recognisable.
- m21: Fetal-dose estimation uses out-of-field scatter/leakage and the aim to keep fetal dose well under 0.1 Gy (threshold present; the "estimate then shield to <5–10 cGy" workflow not).
- m23: Beam obliquity (air gap at an angle) shifts electron dmax toward the surface, increases side scatter and surface dose, and bulges the low isodoses.
- m24: TBI/TSET dosimetry commissioned with ion chambers and verified in vivo with TLD/OSL; TSET bremsstrahlung contamination limits whole-body (marrow) dose (first half present).
- m33: A calculation point placed in the steep gradient near a block edge is unreliable; move the point or use a different normalization.
- m35: Equivalent-square approximation degrades when the elongation ratio exceeds about 2 (teaching example present; the rule is not).
- m36: Lead for an electron arc = E/2 + 1 mm is present; add that a conservative E/2 mm (×1.2 for cerrobend) is the general rule — present, so no action; listed for completeness only.
- m40: Permanent-implant total dose from initial dose rate (1.44 × T½ × 24 × rate) is present; add the inverse (initial peripheral dose rate required for a prescribed total), and mg-Ra-eq-hours of a permanent I-125 implant via Γ ratio (plan has mg-Ra-eq via Γ; the permanent-implant hours case is distinct).
- m41: Radiation-sign wording — "Caution, Radiation Area" vs "Caution/Danger, High Radiation Area" vs "Grave Danger, Very High Radiation Area" with the 0.05 / 1 mSv/h / 5 Gy/h triggers (HRA 1 mSv/h present; the three-tier wording not).
- m41: Magnitude-of-error ladder for QA intuition — a missing physical wedge changes dose 25–300%; normalising on the 50% field edge doubles the dose; heterogeneity on/off moves lung plans 5–30%; a 1 cm SSD error at 100 cm is ~2% (not the 3–7% quoted in the package, which is for shorter SSD); forgetting the TG-51 lead foil is ~0.2%.
- m42: TG-40 symmetry monthly 3% and TG-40 simulator laser 2 mm appear in retired MDCB items (dated); bank should show TG-40 as the historical reference in distractors.
- m42: Autoradiograph for seed-train uniformity is present; add that gross source non-uniformity is specifically what the autoradiograph screens for before ribbon use — present; no action.
- m43: Lens tolerance language in the package — threshold near 0.5–1 Gy, "tolerance" 5 Gy (fractionated) — the 0.5 Gy ICRP threshold is present; the fractionated 5 Gy figure as a distractor is not.

## (c) Plan items judged not exam-relevant, over-weighted, or wrong

- HVL fix (m03/m40): plan standardises Ir-192 lead HVL at 2.5 mm. MDCB Pract Calcs supplies 4.8 mm for Ir-192 in a worked problem (broad-beam value; literature ranges 2.5–6 mm), and the retired MDCB ordering item (Co-60 > Cs-137 > Ir-192 > I-125) works with either. Recommendation: keep a teaching value but never make the HVL number itself the keyed quantity; stems should supply it. Same for Cs-137 (5.5 vs 6.5 mm both appear).
- m43 fix "cord 13 Gy × 1 / 20 Gy × 3": conflicts with TG-101 values already in the bank (point max 14 Gy ×1 and 21.9 Gy ×3; 10 Gy / 18 Gy to 0.35 cm³). Add only as an attributed alternative protocol row (e.g., RTOG 0631-style 14 Gy / 10 Gy-to-10%), not as a replacement key.
- m05 "light field = 50% isodose": physics is correct and should stay, but one retired MDCB key (2023 set, Test 5) marks 75%. Writers should phrase the item so the 50% definition is unambiguous (field edge definition) rather than "light field coincides with X% at dmax".
- m44 "50–80 I–IV and matching items": matching sets are the review course's own drill format, not an MDCB item type; K-type (I–IV) items appear in retired MDCB sets but the current exam is single-best-answer with images. Suggest capping at ~20–30 I–IV items and ≤10 matching, redirecting the rest to image-identification and "which statement is true" stems.
- m10 "CT overestimates prostate volume ~30%": single-source number; the testable fact is direction (CT larger than MRI/US) — keep direction, drop the percentage.
- m24 "15 MV AP/PA for TBI": energy depends on separation (6–10 MV for thin patients); state as "higher energy for thick patients" rather than a fixed 15 MV.
- m07 "FFF 2400 MU/min": vendor-specific (1400 for 6FFF, 2400 for 10FFF on one platform); key on "roughly 2–4× the flattened dose rate", not on 2400.
- Priority 2 "cytogenetic dosimetry": already covered in the worktree (biodosimetry in m41); can be dropped from the to-do.
- Priority 2 "Papillon", "ICRU 24 ±5%", "TG-64/128/129" are low-yield; ICRU 24 duplicates the m39 ±5% item.
- Electron mean energy constant: bank uses E0 ≈ 2.33·R50 (TG-51/TG-25); the package's "updated" sheet insists on 2.4·R50 (IAEA/newer texts). Not a plan error, but items should accept 2.33–2.4 and not key on the third significant figure.
- Pd-103 monotherapy dose: bank keys 125 Gy (TG-137, NIST-99); one quiz in the package uses 110–115 Gy (pre-1999 convention). Keep 125 Gy; mention 115 Gy as the older convention in the Why.
- Exclusion list is sound. One caution: "TG-40 as current" is rightly excluded, but TG-40 numbers still appear in retired MDCB stems, so the bank should name TG-40 in distractors rather than omit it entirely.

## (d) Estimated coverage after the plan is executed

The eight reports already found ~60–85% of each source present in the bank, and the plan picks up
the recurring multi-source gaps (~150 facts, ~20 calculation types). Of roughly 330 testable facts I
probed independently from the four fully-read files and the samples, about 60 were absent from both
the plan and the worktree; most of these are single-source, low-yield items (applicator trivia,
magnitude ladders, radiobiology nomenclature), and perhaps 20–25 are MDCB-style high-yield (the
SSD↔SAD and parallel-opposed arithmetic patterns, electron cut-out/obliquity/hot-spot facts, brachy
point-dose and loading rules, protection and shielding ladders, SRS brainstem and lung-SBRT V20 rows).
Weighting by exam relevance, I estimate the bank will cover about 88–92% of the exam-relevant content
of the package once plan.md is complete, rising to ~95% if the (a)/(b) items above tagged as
high-yield are added; the remaining few percent are dated or physicist-level content that should stay
excluded.
