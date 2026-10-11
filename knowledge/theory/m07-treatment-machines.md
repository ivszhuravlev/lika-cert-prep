# Module 7. Treatment Machine Characteristics

Original notes for MDCB objectives I.2 and I.5.

## Parts of a Linac

**MDCB:** I.2, I.5

**What the exam expects**

You list the components in the order the beam encounters them, separately from the radiofrequency gear that never enters the patient beam. You know which parts move or are removed when the machine changes from photons to electrons, and which part defines a monitor unit.

**Core facts**

Radiofrequency power is produced by a magnetron (typical of lower-energy linacs) or a klystron (typical of higher-energy linacs) and carried in a waveguide. A circulator protects the RF source from reflected power. None of these parts sit in the treatment beam. A stem that asks for beam order and offers “klystron” as the first component is testing that distinction.

Photon beam order, from the electron source to the patient:

1. Electron gun. Injects electrons into the waveguide.
2. Accelerating waveguide. Standing-wave or traveling-wave structure. Electrons gain the stated energy (6 MeV electrons for a 6 MV photon beam).
3. Bending magnet. A 270° achromatic magnet is the common choice so electrons of slightly different energy still hit the target in a tight spot. Some low-energy machines shoot straight through and have no bend. A 90° bend exists on older designs.
4. X-ray target. Transmission target, high Z. Electrons strike it and produce bremsstrahlung.
5. Primary collimator. Fixed. Sets the largest possible field. It does not shape the clinical aperture.
6. Flattening filter. Thick in the center, thin at the edge, so the forward-peaked bremsstrahlung becomes usable and flat at a stated depth. Absent in a flattening-filter-free beam.
7. Monitor ion chamber. Two independent channels measure the beam that will be called a monitor unit. This is the dose-counting device. It is not the target and it is not the ion chamber you put in a water tank.
8. Secondary collimator jaws. Upper and lower jaws, often asymmetric, define the rectangular field.
9. Multileaf collimator. Usually the tertiary collimator, after the jaws. Leaf banks shape the aperture. Some designs integrate the leaves differently; the exam expectation is jaws, then MLC, as the usual clinical order.
10. Accessory mount. Physical wedge, block tray, or electron applicator, closest to the patient of the head components.

Electron beam order uses the same gun, waveguide, and bend, then changes the head:

- Target out.
- Flattening filter out.
- Scattering foil in, to spread the narrow pencil into a usable field.
- Monitor chamber still in the beam.
- Jaws set to the applicator size.
- Electron cone (applicator) on the accessory mount.

Leaving the target in the beam for electrons, or leaving the flattening filter in, is the wrong machine state. The scattering foil is thin metal. It produces a small bremsstrahlung contamination under the electron depth dose.

The monitor chamber, if it is unsealed, responds to temperature and pressure. Many linac chambers are sealed. A Farmer chamber in a water tank is a different device and does need a Ptp correction. Do not apply a weather correction to the MU counter unless the machine’s own chamber is the unsealed type described in its documentation.

Geometric penumbra is set by source size and by distances to the collimator and the patient. The bending magnet and target spot are why the effective source is small on a linac (millimeters) and large on Co-60 (about 1–2 cm). Large source, large penumbra.

**Traps**

Flattening filter placed after the monitor chamber, or before the target. MLC listed as the primary collimator. Klystron placed in the beam path. Electron mode described as “target in, foil out.” Monitor unit described as a gray. The MU is a count from the chamber, converted to gray by calibration under stated conditions (TG-51).

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-51 for what a calibrated MU means. Public blueprint I.2 and I.5.

## Linear Accelerator

**MDCB:** I.2, I.5

**What the exam expects**

You compare the machines the blueprint names: linac photons and electrons, Co-60, HDR (the source, not the linac), superficial and orthovoltage units, proton machines, and an MR-linac at the level of “what is different about the beam.” You know what raises megavoltage skin dose. You can use inverse square at short SSD, where a centimeter matters.

**Core facts**

A linac accelerates electrons and either hits a target (photons) or exits through a scattering foil (electrons). Photon energies in routine use are about 6–18 MV. Electron energies are about 4–20 MeV. Output is metered in monitor units. There is no radioactive source to decay and no timer in the cobalt sense, although the machine still has a backup time interlock.

Co-60 teletherapy. Source half-life 5.26 y, gammas 1.17 and 1.33 MeV, dmax about 0.5 cm, timer, output down about 1.09% per month. Source diameter about 1–2 cm gives a wider penumbra than a linac. No flattening filter of the linac type. Emergency that does not exist on a linac: a source stuck in the “on” position.

HDR. Typically Ir-192, half-life 73.8 days, mean gamma energy about 0.38 MeV, single source stepped through catheters. It is a brachytherapy afterloader, not a linac. Shielding and a treatment time come from activity and dwell, not from monitor units.

Superficial and orthovoltage units are kV x-ray tubes. They are the next lesson. They belong in the comparison: dmax at the surface, timer, HVL as the quality index, large f-factor effects in bone.

Protons. Cyclotron or synchrotron, clinical energies about 150–250 MeV, Bragg peak, no useful exit dose, clinical RBE 1.1. Passive scattering uses apertures and compensators. Pencil-beam scanning paints energy layers. The exam contrast with photons is finite range versus exponential attenuation.

MR-linac. A magnetic field is on during imaging and, on these systems, during treatment. Secondary electrons experience the Lorentz force. At tissue–air interfaces the electron return effect can increase skin dose relative to a conventional linac. The image is of the patient in the treatment position. Dose calculation has to account for the field. The photon beam is still a linac beam.

Skin dose on a megavoltage photon beam rises when you add bolus, when a tray or wedge sits close to the skin (electron contamination), when the beam is oblique, and when a posterior beam traverses a carbon-fiber couch. It also rises in a very large field. Removing the flattening filter changes head scatter and the spectrum slightly; it is not by itself a prescription for higher skin dose. Energy still dominates buildup: 18 MV has a deeper dmax than 6 MV if the beam is otherwise clean.

Approximate dmax values, confirm for the machine in Khan: Co-60 0.5 cm, 6 MV 1.5 cm, 10 MV 2.5 cm, 18 MV about 3.5 cm. Superficial and orthovoltage: surface.

**Formulas**

Inverse square, used here because short-SSD kV units punish a setup error:

Ḋ2 / Ḋ1 = (r1 / r2)^2

**Worked example**

Given: a superficial setup is calibrated at 20.0 cm SSD to the skin. The cone is set so the skin is actually at 19.0 cm SSD. dmax is at the surface, so the prescription point moved from 20 cm to 19 cm. Find the dose ratio.

Formula: Ḋ(19) / Ḋ(20) = (20 / 19)^2

Substitution: 20/19 = 1.0526

Arithmetic: 1.0526^2 = 1.108. The dose rate is 10.8% higher than the 20 cm calibration.

Compare a 1.0 cm error at 100 cm SSD: (100/99)^2 = 1.020, a 2.0% error.

Meaning: “it is a skin treatment, so SSD does not matter” is false. The skin is the calculation point. At 20 cm a 1 cm error is about 11%. At 100 cm the same 1 cm error is about 2%.

Usual wrong turn: the ratio (19/20)^2 = 0.903, which would be correct only if the skin had moved farther away, to 21 cm, or if the distances were swapped. Read which distance is the calibration and which is the actual setup.

**Traps**

Co-60 output left uncorrected for a month because “the half-life is 5 years.” HDR described as a linac energy. Proton RBE omitted or set to 2 (that 2 is w_R, a protection factor). MR-linac described as MRI only, with no effect on electrons. Skin dose assumed to fall whenever energy is raised, even with a tray in contact with the patient.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.5. Proton energy and RBE from the public sampled-skill list. Monthly Co-60 factor derived in the radioactivity notes from the 5.26 y recall half-life.

## Flattening Filters

**MDCB:** I.2, I.5

**What the exam expects**

You know what the filter does to profile, spectrum, and dose rate, and what changes when it is removed (FFF). You do not confuse the filter with a physical wedge or with a scattering foil.

**Core facts**

Bremsstrahlung is forward-peaked. Without a filter, the dose profile is high on the central axis and falls toward the edges. A flattening filter is a metal cone, thick on axis, mounted after the primary collimator and before the monitor chamber. It attenuates the center more than the edge until the profile is acceptably flat at a specified depth (often 10 cm). Flatness at one depth is not flatness at every depth.

The filter hardens the beam. The center, under the thick part, is hardest. Toward the edge the filter is thinner, the spectrum is softer, and the intensity can rise into “horns,” especially at shallow depth. Off-axis softening is a spectrum effect, not only a penumbra effect.

The filter is a major source of head scatter. Collimator scatter factor Sc changes with jaw setting partly because jaws hide or expose different amounts of that scatter. The filter is also a major source of photoneutrons when the beam energy is high enough (above about 10 MV).

Flattening-filter-free (FFF) beams pull the filter out of the path.

- The profile is peaked, not flat. Small fields used for SRS and SBRT do not need a flat 40×40 profile.
- Dose rate is substantially higher because the center of the beam is no longer attenuated by the cone. Commissioned FFF rates are often well above 1000 MU/min, against a few hundred MU/min for a flattened beam. Use the commissioned number for the machine rather than a universal ratio.
- Head scatter is reduced, so Sc varies less with field size.
- The spectrum is slightly softer than the flattened beam of the same accelerating potential, because the hardening filter is gone.
- Neutron production from the filter itself is removed. Other high-Z head parts can still produce neutrons at high energy.

A physical wedge is not a flattening filter. A wedge tilts the profile on purpose and has a wedge factor less than 1. A scattering foil is the electron-mode device. An FFF beam is not “flatter.” The name means the filter is free of the beam, that is, absent.

**Traps**

FFF described as a flatter profile. FFF described as a harder spectrum. Flattening filter left in the beam for electron treatments. Wedge factor and flattening-filter attenuation used as the same number. Off-axis points calculated with the central-axis energy only.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.5.

## Superficial Therapy Units

**MDCB:** I.5, I.2

**What the exam expects**

You separate contact therapy, superficial therapy, and orthovoltage by kV, by how HVL is stated, by SSD, and by the fact that dmax is at the surface. You know the Thoraeus filter and the beryllium window. You apply inverse square at short SSD and you correct a timer end effect when two exposures are given.

**Core facts**

The usual classification, as taught from Khan:

| Class | Potential | Quality stated as | Typical SSD | dmax |
| --- | --- | --- | --- | --- |
| Grenz rays | about 20 kV | very thin Al | short | surface |
| Contact therapy | 40–50 kV | about 1–2 mm Al | under about 2 cm | surface |
| Superficial | 50–150 kV | mm Al | 15–20 cm | surface |
| Orthovoltage (deep therapy) | 150–500 kV | mm Cu | about 50 cm | surface |
| Supervoltage | 500–1000 kV | — | — | near surface |

Megavoltage starts above about 1 MV and is the linac and Co-60 regime, with skin sparing.

Superficial cones set the SSD and the field. The useful beam is soft. A beryllium window lets it out of the tube. Added aluminum filtration is what brings the HVL up to the value the depth-dose table assumes. Treat with the filtration the calibration used. More aluminum, harder beam, lower output, slightly more penetration.

Orthovoltage uses a Thoraeus filter: tin, then copper, then aluminum, with aluminum closest to the patient. Tin and copper harden the beam. They also emit their own characteristic x-rays. The aluminum absorbs those characteristic photons so they do not reach the patient. A hooded anode cuts extrafocal radiation.

There is no skin sparing. The maximum dose is on the surface. Percent depth dose falls quickly. Bone receives more dose per exposure than muscle because the photoelectric effect still matters (f-factor). That is the clinical difference from 6 MV, where bone and soft tissue are much closer.

Dose is timer × output, plus an end effect if the shutter timing requires it. The two-exposure method is in the x-ray tube lesson. The short-SSD inverse-square example is in the linac comparison lesson: 1 cm at 20 cm SSD is about an 11% dose change.

Shielding of the patient for these energies is lead cutouts on the skin, not multileaf collimators. Lead glass or a lead mask is typical around an eye. The calculation is still an x-ray calculation: HVL in lead is small, and scatter from the cone is part of the output.

**Formulas**

The classification table is the exam device. Inverse square and the timer relation are the calculations:

Ḋ ∝ 1/r^2

R ∝ (t + δ), solved from two settings as in the x-ray tube lesson.

**Traps**

Orthovoltage HVL quoted in mm Al and superficial HVL quoted in mm Cu. dmax of a 250 kV beam placed at 1.5 cm because “that is dmax.” That 1.5 cm is 6 MV. Thoraeus layers reversed so aluminum is against the target and tin is against the patient; the aluminum has to be downstream of the tin and copper to absorb their characteristic radiation. Contact therapy (40–50 kV, SSD of a couple of centimeters) lumped with orthovoltage (50 cm SSD).

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.5.

## Linac Accelerator Quiz

This quiz checks beam order from gun to accessory mount, what is removed for electrons (target and flattening filter) and what replaces them (scattering foil and applicator), magnetron or klystron as RF hardware outside the beam, FFF as a peaked high-dose-rate beam, and superficial versus orthovoltage versus megavoltage versus protons. The traps are a flattening filter in electron mode, an FFF beam described as flat, Co-60 metered in monitor units, proton energies in the 6–20 MeV electron range, and dmax at depth for a 100 kV beam.
