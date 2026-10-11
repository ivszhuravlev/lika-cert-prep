# Module 30. Autocontouring

Automatic segmentation can draft an organ. It cannot own one. The exam asks how the contour was made and which errors survive a good-looking overlap score.

## Automatic Segmentation

**MDCB objectives:** III.10, III.4

**What the exam expects**

You can separate threshold segmentation, atlas-based segmentation, and a trained model. You can define Dice in a worked fraction and say why a high Dice can still miss the slice that matters. You know the physician is responsible for the target volume, and that OAR autocontours are edited before planning. Human review is required.

**Core facts**

Three methods cover almost every question:

**Threshold and region growing.** The algorithm keeps voxels inside a Hounsfield window. Lung, external air, and cortical bone segment this way. It fails when contrast, atelectasis, a trachea, or a metal streak crosses the window. The external contour that includes the couch, or that clips the nose, is a threshold error with a direct effect on dose.

**Atlas-based segmentation.** One or more library patients with approved contours are deformably registered to the new CT, and the contours are warped along. It is only as good as the registration. Unusual posture, an empty versus a full bladder, surgery, or arms up versus arms down makes the warp miss. TG-132’s warnings about folding and sliding tissue apply here.

**Model-based or deep-learning segmentation.** A network trained on many contoured scans predicts a label for each voxel. It is fast and, on anatomy it has seen, often closer than a single atlas. It still fails on rare anatomy, on artifact, and on structures that were scarce or inconsistent in the training labels. A model does not know that this patient’s right kidney was removed unless the image and the training set taught it that pattern. Check the empty side.

What review looks like on an axial slice, not on a score:

- External body: includes all tissue, excludes the couch and the immobilization device unless the plan intends to include them.
- Laterality: left parotid on the patient’s left (image right on a standard axial display).
- Small serial organs: optic nerves, chiasm, cord, brainstem, brachial plexus. These are the ones a model smoothes away. A missing chiasm does not create a DVH warning if the objective never ran.
- Air, contrast, and metal: dental artifact through the oral cavity, a hip prosthesis through the pelvis, oral or rectal contrast inside a target.
- Postoperative and edematous anatomy, and any target. Autocontour tools are commonly used to draft organs at risk. A starting CTV still belongs to the physician. Follow the AAMD scope of practice and local policy for who may contour which OAR. Do not present an automatic GTV as a finished target.

Overlap scores are how vendors and papers describe agreement. They are not a chart check.

Dice coefficient:

Dice = 2 |A ∩ B| / (|A| + |B|)

A perfect overlap scores 1. No overlap scores 0. Hausdorff distance is the worst mismatch on the boundary, the largest distance from a point on one contour to the nearest point on the other. A contour can have a respectable Dice and a large Hausdorff distance if a thin tail of cord or a small bump of brainstem is missing. The thin tail is the part that changes a max dose.

Edited contours replace the automatic ones for planning. Save the edited set. A replan that silently reloads the unedited model undoes the review.

**Formulas and a worked Dice**

Physician contour A = 10 cm³. Model contour B = 10 cm³. Overlap = 8 cm³.

Dice = 2 × 8 / (10 + 10) = 16 / 20 = 0.80

Twenty percent of each contour is not shared. If the unshared 2 cm³ of the physician’s cord is the 2 cm³ inside the high-dose field, the plan can meet a constraint on contour B and fail it on contour A. The score 0.80 does not say which 2 cm³ was lost.

A second case. A = 40 cm³, B = 30 cm³, overlap = 30 cm³. The model is entirely inside the physician contour and misses 10 cm³.

Dice = 2 × 30 / (40 + 30) = 60 / 70 = 0.86

The score looks strong. The model never covers the missed 10 cm³. If that 10 cm³ is distal seminal vesicle or the inferior cord, the DVH on the model contour is the wrong organ.

Threshold example, not a universal HU rule: lung is often grown from a low Hounsfield window, and a large airway will be included unless the algorithm or the editor removes it. The density used for dose is a separate decision (the inhomogeneity module). Segmentation and density override are two steps.

**Traps**

- Planning on the first automatic contour because the 3D view looked smooth.
- Trusting Dice and skipping the high-dose slices.
- Swapping left and right on a mirrored atlas.
- Letting a model fill in a kidney that was surgically absent.
- Reloading the unedited structure set at the adaptive replan.
- Using autocontour agreement as evidence the dose grid or the registration was adequate. Different question.

**Sources**

- AAPM TG-132, because atlas methods are deformable registration
- AAPM TG-263, for standardized structure names so a model and a template recognize the organ
- AAMD scope of practice, for who is responsible for which contours under local policy
- ICRU 50, 62, and 83, for the volumes being drawn (GTV and CTV are not OAR autocontours)

## Auto-Segmentation Mini-Quiz

**MDCB objectives:** III.10, III.4

**Skills this quiz trains**

- Identify threshold, atlas, and learned-model segmentation from a short description.
- Compute Dice from two volumes and an overlap.
- Explain a high Dice with a clinically dangerous miss, and name Hausdorff distance as the worst-boundary metric.
- Require an edit of small serial organs, laterality, artifact, and postoperative anatomy.
- Keep the physician responsible for the target.

**Traps**

- A Dice of 0.85 accepted as safe without a slice review.
- Couch included in the external.
- Absent organ “found” by the model.
- Automatic GTV treated as approved.

**Check yourself**

Overlap is 9 cm³, physician volume is 12 cm³, model volume is 12 cm³. What is Dice? Why is that not enough to approve a cord contour?

Walk-through: Dice = 2 × 9 / (12 + 12) = 18 / 24 = 0.75. A quarter of the cord contour is unshared. You still have to see whether the missed strip is in the field. The score cannot answer that.
