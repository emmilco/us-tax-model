# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | cb83c4a7c13e4519c0bb5ff3cf26b9ae43c1b19b2e04d0ad6f490897983a7968 |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 73541683e7181aa17701f3bd9a2e76d9646fc6097a55ed519827a4e0dedbddec; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.1 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **DISAGREE**

Project: $32,936.00
Model: $0.00
Work: Step 5 q2 = No (not self-employed, no Schedule SE or statutory employee), so Worksheet B is not used

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. [dropped]

### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **DISAGREE**

Project: $32,936.00
Model: $0.00
Work: Worksheet B is not used; Worksheet A applies

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. [dropped]

### classm.eic.1 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $32,936.00

### classm.eic.1 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $2,798.00

### classm.eic.1 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $32,936.00

### classm.eic.1 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.1 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $2,798.00
Model: $0.00
Work: Skipped because line 4 = Yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.1 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 750f92b5164385ec10002dcc43bfb897386dc2286110a4e3633c40d9515bd032; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:false, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:false, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $23,500.00
Model: $0.00
Work: Not reached; taxpayer can't take the credit (Step 1 STOP)

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 d9b76729cf64f3c1006324e44a47b3e5ede51e26d4ab92b96dc1b1e47fa742ec; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:true, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $-53,866.40

### classm.eic.3 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $16,351.60

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $649.00
Model: $0.00
Work: No children; line 3 (16,351.60) is less than 17,730 (MFJ), so leave line 5 blank and use line 2

Ruling: representation; project retained; model value dropped from the fixture. Worksheet A says to leave line 5 blank when line 3 is less than the amount for the filing status and number of children ($17,730 married filing jointly with none) and to take line 2; the project looks line 5 up regardless and line 6 takes line 2. The credit, line 6, agrees at $0.00. [dropped]

### classm.eic.3 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.4 — prompt sha256 3c42786d4f3073637704821585b719d7f8841c27746f8add54a8b43e1f544f50; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#2, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#2, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $33.00
Model: $0.00
Work: STOP at line 2 (credit zero); remaining lines not completed

Ruling: representation; project retained; model value dropped from the fixture. Worksheet A line 2 is $0 (the EIC Table gives no credit for this earned income), so the worksheet stops there (amb.2025.eic_below_table); the project figures lines 3 and 5 anyway, and the credit, line 6, agrees at $0.00. [dropped]

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $10.00
Model: $0.00
Work: STOP at line 2

Ruling: representation; project retained; model value dropped from the fixture. Worksheet A line 2 is $0 (the EIC Table gives no credit for this earned income), so the worksheet stops there (amb.2025.eic_below_table); the project figures lines 3 and 5 anyway, and the credit, line 6, agrees at $0.00. [dropped]

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 7a69e3901cad1e187933963eb3df5fa0cbcb102e1cf08fe9eb37048d4d2cfb50; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **DISAGREE**

Project: $62,208.00
Model: $0.00
Work: Step 1 Q1: no qualifying children; line 11b $61,797 is not less than $19,104, so STOP and Worksheet B is not used

Ruling: representation; project retained; model value dropped from the fixture. The flow chart stops at Step 1 (i1040gi p. 40: with no qualifying child, Form 1040 line 11b is not less than $19,104), so no worksheet line is reached; the project figures the lines anyway and its credit, Worksheet A line 6, is $0.00 as the model's. [dropped]

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **DISAGREE**

Project: $62,208.00
Model: $0.00
Work: Not reached; the Step 1 STOP means no worksheet is completed

Ruling: representation; project retained; model value dropped from the fixture. The flow chart stops at Step 1 (i1040gi p. 40: with no qualifying child, Form 1040 line 11b is not less than $19,104), so no worksheet line is reached; the project figures the lines anyway and its credit, Worksheet A line 6, is $0.00 as the model's. [dropped]

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **DISAGREE**

Project: $62,208.00
Model: $0.00
Work: Not reached; Step 1 STOP (also Step 4 Q5: could be a qualifying child of another person, so STOP)

Ruling: representation; project retained; model value dropped from the fixture. The flow chart stops at Step 1 (i1040gi p. 40: with no qualifying child, Form 1040 line 11b is not less than $19,104), so no worksheet line is reached; the project figures the lines anyway and its credit, Worksheet A line 6, is $0.00 as the model's. [dropped]

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $61,797.00
Model: $0.00
Work: Not reached; the credit cannot be taken

Ruling: representation; project retained; model value dropped from the fixture. The flow chart stops at Step 1 (i1040gi p. 40: with no qualifying child, Form 1040 line 11b is not less than $19,104), so no worksheet line is reached; the project figures the lines anyway and its credit, Worksheet A line 6, is $0.00 as the model's. [dropped]

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 3111ece1929b959f3396fa8b25784f4628b41a3d9e62a25210c006490389b25a; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:false, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Not self-employed, no clergy or church income and no statutory employee income, so Worksheet B isn't used; also Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. Step 1 also stops this return. [dropped]

### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Worksheet B isn't used; Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. Step 1 also stops this return. [dropped]

### classm.eic.6 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Step 1: no qualifying children with valid SSNs, and line 11b $51,610 is not less than $19,104, so STOP: you can't take the credit; worksheet not reached

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Not reached; Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **DISAGREE**

Project: yes
Model: no
Work: Not reached; Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 9a294fc99a7b0dd634ac33c14d60665ee105a0191f1e7e16fb81535b9b98d45b; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#2, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **DISAGREE**

Project: $44,084.00
Model: $0.00
Work: Not self-employed (Step 5 Q2 = No), so Worksheet A is used and Worksheet B is not completed

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. [dropped]

### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **DISAGREE**

Project: $44,084.00
Model: $0.00
Work: Worksheet B not used

Ruling: representation; project retained; model value dropped from the fixture. Worksheet B is used only when Step 5, question 2 is Yes (i1040gi p. 42: self-employment, church employee or statutory employee income); the project figures its lines for every return and nothing reads them when it is not used. The credit, Worksheet A line 6 (Form 1040 line 27a), agrees. [dropped]

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $44,084.00

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $2,787.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $44,084.00

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $2,787.00
Model: $0.00
Work: Skipped because line 4 is Yes

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $2,787.00

### case classm.eic.8 — prompt sha256 5d20ba1e9c2a8adc2d93b4f4b8677cd2bf5cc9f25adca7d5694c448d4636f196; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.8 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $108.00
Model: $0.00
Work: STOP at line 2 (credit is zero); remaining lines not completed

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $10.00
Model: $0.00
Work: STOP at line 2

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.8 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Step 5 q2 = No (not self-employed, no Schedule SE or statutory employee), so Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used; Worksheet A applies"
  - printed: "1"
    value: "32936.00"
    work: "Step 5 worksheet: line 1z 32,936 - Medicaid waiver 0 + combat pay 0 = 32,936"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, head of household, 1 child with valid SSN (dep_c) = 2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936"
  - printed: "4"
    value: "yes"
    work: "Line 3 32,936 = line 1 32,936, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 = Yes"
  - printed: "6 (eic.line6)"
    value: "2798.00"
    work: "Amount from line 2 = 2,798"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used: no self-employment, Schedule SE, or statutory employee income, so Step 5 Q2 is No; eligibility also stopped at Step 1"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used; eligibility stopped at Step 1"
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1 STOP: no children, and line 11b of $23,500 is not less than $19,104; Step 1 Q2 STOP (no valid SSN); Step 1 Q3 STOP (Form 2555); worksheet not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; taxpayer can't take the credit (Step 1 STOP)"
  - printed: "3"
    value: "blank"
    work: "Not reached; taxpayer can't take the credit (Step 1 STOP)"
  - printed: "4"
    value: "blank"
    work: "Not reached; taxpayer can't take the credit (Step 1 STOP)"
  - printed: "5"
    value: "blank"
    work: "Not reached; taxpayer can't take the credit (Step 1 STOP)"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Not eligible (Step 1 STOP: AGI, SSN, and Form 2555 tests failed); EIC = 0"
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "4b"
    value: "-53866.40"
    work: "Line 1e + line 2c (Worksheet B Parts 1-2: -57,074.40 + 0) + line 3 (0) + line 4a (3,208.00) = -53,866.40; zero or less, so STOP, no credit"
  - printed: "6 (eic.wsb_6)"
    value: "0.00"
    work: "Line 4b is -53,866.40, which is zero or less, so enter 0"
  - printed: "1"
    value: "0.00"
    work: "Self-employed, so Worksheet B applies; Worksheet B line 6 = 0"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, MFJ, 0 children: 0 is below the first row (1-50), so the credit is 0"
  - printed: "3"
    value: "16351.60"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "no"
    work: "16,351.60 differs from 0"
  - printed: "5"
    value: ""
    work: "No children; line 3 (16,351.60) is less than 17,730 (MFJ), so leave line 5 blank and use line 2"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Line 2 = 0. Also, Step 2 investment income (0 + 11,303 + 0 + 58,915 = 70,218) is more than 11,950 and no Form 4797 is filed, so STOP, no credit"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, no clergy or church income, no statutory employee (Step 5 Q2 = No), so Worksheet A is used and Worksheet B is not completed"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used (Step 5 Q2 = No)"
  - printed: "1"
    value: "0.00"
    work: "Step 5 earned income: line 1z 0.00 - 0 Medicaid waiver + 0 combat pay = 0.00"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, Single, 2 children with valid SSNs (dep_a and dep_c): amount 0 is below the first row (1-50), so credit is 0. Line 2 is zero: STOP, can't take the credit"
  - printed: "3"
    value: "blank"
    work: "STOP at line 2 (credit zero); remaining lines not completed"
  - printed: "4"
    value: "blank"
    work: "STOP at line 2"
  - printed: "5"
    value: "blank"
    work: "STOP at line 2"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "STOP at line 2; no credit; check box on line 27c"
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Step 1 Q1: no qualifying children; line 11b $61,797 is not less than $19,104, so STOP and Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Not reached; the Step 1 STOP means no worksheet is completed"
  - printed: "1"
    value: "blank"
    work: "Not reached; Step 1 STOP (also Step 4 Q5: could be a qualifying child of another person, so STOP)"
  - printed: "2"
    value: "blank"
    work: "Not reached; the credit cannot be taken"
  - printed: "3"
    value: "blank"
    work: "Not reached; the credit cannot be taken"
  - printed: "4"
    value: "blank"
    work: "Not reached; the credit cannot be taken"
  - printed: "5"
    value: "blank"
    work: "Not reached; the credit cannot be taken"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "You can't take the credit (Step 1 STOP); no EIC is entered"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, no clergy or church income and no statutory employee income, so Worksheet B isn't used; also Step 1 says STOP"
  - printed: "line 6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B isn't used; Step 1 says STOP"
  - printed: "1"
    value: "blank"
    work: "Step 1: no qualifying children with valid SSNs, and line 11b $51,610 is not less than $19,104, so STOP: you can't take the credit; worksheet not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; Step 1 says STOP (Step 4 Q3 would also stop: main home not in the U.S.)"
  - printed: "3"
    value: "blank"
    work: "Not reached; Step 1 says STOP"
  - printed: "4"
    value: "blank"
    work: "Not reached; Step 1 says STOP"
  - printed: "5"
    value: "blank"
    work: "Not reached; Step 1 says STOP"
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "Not eligible (Step 1: $51,610 is not less than $19,104 with 0 qualifying children), so EIC = 0"
```
```

### classm.eic.7

```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Not self-employed (Step 5 Q2 = No), so Worksheet A is used and Worksheet B is not completed"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used"
  - printed: "1"
    value: "44084.00"
    work: "Step 5 earned income: 1040 line 1z 44,084 - 0 Medicaid waiver + 0 combat pay = 44,084"
  - printed: "2"
    value: "2787.00"
    work: "EIC Table 44,050-44,100, Single/HOH/QSS (MFS) column, 2 children with valid SSNs = 2,787"
  - printed: "3"
    value: "44084.00"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "yes"
    work: "Line 3 44,084 = line 1 44,084, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "6 (eic.line6)"
    value: "2787.00"
    work: "Amount from line 2"
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Step 5 Q2 = No (not self-employed, no Schedule C or SE), so Worksheet A applies; Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used because Step 5 Q2 = No"
  - printed: "1"
    value: "0.00"
    work: "Step 5 worksheet: line 1z $0 - Medicaid waiver $0 + combat pay $0 = $0 earned income"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, Single, 0 children with valid SSNs (dep_a has no valid SSN); $0 is below the first $1-$50 row, so credit $0; line 2 is zero, STOP"
  - printed: "3"
    value: "blank"
    work: "STOP at line 2 (credit is zero); remaining lines not completed"
  - printed: "4"
    value: "blank"
    work: "STOP at line 2"
  - printed: "5"
    value: "blank"
    work: "STOP at line 2"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "STOP at line 2: you can't take the credit; check the box on line 27c"
```
```
