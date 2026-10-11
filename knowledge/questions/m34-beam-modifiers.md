# Module 34. Effects of beam modifying devices

Original CMD practice items. Not retired MDCB questions and not a commercial quiz.

## Wedges

### Q1
Stem: Which way does a physical wedge tilt the isodose curves?
A. Toward the heel (thick end)
B. Toward the toe (thin end)
C. They stay perpendicular to the central axis
D. They tilt only if the hinge angle is 90°
Answer: A
Objective: IV.2
Why: The heel attenuates more, so a given isodose line sits closer to the surface under the heel and deeper under the toe. The line therefore tilts toward the thick end. Correct choice: Toward the heel (thick end). Dose is higher under the toe, so the isodose for a given value reaches deeper on the toe side and the curve tilts toward the heel. That is the open-beam description at the central axis, before the wedge tilt. The tilt is the wedge angle. The hinge is how two wedged beams are arranged, not the condition for a tilt to exist.

### Q2
Stem: For a sloping surface that is thin on the left, where does the heel of a tissue-compensating wedge belong?
A. Over the thick side
B. Over the thin side
C. Always on the gantry-right, regardless of the slope
D. At the central axis only
Answer: B
Objective: IV.2
Why: The thin side would otherwise be hot because less tissue covers it. The thick end of the wedge (heel) goes over that thin side so both sides move toward the same dose. Correct choice: Over the thin side. The thick side already has more tissue attenuation. Putting the heel there makes the gradient worse. Heel placement follows the missing tissue, not the gantry label. A wedge is a gradient across the field, not a central-axis filter alone.

### Q3
Stem: A physical 45° wedge is measured at the calculation depth. Under the same MU and geometry, the chamber reads 120 with the wedge removed and 78 with the wedge in place. What is the wedge factor (dose with wedge divided by dose without wedge)?
A. 1.538
B. 0.350
C. 0.650
D. 0.825
Answer: C
Objective: IV.2
Why: Wedge factor = reading with wedge / reading without wedge. Substitute 78 / 120 = 0.6500, reported as 0.650. Inverting the ratio (open/wedged) gives 1.538, which is greater than 1 and cannot be a physical wedge factor for a metal wedge that only attenuates. Using the fractional difference (open−wedged)/open gives 0.350, which is the attenuated fraction, not the transmitted factor. Averaging the open and wedged readings and then dividing by the open reading gives 0.825, which is not the transmission.

### Q4
Stem: A dynamic wedge and a physical wedge can share the same nominal wedge angle. Which statement is still true?
A. A dynamic wedge has wedge factor 1 because no metal is in the beam
B. Each still needs its own wedge factor in the MU
C. The physical-wedge factor can be copied to the dynamic wedge
D. Wedge factor is independent of depth for every physical wedge
Answer: B
Objective: IV.2
Why: Whether the gradient comes from metal or from jaw motion, the calculation point sees fewer cGy per MU than the open beam. The MU formula needs the factor measured for that device, depth, and field. Correct choice: Each still needs its own wedge factor in the MU. The jaws spend more time covering the heel side, so dose per MU still falls and the factor is not 1. The factors differ. The dynamic wedge is produced by jaw motion, not by the same attenuation map. Physical wedge factors do change with depth and field size. Using the factor at the wrong depth is a real MU error.

### Q5
Stem: Which factor is the wedge factor?
A. Dose without the wedge divided by dose with the wedge
B. Dose with the wedge divided by dose without the wedge
C. The wedge angle divided by 60°
D. 1 minus the wedge angle over 90°
Answer: B
Objective: IV.2
Why: By definition the wedge factor is the transmitted fraction: dose with wedge / dose open, same MU and geometry. It is the number in the MU denominator. The MU multiplier is 1 over that factor. Correct choice: Dose with the wedge divided by dose without the wedge. That ratio is greater than 1 and is the MU multiplier, not the wedge factor itself. The angle names the isodose tilt. It is not the transmission. That expression is not a measured transmission.

## Wedge Factor Calculation Tutorial

### Q1
Stem: Tutorial measurement at 10 cm depth, 10×10 cm, 6 MV. Under the same MU and geometry, the chamber reads 100 with the wedge removed and 65 with the wedge in place. What is the wedge factor (dose with wedge divided by dose without wedge)?
A. 0.650
B. 1.538
C. 0.350
D. 0.825
Answer: A
Objective: IV.2
Why: Wedge factor = reading with wedge / reading without wedge. Substitute 65 / 100 = 0.6500, reported as 0.650. Inverting the ratio (open/wedged) gives 1.538, which is greater than 1 and cannot be a physical wedge factor for a metal wedge that only attenuates. Using the fractional difference (open−wedged)/open gives 0.350, which is the attenuated fraction, not the transmitted factor. Averaging the open and wedged readings and then dividing by the open reading gives 0.825, which is not the transmission.

### Q2
Stem: Tutorial measurement for a 60° physical wedge. Under the same MU and geometry, the chamber reads 86.4 with the wedge removed and 54 with the wedge in place. What is the wedge factor (dose with wedge divided by dose without wedge)?
A. 1.600
B. 0.375
C. 0.813
D. 0.625
Answer: D
Objective: IV.2
Why: Wedge factor = reading with wedge / reading without wedge. Substitute 54 / 86.4 = 0.6250, reported as 0.625. Inverting the ratio (open/wedged) gives 1.600, which is greater than 1 and cannot be a physical wedge factor for a metal wedge that only attenuates. Using the fractional difference (open−wedged)/open gives 0.375, which is the attenuated fraction, not the transmitted factor. Averaging the open and wedged readings and then dividing by the open reading gives 0.813, which is not the transmission.

### Q3
Stem: Tutorial measurement for a shallow 30° wedge. Under the same MU and geometry, the chamber reads 200 with the wedge removed and 150 with the wedge in place. What is the wedge factor (dose with wedge divided by dose without wedge)?
A. 0.750
B. 1.333
C. 0.250
D. 0.875
Answer: A
Objective: IV.2
Why: Wedge factor = reading with wedge / reading without wedge. Substitute 150 / 200 = 0.7500, reported as 0.750. Inverting the ratio (open/wedged) gives 1.333, which is greater than 1 and cannot be a physical wedge factor for a metal wedge that only attenuates. Using the fractional difference (open−wedged)/open gives 0.250, which is the attenuated fraction, not the transmitted factor. Averaging the open and wedged readings and then dividing by the open reading gives 0.875, which is not the transmission.

### Q4
Stem: Tutorial. The wedge was in the beam and the MU were open-beam MU. The monitor units were calculated for an open beam to deliver 200 cGy at the calculation point. A wedge with wedge factor 0.65 was actually left in the beam. What dose is delivered at that point?
A. 200.0 cGy
B. 130.0 cGy
C. 307.7 cGy
D. 70.0 cGy
Answer: B
Objective: IV.2
Why: The open-beam MU already assume wedge factor 1. With the wedge in the beam every MU is attenuated by the wedge factor, so delivered dose = intended dose × wedge factor. Substitute 200 × 0.65 = 130.00 cGy, reported as 130.0 cGy. The plan underdoses; it does not overdose. Leaving the dose at 200.0 cGy is the open-beam number and ignores the wedge that was in the beam. Dividing by the wedge factor (200/0.65 = 307.7 cGy) is what you do to the MU to restore dose, not what the patient received from the uncorrected MU. Multiplying by (1−wedge factor) treats the factor as if only the attenuated fraction remained in a subtraction sense and gives 70.0 cGy.

### Q5
Stem: Tutorial. A different wedge factor, same omission error. The monitor units were calculated for an open beam to deliver 180 cGy at the calculation point. A wedge with wedge factor 0.72 was actually left in the beam. What dose is delivered at that point?
A. 180.0 cGy
B. 250.0 cGy
C. 129.6 cGy
D. 50.4 cGy
Answer: C
Objective: IV.2
Why: The open-beam MU already assume wedge factor 1. With the wedge in the beam every MU is attenuated by the wedge factor, so delivered dose = intended dose × wedge factor. Substitute 180 × 0.72 = 129.60 cGy, reported as 129.6 cGy. The plan underdoses; it does not overdose. Leaving the dose at 180.0 cGy is the open-beam number and ignores the wedge that was in the beam. Dividing by the wedge factor (180/0.72 = 250.0 cGy) is what you do to the MU to restore dose, not what the patient received from the uncorrected MU. Multiplying by (1−wedge factor) treats the factor as if only the attenuated fraction remained in a subtraction sense and gives 50.4 cGy.

### Q6
Stem: Tutorial. Restore the dose by changing the MU. Open-beam monitor units for this field are 250 MU. The wedge factor is 0.7. What MU should be set so the calculation point still receives the open-beam dose, with the wedge in the beam?
A. 357.1 MU
B. 175.0 MU
C. 250.0 MU
D. 833.3 MU
Answer: A
Objective: IV.2
Why: The wedge lowers dose per MU, so the MU must increase by 1/wedge factor. Substitute 250 / 0.7 = 357.14 MU, reported as 357.1 MU. Multiplying the open MU by the wedge factor (250×0.7 = 175.0 MU) would underdose a second time. Keeping 250.0 MU omits the wedge factor while the wedge is used. Dividing by (1−wedge factor) uses the complement of the factor and gives 833.3 MU.

### Q7
Stem: Tutorial. 30° wedge, open MU already known. Open-beam monitor units for this field are 312 MU. The wedge factor is 0.78. What MU should be set so the calculation point still receives the open-beam dose, with the wedge in the beam?
A. 400.0 MU
B. 243.4 MU
C. 312.0 MU
D. 1418.2 MU
Answer: A
Objective: IV.2
Why: The wedge lowers dose per MU, so the MU must increase by 1/wedge factor. Substitute 312 / 0.78 = 400.00 MU, reported as 400.0 MU. Multiplying the open MU by the wedge factor (312×0.78 = 243.4 MU) would underdose a second time. Keeping 312.0 MU omits the wedge factor while the wedge is used. Dividing by (1−wedge factor) uses the complement of the factor and gives 1418.2 MU.

### Q8
Stem: Tutorial. A heavily attenuating 60° wedge left in by mistake. The monitor units were calculated for an open beam to deliver 240 cGy at the calculation point. A wedge with wedge factor 0.55 was actually left in the beam. What dose is delivered at that point?
A. 132.0 cGy
B. 240.0 cGy
C. 436.4 cGy
D. 108.0 cGy
Answer: A
Objective: IV.2
Why: The open-beam MU already assume wedge factor 1. With the wedge in the beam every MU is attenuated by the wedge factor, so delivered dose = intended dose × wedge factor. Substitute 240 × 0.55 = 132.00 cGy, reported as 132.0 cGy. The plan underdoses; it does not overdose. Leaving the dose at 240.0 cGy is the open-beam number and ignores the wedge that was in the beam. Dividing by the wedge factor (240/0.55 = 436.4 cGy) is what you do to the MU to restore dose, not what the patient received from the uncorrected MU. Multiplying by (1−wedge factor) treats the factor as if only the attenuated fraction remained in a subtraction sense and gives 108.0 cGy.

## Wedge and Hinge Angle

### Q1
Stem: In the simple two-field model, how are wedge angle and hinge angle related?
A. Wedge angle = 90° − (hinge angle)/2
B. Wedge angle = hinge angle
C. Wedge angle = 180° − hinge angle
D. Wedge angle = hinge angle / 2
Answer: A
Objective: IV.2
Why: Each wedge tilts its isodose by the wedge angle. Across the hinge the two tilts should cancel, which gives wedge = 90° − hinge/2, or hinge = 180° − 2 × wedge. Correct choice: Wedge angle = 90° − (hinge angle)/2. They are equal only in the special case of a 60° wedge and a 60° hinge, not in general. That drops the factor of one-half on the hinge. Half the hinge is the amount you subtract from 90°, not the wedge angle itself.

### Q2
Stem: A pair of 30° wedges. Two beams use a wedge angle of 30° each. Using hinge angle = 180° − 2 × wedge angle, what hinge angle makes the combined isodose as flat as this simple model predicts?
A. 75.0°
B. 150°
C. 120°
D. 60.0°
Answer: C
Objective: IV.2
Why: The planning relation used here is hinge = 180° − 2 × wedge angle, because each wedge tilts the isodose by the wedge angle and the two tilts should cancel across the hinge. Substitute 180 − 2 × 30 = 180 − 60 = 120°. Mixing this up with wedge = 90 − hinge/2 and then halving the wedge angle gives 75.0°. Subtracting the wedge angle only once (180−30) gives 150°. Subtracting the wedge angle from 90° and calling that the hinge gives 60.0°.

### Q3
Stem: A pair of 45° wedges. Two beams use a wedge angle of 45° each. Using hinge angle = 180° − 2 × wedge angle, what hinge angle makes the combined isodose as flat as this simple model predicts?
A. 67.5°
B. 135°
C. 90°
D. 45.0°
Answer: C
Objective: IV.2
Why: The planning relation used here is hinge = 180° − 2 × wedge angle, because each wedge tilts the isodose by the wedge angle and the two tilts should cancel across the hinge. Substitute 180 − 2 × 45 = 180 − 90 = 90°. Mixing this up with wedge = 90 − hinge/2 and then halving the wedge angle gives 67.5°. Subtracting the wedge angle only once (180−45) gives 135°. Subtracting the wedge angle from 90° and calling that the hinge gives 45.0°.

### Q4
Stem: An anterior oblique pair with a wide hinge. The hinge angle between two wedged beams is 120°. Using wedge angle = 90° − (hinge angle)/2, what wedge angle does this model call for?
A. 60.0°
B. 30.0°
C. 120.0°
D. 45.0°
Answer: B
Objective: IV.2
Why: Substitute 90 − (120)/2 = 90 − 60 = 30°, reported as 30.0°. Check the inverse relation: hinge = 180 − 2 × wedge = 180 − 2 × 30 = 120°. Subtracting the hinge from 180° runs the companion formula without the factor of 2. That mistake gives 60.0°. Reporting the hinge angle itself leaves the isodose-tilt conversion undone. That mistake gives 120.0°. Adding an extra 15° to the wedge angle is not part of the hinge relation. That mistake gives 45.0°.

### Q5
Stem: A planned hinge of 100°. The hinge angle between two wedged beams is 100°. Using wedge angle = 90° − (hinge angle)/2, what wedge angle does this model call for?
A. 80.0°
B. 100.0°
C. 40.0°
D. 50.0°
Answer: C
Objective: IV.2
Why: Substitute 90 − (100)/2 = 90 − 50 = 40°, reported as 40.0°. Check the inverse relation: hinge = 180 − 2 × wedge = 180 − 2 × 40 = 100°. Subtracting the hinge from 180° runs the companion formula without the factor of 2. That mistake gives 80.0°. Reporting the hinge angle itself leaves the isodose-tilt conversion undone. That mistake gives 100.0°. Stopping at half the hinge never subtracts that half-angle from 90°. That mistake gives 50.0°.

## MLCs

### Q1
Stem: What is the usual clinical consequence of MLC tongue-and-groove design?
A. A hot streak equal to twice the leaf transmission
B. Removal of all interleaf leakage
C. A cold streak where adjacent leaves do not share the same open segment
D. A change in wedge factor
Answer: C
Objective: IV.2
Why: The tongue on one leaf and the groove on the neighbor reduce leakage, but if one leaf shades a pixel that the adjacent segment thought was open, that pixel is underdosed. You see a cold streak. Correct choice: A cold streak where adjacent leaves do not share the same open segment. Tongue-and-groove is an underdose from interlocking edges, not a double transmission. The tongue reduces leakage. It does not make transmission zero, and the groove can cause a cold line. Tongue-and-groove is an MLC edge effect, not the wedge factor.

### Q2
Stem: Rounded MLC leaf ends mainly change which quantity?
A. Penumbra, which gets wider
B. They make transmission zero
C. They remove the need for an equivalent square
D. They double the output factor
Answer: A
Objective: IV.2
Why: A rounded leaf end presents a varying thickness across the edge, so the 50% edge and the penumbra are broader than a focused block edge. Planning systems offset the leaf positions (dosimetric leaf gap) so the light field and the dose edge agree. Correct choice: Penumbra, which gets wider. Rounded ends still transmit, and the transmission is handled with an offset (dosimetric leaf gap), not by assuming zero transmission. Field-size scatter is a separate lookup. Rounding changes the edge, not a global factor of 2.

### Q3
Stem: A point sits under closed MLC leaves. Leaf transmission is 1.5% and the open dose would have been 200 cGy. The open beam would deliver 200 cGy to the point. A partial-transmission block with transmission 0.015 covers that ray, and the MU are not increased. What dose gets through the block?
A. 197.0 cGy
B. 3.0 cGy
C. 13333.3 cGy
D. 200.0 cGy
Answer: B
Objective: IV.2
Why: Transmission is the fraction that passes. Dose = 200 × 0.015 = 3.00 cGy, reported as 3.0 cGy. Multiplying by (1−transmission) gives the removed dose 197.0 cGy, not the dose that remains. Dividing by transmission gives the MU adjustment 13333.3 cGy if you wanted the original dose through the block, which is not what these MU deliver. Ignoring the block leaves the dose at 200.0 cGy.

### Q4
Stem: Interleaf transmission is taken as 2.0% for this estimate, open dose 180 cGy, MU not increased. The open beam would deliver 180 cGy to the point. A partial-transmission block with transmission 0.02 covers that ray, and the MU are not increased. What dose gets through the block?
A. 176.4 cGy
B. 9000.0 cGy
C. 180.0 cGy
D. 3.6 cGy
Answer: D
Objective: IV.2
Why: Transmission is the fraction that passes. Dose = 180 × 0.02 = 3.60 cGy, reported as 3.6 cGy. Multiplying by (1−transmission) gives the removed dose 176.4 cGy, not the dose that remains. Dividing by transmission gives the MU adjustment 9000.0 cGy if you wanted the original dose through the block, which is not what these MU deliver. Ignoring the block leaves the dose at 180.0 cGy.

### Q5
Stem: Why is MLC transmission dose not the same thing as a Clarkson scatter correction?
A. They are two names for the wedge factor
B. Clarkson already includes leaf transmission
C. Transmission is primary leakage through the leaves; Clarkson is phantom scatter from the open field
D. Transmission replaces Sp
Answer: C
Objective: IV.2
Why: Under a closed leaf the patient still receives a small primary leakage dose, typically around 1–2% for a modern MLC, plus some scatter from the open part of the field. Clarkson computes that scatter geometry. It does not replace the transmission measurement. Correct choice: Transmission is primary leakage through the leaves; Clarkson is phantom scatter from the open field. Neither one is the wedge factor. Classic Clarkson sectors are open-phantom scatter, not MLC leakage. Sp is phantom scatter for the irradiated area. Leakage is an extra primary component under the leaves.

## Beam Modifying Devices Quiz

### Q1
Stem: Quiz. Open-beam MU were delivered with a 0.62 wedge actually in the path. The monitor units were calculated for an open beam to deliver 200 cGy at the calculation point. A wedge with wedge factor 0.62 was actually left in the beam. What dose is delivered at that point?
A. 200.0 cGy
B. 322.6 cGy
C. 76.0 cGy
D. 124.0 cGy
Answer: D
Objective: IV.2
Why: The open-beam MU already assume wedge factor 1. With the wedge in the beam every MU is attenuated by the wedge factor, so delivered dose = intended dose × wedge factor. Substitute 200 × 0.62 = 124.00 cGy, reported as 124.0 cGy. The plan underdoses; it does not overdose. Leaving the dose at 200.0 cGy is the open-beam number and ignores the wedge that was in the beam. Dividing by the wedge factor (200/0.62 = 322.6 cGy) is what you do to the MU to restore dose, not what the patient received from the uncorrected MU. Multiplying by (1−wedge factor) treats the factor as if only the attenuated fraction remained in a subtraction sense and gives 76.0 cGy.

### Q2
Stem: Quiz. Compute the MU that restores dose for wedge factor 0.64. Open-beam monitor units for this field are 280 MU. The wedge factor is 0.64. What MU should be set so the calculation point still receives the open-beam dose, with the wedge in the beam?
A. 179.2 MU
B. 280.0 MU
C. 777.8 MU
D. 437.5 MU
Answer: D
Objective: IV.2
Why: The wedge lowers dose per MU, so the MU must increase by 1/wedge factor. Substitute 280 / 0.64 = 437.50 MU, reported as 437.5 MU. Multiplying the open MU by the wedge factor (280×0.64 = 179.2 MU) would underdose a second time. Keeping 280.0 MU omits the wedge factor while the wedge is used. Dividing by (1−wedge factor) uses the complement of the factor and gives 777.8 MU.

### Q3
Stem: Quiz. Find the wedge factor from the two chamber readings. Under the same MU and geometry, the chamber reads 95 with the wedge removed and 66.5 with the wedge in place. What is the wedge factor (dose with wedge divided by dose without wedge)?
A. 0.700
B. 1.429
C. 0.300
D. 0.850
Answer: A
Objective: IV.2
Why: Wedge factor = reading with wedge / reading without wedge. Substitute 66.5 / 95 = 0.7000, reported as 0.700. Inverting the ratio (open/wedged) gives 1.429, which is greater than 1 and cannot be a physical wedge factor for a metal wedge that only attenuates. Using the fractional difference (open−wedged)/open gives 0.300, which is the attenuated fraction, not the transmitted factor. Averaging the open and wedged readings and then dividing by the open reading gives 0.850, which is not the transmission.

### Q4
Stem: Quiz. Hinge for 20° wedges. Two beams use a wedge angle of 20° each. Using hinge angle = 180° − 2 × wedge angle, what hinge angle makes the combined isodose as flat as this simple model predicts?
A. 80.0°
B. 160°
C. 70.0°
D. 140°
Answer: D
Objective: IV.2
Why: The planning relation used here is hinge = 180° − 2 × wedge angle, because each wedge tilts the isodose by the wedge angle and the two tilts should cancel across the hinge. Substitute 180 − 2 × 20 = 180 − 40 = 140°. Mixing this up with wedge = 90 − hinge/2 and then halving the wedge angle gives 80.0°. Subtracting the wedge angle only once (180−20) gives 160°. Subtracting the wedge angle from 90° and calling that the hinge gives 70.0°.

### Q5
Stem: Quiz. Bolus on a 6 MV tangent. A 6 MV beam has dmax at 1.5 cm in water with no bolus. Water-equivalent bolus of 0.5 cm is added on the skin. Assume the buildup curve shifts toward the surface by the bolus thickness. Where is dmax relative to the skin?
A. 2.0 cm below the skin
B. 1.0 cm below the skin
C. 1.5 cm below the skin
D. 0.5 cm below the skin
Answer: B
Objective: IV.2
Why: Bolus fills in buildup, so the dose maximum moves to a shallower depth in the patient. Depth below skin = 1.5 − 0.5 = 1.00 cm, reported as 1.0 cm below the skin. Bolus also raises skin dose. It does not push dmax deeper. Adding the bolus thickness to dmax gives 2.0 cm below the skin and moves the peak the wrong way. Leaving dmax at 1.5 cm below the skin ignores the shift. Reporting only the bolus thickness gives 0.5 cm below the skin.

### Q6
Stem: Quiz. A full centimeter of bolus on a 10 MV beam. A 10 MV beam has dmax at 2.5 cm in water with no bolus. Water-equivalent bolus of 1 cm is added on the skin. Assume the buildup curve shifts toward the surface by the bolus thickness. Where is dmax relative to the skin?
A. 3.5 cm below the skin
B. 2.5 cm below the skin
C. 1.0 cm below the skin
D. 1.5 cm below the skin
Answer: D
Objective: IV.2
Why: Bolus fills in buildup, so the dose maximum moves to a shallower depth in the patient. Depth below skin = 2.5 − 1 = 1.50 cm, reported as 1.5 cm below the skin. Bolus also raises skin dose. It does not push dmax deeper. Adding the bolus thickness to dmax gives 3.5 cm below the skin and moves the peak the wrong way. Leaving dmax at 2.5 cm below the skin ignores the shift. Reporting only the bolus thickness gives 1.0 cm below the skin.

### Q7
Stem: Quiz. Brass compensator for a 4 cm missing-tissue gap. Missing tissue is 4 cm of relative density 1. Compensator relative density is 1.8. The compensator sits at SCD 40 cm and the skin is at SSD 100 cm. Use t = t_miss × (ρ_tissue/ρ_comp) × (SCD/SSD)^2. What compensator thickness is required along this ray?
A. 0.36 cm
B. 2.22 cm
C. 0.64 cm
D. 1.15 cm
Answer: A
Objective: IV.2
Why: Density ratio = 1/1.8 = 0.5556. Distance scale = (40/100)^2 = 0.4000^2 = 0.1600. The compensator is closer to the source than the skin, so a thinner piece removes the diverging fluence that would have crossed the missing tissue; the (SCD/SSD)^2 term is that geometric thinning. t = 4 × 0.5556 × 0.1600 = 0.3556 cm, reported as 0.36 cm. Omitting the distance scale gives 2.22 cm, the thickness you would need if the compensator were at the skin. Omitting the density ratio gives 0.64 cm. Inverting the density ratio gives 1.15 cm.

### Q8
Stem: Quiz. A 40% transmission block is left in and the MU are the open-beam MU. The open beam would deliver 220 cGy to the point. A partial-transmission block with transmission 0.4 covers that ray, and the MU are not increased. What dose gets through the block?
A. 88.0 cGy
B. 132.0 cGy
C. 550.0 cGy
D. 220.0 cGy
Answer: A
Objective: IV.2
Why: Transmission is the fraction that passes. Dose = 220 × 0.4 = 88.00 cGy, reported as 88.0 cGy. Multiplying by (1−transmission) gives the removed dose 132.0 cGy, not the dose that remains. Dividing by transmission gives the MU adjustment 550.0 cGy if you wanted the original dose through the block, which is not what these MU deliver. Ignoring the block leaves the dose at 220.0 cGy.
