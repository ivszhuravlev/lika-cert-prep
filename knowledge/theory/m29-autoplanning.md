# Module 29. Autoplanning

Autoplanning drafts a plan from a template or from a model trained on old plans. It does not approve a plan. The exam tests what the automation is doing and which failures a human still has to catch.

## Autoplanning

**MDCB objectives:** III.10, III.7, III.12

**What the exam expects**

You can describe knowledge-based planning, template planning, and multicriteria optimization as three different tools. You can list the failures that leave a “converged” autoplan unsafe: wrong structures, a model trained on poor plans, missing objectives, unusual anatomy, and devices the model has never seen. Human review is required.

**Core facts**

Three ideas share this lesson and should not be collapsed into one word.

**Template or protocol autoplanning** loads a class solution: beam energy, arc geometry or fixed gantry angles, and a set of optimization objectives for that site. It is a scripted starting point. It will happily optimize a prostate template on a head-and-neck structure set if the names happen to match, and it will do nothing about a constraint that was never in the template.

**Knowledge-based planning** uses a model built from prior clinical plans. The model predicts an achievable dose-volume histogram from the geometry of this patient: how much the parotid overlaps the PTV, how far the rectum is from the prostate, and similar features. Those predictions become objectives and priorities. The optimizer then tries to meet the prediction. If the library plans routinely exceeded a tolerance, the model learns that habit. If the library never included a pacemaker, a hip prosthesis, or a single kidney, the prediction is not a plan for those patients.

**Multicriteria optimization** builds a family of plans along the tradeoff surface (a Pareto set). No plan in the set improves one objective without worsening another. The planner or the physician moves on that surface and chooses a compromise. This is a decision tool. It is not the same thing as a single autoplan that returns one “optimal” result. The blueprint lists MCO with planning methodology and lists autoplanning with automated planning. Know both phrases.

What the human review is for:

- Structure names and laterality. A model keyed to “Cord” will ignore “SpinalCord_PRV” and will not warn you.
- The objectives that were actually loaded, compared with the protocol you think you are following. An autoplan can satisfy every objective it was given and violate a clinical constraint nobody encoded.
- Unusual anatomy: one kidney, a transplant, a large resection cavity, targets on both sides of the cord, a target touching the brachial plexus.
- Implanted devices, contrast, and metal. The model does not interrogate a pacemaker and does not override a hip (TG-203 and the density module).
- Normalization. The autoplan’s definition of 100% may not be the D95 or D50 your prescription uses. Rescale consciously, and remember every OAR dose rescales with it.
- The dose distribution on the slices, not only the DVH. A DVH cannot prove location, contour correctness, or grid size.
- Independent calculation and the ordinary plan check. Automation does not replace them.

Sites with repeatable anatomy and a large library (prostate, head and neck, standard breast tangents) are where these models earn their keep. A re-irradiation, a pediatric case, or a first plan after a new protocol is a weak place to trust an unedited prediction.

Scripting is the delivery mechanism for many of these tools. The computer-systems module covers version control. Here the clinical point is that the script’s output is a plan like any other. If the script sets the wrong fraction dose, it sets it consistently, which is harder to see than a one-time typing error.

Knowledge-based predictions also have a stated uncertainty. A parotid predicted to a mean of 24 Gy with a wide band is not a parotid constrained to 24 Gy. Read the band. Then look at the achieved DVH after optimization, because the optimizer may not reach the prediction when the geometry is an outlier.

**Formulas**

There is no separate autoplanning equation. The objectives it writes are the ones you already use.

A minimum DVH objective on a PTV: at least a stated percent of the volume shall receive at least a stated dose. Example: D95% ≥ 70 Gy, or V70 Gy ≥ 95%. Those are two ways to write a coverage goal. D95 is a dose. V70 Gy is a volume. An autoplan template that swaps them will chase the wrong axis of the DVH.

A maximum DVH objective on an OAR: no more than a stated volume shall exceed a stated dose. Example: V70 Gy ≤ 15% of the rectum, or D2% ≤ 74 Gy.

Equivalent uniform dose collapses a nonuniform distribution into the uniform dose that would have the same biological effect for a chosen volume-effect parameter. A template that sets an EUD objective and a DVH objective on the same organ can fight itself. Review both numbers.

Normalization check, same arithmetic as the planning module. The autoplan reports PTV D95% = 66.5 Gy and the prescription is 70 Gy to D95%. The scale factor is

70 / 66.5 = 1.053

A rectum D2% of 72 Gy becomes 72 × 1.053 = 75.8 Gy. If 75.8 Gy fails the protocol, do not accept the scaled plan. Change the objectives or the geometry. The autoplan will not notice a limit it was not given.

**Traps**

- Accepting a converged optimizer as a reviewed plan.
- Trusting a model on a patient who would have been an outlier in the training set.
- Swapping D and V objectives because the template labels are cryptic.
- Ignoring a structure the model skipped because of a naming mismatch.
- Letting MCO “navigation” replace the protocol constraint. The surface includes plans that fail the protocol. The protocol chooses the point.
- Skipping the slice view because the predicted DVH matched the achieved DVH. The match can be perfect on the wrong contour.

**Sources**

- ICRU 83, for the DVH metrics an autoplan is trying to hit (D98, D50, D2, and the objectives you add)
- AAPM TG-203, for devices the model will not manage for you
- The model’s own training documentation: number of plans, sites included, and known exclusions. Confirm applicability there before you treat an unusual case with it.
