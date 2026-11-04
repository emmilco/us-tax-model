# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ae5c9f11087bd77489d49692a8d8e463240dc399a2a63de2773d7e097d4f8ceb |
| cases | 8 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 58352fe59ed1faf4275d8128aa73c7c42576e3529dfcfe931e89dafe9ed0a098; branches: eic.qc_of_another:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3_married:true, eic.step3:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

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

### classm.eic.1 — 6 — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 ef8dad459add3a6db98bb535eab03c97f6e58e88baf7d03655e8eec350c36ef6; branches: eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.step3_married:true, eic.reached_step5:false, eic.self_employed:true, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:true, eic.show5:false, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: No qualifying child, so Step 4 applies. Q2: taxpayer was not born after 12/31/1960, so not under 65; STOP, can't take the credit. Also has Schedule C, so Worksheet B, not A. Line 4 not reached.

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.3 — prompt sha256 b027cf131ff71e4e1649a9616c748672ab1321e0816ccceb8a5fda903b5d2daa; branches: eic.married_rules:true, eic.top_limit#2, eic.below_top:false, eic.limit#2, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_other:true, eic.step4:false, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line2#0, eic.show3:false, eic.line4:false, eic.line5_threshold#2, eic.show5:false, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Step 1 Q1: 2 children with valid SSNs; line 11b $270,589 is not less than $57,310, so STOP (can't take the credit) and Worksheet A is not reached

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.4 — prompt sha256 ef9b6a6382b9fe3361789a94f729e8298356187b29d14a191a88f3b6f839c221; branches: eic.qc_of_another:false, eic.died_2025:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:true, eic.show_wsb4b:true, eic.show_wsb6:true, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:true, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:true, eic.show5:false, eic.line5#0, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $11,747.00

### classm.eic.4 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $11,747.00

### classm.eic.4 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $11,747.00

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $-105,303.10

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Skipped because of the STOP at line 2 (zero credit)

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 4bded72165505068291cf9c86c3e2a3a6717f5d67220ab9e0ee551578c2b78c1; branches: eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_other:true, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.5 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $0.00

### classm.eic.5 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.5 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.eic.5 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.5 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 5 Q2 is No (no Schedule C or SE, not self-employed), so Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used; Worksheet A applies

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: STOP at line 2 (credit zero); remaining lines not completed

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: STOP at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: STOP at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 ff83a3baa08999e57921c06bfcadf6c13a4ee1212904f0f6240dcc666757ac3b; branches: eic.married_rules:false, eic.top_limit#0, eic.below_top:false, eic.limit#0, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:false, eic.step2_other:true, eic.step3_married:true, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.eligible:false, eic.line1#0, eic.line1_in_table:false, eic.line2#1, eic.show3:false, eic.line4:false, eic.line5_threshold#0, eic.show5:false, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Step 1 Q1: 3 children with valid SSNs; line 11b $183,500.15 is not less than $61,555 (Single). STOP, you can't take the credit, so Worksheet A is not completed.

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.7 — prompt sha256 62601089a6fd3be69ee7fc1a07d8b8b0e51338adf47bc8516a098c609b27e0d8; branches: eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_other:true, eic.step3_married:true, eic.step3:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:true, eic.show5:false, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.7 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Line 2 is zero: STOP, can't take the credit (check box 27c); line 4 is not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 — This is your earned income credit
Status: **SKIPPED**

Model: blank
Work: Line 2 is zero: STOP; no earned income credit is figured

No numeric assertion or class M credit: the model left this line blank.

### case classm.eic.8 — prompt sha256 fad7364c707f5dbf37f4a1ef3de2768a71c5bf066998f547a2b341e44a2eeccb; branches: eic.qc_of_another:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:true, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

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

### classm.eic.8 — 6 — This is your earned income credit
Status: **AGREE**

Value: $4,044.00

## Raw responses

### classm.eic.1

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "32936.00"
    work: "Form 1040 line 1z = 32,936.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "Medicaid waiver payments excluded = 0"
  - printed: "Step 5, 3"
    value: "32936.00"
    work: "32,936.00 - 0 = 32,936.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "Nontaxable combat pay elected = 0"
  - printed: "Step 5, 5"
    value: "32936.00"
    work: "32,936.00 + 0 = 32,936.00 earned income"
  - printed: "1"
    value: "32936.00"
    work: "Earned income from Step 5, line 5"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, HOH column, 1 child with valid SSN (dep_c) = 2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936.00"
  - printed: "4"
    value: "yes"
    work: "Line 3 32,936.00 = line 1 32,936.00; skip line 5, line 2 goes to line 6"
  - printed: "6"
    value: "2798.00"
    work: "Line 4 is yes, so enter line 2 = 2,798.00"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "4"
    value: "blank"
    work: "No qualifying child, so Step 4 applies. Q2: taxpayer was not born after 12/31/1960, so not under 65; STOP, can't take the credit. Also has Schedule C, so Worksheet B, not A. Line 4 not reached."
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "4"
    value: "blank"
    work: "Step 1 Q1: 2 children with valid SSNs; line 11b $270,589 is not less than $57,310, so STOP (can't take the credit) and Worksheet A is not reached"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "11747.00"
    work: "Form 1040 line 1z = 11,747.00"
  - printed: "line (Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero"
  - printed: "line (Step 5, 3)"
    value: "11747.00"
    work: "11,747.00 - 0.00"
  - printed: "line (Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero"
  - printed: "line (Step 5, 5)"
    value: "11747.00"
    work: "11,747.00 + 0.00; Schedule C filed, so Step 5 Q2 is Yes and Worksheet B is used"
  - printed: "line 4b"
    value: "-105303.10"
    work: "Parts 1-2 (-117,050.10) + line 3 (0) + 4a (11,747.00) = -105,303.10; zero or less, so STOP: no credit"
  - printed: "line 6 (eic.wsb_6)"
    value: "0.00"
    work: "Line 4b is zero or less, so enter 0"
  - printed: "line 1"
    value: "0.00"
    work: "Earned income from Worksheet B line 6 = 0.00"
  - printed: "line 2"
    value: "0.00"
    work: "0 is below the first table row ($1-$50); credit 0; if line 2 is zero, STOP"
  - printed: "line 4"
    value: "blank"
    work: "Skipped because of the STOP at line 2 (zero credit)"
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "No credit allowed (line 4b is 0 or less and line 2 is 0)"
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "0.00"
    work: "Form 1040 line 1z = 0.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "Step 5, 3"
    value: "0.00"
    work: "Line 1 minus line 2: 0.00 - 0.00 = 0.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "0.00"
    work: "Line 3 plus line 4: 0.00 + 0.00 = 0.00, earned income"
  - printed: "4b"
    value: "blank"
    work: "Step 5 Q2 is No (no Schedule C or SE, not self-employed), so Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used; Worksheet A applies"
  - printed: "1"
    value: "0.00"
    work: "Worksheet A line 1 = earned income from Step 5 line 5 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "0.00 is below the table's first row (1-50); HOH, 0 children: credit 0. Line 2 is zero, so STOP; check box 27c"
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
    value: "0.00"
    work: "Can't take the credit (line 2 is zero); EIC = 0.00"
```
```

### classm.eic.6

```yaml
lines:
  - printed: "4"
    value: "blank"
    work: "Step 1 Q1: 3 children with valid SSNs; line 11b $183,500.15 is not less than $61,555 (Single). STOP, you can't take the credit, so Worksheet A is not completed."
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "0.00"
    work: "Form 1040 line 1z = 0.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "Step 5, 3"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00 earned income"
  - printed: "1"
    value: "0.00"
    work: "Earned income from Step 5 line 5 = 0.00 (no Schedule C/SE, so Worksheet A)"
  - printed: "2"
    value: "0.00"
    work: "EIC Table starts at $1; earned income of $0 gives a credit of 0"
  - printed: "4"
    value: ""
    work: "Line 2 is zero: STOP, can't take the credit (check box 27c); line 4 is not reached"
  - printed: "6"
    value: ""
    work: "Line 2 is zero: STOP; no earned income credit is figured"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "25118.00"
    work: "Form 1040 line 1z = 25,118.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "Step 5, 3"
    value: "25118.00"
    work: "25,118.00 - 0.00 = 25,118.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "25118.00"
    work: "25,118.00 + 0.00 = 25,118.00 earned income"
  - printed: "1"
    value: "25118.00"
    work: "Earned income from Step 5, line 5 (Worksheet A: no self-employment)"
  - printed: "2"
    value: "4044.00"
    work: "EIC Table row 25,100-25,150, Single/HOH/QSS (MFS star) column, 1 child with valid SSN (dep_a) = 4,044"
  - printed: "3"
    value: "23618.00"
    work: "Form 1040 line 11b = 23,618.00"
  - printed: "4"
    value: "no"
    work: "23,618.00 is not equal to 25,118.00"
  - printed: "5"
    value: "4284.00"
    work: "1+ child and line 3 23,618 is not less than 23,350; EIC Table row 23,600-23,650, 1 child = 4,284"
  - printed: "6"
    value: "4044.00"
    work: "Smaller of line 5 (4,284) and line 2 (4,044) = 4,044"
```
```
