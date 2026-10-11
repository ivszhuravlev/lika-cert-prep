# Module 15. Patient Immobilization and Motion Management Techniques

Original notes for MDCB objective II.3. The reference report is AAPM TG-76.

## Management of Respiratory Motion

**MDCB:** II.3, II.4, I.8

**What the exam expects**

You name the TG-76 strategies, you know what each one does to the PTV, and you can say which CT data set is for the ITV and which is for dose. You do not add a second full motion margin on top of an ITV. You know why left-breast deep inspiration is used, and you can turn a gating duty cycle into a clock time.

**Core facts**

Respiratory motion is largest in the superior-inferior direction for lower-lobe lung, diaphragm, and liver. Excursions of about 1–2 cm are common and can be larger. Upper-lobe targets move less. TG-76 is the reference. A stem that quotes a measured excursion wants you to use that measurement, not a typical value.

The target volume language matters. The CTV is biological. The internal margin added to the CTV for motion produces the ITV (ICRU 62). The PTV is the ITV plus setup and residual uncertainty. If you already drew an ITV, the PTV margin is not “motion plus setup” again. Adding the excursion a second time treats lung that the ITV already covers.

Strategies in TG-76, and what each costs:

Motion-encompassing. Free breathing. 4DCT. ITV equals the union of the CTV positions, often contoured on the MIP for a solid tumor in lung. PTV is larger. Treatment is simpler. Dose is calculated on the average CT or a phase CT, with the ITV density overridden to tumor density if the average blurred it. The MIP is not the dose grid.

Gating. The beam is on only in a window of the cycle, usually around end-exhale, which is more reproducible than end-inhale and where the patient spends more time. Residual motion inside the window remains. The duty cycle is often about 30%, so clock time is about three times the beam-on time. The gate is only as good as the surrogate (abdominal bellows, surface marker, spirometer).

Breath hold. The patient holds a stated inspiration or expiration. Deep-inspiration breath hold for left breast moves the heart posterior and inferior, away from the tangential fields, and expands the lung. The scan, the plan, and every fraction have to be in that hold. A free-breathing plan is not delivered under DIBH. Active breathing control (ABC) uses a spirometer valve to enforce the hold. Voluntary hold needs coaching. Surface guidance can coach and can interrupt, and it still does not see the tumor.

Abdominal compression. A belt or a plate limits diaphragm excursion for SBRT lung and liver. Motion is reduced, not removed. The ITV is measured with the compression device on, in the same position as treatment. A compression scan planned and then treated without the plate uses the wrong ITV.

Forced shallow breathing. The patient is coached to breathe with a small amplitude. It is a different instruction from a breath hold and from a gate.

Real-time tracking. The beam follows the target (robotic linac with a correlation model, gimbal, or MLC tracking where commissioned). Implanted electromagnetic beacons are used more often for prostate than for lung, and the principle is the same: an internal surrogate. Margins shrink only to the residual tracking error. A chest-marker model that was built at the start of treatment can drift as the relationship between skin and tumor changes. Baseline shift is that drift.

Coaching with audio or video feedback tightens whichever of the above you chose. It is not itself a margin recipe.

4DCT artifacts. Irregular breathing sorts the same anatomy into the wrong phase. You see duplicated diaphragms or a missing slab. Do not contour the artifact as tumor, and do not accept an ITV from a MIP that contains a sorting failure. Amplitude-based sorting can be more honest than phase-based sorting when the period is irregular. Look at the cine or the phases before you draw.

End-exhale is the stable phase. End-inhale is deep, variable, and a poor default gate unless the technique is DIBH for a reason (heart sparing).

SGRT watches the surface. It is appropriate for a breast breath hold and for detecting a posture change. It does not measure a lower-lobe tumor’s superior-inferior position if the surface and the tumor disagree.

Immobilization that is not respiratory still belongs to this objective: mask, vac-lok, bite block, indexed board. A loose mask is a setup margin, and it shows up as a systematic shift on imaging. Do not hide a loose mask inside a respiratory ITV.

**Formulas**

Duty cycle is the fraction of time the beam is enabled.

Clock time ≈ beam-on time / duty cycle

PTV expansion from an ITV uses the setup and residual margin only.

ITV already includes the internal margin. Do not add the excursion again.

**Worked example**

Given: a gated beam needs 2.00 minutes of beam-on time. The duty cycle is 30%. Separately, the 4DCT excursion of the CTV is 1.0 cm superior and 0.8 cm inferior, and the setup margin is 0.5 cm isotropic. The ITV was drawn as the union of the CTV positions. How long is the gated slot on the clock, and what extra margin belongs on the ITV?

Formula: clock time = 2.00 / 0.30. PTV margin beyond the ITV = setup margin.

Arithmetic: 2.00 / 0.30 = 6.67 minutes.

The ITV already extends 1.0 cm superior and 0.8 cm inferior beyond the CTV. The PTV is that ITV plus 0.5 cm. It is not the ITV plus 1.0 cm plus 0.5 cm.

Meaning: gating stretches a 2-minute beam to about 6.7 minutes of room time. The volume expansion uses 0.5 cm, not 1.5 cm, once the ITV exists. Someone who adds the motion again has expanded the high-dose region by an extra centimeter of lung.

Usual wrong turn: 2.00 × 0.30 = 0.60 minutes, which makes gating look faster than free breathing. Or a PTV margin of 1.5 cm superior “to be safe” after the ITV was already drawn on the MIP. Or dose calculated on that MIP, so the entire 1 cm path is assigned tumor density and the lung dose is wrong in the other direction.

**Traps**

DIBH plan delivered in free breathing, or the reverse. Compression device left off at treatment. End-inhale chosen as the default gate because the lung looks larger. Artifact on 4DCT contoured as GTV. SGRT accepted as proof the tumor is at isocenter. Tracking margins set to zero.

**Sources**

AAPM TG-76, *The Management of Respiratory Motion in Radiation Oncology*. ICRU 62 for the internal margin and the ITV. Public blueprint II.3.

## Respiratory Motion Management Mini-Quiz

This quiz checks the TG-76 options (encompass, gate, breath hold, compress, track), ITV versus a second motion margin, MIP versus average CT, DIBH for left-breast heart displacement, and duty cycle as a clock-time divisor. The traps are PTV = ITV + motion + setup, dose on the MIP, gating time multiplied by the duty cycle, a free-breathing plan used for a breath-hold treatment, and end-inhale treated as the most stable phase.
