# Module 7. Treatment Machine Characteristics

Original items. Gaps identified in the RM Review port: RF engineering, modulator, waveguides, energy and dose-rate controls, bending magnets, head hardware numbers.

## RF Engineering of the Linac

### Q1
Stem: In which accelerating structure does the microwave power enter one end, move along with the electrons, and leave at the far end into a load?
A. Standing-wave guide
B. Traveling-wave guide
C. Side-coupled guide
D. Betatron doughnut
Answer: B
Objective: I.5
Why: A traveling-wave structure carries the RF down the guide with the electron bunches and dumps the residual power at the exit. A standing-wave guide reflects the RF at both ends so the field pattern is stationary, and it uses side-coupled cavities to shorten the structure. The betatron has no waveguide; it accelerates electrons by a changing magnetic flux.

### Q2
Stem: A standing-wave accelerating structure reflects RF power back toward the source. Which component protects the klystron or magnetron from that reflected power?
A. The thyratron
B. The pulse-forming network
C. The circulator (isolator)
D. The energy switch
Answer: C
Objective: I.5
Why: The circulator is a ferrite device that passes power forward to the guide and routes any reflected power into a water load instead of back into the RF source. The thyratron is the high-voltage switch in the modulator. The pulse-forming network stores the energy for each pulse. The energy switch changes the beam energy by detuning part of the standing-wave guide.

### Q3
Stem: A linac RF system operates at 3 GHz. The free-space wavelength of that microwave is:
A. 1 cm
B. 3 cm
C. 10 cm
D. 100 cm
Answer: C
Objective: I.5
Why: Wavelength equals speed of light divided by frequency: 3 times ten to the 8 m/s divided by 3 times ten to the 9 Hz equals 0.10 m, which is 10 cm. Check: 10 cm times 3 GHz returns 3 times ten to the 8 m/s. 1 cm would need 30 GHz, 3 cm about 10 GHz, and 100 cm 300 MHz. The 10 cm figure is the S-band and sets the size of the accelerating cavities.

### Q4
Stem: Sulfur hexafluoride gas is used in a medical linac to:
A. Fill the accelerating structure so electrons travel in a dense medium
B. Pressurize the RF waveguide between the source and the structure to prevent arcing
C. Cool the x-ray target
D. Insulate the thyratron tube
Answer: B
Objective: I.5
Why: SF6 is an electronegative dielectric gas that suppresses electrical breakdown in the high-field RF transmission guide. The accelerating structure is kept under high vacuum, not filled with gas, because electrons must not collide with molecules. The target is water-cooled. The thyratron contains low-pressure hydrogen or deuterium as part of its switching action, not SF6.

### Q5
Stem: In the linac modulator, the device that is triggered to discharge the stored high-voltage pulse to the klystron or magnetron and to the electron gun is the:
A. Thyratron
B. Circulator
C. Klystron driver
D. Bending magnet
Answer: A
Objective: I.5
Why: The thyratron is a gas-filled high-voltage switch; when triggered it dumps the pulse-forming network through a pulse transformer in a few microseconds, and the same pulse fires the RF source and the gun so electrons are injected while RF is present. The circulator handles reflected RF. The klystron driver supplies the low-power RF input that the klystron amplifies. The bending magnet acts on the beam after acceleration.

### Q6
Stem: The pulse-forming network in a linac modulator functions to:
A. Generate the 3 GHz microwaves
B. Store energy between pulses and shape each high-voltage pulse that is delivered
C. Focus the electron beam in the waveguide
D. Monitor beam symmetry
Answer: B
Objective: I.5
Why: The network is a ladder of capacitors and inductors that charges slowly from the high-voltage supply and releases its energy as a flat pulse of defined width when the thyratron fires. Microwaves come from the magnetron or klystron. Focusing coils around the guide confine the beam. Symmetry is read by the segmented monitor ion chamber.

### Q7
Stem: At a fixed beam energy, which adjustment raises the linac dose rate?
A. Lengthening the accelerating guide
B. Shortening the energy switch
C. Increasing the electron gun current or the pulse repetition frequency
D. Reducing the RF power
Answer: C
Objective: I.5
Why: Dose rate scales with electrons per pulse (gun current) and pulses per second (repetition frequency). Guide length and RF power set the energy available to each electron. The energy switch is a cavity detuning control for energy, not a mechanical length. Reducing RF power lowers the energy and, through beam loading, would require the servo to reduce current.

### Q8
Stem: If the RF power to the accelerating guide is held constant and the injected gun current is raised sharply, the electron beam energy will:
A. Rise, because more electrons carry more energy
B. Fall, because the electrons extract more energy from the RF field (beam loading)
C. Stay the same, because energy depends only on frequency
D. Oscillate at the pulse repetition frequency
Answer: B
Objective: I.5
Why: Beam loading describes the drop in accelerating field when more charge draws power from the RF; with fixed RF input the energy per electron falls. Energy is set by RF power, guide length, and the energy switch, with the current acting as a load. Frequency must stay tuned to the guide but does not by itself set the energy. The pulse repetition frequency sets dose rate, not energy oscillation.

### Q9
Stem: Compared with photon mode, the electron gun current used in electron mode on the same linac is:
A. About the same
B. Much lower, roughly a hundred to a thousand times smaller
C. Much higher, to compensate for the scattering foil
D. Zero, because electrons come from the target
Answer: B
Objective: I.5
Why: In photon mode, bremsstrahlung conversion is inefficient and the flattening filter absorbs most of the central fluence, so a large current is needed to reach 1 cGy per MU. In electron mode almost every accelerated electron reaches the patient after the thin scattering foil, so the current is reduced by orders of magnitude; the monitor-chamber interlocks exist partly to stop photon-level current in electron mode. The target produces photons, not electrons.

### Q10
Stem: Which historical accelerator accelerates electrons on a circular orbit using a changing magnetic flux, like the secondary of a transformer, and was limited by a low dose rate?
A. Microtron
B. Van de Graaff generator
C. Cyclotron
D. Betatron
Answer: D
Objective: I.5
Why: The betatron uses induction: a rising magnetic field drives electrons around a doughnut-shaped vacuum chamber, reaching 20 to 45 MeV but with a low output and small fields. The microtron sends electrons repeatedly through one RF cavity on orbits of increasing radius. The Van de Graaff is an electrostatic machine for 1 to 2 MV photons. The cyclotron accelerates heavy charged particles such as protons.

### Q11
Stem: In a microtron the electron energy is chosen by:
A. Selecting which orbit is extracted after a given number of passes through the single RF cavity
B. Changing the SF6 pressure in the waveguide
C. Replacing the target with a scattering foil
D. Raising the klystron frequency
Answer: A
Objective: I.5
Why: Each lap through the cavity adds a fixed energy increment and the magnet bends the beam onto a larger circle; a deflector pulls the beam out at the orbit matching the wanted energy, giving a narrow energy spread and simple energy switching. SF6 pressure is an insulation setting, not an energy control. Target versus foil chooses photons versus electrons, not energy. Frequency must stay resonant with the cavity.

## Beam Transport and Head Hardware Numbers

### Q1
Stem: The main advantage of a 270 degree achromatic bending magnet over a simple 90 degree magnet is that:
A. It shortens the treatment head
B. Electrons of slightly different energies are brought back to the same spot and direction on the target
C. It eliminates the need for a flattening filter
D. It increases the dose rate
Answer: B
Objective: I.5
Why: The achromatic design cancels the energy dependence of the bend, so an energy drift does not move or enlarge the focal spot and the beam axis stays stable. A 90 degree magnet is chromatic and spreads the spot. The 270 degree loop actually makes the head taller, which is why the compact slalom design exists. The flattening filter is still required for a flat photon beam, and dose rate is set by the gun current and pulse rate.

### Q2
Stem: The slalom bending-magnet design used on some linacs is best described as:
A. A single 90 degree chromatic magnet
B. A straight-through design with no bend
C. A compact achromatic arrangement of three smaller magnets in an S-shaped path
D. A 360 degree storage ring
Answer: C
Objective: I.5
Why: The slalom magnet achieves achromatic focusing like a 270 degree system but with a lower head profile by bending the beam in alternating directions through three magnets. A single 90 degree magnet is chromatic. Straight-through heads exist only on low-energy single-energy machines. No clinical linac uses a storage ring.

### Q3
Stem: To produce a flat profile at 10 cm depth, the flattening filter attenuates the central-axis photon fluence by roughly what factor?
A. About 2 to 4
B. About 1.05
C. About 100
D. It does not attenuate the central axis; it only adds fluence at the edges
Answer: A
Objective: I.5
Why: Megavoltage bremsstrahlung is strongly forward-peaked, so the cone must cut the center down to the level of the edge, removing most of the central fluence; the dose rate gain of two to four times when the filter is removed for FFF beams is the same factor. A few percent would not flatten anything. A factor of 100 would make photon mode impossible. A filter cannot add fluence; it can only remove it.

### Q4
Stem: Transmission of the primary beam through a closed secondary collimator jaw on a modern linac is approximately:
A. 5%
B. 2 to 3%
C. Less than 0.5%
D. 0.01%
Answer: C
Objective: I.5
Why: Jaws are about 7.5 to 8 cm of tungsten or lead and pass under half a percent of the primary beam. Two to three percent is the MLC leaf and interleaf leakage range, which is why jaws are set close to the MLC edge. Five percent would be unacceptable for any collimator. 0.01% is below even the head-leakage specification of 0.1% at one meter.

### Q5
Stem: The electronic portal imaging device on a current linac is:
A. A film cassette read by a digitizer
B. An amorphous-silicon flat panel with a copper plate, a phosphor screen, and a photodiode array
C. A liquid-filled ion-chamber matrix
D. A camera viewing a fluorescent screen through a mirror
Answer: B
Objective: I.5
Why: The a-Si panel converts megavoltage photons to electrons in the copper plate, to light in the gadolinium oxysulfide scintillator, and to charge in the photodiode matrix read out by thin-film transistors; it gives an image in seconds and can be calibrated for IMRT QA and transit dosimetry. Film, liquid-ion-chamber matrices, and camera-mirror systems are earlier generations that the flat panel replaced.
