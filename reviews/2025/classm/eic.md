# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 75f7a863f6829e8f510ff9dfeac80b0f549782d6d590d290de2105e98228ca1a |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 d16b0c37d4b6ed1dca2f2911cb129f1fcc03b89a6e1ebf0d037693f63522ceec; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#4, eic.line5_blank:true, eic.line5#1, eic.smaller:left, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.1 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not self-employed, no Schedule SE and no statutory-employee Schedule C, so Step 5 Q2 is No. Use Worksheet A; Worksheet B is not used.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.1 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $5,137.00

### classm.eic.1 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $1,743.00

### classm.eic.1 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $2,137.00

### classm.eic.1 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.1 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: 1 qualifying child and line 3 of $2,137 is less than $23,350, so leave line 5 blank and enter line 2 on line 6.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.1 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $1,743.00

### case classm.eic.2 — prompt sha256 d287a5d6fec1b74b695db23e0905d0a119958c2c1ca9969ecf953364c7675912; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.self_employed:true, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP: no qualifying children with valid SSNs and line 11b $22,732 is not less than $19,104

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP. Investment income $97,691 also exceeds $11,950 with no Form 4797, and MFS with no qualifying child also stops at Step 4 q1

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP, so Worksheet A is not used

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached; Step 1 STOP

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 f935455101879eed1b649264b83c6e064a3997f66371b137730485f04e9201ea; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#2, eic.smaller:left, eic.after_line4#0, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not self-employed, no Schedule SE, not a statutory employee; Step 5 Q2 = No, so use Worksheet A, not B

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.3 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used (Step 5 Q2 = No)

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.3 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $13,709.00

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $5,490.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $13,709.00

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped because line 4 = Yes

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.3 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $5,490.00

### case classm.eic.4 — prompt sha256 ac95d1592bd6da48a71a922224448c306d68a43209f1f03f0f53435b821cf9e4; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used: no self-employment, no Schedule C or SE (Step 5 Q2 = No); the flowchart stops earlier anyway

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: STOP before Step 5: no EIC qualifying child; Step 4 Q1 married + head of household = can't take credit (also Step 1 Q3 Form 2555 = yes; Step 4 Q3 main home not in US)

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached; ineligible per the flowchart

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Not reached; ineligible per the flowchart

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Not reached; ineligible per the flowchart

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached; ineligible per the flowchart

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 5d3cc5003451f1536660ac4cad6a6bd5d085409afa1877569c0dacbbc86a1c88; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:true, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:true, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:true, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $-18,567.98

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $16,111.02

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: No qualifying children; line 3 16,111.02 < 17,730 (MFJ), so leave blank and carry line 2 to line 6

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 d3ccca81282b2956d490f90ee3f6bc328b2098fb0f3f06bd96e3491bbb956b09; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used: no self-employment, clergy income or statutory-employee income (0 Schedules C). Step 1 also stops the credit.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used, and Step 1 stops the credit.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Step 1 STOP: single with no children who have valid SSNs, and line 11b $66,664 is not less than $19,104. You can't take the credit.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached because Step 1 says STOP.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Not reached because Step 1 says STOP.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Not reached because Step 1 says STOP.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Not reached because Step 1 says STOP.

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 121e22481e40ea9bbfd2dc16b5c1607cc6fe8e0d40c20e576b170cbba3cc8072; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.self_employed:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:true, eic.line5#2, eic.smaller:left, eic.after_line4#0, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 5 Q2 = No (not self-employed, no clergy or church income, no statutory employee), so Worksheet A applies and Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used; Worksheet A applies

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $19,388.00

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $7,152.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $19,388.00

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped because line 4 is Yes

No numeric assertion or class M credit: the model left this line blank.


### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $7,152.00

### case classm.eic.8 — prompt sha256 32472060332038f33c50c9388e3a4e58519bc574b41749a2457b77f3ebeff8ce; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.self_employed:true, eic.wsb_6:positive, eic.earned_for_limit#1, eic.step5_income:false, eic.eligible:false, eic.line1#1, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:true, eic.wsb_line5_stop:true, eic.separated_box:false, eic.clergy:false

### classm.eic.8 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $55,005.10

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $55,005.10

### classm.eic.8 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $55,005.10

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $48,693.10

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $281.00
Model: $1,819.00
Work: 48,693.10 is not less than 23,350; table row 48,650-48,700, Single, 1 child = 1,819

Ruling: model table-reading error; project retained; model value dropped from the fixture. The 2025 EIC Table row 'At least 48,650 But less than 48,700', one qualifying child, in the column for single, head of household or qualifying surviving spouse, is $281 (i1040gi, the EIC Table page whose rows run 48,600 to 48,800; the printed row reads '289 281 273 265' for 48,600, 48,650, 48,700 and 48,750); the model's $1,819 appears in no column of that row. Line 3 ($48,693.10) is above the $23,350 line 5 amount, so line 5 is looked up, as both sides agree. [dropped]

### classm.eic.8 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

```yaml
```yaml
lines:
  - printed: "4b"
    value: ""
    work: "Not self-employed, no Schedule SE and no statutory-employee Schedule C, so Step 5 Q2 is No. Use Worksheet A; Worksheet B is not used."
  - printed: "6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B is not used."
  - printed: "1"
    value: "5137.00"
    work: "Step 5 earned income: Form 1040 line 1z $5,137 - $0 Medicaid waiver + $0 combat pay = $5,137."
  - printed: "2"
    value: "1743.00"
    work: "EIC Table row $5,100-$5,150, qualifying surviving spouse column, 1 child with a valid SSN (dep_a): $1,743."
  - printed: "3"
    value: "2137.00"
    work: "Form 1040 line 11b."
  - printed: "4"
    value: "no"
    work: "$2,137 is not the same as $5,137, so go to line 5."
  - printed: "5"
    value: ""
    work: "1 qualifying child and line 3 of $2,137 is less than $23,350, so leave line 5 blank and enter line 2 on line 6."
  - printed: "6 (eic.line6)"
    value: "1743.00"
    work: "Line 2 amount: $1,743."
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Not reached; Step 1 STOP: no qualifying children with valid SSNs and line 11b $22,732 is not less than $19,104"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Not reached; Step 1 STOP. Investment income $97,691 also exceeds $11,950 with no Form 4797, and MFS with no qualifying child also stops at Step 4 q1"
  - printed: "1"
    value: "blank"
    work: "Not reached; Step 1 STOP, so Worksheet A is not used"
  - printed: "2"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "3"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "4"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "5"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Not eligible, so no earned income credit; credit is $0"
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, no Schedule SE, not a statutory employee; Step 5 Q2 = No, so use Worksheet A, not B"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used (Step 5 Q2 = No)"
  - printed: "1"
    value: "13709.00"
    work: "Step 5 earned income = 1z 13,709 - 0 Medicaid waiver + 0 combat pay = 13,709"
  - printed: "2"
    value: "5490.00"
    work: "EIC Table row 13,700-13,750, Single, 2 qualifying children with valid SSNs (dep_a, dep_c) = 5,490"
  - printed: "3"
    value: "13709.00"
    work: "Form 1040 line 11b = 13,709"
  - printed: "4"
    value: "yes"
    work: "Line 3 13,709 = line 1 13,709; skip line 5, enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 = Yes"
  - printed: "6 (eic.line6)"
    value: "5490.00"
    work: "Amount from line 2 = 5,490"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "line 4b"
    value: "blank"
    work: "Worksheet B is not used: no self-employment, no Schedule C or SE (Step 5 Q2 = No); the flowchart stops earlier anyway"
  - printed: "line 6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used"
  - printed: "line 1"
    value: "blank"
    work: "STOP before Step 5: no EIC qualifying child; Step 4 Q1 married + head of household = can't take credit (also Step 1 Q3 Form 2555 = yes; Step 4 Q3 main home not in US)"
  - printed: "line 2"
    value: "blank"
    work: "Not reached; ineligible per the flowchart"
  - printed: "line 3"
    value: "blank"
    work: "Not reached; ineligible per the flowchart"
  - printed: "line 4"
    value: "blank"
    work: "Not reached; ineligible per the flowchart"
  - printed: "line 5"
    value: "blank"
    work: "Not reached; ineligible per the flowchart"
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "You can't take the credit; EIC = 0"
```
```

### classm.eic.5

```yaml
lines:
  - printed: "4b"
    value: "-18567.98"
    work: "Parts 1–2: -64,231.98 + 0.00 = -64,231.98; Part 3 = 0; 4a = line 1z 45,664.00; total = -18,567.98. Zero or less, so STOP: no credit"
  - printed: "6 (eic.wsb_6)"
    value: "0.00"
    work: "Line 4b (-18,567.98) is zero or less, so enter 0"
  - printed: "1"
    value: "0.00"
    work: "From Worksheet B line 6 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, MFJ, 0 children: 0 is below the first row (1–50), so credit 0. Line 2 is zero, so STOP: no credit"
  - printed: "3"
    value: "16111.02"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "no"
    work: "16,111.02 ≠ 0.00"
  - printed: "5"
    value: "blank"
    work: "No qualifying children; line 3 16,111.02 < 17,730 (MFJ), so leave blank and carry line 2 to line 6"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Line 2 = 0. Also ineligible: Step 1 Q2 no valid SSNs (STOP), investment income 34,679 > 11,950 with no Form 4797 (STOP), line 4b ≤ 0"
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "line 4b"
    value: "blank"
    work: "Worksheet B is not used: no self-employment, clergy income or statutory-employee income (0 Schedules C). Step 1 also stops the credit."
  - printed: "line 6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used, and Step 1 stops the credit."
  - printed: "line 1"
    value: "blank"
    work: "Step 1 STOP: single with no children who have valid SSNs, and line 11b $66,664 is not less than $19,104. You can't take the credit."
  - printed: "line 2"
    value: "blank"
    work: "Not reached because Step 1 says STOP."
  - printed: "line 3"
    value: "blank"
    work: "Not reached because Step 1 says STOP."
  - printed: "line 4"
    value: "blank"
    work: "Not reached because Step 1 says STOP."
  - printed: "line 5"
    value: "blank"
    work: "Not reached because Step 1 says STOP."
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "No credit is allowed: AGI $66,664 is not less than the $19,104 limit for single filers with no qualifying children."
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "4b"
    value: "blank"
    work: "Step 5 Q2 = No (not self-employed, no clergy or church income, no statutory employee), so Worksheet A applies and Worksheet B is not used"
  - printed: "line 6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used; Worksheet A applies"
  - printed: "1"
    value: "19388.00"
    work: "Step 5 earned income: line 1z 19,388 - Medicaid waiver 0 + combat pay 0 = 19,388"
  - printed: "2"
    value: "7152.00"
    work: "EIC Table row 19,350-19,400, Single/HOH/QSS column (★ used for MFS), 2 qualifying children with valid SSNs = 7,152"
  - printed: "3"
    value: "19388.00"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "yes"
    work: "Line 3 19,388 = line 1 19,388, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "line 6 (eic.line6)"
    value: "7152.00"
    work: "Amount from line 2; eligible under the MFS separated-spouse rule (Step 3 Q4 = No, Q6 = No)"
```
```

### classm.eic.8

```yaml
lines:
  - printed: "4b"
    value: "55005.10"
    work: "Parts 1-3 (1e+2c+3) -18,573.90 + 4a 73,579.00 (Step 5 earned income from 1040 line 1z) = 55,005.10"
  - printed: "6 (eic.wsb_6)"
    value: "55005.10"
    work: "From line 4b 55,005.10 (positive). Line 5 test: 1 child, 55,005.10 is not less than 50,434, so STOP, you can't take the credit"
  - printed: "1"
    value: "55005.10"
    work: "Worksheet B line 6 = 55,005.10"
  - printed: "2"
    value: "0.00"
    work: "55,005.10 is at least $50,434 with 1 qualifying child, so you can't take the credit; table gives 0"
  - printed: "3"
    value: "48693.10"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "no"
    work: "48,693.10 is not equal to 55,005.10"
  - printed: "5"
    value: "1819.00"
    work: "48,693.10 is not less than 23,350; table row 48,650-48,700, Single, 1 child = 1,819"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Smaller of line 5 (1,819) and line 2 (0) = 0; earned income fails the line 5 limit, so no credit"
```
