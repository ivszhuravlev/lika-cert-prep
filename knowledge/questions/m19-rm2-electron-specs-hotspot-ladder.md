# Module 19. Isodose distributions and dose metrics

Original items. Electron profile specifications, cut-out limits, virtual SSD, hot-spot ladders by technique, lead-edge and air-cavity hot spots, and penumbra definitions.

## Electron Beam Specifications and Cut-out Limits

### Q1
Stem: A physicist is asked at which depth the flatness and symmetry of a 12 MeV electron beam are specified. Which depth is correct?
A. At dmax, the same plane used for photon profiles
B. At 10 cm, so electron and photon profiles can be compared directly
C. In a plane at the depth of the 95 percent isodose beyond dmax
D. At the practical range, where the profile is widest
Answer: C
Objective: I.3
Why: TG-25 specifies electron flatness and symmetry in a reference plane perpendicular to the central axis at the depth of the 95 percent isodose beyond dmax, which is close to the therapeutic depth of the beam. Photon profiles are classically taken at dmax or at 10 cm, but those depths have no special meaning for an electron curve whose shape changes rapidly with depth. The practical range is where the electron dose has essentially vanished, so there is no useful profile to flatten there.

### Q2
Stem: In the electron reference plane, two points at equal distances on opposite sides of the central axis read 102.4 percent and 99.6 percent of the central-axis value. What is the symmetry as a mirror-point difference, and does it meet the TG-25 criterion of about 2 percent?
A. 1.4 percent, passes
B. 2.8 percent, fails
C. 5.6 percent, fails
D. 0.7 percent, passes
Answer: B
Objective: I.3
Why: Electron symmetry in TG-25 is the difference between mirror-image points in the reference plane: 102.4 − 99.6 = 2.8 percent. Check: 99.6 + 2.8 = 102.4. That exceeds the 2 percent criterion, so the beam fails. Halving the difference to 1.4 percent is the deviation of each point from the mean, not the mirror difference. Doubling it to 5.6 percent has no definition. Dividing by four to get 0.7 percent is not a recognised convention.

### Q3
Stem: Using the lateral-equilibrium rule that an electron field must be at least about E over 2 centimeters wide to behave as a large field, what is the smallest cut-out width for a 16 MeV beam that can use the open-cone output and depth-dose data?
A. 4 cm
B. 5 cm
C. 16 cm
D. 8 cm
Answer: D
Objective: III.1
Why: The lateral range of the electrons is about the practical range, Rp ≈ E/2 cm, so the smallest field dimension should be at least 16/2 = 8 cm. Check: 8 × 2 = 16 MeV. A 4 cm width uses E/4, which is a therapeutic-depth rule, not a field-width rule. A 5 cm width is E/3.2, the 90 percent depth rule. Equating the width to the energy in centimeters, 16 cm, has no basis and would call almost every clinical field small.

### Q4
Stem: Four electron cut-outs are proposed. Which one has lost lateral electron equilibrium and therefore needs its own measured output factor and depth-dose curve rather than the open-cone data?
A. 6 MeV with a 4 by 6 cm cut-out
B. 12 MeV with a 5 by 9 cm cut-out
C. 9 MeV with a 5 by 5 cm cut-out
D. 16 MeV with a 9 by 12 cm cut-out
Answer: B
Objective: III.1
Why: The test is the smallest dimension against E/2 cm. For 12 MeV the threshold is 6 cm and the 5 cm side falls below it, so output drops, dmax moves toward the surface, and the depth-dose curve shortens; it must be measured. For 6 MeV the threshold is 3 cm and 4 cm passes. For 9 MeV the threshold is 4.5 cm and 5 cm passes. For 16 MeV the threshold is 8 cm and 9 cm passes. Area and the long side do not decide the question; the short side does.

### Q5
Stem: A clinic measures the virtual source distance of its electron beams. Which pattern should it expect?
A. The virtual SSD equals the nominal 100 cm for all energies because the photon target defines the source
B. The virtual SSD is longer than 100 cm, most so for high energies and large cones
C. The virtual SSD is shorter than 100 cm, with the largest shortfall for low energies and small cones
D. The virtual SSD is shorter than 100 cm only for energies above 15 MeV
Answer: C
Objective: I.3
Why: Scattering in the foils, monitor chamber, applicator, and air makes the electron beam behave as if it came from a point closer to the patient than the target, typically 80 to 95 cm. The shortfall is largest where scatter is the biggest share of the fluence, which is at low energy and for small cones. The photon target position is irrelevant to where the scattered electron fluence appears to originate. The effect is not confined to high energies; it is weakest there.

### Q6
Stem: An electron beam has a virtual SSD of 85 cm and dmax of 1.5 cm. The applicator is used at a 10 cm air gap beyond the standard set-up. Using inverse square from the virtual source, by what factor does the output at dmax change relative to the standard set-up, to three decimals?
A. 0.829
B. 0.803
C. 0.896
D. 0.723
Answer: B
Objective: III.1
Why: The distances from the virtual source are 85 + 1.5 = 86.5 cm at the standard set-up and 96.5 cm with the gap; the factor is (86.5/96.5) squared = 0.896 squared = 0.803. Check: 0.803 × 96.5 squared = 0.803 × 9312 = 7478, and 86.5 squared = 7482, which agree to rounding. Using the nominal 100 cm gives (101.5/111.5) squared = 0.829, about 3 percent too high. The unsquared ratio 0.896 forgets to square. The ratio (85/100) squared = 0.723 compares the virtual and nominal distances and is not an output change.

## Hot-Spot Ladders, Lead Edges, and Penumbra Definitions

### Q1
Stem: A PTV prescribed to 50 Gy has a maximum of 54.6 Gy and a minimum of 49.0 Gy. What is the inhomogeneity index defined as Dmax divided by Dmin?
A. 1.114
B. 0.112
C. 1.092
D. 0.897
Answer: A
Objective: III.12
Why: Dmax/Dmin = 54.6/49.0 = 1.114. Check: 49.0 × 1.114 = 54.6. The value 0.112 is the range divided by the prescription, (54.6 − 49.0)/50, which is a different, difference-based index. The value 1.092 is Dmax divided by the prescription and ignores the minimum. The value 0.897 is Dmin/Dmax, the ratio inverted.

### Q2
Stem: A head-and-neck IMRT plan shows a global maximum of 113 percent of the prescription inside the PTV. How should the reviewer judge this number?
A. It exceeds any accepted range and the plan must be re-optimized
B. It is within the 110 to 115 percent band usual for IMRT and VMAT, although above the 107 to 110 percent expected of a 3D conformal plan
C. ICRU 50 limits every technique to 107 percent, so the plan fails
D. It is typical only of stereotactic plans, which run 125 to 200 percent
Answer: B
Objective: III.12
Why: Inverse-planned IMRT and VMAT trade homogeneity for conformity, and internal maxima of about 110 to 115 percent inside the target are routine. The 107 percent figure from ICRU 50 was written for conventional point-prescribed plans and is extended to about 110 percent for 3D conformal and field-in-field work, not applied to IMRT. Stereotactic plans prescribe to a low isodose line, so their 125 to 200 percent maxima are a different design, and 113 percent would be unusually homogeneous for them.

### Q3
Stem: A lead shield rests directly on the skin at the edge of an electron field to protect the lens. Where does the characteristic hot spot appear?
A. Under the lead, because electrons backscatter from the shield into the shielded tissue
B. At the exit side of the patient beyond the practical range
C. Just inside the open field beside the lead edge, as a tear-drop shaped region a few millimetres under the surface
D. Nowhere; the shield only lowers dose and never raises it
Answer: C
Objective: III.1
Why: Electrons striking the vertical face of the shield scatter into the adjacent open tissue, so a tear-drop hot spot forms just inside the field next to the lead edge, while the dose under the lead is low. Backscatter does raise dose on the upstream face of an internal shield, which is a different geometry (shield inside the mouth or under the eyelid), and even there the hot spot is in the tissue in front of the lead, not under it. No electron dose exists beyond the practical range. Coating the shield edge with wax or bolus absorbs the scattered electrons and removes the hot spot.

### Q4
Stem: An electron field treats the nose and ethmoid region, and the nasal cavity is left air-filled. Compared with a water calculation, what does the air cavity do to the dose?
A. It raises the dose and extends the range beyond the cavity, with hot spots in the tissue beside the cavity walls
B. It lowers the dose beyond the cavity because air scatters electrons more than tissue
C. It has no effect, because electron dose depends only on depth from the skin
D. It shifts dmax deeper on the central axis but leaves the lateral dose unchanged
Answer: A
Objective: III.1
Why: Electrons lose almost no energy crossing air, so the dose downstream of the cavity is higher and the range is longer than the water calculation predicts. At the lateral walls, scatter from tissue into air is not balanced by scatter back, so hot spots form in the tissue columns beside the cavity and cold regions sit behind them. Air does not increase attenuation. Electron dose depends strongly on the density along the path, not on geometric depth alone. The effect is lateral as well as axial, which is why the cavity is packed with wax or bolus.

### Q5
Stem: A profile at 10 cm depth puts the 90 percent point at 4.8 cm, the 80 percent point at 5.1 cm, and the 20 percent point at 5.9 cm from the central axis. What is the penumbra by the 90 to 20 percent definition, and how does it compare with the 80 to 20 percent value?
A. 0.8 cm, equal to the 80 to 20 value
B. 0.3 cm, narrower than the 80 to 20 value
C. 1.9 cm, the sum of the two widths
D. 1.1 cm, wider than the 0.8 cm 80 to 20 value
Answer: D
Objective: III.1
Why: The 90 to 20 penumbra is 5.9 − 4.8 = 1.1 cm; the 80 to 20 penumbra is 5.9 − 5.1 = 0.8 cm. Check: the two differ by the 90-to-80 spacing, 5.1 − 4.8 = 0.3 cm, and 0.8 + 0.3 = 1.1 cm. A 90 to 20 width is always larger on the same profile because the 90 percent point lies farther inside the field. The 0.3 cm figure is only the spacing between the 90 and 80 percent points. Adding the two widths has no meaning. This bank reads an unspecified penumbra as 80 to 20; a stem that names the levels overrides that.
