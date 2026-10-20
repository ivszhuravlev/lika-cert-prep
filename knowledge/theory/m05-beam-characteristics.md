# Module 5. Characteristics of X-Rays and Particle Beams

Original notes for MDCB objectives I.3 and the weighting-factor portion of radiobiology that this module is assigned.

## Electromagnetic Radiation vs. Particulate Radiation

**MDCB:** I.3, III.3

**What the exam expects**

You contrast how photons deposit dose with how charged particles deposit dose. Photons are attenuated exponentially and have no finite range. Charged particles have a range set by stopping power. Protons have a Bragg peak. Clinical electrons do not have a useful one. You can say which radiations are directly ionizing.

**Core facts**

Photons (x-rays and gamma rays) are electromagnetic. No charge, no rest mass, speed c in vacuum, energy E = hν. They interact by probability. A photon that has not interacted still has its original energy. The beam intensity falls approximately exponentially. There is always a nonzero probability that a primary photon traverses the patient. That is an exit dose.

Electrons are light charged particles. They ionize continuously, scatter through large angles, and radiate bremsstrahlung in high-Z material. A clinical electron beam has a practical range and a finite depth where the dose falls to the bremsstrahlung tail. Multiple scattering washes out any sharp Bragg peak. Dose rises to a shallow dmax and then falls.

Percent surface dose on a clinical electron beam rises as the energy rises. Among 4 MeV electrons, 6 MV photons, 10 MV photons, and 16 MeV electrons, the 16 MeV beam has the highest skin dose, because the photon beams are still in buildup. The most probable electron energy at the surface is determined from the practical range. Mean energy then falls about linearly with depth, not as a quadratic. Percent depth dose increases with beam energy for both megavoltage electrons and photons. A finite range and a high surface dose are electron features, not shared with photons.

Protons and heavier ions are charged and much heavier. They scatter little, travel in nearly straight lines, and have a range fixed by energy. Stopping power rises sharply as they slow, producing the Bragg peak near the end of the range. Clinical proton energies are about 150–250 MeV. The clinical RBE used for protons is 1.1. There is essentially no dose beyond the range, apart from a small biologic and physics nuance at the distal end that module 19 treats in more detail. The machine fact for this module: range is finite, exit dose is not a photon-style exponential tail.

Alpha particles are helium nuclei, charge +2, high LET, range of centimeters in air and micrometers in tissue. They are not an external-beam modality.

Neutrons are uncharged particles. They are indirectly ionizing. In tissue the dominant interaction at therapy-relevant energies is elastic scatter on hydrogen, producing recoil protons that ionize. Neutrons do not have a Bragg peak of their own.

Attenuation describes photon (and neutron) removal. Stopping power describes how much energy a charged particle loses per unit path length. Mixing the two words is a standard miss. A “half-value layer” is a photon concept. A “range” is a charged-particle concept. Protons have both a range and, in a different sense, nuclear interactions that throw a small dose beyond the Bragg peak; the exam contrast is still range versus exponential attenuation.

Mass stopping power has a collision part (ionizations and excitations, which become dose) and a radiative part (bremsstrahlung). The radiative share grows with electron energy and with Z of the medium. That is why a high-energy electron beam on a high-Z target is an x-ray machine, and why a high-Z shield is a poor choice for a pure beta emitter if you wanted to avoid x-rays.

**Formulas**

Photon narrow-beam attenuation: I = I0 exp(−μx). No finite range.

Charged-particle range is the path length over which the kinetic energy is spent. Continuous slowing down approximation range comes from integrating 1/S, where S = −dE/dx is the total stopping power.

- S: stopping power, energy lost per unit path length
- Collision stopping power: the part that goes into ionizations and excitations
- Radiative stopping power: the part that goes into bremsstrahlung

LET, linear energy transfer, is the collision energy deposited in the immediate neighborhood of the track, in keV/μm. Photons and clinical electrons are low LET. Alphas are high LET. Proton LET rises sharply in the Bragg peak.

**Traps**

Assigning a Bragg peak to clinical electrons. Assigning an exponential HVL to a proton range. Calling protons indirectly ionizing. Quoting proton RBE as 1.0 because they are “sparsely ionizing like photons” over most of the track; the clinical factor used in planning is 1.1. Using 50 MeV as a typical proton treatment energy; that is electron-beam territory. Proton treatment energies are about 150–250 MeV.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.3. Proton energy and RBE as sampled in the public skills list tied to that blueprint.

## X-Ray Spectrum

**MDCB:** I.2, I.3

**What the exam expects**

You describe the beam the patient actually receives. A kV beam and a linac beam are polyenergetic bremsstrahlung. Co-60 is two gamma lines. You connect spectrum to HVL, to dmax, and to why bone dose is different at orthovoltage than at megavoltage. Production details were the previous module. This lesson is the beam as a clinical object.

**Core facts**

A therapy x-ray beam from a tube is specified by kVp and by HVL (mm Al in the superficial range, mm Cu in the orthovoltage range), plus SSD and filtration. Two beams with the same kVp and different HVL are not the same beam. HVL is the practical quality index for kV.

A linac photon beam is named by its maximum electron energy on the target (6 MV, 10 MV, 18 MV). The photons are bremsstrahlung from that endpoint down. The mean energy is well below the named MV. The flattening filter hardens the center of the beam more than the periphery, so the off-axis spectrum is softer. Beam quality for dosimetry is not the nominal MV. TG-51 uses TPR20,10 or a PDD(10) measurement. Those ratios are defined in the measurement module.

Co-60 emits 1.17 and 1.33 MeV gammas. The spectrum does not harden in the patient the way 120 kV hardens, because it is already two lines. The average is 1.25 MeV. dmax in water is about 0.5 cm. There is modest skin sparing, much less than at 6 MV.

Approximate photon dmax in water, for orientation, confirm for a named machine in Khan:

| Beam | dmax |
| --- | --- |
| Superficial and orthovoltage | surface |
| Co-60 | 0.5 cm |
| 6 MV | 1.5 cm |
| 10 MV | 2.5 cm |
| 18 MV | about 3.5 cm |

dmax increases with energy because secondary electrons are more energetic and travel farther before depositing their energy. Skin dose for a clean megavoltage beam is lower than the dose at dmax. Electron contamination from the head, a physical wedge or tray close to the skin, oblique incidence, bolus, and a carbon-fiber couch in a posterior field all raise the surface dose relative to that clean beam.

Penetration: higher energy, larger field (more phantom scatter), and larger SSD (Mayneord, inverse square only) each raise percent depth dose. The first two also change scatter. The SSD effect is mostly inverse square.

In the Compton range (therapy photons in soft tissue) dose tracks electron density. In the photoelectric range (orthovoltage and below, especially in bone) dose per roentgen is much higher in high-Z material than in muscle. An orthovoltage bone treatment and a megavoltage bone treatment are not interchangeable f-factor problems. The f-factor is in the units module.

Homogeneity: Co-60 is the near-monoenergetic case among common therapy beams, two lines close together. A 250 kV beam with HC well below 1 is the polyenergetic case. You already compute HC = HVL1/HVL2.

**Formulas**

Quality indices, stated here and used numerically in later lessons:

HVL for kV beams.

For megavoltage photons, TG-51 beam quality TPR20,10 = dose at 20 cm depth / dose at 10 cm depth, 10×10 cm² field, under the geometry TG-51 specifies. Confirm the measurement geometry in TG-51. Do not invent the PDD-to-TPR conversion coefficients; they are printed in that report.

Mayneord F, inverse-square-only SSD correction of PDD, is derived in the measurement module.

**Traps**

Calling a 6 MV beam monoenergetic at 6 MeV. Using kVp language for Co-60. Assuming a higher MV always lowers skin dose after a block tray has been added; the tray can put contaminant electrons on the skin. Using one HVL to characterize a linac the way you characterize 100 kV. Off-axis dose calculated with the central-axis spectrum only, ignoring softening under the thin part of the flattening filter.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-51 for the megavoltage quality index. Public blueprint I.2 and I.3.

## Neutrons 101 and Radiation Weighting Factors

**MDCB:** I.3, III.3

**What the exam expects**

You know how neutrons interact in tissue, where neutrons appear around a high-energy linac, and the difference between radiation weighting factor w_R, quality factor Q, and RBE. You recall w_R for photons, electrons, protons, alphas, and the energy dependence for neutrons.

**Core facts**

Neutrons in a department come from photonuclear reactions in a high-energy linac (practically, beams above about 10 MV), from the target, the primary collimator, and the flattening filter. They also come from some isotope sources and from proton machines. They are a shielding and a pacemaker problem (TG-203 later), not a prescribed treatment beam in ordinary external-beam practice.

In tissue, a fast neutron collides with a hydrogen nucleus. The masses are nearly equal, so the neutron can hand over any fraction of its kinetic energy up to all of it. The recoil proton is densely ionizing. Thermal neutrons are captured. Capture emits a gamma, and in some materials a charged particle. Borated polyethylene is used in doors because hydrogen slows the neutron and boron captures the thermal neutron. That shielding fact is used again in radiation protection; the interaction reason is this lesson.

Radiation weighting factor w_R converts absorbed dose in gray, averaged over an organ, into equivalent dose in sievert:

H_T = w_R × D_T

Photons: w_R = 1. Electrons: w_R = 1. Protons: w_R = 2 in ICRP 103 (ICRP 60 used 5; use the table the stem names). Alpha particles and heavy ions: w_R = 20.

Neutron w_R depends on energy. The older ICRP 60 step values, which many stems still use, are:

| Neutron energy | w_R |
| --- | --- |
| below 10 keV | 5 |
| 10 keV to 100 keV | 10 |
| 100 keV to 2 MeV | 20 |
| 2 MeV to 20 MeV | 10 |
| above 20 MeV | 5 |

ICRP 103 replaced the steps with a continuous function that still peaks near 20 around 1 MeV. If the stem does not say which publication, and it offers the step table, use the steps. Do not assign neutrons a flat w_R of 1.

Quality factor Q is a function of LET used in the older dose-equivalent definition at a point. w_R is assigned by radiation type and energy for organ equivalent dose. They are not interchangeable symbols. RBE is a measured biologic ratio for a stated endpoint and dose, not a protection factor. Proton RBE 1.1 is an RBE used for clinical dose. Proton w_R of 2 is a protection quantity. Do not plan a proton treatment with w_R = 2, and do not shield a proton vault with RBE 1.1 as if it were w_R.

Absorbed dose is gray for every radiation. Equivalent dose is sievert. A statement “the neutron dose was 1 cGy, w_R = 20, so the equivalent dose is 1 cSv” has dropped the weighting factor.

**Formulas**

H_T = w_R D_T

- H_T: equivalent dose to tissue T, sievert
- w_R: radiation weighting factor, dimensionless
- D_T: mean absorbed dose to that tissue, gray

**Worked example**

Given: an organ receives 1.00 cGy from alpha particles, w_R = 20. Find the equivalent dose in rem and in sievert. Photons are not involved.

Formula: H = w_R D, with D in gray giving H in sievert. Numerically, rad × w_R = rem, and 1 cGy = 1 rad.

Substitution: D = 1.00 cGy = 0.0100 Gy. w_R = 20. H = 20 × 0.0100 Sv.

Arithmetic: H = 0.200 Sv = 20.0 rem = 20.0 cSv.

Meaning: the absorbed dose is still 1 cGy. The protection quantity is 20 times larger because of w_R. For photons the same 1 cGy would be 1 cSv.

Usual wrong turn: 1 cGy × 20 = 20 Gy, mixing the sievert scale with a second factor of 100. Or leaving the answer as 1 cSv because “a centigray is a centisievert,” which is true only for w_R = 1.

**Traps**

Neutron w_R fixed at 20 for every energy, including thermal neutrons, when the stem uses the ICRP 60 table (thermal is 5). Proton clinical RBE 1.1 used as w_R. Q, w_R, and RBE treated as three names for one number. A Geiger counter described as the instrument that measures neutron equivalent dose; neutron survey instruments are a different detector. Photonuclear neutrons described as appearing at 6 MV in a clinically important amount. The usual threshold region quoted for linac neutron production is above about 10 MV.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. ICRP 60 step values and ICRP 103 continuous neutron function, as summarized in that literature. AAPM TG-203 is the later implanted-device reference for neutrons; the interaction fact belongs here. Public blueprint I.3 and III.3.

## Characteristics of X-Ray and Particle Beams Mini-Quiz

This quiz checks exponential attenuation versus finite range, which particles are directly ionizing, where the Bragg peak does and does not appear, approximate dmax rising from Co-60 to 18 MV, and w_R for photons, protons, alphas, and energy-dependent neutrons. The traps are a Bragg peak on a clinical electron curve, proton treatment energy confused with megavoltage electron energy, w_R = 1 for neutrons, and a 6 MV beam treated as monoenergetic 6 MeV photons.

## Light Field and Penumbra Definitions

**Objectives:** I.3, VII.1

**What the exam expects**

You state the rule that connects the light field to the dose distribution, you name the three penumbra components and the 80–20% definition of the physical penumbra, and you predict which setup change widens or narrows the penumbra.

**Core facts**

The radiation field size is defined at the 50% isodose line: the width between the two points, at the depth of maximum dose, where the dose has fallen to half of the central-axis value. The light field is adjusted at commissioning so that its edge projects onto that 50% line. That is why the light field edge is a 50% edge and not a 90% or 100% edge. A target placed exactly at the light edge receives about half the central-axis dose, and planners add margin so the 90% or 95% line, not the 50% line, covers the target. Light-to-radiation coincidence is checked monthly under TG-142 with a tolerance of 2 mm or 1% per side.

Geometric penumbra is the region at the field edge that sees only part of the finite source. It is set by the source diameter s, the source-to-collimator (diaphragm) distance SCD, and the source-to-point distance (SSD plus depth): P = s × (SSD + d − SCD) / SCD. It grows with a larger source, a longer SSD, a deeper point, and a collimator that sits farther from the patient (smaller SCD). It shrinks when the collimator is brought closer to the patient (larger SCD), which is why SRS cones and electron applicators sharpen the edge, and why a Co-60 source of 1–2 cm has a far wider penumbra than a linac spot of a few millimeters.

Transmission penumbra is the dose at the edge from photons that pass through the tapered tip of the collimator jaw or block. A divergent (focused) jaw face minimizes it; a non-divergent block or a rounded MLC leaf end contributes more.

Physical penumbra is what is actually measured on a profile: the lateral distance between the 80% and 20% isodose lines (some references use 90–10%; the bank uses 80–20% as the standard definition). It includes the geometric and transmission penumbra plus the lateral scatter of photons and electrons in the patient, which is why the physical penumbra widens with depth and with energy even when the geometry is fixed. Typical physical penumbra at 10 cm depth is about 6–8 mm for a 6 MV beam and larger for 18 MV.

**Formulas**

Geometric penumbra: P = s × (SSD + d − SCD) / SCD

- s: source diameter
- SCD: source-to-collimator distance (distal face of the jaw)
- SSD + d: source-to-point distance

**Worked example**

Given: a Co-60 unit with a 2.0 cm source, collimator face at 45 cm, SSD 80 cm. Find the geometric penumbra at 10 cm depth.

Formula: P = s × (SSD + d − SCD) / SCD

Substitution: P = 2.0 × (80 + 10 − 45) / 45

Arithmetic: 80 + 10 − 45 = 45. P = 2.0 × 45/45 = 2.0 cm.

Meaning: a 2 cm source at this geometry throws a 2 cm geometric penumbra at 10 cm depth. Repeat with a 0.3 cm linac spot at SCD 50 cm and SSD 100 cm: 0.3 × (100 + 10 − 50)/50 = 0.36 cm. The source size is the dominant difference between cobalt and linac edges.

Usual wrong turn: dropping the depth and using SSD − SCD only (giving 1.56 cm), or inverting the ratio so a larger SCD appears to widen the penumbra.

**Traps**

Placing the light field edge at the 90% line. Calling the 80–20% distance the geometric penumbra. Claiming penumbra decreases with depth. Believing a larger field size changes the geometric penumbra (it does not; it changes the scatter contribution only slightly).

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, field-shaping chapter. AAPM TG-142 for the light-radiation tolerance. Public blueprint I.3 and VII.1.

## Flattening-Filter-Free Beam Facts

**Objectives:** I.3, I.5

**What the exam expects**

You give the direction and approximate size of each change when the flattening filter is removed: depth dose, surface dose, dose rate, spectrum, profile shape, and head scatter. Module 7 covers the hardware; this lesson is the beam.

**Core facts**

Removing the filter removes the material that hardened the central axis. The FFF spectrum is softer, so the beam is slightly less penetrating. For 6 MV the percent depth dose at 10 cm drops by about 3 percentage points (roughly 67% flattened to about 64% FFF for a 10 × 10 field) and dmax moves a few millimeters shallower. For 10 MV the drop is similar, from about 73% to about 71%. An FFF beam is therefore specified by its own PDD or TPR, not by the flattened beam's quality index.

Surface dose is higher with FFF. The softer spectrum and the loss of the filter's absorption of low-energy photons and contaminant electrons raise the buildup-region dose by several percent of the maximum. Together with the higher dose rate this is why skin reactions are watched in FFF SBRT.

Dose rate rises by a factor of about 2 to 4 because the center of the beam is no longer attenuated. Commercial values are about 1400 MU/min for 6 MV FFF and 2400 MU/min for 10 MV FFF, against 600 MU/min for flattened beams on the same machine. The increased dose per pulse raises ion recombination in the measuring chamber, so Pion must be re-determined for FFF.

The profile is forward-peaked, falling off smoothly from the central axis without horns. Flatness is not a meaningful specification; the beam is characterized by the unflattened profile shape and by symmetry. Head scatter is lower and the collimator scatter factor varies less with field size. Out-of-field leakage per MU is lower, and photoneutron yield per MU drops for high-energy beams because the filter was a high-Z source. The number of monitor units for a given dose is similar to or somewhat larger than the flattened beam's, because output per MU is still calibrated to 1 cGy/MU at reference conditions; the gain is in time, not in MU.

**Traps**

Describing FFF as a harder beam. Quoting a higher PDD for FFF. Saying FFF lowers skin dose. Using the flattened beam's TPR20,10 for an FFF beam. Assuming 2400 MU/min applies to every FFF energy; it is the 10 MV FFF figure.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. AAPM TG-51 addendum for FFF reference dosimetry and recombination. Vendor commissioning data for the 1400/2400 MU/min dose rates. Public blueprint I.3 and I.5.

## Choosing a Skin Beam and Surface Dose Numbers

**Objectives:** I.3

Skin and very superficial lesions can be treated with low-energy x-rays or with electrons, and the exam asks you to compare them on surface dose, depth of fall-off and dose to underlying bone.

Superficial x-rays (about 50 to 150 kVp, HVL of a few millimeters of aluminum) and orthovoltage x-rays (about 150 to 500 kVp, HVL of a few millimeters of copper) have their maximum dose at the surface: the percent surface dose is 100% because there is no buildup region at these energies. The depth dose falls off by attenuation and inverse square, slowly enough that a 2 cm thick lesion is still well covered by orthovoltage, but there is no sharp end to the beam, so tissue well beyond the target keeps receiving dose. Because the photoelectric effect dominates below a few hundred keV, bone absorbs several times more dose per unit mass than soft tissue (the f-factor for bone is up to about 4 at 50 keV against 1 for water), so an orthovoltage field over the scalp or the shin deposits far more dose in bone than the prescription suggests. These beams are prescribed at the surface (Dmax equals the surface dose), they need no bolus, and the small cones give a sharp field edge.

Clinical electron beams (6 to 20 MeV) enter with a surface dose below 100%, rise to a dmax a centimeter or more deep, and then fall off steeply to a practical range of about E/2 cm, with only a few percent of bremsstrahlung tail beyond it. The surface dose rises with energy: about 75% for 6 MeV, around 85% for 9 to 12 MeV, and about 95% for 18 to 20 MeV. The reason is scattering: low-energy electrons are scattered through larger angles in the first millimeters of tissue, so fluence builds up more between the surface and dmax, whereas high-energy electrons travel nearly straight and the dose at the surface is already close to the maximum. Bone dose with electrons is close to soft-tissue dose per gram because collisional stopping power is nearly Z-independent (bone is actually slightly lower per gram because of its lower electron density per gram), so electrons protect bone and the tissue behind the range. The price is the lower surface dose, which is why skin targets treated with electrons get 0.5 to 1 cm of bolus to pull dmax to the surface, and the wider penumbra at depth.

Megavoltage photons behave the opposite way to electrons at the surface. The surface dose for a 10 × 10 cm open field is about 15 to 20% for Co-60, 10 to 15% for 6 MV and under 10% for 18 MV: as the energy rises the secondary electrons are more forward-directed and travel farther, so the buildup region lengthens (dmax 0.5, 1.5, 3.0 to 3.5 cm) and the entrance dose falls. Surface dose rises with field size, with trays or blocks close to the skin, with FFF beams, and with oblique incidence; it is lowest for a small field at high energy with nothing in the beam.

**Traps**

Electron surface dose said to fall with energy (that is the photon behavior). Orthovoltage assigned a buildup region. Bone dose with orthovoltage treated as equal to soft tissue. Electrons for skin prescribed without bolus at 6 MeV and the 75% entrance accepted as adequate. Co-60 given the lowest surface dose because it is "older".

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*, electron beam therapy and dose distribution chapters. AAPM TG-25 and TG-70 for electron percent depth dose characteristics. Standard orthovoltage f-factor tables.
