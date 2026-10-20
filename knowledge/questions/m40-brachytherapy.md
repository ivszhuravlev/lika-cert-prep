# Module 40. Brachytherapy

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Radioactive Source Characteristics

### Q1
Stem: Which half-life is the usual value for Ir-192?
A. 59.4 days
B. 73.8 days
C. 17.0 days
D. 30 years
Answer: B
Objective: V.1
Why: Ir-192, the common HDR source, has a half-life of 73.8 days, so the source is exchanged about every few months and every treatment needs a decay correction. I-125 is 59.4 days, Pd-103 is 17.0 days, and Cs-137 is 30 years. Correct choice: 73.8 days. 59.4 days is I-125. 17.0 days is Pd-103. 30 years is Cs-137.

### Q2
Stem: Which quantity in TG-43 is the dose-rate constant?
A. Sk
B. g(r)
C. Λ
D. F(r, θ)
Answer: C
Objective: V.1
Why: TG-43 writes dose rate as Sk × Λ × (G/G0) × g(r) × F(r, θ). Λ converts air-kerma strength to dose rate in water on the transverse axis at the reference point. Correct choice: Λ. Sk is the air-kerma strength. g(r) is the radial dose function. F is the anisotropy function.

### Q3
Stem: A permanent prostate implant uses I-125 seeds. Which description matches that source?
A. An HDR afterloader source with a 73.8 day half-life that is withdrawn after minutes
B. A Cs-137 tube removed after hours
C. A Co-60 teletherapy source
D. Low-energy photon seeds left in place
Answer: D
Objective: V.1
Why: I-125 permanent seeds emit low-energy photons and stay in the prostate. Total dose uses the mean life, 1.443 × half-life, because the source is never removed. Correct choice: Low-energy photon seeds left in place. That is Ir-192 HDR, not a permanent seed implant. Cs-137 LDR tubes are temporary implants. Co-60 teletherapy is an external beam.

### Q4
Stem: An Ir-192 HDR source had a calibration activity of 10 Ci. Elapsed time is 14 days. The half-life is 73.8 days. What activity remains?
A. 8.77 Ci
B. 8.10 Ci
C. 5.00 Ci
D. 9.13 Ci
Answer: A
Objective: V.1
Why: Number of half-lives = 14/73.8 = 0.1897. Fraction remaining = (1/2)^(0.1897) = 0.8768. Activity = 10 × 0.8768 = 8.7679 Ci, reported as 8.77 Ci. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.1897) = 0.8768. A linear model A0×(1−t/T½) gives 8.10 Ci and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 5.00 Ci. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 9.13 Ci. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q5
Stem: Au-198, used historically for permanent implants, has a half-life nearest to which value?
A. 2.7 years
B. 59.4 days
C. 5.26 years
D. 2.7 days
Answer: D
Objective: V.1
Why: Au-198 decays quickly, half-life about 2.7 days, which is why a permanent gold implant delivers most of its dose in a short time. Correct choice: 2.7 days. A 2.7 year half-life would not decay out during a permanent-implant time scale the way gold does. That is I-125. That is Co-60.

## HDR and LDR Treatment Planning

### Q1
Stem: Where is Manchester point A?
A. At the vaginal surface of a cylinder
B. 2 cm superior and 5 cm lateral
C. At the tip of the tandem
D. 2 cm superior to the external cervical os and 2 cm lateral to the tandem
Answer: D
Objective: V.2
Why: Point A is 2 cm up from the external os along the tandem and 2 cm lateral. It was meant to represent dose near the paracervical triangle, not a target volume. Correct choice: 2 cm superior to the external cervical os and 2 cm lateral to the tandem. Surface dose on a cylinder is a different prescription point. 5 cm lateral is not point A. Point B is the farther pelvic-wall point in the classic system. The tandem tip is a source position, not point A.

### Q2
Stem: Which dose rate is HDR by the usual ICRU boundary?
A. Above 12 Gy/h
B. 0.4 to 2 Gy/h
C. Exactly 1 cGy/h
D. 2 to 12 Gy/h
Answer: A
Objective: V.2
Why: LDR is about 0.4–2 Gy/h, medium dose rate sits between that and HDR, and HDR is above 12 Gy/h. An Ir-192 afterloader is HDR. Correct choice: Above 12 Gy/h. That range is LDR. That is far below even LDR. That middle band is medium dose rate, not HDR.

### Q3
Stem: An HDR cylinder course is 4 fractions of 7 Gy. Tumor α/β = 10 Gy. What is the EQD2?
A. 47.6 Gy
B. 28.0 Gy
C. 39.7 Gy
D. 56.0 Gy
Answer: C
Objective: V.2
Why: Physical dose = 4 × 7 = 28 Gy. BED = 28 × (1 + 7/10) = 28 × 1.7000 = 47.60 Gy. The 2 Gy denominator factor is 1 + 2/10 = 1.2000. EQD2 = 47.60 / 1.2000 = 39.67 Gy, reported as 39.7 Gy. If the fraction size is already 2 Gy, EQD2 equals the physical dose for any α/β. Here the fraction size is 7 Gy, so that shortcut applies only when d = 2. Stopping at the BED and not dividing by (1+2/(α/β)) gives 47.6 Gy. Reporting only the physical dose gives 28.0 Gy. Using α/β = 3 Gy instead of 10 Gy gives 56.0 Gy.

### Q4
Stem: An HDR plan optimizes dwell times. What is the planner changing?
A. The half-life of Ir-192
B. The wedge angle of an external beam
C. The CT-density table
D. How long the source stops at each position
Answer: D
Objective: V.2
Why: The afterloader steps the source through the catheter and holds it for a programmed time at each dwell. Optimization changes those times (and which dwells are used) to shape the dose. Correct choice: How long the source stops at each position. The half-life is a property of the nuclide. Dwell time does not change it. Dwell times belong to the afterloader, not to a linac wedge. Density is an external-beam calculation input.

### Q5
Stem: A vaginal cylinder is prescribed to 5 mm depth rather than to the surface. Which way does the surface dose move, for the same depth dose?
A. The surface dose equals the 5 mm dose
B. The surface dose is lower
C. Point A becomes the surface
D. The surface dose is higher than the 5 mm dose
Answer: D
Objective: V.2
Why: For a line source in a cylinder, dose falls as you move out from the applicator. Prescribing to 5 mm depth means the vaginal surface, which is closer to the source, receives more than the prescription dose. Correct choice: The surface dose is higher than the 5 mm dose. Inverse square and attenuation make dose fall with distance from the source. The surface is closer, so it is higher. That reverses the geometry. Point A is a cervical definition, not the cylinder surface.

## HDR and LDR Delivery Systems

### Q1
Stem: What does a remote afterloader keep outside the patient between dwells?
A. A cobalt teletherapy head
B. The HDR source, parked in a shielded safe
C. Permanent I-125 seeds
D. The ion chamber used for TG-51
Answer: B
Objective: V.2
Why: Between treatments and between dwells the Ir-192 source is driven back into the shielded safe in the afterloader. That is why the room can be entered only after the source is confirmed parked. Correct choice: The HDR source, parked in a shielded safe. The afterloader is not the teletherapy unit. Seeds are not withdrawn into a safe. They stay in the patient. TG-51 is external-beam calibration.

### Q2
Stem: The HDR source fails to retract. What is the immediate priority?
A. Finish the remaining dwells manually with the room door open
B. Ignore it if the fraction is more than half done
C. Emergency retraction and removal of the applicator if needed, following the posted procedure
D. Recalculate the wedge factor
Answer: C
Objective: V.2
Why: A stuck HDR source is an emergency. The posted steps are emergency return, survey to confirm the source location, and applicator removal into a shielded container if the source will not park. Correct choice: Emergency retraction and removal of the applicator if needed, following the posted procedure. Staff do not stand in the room to complete a stuck source. A stuck source keeps delivering dose. Time matters. A wedge factor is not the emergency.

### Q3
Stem: Pulsed dose rate (PDR) differs from classic HDR how?
A. PDR seeds are permanent
B. PDR has no dwell positions
C. PDR uses a linac wedge
D. The source pulses over many hours instead of a few large HDR fractions
Answer: D
Objective: V.2
Why: PDR uses a stepping source in pulses, often hourly, to mimic LDR biology while still using an afterloader. It is not a permanent implant and not an external wedge. Correct choice: The source pulses over many hours instead of a few large HDR fractions. PDR is a remote afterloader technique, not a permanent seed implant. It still dwells. The schedule is pulsed. No.

### Q4
Stem: Before the first dwell, what must match the plan?
A. The linac MU second check only
B. Channel map, applicator, and total dwell time or source strength
C. The patient's shoe size
D. The Mayneord F factor
Answer: B
Objective: V.2
Why: The transfer tubes have to be on the planned channels, the applicator has to be the one that was planned, and the decayed source strength has to be the one in the plan. A swapped channel treats the wrong catheter. Correct choice: Channel map, applicator, and total dwell time or source strength. HDR is not checked by a linac MU calculation. Irrelevant. Mayneord F is an external PDD correction.

### Q5
Stem: What is a typical step size choice for an HDR dwell string?
A. 1 m
B. One step equal to the half-life
C. The geometric penumbra
D. A fixed step near 5 mm, or a step the plan states
Answer: D
Objective: V.2
Why: Afterloaders step the source by a fixed distance, commonly 5 mm, though the plan may use a stated step. The independent check should use the same step the plan used. Correct choice: A fixed step near 5 mm, or a step the plan states. A 1 m step cannot shape a cervical or breast implant. Half-life is time, not a position step. Penumbra is an external-beam edge width.

## Brachytherapy treatment device verification (seeds applicators)

### Q1
Stem: A prostate seed implant radiograph shows 78 seeds and the written directive ordered 84. What fails?
A. Nothing, because 78 is within 20%
B. The Ir-192 half-life
C. The seed count does not match the directive
D. The linac output constancy
Answer: C
Objective: V.3
Why: Device verification includes counting seeds against the written directive and the plan. 78 is not 84, so the implant is not confirmed until the missing seeds are found or the directive is formally revised. Correct choice: The seed count does not match the directive. A missing-seed discrepancy is investigated, not waived by a made-up percent. This implant is seeds, and the failure is the count, not a half-life. External-beam output does not explain missing seeds.

### Q2
Stem: What is an autoradiograph of a ribbon or seed train used for?
A. To measure linac flatness
B. To compute Mayneord F
C. To image the activity distribution along the source
D. To replace a leak test
Answer: C
Objective: V.3
Why: Film or a detector against the source train shows whether activity is where the plan thinks it is, including gaps or a reversed ribbon. Correct choice: To image the activity distribution along the source. Flatness is a teletherapy scan. Mayneord F is not an image of a source. A leak test looks for removable contamination. An autoradiograph looks at where the activity sits.

### Q3
Stem: A cylinder plan was done for a 3.0 cm diameter applicator, but a 2.5 cm cylinder was placed. If the plan is delivered unchanged, what happens at the vaginal surface?
A. Surface dose falls because the cylinder is smaller
B. Point A absorbs the difference
C. The surface is closer to the source than planned, so surface dose rises
D. Nothing, because dwell times do not depend on radius
Answer: C
Objective: V.3
Why: Dose falls rapidly with distance from a brachytherapy source. A smaller cylinder brings tissue closer, so the planned dwell times overdose the surface relative to the 3.0 cm plan. Correct choice: The surface is closer to the source than planned, so surface dose rises. Smaller radius means the surface is nearer the source. Inverse square raises the dose. Point A is not the cylinder surface. The dwell times were calculated for a different distance. Delivering them in a smaller cylinder changes the dose.

### Q4
Stem: Tandem and ovoid markers on the planning radiograph do not match the applicator that is in the patient today. What is the correct action?
A. Treat, then shift the dwells by Mayneord F
B. Ignore markers if the dwell times look familiar
C. Do not treat on that plan until the geometry is reconciled
D. Replace the source half-life in the plan and proceed
Answer: C
Objective: V.3
Why: Applicator verification means the device in the patient is the device in the plan: diameter, tandem length, ovoid size, and marker positions. A mismatch stops the treatment. Correct choice: Do not treat on that plan until the geometry is reconciled. Mayneord F cannot repair the wrong applicator. Familiar times in the wrong geometry are still the wrong dose. The half-life is not the mismatch.

### Q5
Stem: Which pair belongs in a pre-treatment HDR device check?
A. Transfer-tube length and channel number
B. Wedge angle and hinge angle
C. CT Hounsfield unit of water only
D. Equivalent square of the cylinder
Answer: A
Objective: V.3
Why: A tube that is too long or on the wrong channel puts the dwells in the wrong place even when the dwell times are numerically right. Length and channel are device checks. Correct choice: Transfer-tube length and channel number. Those are external-beam modifiers. HU of water is a CT QA test, not the HDR device check. Cylinders are round applicators. They are not Sterling rectangles.

## Secondary/Independent Calculations

### Q1
Stem: Independent check. Decay the HDR source strength before comparing dwell times. Activity at calibration was 8.5 Ci. Elapsed time is 21 days. The half-life is 73.8 days. What activity remains?
A. 6.08 Ci
B. 6.98 Ci
C. 4.25 Ci
D. 7.41 Ci
Answer: B
Objective: V.6
Why: Number of half-lives = 21/73.8 = 0.2846. Fraction remaining = (1/2)^(0.2846) = 0.8210. Activity = 8.5 × 0.8210 = 6.9785 Ci, reported as 6.98 Ci. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.2846) = 0.8210. A linear model A0×(1−t/T½) gives 6.08 Ci and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 4.25 Ci. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 7.41 Ci. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q2
Stem: Independent check. Air-kerma strength at calibration was 41200 U. Elapsed time is 7 days. The half-life is 73.8 days. What activity remains?
A. 38578 U
B. 37292 U
C. 20600 U
D. 39365 U
Answer: A
Objective: V.6
Why: Number of half-lives = 7/73.8 = 0.0949. Fraction remaining = (1/2)^(0.0949) = 0.9364. Activity = 41200 × 0.9364 = 38578.4021 U, reported as 38578 U. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.0949) = 0.9364. A linear model A0×(1−t/T½) gives 37292 U and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 20600 U. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 39365 U. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q3
Stem: Independent check of an I-125 point. Air-kerma strength Sk = 2.5 U, dose-rate constant Λ = 0.965 cGy/(h·U), geometry function ratio G/G0 = 1, radial dose function g(r) = 0.94, and anisotropy F = 0.97. What is the dose rate?
A. 2.27 cGy/h
B. 2.20 cGy/h
C. 2.34 cGy/h
D. 2.41 cGy/h
Answer: B
Objective: V.6
Why: Substitute 2.5 × 0.965 = 2.4125. × 1 = 2.4125. × 0.94 = 2.2677. × 0.97 = 2.1997 cGy/h, reported as 2.20 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Dropping anisotropy gives 2.27 cGy/h. Using only Sk × Λ × F and dropping geometry and radial dose gives 2.34 cGy/h. Stopping after Sk × Λ gives 2.41 cGy/h.

### Q4
Stem: Independent check of an off-axis HDR point. Air-kerma strength Sk = 10 U, dose-rate constant Λ = 1.115 cGy/(h·U), geometry function ratio G/G0 = 0.9, radial dose function g(r) = 0.99, and anisotropy F = 0.88. What is the dose rate?
A. 9.93 cGy/h
B. 9.81 cGy/h
C. 9.71 cGy/h
D. 8.74 cGy/h
Answer: D
Objective: V.6
Why: Substitute 10 × 1.115 = 11.1500. × 0.9 = 10.0350. × 0.99 = 9.9346. × 0.88 = 8.7425 cGy/h, reported as 8.74 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Dropping anisotropy gives 9.93 cGy/h. Using only Sk × Λ × F and dropping geometry and radial dose gives 9.81 cGy/h. Dropping the geometry ratio gives 9.71 cGy/h.

### Q5
Stem: Independent check of a permanent implant. A permanent I-125 implant has an initial dose rate of 7 cGy/h and a half-life of 59.4 days. What is the total dose to complete decay, to the nearest cGy?
A. 6916 cGy
B. 14400 cGy
C. 9979 cGy
D. 600 cGy
Answer: B
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 59.4 = 85.7142 days = 85.7142 × 24 = 2057.1408 hours. Total dose = 7 cGy/h × 2057.1408 h = 14400.0 cGy, reported as 14400 cGy. In one line: 7 × 1.443 × 59.4 × 24 = 14400.0. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 6916 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 9979 cGy. Forgetting to convert days to hours (omitting ×24) gives 600 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q6
Stem: Independent check. A permanent Pd-103 implant has an initial dose rate of 10 cGy/h and a half-life of 17 days. What is the total dose to complete decay, to the nearest cGy?
A. 5887 cGy
B. 2827 cGy
C. 4080 cGy
D. 245 cGy
Answer: A
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 17 = 24.5310 days = 24.5310 × 24 = 588.7440 hours. Total dose = 10 cGy/h × 588.7440 h = 5887.4 cGy, reported as 5887 cGy. In one line: 10 × 1.443 × 17 × 24 = 5887.4. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 2827 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 4080 cGy. Forgetting to convert days to hours (omitting ×24) gives 245 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q7
Stem: Independent check. The initial dose rate is 40 cGy/day and the half-life is 60 days. What is the total dose to complete decay, to the nearest cGy?
A. 3463 cGy
B. 1663 cGy
C. 2400 cGy
D. 83117 cGy
Answer: A
Objective: V.6
Why: Units already match, so mean life in days is 1.443 × 60 = 86.5800 days. Total = 40 × 1.443 × 60 = 40 × 86.5800 = 3463.20 cGy, reported as 3463 cGy. Using 0.693 instead of 1.443 gives 1663 cGy. Using the half-life with no mean-life factor gives 2400 cGy. Multiplying by an extra 24, as if the dose rate were per hour, gives 83117 cGy.

### Q8
Stem: Independent check. The exposure-rate constant Γ is 4.69 R·cm²/(mCi·h). Activity is 10000 mCi. Distance is 100 cm. What is the exposure rate?
A. 469.00 R/h
B. 4.69 R/h
C. 4.69 mR/h
D. 1.17 R/h
Answer: B
Objective: V.6
Why: Substitute 4.69 × 10000 / (100)^2 = 46900 / 10000 = 4.690000 R/h, reported as 4.69 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 469.00 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 4.69 mR/h. Doubling the distance inside the square (a 2× distance error) gives 1.17 R/h.

## Surveying (background pre and post implant, shielding, bedside dose)

### Q1
Stem: A post-implant survey reads 0.18 mR/h and the pre-implant background in the same spot was 0.03 mR/h. What is the net reading?
A. 0.18 mR/h
B. 0.15 mR/h
C. 0.21 mR/h
D. 0.03 mR/h
Answer: B
Objective: V.4
Why: Net = post − background = 0.18 − 0.03 = 0.15 mR/h. A survey that forgets to subtract background overstates the implant. Correct choice: 0.15 mR/h. 0.18 includes background. Adding background instead of subtracting it gives 0.21. 0.03 is the background alone.

### Q2
Stem: Bedside survey estimate. The exposure-rate constant Γ is 4.6 R·cm²/(mCi·h). Activity is 5000 mCi. Distance is 100 cm. What is the exposure rate?
A. 2.30 R/h
B. 230.00 R/h
C. 2.30 mR/h
D. 0.58 R/h
Answer: A
Objective: V.4
Why: Substitute 4.6 × 5000 / (100)^2 = 23000 / 10000 = 2.300000 R/h, reported as 2.30 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 230.00 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 2.30 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.58 R/h.

### Q3
Stem: A bedside distance of 40 cm. The 100 cm reading is the starting value. Inverse square only. The value is 1.2 mR/h at 100 cm from the source. What is it at 40 cm if only inverse square changes?
A. 3.0 mR/h
B. 0.2 mR/h
C. 3.3 mR/h
D. 7.5 mR/h
Answer: D
Objective: V.4
Why: Inverse square: intensity scales with (d1/d2)^2, and the farther distance gets the smaller value. Substitute 1.2 × (100/40)^2 = 1.2 × (2.5000)^2 = 1.2 × 6.2500 = 7.5 mR/h. Dropping the square and multiplying by the bare ratio 100/40 gives 3.0 mR/h. Inverting the distances, (40/100)^2, gives 0.2 mR/h and would raise the reading when the detector moves out. Using the gap between the two distances (60 cm) as if it were the source distance gives 3.3 mR/h, which is not a point on the beam axis from the source.

### Q4
Stem: Why is a background survey recorded before a permanent seed implant?
A. To commission the linac TG-51 factor
B. To replace the written directive
C. So the post-implant reading can be compared with the room, not just with zero
D. To measure wedge transmission
Answer: C
Objective: V.4
Why: The room already has a background. The post-implant survey means something only if you know what the meter read before the sources arrived. Correct choice: So the post-implant reading can be compared with the room, not just with zero. TG-51 is not this survey. The directive still stands. No wedge is involved.

### Q5
Stem: A bedside lead shield is placed for an LDR patient. What does the shield change?
A. The half-life
B. The written directive dose
C. The dose rate in the shadowed direction, not the source activity
D. The seed count
Answer: C
Objective: V.4
Why: Lead between the patient and the bed partner cuts the exposure rate in that direction. The activity inside the patient is unchanged. Correct choice: The dose rate in the shadowed direction, not the source activity. Shielding does not change the nuclide. The directive is the prescription. The shield protects people outside the patient. The shield does not add or remove seeds.

## Regulatory requirements for radioactive sources (NRC vs. State requirements)

### Q1
Stem: In an Agreement State, who regulates most medical byproduct material?
A. Only the NRC, in every state
B. The state, under rules compatible with the NRC
C. The Joint Commission alone
D. The dosimetrist on call
Answer: B
Objective: V.5
Why: Agreement States license and inspect byproduct material under a framework compatible with the NRC. In non-Agreement States the NRC does that directly. Correct choice: The state, under rules compatible with the NRC. Agreement States have taken that authority. Accreditation is not the radioactive-materials license. A person does not replace the regulator.

### Q2
Stem: Which document must exist before a therapeutic HDR fraction?
A. A Mayneord F worksheet only
B. A written directive
C. A TG-142 daily linac output sheet only
D. An unsigned verbal dose from the hallway
Answer: B
Objective: V.5
Why: NRC and compatible state rules require a written directive for therapeutic brachytherapy: isotope, site, dose, and, for HDR, the details the regulation lists. Treatment without it is a medical-event problem, not a paperwork nicety. Correct choice: A written directive. An external PDD factor is not the HDR prescription. Linac output does not authorize an HDR treatment. Therapeutic brachytherapy needs a signed written directive.

### Q3
Stem: How often are most sealed brachytherapy sources leak-tested?
A. Every day, like a linac door interlock
B. Only after the source is retired
C. Every 30 years
D. Every 6 months
Answer: D
Objective: V.5
Why: Sealed sources in medical use are generally leak-tested at intervals not to exceed 6 months, unless a specific exemption applies. Correct choice: Every 6 months. The door interlock is a linac daily check. Leak tests of sealed sources are periodic, commonly semiannual. You need the test while the source is in use. That is a Cs-137 half-life, not a leak-test interval.

### Q4
Stem: The public release criterion most often cited for a patient who contains radioactive material is a dose to another person not exceeding what?
A. 50 mSv
B. 500 mSv
C. 5 Gy
D. 5 mSv
Answer: D
Objective: V.5
Why: Under the NRC patient-release rule, a patient may be released if the total effective dose equivalent to any other individual is not likely to exceed 5 mSv (500 mrem). Correct choice: 5 mSv. 50 mSv is the NCRP 116 occupational annual limit, not the patient-release criterion. 500 mSv is the occupational extremity limit in NCRP 116, not release. 5 Gy in an hour is a very-high-radiation-area posting idea, not patient release.

### Q5
Stem: A source inventory cannot find one Ir-192 seed. What is required?
A. Nothing until the next leak test
B. A search and a report according to the license
C. Only a note in the linac logbook
D. Decay-correct the missing source and close the log
Answer: B
Objective: V.5
Why: License conditions require inventory and accountability. A missing source triggers a search and the notifications the license and regulations specify. Correct choice: A search and a report according to the license. A missing source is immediate, not deferred to the semiannual test. The linac log is the wrong record. Decay math does not find a source.

## Brachytherapy Quiz

### Q1
Stem: Quiz. An Ir-192 source had a calibration activity of 6.2 Ci. Elapsed time is 30 days. The half-life is 73.8 days. What activity remains?
A. 3.68 Ci
B. 4.68 Ci
C. 3.10 Ci
D. 5.10 Ci
Answer: B
Objective: V.6
Why: Number of half-lives = 30/73.8 = 0.4065. Fraction remaining = (1/2)^(0.4065) = 0.7544. Activity = 6.2 × 0.7544 = 4.6776 Ci, reported as 4.68 Ci. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.4065) = 0.7544. A linear model A0×(1−t/T½) gives 3.68 Ci and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 3.10 Ci. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 5.10 Ci. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q2
Stem: Quiz. A permanent I-125 implant has an initial dose rate of 5 cGy/h and a half-life of 59.4 days. What is the total dose to complete decay, to the nearest cGy?
A. 10286 cGy
B. 4940 cGy
C. 7128 cGy
D. 429 cGy
Answer: A
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 59.4 = 85.7142 days = 85.7142 × 24 = 2057.1408 hours. Total dose = 5 cGy/h × 2057.1408 h = 10285.7 cGy, reported as 10286 cGy. In one line: 5 × 1.443 × 59.4 × 24 = 10285.7. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 4940 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 7128 cGy. Forgetting to convert days to hours (omitting ×24) gives 429 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q3
Stem: Quiz. The exposure-rate constant Γ is 8.25 R·cm²/(mCi·h). Activity is 10 mCi. Distance is 50 cm. What is the exposure rate?
A. 1.650 R/h
B. 0.033 R/h
C. 0.033 mR/h
D. 0.008 R/h
Answer: B
Objective: V.6
Why: Substitute 8.25 × 10 / (50)^2 = 82.5 / 2500 = 0.033000 R/h, reported as 0.033 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 1.650 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.033 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.008 R/h.

### Q4
Stem: Quiz. An HDR course is 3 fractions of 8 Gy. Use α/β = 10 Gy. What is the BED?
A. 24.0 Gy
B. 54.0 Gy
C. 36.0 Gy
D. 43.2 Gy
Answer: D
Objective: V.6
Why: Physical dose = 3 × 8 = 24 Gy. Relative effectiveness = 1 + 8/10 = 1 + 0.8000 = 1.8000. BED = 24 × 1.8000 = 43.20 Gy, reported as 43.2 Gy. EQD2 would divide this BED by (1 + 2/(α/β)) = 1.2000, giving 36.00 Gy. That is a different question. Stopping at the physical dose gives 24.0 Gy and omits the fraction-size term. Inverting the fraction-size term to 1+(α/β)/d gives 54.0 Gy. Reporting the EQD2 (36.0 Gy) answers a different quantity than BED.

### Q5
Stem: Quiz. The same HDR course is 3 fractions of 8 Gy. Use α/β = 10 Gy. What is the EQD2?
A. 36.0 Gy
B. 43.2 Gy
C. 24.0 Gy
D. 52.8 Gy
Answer: A
Objective: V.6
Why: Physical dose = 3 × 8 = 24 Gy. BED = 24 × (1 + 8/10) = 24 × 1.8000 = 43.20 Gy. The 2 Gy denominator factor is 1 + 2/10 = 1.2000. EQD2 = 43.20 / 1.2000 = 36.00 Gy, reported as 36.0 Gy. If the fraction size is already 2 Gy, EQD2 equals the physical dose for any α/β. Here the fraction size is 8 Gy, so that shortcut applies only when d = 2. Stopping at the BED and not dividing by (1+2/(α/β)) gives 43.2 Gy. Reporting only the physical dose gives 24.0 Gy. Using α/β = 3 Gy instead of 10 Gy gives 52.8 Gy.

### Q6
Stem: Quiz. TG-43 point with a radial dose function below 1. Air-kerma strength Sk = 1.8 U, dose-rate constant Λ = 1 cGy/(h·U), geometry function ratio G/G0 = 1, radial dose function g(r) = 0.9, and anisotropy F = 1. What is the dose rate?
A. 1.80 cGy/h
B. 2.00 cGy/h
C. 1.46 cGy/h
D. 1.62 cGy/h
Answer: D
Objective: V.6
Why: Substitute 1.8 × 1 = 1.8000. × 1 = 1.8000. × 0.9 = 1.6200. × 1 = 1.6200 cGy/h, reported as 1.62 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Using only Sk × Λ × F and dropping geometry and radial dose gives 1.80 cGy/h. Dividing by g(r) instead of multiplying gives 2.00 cGy/h. Squaring the radial dose function gives 1.46 cGy/h.

### Q7
Stem: Which source is typically HDR?
A. Ir-192 in a remote afterloader
B. I-125 seeds left in the prostate
C. Pd-103 seeds
D. A superficial orthovoltage tube
Answer: A
Objective: V.2
Why: HDR in the clinic is usually an Ir-192 stepping source in a remote afterloader, dose rate above 12 Gy/h. Permanent seeds are a different modality. Correct choice: Ir-192 in a remote afterloader. Those are permanent LDR seeds. Also a permanent seed. That is an external x-ray unit.

### Q8
Stem: Point A is used for which classic treatment?
A. Whole-brain opposed laterals
B. Permanent I-125 as the only target point required by TG-43
C. Electron cutout output
D. Cervical brachytherapy
Answer: D
Objective: V.2
Why: Point A belongs to intracavitary cervical brachytherapy. It is 2 cm superior and 2 cm lateral to the os/tandem reference. Correct choice: Cervical brachytherapy. That is external beam. TG-43 is a dose-calculation formalism, not a statement that point A is the prostate target. Cutout factors are external electrons.

## Brachytherapy Calculations

### Q1
Stem: Calculation. A permanent I-125 implant has an initial dose rate of 8 cGy/h and a half-life of 59.4 days. What is the total dose to complete decay, to the nearest cGy?
A. 7904 cGy
B. 11405 cGy
C. 16457 cGy
D. 686 cGy
Answer: C
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 59.4 = 85.7142 days = 85.7142 × 24 = 2057.1408 hours. Total dose = 8 cGy/h × 2057.1408 h = 16457.1 cGy, reported as 16457 cGy. In one line: 8 × 1.443 × 59.4 × 24 = 16457.1. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 7904 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 11405 cGy. Forgetting to convert days to hours (omitting ×24) gives 686 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q2
Stem: Calculation. A permanent Cs-131 implant has an initial dose rate of 12 cGy/h and a half-life of 9.7 days. What is the total dose to complete decay, to the nearest cGy?
A. 1936 cGy
B. 4031 cGy
C. 2794 cGy
D. 168 cGy
Answer: B
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 9.7 = 13.9971 days = 13.9971 × 24 = 335.9304 hours. Total dose = 12 cGy/h × 335.9304 h = 4031.2 cGy, reported as 4031 cGy. In one line: 12 × 1.443 × 9.7 × 24 = 4031.2. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 1936 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 2794 cGy. Forgetting to convert days to hours (omitting ×24) gives 168 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q3
Stem: Calculation. A permanent Au-198 implant has an initial dose rate of 20 cGy/h and a half-life of 2.7 days. What is the total dose to complete decay, to the nearest cGy?
A. 898 cGy
B. 1296 cGy
C. 78 cGy
D. 1870 cGy
Answer: D
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 2.7 = 3.8961 days = 3.8961 × 24 = 93.5064 hours. Total dose = 20 cGy/h × 93.5064 h = 1870.1 cGy, reported as 1870 cGy. In one line: 20 × 1.443 × 2.7 × 24 = 1870.1. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 898 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 1296 cGy. Forgetting to convert days to hours (omitting ×24) gives 78 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q4
Stem: Calculation. An I-125 source has an initial dose rate of 25 cGy/day and a half-life of 59.4 days. What is the total dose to complete decay, to the nearest cGy?
A. 1029 cGy
B. 1485 cGy
C. 51429 cGy
D. 2143 cGy
Answer: D
Objective: V.6
Why: Units already match, so mean life in days is 1.443 × 59.4 = 85.7142 days. Total = 25 × 1.443 × 59.4 = 25 × 85.7142 = 2142.86 cGy, reported as 2143 cGy. Using 0.693 instead of 1.443 gives 1029 cGy. Using the half-life with no mean-life factor gives 1485 cGy. Multiplying by an extra 24, as if the dose rate were per hour, gives 51429 cGy.

### Q5
Stem: Calculation. Air-kerma strength at calibration was 37000 U. Elapsed time is 14 days. The half-life is 73.8 days. What activity remains?
A. 29981 U
B. 18500 U
C. 32441 U
D. 33777 U
Answer: C
Objective: V.6
Why: Number of half-lives = 14/73.8 = 0.1897. Fraction remaining = (1/2)^(0.1897) = 0.8768. Activity = 37000 × 0.8768 = 32441.1143 U, reported as 32441 U. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.1897) = 0.8768. A linear model A0×(1−t/T½) gives 29981 U and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 18500 U. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 33777 U. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q6
Stem: Calculation. TG-43 point: air-kerma strength Sk = 5 U, dose-rate constant Λ = 1.11 cGy/(h·U), geometry function ratio G/G0 = 0.85, radial dose function g(r) = 0.96, and anisotropy F = 0.91. What is the dose rate?
A. 4.53 cGy/h
B. 4.12 cGy/h
C. 5.05 cGy/h
D. 4.85 cGy/h
Answer: B
Objective: V.6
Why: Substitute 5 × 1.11 = 5.5500. × 0.85 = 4.7175. × 0.96 = 4.5288. × 0.91 = 4.1212 cGy/h, reported as 4.12 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Dropping anisotropy gives 4.53 cGy/h. Using only Sk × Λ × F and dropping geometry and radial dose gives 5.05 cGy/h. Dropping the geometry ratio gives 4.85 cGy/h.

### Q7
Stem: Calculation. The exposure-rate constant Γ is 4.69 R·cm²/(mCi·h). Activity is 8000 mCi. Distance is 50 cm. What is the exposure rate?
A. 750.40 R/h
B. 15.01 R/h
C. 0.02 R/h
D. 3.75 R/h
Answer: B
Objective: V.6
Why: Substitute 4.69 × 8000 / (50)^2 = 37520 / 2500 = 15.008000 R/h, reported as 15.01 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 750.40 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.02 R/h. Doubling the distance inside the square (a 2× distance error) gives 3.75 R/h.

### Q8
Stem: Calculation. An HDR course is 5 fractions of 6 Gy. Use α/β = 10 Gy. What is the EQD2?
A. 40.0 Gy
B. 48.0 Gy
C. 30.0 Gy
D. 54.0 Gy
Answer: A
Objective: V.6
Why: Physical dose = 5 × 6 = 30 Gy. BED = 30 × (1 + 6/10) = 30 × 1.6000 = 48.00 Gy. The 2 Gy denominator factor is 1 + 2/10 = 1.2000. EQD2 = 48.00 / 1.2000 = 40.00 Gy, reported as 40.0 Gy. If the fraction size is already 2 Gy, EQD2 equals the physical dose for any α/β. Here the fraction size is 6 Gy, so that shortcut applies only when d = 2. Stopping at the BED and not dividing by (1+2/(α/β)) gives 48.0 Gy. Reporting only the physical dose gives 30.0 Gy. Using α/β = 3 Gy instead of 10 Gy gives 54.0 Gy.

## Brachytherapy Calculations Quiz

### Q1
Stem: Calculations quiz. A permanent Pd-103 implant has an initial dose rate of 6 cGy/h and a half-life of 17 days. What is the total dose to complete decay, to the nearest cGy?
A. 1696 cGy
B. 2448 cGy
C. 3532 cGy
D. 147 cGy
Answer: C
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 17 = 24.5310 days = 24.5310 × 24 = 588.7440 hours. Total dose = 6 cGy/h × 588.7440 h = 3532.5 cGy, reported as 3532 cGy. In one line: 6 × 1.443 × 17 × 24 = 3532.5. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 1696 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 2448 cGy. Forgetting to convert days to hours (omitting ×24) gives 147 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q2
Stem: Calculations quiz. A permanent I-125 implant has an initial dose rate of 4 cGy/h and a half-life of 59.4 days. What is the total dose to complete decay, to the nearest cGy?
A. 3952 cGy
B. 8229 cGy
C. 5702 cGy
D. 343 cGy
Answer: B
Objective: V.6
Why: 1.443 × half-life is the mean life. The source is never removed, so the total dose is initial dose rate times mean life, not times half-life and not times 0.693. Mean life = 1.443 × 59.4 = 85.7142 days = 85.7142 × 24 = 2057.1408 hours. Total dose = 4 cGy/h × 2057.1408 h = 8228.6 cGy, reported as 8229 cGy. In one line: 4 × 1.443 × 59.4 × 24 = 8228.6. Replacing 1.443 with 0.693 uses ln(2) instead of the mean-life factor 1/ln(2) and gives 3952 cGy. Multiplying dose rate by the half-life in hours but forgetting the 1.443 mean-life factor gives 5702 cGy. Forgetting to convert days to hours (omitting ×24) gives 343 cGy, which is numerically a dose rate times a day-count and is far too small.

### Q3
Stem: Calculations quiz. Activity at calibration was 9.4 Ci. Elapsed time is 10 days. The half-life is 73.8 days. What activity remains?
A. 8.56 Ci
B. 8.13 Ci
C. 4.70 Ci
D. 8.81 Ci
Answer: A
Objective: V.6
Why: Number of half-lives = 10/73.8 = 0.1355. Fraction remaining = (1/2)^(0.1355) = 0.9104. Activity = 9.4 × 0.9104 = 8.5573 Ci, reported as 8.56 Ci. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.1355) = 0.9104. A linear model A0×(1−t/T½) gives 8.13 Ci and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 4.70 Ci. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 8.81 Ci. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q4
Stem: Calculations quiz. Activity at calibration was 25000 U. Elapsed time is 40 days. The half-life is 73.8 days. What activity remains?
A. 11450 U
B. 12500 U
C. 17170 U
D. 19269 U
Answer: C
Objective: V.6
Why: Number of half-lives = 40/73.8 = 0.5420. Fraction remaining = (1/2)^(0.5420) = 0.6868. Activity = 25000 × 0.6868 = 17170.3884 U, reported as 17170 U. The same fraction is e^(−ln(2) × t/T½) = e^(−0.6931 × 0.5420) = 0.6868. A linear model A0×(1−t/T½) gives 11450 U and is not radioactive decay. Assuming a full half-life has passed and taking half of A0 gives 12500 U. Using the mean life (1.443×T½) in place of the half-life inside (1/2)^(t/T) gives 19269 U. Decay itself is e^(−t/mean life), which is the same as (1/2)^(t/T½), so the mean life does not belong in that exponent as a substitute half-life.

### Q5
Stem: Calculations quiz. The exposure-rate constant Γ is 3.26 R·cm²/(mCi·h). Activity is 20 mCi. Distance is 20 cm. What is the exposure rate?
A. 0.163 R/h
B. 3.260 R/h
C. 0.163 mR/h
D. 0.041 R/h
Answer: A
Objective: V.6
Why: Substitute 3.26 × 20 / (20)^2 = 65.2 / 400 = 0.163000 R/h, reported as 0.163 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 3.260 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.163 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.041 R/h.

### Q6
Stem: Calculations quiz. The exposure-rate constant Γ is 13.07 R·cm²/(mCi·h). Activity is 5 mCi. Distance is 100 cm. What is the exposure rate?
A. 0.0065 R/h
B. 0.6535 R/h
C. 0.0065 mR/h
D. 0.0016 R/h
Answer: A
Objective: V.6
Why: Substitute 13.07 × 5 / (100)^2 = 65.35 / 10000 = 0.006535 R/h, reported as 0.0065 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 0.6535 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.0065 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.0016 R/h.

### Q7
Stem: Calculations quiz. TG-43 point: air-kerma strength Sk = 4.2 U, dose-rate constant Λ = 0.965 cGy/(h·U), geometry function ratio G/G0 = 0.78, radial dose function g(r) = 1, and anisotropy F = 0.95. What is the dose rate?
A. 3.16 cGy/h
B. 3.85 cGy/h
C. 3.00 cGy/h
D. 4.05 cGy/h
Answer: C
Objective: V.6
Why: Substitute 4.2 × 0.965 = 4.0530. × 0.78 = 3.1613. × 1 = 3.1613. × 0.95 = 3.0033 cGy/h, reported as 3.00 cGy/h. Leaving out anisotropy is a common independent-check miss when the point is not on the transverse axis, where F is not 1. Dropping anisotropy gives 3.16 cGy/h. Using only Sk × Λ × F and dropping geometry and radial dose gives 3.85 cGy/h. Stopping after Sk × Λ gives 4.05 cGy/h.

### Q8
Stem: Calculations quiz. An HDR course is 4 fractions of 7 Gy. Use α/β = 10 Gy. What is the BED?
A. 28.0 Gy
B. 68.0 Gy
C. 39.7 Gy
D. 47.6 Gy
Answer: D
Objective: V.6
Why: Physical dose = 4 × 7 = 28 Gy. Relative effectiveness = 1 + 7/10 = 1 + 0.7000 = 1.7000. BED = 28 × 1.7000 = 47.60 Gy, reported as 47.6 Gy. EQD2 would divide this BED by (1 + 2/(α/β)) = 1.2000, giving 39.67 Gy. That is a different question. Stopping at the physical dose gives 28.0 Gy and omits the fraction-size term. Inverting the fraction-size term to 1+(α/β)/d gives 68.0 Gy. Reporting the EQD2 (39.7 Gy) answers a different quantity than BED.

## Exposure Rate Calculation Tutorial

### Q1
Stem: Tutorial. A 10 Ci source has already been converted to 10000 mCi. The exposure-rate constant Γ is 4.69 R·cm²/(mCi·h). Distance is 100 cm. What is the exposure rate?
A. 469.00 R/h
B. 4.69 R/h
C. 4.69 mR/h
D. 1.17 R/h
Answer: B
Objective: V.6
Why: Substitute 4.69 × 10000 / (100)^2 = 46900 / 10000 = 4.690000 R/h, reported as 4.69 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 469.00 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 4.69 mR/h. Doubling the distance inside the square (a 2× distance error) gives 1.17 R/h.

### Q2
Stem: Tutorial. The same source has exposure-rate constant Γ of 4.69 R·cm²/(mCi·h) and activity 10000 mCi. Distance is 50 cm. What is the exposure rate?
A. 938.00 R/h
B. 0.02 R/h
C. 18.76 R/h
D. 4.69 R/h
Answer: C
Objective: V.6
Why: Substitute 4.69 × 10000 / (50)^2 = 46900 / 2500 = 18.760000 R/h, reported as 18.76 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 938.00 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.02 R/h. Doubling the distance inside the square (a 2× distance error) gives 4.69 R/h.

### Q3
Stem: Tutorial. The same source has exposure-rate constant Γ of 4.69 R·cm²/(mCi·h) and activity 10000 mCi. Distance is 200 cm. What is the exposure rate?
A. 1.173 R/h
B. 234.500 R/h
C. 0.001 R/h
D. 0.293 R/h
Answer: A
Objective: V.6
Why: Substitute 4.69 × 10000 / (200)^2 = 46900 / 40000 = 1.172500 R/h, reported as 1.173 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 234.500 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.001 R/h. Doubling the distance inside the square (a 2× distance error) gives 0.293 R/h.

### Q4
Stem: Tutorial. A classic radium-equivalent constant is used at 1 m. The exposure-rate constant Γ is 8.25 R·cm²/(mCi·h). Activity is 10 mCi. Distance is 100 cm. What is the exposure rate?
A. 0.8250 R/h
B. 0.0083 R/h
C. 0.0083 mR/h
D. 0.0021 R/h
Answer: B
Objective: V.6
Why: Substitute 8.25 × 10 / (100)^2 = 82.5 / 10000 = 0.008250 R/h, reported as 0.0083 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 0.8250 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.0083 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.0021 R/h.

### Q5
Stem: Tutorial. Move that source to 25 cm. The exposure-rate constant Γ is 8.25 R·cm²/(mCi·h). Activity is 10 mCi. Distance is 25 cm. What is the exposure rate?
A. 3.300 R/h
B. 0.132 mR/h
C. 0.132 R/h
D. 0.033 R/h
Answer: C
Objective: V.6
Why: Substitute 8.25 × 10 / (25)^2 = 82.5 / 625 = 0.132000 R/h, reported as 0.132 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 3.300 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.132 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.033 R/h.

### Q6
Stem: Tutorial. The exposure-rate constant Γ is 3.26 R·cm²/(mCi·h). Activity is 100 mCi. Distance is 50 cm. What is the exposure rate?
A. 6.520 R/h
B. 0.130 R/h
C. 0.130 mR/h
D. 0.033 R/h
Answer: B
Objective: V.6
Why: Substitute 3.26 × 100 / (50)^2 = 326 / 2500 = 0.130400 R/h, reported as 0.130 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 6.520 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.130 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.033 R/h.

### Q7
Stem: Tutorial. The exposure-rate constant Γ is 13.07 R·cm²/(mCi·h). Activity is 2 mCi. Distance is 30 cm. What is the exposure rate?
A. 0.8713 R/h
B. 0.0290 mR/h
C. 0.0073 R/h
D. 0.0290 R/h
Answer: D
Objective: V.6
Why: Substitute 13.07 × 2 / (30)^2 = 26.14 / 900 = 0.029044 R/h, reported as 0.0290 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 0.8713 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 0.0290 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.0073 R/h.

### Q8
Stem: Tutorial. The exposure-rate constant Γ is 4.6 R·cm²/(mCi·h). Activity is 2500 mCi. Distance is 100 cm. What is the exposure rate?
A. 115.00 R/h
B. 1.15 mR/h
C. 0.29 R/h
D. 1.15 R/h
Answer: D
Objective: V.6
Why: Substitute 4.6 × 2500 / (100)^2 = 11500 / 10000 = 1.150000 R/h, reported as 1.15 R/h. If the activity had been given in curies, it would need ×1000 to become mCi before using a per-mCi gamma constant. Moving the point and applying inverse square is the same d² already in this formula. Forgetting to square the distance gives 115.00 R/h. Dividing an extra 1000, as if the activity were still in curies after it was already converted to mCi, gives 1.15 mR/h. Doubling the distance inside the square (a 2× distance error) gives 0.29 R/h.

## Strength, points, prescriptions, and directives

### Q1
Stem: Which statement defines 1 U of air-kerma strength?
A. 1 µGy m²/h, which is the same as 1 cGy cm²/h
B. 1 mCi of apparent activity
C. 1 Gy at 1 cm in water
D. 1 R cm² per mCi per hour
Answer: A
Objective: V.1
Why: One unit of air-kerma strength is 1 µGy m²/h, and that product is the same as 1 cGy cm²/h. Sk is the source specification in TG-43. Apparent activity in mCi is a derived label, not the definition of 1 U. A gray at 1 cm is a dose. The R cm² per mCi per hour quantity is an exposure-rate constant.

### Q2
Stem: A certificate lists both an apparent activity and an air-kerma strength. Which quantity specifies the source for TG-43 in this bank?
A. Apparent activity, using one mCi-per-U factor for every nuclide
B. The exposure-rate constant alone
C. The half-life alone
D. Air-kerma strength, Sk
Answer: D
Objective: V.1
Why: TG-43 uses Sk. Apparent activity is a derived label. This bank does not quote one mCi-per-U factor. The exposure-rate constant is the survey route, and the half-life is for decay, not the source specification.

### Q3
Stem: In an HDR plan, what is the dwell time at one stopping position?
A. The half-life of Ir-192
B. The cylinder radius
C. The dose wanted from that stop, divided by the dose rate at that stop
D. The number of fractions in the course
Answer: C
Objective: V.2
Why: Dwell time is dose divided by dose rate at that dwell. The afterloader holds the source there for that time. Half-life, radius, and fraction count belong to other parts of the plan.

### Q4
Stem: An HDR plan was timed on the calibration day, and treatment is several days later. What is done with the dwell times?
A. They stay at the calibration-day times, because a week of Ir-192 decay is ignored
B. They are decayed to the treatment date so the weaker source still delivers the prescribed dose
C. They are replaced by the mean life
D. They are set equal to the leak-test interval
Answer: B
Objective: V.6
Why: The time used on the treatment day is the time corrected for decay to that date. A weaker source needs a longer dwell for the same dose. Calibration-day times left unchanged underdose. Mean life is the permanent-implant integral, not an HDR dwell. The leak test is a six-month wipe, not a dwell time.

### Q5
Stem: Where is the ICRU 38 bladder point?
A. 2 cm superior to the os and 2 cm lateral to the tandem
B. 5 mm behind the posterior vaginal wall
C. At the apex of an eye plaque
D. Center of a 7 cm³ Foley balloon on the anterior film, and the posterior surface of that balloon on the lateral film
Answer: D
Objective: V.2
Why: The ICRU 38 bladder point uses a Foley balloon filled with 7 cm³ of contrast: the center of the balloon on the anterior radiograph, and the posterior surface of the balloon on the lateral radiograph. Two centimeters up and two centimeters lateral is Manchester point A. Five millimeters behind the vaginal wall is the rectal point. The eye-plaque apex is an ocular prescription point.

### Q6
Stem: Where is the ICRU 38 rectum point?
A. 5 mm posterior to the posterior vaginal wall, on the midline, at the mid-ovoid level
B. The center of the Foley balloon
C. 5 cm from the patient’s midline
D. The hottest 2 cm³ of the bladder
Answer: A
Objective: V.2
Why: The rectal reference point sits 5 mm behind the posterior vaginal wall, on the midline, at the level of the middle of the ovoids. The Foley balloon defines the bladder point. Five centimeters from the midline is point B. Bladder D2cc is a contoured volume dose, not this film point.

### Q7
Stem: In the GEC-ESTRO correlates used in this bank, what is HR-CTV D90?
A. The dose to 90% of the rectum
B. Manchester point A
C. The dose that covers 90% of the high-risk clinical target volume
D. Total reference air kerma
Answer: C
Objective: V.2
Why: HR-CTV D90 is the dose covering 90% of the high-risk CTV, residual disease plus the cervix at brachytherapy. It is the target-coverage correlate in this bank. It is not a rectal dose, not point A, and not TRAK.

### Q8
Stem: Which organ correlate does this bank hold near 65–75 Gy EQD2?
A. Bladder D2cc
B. Rectum D2cc
C. A single HDR fraction at point A
D. Patient release to another person
Answer: B
Objective: V.2
Why: In this bank, rectum D2cc is often held near 65–75 Gy EQD2. Bladder D2cc is the higher band, near 80–90 Gy EQD2. One fraction at point A is a physical dose. Five millisieverts is the release criterion, not a rectal EQD2.

### Q9
Stem: Which organ correlate does this bank hold near 80–90 Gy EQD2?
A. Rectum D2cc
B. Vaginal surface dose from a cylinder
C. A public dose of 5 mSv
D. Bladder D2cc
Answer: D
Objective: V.2
Why: This bank holds bladder D2cc near 80–90 Gy EQD2. Rectum D2cc is the 65–75 Gy EQD2 band. A cylinder surface dose is not that bladder correlate. Five millisieverts is patient release for another person.

### Q10
Stem: Which prescription matches the HDR vaginal-cuff course in this bank?
A. 7 Gy times 3, specified at 0.5 cm from the cylinder surface
B. 13.5 Gy times 2 to the prostate
C. 145 Gy with I-125 seeds
D. 85 Gy to the apex of an eye plaque
Answer: A
Objective: V.2
Why: The vaginal-cuff regimen to memorize is 7 Gy × 3 at 0.5 cm. A prostate HDR boost of 13.5 Gy × 2, I-125 monotherapy of 145 Gy, and an eye plaque of 85 Gy to the apex are different prescriptions.

### Q11
Stem: Which pair are the cervix HDR fractionations this bank expects you to recognize?
A. 2 Gy times 25, and 1.8 Gy times 28
B. 13.5 Gy times 2 only
C. 7 Gy times 4, or 5.5 Gy times 5
D. 125 Gy with Pd-103 seeds
Answer: C
Objective: V.2
Why: Cervix HDR in this bank is often 7 Gy × 4 or 5.5 Gy × 5. Daily external-beam fractions are not those HDR schedules. 13.5 Gy × 2 is a prostate HDR boost. 125 Gy is Pd-103 monotherapy.

### Q12
Stem: Which fractionation is one common prostate HDR boost in this bank?
A. 7 Gy times 3 at 0.5 cm
B. 13.5 Gy times 2
C. 5.5 Gy times 5 to the cervix
D. 85 Gy to the sclera
Answer: B
Objective: V.2
Why: One common prostate HDR boost here is 13.5 Gy × 2. The 7 Gy × 3 course is vaginal cuff. The 5.5 Gy × 5 course is cervix. The eye-plaque dose is 85 Gy to the apex, not the sclera.

### Q13
Stem: Which monotherapy doses does this bank pair with permanent prostate seeds?
A. I-125 125 Gy and Pd-103 145 Gy
B. Both 85 Gy to the apex
C. Both 7 Gy times 4
D. I-125 145 Gy and Pd-103 125 Gy
Answer: D
Objective: V.2
Why: I-125 monotherapy is 145 Gy. Pd-103 monotherapy is 125 Gy. Swapping them is the usual trap. 85 Gy is the eye-plaque apex dose. 7 Gy × 4 is cervix HDR.

### Q14
Stem: An I-125 eye plaque in this bank is prescribed to which dose and point?
A. 85 Gy to the apex
B. 145 Gy to the prostate
C. 125 Gy to the base of the plaque
D. 7 Gy times 3 at 0.5 cm
Answer: A
Objective: V.2
Why: The I-125 eye-plaque prescription to memorize is 85 Gy to the tumor apex. 145 Gy is prostate I-125 monotherapy. The plaque point is the apex, not the base. The 7 Gy × 3 course is a vaginal cylinder.

### Q15
Stem: Which mean photon energy belongs with Ir-192?
A. About 21 keV
B. About 28 keV
C. About 380 keV
D. 662 keV
Answer: C
Objective: V.1
Why: Ir-192 is remembered at about 380 keV mean, the same as about 0.38 MeV. Pd-103 is about 21 keV, I-125 is about 28 keV, and Cs-137 is 662 keV.

### Q16
Stem: Which energies match Cs-137 and the two permanent seed nuclides?
A. Cs-137 about 380 keV, and both seeds at 662 keV
B. Cs-137 662 keV, I-125 about 28 keV, and Pd-103 about 21 keV
C. Cs-137 about 21 keV, and I-125 at 662 keV
D. All three about 380 keV
Answer: B
Objective: V.1
Why: Cs-137 is 662 keV. I-125 is about 28 keV and Pd-103 is about 21 keV. Ir-192, not cesium, is the source near 380 keV. The three nuclides are not one energy.

### Q17
Stem: Before an HDR fraction, which set must the written directive contain?
A. Only the linac monitor units
B. Only a verbal order from the hallway
C. Only the exposure-rate constant
D. Radionuclide, treatment site, dose per fraction, number of fractions, and total dose
Answer: D
Objective: V.5
Why: Under 10 CFR 35.40 the HDR written directive, dated and signed by the authorized user before treatment, states the radionuclide, the site, the dose per fraction, the number of fractions, and the total dose. Monitor units, a verbal order, and an exposure-rate constant do not replace that directive.

### Q18
Stem: Before a permanent seed implant, what does the written directive state?
A. The radionuclide, the treatment site, and the total source strength
B. Only the room-survey background
C. Another patient’s bladder D2cc
D. A linac wedge angle
Answer: A
Objective: V.5
Why: Before seeds are implanted, the written directive carries the radionuclide, the site, and the total source strength. That is the activity form of the order. A survey background, another patient’s organ dose, and a wedge angle do not authorize the implant.

### Q19
Stem: For a temporary LDR implant, the written directive can state the dose, or which activity-and-time pair?
A. The quarterly inventory date only
B. Point A with no dose
C. Total source strength and the exposure time
D. Only the patient’s release reading
Answer: C
Objective: V.5
Why: When an LDR directive is not written as a dose, it states the total source strength and the time the sources are applied. An inventory date, a geometry point without a dose, and a release survey do not replace that order. The teaching set is nuclide, site, and dose, or activity and time.

### Q20
Stem: Which administration matches the usual teaching form of a medical event?
A. A leak-test result under 185 Bq
B. A delivered dose about 20% away from the prescribed dose
C. A background survey before the implant
D. An agreement-state license posted on the door
Answer: B
Objective: V.5
Why: In the usual teaching form, a medical event includes a dose that differs by about 20% of the prescribed dose, or by about 50% of one fraction, and also the wrong patient or the wrong site. A leak test under 185 Bq passes. Background and a posted license are not an administration error.

### Q21
Stem: One HDR fraction delivers about 50% more than that fraction’s written dose. What follows in this bank?
A. Later fractions are assumed to average it out, so nothing is reported
B. The half-life in the chart is edited and the log is closed
C. The case is handled only as a 5 mSv release decision
D. It is a medical event in the usual teaching form: verbal report in about 24 hours and a written report in about 15 days
Answer: D
Objective: V.5
Why: About 50% of a fraction is the per-fraction teaching threshold. The report is verbal in about 24 hours and written in about 15 days. Hoping later fractions will average the miss does not erase it. Changing the half-life is not the report. Patient release at 5 mSv is a separate rule about dose to another person.

### Q22
Stem: Brachytherapy is delivered to the wrong patient. Which statement fits the teaching form of 10 CFR 35.3045?
A. Wrong patient is a medical event
B. Wrong patient counts only when the dose is also 20% high
C. Wrong site is ignored when the nuclide was correct
D. No report is due if the console said the source retracted
Answer: A
Objective: V.5
Why: Wrong patient and wrong site are medical events in this teaching form, not only a percent-dose miss. A correct nuclide in the wrong place is still the wrong site. A retracted-source light does not undo treatment of the wrong person. The clocks remain about 24 hours verbal and about 15 days written.

### Q23
Stem: What does this bank mean by TRAK?
A. The dose at Manchester point A
B. The leak-test activity on the wipe
C. The sum over sources of reference air-kerma rate times duration
D. The EQD2 of bladder D2cc
Answer: C
Objective: V.6
Why: Total reference air kerma adds, for every source, the reference air-kerma rate multiplied by how long that source is applied. It describes the application at the reference distance. It is not point A, not a wipe test, and not an organ EQD2.

### Q24
Stem: What belongs in the HDR emergency kit named in this note?
A. A linac wedge and a Mayneord worksheet
B. Long tongs and a shielded container
C. Only a personnel film badge
D. A Foley balloon filled to 7 cm³
Answer: B
Objective: V.2
Why: If the source will not return, the kit has long tongs and a shielded container so the applicator can be moved and the source shielded. A wedge worksheet, a badge, and the bladder-point balloon are not that kit. The survey meter stays on, and the patient is surveyed after the source is back in the safe.

### Q25
Stem: Which pair does this bank name for brachytherapy physics practice and HDR delivery, without a tolerance table?
A. TG-51 and TG-142
B. ICRU 83 and QUANTEC
C. TG-43 and TG-51
D. TG-56 and TG-59
Answer: D
Objective: V.2
Why: TG-56 is the brachytherapy physics code of practice. TG-59 is the HDR treatment-delivery report. This bank names them and does not attach a tolerance table. TG-51 and TG-142 are external-beam calibration and linac QA. ICRU 83 and QUANTEC are volume and organ-dose reports. TG-43 is the dose formalism, not that delivery pair.

### Q26
Stem: What is the brachytherapy source-inventory idea in this bank?
A. A quarterly physical count of each source, its nuclide, its nominal activity, and its location
B. A daily linac output check
C. A leak test every 30 years
D. A count performed only after a source is retired
Answer: A
Objective: V.5
Why: The inventory idea here is quarterly: what is on hand, which nuclide, what nominal activity, and where it sits. Linac output is external-beam QA. The leak test is about every six months and is a wipe, not this count. Waiting until a source is retired leaves it unaccounted for while it is in use.

### Q27
Stem: Who signs the written directive, who checks the source and the dwells, and who runs the safety program?
A. The dosimetrist signs the directive, the therapist is the radiation safety officer, and the patient is the authorized user
B. The radiation safety officer prescribes the dose, and the authorized user only updates the inventory
C. The authorized user signs the directive, the authorized medical physicist checks the source and the dwells, and the radiation safety officer runs the safety program
D. Any staff member may sign the directive once the console is armed
Answer: C
Objective: V.5
Why: The authorized user is the physician who signs the written directive. The authorized medical physicist checks source calibration, the plan, and the dwells. The radiation safety officer runs the safety program, including inventory, leak tests, and the reports the license requires. A dosimetrist does not prescribe. Arming the console is not a signature.

### Q28
Stem: After the afterloader says the HDR source has returned, what survey is still required?
A. None, if the console light is green
B. A survey of the patient, compared with background, with the meter already on
C. A water-tank calibration of a linac
D. An exit-dose diode on an external beam
Answer: B
Objective: V.4
Why: The source is confirmed home by the unit and by a survey of the patient. The meter is on before the source is sent out, and the reading after return is compared with background. A green light alone is not the survey. A water tank and an exit diode are external-beam checks.
