# Module 11. HU Unit Conversion to CT Density Table (TPS)

Original items. Gaps identified in the RM Review port: beam hardening and cupping, ring artifacts, bit depth of the HU scale, and the CT-versus-MRI prostate volume bias.

## HU Artifacts, Bit Depth and Modality Volume Bias

### Q1
Stem: The daily water-phantom scan on a CT simulator shows Hounsfield values near 0 at the edge but about minus 12 at the center, in a smooth radial dip. The cause is most likely:
A. Beam hardening that is not fully corrected, because rays through the center emerge with a higher mean energy and are attenuated less than the water calibration assumes
B. A single miscalibrated detector element
C. Photon starvation from an mAs that is too low
D. A phantom that is wider than the field of view
Answer: A
Objective: I.9
Why: Cupping is the signature of beam hardening: the polychromatic beam loses its soft photons through the long central path, so the center is reconstructed too low, and the bowtie filter and software correction are supposed to flatten it to within the TG-66 tolerance of a few HU. A bad detector element produces a ring, not a smooth dip. Low mAs raises random noise and streaks but does not bias the center downward. Truncation clips the edge of the object rather than lowering its middle.

### Q2
Stem: A planning CT shows several thin concentric circles centered on the scanner axis that run through the liver. The correct interpretation is:
A. Respiratory motion during the helical acquisition
B. A detector-channel calibration fault in a third-generation scanner, which needs an air calibration or service rather than a different reconstruction kernel
C. Beam hardening between the ribs
D. Normal appearance of a fourth-generation scanner
Answer: B
Objective: I.9
Why: In rotate-rotate geometry one detector element that reads consistently off is back-projected as a ring, so the artifact is a hardware calibration problem and the HU along the ring are false. Motion produces blurring and duplicated edges, not perfect circles. Beam hardening gives cupping and dark bands between dense objects. A fourth-generation scanner with a stationary detector ring is the design that does not produce rings.

### Q3
Stem: A prostate contoured on the planning CT measures 45 cubic centimeters. Published comparisons find that CT overestimates the gland by about 30 percent relative to MRI. The expected MRI volume is closest to:
A. 58 cm³
B. 31 cm³
C. 35 cm³
D. 45 cm³
Answer: C
Objective: I.9
Why: If the CT value is 1.30 times the MRI value, the MRI value is 45 divided by 1.30, which is 34.6 cubic centimeters. Check: 35 times 1.3 returns 45. 58 cm³ multiplies instead of dividing. 31 cm³ subtracts 30 percent of the CT value, which treats the overestimate as a fraction of the wrong volume. 45 cm³ assumes the modalities agree, which they do not because the apex, capsule and seminal vesicles cannot be separated on CT; that is why T2 MRI is fused for prostate targets.

### Q4
Stem: A CT scanner stores each pixel as a 12-bit value, with the Hounsfield scale running from minus 1,024 to plus 3,071. How many distinct attenuation levels does that represent, and how does it compare with the display?
A. 1,024 levels, the same as the display
B. 12 levels, one per bit
C. 3,071 levels, more than the display can show
D. 4,096 levels, far more than the 256 grays of an 8-bit display, which is why a window and level are applied
Answer: D
Objective: I.9
Why: Two to the twelfth power is 4,096, which is the span from minus 1,024 through plus 3,071 inclusive, and an 8-bit monitor shows 256 grays of which the eye separates only a few dozen, so a window selects which part of the scale is spread across the display. 1,024 is two to the tenth. 12 confuses the bit count with the level count. 3,071 is the top of the scale, not the number of values.
