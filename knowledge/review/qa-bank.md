PASS python3 -m study.coverage
PASS questions 1365
PASS modules with questions 45/45
PASS lessons with no questions 0
PASS lessons under 5 questions 0
PASS MDCB objectives with no item 0
PASS python3 -m unittest tests.test_study -q
PASS ----------------------------------------------------------------------
PASS Ran 4 tests in 0.182s
PASS OK
PASS Локальная сессия сошлась: число, буква, промах в начало, HVL не в дороге.
PASS python3 -m study check
PASS Локальная сессия сошлась: число, буква, промах в начало, HVL не в дороге.
PASS m03 road_prompt body after Модуль: length 10568; HVL count 0; DVH count 0; monitor unit count 0; half-life present; decay present; ROAD_ASSERT PASS
PASS knowledge/questions/m36-special-calculations.md, m36::Gap Calculation Mini-Quiz::Q6, expected 1.90 cm, actual 1.90 cm, (22/2)*(10/110)+(18/2)*(10/100)=1+0.9=1.9000
PASS knowledge/questions/m36-special-calculations.md, m36::Couch/Collimator Divergence Tutorial::Q1, expected 5.7°, actual 5.7°, arctan(10/100)=5.710593° rounds to 5.7°
PASS knowledge/questions/m36-special-calculations.md, m36::Geometric Penumbra Mini-Quiz::Q7, expected 0.72 cm, actual 0.72 cm, 0.5*(100+10-45)/45=0.722222 rounds to 0.72
PASS knowledge/questions/m35-pdd-tmr-mu.md, m35::PDD and TMR Calculation Tutorial::Q7, expected 71.0%, actual 71.0%, 70*((111.5/101.5)^2)*((110/120)^2)=70.980421 rounds to 71.0
PASS knowledge/questions/m19-isodose-metrics.md, header, expected Khan 90% depth E/3.2 and Bentel 90% depth E/4, actual Khan 90% depth ≈ E/3.2 cm and Bentel 90% depth ≈ E/4 cm
BUG minor, knowledge/questions/m35-pdd-tmr-mu.md, m35::MU Calc Quiz::Q7, expected 240/0.4376 = 548.446 (exact 0.69×1.04×1.02×0.61×0.98 = 0.4375609056, 240/0.4375609056 = 548.495 rounds to keyed 548.5), actual Why states 240/0.4376 = 548.50
