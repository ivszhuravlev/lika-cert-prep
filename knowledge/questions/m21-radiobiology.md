# Module 21 — Radiobiology

Original practice items for CMD preparation. Not retired MDCB items and not a commercial quiz.

BED = n × d × (1 + d / (α/β)), where n is the number of fractions and d is the dose per fraction.
EQD2 = BED / (1 + 2 / (α/β)).
When the dose per fraction is already 2 Gy, EQD2 equals the total physical dose.

## Cell Survival Curve

### Q1
Stem: A cell-survival curve is plotted as the log of surviving fraction against dose. The linear-quadratic model is S = exp(−αD − βD²). At a low dose per fraction, which term dominates cell kill, and which term grows faster as the dose per fraction rises?
A. The βD² term dominates at low dose; the αD term grows faster as dose rises
B. The linear αD term dominates at low dose; the quadratic βD² term contributes a larger share as the dose per fraction rises
C. Both terms are independent of dose
D. The curve is a straight line through the origin on a linear plot for low-LET radiation, with no shoulder
Answer: B
Objective: III.3
Why: Answer B. The ratio of the quadratic contribution to the linear contribution inside the exponent is (βD²)/(αD) = D/(α/β). When D is much smaller than α/β, the linear term dominates. When D is large, the square term dominates. That is why raising the dose per fraction hurts tissues with a small α/β (late tissues, and prostate) more than tissues with a large α/β. Low-LET photon curves have a shoulder on a semi-log plot. A straight line through the origin, with little shoulder, is the high-LET shape.

### Q2
Stem: On the exponential tail of a multi-target survival curve, D0 is 1.5 Gy. Survival at one point on that tail is 10%. What dose increment, along the same tail, reduces survival from 10% to 3.7%?
A. 0.37 Gy
B. 1.5 Gy
C. 3.0 Gy
D. 15 Gy
Answer: B
Objective: III.3
Why: Answer B. D0, the mean lethal dose, is the dose that reduces survival to 37% of its previous value on the straight portion of a semi-log survival curve. The ratio 3.7/10 = 0.37, so the step from 10% to 3.7% is exactly one D0. The increment is 1.5 Gy, not 0.37 Gy and not a new total dose of 15 Gy. D0 is not the quasithreshold dose Dq, which describes the width of the shoulder rather than the slope of the tail.

### Q3
Stem: Two photon survival curves are drawn for the same cells. Curve A has a wide shoulder. Curve B becomes much steeper and loses the shoulder when the same cells are irradiated with neutrons. What changed?
A. Neutrons lowered the LET, so more sublethal damage can be repaired and the shoulder widens
B. Neutrons raised the LET; more of the damage is irreparable single-track injury, the α term effectively increases, and repair between fractions matters less
C. The neutron curve is shallower because RBE is less than 1
D. A shoulder appears only for high-LET radiation
Answer: B
Objective: III.3
Why: Answer B. Neutrons (and the distal end of a heavy-ion track) have a high linear energy transfer. Dense ionization produces damage that a cell repairs poorly, which straightens the survival curve and increases RBE above 1. Fractionation, which exists to let normal cells repair sublethal damage between photon fractions, buys less protection when the shoulder is already gone. Low-LET photons are the curves with the shoulder. RBE greater than 1 means less dose is required for the same effect, so the neutron curve is steeper, not shallower.

### Q4
Stem: The oxygen enhancement ratio is the dose in hypoxia divided by the dose in air that produces the same cell kill. For photons it is about 2.5 to 3. For high-LET radiation it moves closer to 1. What does a ratio of 3 mean in the clinic?
A. Hypoxic cells are more sensitive than oxygenated cells
B. About three times as much photon dose is required under hypoxia as under oxygen for the same kill; oxygen "fixes" indirect free-radical damage
C. Oxygen protects cells by scavenging every direct ionization
D. The ratio is 3 for neutrons and 1 for photons
Answer: B
Objective: III.3
Why: Answer B. Most photon damage is indirect, through free radicals. Oxygen makes that chemical damage permanent, so well-oxygenated cells die at a lower dose. If the oxygen enhancement ratio is 3, the hypoxic dose for the same survival is three times the oxic dose. Tumors with hypoxic regions are relatively resistant to a single photon fraction, which is one reason fractionation helps: reoxygenation between fractions brings those cells back to a sensitive state. High-LET damage is more often direct, so oxygen matters less and the ratio falls toward 1. The ratio is not higher for neutrons than for photons.

### Q5
Stem: α/β is 10 Gy for an early-responding tissue and 3 Gy for a late-responding tissue. At which dose per fraction are the linear and quadratic contributions equal for the late tissue, and what does the smaller α/β imply?
A. Equal at 10 Gy; the late tissue is less sensitive to fraction size than the early tissue
B. Equal at 3 Gy; the late tissue's survival curve bends more, so large fractions increase late injury relative to early injury
C. Equal at 2 Gy for every tissue, because EQD2 uses 2 Gy
D. Equal at 0 Gy, because α and β are doses
Answer: B
Objective: III.3
Why: Answer B. By definition, αD equals βD² when D equals α/β. For the late tissue that dose is 3 Gy. Below 3 Gy the linear term dominates; above 3 Gy the quadratic term dominates. A smaller α/β means the quadratic term takes over sooner, so the tissue is more punished by a large dose per fraction. That is the biological reason conventional fractionation (about 2 Gy) spares late normal tissue relative to a tumor with α/β near 10, and why hypofractionation needs a small volume and a steep gradient. EQD2 is a conversion, not the definition of α/β.

## Cell Cycle

### Q1
Stem: Cells in which phase of the cycle are the most radiosensitive, and cells in which phase are the most resistant?
A. Most sensitive in late S; most resistant in mitosis
B. Most sensitive in mitosis and late G2; most resistant in late S
C. Sensitivity is identical in G1, S, G2, and M for photons
D. Most sensitive in G0; most resistant in M
Answer: B
Objective: III.3
Why: Answer B. Mitosis, and the late G2 period just before it, is the most sensitive part of the cycle. Late S, when DNA has been replicated and repair is effective, is the most resistant. G0 cells are not uniformly the most sensitive; quiescent cells can repair potentially lethal damage. A survival curve measured on an asynchronous population is an average over these phases, which is one reason a single fraction does not sterilize every cell that the average curve appears to kill.

### Q2
Stem: After a photon fraction, the surviving cells are enriched in late S. Over the next several hours many of them progress into G2 and M. What is the name of this "R," and how can it increase kill from the next fraction?
A. Repopulation; the resistant survivors divide and the next fraction is less effective
B. Redistribution (reassortment); survivors move out of the resistant phase into a sensitive phase before the next fraction
C. Reoxygenation; S-phase cells lose oxygen as they enter mitosis
D. Repair; progression into G2 restores the original shoulder within minutes
Answer: B
Objective: III.3
Why: Answer B. Redistribution is one of the four Rs (repair, redistribution, repopulation, reoxygenation). A dose selectively kills the sensitive phases, so the survivors are biased toward late S. As those cells continue around the cycle they re-enter G2 and M and become sensitive again. A later fraction then kills cells that would have been resistant immediately after the first dose. That is not repopulation, which adds new cells and works against control, and it is not repair, which decreases the effect of a second fraction given too soon.

### Q3
Stem: A head-and-neck course is prolonged by 7 unplanned days. The stem of the protocol states that, past the lag period, tumor control is lost at about 0.6 Gy per extra day. How much extra dose does that factor assign to the break, and which R is this?
A. 7 × 0.6 = 4.2 Gy; repopulation
B. 7 × 0.6 = 4.2 Gy; repair of sublethal damage, which requires a longer gap to be less complete
C. 0.6 / 7 = 0.09 Gy; reoxygenation
D. No extra dose; overall time does not matter for a tumor with a high α/β
Answer: A
Objective: III.3
Why: Answer A. Accelerated repopulation in head-and-neck squamous cell carcinoma is why overall time is part of the prescription. Using the factor the stem supplied, 7 × 0.6 = 4.2 Gy of dose-equivalent is lost to new tumor cells during the break. Making the gap longer would only help if the problem were incomplete repair between two fractions on the same day. Here the days are added to the course, so more time means more repopulation, not more repair. A high α/β does not turn off proliferation.

### Q4
Stem: Sublethal damage repair after a photon fraction is largely complete by about 6 hours. A twice-daily schedule leaves a 3 hour gap. What is the effect on normal tissue relative to a 6 hour gap?
A. The shorter gap allows more repair, so late effects fall
B. Repair is incomplete, so the second fraction adds to residual injury and the biologically effective dose is higher than the complete-repair formula predicts
C. The gap affects tumors only; normal-tissue repair is instant
D. A 3 hour gap converts low-LET radiation into high-LET radiation
Answer: B
Objective: III.3
Why: Answer B. The linear-quadratic BED formula used in the BED section assumes full repair between fractions. That assumption is reasonable at about 6 hours and is not reasonable at 3 hours. Residual sublethal damage makes the pair behave like a larger single dose, which is particularly costly for late-responding normal tissue. Twice-daily head-and-neck and total-body schedules therefore specify a minimum interfraction interval of about 6 hours. The gap does not change the LET of the beam.

### Q5
Stem: Which list correctly matches the four Rs to the problem each one addresses in fractionated radiotherapy?
A. Repair: tumor growth during a long course. Repopulation: hypoxic cells regaining oxygen. Reoxygenation: sublethal damage. Redistribution: movement into a sensitive phase
B. Repair: sublethal damage between fractions. Redistribution: movement from resistant to sensitive phases. Repopulation: new cell division, especially in a prolonged course. Reoxygenation: hypoxic survivors becoming oxygenated
C. All four Rs describe repair; the other names are synonyms
D. Reoxygenation is the reason a single fraction is always better than 30 fractions
Answer: B
Objective: III.3
Why: Answer B. Repair of sublethal injury in late normal tissues is the benefit of splitting a dose into fractions. Redistribution moves tumor cells that survived in a resistant phase into a sensitive one. Repopulation is usually a cost, because tumor cells (and early-reacting mucosa) divide during a long course. Reoxygenation restores sensitivity to cells that were hypoxic during the previous fraction. A single fraction gives up repair, redistribution, and reoxygenation together. A fifth R sometimes added to the list is intrinsic radiosensitivity, which fractionation does not remove.

## BEDs

### Q1
Stem: A course delivers 30 Gy in 10 fractions of 3 Gy. For a tumor with α/β = 10 Gy, what are the BED and the EQD2?
A. BED 39 Gy10 and EQD2 32.5 Gy
B. BED 60 Gy10 and EQD2 36 Gy
C. BED 30 Gy10 and EQD2 30 Gy
D. BED 32.5 Gy10 and EQD2 39 Gy
Answer: A
Objective: III.3
Why: Answer A. BED = total dose × (1 + d/(α/β)) = 30 × (1 + 3/10) = 30 × 1.3 = 39 Gy10. EQD2 divides that BED by the relative effectiveness of 2 Gy fractions: 1 + 2/10 = 1.2. EQD2 = 39 / 1.2 = 32.5 Gy. The same physical schedule with α/β = 3 Gy would give BED = 30 × (1 + 3/3) = 30 × 2 = 60 Gy3 and EQD2 = 60 / (1 + 2/3) = 60 / (5/3) = 36 Gy. That pair is answer B, but it is the late-tissue result, not the α/β = 10 result the question asked for. Swapping BED and EQD2 produces answer D.

### Q2
Stem: The same 30 Gy in 10 fractions of 3 Gy is scored for a late-responding tissue with α/β = 3 Gy. What is the BED?
A. 39 Gy3
B. 36 Gy3
C. 60 Gy3
D. 90 Gy3
Answer: C
Objective: III.3
Why: Answer C. BED = 30 × (1 + 3/3) = 30 × (1 + 1) = 30 × 2 = 60 Gy3. The relative effectiveness is 2, twice the physical dose, because the dose per fraction equals α/β. The EQD2 is not the BED: EQD2 = 60 / (5/3) = 36 Gy, which is the trap in B. Thirty-nine Gy3 is the BED of this schedule at α/β = 10, not at α/β = 3. Ninety would be 30 × (1 + 3/1), which invents an α/β of 1 Gy.

### Q3
Stem: Sixteen fractions of 3 Gy deliver 48 Gy. For α/β = 10 Gy, what is the BED?
A. 48 Gy10
B. 52 Gy10
C. 62.4 Gy10
D. 72 Gy10
Answer: C
Objective: III.3
Why: Answer C. BED = 48 × (1 + 3/10) = 48 × 1.3. Forty-eight times 1 is 48, and 48 × 0.3 = 14.4, so BED = 62.4 Gy10. The EQD2 is 62.4 / 1.2 = 52 Gy, which is answer B and is not the BED. The physical dose, 48 Gy, is not a BED unless the fraction size is vanishingly small. Seventy-two Gy10 would be the BED of 60 Gy in 2 Gy fractions (60 × 1.2), a different schedule.

### Q4
Stem: Compare 78 Gy in 39 fractions of 2 Gy with 60 Gy in 20 fractions of 3 Gy, for a late tissue with α/β = 3 Gy. What is the EQD2 of the 60 Gy course, and how does it compare with 78 Gy?
A. EQD2 is 72 Gy, which is lower than 78 Gy
B. EQD2 is 77.1 Gy, which is higher than 78 Gy
C. EQD2 is 60 Gy, because hypofractionation does not change EQD2
D. EQD2 is 120 Gy, the BED rather than the EQD2
Answer: A
Objective: III.3
Why: Answer A. For any schedule already given at 2 Gy per fraction, EQD2 equals the physical dose, so 78 Gy in 39 fractions has EQD2 = 78 Gy. For 60 Gy in 20 fractions, BED = 60 × (1 + 3/3) = 60 × 2 = 120 Gy3. EQD2 = 120 / (1 + 2/3) = 120 / (5/3) = 120 × 3/5 = 72 Gy. Seventy-two is lower than 78, so at α/β = 3 the conventional course is the hotter late-tissue regimen. The often-quoted prostate comparison uses α/β near 1.5 Gy, where 60 Gy in 20 fractions has BED = 60 × (1 + 3/1.5) = 60 × 3 = 180 Gy and EQD2 = 180 / (1 + 2/1.5) = 180 / (7/3) = 180 × 3/7 ≈ 77.1 Gy, almost equal to 78. That 77.1 Gy figure is the wrong α/β for this question. One hundred twenty is the BED, not the EQD2.

### Q5
Stem: An organ previously received 50.4 Gy in 28 fractions of 1.8 Gy. A new plan would add 24 Gy in 12 fractions of 2 Gy. Using α/β = 3 Gy and assuming full repair and no time discount, what is the cumulative EQD2?
A. 74.4 Gy, the sum of the physical doses
B. 48.4 Gy, the first course only
C. 72.4 Gy
D. 80.6 Gy, the BED of the first course
Answer: C
Objective: III.3
Why: Answer C. First course: BED = 50.4 × (1 + 1.8/3) = 50.4 × (1 + 0.6) = 50.4 × 1.6. Fifty times 1.6 is 80, and 0.4 × 1.6 is 0.64, so BED = 80.64 Gy3. EQD2 = 80.64 / (5/3) = 80.64 × 3/5. Eighty point six four times 0.6 is 48.384 Gy. Second course: the fraction size is 2 Gy, so EQD2 = 24 Gy. Cumulative EQD2 = 48.384 + 24 = 72.384 Gy, which is 72.4 Gy. Adding the physical doses, 50.4 + 24 = 74.4 Gy, ignores that 1.8 Gy fractions are slightly gentler, at α/β = 3, than 2 Gy fractions. Eighty point six four is the first-course BED, not an EQD2.

### Q6
Stem: A single 8 Gy fraction is given for a painful metastasis. For a late tissue with α/β = 3 Gy, what is the BED?
A. 8 Gy3
B. 14.4 Gy3
C. 17.6 Gy3
D. 29.3 Gy3
Answer: D
Objective: III.3
Why: Answer D. BED = 8 × (1 + 8/3) = 8 × (1 + 2.667) = 8 × (11/3) = 88/3 = 29.333 Gy3, about 29.3 Gy3. The same single fraction at α/β = 10 Gy would be 8 × (1 + 8/10) = 8 × 1.8 = 14.4 Gy10, which is answer B and is the tumor BED, not the late BED. The late EQD2 is 29.333 / (5/3) = 29.333 × 0.6 = 17.6 Gy, answer C. The physical dose, 8 Gy, is neither the BED nor the EQD2. The quadratic term is large because the entire dose arrives in one fraction: 8/3 is much greater than 2/3.

### Q7
Stem: A cord point receives 2.5 Gy per fraction for 20 fractions, a physical dose of 50 Gy. The limit is an EQD2 of 50 Gy at α/β = 2 Gy. Does this point satisfy the limit, and what is its EQD2?
A. Yes; the physical dose is 50 Gy, so the EQD2 is 50 Gy
B. No; EQD2 is 56.25 Gy, which exceeds 50 Gy
C. No; EQD2 is 112.5 Gy
D. Yes; EQD2 is 45 Gy because 2.5 Gy fractions are gentler than 2 Gy fractions at α/β = 2
Answer: B
Objective: III.3
Why: Answer B. BED = 50 × (1 + 2.5/2) = 50 × (1 + 1.25) = 50 × 2.25 = 112.5 Gy2. For α/β = 2 Gy, the EQD2 divisor is 1 + 2/2 = 2. EQD2 = 112.5 / 2 = 56.25 Gy. That exceeds a 50 Gy EQD2 limit even though the physical dose is exactly 50 Gy, because 2.5 Gy fractions are harsher than 2 Gy fractions when α/β is 2. Answer C stops at the BED. Answer D has the fraction-size effect backward: a dose per fraction above 2 Gy raises, rather than lowers, the EQD2 relative to the physical dose for any finite α/β.

### Q8
Stem: How many fractions of 5 Gy produce a tumor BED of 90 Gy when α/β = 10 Gy, and what physical dose is that?
A. 10 fractions, 50 Gy
B. 12 fractions, 60 Gy
C. 15 fractions, 75 Gy
D. 18 fractions, 90 Gy
Answer: B
Objective: III.3
Why: Answer B. One 5 Gy fraction has relative effectiveness 1 + 5/10 = 1.5, so its BED is 5 × 1.5 = 7.5 Gy10. The number of fractions is 90 / 7.5 = 12. The physical dose is 12 × 5 = 60 Gy. Check: 60 × 1.5 = 90 Gy10. Ten fractions would be 75 Gy10, not 90. Eighteen fractions of 5 Gy would be a physical dose of 90 Gy and a BED of 135 Gy10, which confuses the physical dose with the BED. Fifteen fractions give 75 × 1.5 = 112.5 Gy10.

### Q9
Stem: A head-and-neck BED calculated without a time correction is 84 Gy10 for 70 Gy in 35 fractions at α/β = 10 Gy. The protocol then subtracts 0.6 Gy10 per day for 5 extra days of repopulation. What is the corrected BED?
A. 84 Gy10, because repopulation is already inside α/β
B. 87 Gy10
C. 81 Gy10
D. 84 − 5 × 2 = 74 Gy10, using the dose per fraction instead of 0.6
Answer: C
Objective: III.3
Why: Answer C. Confirm the uncorrected BED: 70 × (1 + 2/10) = 70 × 1.2 = 84 Gy10. The time term is given as 0.6 Gy10 per extra day, so 5 × 0.6 = 3.0 Gy10 is subtracted. Corrected BED = 84 − 3 = 81 Gy10. Adding the time term would mean the break increased cell kill, which is the wrong direction for repopulation. Replacing 0.6 with the 2 Gy fraction size invents a correction the protocol did not state. This subtraction is only as good as the 0.6 Gy10 per day the protocol supplied; it is not a universal constant to invent on a different disease.

## Radiobiology Quiz

### Q1
Stem: A protocol offers hyperfractionation: 1.15 Gy twice daily, with at least 6 hours between fractions, to a higher total dose than 2 Gy daily. Which normal-tissue goal is this designed to achieve?
A. Increase late effects on purpose, because late tissues have a high α/β
B. Spare late-responding tissue, which has a low α/β, by using a smaller dose per fraction, while the higher total dose still controls a tumor with a higher α/β
C. Finish the course in fewer calendar days than conventional fractionation, which is the definition of hyperfractionation
D. Remove the need for a gap between the two daily fractions
Answer: B
Objective: III.3
Why: Answer B. Hyperfractionation uses a dose per fraction below 2 Gy so the quadratic term in a low-α/β late tissue stays small. The total dose is raised to keep tumor control, on the argument that a tumor with α/β near 10 loses less from the smaller fraction than the late tissue gains. The interval has to be long enough for repair, about 6 hours. Shortening the calendar time is accelerated fractionation, a different modification, and it tends to increase acute mucositis. The two ideas are sometimes combined, but a smaller fraction size is the hyperfractionation part.

### Q2
Stem: Hypofractionation gives a larger dose per fraction in fewer fractions. For a prostate cancer with α/β near 1.5 Gy sitting inside late rectal tissue that also has a low α/β, why can a shorter course still be rational?
A. Because any increase in fraction size spares the rectum more than the tumor when both have a low α/β
B. Because the tumor's low α/β means it is not spared by 2 Gy fractions the way a high-α/β tumor would be, so fewer larger fractions can match tumor BED, provided the rectal volume in the high dose is small
C. Because α/β near 1.5 Gy means fractionation does not change BED at all
D. Because hypofractionation lowers the BED of a 3 Gy fraction below the BED of a 2 Gy fraction for the same total dose
Answer: B
Objective: III.3
Why: Answer B. Classical fractionation assumes the tumor α/β is higher than the late-normal α/β. Prostate cancer is unusual: its α/β is estimated near 1.5 to 3 Gy, similar to late rectum. Two gray fractions then do not preferentially spare the tumor's BED. A moderately hypofractionated course can keep a similar tumor EQD2 with a lower total physical dose, which is the 60 Gy in 20 fractions versus 78 Gy in 39 fractions comparison. The rectum still has a low α/β, so the high dose per fraction is only tolerable if the volume of rectum at that dose is limited by conformal planning. For the same total physical dose, a larger fraction size raises BED; it does not lower it.

### Q3
Stem: The therapeutic ratio is tumor control probability divided by the normal-tissue complication probability, in conceptual terms. Fractionation at about 2 Gy improves that ratio, relative to a single large fraction, under which condition?
A. When the tumor α/β is higher than the late-normal α/β, so late injury falls more than tumor kill does as the fraction size is reduced
B. When the tumor α/β is lower than the late-normal α/β
C. Only when the beam is changed from photons to neutrons
D. Fractionation never changes the therapeutic ratio, only the total dose does
Answer: A
Objective: III.3
Why: Answer A. Reducing the dose per fraction removes more of the quadratic kill in the tissue with the smaller α/β. If that tissue is the late normal tissue and the tumor has a larger α/β, the normal tissue is spared more than the tumor, and the total dose can be raised until tumor control is acceptable. That improvement is the therapeutic ratio argument for conventional fractionation. It weakens or reverses if the tumor α/β is as low as the normal tissue's. Neutrons, with less repair, reduce the benefit of fractionation rather than create it.

### Q4
Stem: A neutron dose of 2 Gy has an RBE of 3 for a stated late effect relative to photons. What photon dose produces about the same biological effect, and why is a photon BED formula not applied to the raw 2 Gy?
A. 2/3 Gy; the neutron dose is already a photon dose
B. About 6 Gy of photons; the physical neutron dose must be scaled by RBE before it is compared with a photon tolerance
C. 2 Gy of photons, because RBE cancels in the BED formula
D. 5 Gy of photons, because RBE is added to the dose
Answer: B
Objective: III.3
Why: Answer B. RBE is the ratio of a reference photon dose to the test-radiation dose for the same effect. If the RBE is 3, 2 Gy of neutrons corresponds to about 2 × 3 = 6 Gy of photons for that endpoint. Putting the unscaled 2 Gy into a photon BED formula treats the neutron fraction as if it were a 2 Gy photon fraction and understates the injury. Proton prescriptions avoid this mistake by stating Gy (RBE) with RBE = 1.1. Adding RBE to the dose (2 + 3 = 5) is not the definition.

### Q5
Stem: The law of Bergonié and Tribondeau relates radiosensitivity to proliferation and differentiation. Which statement agrees with that law, and which cell is the classic exception?
A. Slowly dividing, highly differentiated cells are the most sensitive; lymphocytes are the most resistant cells in the body
B. Rapidly dividing, poorly differentiated cells are more sensitive; mature lymphocytes are a major exception because they die readily by apoptosis despite being differentiated
C. Radiosensitivity depends only on oxygen and not on mitotic rate
D. The law says postmitotic cells such as muscle and nerve are more sensitive than intestinal crypt cells
Answer: B
Objective: III.3
Why: Answer B. The historical law says cells are more radiosensitive when they are undifferentiated, when they have a long mitotic future, and when they are actively dividing. That fits intestinal crypts, basal skin, and many tumors, and it fits the resistance of muscle and nerve. Lymphocytes break the rule: they are highly differentiated and still extremely sensitive, through apoptosis. The law is a tendency, not a substitute for a measured α/β or a tolerance dose.

### Q6
Stem: Potentially lethal damage repair is most associated with which condition after irradiation?
A. Cells that are allowed to remain in a quiescent state before being forced to divide, so some injuries that would have been lethal are repaired
B. A second fraction delivered 3 hours later, which is sublethal damage repair only
C. Immediate plating of cells so they must attempt mitosis at once, which maximizes this repair
D. High-LET irradiation, where this repair is largest
Answer: A
Objective: III.3
Why: Answer A. Potentially lethal damage is injury that becomes lethal if the cell tries to divide at once, and that can be repaired if division is delayed, as in a quiescent or density-inhibited population. Sublethal damage repair is the rejoining of injuries between two split doses and is the process that creates the fractionation benefit and the shoulder. Forcing immediate mitosis does not give time for potentially lethal damage repair. High-LET damage is less available for either kind of repair.

### Q7
Stem: A tumor contains a hypoxic fraction. It is treated with 30 photon fractions rather than one fraction of the same total dose. Besides repair of normal tissues, which tumor-specific R is the reason the later fractions can kill cells the first fraction spared?
A. Repopulation of hypoxic cells, which makes them more numerous and more sensitive
B. Reoxygenation of cells that were hypoxic during the first fraction
C. Redistribution is impossible in a hypoxic tumor
D. Converting the photons to a higher LET by fractionation
Answer: B
Objective: III.3
Why: Answer B. Cells that are hypoxic at the moment of a fraction are relatively resistant (oxygen enhancement ratio about 2.5 to 3 for photons). After the well-oxygenated cells die, oxygen reaches some of the survivors before the next fraction. That is reoxygenation, and a single-fraction treatment never gets it. Repopulation increases the number of clonogens and works against control. Fractionation does not change the LET of the photon beam. Redistribution can still occur; it is a separate R, not the oxygen one.

### Q8
Stem: Two schedules deliver the same physical dose of 50 Gy. Schedule A uses 2 Gy fractions. Schedule B uses 5 Gy fractions. For α/β = 3 Gy, which schedule has the higher BED, and by how much?
A. They have the same BED because the physical dose is the same
B. Schedule B is higher: BED 133.3 Gy3 versus 83.3 Gy3
C. Schedule A is higher: BED 100 Gy3 versus 50 Gy3
D. Schedule B is higher by the ratio of the fraction sizes only, a factor of 2.5, so its BED is 2.5 × 50 = 125 Gy3
Answer: B
Objective: III.3
Why: Answer B. Schedule A: BED = 50 × (1 + 2/3) = 50 × 5/3 = 250/3 = 83.3 Gy3. Schedule B: BED = 50 × (1 + 5/3) = 50 × (8/3) = 400/3 = 133.3 Gy3. The same physical dose is more damaging to a low-α/β tissue when it is given in larger fractions. The EQD2 values are 83.3 / (5/3) = 50 Gy for schedule A, as required for 2 Gy fractions, and 133.3 / (5/3) = 80 Gy for schedule B. Multiplying 50 by 5/2 = 125 skips the proper relative-effectiveness term 1 + d/(α/β).

### Q9
Stem: A planner adds the DVH mean doses from two courses in gray and calls the sum a cumulative BED. The first course was 2 Gy per fraction and the second was 4 Gy per fraction, both to the same organ with α/β = 3 Gy. What is wrong with that sum?
A. Nothing; BED is the sum of physical mean doses
B. The 4 Gy course contributes more biological dose per gray than the 2 Gy course, so physical grays cannot be added; each course needs its own EQD2 before the totals are added
C. The 2 Gy course contributes more biological dose per gray, so it should be weighted double
D. BED addition is valid only when the second course uses a higher energy
Answer: B
Objective: III.3
Why: Answer B. Relative effectiveness is 1 + d/(α/β). For 2 Gy and α/β = 3, it is 1 + 2/3 = 5/3 ≈ 1.67. For 4 Gy it is 1 + 4/3 = 7/3 ≈ 2.33. Each gray of the second course is worth more biologically than each gray of the first. The correct accumulation, ignoring time and partial recovery, converts each course to EQD2 (or to BED in the same units) and then adds. Adding the mean doses treats a 4 Gy fraction as if it were a 2 Gy fraction. Energy does not enter the linear-quadratic formula.
