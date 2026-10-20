# Module 9. Radiation Measurement

Original items. Gaps identified in the RM Review port: detector-to-task matching, chamber volumes and bias, recombination and polarity corrections, TLD, OSL, MOSFET and film properties, calibration intervals and the IROC audit.

## Matching the Detector to the Task

### Q1
Stem: A physicist is performing the annual TG-51 output calibration of a 6 MV beam in a water tank at 10 cm depth in a 10 by 10 cm field. Which detector is the appropriate reference instrument?
A. A shielded silicon diode
B. A cylindrical Farmer-type chamber of about 0.6 cubic centimeters
C. A well-type chamber of about 245 cubic centimeters
D. A Geiger–Müller probe with an energy-compensated shield
Answer: B
Objective: I.10
Why: Reference dosimetry uses a cylindrical chamber with an ADCL absorbed-dose-to-water coefficient, and the 0.6 cc Farmer is the standard instrument because the 10 by 10 cm field is flat across its length and its volume gives a stable signal. A diode has energy, temperature and angular dependence and carries no N_D,w. A well chamber is built to surround a brachytherapy source, not to sit in a photon beam. A GM tube counts events and saturates in a pulsed linac beam, so it cannot give dose.

### Q2
Stem: An output factor for a 1 by 1 cm stereotactic field is measured with a Farmer chamber and comes out 15 percent lower than the planning system expects. The most likely explanation and the right fix are:
A. The chamber's buildup cap was left off; repeat with the cap on
B. The beam is miscalibrated; repeat the TG-51 calibration
C. The planning system is wrong; adjust the small-field data to match the chamber
D. The 2 cm long chamber averages over the penumbra of a 1 cm field; repeat with a micro-chamber of about 0.01 cubic centimeters or a small-field diode
Answer: D
Objective: I.10
Why: A Farmer chamber is longer than a 1 cm field, so much of its volume sits in the penumbra and the reading is a volume-averaged underestimate. Small fields need a point detector such as a 0.01 to 0.02 cc micro-chamber, a diode, a diamond or a plastic scintillator with the corrections in TG-155 and TRS-483. A buildup cap is for in-air measurements, not for water. A 15 percent error confined to the smallest field is not a calibration error, and fitting the model to a flawed measurement propagates the error into every SRS plan.

### Q3
Stem: Which chamber is preferred for the reference-depth output measurement of a 6 MeV electron beam, and why?
A. A parallel-plate chamber, because the steep electron dose gradient is less perturbed by a thin flat cavity and its gradient correction is unity
B. A Farmer chamber, because its calibration coefficient is more accurate than that of any other chamber
C. A well chamber, because it collects every electron that enters it
D. A micro-chamber, because electron fields are always small
Answer: A
Objective: I.10
Why: Below about 10 MeV the dose falls steeply with depth and a cylindrical cavity displaces the point of measurement and perturbs the fluence, so TG-51 recommends a parallel-plate chamber, for which the gradient correction is 1 and the point of measurement is the inner face of the window. A Farmer chamber is acceptable only for higher electron energies. A well chamber is a brachytherapy source assay device. Electron applicator fields are typically 6 by 6 cm or larger, so a micro-chamber brings no advantage and a weaker signal.

### Q4
Stem: A new Ir-192 HDR source arrives and its air-kerma strength must be verified before clinical use. The instrument designed for this measurement is:
A. A Farmer chamber in the water tank at 10 cm depth
B. An ion-chamber survey meter held at 1 meter
C. A well-type chamber with a collecting volume of roughly 245 cubic centimeters and an ADCL calibration for that source model
D. A diode array used for IMRT QA
Answer: C
Objective: I.10
Why: Source strength is assayed in a re-entrant well chamber whose large gas volume surrounds the source, giving high sensitivity and low dependence on small positioning errors, with a calibration coefficient specific to the source type. A Farmer chamber in water measures beam output, not Sk. A survey meter at 1 meter confirms the source is present and gives a rough exposure rate but is not a calibration instrument. A diode array is a relative planar dosimeter.

### Q5
Stem: A 18 MV linac vault is being surveyed at the door with the beam on. Which instrument is required in addition to a photon survey meter?
A. A Geiger–Müller counter, because it is the most sensitive detector available
B. A moderated proportional counter such as a rem-ball with a boron trifluoride or helium-3 tube
C. A second ion chamber of larger volume
D. A thermoluminescent dosimeter read the next day
Answer: B
Objective: I.10
Why: Photon beams above 10 MV produce photoneutrons, and a photon meter does not register them; the standard neutron survey instrument is a thermal-neutron proportional counter inside a polyethylene moderating sphere, which gives a dose-equivalent reading. A GM tube is nearly blind to neutrons and saturates in a pulsed field. A larger ion chamber improves photon sensitivity but still does not see neutrons. A TLD gives no real-time reading and ordinary LiF is not a neutron dosimeter without a lithium-6 and lithium-7 pair.

### Q6
Stem: A Geiger–Müller probe with a dead time of 100 microseconds displays 2,000 counts per second. Using the non-paralyzable correction, the true count rate is approximately:
A. 2,500 counts per second
B. 2,000 counts per second
C. 1,600 counts per second
D. 4,000 counts per second
Answer: A
Objective: I.10
Why: The lost fraction is the observed rate times the dead time, 2,000 times 0.0001, which is 0.20, so the true rate is 2,000 divided by 0.80, or 2,500 counts per second. Check: 2,500 times 0.80 returns 2,000. 2,000 ignores the dead time. 1,600 multiplies by 0.80 instead of dividing. 4,000 would need a lost fraction of 0.5, which corresponds to 250 microseconds. At ten thousand counts per second the product reaches 1 and the tube is paralyzed, which is why a GM is useless in a linac beam.

### Q7
Stem: According to TG-51, how often should the clinic's reference ion chamber and electrometer be recalibrated at an Accredited Dosimetry Calibration Laboratory?
A. Annually, at the same time as the linac annual QA
B. Every six months
C. Once, when the chamber is purchased
D. Every two years, with constancy checks against a check source or a redundant chamber in between
Answer: D
Objective: VII.3
Why: TG-51 and its addendum state a two-year ADCL interval for the reference chamber and electrometer, with the clinic monitoring stability between calibrations by Sr-90 check-source readings or a redundant-chamber intercomparison. Annual and six-monthly are the intervals for other items such as survey meters and linac calibration, not for the ADCL coefficient. A single calibration at purchase is not traceable practice because the chamber response drifts with age and damage.

### Q8
Stem: A wipe test of a sealed Cs-137 source must show removable contamination below 0.005 microcuries, about 11,000 disintegrations per minute. The appropriate counting instrument is:
A. A Farmer chamber with its electrometer on the most sensitive range
B. An ion-chamber survey meter in integrate mode
C. A sodium iodide scintillation well counter
D. A diode held against the wipe
Answer: C
Objective: VII.3
Why: A wipe at the regulatory limit emits a few hundred decays per second, far below what any ionization chamber can resolve above leakage; a NaI(Tl) well counter detects individual photons with high efficiency and reaches that level in seconds. A Farmer chamber is thousands of times less sensitive and reads charge, not counts. A survey ion chamber is designed for exposure rates around sources and patients, not for counting a swab. A diode has no counting electronics and a tiny volume.

## Chamber Corrections and Passive Dosimeters

### Q1
Stem: In a 6 MV beam a Farmer chamber reads 25.20 nanocoulombs at its normal 300 volt bias and 25.05 nanocoulombs at 150 volts. Using the two-voltage method, the recombination correction at 300 volts is approximately:
A. 0.994
B. 1.006
C. 1.012
D. 2.000
Answer: B
Objective: I.10
Why: The ratio of readings is 25.20 over 25.05, which is 1.006. Pion equals 1 minus 2, divided by 1.006 minus 2, which is minus 1 over minus 0.994, or 1.006. Check: the lower bias lost about 0.6 percent of the charge, so the full-bias reading is corrected up by about 0.6 percent. 0.994 is the inverted ratio and corrects the wrong direction. 1.012 doubles the correction as if all the loss at half bias also occurred at full bias. 2.000 is the voltage ratio, not a correction.

### Q2
Stem: With positive bias a chamber reads plus 25.20 nanocoulombs; with the bias reversed it reads minus 25.00 nanocoulombs. The clinic calibrates at positive bias. The polarity correction is approximately:
A. 1.004
B. 0.992
C. 0.996
D. 1.008
Answer: C
Objective: I.10
Why: Ppol is the sum of the two magnitudes divided by twice the working-polarity reading: 50.20 divided by 50.40 equals 0.996. Check: the working polarity reads slightly high, so the correction is slightly below 1. 1.004 is the simple ratio of the two magnitudes, which is not the TG-51 definition. 0.992 doubles the deviation. 1.008 is both doubled and in the wrong direction.

### Q3
Stem: A clinic commissions a 10 MV flattening-filter-free beam at 2,400 monitor units per minute. Compared with the flattened 10 MV beam measured with the same Farmer chamber, which TG-51 correction is expected to increase noticeably?
A. The temperature–pressure correction
B. The electrometer correction
C. The polarity correction
D. The ion recombination correction
Answer: D
Objective: I.10
Why: Recombination in a pulsed beam depends on the charge liberated per pulse, and an FFF beam delivers several times more dose per pulse, so Pion rises and must be remeasured for that beam. Ptp depends only on the air in the cavity and the weather. Pelec is a property of the electrometer. Ppol changes little between flattened and unflattened photon beams of the same energy.

### Q4
Stem: A plot of light output against heating temperature obtained when a lithium fluoride chip is read is called a:
A. Glow curve, and the dose is taken from the high-temperature peak near 210 degrees Celsius
B. Sensitometric curve, and the dose is taken from the straight-line region
C. Bragg curve, and the dose is taken from the peak
D. Saturation curve, and the dose is taken from the plateau
Answer: A
Objective: I.10
Why: Heating a thermoluminescent dosimeter releases trapped electrons as light; the output against temperature is the glow curve, and the stable dosimetric peak is peak 5 near 210 degrees Celsius because the low-temperature peaks fade within hours. A sensitometric or H&D curve is optical density against log exposure for film. A Bragg curve is ionization against depth for a charged particle. A saturation curve is ion-chamber current against bias voltage.

### Q5
Stem: Which statement correctly distinguishes an optically stimulated luminescence dosimeter from a thermoluminescent dosimeter?
A. OSL uses lithium fluoride and TLD uses aluminum oxide
B. OSL releases only a small fraction of the trapped charge per read, so it can be re-read, whereas reading a TLD empties the traps
C. OSL must be annealed at 400 degrees Celsius after each use, whereas TLD is cleared by light
D. OSL is read in real time during the irradiation, whereas TLD is read afterward
Answer: B
Objective: I.10
Why: An OSLD of carbon-doped aluminum oxide is stimulated by a light pulse that empties only part of the traps, so the same dosimeter can be read several times and is later bleached with light; a LiF TLD is read by heating, which empties the traps, and it is then thermally annealed before reuse. The materials in option A are reversed. Option C swaps the clearing methods. Both are passive integrating dosimeters read after the exposure, not real-time devices.

### Q6
Stem: A MOSFET dosimeter placed on the skin during a treatment reports dose by measuring:
A. The charge collected between two plates under a 300 volt bias
B. The light emitted when the device is heated
C. The change in optical density of a polymer layer
D. The shift in the transistor's threshold voltage caused by charge trapped in the gate oxide
Answer: D
Objective: I.10
Why: Radiation traps charge in the oxide of the MOSFET and the gate voltage needed to turn the transistor on shifts in proportion to dose, which is read out immediately; the device has a finite total shift, so its useful life is limited, and it needs temperature and energy corrections. Charge collection under a bias describes an ion chamber. Light on heating is a TLD. Polymer darkening is radiochromic film.

### Q7
Stem: A physicist wants an absolute dose from a piece of radiochromic film exposed in a brachytherapy check. Compared with radiographic film described by an H&D curve, the correct handling is:
A. Scan it after about 24 hours, with no chemical processing, because the polymer darkening continues for several hours after exposure
B. Develop it in the processor within 10 minutes so that the latent image does not fade
C. Read it immediately, because radiochromic density is fixed at the instant of exposure
D. Heat it to 210 degrees Celsius and record the emitted light
Answer: A
Objective: I.10
Why: Radiochromic film self-develops by polymerization and its optical density keeps rising for hours, so protocols read it after a fixed delay, commonly 24 hours, against a calibration read at the same delay; it needs no processor and is near tissue-equivalent with little energy dependence. Chemical processing and the H&D curve belong to silver-halide film. Immediate reading gives a dose that is systematically low unless a short-delay calibration is used. Heating and light output is TLD readout.
