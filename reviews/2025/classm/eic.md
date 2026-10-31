# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ae5c9f11087bd77489d49692a8d8e463240dc399a2a63de2773d7e097d4f8ceb |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 6fc5cb49f093a0cf00f2c0a267a3b03ffa440f99ea7af3cd64edd292303399ad; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

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
Work: Step 5 question 2 is No (no self-employment, clergy, church or statutory income), so Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used; Worksheet A applies

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
Work: Line 4 is Yes; skip line 5

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 197065e2bd63fb2daf584aa01900546c97d97878c07709e8253f10aab2d0b6df; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:true, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q1: no qualifying children; line 11b 65,538.15 is not less than 19,104, so STOP; line not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached; STOP at Step 1 Q1 (you can't take the credit)

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: No credit: STOP at Step 1 Q1; investment income 82,786.00 > 11,950 and MFS with no qualifying child would also STOP

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.3 — prompt sha256 dd6f81fd38c45ba7d056ea1db79f58c4a01172f2c6c4db4f8df6764a893d3c5c; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:true, eic.show_wsb4b:true, eic.show_wsb6:true, eic.wsb_6:positive, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:true, eic.line1#1, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.show3:true, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.show5:false, eic.line5#2, eic.smaller:left, eic.after_line4#0, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

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

### case classm.eic.4 — prompt sha256 cf805b435e7c79a07f05189ddc6daf660f7582e391b1d217b0ad3a6a11db3935; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#4, eic.line5_blank:true, eic.show5:false, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

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
Work: No self-employment, clergy, church employee or statutory employee income, so Step 5 Q2 is No; Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used because Step 5 Q2 is No

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
Work: 1 qualifying child and line 3 of 16,019 is less than 23,350: Yes, leave line 5 blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $1,743.00

### case classm.eic.5 — prompt sha256 36fd4d30bc8649d88edfddbce26ba21feba36260bd9b8b099db7abaf8dc7395e; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#1, eic.step1_income:true, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:false, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:true, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1, question 2: SSNs valid for the EIC = no, so STOP; can't take the credit; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1, question 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: No EIC: Step 1 Q1 passes ($32,039 < $57,554), Q2 = no, so STOP and check the box on line 27c

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.6 — prompt sha256 402e2cfa8cea93a9cee367f4b70dc2db72d37643e20226794f42d76de1544a53; branches: eic.qc_of_another:true, eic.died_2025:false, eic.age_range:true, eic.us_home:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.6 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Not reached: no qualifying child, so Step 3 goes to Step 4; Step 4 Q1 married with head of household status = STOP before Step 5

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached: Step 4 Q1 STOP, can't take the credit

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached: Step 4 Q1 STOP, can't take the credit

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached: Step 4 Q1 STOP, can't take the credit

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached: Step 4 Q1 STOP, can't take the credit

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: Step 4 Q1 STOP came first

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: No credit: married at end of 2025, filing head of household, no qualifying child; Step 4 Q1 says can't take the credit

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.7 — prompt sha256 ad9b0222aebbc9260bbada37dec653b822137f1579de6315d9f580276c50e234; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:false, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Not reached: no qualifying children and Step 1 Q1 line 11b $50,354 is not less than $19,104, so STOP

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used: STOP at Step 1 Q1; no Schedule C or SE and Worksheet B Parts 1 and 2 are $0

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1 Q1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: You can't take the credit: $50,354 is not less than the $19,104 limit for Single with no children, so no EIC is figured

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.8 — prompt sha256 cda756dd5c1df6474be6ac34d86c30dd4dcf8cb99647f5bea223aa14828786a3; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:true, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

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
Work: Step 5 question 2 is No (no self-employment), so Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Step 5 question 2 is No (no self-employment), so Worksheet B is not used

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
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "32936.00"
    work: "Form 1040 line 1z = 32,936.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "32936.00"
    work: "32,936.00 - 0.00 = 32,936.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "32936.00"
    work: "32,936.00 + 0.00 = 32,936.00; earned income"
  - printed: "4b"
    value: "blank"
    work: "Step 5 question 2 is No (no self-employment, clergy, church or statutory income), so Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used; Worksheet A applies"
  - printed: "1"
    value: "32936.00"
    work: "Earned income from Step 5, line 5"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table, 32,900-32,950, single/HOH column with 1 child (only dep_c has a valid SSN) = 2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936.00"
  - printed: "4"
    value: "yes"
    work: "Line 3 (32,936.00) equals line 1 (32,936.00)"
  - printed: "5"
    value: "blank"
    work: "Line 4 is Yes; skip line 5"
  - printed: "6 (eic.line6)"
    value: "2798.00"
    work: "Line 4 is Yes; enter line 2 amount = 2,798.00"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Step 1 Q1: no qualifying children; line 11b 65,538.15 is not less than 19,104, so STOP; line not reached"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached; STOP at Step 1 Q1 (you can't take the credit)"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached; STOP at Step 1 Q1"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached; STOP at Step 1 Q1"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached; STOP at Step 1 Q1"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not reached; STOP at Step 1 Q1"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not reached; STOP at Step 1 Q1"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached; STOP at Step 1 Q1"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached; STOP at Step 1 Q1"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached; STOP at Step 1 Q1"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached; STOP at Step 1 Q1"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached; STOP at Step 1 Q1"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "No credit: STOP at Step 1 Q1; investment income 82,786.00 > 11,950 and MFS with no qualifying child would also STOP"
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "13709.00"
    work: "Form 1040 line 1z = 13,709.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "13709.00"
    work: "13,709.00 - 0.00 = 13,709.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "13709.00"
    work: "13,709.00 + 0.00 = 13,709.00"
  - printed: "4b"
    value: "12259.68"
    work: "Has Schedule C, so Step 5 Q2 is yes and Worksheet B applies: -1,449.32 (Parts 1 and 2) + 0 (line 3) + 13,709.00 (line 4a) = 12,259.68"
  - printed: "6 (eic.wsb_6)"
    value: "12259.68"
    work: "Worksheet B line 4b is above zero and less than $57,310 (2 qualifying children with valid SSNs), so enter 12,259.68"
  - printed: "1"
    value: "12259.68"
    work: "Self-employed, so use Worksheet B line 6 = 12,259.68"
  - printed: "2"
    value: "4910.00"
    work: "EIC Table row 12,250-12,300, Single column, 2 children (dep_a and dep_c have valid SSNs) = 4,910"
  - printed: "3"
    value: "12259.68"
    work: "Form 1040 line 11b = 12,259.68"
  - printed: "4"
    value: "yes"
    work: "Line 3 12,259.68 equals line 1 12,259.68; skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is yes"
  - printed: "6 (eic.line6)"
    value: "4910.00"
    work: "Line 4 is yes, so enter the line 2 amount = 4,910"
```
```

### classm.eic.4

```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "5137.00"
    work: "Form 1040 line 1z = 5,137.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "5137.00"
    work: "5,137.00 - 0.00 = 5,137.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "5137.00"
    work: "5,137.00 + 0.00 = 5,137.00"
  - printed: "4b"
    value: "blank"
    work: "No self-employment, clergy, church employee or statutory employee income, so Step 5 Q2 is No; Worksheet B not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used because Step 5 Q2 is No"
  - printed: "1"
    value: "5137.00"
    work: "Worksheet A uses earned income from Step 5, line 5 = 5,137.00"
  - printed: "2"
    value: "1743.00"
    work: "EIC Table row 5,100-5,150, qualifying surviving spouse column, 1 child with valid SSN (dep_a only) = 1,743"
  - printed: "3"
    value: "16019.00"
    work: "Form 1040 line 11b = 16,019.00"
  - printed: "4"
    value: "no"
    work: "16,019.00 is not the same as 5,137.00; go to line 5"
  - printed: "5"
    value: "blank"
    work: "1 qualifying child and line 3 of 16,019 is less than 23,350: Yes, leave line 5 blank"
  - printed: "6 (eic.line6)"
    value: "1743.00"
    work: "Line 5 test is Yes, so enter the amount from line 2 = 1,743.00"
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Step 1, question 2: SSNs valid for the EIC = no, so STOP; can't take the credit; Step 5 not reached"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached; stopped at Step 1, question 2"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached; stopped at Step 1, question 2"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached; stopped at Step 1, question 2"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached; stopped at Step 1, question 2"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used; stopped at Step 1, question 2"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used; stopped at Step 1, question 2"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1, question 2"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1, question 2"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1, question 2"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1, question 2"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1, question 2"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "No EIC: Step 1 Q1 passes ($32,039 < $57,554), Q2 = no, so STOP and check the box on line 27c"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Not reached: no qualifying child, so Step 3 goes to Step 4; Step 4 Q1 married with head of household status = STOP before Step 5"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached: Step 4 Q1 STOP, can't take the credit"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached: Step 4 Q1 STOP, can't take the credit"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached: Step 4 Q1 STOP, can't take the credit"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached: Step 4 Q1 STOP, can't take the credit"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used: Step 4 Q1 STOP came first"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used: Step 4 Q1 STOP came first"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached: Step 4 Q1 STOP came first"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached: Step 4 Q1 STOP came first"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached: Step 4 Q1 STOP came first"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached: Step 4 Q1 STOP came first"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached: Step 4 Q1 STOP came first"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "No credit: married at end of 2025, filing head of household, no qualifying child; Step 4 Q1 says can't take the credit"
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Not reached: no qualifying children and Step 1 Q1 line 11b $50,354 is not less than $19,104, so STOP"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached: STOP at Step 1 Q1"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached: STOP at Step 1 Q1"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached: STOP at Step 1 Q1"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached: STOP at Step 1 Q1"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used: STOP at Step 1 Q1; no Schedule C or SE and Worksheet B Parts 1 and 2 are $0"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used: STOP at Step 1 Q1"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1 Q1"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1 Q1"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1 Q1"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1 Q1"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1 Q1"
  - printed: "6 (eic.line6)"
    value: "blank"
    work: "You can't take the credit: $50,354 is not less than the $19,104 limit for Single with no children, so no EIC is figured"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "25118.00"
    work: "Form 1040 line 1z = 25,118.00; Steps 1-3 passed (AGI under 50,434, investment income 0, separate residence last 6 months, not a qualifying child of another)"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "25118.00"
    work: "25,118.00 - 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "25118.00"
    work: "25,118.00 + 0.00; less than 50,434 with 1 qualifying child"
  - printed: "4b"
    value: "blank"
    work: "Step 5 question 2 is No (no self-employment), so Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Step 5 question 2 is No (no self-employment), so Worksheet B is not used"
  - printed: "1"
    value: "25118.00"
    work: "Worksheet A line 1 = Step 5 line 5 = 25,118.00"
  - printed: "2"
    value: "4044.00"
    work: "EIC Table row 25,100-25,150, starred single/HOH/MFS column, 1 child = 4,044"
  - printed: "3"
    value: "23618.00"
    work: "Form 1040 line 11b = 23,618.00"
  - printed: "4"
    value: "no"
    work: "23,618.00 is not equal to 25,118.00; go to line 5"
  - printed: "5"
    value: "4284.00"
    work: "23,618 is not less than 23,350; EIC Table row 23,600-23,650, starred column, 1 child = 4,284"
  - printed: "6 (eic.line6)"
    value: "4044.00"
    work: "Smaller of line 5 (4,284) and line 2 (4,044) = 4,044"
```
```
