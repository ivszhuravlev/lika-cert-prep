# Module 29 — Autoplanning

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

## Autoplanning

### Q1
Stem: A knowledge-based planning model predicts an organ-at-risk DVH from the geometry of the current patient, using a library of previously treated plans. Which input actually drives that prediction?
A. The patient's name and the monitor units of the library plans
B. Geometric features such as the distance from the organ to the target and the overlap of the organ with the target, compared with the library
C. Only the prescription dose, with no use of the organ's shape
D. The Hounsfield number of the organ, converted directly into a DVH without geometry
Answer: B
Objective: III.10
Why: Answer B. Knowledge-based models learn the DVHs that the clinic achieved for similar geometry. The useful predictors are spatial: how much of the organ overlaps the target, how the organ-target distance histogram looks, and related shape features. The model then proposes objectives so the optimizer aims at a DVH the library says is achievable. Identity and historical monitor units are not the predictors. A prescription alone cannot tell a parotid that overlaps the PTV from one that sits 2 cm away. Hounsfield units do not encode that geometry.

### Q2
Stem: The prostate knowledge-based model was trained only on plans with no hip prosthesis. Today's patient has a left hip replacement, and the model still prints a full set of rectal and bladder objectives. How should the prediction be used?
A. As a validated optimum, because a model generalizes to every implant once it has learned the rectum
B. As an unvalidated suggestion; the training set did not include metal artifact or beams that must avoid a prosthesis, so the planner has to build those constraints explicitly
C. As a requirement to send lateral beams through the prosthesis, because that is how the library spared the rectum
D. As a substitute for contouring the rectum, since the model already knows a standard rectal volume
Answer: B
Objective: III.10
Why: Answer B. A knowledge-based model is only as representative as its library. Metal changes both the achievable beam angles and the dose calculation, and artifact can corrupt the contours the geometry features are built from. Applying a no-implant model without review can propose objectives that are not achievable without irradiating the prosthesis, or that look fine on a DVH computed through bad densities. The correct use is to treat the prediction as a starting point, add a prosthesis avoidance the library never saw, and judge the dose with a suitable algorithm. C is the beam angle to avoid. D is wrong because the model does not draw the organ; a wrong rectum produces a confident, irrelevant DVH.

### Q3
Stem: A template autoplan for head and neck loads a class solution: nine beam angles and a standard set of parotid, cord, and larynx objectives. The patient has a unilateral early tonsil cancer, and the template still opens beams that cross the contralateral parotid. What is the limitation of template autoplanning shown here?
A. A class solution encodes one geometry and one set of tradeoffs; it does not know that this patient's contralateral neck is not a target
B. Templates reoptimize beam angles from scratch for every patient, so the contralateral beams cannot be real
C. Once a template meets its cost function, contralateral dose can be ignored because templates are commissioned like a linac
D. Template plans do not use contours, so parotid dose is independent of beam angle
Answer: A
Objective: III.10
Why: Answer A. A template (class solution) is a stored technique: beam geometry plus objectives that fit the cases it was written for, often bilateral head and neck. It will faithfully spare what it was told to spare and cover what it was told to cover, including a contralateral neck that this patient does not need treated. Someone has to turn those beams and targets off. Templates do not invent a new beam arrangement by themselves unless a separate optimizer is allowed to, and even then the starting objectives matter. Meeting a cost function is not commissioning, and the dose to a parotid clearly depends on whether a beam crosses it.

### Q4
Stem: An autoplan report says every constraint is met: PTV D95 is at the prescription, cord maximum is under the limit, and the optimization score is the best in the department this month. The hot spot of 115% sits on the larynx, which had no objective. What does the score fail to guarantee?
A. Nothing; a best score means the plan is clinically acceptable
B. That dose outside the optimized structures is acceptable; a structure with no objective can absorb the hot spot while the score still looks excellent
C. That the PTV was contoured; the score contours the target from the score value
D. That 115% is below 100%, because scores are reported in BED
Answer: B
Objective: III.10
Why: Answer B. Optimizers and autoplanning scores only pay attention to structures and objectives they were given. An unconstrained larynx, an unconstrained hotspot in unspecified tissue, a beam entering through a pacemaker, or a collision are invisible to a score that never included them. Clinical review looks at where the high dose sits, not only at the number. A is the automation trap. C reverses responsibility: contours go in, scores come out. D confuses a planning score with biologically equivalent dose.

### Q5
Stem: Two planners run the same autoplan script on the same approved contours and the same prescription. One result spares the rectum and the other heavily doses it. The script maps structures by name. The rectum was named "Rectum" in one session and "rectum_wall" in the other, and the script did not find "rectum_wall." What is the failure mode?
A. Knowledge-based models always randomize the rectal dose to explore the Pareto surface
B. A scripted or templated plan that identifies organs by name can silently drop an organ it does not recognize, then report success on the organs it did find
C. Autoplan cannot spare the rectum under any naming convention, so the doses should differ
D. The difference is expected biological uncertainty from α/β, not a software mapping error
Answer: B
Objective: III.10
Why: Answer B. Automation is literal. If the script looks up "Rectum" and the contour is named something else, that organ never receives an objective. The optimizer then has no reason to avoid it, and a checklist that only tests "all mapped organs met their goals" still passes. The fix is a naming convention, a script that fails closed when an expected organ is missing, and a human check of the rectal DVH before the plan is called done. A Pareto navigator does explore tradeoffs, but it does not do so by losing a structure name. C and D invent limits that are not the cause of this discrepancy.
