# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | d8cd1e7cfda63ac5ad42f4c11c90f6933c451f95a3d0ca28d3bfc1891171479f |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 2f0a2b64de8a51b6cc63c69982986356143de9a7e0690f51696f0b29c8bab90a; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.1 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $32,936.00

### classm.eic.1 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.1 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $32,936.00

### classm.eic.1 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.1 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $32,936.00

### classm.eic.1 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used because Step 5 Q2 is No

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used because Step 5 Q2 is No

No numeric assertion or class M credit: the model left this line blank.

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
Status: **SKIPPED**

Model: blank
Work: Skipped because line 4 is Yes

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 f6af437905efb58814c93ae8f9f82cd49b2f0a3abc7416121def126fbf7b40d1; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:true, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Stopped at Step 1: AGI $65,538.15 exceeds the no-child threshold and all applicable child thresholds for MFS.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Step 5 not reached because Step 1 STOP disallows the EIC.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Step 5 not reached because Step 1 STOP disallows the EIC.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Step 5 not reached because Step 1 STOP disallows the EIC.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Step 5 not reached because Step 1 STOP disallows the EIC.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached because the EIC is disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: No earned income credit allowed after Step 1 STOP.

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.3 — prompt sha256 ff595cf497062f7ed3ce51027787eb85d27841ba24dff1c203670fa86bb82330; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:true, eic.show_wsb4b:true, eic.show_wsb6:true, eic.wsb_6:positive, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:true, eic.line1#1, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.show3:true, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.show5:false, eic.line5#2, eic.smaller:left, eic.after_line4#0, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $13,709.00

### classm.eic.3 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.3 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $13,709.00

### classm.eic.3 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.3 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $13,709.00

### classm.eic.3 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $12,259.68

### classm.eic.3 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $12,259.68

### classm.eic.3 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $12,259.68

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $4,910.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $12,259.68

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped because line 4 is yes

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.3 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $4,910.00

### case classm.eic.4 — prompt sha256 60f126faf7f84feb08c9618673a18384791c153959f8fc9e826973677100a2c0; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#4, eic.line5_blank:true, eic.show5:false, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $5,137.00

### classm.eic.4 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $5,137.00

### classm.eic.4 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $5,137.00

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; no self-employment, so skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $5,137.00

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $1,743.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $16,019.00

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: 1+ child and 16,019.00 < 23,350.00: leave line 5 blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $1,743.00

### case classm.eic.5 — prompt sha256 56c6a40aa252e36592aa4bad3f25cbcf397a3581342f61224073148dc0d63b81; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#1, eic.step1_income:true, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:false, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:true, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit.

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.6 — prompt sha256 1dc893df8ef83d795e0dca51d4cd3b3b1ea02a033207b76d21fc7f738d89adef; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.6 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet B is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet B is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: Skipped: Step 1 Q3 is yes (Form 2555), so no EIC is allowed.

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.7 — prompt sha256 30c2ed71b94888cb0249caf897533d8328f99392f3feaa8f9554a46e0a5f91c2; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $52,948.00

### classm.eic.7 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $52,948.00

### classm.eic.7 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $52,948.00

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; Step 5 Q2 = No

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $52,948.00

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Skipped—Worksheet A line 2 is zero; STOP, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Skipped after STOP at Worksheet A line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped after STOP at Worksheet A line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: No earned income credit; STOP at Worksheet A line 2

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.8 — prompt sha256 ebacd93a25734e78ae7d70c3cf6d577f6465467f97d237a69e74494af93fa798; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:true, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

### classm.eic.8 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $25,118.00

### classm.eic.8 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.8 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $25,118.00

### classm.eic.8 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.8 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $25,118.00

### classm.eic.8 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Skipped; Worksheet B not used because Step 5 Q2 is No

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Skipped; Worksheet B not used because Step 5 Q2 is No

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $25,118.00

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $4,044.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $23,618.00

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $4,284.00

### classm.eic.8 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $4,044.00

## Raw responses

### classm.eic.1

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "32936.00"
    work: "Form 1040 line 1z = 32,936.00"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "Medicaid waiver payments excluded = 0"
  - printed: "line (Step 5, 3)"
    value: "32936.00"
    work: "32,936.00 - 0.00 = 32,936.00"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay election"
  - printed: "line (Step 5, 5)"
    value: "32936.00"
    work: "32,936.00 + 0.00 = 32,936.00"
  - printed: "line 4b"
    value: ""
    work: "Worksheet B not used because Step 5 Q2 is No"
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used because Step 5 Q2 is No"
  - printed: "line 1"
    value: "32936.00"
    work: "Earned income from Step 5 = 32,936.00"
  - printed: "line 2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, HOH, 1 child = 2,798"
  - printed: "line 3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936.00"
  - printed: "line 4"
    value: "yes"
    work: "Line 3 32,936.00 equals line 1 32,936.00"
  - printed: "line 5"
    value: ""
    work: "Skipped because line 4 is Yes"
  - printed: "line 6 (eic.line6)"
    value: "2798.00"
    work: "Line 4 Yes: enter line 2 amount = 2,798.00"
```

### classm.eic.2

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: ""
    work: "Stopped at Step 1: AGI $65,538.15 exceeds the no-child threshold and all applicable child thresholds for MFS."
  - printed: "line (Step 5, 2)"
    value: ""
    work: "Step 5 not reached because Step 1 STOP disallows the EIC."
  - printed: "line (Step 5, 3)"
    value: ""
    work: "Step 5 not reached because Step 1 STOP disallows the EIC."
  - printed: "line (Step 5, 4)"
    value: ""
    work: "Step 5 not reached because Step 1 STOP disallows the EIC."
  - printed: "line (Step 5, 5)"
    value: ""
    work: "Step 5 not reached because Step 1 STOP disallows the EIC."
  - printed: "line 4b"
    value: ""
    work: "Worksheet B not reached because the EIC is disallowed at Step 1."
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not reached because the EIC is disallowed at Step 1."
  - printed: "line 1"
    value: ""
    work: "Worksheet A not reached because the EIC is disallowed at Step 1."
  - printed: "line 2"
    value: ""
    work: "Worksheet A not reached because the EIC is disallowed at Step 1."
  - printed: "line 3"
    value: ""
    work: "Worksheet A not reached because the EIC is disallowed at Step 1."
  - printed: "line 4"
    value: ""
    work: "Worksheet A not reached because the EIC is disallowed at Step 1."
  - printed: "line 5"
    value: ""
    work: "Worksheet A not reached because the EIC is disallowed at Step 1."
  - printed: "line 6 (eic.line6)"
    value: ""
    work: "No earned income credit allowed after Step 1 STOP."
```

### classm.eic.3

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "13709.00"
    work: "Form 1040 line 1z = 13,709.00"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "Medicaid waiver payments = 0.00"
  - printed: "line (Step 5, 3)"
    value: "13709.00"
    work: "13,709.00 - 0.00 = 13,709.00"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "Nontaxable combat pay elected = 0.00"
  - printed: "line (Step 5, 5)"
    value: "13709.00"
    work: "13,709.00 + 0.00 = 13,709.00"
  - printed: "line 4b"
    value: "12259.68"
    work: "Worksheet B Parts 1&2 -1,449.32 + line 4a 13,709.00 = 12,259.68"
  - printed: "line 6 (eic.wsb_6)"
    value: "12259.68"
    work: "Line 4b is positive: 12,259.68"
  - printed: "line 1"
    value: "12259.68"
    work: "Use Worksheet B line 6 = 12,259.68"
  - printed: "line 2"
    value: "4910.00"
    work: "EIC Table: 12,250 to <12,300; single, 2 valid-SSN children = 4,910.00"
  - printed: "line 3"
    value: "12259.68"
    work: "Form 1040 line 11b = 12,259.68"
  - printed: "line 4"
    value: "yes"
    work: "12,259.68 equals 12,259.68"
  - printed: "line 5"
    value: ""
    work: "Skipped because line 4 is yes"
  - printed: "line 6 (eic.line6)"
    value: "4910.00"
    work: "Line 4 yes: enter line 2 amount = 4,910.00"
```

### classm.eic.4

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "5137.00"
    work: "Form 1040 line 1z = 5,137.00"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "Medicaid waiver payments excluded = 0"
  - printed: "line (Step 5, 3)"
    value: "5137.00"
    work: "5,137.00 - 0.00 = 5,137.00"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "Nontaxable combat pay elected = 0"
  - printed: "line (Step 5, 5)"
    value: "5137.00"
    work: "5,137.00 + 0.00 = 5,137.00"
  - printed: "line 4b"
    value: ""
    work: "Worksheet B not used; no self-employment, so skipped"
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used; skipped"
  - printed: "line 1"
    value: "5137.00"
    work: "Use Step 5 line 5 earned income = 5,137.00"
  - printed: "line 2"
    value: "1743.00"
    work: "EIC Table 5,100-5,150, QSS, 1 child = 1,743"
  - printed: "line 3"
    value: "16019.00"
    work: "Form 1040 line 11b = 16,019.00"
  - printed: "line 4"
    value: "no"
    work: "16,019.00 is not equal to 5,137.00"
  - printed: "line 5"
    value: ""
    work: "1+ child and 16,019.00 < 23,350.00: leave line 5 blank"
  - printed: "line 6 (eic.line6)"
    value: "1743.00"
    work: "Line 4 No; line 3 below threshold, so enter line 2 amount"
```

### classm.eic.5

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line (Step 5, 2)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line (Step 5, 3)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line (Step 5, 4)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line (Step 5, 5)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 4b"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 1"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 2"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 3"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 4"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 5"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
  - printed: "line 6 (eic.line6)"
    value: ""
    work: "Step 1 Q2 No (no valid EIC SSN); STOP, cannot take credit."
```

### classm.eic.6

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken."
  - printed: "line (Step 5, 2)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken."
  - printed: "line (Step 5, 3)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken."
  - printed: "line (Step 5, 4)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken."
  - printed: "line (Step 5, 5)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so the EIC stops and cannot be taken."
  - printed: "line 4b"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet B is not used."
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet B is not used."
  - printed: "line 1"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used."
  - printed: "line 2"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used."
  - printed: "line 3"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used."
  - printed: "line 4"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used."
  - printed: "line 5"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so Worksheet A is not used."
  - printed: "line 6 (eic.line6)"
    value: ""
    work: "Skipped: Step 1 Q3 is yes (Form 2555), so no EIC is allowed."
```

### classm.eic.7

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "52948.00"
    work: "Form 1040 line 1z = 52,948.00"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "Medicaid waiver payments excluded from income = 0.00"
  - printed: "line (Step 5, 3)"
    value: "52948.00"
    work: "52,948.00 - 0.00 = 52,948.00"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected = 0.00"
  - printed: "line (Step 5, 5)"
    value: "52948.00"
    work: "52,948.00 + 0.00 = 52,948.00"
  - printed: "line 4b"
    value: ""
    work: "Worksheet B not used; Step 5 Q2 = No"
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used; skipped"
  - printed: "line 1"
    value: "52948.00"
    work: "Worksheet A uses Step 5 earned income = 52,948.00"
  - printed: "line 2"
    value: "0.00"
    work: "EIC table: single, 0 qualifying children, 52,948.00 = 0.00"
  - printed: "line 3"
    value: ""
    work: "Skipped—Worksheet A line 2 is zero; STOP, no credit"
  - printed: "line 4"
    value: ""
    work: "Skipped after STOP at Worksheet A line 2"
  - printed: "line 5"
    value: ""
    work: "Skipped after STOP at Worksheet A line 2"
  - printed: "line 6 (eic.line6)"
    value: ""
    work: "No earned income credit; STOP at Worksheet A line 2"
```

### classm.eic.8

```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "25118.00"
    work: "Form 1040 line 1z"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded"
  - printed: "line (Step 5, 3)"
    value: "25118.00"
    work: "25,118 - 0"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected"
  - printed: "line (Step 5, 5)"
    value: "25118.00"
    work: "25,118 + 0 = earned income"
  - printed: "line 4b"
    value: ""
    work: "Skipped; Worksheet B not used because Step 5 Q2 is No"
  - printed: "line 6 (eic.wsb_6)"
    value: ""
    work: "Skipped; Worksheet B not used because Step 5 Q2 is No"
  - printed: "line 1"
    value: "25118.00"
    work: "Use Step 5 earned income"
  - printed: "line 2"
    value: "4044.00"
    work: "EIC Table: 25,118; MFS uses single column, 1 child"
  - printed: "line 3"
    value: "23618.00"
    work: "Form 1040 line 11b"
  - printed: "line 4"
    value: "no"
    work: "23,618 is not equal to 25,118"
  - printed: "line 5"
    value: "4284.00"
    work: "23,618 not less than 23,350; table row 23,600-23,650, 1 child"
  - printed: "line 6 (eic.line6)"
    value: "4044.00"
    work: "Smaller of line 5 4,284 and line 2 4,044"
```
