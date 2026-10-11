# Module 26. DICOM Data Transfer

DICOM is the transfer standard between the scanner, the planning system, and the record-and-verify system. The exam asks which object carries which information, and what breaks when the links between objects are wrong.

## DICOM

**MDCB objectives:** III.9, II.1

**What the exam expects**

You can name the five radiotherapy objects: CT Image, RT Structure Set, RT Plan, RT Dose, and RT Image. You can say what each contains and which object references which. You can describe a transfer failure that moves an isocenter or drops a contour even though every file “imported.”

**Core facts**

DICOM is a standard for storing and sending medical images and the radiotherapy objects attached to them. A dosimetrist’s job at import is the localization objective in the blueprint: assess, import, translate, and validate. A successful network transfer is not yet a validated plan.

The five objects:

- **CT Image.** The axial (or helical) slices. Pixel values are Hounsfield units. Geometry is in the slice position, orientation, pixel spacing, and slice thickness. This is the dataset the dose is calculated on. A cone-beam or an MVCT may also be stored as a CT-class image and is still not the commissioned planning CT.
- **RT Structure Set.** The contours. Each region of interest is a set of points on the referenced slices, plus a name, a color, and a type. It references the CT series it was drawn on. A structure set with no image, or with the wrong image, is a stack of coordinates in space.
- **RT Plan.** The beams or arcs: energy, isocenter, monitor units, control points, MLC shapes, wedges, bolus, fraction group, and the prescription description as the planning system stored it. It references the structure set. It does not contain the pixel data of the CT and it does not contain the 3D dose grid.
- **RT Dose.** The 3D dose grid: origin, spacing, size, and the dose values. It references the plan. The grid can be coarser than the CT voxels. A pretty dose wash on the wrong origin is still a pretty wash in the wrong place.
- **RT Image.** A 2D image in a beam geometry: a digitally reconstructed radiograph or a portal image. It is not the planning CT. It carries its own pixel spacing and its relationship to the beam. Portal verification compares an RT Image with the DRR, which is also an RT Image, both tied back to the plan.

The reference chain runs CT Image → RT Structure Set → RT Plan → RT Dose. RT Images hang off the plan geometry. Break a link and the receiving system can still display something. What it displays may be shifted, empty, or calculated on the wrong frame.

Identity is a set of unique identifiers. The Frame of Reference UID is the one that says two objects share a coordinate system. Study, Series, and SOP Instance UIDs identify the exam, the series, and the single object. A spatial-registration object can store a rigid transform between two frames of reference. If that object is dropped on transfer, the MRI may import “successfully” and sit on the wrong origin relative to the CT.

Validation after import, before anyone plans or treats:

- Patient name and ID, orientation (head-first supine versus feet-first), and scan extent.
- Slice thickness and a continuous series, with no missing or duplicated slices.
- Structure names and a spot check that the cord, the target, and the external land on the right tissue.
- Isocenter coordinates against the simulation document.
- Energy, monitor units, fraction dose, and number of fractions against the prescription.
- Dose grid origin and spacing, and a point dose that matches the planning system you exported from.
- Frame of reference shared by the CT, the contours, and the dose.

Exporting a plan without its structure set, or a dose without its plan, is an incomplete transfer. Anonymization that strips UIDs or shifts the origin will import as an unlinked or displaced dataset. Fix the identifiers. Do not “nudge” a patient until the pictures look right and then treat.

Secondary systems (record-and-verify, a second-check calculation) may store a copy in DICOM or in a private format. The planning system remains the place the dose was computed. The record-and-verify system is the place the machine is told what to deliver. Those two copies have to match in energy, MU, MLC, and isocenter. A DICOM RT Plan is the usual language of that comparison.

**Formulas**

There is no dose formula in the transfer itself. There is a coordinate check. Suppose the planning CT origin and the imported dose origin differ by 5.0 cm in the superior–inferior direction and the pixel spacing is 1.0 mm. The dose grid has been translated by

5.0 cm / 0.1 cm = 50 pixels

along that axis. Every DVH computed on that shifted grid belongs to the wrong anatomy. The fix is to restore the shared frame of reference, not to reinterpret the DVH.

A structure set that references a series UID you do not have will not land on today’s CT even if the contour names look familiar. The reference is part of the data. The name “PTV” is only a label.

**Traps**

- Calling an RT Image the planning CT. RT Image is a DRR or a portal. CT Image is the volume.
- Sending an RT Plan alone and expecting contours and dose to appear.
- Ignoring a frame-of-reference mismatch because the import window said “complete.”
- Treating cone-beam DICOM as a density table for calculation.
- Anonymizing away the UIDs that tie dose to plan to CT.
- Assuming Hounsfield values survive every conversion unchanged. Confirm the density table on the receiving planning system. The HU module is where that table is used.

**Sources**

- The DICOM standard (NEMA), radiotherapy objects: CT Image, RT Structure Set, RT Plan, RT Dose, RT Image
- AAPM TG-132, for the registration object that aligns two frames of reference
- Departmental import checklists, which should implement the assess–import–translate–validate steps

## DICOM Data Transfer Mini Quiz

**MDCB objectives:** III.9, II.1

**Skills this quiz trains**

- Assign contours to RT Structure Set, beams and MU to RT Plan, the 3D grid to RT Dose, the volume to CT Image, and a DRR or portal to RT Image.
- Recite the reference chain from CT to structure set to plan to dose.
- Use the Frame of Reference UID as the coordinate contract.
- Reject an import that has not been checked against orientation, isocenter, fractions, and a point dose.
- Explain a 5 cm origin shift as a displaced dose grid, not as a new clinical plan.

**Traps**

- RT Image confused with CT Image.
- A complete transfer message accepted as validation.
- Dose displayed on a CT it does not reference.
- Private plan files assumed to be interchangeable with DICOM without an export test.

**Check yourself**

The receiving system shows beams and monitor units and an empty contour list. Which object is missing? The dose wash is 5 cm inferior to the tattoos on an otherwise correct CT. Which identifier class has failed?

Walk-through: The RT Structure Set is missing or is pointing at another series. The frame of reference (or the origin inside it) does not match the CT the dose is drawn on. Do not shift the patient by 5 cm to compensate. Repair the link and recheck a point dose.
