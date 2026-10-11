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

### Q20
Stem: A knowledge-based planning model for the prostate was trained only on patients with no hip prosthesis. Today's patient has a left hip replacement and streak artifact across the rectum. The model still prints rectal and bladder objectives. How should those objectives be used?
A. As a validated optimum; once the model has learned a rectum it applies to every implant
B. As a reason to send lateral beams through the prosthesis, which is how the library spared the rectum
C. As an unvalidated suggestion; the training set did not include metal artifact or beams that must avoid a prosthesis, so those constraints have to be built explicitly and the dose checked with a suitable algorithm
D. As a substitute for contouring, because the model already stores a standard rectal volume
Answer: C
Objective: III.10
Why: Answer C. A knowledge-based model is only as representative as its library. Metal changes the beam angles that are allowed and the dose calculation, and artifact can corrupt the contours the geometry features are built from. A no-implant model can propose objectives that are not achievable without irradiating the prosthesis, or that look acceptable on a DVH computed through bad densities. Use the printout as a starting point, add a prosthesis avoidance the library never saw, and judge the dose with an algorithm that can handle the metal. Lateral beams through the implant are the arrangement to avoid. The model does not draw the rectum.

### Q21
Stem: A class-solution template was written for an intact right breast: tangent geometry, heart objectives written for a heart beside a right-sided target, and a structure named Breast_R. The template is applied, unedited, to a left-breast case. What limitation does that expose?
A. The template detects laterality from the CT and flips the tangents, so the right-breast version cannot be applied to the left
B. Templates ignore structure names, so Breast_R is dropped and the heart is spared automatically
C. A template that meets its cost function has been commissioned, so heart dose on the left can be ignored
D. A template stores one laterality and one set of tradeoffs; on the opposite breast it will chase the wrong beams and the wrong heart geometry until a planner edits it
Answer: D
Objective: III.10
Why: Answer D. A template is a stored technique: beam geometry plus the objectives it was written for. A right-breast class solution does not discover that this target is on the left, and it does not rewrite the heart tradeoff for a left-sided tangent pair. Someone has to change the beams, the structure names, and the objectives. Meeting a cost function is not commissioning. Structure names are how many templates find their organs, so a name such as Breast_R is not ignored; it is simply the wrong breast.

### Q22
Stem: An autoplan script binds objectives by structure name. It expects Parotid_L. This contour is named Lt_Parotid. The script completes and states that every structure it mapped met its goal. The left parotid mean dose is well above the protocol. What failed?
A. Multicriteria optimization removed the parotid on purpose to draw a tradeoff surface
B. The name did not match, so the script dropped the organ, gave it no objective, and the success line never included it
C. Knowledge-based planning cannot spare a parotid in a patient who has a hip prosthesis
D. The two names are biologically different organs, so the dose difference is α/β, not a mapping error
Answer: B
Objective: III.10
Why: Answer B. Automation is literal. If the script looks up Parotid_L and the contour is named Lt_Parotid, that parotid never receives an objective. The optimizer then has no reason to avoid it, and a report that only checks mapped organs still passes. The fix is a naming convention, a script that fails when an expected organ is missing, and a human check of the left parotid DVH. A tradeoff surface does not appear because a name was missed. A prosthesis model is a different failure. α/β does not rename structures.

### Q23
Stem: Tool 1 returns a family of plans on a tradeoff surface: no plan in the family improves one objective without worsening another, and the clinician chooses a point. Tool 2 predicts an organ DVH from the geometry of this patient and a library of prior plans, then writes objectives toward that prediction. Which statement is correct?
A. Tool 1 is multicriteria optimization and tool 2 is knowledge-based planning; they are not the same tool
B. They are the same tool; the surface is the predicted DVH plotted a second time
C. Tool 2 is multicriteria optimization and tool 1 is a template that cannot be navigated
D. Knowledge-based planning returns the surface, and multicriteria optimization predicts a DVH without using prior plans
Answer: A
Objective: III.10
Why: Answer A. Multicriteria optimization builds a Pareto set. Moving toward a better result on one objective costs another, and the clinician picks the compromise. Knowledge-based planning predicts an achievable DVH from geometric features and prior plans, then hands those predictions to the optimizer as objectives. One tool is a surface of tradeoffs. The other is a prediction from the library. A template is a third thing: a stored class solution, not either of these.

### Q24
Stem: On a multicriteria surface, the point with the lowest parotid mean puts the cord above the departmental maximum. A neighboring point meets the cord limit and spares the parotid less. What is the surface not entitled to decide?
A. That every displayed point already satisfies the protocol
B. That the parotid and the cord can both be improved by picking a third point that dominates both
C. Whether a point is allowed; the protocol selects the point, and the surface can contain plans that fail a limit the navigator did not lock
D. That the display is knowledge-based planning, because a surface is a DVH predicted from last year's plans
Answer: C
Objective: III.10
Why: Answer C. A Pareto surface shows compromises. It does not know the departmental cord limit unless that limit was locked. Plans that fail the protocol can sit on the surface, and the protocol, not the navigator, decides which point may be used. No point on a true Pareto set improves the parotid and the cord together relative to the set. The surface is also not a knowledge-based prediction; knowledge-based planning proposes a DVH from prior plans rather than handing back a family of plans to navigate.

### Q25
Stem: A head-and-neck knowledge-based model was trained on plans that usually exceeded the written larynx tolerance. On a new patient the predicted larynx DVH sits above that tolerance, and the optimizer achieves the prediction. What did the model teach the optimizer?
A. The protocol limit, independent of the library
B. A Pareto surface the physician must navigate before dose is computed
C. The Hounsfield number of the larynx, turned directly into a constraint
D. The DVHs the library actually produced, including a habit of running the larynx hot
Answer: D
Objective: III.10
Why: Answer D. The model learns what the training plans did, not the tolerance they were supposed to meet. If those plans ran the larynx hot, the prediction sits hot, and an optimizer that achieves the prediction inherits the habit. A human still has to compare that DVH with the protocol. Multicriteria optimization is a different tool and does not get produced by a high larynx prediction. Hounsfield units are not the feature that writes the DVH objective.

### Q26
Stem: An autoplan reports PTV D95% of 66.5 Gy. The prescription is 70 Gy to D95%. Scaling the plan by 70/66.5 raises a rectum D2% from 72 Gy to about 75.8 Gy, which fails the rectal limit. What should the planner conclude?
A. Scale the target only; organ doses stay at the pre-scale values
B. The whole distribution scales together; if the scaled rectum fails, change the objectives or the geometry, because the autoplan will not enforce a limit it was not given
C. 70/66.5 is less than 1, so the rectum dose should have decreased
D. The increase proves the tool was multicriteria optimization, which refuses to scale
Answer: B
Objective: III.10
Why: Answer B. The scale factor is 70/66.5 = 1.053. Every dose in the distribution moves with it, so a rectum D2% of 72 Gy becomes 72 × 1.053 = 75.8 Gy. If 75.8 Gy fails the protocol, do not accept the scaled plan. Change the objectives or the geometry. The autoplan will not notice a limit it was never given. Organ doses do not stay behind when the target is rescaled. 70/66.5 is greater than 1. Scaling is ordinary normalization, not a sign that the tool was multicriteria optimization.

### Q27
Stem: A knowledge-based model predicts a parotid mean of 24 Gy with a wide uncertainty band. After optimization the achieved mean is 31 Gy. The geometry is an outlier relative to the library. Which reading is sound?
A. The prediction is not a guarantee and not a multicriteria surface; read the band, then judge the achieved DVH, because the optimizer may not reach the prediction
B. 24 Gy was a hard constraint, so 31 Gy means the optimizer violated a commissioned limit
C. Replace 31 Gy with 24 Gy in the record without looking at the dose on the slices
D. The 7 Gy gap identifies the tool as multicriteria optimization, which returns one DVH from prior plans and no band
Answer: A
Objective: III.10
Why: Answer A. A predicted mean with a wide band is a statement about similar prior plans, not a constraint the optimizer is guaranteed to hit. Outlier geometry is where the prediction is weakest. Read the band, then read the achieved DVH and the slices. Recording 24 Gy in place of 31 Gy falsifies the plan. A single predicted DVH is knowledge-based planning. Multicriteria optimization returns a surface of plans, not one library DVH and a band.
