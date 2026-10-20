# Module 42. QA and Standard of Care

Original items. Round 2 of the RM Review porting wave: the TG-100 human-factors finding, EPID and portal-imaging QA (Las Vegas phantom, monthly imaging checks), electron-cone and cut-out measurement, DVH resolution, CBCT dose reduction, and TG-40 legacy numbers used as named distractors against TG-142.

## Imaging QA, Human-Factor Findings, and TG-40 Legacy Numbers

### Q1
Stem: When TG-100 and the incident-learning literature it draws on classified the root causes of radiotherapy events, which category came out on top?
A. Linac hardware failure, mostly MLC and dose-monitor faults
B. Failures of communication, hand-offs, and other human and process errors
C. Dose-calculation algorithm errors in the planning system
D. Imaging-system miscalibration
Answer: B
Objective: VII.7
Why: The analyses behind TG-100 (and the RO-ILS data since) place communication breakdowns, hand-off errors, wrong-patient or wrong-site mix-ups, and other human and process failures far ahead of equipment faults as the leading cause of events, which is why the report shifted QA effort from machine tests toward process mapping, FMEA, and independent checks. Hardware failure is caught by interlocks and TG-142 QA and accounts for a small share. Algorithm errors are rare once a system is commissioned. Imaging miscalibration produces setup errors but is not the leading category.

### Q2
Stem: A physicist images a test object with the EPID each month and counts how many of the drilled holes of different depth and diameter are visible. What is the object, and what is being tested?
A. A Winston–Lutz ball, testing radiation-isocenter coincidence
B. A picket-fence pattern, testing MLC leaf position
C. A Las Vegas phantom, testing MV portal-image contrast and spatial resolution against the commissioning baseline
D. A Catphan, testing CBCT Hounsfield-unit constancy
Answer: C
Objective: VII.9
Why: The Las Vegas phantom is an aluminium block with a grid of holes of graded depth and diameter; the number of holes seen at a fixed exposure scores the low-contrast and spatial resolution of the MV imager, and TG-142 asks for that score monthly against baseline. The Winston–Lutz ball tests isocenter, not image quality. The picket fence is delivered through the MLC and read for leaf gaps. The Catphan is the kV CBCT image-quality phantom, with HU constancy as one of its modules.

### Q3
Stem: Which list contains only monthly TG-142 imaging checks for a linac with kV and MV planar imaging and CBCT?
A. Imaging and treatment coordinate coincidence, spatial resolution, contrast, uniformity and noise, scaling, and CBCT Hounsfield-unit constancy
B. Collision interlocks, output constancy at 3 percent, and lasers
C. TG-51 absolute calibration, imaging dose, and full-range MLC transmission
D. Door interlock, audio-visual monitors, and the beam-on indicator
Answer: A
Objective: VII.9
Why: TG-142 moves image quality to the monthly column: planar kV and MV spatial resolution, contrast, uniformity and noise, scaling or distortion (2 mm), and imaging-to-treatment coordinate coincidence (2 mm, 1 mm SRS), plus CBCT geometric distortion, resolution, contrast, HU constancy, and uniformity against baseline; daily imaging QA is limited to collision interlocks, positioning and repositioning, and the coincidence check. Option B is the daily list. TG-51, imaging dose, and MLC transmission are annual. Option D is daily safety.

### Q4
Stem: On an SRS-class linac, the monthly kV-to-MV imaging coordinate coincidence measures 1.4 mm. What is the verdict?
A. Passes, because the tolerance for all machines is 2 mm
B. Passes, because imaging coincidence has no SRS column
C. Fails, because the SRS tolerance is 0.5 mm
D. Fails, because the SRS/SBRT tolerance is 1 mm and 1.4 mm is 0.4 mm over it
Answer: D
Objective: VII.9
Why: TG-142 gives imaging and treatment coordinate coincidence 2 mm for non-SRS machines and 1 mm for SRS/SBRT machines; 1.4 − 1.0 = 0.4 mm over, so the SRS machine fails and the imager is recalibrated before stereotactic use. The 2 mm column belongs to conventional machines. The imaging table does carry the SRS column. There is no 0.5 mm imaging tolerance in TG-142. Check: 1.4 mm would pass on a conventional machine with 0.6 mm to spare.

### Q5
Stem: A clinic receives a replacement 10 by 10 cm electron applicator for its 12 MeV beam and a planner also designs a new 4 by 6 cm cut-out for it. What must happen before either is used clinically?
A. Nothing; applicator factors are part of the beam model and cut-out factors scale with area
B. Only the applicator is measured; the cut-out factor can be read from the photon field-size table
C. Only the cut-out is measured; replacement applicators are factory matched
D. The output of the new applicator and of the new cut-out are measured, because neither may be assumed from the old data or from a table
Answer: D
Objective: VII.5
Why: Electron output depends on the applicator scatter and on the insert when lateral equilibrium is lost, so a replacement applicator is re-measured at acceptance and every new small or irregular cut-out gets its own output measurement (or a validated calculation checked against measurement); a 4 by 6 cm insert at 12 MeV is near the equilibrium limit and cannot be assumed. Scaling with area is not how electron output behaves. Photon field-size tables are for a different particle and a different scatter geometry. A factory applicator still needs the beam it will be used on.

### Q6
Stem: Two DVHs of the same plan give the cord Dmax as 46.8 Gy and 48.1 Gy. The second was computed with a finer dose grid and finer dose bins. Which statement is correct?
A. The first is correct, because coarse grids are conservative
B. The two cannot differ, because the DVH depends only on the contour
C. The second is the better estimate, because DVH accuracy, especially the maximum and small-volume metrics, depends on dose-grid spacing and bin width
D. Average the two
Answer: C
Objective: VII.1
Why: A DVH is sampled from the dose grid and binned; a coarse grid smooths the high-dose spike near a thin serial organ and wide bins blur the maximum, so the finer calculation is the one to trust, and TG-101 asks for 2 mm or finer grids on stereotactic plans for this reason. Coarse grids under-report maxima; that is the opposite of conservative. The contour is only one input. Averaging two samples of different quality is not a method.

### Q7
Stem: A daily CBCT protocol for a prostate patient images the whole pelvis. Which single change most reduces the imaging dose while keeping the soft-tissue match?
A. Switch from kV CBCT to MV CBCT
B. Increase the mAs to reduce noise so fewer repeat scans are needed
C. Use a bow-tie-free scan
D. Collimate the field of view and scan length to the prostate and immediate margin
Answer: D
Objective: VII.9
Why: Collimating the scan to the region needed (shorter longitudinal length, smaller FOV) reduces the irradiated volume and the integral dose roughly in proportion, and the prostate match does not need the iliac crests; TG-180 also asks that this dose be recorded. MV CBCT delivers more dose per image than kV. Raising mAs increases dose per scan. Removing the bow-tie filter increases peripheral dose and worsens uniformity.

### Q8
Stem: A legacy question keys the monthly beam-symmetry tolerance at 3 percent. Which document is it citing, and what is the current TG-142 figure?
A. TG-40, 3 percent symmetry; TG-142 writes 1 percent change from the commissioning baseline
B. TG-142, 3 percent; TG-40 wrote 1 percent
C. TG-51; symmetry is not in TG-142
D. Both documents write 3 percent
Answer: A
Objective: VII.9
Why: TG-40 (1994) set photon and electron symmetry at 3 percent as an absolute figure (photon flatness was tighter, electron flatness 3 percent); TG-142 (2009) replaced the absolute numbers with a 1 percent constancy check against the machine's own baseline profile. Option B reverses the two reports. TG-51 is beam calibration and says nothing about symmetry. Where a stem names TG-40, answer 3 percent; where it names TG-142, answer 1 percent from baseline. The TG-40 table earlier in this module lists the same legacy figures.

### Q9
Stem: A stem asks for the laser-alignment tolerance on an SRS linac and offers 2 mm "from the simulator table." Which answer is correct?
A. 2 mm, because lasers are 2 mm in every AAPM document
B. 1 mm, the TG-142 SRS/SBRT figure; 2 mm is the TG-40 figure for all linacs and the CT-simulator figure in TG-66
C. 1.5 mm, the TG-142 figure for every IGRT machine
D. 0.5 mm, the TG-142 SRS figure
Answer: B
Objective: VII.9
Why: TG-142 grades lasers by machine class, 2 mm non-IMRT, 1.5 mm IMRT, 1 mm SRS/SBRT, so the SRS machine is held to 1 mm. The 2 mm figure survives in two legacy places, the TG-40 linac and simulator tables and the TG-66 CT-simulator laser tolerance, which is why it appears as a distractor. 1.5 mm is the IMRT column, not the SRS column. No TG-142 laser cell is 0.5 mm.
