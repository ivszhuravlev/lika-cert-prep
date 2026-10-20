# Module 18. IGRT

Original items. Prospective versus retrospective 4D-CT, the imaging geometry of CyberKnife and ExacTrac, and where electromagnetic transponders are used.

## Tracking System Geometry and 4D-CT Modes

### Q1
Stem: A lung SBRT plan needs a maximum-intensity projection for the ITV, an average-intensity image for dose calculation, and the end-exhale phase for a possible gated plan. Which acquisition supplies all three?
A. A prospective gated CT triggered at end-exhale
B. A retrospective 4D-CT sorted into phase bins after a continuous acquisition
C. A standard helical CT at a fast pitch during free breathing
D. A breath-hold CT at deep inspiration
Answer: B
Objective: II.6
Why: Only a retrospective acquisition records the whole breathing cycle and bins it afterward, so every phase, the MIP and the average image can be reconstructed from it. A prospective scan triggers the scanner inside one gate and yields a single phase at lower dose, useful when that phase is all that will be treated. A fast helical scan freezes each slice at a random phase and produces motion artifacts. A breath-hold scan is one position and contains no motion information.

### Q2
Stem: Which description matches the imaging geometry of a CyberKnife unit?
A. Two kilovoltage tubes in the floor and two flat panels on the ceiling, with an infrared camera driving a six-degree-of-freedom couch
B. A single kilovoltage source and panel mounted on the gantry at 90 degrees to the treatment beam
C. Two kilovoltage tubes in the ceiling and two flat panels recessed in the floor, with the robot rather than the couch correcting the beam
D. A megavoltage portal imager opposite the treatment head
Answer: C
Objective: II.6
Why: The CyberKnife mounts its stereoscopic kilovoltage tubes in the ceiling and its detectors flush with the floor; the two oblique images are matched to DRRs for skull, spine or fiducial tracking, and the robotic arm redirects the beam. Option A is the ExacTrac layout, the mirror image. Option B is the gantry-mounted kV system used for CBCT on a conventional linac. Option D is a conventional EPID.

### Q3
Stem: An ExacTrac system is being described to a new dosimetrist. Which statement is correct?
A. Its infrared camera tracks reflective markers on the patient while two floor-mounted kV tubes and ceiling panels verify bone or fiducial position
B. It reconstructs a soft-tissue cone-beam volume from the two oblique projections
C. Its two kV tubes are mounted on the ceiling and image downward onto floor panels
D. It requires an invasive stereotactic frame for all intracranial treatments
Answer: A
Objective: II.6
Why: ExacTrac combines an infrared surface tracking system that drives a robotic couch with a stereoscopic kV pair from floor tubes to ceiling panels, matched to DRRs on bone or implanted fiducials. It produces two planar images, not a volume, so it does not image soft tissue directly. Ceiling tubes and floor panels is the CyberKnife arrangement. The system was designed for frameless setups with a mask.

### Q4
Stem: Implanted electromagnetic transponders for real-time tracking are used far more often in prostate than in lung because:
A. Lung tumors do not move enough to justify real-time tracking
B. Only two beacons are needed in prostate, while lung requires five
C. The transponders provide a cone-beam image of the prostate but not of the lung
D. The prostate is a well-defined, non-deforming organ with slow intrafraction drift, whereas lung placement is invasive and beacons can migrate
Answer: D
Objective: II.6
Why: Three beacons implanted transperineally in the prostate stay fixed relative to the gland and catch the slow drift from rectal and bladder filling without imaging dose; in lung the bronchoscopic placement carries a pneumothorax risk, beacons can migrate in soft tissue, large patients exceed the array range, and fast respiratory motion is better handled by gating or correlation tracking. Lung tumors can move more than a centimeter. Transponders are not an imaging device. Three beacons are the standard in both sites.
