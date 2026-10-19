# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 8 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 6869aa66d00bb3f48a088227922056db08f299d988fac6910e1bf4b312f14aab; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

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
Work: Skipped because line 4 is Yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.1 — 6 — This is your earned income credit
Status: **AGREE**

Value: $2,798.00

### case classm.eic.2 — prompt sha256 38025bfd5927eba964e03e9df5c5742fcb69e9897f51cc682308175775e46da2; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:false, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $23,500.00
Model: $0.00
Work: Not reached; stopped at Step 1

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 718ff01730cc1c95680d993f5665aba96f63ae21cde9bbfce9679282ee9f7551; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:false, eic.line1_table#2, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#2, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $33.00
Model: $0.00
Work: Not reached because of the STOP at line 2

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $10.00
Model: $0.00
Work: Not reached because of the STOP at line 2

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.3 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.4 — prompt sha256 3d89b98d46d4d5bbafcaf247ccc4f18198d98124ed4fd95e3d962dc6f3a6520e; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $62,208.00
Model: $0.00
Work: Step 1 Q1: no qualifying children; line 11b $61,797 is not less than $19,104, so STOP. You can't take the credit, and the worksheet is not reached.

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $61,797.00
Model: $0.00
Work: Not reached; the flowchart stopped at Step 1.

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 77181f05959d48dfa4afd16f48c92e2fbf5a5d403ff3c907a6d9b7519173b1e0; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $13,054.00
Model: $0.00
Work: Not reached; stopped at Step 2

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $649.00
Model: $0.00
Work: Not reached; stopped at Step 2

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.5 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 b9bf19c69e2d7eaccc7b2e2f5f64d66a326038c55afea80262800001f79442fc; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:false, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.6 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Step 1 Q1: no qualifying children with valid SSNs; line 11b $51,610 is not less than $19,104, so STOP. You can't take the credit and Worksheet A is not reached.

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $51,610.00
Model: $0.00
Work: Worksheet not completed because of the Step 1 STOP.

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **DISAGREE**

Project: yes
Model: no
Work: Worksheet not completed because of the Step 1 STOP.

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 bcc74278c6ec0c4bcf2a63a3047866441694db5ef01c066acbca84c3f17bdf4f; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#2, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.separated_box:true, eic.clergy:false

### classm.eic.7 — 1 — Enter your earned income from Step 5
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
Work: Skipped because line 4 is yes

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.7 — 6 — This is your earned income credit
Status: **AGREE**

Value: $2,787.00

### case classm.eic.8 — prompt sha256 b4901f60aa492e7e4b8bea65c5478420bb68a5ae1041ae89ae1f33966319153f; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.separated_box:false, eic.clergy:false

### classm.eic.8 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $108.00
Model: $0.00
Work: Left blank: the STOP at line 2 ends the worksheet

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $10.00
Model: $0.00
Work: Left blank: the STOP at line 2 ends the worksheet

Ruling: representation; project retained; model value dropped from the fixture. The model leaves Worksheet A lines blank after a STOP (or line 5 when line 4 is Yes); the project figures each line always and the credit reads it only where the worksheet uses it, so line 6 and Form 1040 line 27a are the same (as ruled in Stage 9; i1040gi pp. 40-46). [dropped]

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
    work: "Step 5: line 1z 32,936 - Medicaid waiver 0 + combat pay 0 = 32,936"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, HOH column, 1 qualifying child with valid SSN (dep_c) = 2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936"
  - printed: "4"
    value: "yes"
    work: "Line 3 (32,936) equals line 1 (32,936); skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: ""
    work: "Skipped because line 4 is Yes"
  - printed: "6"
    value: "2798.00"
    work: "Amount from line 2 = 2,798"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no children with valid SSNs; line 11b $23,500 is not less than $19,104 (MFS) -> STOP, can't take the credit; worksheet not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "3"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "4"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "5"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "6"
    value: "blank"
    work: "No EIC; ineligible at Step 1 Q1"
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5: line 1z 0.00 - Medicaid waiver 0.00 + combat pay 0.00 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "Earned income 0 is below the table's first row (at least $1), so credit is 0. Single, 2 qualifying children with valid SSNs (dep_a, dep_c). Line 2 is zero, so STOP: no credit; check box 27c."
  - printed: "3"
    value: "blank"
    work: "Not reached because of the STOP at line 2"
  - printed: "4"
    value: "blank"
    work: "Not reached because of the STOP at line 2"
  - printed: "5"
    value: "blank"
    work: "Not reached because of the STOP at line 2"
  - printed: "6"
    value: "blank"
    work: "Not reached because of the STOP at line 2; no EIC allowed"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children; line 11b $61,797 is not less than $19,104, so STOP. You can't take the credit, and the worksheet is not reached."
  - printed: "2"
    value: "blank"
    work: "Not reached; the flowchart stopped at Step 1 Q1. Step 4 Q5 would also stop it, since the filer could be a qualifying child of another person."
  - printed: "3"
    value: "blank"
    work: "Not reached; the flowchart stopped at Step 1."
  - printed: "4"
    value: "blank"
    work: "Not reached; the flowchart stopped at Step 1."
  - printed: "5"
    value: "blank"
    work: "Not reached; the flowchart stopped at Step 1."
  - printed: "6"
    value: "0.00"
    work: "You can't take the credit (AGI $61,797 is at or above the $19,104 limit for no children), so the EIC is $0."
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 2: investment income 0+0+0+14,303 = 14,303 > 11,950; no Form 4797 (no 4797 amount in line 7a), so STOP, you can't take the credit; Worksheet A not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; stopped at Step 2 question 3 (earned income is also 0, line 1z = 0)"
  - printed: "3"
    value: "blank"
    work: "Not reached; stopped at Step 2"
  - printed: "4"
    value: "blank"
    work: "Not reached; stopped at Step 2"
  - printed: "5"
    value: "blank"
    work: "Not reached; stopped at Step 2"
  - printed: "6"
    value: "0.00"
    work: "Not eligible: investment income 14,303 > 11,950 and no Form 4797; EIC = 0 (check box on line 27c only if you choose not to claim)"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children with valid SSNs; line 11b $51,610 is not less than $19,104, so STOP. You can't take the credit and Worksheet A is not reached."
  - printed: "2"
    value: "blank"
    work: "Worksheet not completed because of the Step 1 STOP."
  - printed: "3"
    value: "blank"
    work: "Worksheet not completed because of the Step 1 STOP."
  - printed: "4"
    value: "blank"
    work: "Worksheet not completed because of the Step 1 STOP."
  - printed: "5"
    value: "blank"
    work: "Worksheet not completed because of the Step 1 STOP."
  - printed: "6"
    value: "blank"
    work: "No EIC. Step 1 STOP (AGI $51,610 >= $19,104 with 0 children); Step 4 Q3 main home not in U.S. would also STOP."
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "1"
    value: "44084.00"
    work: "Step 5: line 1z 44,084 - Medicaid waiver 0 + combat pay 0 = 44,084"
  - printed: "2"
    value: "2787.00"
    work: "EIC Table row 44,050-44,100, MFS (starred single/HOH column), 2 children with valid SSNs (dep_b, dep_c) = 2,787"
  - printed: "3"
    value: "44084.00"
    work: "Form 1040 line 11b = 44,084"
  - printed: "4"
    value: "yes"
    work: "Line 3 44,084 = line 1 44,084, so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: ""
    work: "Skipped because line 4 is yes"
  - printed: "6"
    value: "2787.00"
    work: "Line 6 = line 2 = 2,787"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5 earned income: Form 1040 line 1z $0.00 - Medicaid waiver $0 + combat pay $0 = $0.00"
  - printed: "2"
    value: "0.00"
    work: "$0 is below the first EIC Table row ($1-$50), so the credit is $0 (Single, 0 children with valid SSNs); line 2 is zero, so STOP and check box 27c"
  - printed: "3"
    value: ""
    work: "Left blank: the STOP at line 2 ends the worksheet"
  - printed: "4"
    value: ""
    work: "Left blank: the STOP at line 2 ends the worksheet"
  - printed: "5"
    value: ""
    work: "Left blank: the STOP at line 2 ends the worksheet"
  - printed: "6"
    value: ""
    work: "Left blank: the STOP at line 2 means no earned income credit can be taken"
```
```
