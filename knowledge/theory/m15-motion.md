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

## TG-76 Thresholds, Gating Modes, and Surrogates

**Objectives:** II.3, II.4

**What the exam expects**

You can state the TG-76 motion threshold above which a management technique is considered. You can tell prospective from retrospective acquisition, phase from amplitude gating, and an external surrogate from an internal fiducial. You can explain what a duty cycle trades against residual motion. You know what a maximum-intensity projection is good for and where it fails. You can describe what an infrared marker-block system and an electromagnetic transponder system measure, and you can say when compression or a breath hold is the better fit.

**Core facts**

The threshold. TG-76 recommends considering a respiratory management technique when the target moves more than 5 mm in any direction, provided the patient can tolerate the technique and the department has it commissioned. Below 5 mm the motion is usually absorbed by the margin and no special technique is required. The excursion is measured, not assumed, which is why a 4DCT or a fluoroscopic look is the first step for a thoracic or upper-abdominal target. Nasopharynx, brain, and most head-and-neck sites do not need respiratory management.

Prospective versus retrospective. In a prospective (gated) acquisition the scanner is triggered by the respiratory signal and acquires images only inside a chosen window, so the result is a single phase or a breath-hold data set with fewer images and less imaging dose. In a retrospective acquisition the scanner oversamples every couch position for at least one full breathing cycle while the trace is recorded, and the images are sorted afterward into phase or amplitude bins. A ten-phase 4DCT is retrospective, which is why it produces on the order of a thousand or more images and a higher CT dose, and why it can also deliver a maximum-intensity, average-intensity, and minimum-intensity projection from the same scan.

Phase versus amplitude. Phase-based sorting or gating divides each cycle by time: 0 percent is end-inhale, 50 percent is near end-exhale, and a gate around end-exhale might be the 30 to 70 percent phases. It assumes a regular period and misassigns slices when the patient's rhythm changes. Amplitude-based sorting or gating uses the displacement of the surrogate: the beam is on while the marker lies within a stated window of positions. It is more honest when the period is irregular, and its weakness is baseline drift, because a slowly shifting resting position moves the window off the anatomy it was set on. Both approaches rely on the surrogate following the tumor.

Duty cycle. The duty cycle is the fraction of the breathing cycle during which the beam is enabled. Typical gates run from about 30 to 50 percent. Narrowing the window reduces the residual motion inside the gate and reduces the duty cycle, so beam-on time stretches and the fraction takes longer; a 25 percent duty cycle quadruples the beam time. The planner chooses the window as a trade between residual motion and treatment time, and a patient who cannot hold a steady rhythm for a long fraction may be a better fit for an ITV or compression.

The MIP and its pitfalls. The maximum-intensity projection assigns each voxel the brightest value it took across the phases, so a solid tumor moving through dark lung paints its whole excursion as a bright envelope that can be contoured as the ITV in one step. It fails where the tumor abuts tissue of similar density, at the diaphragm, the chest wall, or the mediastinum, because the bright tumor merges with bright neighbors and part of the excursion disappears; there the ITV underestimates motion and the tumor should be contoured on each phase and the contours combined. A sorting artifact inside the MIP becomes a false ITV. The MIP is never the dose-calculation set.

Compression and breath hold. Abdominal compression is a passive technique: a plate or belt pressed on the upper abdomen limits diaphragm travel for lung and liver stereotactic treatments, typically cutting motion by about half rather than removing it. It suits a patient who cannot follow breathing instructions or hold a breath, and it is uncomfortable, so it is rarely used for long courses. A breath hold is an active technique that needs patient cooperation and reproducible lung volume, held for roughly 15 to 25 seconds at a time. Deep-inspiration breath hold for left-sided breast treatment expands the lungs and pulls the heart inferiorly and posteriorly, away from the tangents, lowering mean heart dose and left anterior descending artery dose. Active breathing control enforces the volume with a spirometer and a valve; a voluntary hold is monitored by surface imaging or a marker block.

External surrogate versus internal fiducial. External surrogates include an infrared reflective marker block on the abdomen, a pressure belt, a spirometer, and the surface camera. They are non-invasive and carry no imaging dose, and they assume a stable relationship between the surface and the tumor. That relationship can have a phase lag, can be different at inhale and exhale, and can drift during a fraction. Internal surrogates include implanted radiopaque fiducials seen on kV imaging or fluoroscopy and implanted electromagnetic transponders. They sit near the tumor and track it directly, at the price of an invasive procedure, a pneumothorax risk for transthoracic lung placement, and the chance of marker migration. At least three markers are needed to detect rotation as well as translation.

Named systems. The infrared marker-block system (Varian RPM is the common example) is a camera that follows reflective dots on a small plastic block placed on the patient's abdomen; the vertical trace it produces is used to sort the 4DCT and to gate the beam, and it is purely an external surrogate. The electromagnetic transponder system (Calypso) implants three small wireless beacons in or near the target, excites them with an array over the patient, and reports their position continuously at several times per second without ionizing radiation; it is used mainly for prostate and is also available for lung. It is a localization and tracking system, not an imaging system, so it cannot show the anatomy around the beacons, and the array in the beam path and the beacons' MRI artifacts are its practical limits. Stereoscopic kV systems and surface-guidance systems are described in the IGRT module.

**Formulas**

Clock time ≈ beam-on time / duty cycle, so a 25 percent duty cycle quadruples a 3-minute beam to 12 minutes.

Percent of excursion left after compression ≈ residual motion / free-breathing motion; a plate that takes 1.6 cm to 0.8 cm leaves 50 percent.

**Worked example**

Given: a lower-lobe tumor moves 1.4 cm on 4DCT. The TG-76 threshold is 5 mm, so a management technique is considered. The patient is deaf and cannot follow coaching, so breath hold and coached gating are poor fits; abdominal compression reduces the excursion to 0.6 cm. The ITV is then drawn with the plate in place from a repeat 4DCT. Because the tumor touches the diaphragm, the MIP would blend the tumor into the dome, so the GTV is contoured on each of the ten phases and the union forms the ITV. Check: 0.6 cm is still above 5 mm, so the residual is covered by the ITV rather than ignored.

**Traps**

- Managing motion at 3 mm because "any motion matters," or ignoring 1.5 cm because "the margin covers it."
- Calling a 4DCT prospective. The sorting after the scan is what makes it retrospective.
- Mixing up the two gating modes: phase uses time within the cycle, amplitude uses displacement.
- Drawing the ITV from the MIP of a tumor sitting on the diaphragm.
- Treating a marker block or a surface as if it saw the tumor; treating electromagnetic transponders as an imaging device.

**Sources**

- AAPM TG-76, management of respiratory motion in radiation oncology, for the 5 mm threshold, the technique families, and the duty-cycle trade.
- AAPM TG-147 for nonradiographic localization, including electromagnetic transponders and infrared marker systems.
- ICRU 62 for the internal margin and the ITV.
