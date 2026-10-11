# Module 18. IGRT

This module is the toolbox: which image is acquired, what anatomy it can show, and how a match becomes a couch correction. The ways those images mislead you are module 32. Learn the tool here, then learn its limits.

## Treatment Verification

**MDCB objectives:** II.6, I.8

**What the exam expects**

You can name the common image-guidance methods and the anatomy each one actually sees. You can say what the reference image is (planning CT or DRR from that CT). You can describe a shift as a rigid correction in the patient coordinate system, including the difference between a three-degree couch and a six-degree couch. You can separate imaging used to aim the beam from the planning CT used to calculate dose.

**Core facts**

Image guidance compares the patient on the treatment table with the patient the plan was calculated on. The comparison produces a rigid correction: translations, and rotations if the couch and the protocol allow them. After the couch moves, a second image is the confirmation that the correction landed.

The reference for a cone-beam or a CT-on-rails match is the planning CT, in the same orientation (head-first supine or whatever was simulated). The reference for a portal image is the digitally reconstructed radiograph from that planning CT in the same beam’s-eye view. Matching today to yesterday’s cone-beam walks the isocenter off the anatomy that was planned.

What each method can show:

| Method | What you can verify |
| --- | --- |
| kV orthogonal pair | Bone and fiducials on two projections. Two 2D images support a 3D translation. Soft tissue and rotation are weak. |
| MV portal / EPID | The treatment aperture in the beam’s-eye view, and bony alignment. Soft-tissue contrast is poor. This is the image of the beam you are about to treat with. |
| kV CBCT | A volume: soft tissue, bone, fiducials, bladder filling, rectal gas. Acquired on the linac. Used to align. It is a different dataset from the planning CT. |
| MVCT (helical tomotherapy) | A volume from the treatment-energy beam, detuned for imaging. Soft-tissue contrast is less than kV CBCT. It is the onboard image for that machine. |
| Fiducial match | Marker position as a surrogate for the target (prostate, liver). The marker is not the GTV. |
| Surface guidance (SGRT) | The external surface, often in real time, including breath-hold. Internal targets that are not locked to that surface are invisible to it. |
| Fluoroscopy or electromagnetic tracking | Intrafraction motion of a surrogate. |

Daily imaging is the usual expectation for stereotactic treatments and for many modulated courses. The required frequency and the shift that triggers a physician or a physics review are departmental. Confirm those action levels in the departmental IGRT policy. AAPM TG-142 is the machine QA document for the imager (geometry, image quality, isocenter coincidence). A TG-142 imaging tolerance is not the same number as the clinical margin or the clinical action level.

A practical verification sequence:

1. Confirm the patient, the site, the plan, the energy, and the accessories (bolus, mask, knee rest).
2. Acquire the image the protocol names.
3. Match on the anatomy the protocol names. Pelvic bone, prostate soft tissue, fiducials, and surface are four different matches.
4. Apply the translation. Apply a rotation only when the couch has that degree of freedom and the protocol allows it.
5. Decide whether the residual, or the size of the shift, needs a repeat image.
6. Treat. For gated or breath-hold treatment, the gating trace has to match the simulated phase or the simulated deep-inspiration level, not merely the average free-breathing surface.

Cone-beam geometry is a cone, so one rotation covers a limited length and a limited diameter. Anatomy outside that field of view is truncated. The Hounsfield numbers are not the commissioned planning-CT density table. Module 32 is the full list of reasons a cone-beam must not be dropped into the dose engine as if it were the simulation CT.

Respiratory motion management is verified, not assumed. A four-dimensional planning CT defined an internal target over the breathing cycle. Guidance has to confirm that today’s motion is the motion that was planned: amplitude, phase, breath-hold level, or an internal surrogate such as an implanted marker. Surface guidance is well suited to a breast deep-inspiration breath hold because the target is tied to the surface. It is a poor sole check for a prostate.

Shifts are reported in a coordinate system. Know the sign convention your department uses (IEC couch coordinates versus patient left–right). A correctly computed 0.7 cm left shift applied with the opposite sign is a 1.4 cm error. Read the direction in the room, not only the number on the screen.

**Formulas**

The couch correction is rigid. The same small-angle estimate used for registrations tells you when a rotation matters. A point a distance r from the match center, rotated by an angle θ in radians, is displaced by about rθ.

Example: the match is centered at the nasopharynx. A supraclavicular node is 20 cm inferior. The proposed correction is a 2° pitch and no translation.

2° = 2 × π / 180 = 0.0349 rad.

Displacement at the node ≈ 20 × 0.0349 = 0.70 cm.

Seven millimeters at the end of the field is a real setup change. On a three-degree-of-freedom couch you cannot apply that pitch. You then either accept a compromise translation or reset the patient. On a six-degree couch you can apply it only if the protocol says rotations of that size are allowed, and you still re-image.

**Traps**

- Using yesterday’s cone-beam as the new reference.
- Matching bone for a target that moves inside the pelvis or the lung.
- Treating a surface-guidance camera as an internal image.
- Reading a TG-142 imager tolerance as the clinical PTV margin.
- Applying a rotation the couch cannot perform, or applying the correct centimeters in the wrong direction.
- Calling a portal image a soft-tissue volumetric match. A portal image shows the aperture and the bone in that beam’s-eye view.

**Sources**

- AAPM TG-142, quality assurance of medical accelerators, including imaging geometry
- AAPM TG-179, quality assurance for CT-based image guidance
- AAPM TG-147, nonradiographic localization, including surface imaging
- ICRU 62, setup margin and internal margin, which are the uncertainties image guidance is trying to shrink

## IGRT Mini-Quiz

**MDCB objectives:** II.6, I.8

**Skills this quiz trains**

- Match the image type to the anatomy it can prove: bone, aperture, soft tissue, fiducial, or surface.
- Name the planning CT or the DRR as the reference, and keep a prior cone-beam from becoming the reference.
- Separate a translation-only couch from a six-degree couch.
- Estimate the displacement at the end of a long target from a small rotation.
- State that cone-beam Hounsfield numbers are not the planning density table.
- Place TG-142 on the imager and the departmental policy on the clinical action level.

**Traps**

- Bone match accepted for prostate localization.
- Surface guidance accepted as proof the prostate or a lung tumor is on target.
- Portal image described as a soft-tissue 3D match.
- A 2° rotation dismissed at a site 20 cm from the match point.
- Imaging QA tolerance copied in as the PTV expansion.

**Check yourself**

A left breast deep-inspiration breath-hold plan is monitored with surface guidance, and the surface is within the departmental tolerance for the whole fraction. A prostate plan the same afternoon is also on the surface-guidance system, with an equally quiet surface trace and no cone-beam and no fiducials. Which case has the target tied to the signal the camera can see?

Walk-through: The breast target moves with the chest wall, so the surface is a direct surrogate for that treatment. The prostate moves with rectum and bladder and is invisible to a surface camera. A quiet skin trace does not locate the prostate. That prostate fraction still needs the internal check the protocol names (fiducials or soft-tissue cone-beam).
