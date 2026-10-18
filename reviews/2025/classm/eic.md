# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 16ecb9e54f119685382216d007d7056e527a235a88a34399ef6d5a1331c62e7b; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0

### classm.eic.1 — 1 — Enter your earned income from Step 5
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
Work: Skipped because line 4 is yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.1 — 6 — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 001e04369ffa65fcd8ec2f69120c7cb9512ef773e0fd56d5f62fda7455e57206; branches: eic.qc_of_another:true, eic.born_before_2001:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1

### classm.eic.2 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $5,402.00
Model: $0.00
Work: Left blank because the worksheet stopped at line 2

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $415.00
Model: $0.00
Work: Left blank because the worksheet stopped at line 2

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.2 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 96662bd5189c1df88eb9d1672d7fea6b634c26e42467196982c91ae5735c39b4; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#2, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#2, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.3 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $57,180.00
Model: $0.00
Work: Worksheet A not completed; Step 2 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $28.00
Model: $0.00
Work: Worksheet A not completed; Step 2 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.3 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.4 — prompt sha256 7192d7d8fac4f446d3504ef9802a7d5c4ae6359f368ecb952ab0a0da5c3f1034; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.4 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $61,335.00

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $61,822.00
Model: $0.00
Work: Not reached because of the STOP at line 2.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 99e9918db1fe8e663cec102109b8f75c7599a261d35daa9938b42245a6584b34; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#3, eic.limit_joint#3, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:false, eic.line1_table#3, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#3, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0

### classm.eic.5 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $3,168.00
Model: $0.00
Work: Skipped: worksheet stops at line 2 because line 2 is zero

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $1,429.00
Model: $0.00
Work: Skipped: worksheet stops at line 2 because line 2 is zero

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.5 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 90613bdb44b10c91c178026034822de3c0ce284a87bda0eac1b778a1b1d4d80b; branches: eic.qc_of_another:false, eic.born_before_2001:false, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#1, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.6 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $43,632.00
Model: $0.00
Work: Step 1 Q1: 1 child with valid SSN, MFJ; line 11b 67,962.00 is not less than 57,554, so STOP and the worksheet is not reached. Step 2 also stops: investment income 27,330.00 is over 11,950 and no Form 4797.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $2,226.00
Model: $0.00
Work: Not reached; the Step 1 STOP means no credit.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $67,962.00
Model: $0.00
Work: Not reached; the Step 1 STOP means no credit.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 e2227826472d0381bd97be274e529f8939b71dfcd873da6454db96d4c0242f9a; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0

### classm.eic.7 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $16,548.00

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $197.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $16,548.00

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $197.00
Model: $0.00
Work: Skipped because line 4 is Yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.7 — 6 — This is your earned income credit
Status: **AGREE**

Value: $197.00

### case classm.eic.8 — prompt sha256 48b865c5767127f2202eaca32ff34dcae626d04ff0027ff00eb6cf3c72507091; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:false, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.8 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $61,004.00
Model: $0.00
Work: Not reached; Step 1 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "32936.00"
    work: "Step 5 earned income: Form 1040 line 1z $32,936 - Medicaid waiver $0 + combat pay $0 = $32,936"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, head of household column with 1 qualifying child with a valid SSN (dep_c) = $2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = $32,936"
  - printed: "4"
    value: "yes"
    work: "Line 3 $32,936 equals line 1 $32,936, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is yes"
  - printed: "6"
    value: "2798.00"
    work: "Amount from line 2 = $2,798"
```
```

### classm.eic.2

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 4 Q5 is yes (you could be a qualifying child of another person), so the credit stops there; earned income is Form 1040 line 1z $0 - $0 + $0 = $0"
  - printed: "2"
    value: "0.00"
    work: "$0 is below the table's first row (starts at $1), so the credit is $0; line 2 is zero, so STOP and check the box on line 27c"
  - printed: "3"
    value: ""
    work: "Left blank because the worksheet stopped at line 2"
  - printed: "4"
    value: ""
    work: "Left blank because the worksheet stopped at line 2"
  - printed: "5"
    value: ""
    work: "Left blank because the worksheet stopped at line 2"
  - printed: "6"
    value: "0.00"
    work: "No credit allowed (Step 4 Q5 STOP and line 2 is zero), so the EIC is $0"
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 2: investment income 0 + 7,231 + 0 + 49,949 = 57,180 > 11,950; no Form 4797 → STOP, can't take credit; worksheet not reached"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not completed; Step 2 STOP (investment income over $11,950)"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not completed; Step 2 STOP"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not completed; Step 2 STOP"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not completed; Step 2 STOP"
  - printed: "6"
    value: "blank"
    work: "No EIC allowed: investment income 57,180 exceeds 11,950 and no Form 4797 amount"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "61335.00"
    work: "Step 5 line 1z $61,335 - Medicaid waiver $0 + combat pay $0 = $61,335. Step 1 already failed: no valid SSN, and AGI $61,822 is not under $19,104 with 0 qualifying children with valid SSNs."
  - printed: "2"
    value: "0.00"
    work: "EIC Table, $61,335 row, qualifying surviving spouse, 0 children column = $0. Line 2 is zero, so STOP: no credit; check box 27c."
  - printed: "3"
    value: "blank"
    work: "Not reached because of the STOP at line 2."
  - printed: "4"
    value: "blank"
    work: "Not reached because of the STOP at line 2."
  - printed: "5"
    value: "blank"
    work: "Not reached because of the STOP at line 2."
  - printed: "6"
    value: "0.00"
    work: "Not eligible for the EIC (no valid SSN, income over limit), so the credit is $0."
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5 worksheet: line 1z 0.00 - Medicaid waiver 0 + combat pay 0 = 0.00 earned income"
  - printed: "2"
    value: "0.00"
    work: "EIC Table starts at 'At least 1'; 0.00 earned income gives no credit, so 0. Line 2 is zero, so STOP: you can't take the credit; check box 27c"
  - printed: "3"
    value: "blank"
    work: "Skipped: worksheet stops at line 2 because line 2 is zero"
  - printed: "4"
    value: "blank"
    work: "Skipped: worksheet stops at line 2 because line 2 is zero"
  - printed: "5"
    value: "blank"
    work: "Skipped: worksheet stops at line 2 because line 2 is zero"
  - printed: "6"
    value: "blank"
    work: "Skipped: no EIC allowed because line 2 is zero (STOP)"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: 1 child with valid SSN, MFJ; line 11b 67,962.00 is not less than 57,554, so STOP and the worksheet is not reached. Step 2 also stops: investment income 27,330.00 is over 11,950 and no Form 4797."
  - printed: "2"
    value: "blank"
    work: "Not reached; the Step 1 STOP means no credit."
  - printed: "3"
    value: "blank"
    work: "Not reached; the Step 1 STOP means no credit."
  - printed: "4"
    value: "blank"
    work: "Not reached; the Step 1 STOP means no credit."
  - printed: "5"
    value: "blank"
    work: "Not reached; the Step 1 STOP means no credit."
  - printed: "6"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP), so the EIC is -0-."
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "1"
    value: "16548.00"
    work: "Step 5 earned income: 1040 line 1z 16,548 - Medicaid waiver 0 + combat pay 0 = 16,548"
  - printed: "2"
    value: "197.00"
    work: "EIC Table row 16,500-16,550, Single column, 0 qualifying children with valid SSNs = 197"
  - printed: "3"
    value: "16548.00"
    work: "Form 1040 line 11b = 16,548"
  - printed: "4"
    value: "yes"
    work: "Line 3 16,548 = line 1 16,548, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "6"
    value: "197.00"
    work: "Amount from line 2 = 197"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children with valid SSNs, and line 11b $61,004 is not less than $19,104, so STOP: you can't take the credit; Worksheet A is not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; Step 1 STOP (investment income 0+21,434+42,570+0 = $64,004 > $11,950 also fails Step 2)"
  - printed: "3"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "4"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "5"
    value: "blank"
    work: "Not reached; Step 1 STOP"
  - printed: "6"
    value: "blank"
    work: "No earned income credit; Step 1 STOP: you can't take the credit"
```
```
