# Independent exam-readiness review

Reviewer did not write the bank. Verdict: not ready.

The largest hole is treatment-planning judgment. Planning is 42% of the 155-item exam. The bank drills hand arithmetic and is thin on site technique, stereotactic constraints, and image-based plan review. There is no ProKnow dataset and no unlabeled CT.

Hand formulas in modules 3, 8, 33, 35, 36, and 40 have real number variants. Practice Exam 1 and 2 match the published weights, except localization is light (2 of 40 instead of about 3).

## Fixes, in the reviewer's order

1. Block. Modules 20 and 25. Site-planning cases the current oncology items skip: anal, bladder, endometrium, larynx, pancreas, Hodgkin, breast nodes and boost, craniospinal. Technique, energy, match, nodes, fractionation, and the organ that limits the plan.
2. Block. Module 43. TG-101 and Timmerman items for 1, 3, and 5 fractions, including optic pathway, brainstem, and brachial plexus. The cord numbers are in the notes and in zero items.
3. Block. Module 43. Rewrite the QUANTEC quiz with new numbers. The current quiz repeats the lesson figures. Keep the rectum as a five-bin set.
4. Block. Module 22. Unlabeled-slice items. The current stems narrate the landmark, so they do not test recognition.
5. Block. Module 19. Plan-evaluation items where the DVH meets a limit and the geometry does not. ProKnow viewer drills stay on mdcb.proknow.com. This bank cannot host that dataset.
6. Block. Module 44. One 155-item timed form is out of scope for a single patch. Raise localization in the practice exams from 2/40 toward about 8%.
7. Should. Modules 19 and 25. At least eight optimization items: EUD, min and max DVH, a hotspot in a structure with no objective, a multicriteria compromise.
8. Should. Module 28. Offline versus online adaptation, a cone-beam that is not a planning CT, a rigid shift that cannot undo deformation. The file has five items.
9. Should. Module 29. Knowledge-based model outside its training set, a template on the wrong side, a script that drops an organ. The file has five items.
10. Should. Modules 38 and 39. Sliding lung, rectal gas, a stretched voxel, a coarse grid on a small cord, contrast left at the wrong density. Five items each.
11. Should. Module 41. Secondary barrier from leakage and patient scatter. Primary transmission already has two number sets.
12. Should. Modules 7 or 34. Skin dose from tray distance and a carbon-fiber couch. Bolus and obliquity are already drilled.
13. Should. Modules 14, 17, 18, and 32. A second set of localization cases. Ten items is one pass.
14. Later. Modules 26, 30, and 31. A second pass for DICOM frame-of-reference, autocontour naming, and devices other than a pacemaker.
15. Later. Module 42. Record-and-verify failures where the monitor units match and another parameter does not.

## Corrected from the planning review

Khan is 90% ≈ E/3.2 and 80% ≈ E/2.8. Bentel is 90% ≈ E/4 and 80% ≈ E/3. The question file had those authors swapped, so the keyed answers taught Bentel's rule as Khan's. Fixed in m19 (header, Electrons 101 Q2 rationale and Q3 key, Electrons Quiz Q1 and Q2 keys, bolus item author), m25 (notes and Beam Energy Q4, now named Bentel), m31 (E/2 is not called Khan), m44 (80% E/3 named Bentel), and m45 notes. Internal eye shields are stated as about 9 MeV and below in m19 and m24.

## Corrected from the physics review

The photoelectric item that said “per atom” and keyed a factor of 8 now asks for the mass attenuation coefficient (Z^3). A separate item asks for the per-atom estimate and keys 16 (Z^4). Wavelength rationales now parenthesize c/λ. The mean-life note says 1.44 gives 43.2 years and 1.443 gives 43.3 years. Added numeric items for I-125 recall, Ir-192 and Co-60 decay, Pd-103 total dose, a non-integer half-life, Mo-99/Tc-99m equilibrium, orthovoltage timer error, pair-production kinetic energy, magnification with depth, Mayneord F, Ptp, roentgen to air dose, HDR versus a linac, proton energy, SGRT, and kV versus MV contrast.

## Corrected from the calculation review

Breast superior–inferior length is the couch kick (20 cm at SAD 100 cm is 5.7°). A posterior width is a gantry adjustment or a half-beam jaw (16 cm is 4.6°). After the couch kick, the collimator only parallels the posterior border to the chest wall. Primary-barrier transmission is dimensionless, not Gy/week.

Added: a named couch-kick item (20 cm superior–inferior length, 5.7°) and a named gantry item (16 cm posterior width, 4.6°), a half-beam skin gap of 0 cm, a negative cobalt timer error (set time 2.20 min for 200 cGy), an SAD-calibrated MU with SSD 100 cm (307.5 MU, not 298.5), a cord peak missed by a coarse grid (3.7 Gy), an EQD2 sum of 76 Gy, and a TG-101 three-fraction cord point dose that fails 21.9 Gy.

All four independent reviews are in. Remaining holes that this patch does not close: unlabeled CT and ProKnow, a 155-item timed form, multicriteria optimization, and a second pass on the short localization files.
