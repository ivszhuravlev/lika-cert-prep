# Module 12. Radiation Units (Activity, Exposure, Absorbed Dose, Dose Equivalent)

Original notes for MDCB objective I.10.

## Units

**MDCB:** I.10, VI.1

**What the exam expects**

You name the quantity, the SI unit, and the older unit, and you convert. You do not treat roentgen, rad, and rem as three words for one thing. You attach w_R only when the quantity is equivalent dose.

**Core facts**

Activity. Decays per time. SI unit becquerel, 1 Bq = 1 s^−1. Older unit curie, 1 Ci = 3.7×10^10 Bq. Shortcuts: 1 Ci = 37 GBq, 1 mCi = 37 MBq. Activity is not dose rate.

Exposure. Ionization produced in air by photons. SI unit coulomb per kilogram. Older unit roentgen, 1 R = 2.58×10^−4 C/kg. Exposure is defined for photons in air, practically up to a few MeV. It is not defined for protons in tissue, and it is not a dose.

Air kerma. Kinetic energy transferred to charged particles per unit mass of air. Unit gray. Under equilibrium, exposure and air kerma are convertible. The number to remember from that conversion is below: 1 R corresponds to about 0.876 rad (0.876 cGy) of absorbed dose in air.

Absorbed dose. Energy imparted per unit mass, any radiation, any medium. SI unit gray, 1 Gy = 1 J/kg. Older unit rad. 1 Gy = 100 rad = 100 cGy. 1 cGy = 1 rad. Prescriptions are written in cGy or Gy. They are not written in roentgen.

Kerma uses the gray as well. Kerma and dose share a unit and are still different quantities, as module 9 separates them. The centigray is a legitimate unit of kerma as well as of absorbed dose, and 1 cGy is 0.01 Gy, not 100 Gy.

Equivalent dose (and the older dose equivalent). Absorbed dose weighted for radiation type. SI unit sievert. Older unit rem. 1 Sv = 100 rem. 1 cSv = 1 rem.

H = w_R D

For photons and electrons w_R = 1, so the number in sievert equals the number in gray, and the number in rem equals the number in rad. For alphas w_R = 20, so 1 rad becomes 20 rem. Neutron w_R depends on energy (module 5). Proton w_R for protection is 2. Clinical proton RBE is 1.1 and is not this conversion.

Effective dose. Equivalent dose multiplied by a tissue weighting factor and summed over organs. Also in sievert. w_T and w_R are different tables. ICRP has published more than one w_T set. Use the table the stem names. Do not invent tissue weights.

Air-kerma strength, used later for brachytherapy, has unit μGy·m²/h, also called U. 1 U = 1 cGy·cm²/h. It replaces mg-Ra eq and the old activity-times-exposure-rate-constant description. You need the unit identity now so a later TG-43 stem is not a new language.

f-factor. Under charged-particle equilibrium, rad per roentgen in a medium. In air it is the 0.876 derived below. In muscle, in the Compton range, it is near 0.97. Confirm a medium-specific table in Khan. The factor is much larger in bone at orthovoltage than at 6 MV.

**Formulas**

1 Ci = 3.7×10^10 Bq

1 R = 2.58×10^−4 C/kg

1 Gy = 100 cGy = 100 rad

1 cGy = 1 rad

1 Sv = 100 rem

1 cSv = 1 rem

H (Sv) = w_R × D (Gy)

Dose in air per roentgen, with W/e = 33.97 J/C:

(2.58×10^−4 C/kg) × (33.97 J/C) = 0.00876 J/kg = 0.876 rad in air per roentgen.

**Traps**

1 Gy = 1 rad. 1 cGy = 1 Gy. 1 R = 1 rad. 1 rem = 1 rad when the radiation is neutrons or alphas. Exposure assigned to a proton beam. Effective dose and equivalent dose swapped: equivalent dose is one organ and one w_R; effective dose folds in w_T. Air-kerma strength called a becquerel.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.10. W/e = 33.97 J/C and 1 R = 2.58×10^−4 C/kg are the constants that produce 0.876 rad/R in air; confirm the rounded f-factor table for tissue in Khan.

## Unit Conversion Tutorial

**MDCB:** I.10

**What the exam expects**

A stem stacks two conversions: activity and a dose, or a dose and a dose equivalent. You convert one step at a time and you stop in the unit the question asks for. This lesson is that sequence.

**Core facts**

Write the quantity first (activity, absorbed dose, equivalent dose, exposure). Then write the factor. Then multiply. Do not chain factors you cannot name.

Useful one-step factors:

- mCi to MBq: multiply by 37
- Ci to GBq: multiply by 37
- cGy to Gy: divide by 100
- Gy to rad: multiply by 100
- cGy to rad: multiply by 1
- rem to mSv: multiply by 10, because 1 rem = 0.01 Sv = 10 mSv
- mrem to mSv: divide by 100, because 1 mrem = 0.01 mSv
- rad of photons to rem: multiply by 1
- rad of alpha to rem: multiply by 20

**Formulas**

The identities in the previous lesson. Nothing new belongs in the arithmetic.

**Worked example**

Given, all in one stem the way an item is written:

- Source assay 2.50 mCi. Report Bq and MBq.
- Prescription 4500 cGy photons. Report Gy and rad.
- A badge reads 400 mrem of photons. Report mSv.
- A separate unsealed-source area survey reads 10.0 R in air under equilibrium. Report the absorbed dose in air in cGy.
- An alpha contamination event deposits 1.00 cGy in tissue, w_R = 20. Report equivalent dose in rem.

Activity. 1 mCi = 3.7×10^7 Bq, also 37 MBq.

2.50 × 3.7×10^7 = 9.25×10^7 Bq = 92.5 MBq.

Check: 2.50 × 37 = 92.5 MBq. Same.

Absorbed dose. 4500 cGy = 45.00 Gy = 4500 rad.

Because 1 cGy = 0.01 Gy and 1 cGy = 1 rad.

Badge. 400 mrem = 400 × 0.01 mSv = 4.00 mSv.

Because 1 rem = 10 mSv and 1 mrem = 0.01 mSv. Check: 400 mrem = 0.400 rem = 4.00 mSv.

Exposure to air dose. 1 R → 0.876 rad = 0.876 cGy in air.

10.0 × 0.876 = 8.76 cGy in air.

Alpha. D = 1.00 cGy = 0.0100 Gy. H = 20 × 0.0100 = 0.200 Sv = 20.0 rem.

Numeric shortcut that is legal here: the cGy number times w_R equals the rem number, because 1 cGy = 1 rad and 1 rad × w_R = 1 rem × w_R. 1 × 20 = 20 rem.

Meaning: 2.50 mCi is 92.5 million decays per second, not 2.50 decays per second. 4500 cGy is 45 Gy, not 4500 Gy. 400 mrem is 4 mSv, not 400 mSv. 10 R is 8.76 cGy in air, not 10 cGy and not 10 Gy. 1 cGy of alpha is 20 rem, not 1 rem.

Usual wrong turn: 1 mCi = 3.7×10^10 Bq, which is the curie, so 2.50 mCi becomes 9.25×10^10 Bq, a thousand times high. 4500 cGy called 4500 Gy. 400 mrem called 400 mSv (that would be 40 rem). 1 R called 1 rad in tissue. Alpha left at 1 rem because the cGy and the cSv were treated as identical.

**Traps**

Stopping after the first conversion when the stem asked for a second unit. Applying w_R to the photon prescription and reporting 4500 cSv as if something changed; for photons the number is allowed to stay, and the unit name changes only if they asked for equivalent dose. Applying the air f-factor 0.876 to a water prescription that was already in cGy. The 0.876 factor starts from roentgen, not from cGy.

**Sources**

Khan and Gibbons, *The Physics of Radiation Therapy*. Public blueprint I.10.

## Units Quiz

This quiz checks Ci to Bq, cGy to Gy, rad to cGy, rem to Sv, roentgen to air dose, and w_R applied only to equivalent dose. The traps are 1 Gy = 1 rad, 1 cGy = 1 Gy, 1 R = 1 rad, a factor of 37 pointed at the wrong prefix (mCi versus Ci), and w_R = 1 used for alpha particles.
