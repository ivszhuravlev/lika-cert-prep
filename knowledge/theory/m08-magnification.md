# Module 8. Geometric Characteristics (Magnification, Minification)

Original notes for MDCB objective I.6.

## Magnification Tutorial

**MDCB:** I.6

**What the exam expects**

You compute magnification from distances and from measured sizes, convert an image measurement back to the object, and place the object at depth when the stem gives SSD and depth rather than source-to-object distance directly.

**Core facts**

On a diverging beam the image on a film or a detector distal to the patient is larger than the object. Magnification is the ratio of those sizes. It is also the ratio of distances from the source, because similar triangles share the source as the vertex.

The object is not always at the isocenter, and the image is not always at a fixed tray. Read the stem for three locations: source, object, image. Source-to-object distance is SOD. Source-to-image distance is SID. Older stems say source-to-film distance for SID.

If the object is at depth d below the skin,

SOD = SSD + d

SID = SOD + (object-to-image distance)

M is never less than 1 for a physical receptor beyond the object. A displayed image can be digitally minified. That scale factor is not geometric magnification. Geometric minification, when the word is used for a film, means recovering the true size by dividing by M. The factor 1/M is the minification that returns the object size.

**Formulas**

M = SID / SOD = (image size) / (object size)

object size = (image size) / M

image size = (object size) × M

minification factor used to recover true size = 1/M = SOD / SID

- M: magnification, dimensionless
- SID: source-to-image (source-to-film) distance
- SOD: source-to-object distance
- SSD: source-to-skin distance
- d: depth of the object below the skin along the ray

SOD = SSD + d, when d is given and the object is not in the skin plane.

**Worked example**

Given: SSD = 100 cm. A tumor is 10 cm deep. The film is 30 cm beyond the tumor. The tumor image on the film measures 5.09 cm. Find SOD, SID, M, and the true tumor size. Also find how large a 10.0 cm isocenter field would look if it were filmed at 150 cm with the object at isocenter (SOD = 100 cm).

Formula: SOD = SSD + d. SID = SOD + object-to-image distance. M = SID / SOD. True size = image / M.

Substitution for the tumor: SOD = 100 + 10 = 110 cm. SID = 110 + 30 = 140 cm. M = 140 / 110.

Arithmetic: M = 1.273. True size = 5.09 / 1.273 = 4.00 cm.

Check: 4.00 × 1.273 = 5.09 cm.

Second part, object at isocenter: M = 150 / 100 = 1.50. Image of a 10.0 cm field = 15.0 cm.

Meaning: the same 140 cm film distance gives M = 1.40 if you wrongly use SOD = SSD = 100, and M = 1.27 when the object is actually 10 cm deep. The true tumor is 4.0 cm, not 5.09 cm and not 5.09/1.40 = 3.64 cm.

Usual wrong turn: M = SOD / SID = 110/140 = 0.786, then “true size” = 5.09 × 0.786 = 4.00 cm by luck of multiplying when you should have divided, or 5.09 / 0.786 = 6.48 cm if you divide by a fraction that was already inverted. Write M = SID/SOD first, force M > 1, then divide the image by that number. The other miss is SOD = SSD when the object is at depth.

**Traps**

Image size × M reported as the object. That product is a twice-magnified image. Film at the isocenter (SID = SOD) assigned M = 0. SSD used in the numerator. Object-to-film distance used as SID. SID is measured from the source.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.6. The public sampled-skill statement of this relation is source-to-film over source-to-object.

## Magnification Concepts

**MDCB:** I.6

**What the exam expects**

You explain why M equals a distance ratio, when a number less than 1 is a real answer, and how magnification differs from minification on a display. You can do a second numeric case without confusing it with inverse square. Magnification scales length. Inverse square scales dose rate. They both use distances from the source and they are not the same formula.

**Core facts**

Similar triangles: the beam width grows in proportion to distance from the source. A field that is 10 cm wide at 100 cm is 15 cm wide at 150 cm. That is magnification of the field, and it is also why equivalent-square and blocking trays have to state the distance at which the size is defined. Collimator field size is stated at isocenter. If the isocenter lies anterior to the target, the posterior opening, quoted at isocenter, must be larger than the anterior opening to cover the same tissue, because the posterior beam has diverged less at that nearer target than it will at isocenter.

Minification is the operation of going back from the large image to the small object: divide by M. If a journal prints the film at half scale, the print has been minified by an extra factor of 2 on top of geometry. Geometric M does not know about the printer.

M = 1 only when the image plane and the object plane are the same plane. A portal imager panel is beyond the patient, so anatomy on an EPID is magnified. The planner’s DRR is a calculation, scaled to a stated plane, often isocenter. Compare lengths only in the same plane.

Dose rate does not grow with M. As the field image gets larger, the dose rate falls as 1/r^2. At 150 cm versus 100 cm, linear sizes are ×1.5 and dose rate is ×(100/150)^2 = ×0.444. A candidate who multiplies dose by the magnification will be high by a large factor.

Collimator angle and gantry do not change the definition of M. They change where the magnified image lands. The distance along the central axis is what enters SID and SOD for a central-axis object.

**Formulas**

M = SID / SOD

Length scales with r. Dose rate scales with 1/r^2.

Field size at distance r2 = field size at r1 × (r2 / r1)

**Worked example**

Given: a 12.0 cm object at SOD = 100 cm is imaged at SID = 140 cm. The picture is then printed at half the linear size of the film. Find the geometric magnification, the size on the film, and the size on the print.

Formula: M = SID / SOD. Film size = object × M. Print size = film size × 0.50.

Substitution: M = 140/100 = 1.40. Film = 12.0 × 1.40. Print = film × 0.50.

Arithmetic: film = 16.8 cm. Print = 8.4 cm.

Meaning: the film is magnified (M = 1.40). The print is smaller than the object (8.4 versus 12) because a digital or optical reduction was applied after a geometric magnification. Calling 8.4/12 = 0.70 “the magnification of the setup” mixes the printer with the geometry. The geometry is 1.40. To recover the object from the print you undo both factors: 8.4 / 0.50 = 16.8, then 16.8 / 1.40 = 12.0.

Usual wrong turn: one factor only, 8.4 × 1.40 = 11.8 cm, close to 12 and therefore easy to trust, but the print reduction was ignored. Or dose “magnified” by 1.40 so a 100 cGy/min calibration at 100 cm becomes 140 cGy/min at 140 cm. The dose rate at 140 cm is 100 × (100/140)^2 = 51.0 cGy/min.

**Traps**

M < 1 accepted for a film distal to the patient. Length and dose rate given the same ratio. Tray size at 65 cm compared with a field size at isocenter without a distance ratio. Similar triangles drawn from the isocenter instead of from the source.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.6.

## Magnification Quiz

This quiz checks M = SID/SOD, object size = image size/M, SOD = SSD + depth when the object is not at the skin, and the separation between a geometric magnification greater than 1 and a later minification on a display. The traps are the inverted ratio, multiplying the image by M to “correct” it, using SSD as SOD for a deep object, and scaling dose rate by M instead of by the inverse square.

## Block-Cutter Geometry and Block Shifts

**Objectives:** I.6

**What the exam expects**

You explain why a block cutter reproduces the simulator geometry, and you convert a distance drawn or measured on a film into the matching distance at the block tray and at the isocenter. The same ratio does all three jobs; the exam tests whether you pick the right pair of distances.

**Core facts**

A conventional block cutter is a hot-wire divergent cutter. The wire pivots about a point that stands in for the x-ray source. The film (or a printout of the DRR) is clamped at the same source-to-film distance (SFD) at which it was taken, and the styrofoam block sits at the same source-to-tray distance (STD) that the block will occupy in the treatment head. Because the wire passes through the pivot, the aperture traced on the film is cut with the same divergence the real beam has, and the block edge is automatically focused toward the source. If the film were placed at the wrong distance, the cut block would be the wrong size in the tray even though it matched the film.

Everything in the beam scales with distance from the source. A length L_film measured on the film at SFD corresponds to L_tray = L_film × STD / SFD at the tray and to L_iso = L_film × SAD / SFD at the isocenter plane. The tray is nearer the source than the isocenter, so a tray aperture is always smaller than the field it produces at isocenter: L_iso = L_tray × SAD / STD.

Block shifts follow the same rule. If a physician asks for the block edge to move 2 cm as seen on a film taken at 140 cm, the block in a tray at 65 cm moves 2 × 65/140 = 0.93 cm, and the field edge at isocenter (100 cm) moves 2 × 100/140 = 1.43 cm. Any movement at the tray is magnified toward the patient: a 5 mm positioning error of the block in the tray becomes 5 × 100/65 = 7.7 mm at isocenter. That is why tray slots are indexed and why TG-142 tolerances on block and MLC position are stated at isocenter.

For an SSD setup the same similar-triangle scaling converts a field or block size at the skin to the size at depth: size at depth d = size at surface × (SSD + d) / SSD. A 10 × 10 field at 100 cm SSD is 11 × 11 at 10 cm depth.

**Formulas**

Length at distance r2 = length at distance r1 × r2 / r1 (from the source)

Shift at tray = shift on film × STD / SFD

Shift at isocenter = shift on film × SAD / SFD

Size at depth = size at surface × (SSD + d) / SSD

**Worked example**

Given: a simulator film was taken at SFD 140 cm with the isocenter at 100 cm. The physician draws the block edge 2.8 cm farther from the central axis than the cut block. The block tray is at 65 cm from the source. Find the required block shift at the tray and the resulting field-edge shift at isocenter.

Formula: tray shift = film shift × STD / SFD. Isocenter shift = film shift × SAD / SFD.

Substitution: tray shift = 2.8 × 65 / 140. Isocenter shift = 2.8 × 100 / 140.

Arithmetic: 65/140 = 0.464. Tray shift = 1.3 cm. 100/140 = 0.714. Isocenter shift = 2.0 cm. Check: 1.3 × 100/65 = 2.0 cm, the same isocenter shift from the tray value.

Meaning: a 2.8 cm change on the film is 1.3 cm of block movement and 2.0 cm of anatomy. All three are the same geometric ray, read at three distances.

Usual wrong turn: moving the block 2.8 cm (no scaling), or multiplying by 140/65 and moving it 6.0 cm, which would be the film distance for a tray-plane measurement.

**Traps**

Clamping the film at the tray distance in the cutter. Scaling a tray-plane length by SAD/SFD instead of SAD/STD. Treating a block positioning error as the same size at the patient. Using SSD instead of SSD + d for a field size at depth.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, treatment-planning and field-shaping chapters. Bentel, *Radiation Therapy Planning*. Public blueprint I.6.

## Magnification Ring and Distance Scaling

**Objectives:** I.6

**What the exam expects**

You use a marker of known size to find the magnification of a film without knowing the distances, and you scale a measured length or a field size from one source distance to another.

**Core facts**

A magnification ring (or any marker of known dimension, such as a ruler or a seed of known length) is taped to the patient in the plane of interest, usually at the isocenter depth or on the skin at the level of the target. On the film the ring projects larger than life. The ratio of the measured image to the known true size is the magnification of that plane, and every other length lying in that plane divides by the same ratio. The ring is the practical substitute for SID/SOD when the object depth is unknown, when a film was taken on a diagnostic unit with unknown geometry, or when a brachytherapy source film must be reconstructed. If the ring is not in the plane of the object, the magnification it reports is for the wrong plane.

Field-size and length scaling between distances is the same similar-triangle ratio: a field quoted at 100 cm is quoted at any other distance by multiplying by the new distance over 100. A 15 × 15 field at 100 cm SAD is 12 × 12 at an 80 cm source-to-tray plane and 19.5 × 19.5 at 130 cm extended SSD. For total-body or extended-SSD treatments the needed distance is the ratio of the required field to the collimator maximum times 100 cm, and the collimator is rotated 45° so the diagonal (1.41 × the side) becomes the useful length.

**Formulas**

M = measured ring size / true ring size

True length = measured length / M

Size at r2 = size at r1 × r2 / r1

**Worked example**

Given: a 3.0 cm ring at the level of the target projects as 4.2 cm on the film. A node in the same plane measures 5.6 cm on the film. Find the magnification and the true node length.

Formula: M = image / true. True node = measured / M.

Substitution: M = 4.2 / 3.0. True node = 5.6 / M.

Arithmetic: M = 1.40. True node = 5.6 / 1.40 = 4.0 cm. Check: 4.0 × 1.40 = 5.6 cm.

Meaning: the film exaggerates every length in that plane by 40%. The distances were never needed.

Usual wrong turn: multiplying 5.6 by 1.40 to get 7.8 cm, or dividing the ring measurement by the node (4.2/5.6) and using 0.75 as the magnification.

**Traps**

Ring placed on the skin for a mid-plane object. Magnification reported as a number less than 1 for a film beyond the patient. Field at depth scaled by d/SSD rather than (SSD + d)/SSD. Dose rate scaled by the same ratio as length.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.6.
