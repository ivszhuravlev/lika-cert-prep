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
