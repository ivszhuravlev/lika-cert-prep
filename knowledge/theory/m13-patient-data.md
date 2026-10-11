# Module 13. Acquisition of Patient Data

Original notes for MDCB objectives II.1 and IV.4.

## General Introduction

**MDCB:** II.1, II.4, IV.4

**What the exam expects**

You can say what the planning data set has to contain before any beam is legal: a complete external contour, a density for every voxel the beam crosses, a known patient orientation, and markers you can tell from tissue. Contour corrections and inhomogeneity corrections are the two classical fixes when the patient is not a flat water tank. The CT scanner does not apply them. The planner does, or the algorithm does if it was commissioned to.

**Core facts**

The chain is: simulation under a written preparation, a CT (or a CT plus fused studies) that covers every beam entrance and exit, an external contour that includes the skin, target and organ contours, then a calculation. Window level, fusion, and a pretty DRR do not replace a missing slice or a truncated flank.

Orientation is part of the data. Head-first supine and feet-first supine are different orientations of the same couch. A left-right flip treats the other side of the patient. DICOM patient axes for a head-first supine scan: +x toward the patient’s left, +y toward the posterior, +z toward the head. Confirm the orientation tag on the data set before you believe a shift.

What you are correcting, in the two lessons that follow:

- Contour irregularity. The surface is not flat and not perpendicular to the beam. Missing tissue or extra tissue changes SSD along each ray. The old correction methods are isodose shift, effective SSD, and a TAR ratio. A modern algorithm traces the ray through the real surface. You still have to recognize the hand methods, because stems are written from them.
- Inhomogeneity. Lung, bone, air cavity, prosthesis. Equivalent path length is the hand method. It does not restore electronic equilibrium. The algorithm lesson comes later. The decision that belongs here is which density you assigned and whether that assignment is contrast, artifact, or real tissue.

A data set that fails the contour test cannot be saved by a clever inhomogeneity correction. Both errors move the dose.

**Traps**

Starting a monitor-unit calculation on a scan that cuts off the posterior skin for a PA beam. Treating the laser BB as tissue density. Assuming the planning system’s default body contour followed the skin when the window or the field of view clipped it.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-66. Public blueprint II.1 and II.4.

## Acquisition of Patient Data

**MDCB:** II.1, II.4, I.8

**What the exam expects**

You list what a complete simulation data set contains and how you would reject a bad one. You know which CT-derived image is legal for dose (average or a phase) and which is only for contouring (MIP). You know contrast, wires, and BBs have to be identified before the density table runs.

**Core facts**

Preparation is part of the data. Bladder filling, rectal emptying, fasting, contrast timing, a vaginal or anal marker, scar wires, and fiducials change the anatomy you plan on. The plan is valid for the anatomy that was scanned. A full-bladder scan planned and then treated empty is a different patient. The planning-target margin covers setup variation and internal motion. A positive surgical margin is disease and belongs in the clinical target, and inconsistent drawing is corrected on the contour, not absorbed into that margin. If the patient has gained weight and the separation over the field is larger than on the planning scan, tell the radiation oncologist before treatment. Do not deliver the old plan and mention the change afterward.

Scan extent. Include the target, the organs that carry a dose constraint, and the entrance and exit of every beam you might use, including arcs and non-coplanar beams. Breast fields need flash beyond the skin. A scan that starts at the clavicle and ends at the xiphoid is not a breast planning scan if the tangents exit into the lung and the heart constraint needs the whole heart. Slice thickness matches the target: thin for SRS, SBRT, and small nodes; thicker only for large palliative fields where partial volume will not hide the volume you are treating.

Indexed immobilization is in the scan. The device that will be on the couch for treatment is on the couch for the CT. A vac-lok scanned on a curved diagnostic table is not the treatment geometry.

Markers. BBs at the reference point, wires on scars and palpable nodes, rectal contrast or a marker for some pelvis protocols. Document them. A wire contoured as GTV, or a BB left at metal density in the beam, is a data error. Override the marker density when it sits in a calculation ray and is not tissue.

Contrast. Iodine raises HU through the photoelectric effect at kV. Megavoltage dose does not see iodine as bone. Override contrast-filled bowel, bladder, or vessels to the density of the contents you intend (usually water or soft tissue). Module 11 is the HU arithmetic.

4DCT. Contour the ITV from the MIP or from the union of phases. Calculate dose on the average CT or on a selected phase. On the average CT, assign the ITV a tumor density if motion blended it with lung. Do not calculate on the MIP.

Import checks before any contour is trusted: patient name and ID, study date, orientation (head-first versus feet-first, supine versus prone), slice spacing uniform, no missing or duplicated slices, left and right not flipped, field of view includes the skin, external contour closed. A fused MRI does not carry the density. The CT under it does.

Truncation. If the flanks are cut off, scatter is missing and a lateral beam’s path length is wrong. Rescan when you can. An invented contour extension is a clinical compromise, not “the same as a full scan.”

**Traps**

Dose on the MIP. Contrast left at 300 HU or higher for a 6 MV plan. A diagnostic contrast CT used as the planning CT without checking table shape, field of view, and slice coverage. Orientation read from the way the image “looks” on the screen rather than from the DICOM tag. A BB included in the external contour as a horn of tissue.

**Sources**

AAPM TG-66. Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint II.1 and II.4.

## Corrections for Contour Irregularities

**MDCB:** IV.4, I.10

**What the exam expects**

You can shift an isodose chart by k times the air gap, and you can apply an effective-SSD inverse-square correction to dmax. You know the shift is a fraction of the gap, not the whole gap, and you know the direction. You know Mayneord can adjust PDD for the new SSD and that it is inverse square only.

**Core facts**

Hand calculation tables assume a flat surface perpendicular to the central axis. Patients have sloping surfaces, missing tissue under a tangential beam, and bolus-like extra tissue. Three classical methods:

Isodose shift. Measure the gap h between the flat-phantom surface and the real surface along a fan line. Move the isodose chart along that line by k × h. The factor k falls with energy. The approximate factors candidates are expected to recall from Khan:

| Beam | k |
| --- | --- |
| below about 1 MV | 0.8 |
| Co-60 through about 5 MV | 0.7 |
| about 5–15 MV | 0.6 |
| about 15–30 MV | 0.5 |
| above about 30 MV | 0.4 |

Confirm the table in Khan before you treat a borderline energy as settled. The factor is less than 1 because scatter does not change as fast as primary attenuation. Shifting by the full gap overcorrects.

Direction. Missing tissue (surface farther from the source than the flat phantom, an air gap): less attenuation, so a given isodose reaches deeper. Shift the curves downstream, away from the source, by k × h. Extra tissue: more attenuation, shift the curves toward the source by k × h.

Effective SSD. Keep the depth measured from the actual skin. Adjust the dose at dmax by inverse square from the calibration SSD to the actual SSD:

relative output at dmax = [(SSD_cal + dmax) / (SSD_actual + dmax)]^2

Then multiply by PDD/100 for the depth and the SSD you are actually treating. If your only PDD table is for SSD_cal, Mayneord’s factor estimates the PDD at the new SSD. It does not include a scatter change.

TAR (or TMR) method. Compute the dose as if the point were at the depth under the real surface, using TAR or TMR at that depth and the inverse square to the point. This is the natural isocentric method: the point is fixed, the surface position changes the depth. It is the same physics as effective SSD, arranged for a fixed source-to-point distance.

Bolus is the physical version of filling the gap. A tissue-equivalent bolus that fills an air gap removes the need for an air-gap correction and destroys skin sparing under the bolus. That trade is intentional when the skin is the target.

**Formulas**

Isodose shift distance = k × h

- h: tissue deficit or excess along the ray
- k: energy-dependent factor from the table above

Effective SSD, dose at dmax relative to a calibration at SSD_cal:

Ḋ(dmax) / Ḋ_cal = [(SSD_cal + dmax) / (SSD + dmax)]^2

Mayneord, PDD from SSD1 to SSD2:

F = [(SSD2 + dmax) / (SSD1 + dmax)]^2 × [(SSD1 + d) / (SSD2 + d)]^2

**Worked example**

Given: 6 MV, dmax = 1.5 cm, calibration SSD 100 cm, output 1.000 cGy/MU at dmax. Along this ray the skin is 4.0 cm farther from the source than the calibration surface, so SSD = 104 cm. Depth of the point below the actual skin is 10.0 cm. The 100 cm PDD at 10 cm is 67.0%. Use the effective-SSD inverse square, then Mayneord, to estimate dose per MU at 10 cm. Also compute the isodose shift for a 3.0 cm air gap at 10 MV (k = 0.6).

Inverse square to the new dmax:

(101.5 / 105.5)^2

101.5 / 105.5 = 0.9621. Squared = 0.9256.

So the patient’s dmax receives 0.926 cGy/MU before percent depth dose.

Mayneord from 100 cm to 104 cm at d = 10 cm:

F = (105.5 / 101.5)^2 × (110 / 114)^2

105.5 / 101.5 = 1.0394, squared = 1.080.

110 / 114 = 0.9649, squared = 0.931.

F = 1.080 × 0.931 = 1.006.

PDD at 104 cm ≈ 67.0 × 1.006 = 67.4%.

Dose at 10 cm ≈ 0.9256 × 0.674 = 0.624 cGy/MU.

Isodose shift: 0.6 × 3.0 cm = 1.8 cm. Missing tissue, so the curves move 1.8 cm deeper, not 3.0 cm deeper.

Meaning: a 4 cm increase in SSD costs about 7% at dmax by inverse square. The PDD shape changes by under 1%. The dominant correction is the inverse square to dmax, not the Mayneord tweak. The isodose chart moves by 1.8 cm, not by the whole 3 cm gap.

Usual wrong turn: shift the isodose by the full 3 cm. Or apply inverse square from the source to the 10 cm point and also multiply by PDD, which counts the depth inverse square twice (PDD already includes it). Or move the isodose toward the source for missing tissue, which doubles the error instead of correcting it. Or use k = 0.6 for Co-60; cobalt’s factor on this table is 0.7.

**Traps**

k = 1. Mayneord applied on top of a TMR calculation that is already SSD-independent. Effective SSD used with the depth measured from the flat phantom instead of from the real skin. Bolus added in the plan and an air-gap correction applied as well.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, including the isodose-shift factors. Public blueprint IV.4.

## Corrections for Tissue Inhomogeneities

**MDCB:** IV.4, I.9

**What the exam expects**

You compute an equivalent depth from relative densities and you know what that number does and does not fix. You override contrast and metal. You know lung plus small field plus high energy is an electronic-disequilibrium problem, not a path-length problem.

**Core facts**

Equivalent path length (radiologic depth) replaces each physical thickness by density times thickness:

d′ = Σ ρ_i t_i

You then read TMR or TAR at d′ instead of at the physical depth d. The correction factor relative to a homogeneous water calculation is

CF = TMR(d′, r_d) / TMR(d, r_d)

using the same idea with TAR. This is the ratio-of-TAR idea reduced to a depth shift. It changes the primary attenuation. It does not move scatter from one place to another, and it does not put electronic equilibrium back.

A lung voxel at HU = −700 has μ/μ_water = 1 − 0.700 = 0.30 at CT energy (module 11). Using 0.30 as a relative density is the hand-calculation estimate. The planning system uses the commissioned curve, which is close to this for lung and not a straight line for bone.

Worked pattern: 5.0 cm of density 0.30 followed by 3.0 cm of density 1.0 is 1.5 + 3.0 = 4.5 cm equivalent, not 8.0 cm physical. You look up the depth-dose quantity at 4.5 cm.

Beyond a slab of lung, the equivalent-path method predicts higher dose than water because there was less attenuation. Inside the lung, in a small high-energy field, dose can instead fall because electrons leave the field and are not replaced. Path length predicts the wrong sign of the correction there. Convolution, superposition, and Monte Carlo model that lateral disequilibrium better than a pencil beam or a one-dimensional path length. Algorithm choice is scored later. The fact that path length is not enough is scored with this objective.

Bone. At megavoltage energies the correction is mostly the extra electrons per cubic centimeter. At orthovoltage the photoelectric effect raises bone dose well beyond a density ratio. Do not use a 6 MV inhomogeneity factor on a 250 kV bone calculation.

Air cavities. A cavity reduces attenuation and, past the cavity, the dose rebuilds as electrons are set in motion again. A nasopharynx or a trachea on a high-energy beam is a rebuild-up problem, not a pure equivalent-depth problem.

The Batho power-law method raises TAR values to a power that depends on (ρ_e − 1). It is a better one-dimensional attempt at scatter from the slab than raw path length. The depth index on each TAR is easy to get wrong. Confirm the labeling in Khan before you compute a Batho factor on an item. If the stem gives densities and thicknesses and asks for equivalent depth, it wants Σ ρ t, not Batho.

Overrides restated because they are density decisions: iodine contrast to water or tissue, metal artifact off the streak values, prosthesis to a known density, ITV in lung on an average CT to soft-tissue density. An override of the entire lung to 1.0 is a homogeneity assumption, not a correction. Know which one the plan used.

**Formulas**

d′ = Σ ρ_i t_i

- ρ_i: relative electron density, or relative physical density, as the method specifies
- t_i: physical thickness of slab i
- d′: equivalent depth in water

CF = TMR(d′, r_d) / TMR(d, r_d)

From HU, the attenuation ratio at CT energy is 1 + HU/1000. For lung in a hand calculation that ratio is the usual stand-in for ρ. For bone, use the calibration curve.

**Worked example**

Given: a 6 MV ray passes through 5.0 cm of lung and then 3.0 cm of unit-density tissue to the point. The lung is HU = −700. Use ρ = 1 + HU/1000. Physical depth is 8.0 cm. Find the equivalent depth. State which TMR you would read.

Formula: ρ_lung = 1 + HU/1000. d′ = ρ_lung × 5.0 + 1.0 × 3.0.

Substitution: ρ_lung = 1 − 0.700 = 0.300. d′ = 0.300 × 5.0 + 3.0.

Arithmetic: 1.50 + 3.0 = 4.5 cm.

Meaning: read TMR(4.5 cm), not TMR(8.0 cm). The lung removed 3.5 cm of equivalent water (5.0 − 1.5). Dose from primary transmission is higher than an all-water 8 cm calculation. If this same point were inside a 3×3 cm field at 18 MV, you would not trust that statement without a calculation that handles lateral electron loss. The hand answer is still 4.5 cm if the question asked for equivalent depth.

Usual wrong turn: d′ = (1 − 0.30) × 5 + 3 = 6.5 cm, using the density deficit as if it were the density. Or d′ = −700 × 5, nonsense. Or reading TMR at 8 cm and multiplying by 0.30 once, which is not the definition. Or adding a second 3.5 cm correction on a planning system that already used the CT densities, which double-counts the lung.

**Traps**

Path length used as a full account of lung dose in a small high-energy field. Contrast overridden to bone because the HU was high. Bone at 250 kV corrected with a Compton-only density. Batho exponents applied to the wrong depth. MIP densities used as ρ_i.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-65 for inhomogeneity corrections. Public blueprint IV.4 and I.9.

## Acquisition of Patient Data Mini-Quiz

This quiz checks a complete scan (skin, entrance, exit, orientation), MIP for lung ITV versus average CT for dose, contrast and marker overrides, isodose shift k×h in the correct direction, effective-SSD inverse square, and equivalent depth Σ ρ t. The traps are calculating on the MIP, shifting by the full air gap, using k for the wrong energy, measuring depth from the flat surface after the SSD has changed, and double-counting lung density on a CT that already contains it.
