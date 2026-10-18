# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 10 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 7878d00f6f4a9bad40fb6e0db79fbcce424f5c9f14b595f429e24d938c532c4f; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

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

### case classm.eic.2 — prompt sha256 744cbdd4ac3403910ffc43574a6f470e120f4d7c9b8c9e19025bcc79e6fa3996; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $64,140.00
Model: $0.00
Work: Not reached: STOP at line 2 because line 2 is zero.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 f0a62d0601b36ec6f41b62506d9aedd2d3987455014fa0e20c0f0d0c4758fdb3; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:false, eic.line1_table#2, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#2, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.separated_box:false, eic.clergy:false

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
Work: Not reached: the worksheet stopped at line 2 because line 2 is zero

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $10.00
Model: $0.00
Work: Not reached: the worksheet stopped at line 2 because line 2 is zero

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.3 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.4 — prompt sha256 58fe6f9f1583fd46f8e8eac518ee6d95f174c526199ddd6899af227b5702526a; branches: eic.qc_of_another:true, eic.born_before_2001:false, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $45,880.00
Model: $0.00
Work: Step 1 Q1: no qualifying children with valid SSNs and line 11b $45,880 is not less than $19,104, so STOP; the worksheet is not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $45,880.00
Model: $0.00
Work: Not reached; the Step 1 STOP means you can't take the credit

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **DISAGREE**

Project: yes
Model: no
Work: Not reached; the Step 1 STOP means you can't take the credit

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 32251b66276517399b142ab9a0c0c16d4d78c835969a8a619bdba0131bc2df4a; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:false, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $66,499.00
Model: $0.00
Work: Blank. Step 1 Q1 says STOP: with no qualifying children, line 11b ($66,558) is not under $26,214 (MFJ). Q2 also says STOP because there is no valid SSN. Worksheet A is not reached.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $66,558.00
Model: $0.00
Work: Blank. The Step 1 STOP means you can't take the credit.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 9072f2885df5f7f803374c80e5398a7d98c54a8c883cf0617d83fa10b92a5c57; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:false, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:false, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.6 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $33,401.00
Model: $0.00
Work: Step 1 Q1: 0 qualifying children with valid SSNs and line 11b $33,704 is not under $19,104; STOP, worksheet not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $33,704.00
Model: $0.00
Work: Not reached; Step 1 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 50700bd71c2c0b237e053b22cff2eb006cfdfd496cd963d4fe2ad1e27f4fa559; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:false, eic.us_home:false, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $25,428.00
Model: $0.00
Work: Step 1 Q1: no children with valid SSNs and line 11b $25,686 is not less than $19,104, so STOP; Worksheet A is not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $25,686.00
Model: $0.00
Work: Not reached; the credit is barred at Step 1 Q1

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.8 — prompt sha256 548e302b6fdc2b72b589ebc3b43522490914016307dde7d0c3f70e092a4fc354; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:true, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.clergy:false

### classm.eic.8 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $10,723.00
Model: $0.00
Work: Step 1 Q3: filing Form 2555 = yes, so STOP, you can't take the credit; Worksheet A is not completed

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $3,647.00
Model: $0.00
Work: Not reached: credit barred at Step 1 Q3 (Form 2555)

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $20,673.00
Model: $0.00
Work: Not reached: credit barred at Step 1 Q3 (Form 2555)

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $4,328.00
Model: $0.00
Work: Not reached: credit barred at Step 1 Q3 (Form 2555)

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.8 — 6 — This is your earned income credit
Status: **DISAGREE**

Project: $3,647.00
Model: $0.00
Work: No EIC allowed because the filer is filing Form 2555; nothing is entered on Form 1040 line 27a

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### case classm.eic.9 — prompt sha256 f440a3892deba0e60a063c73e4f2f8c822e60b588262db20f1364fe98a0e1ac4; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#2, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.separated_box:true, eic.clergy:false

### classm.eic.9 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $44,084.00

### classm.eic.9 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $2,787.00

### classm.eic.9 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $44,084.00

### classm.eic.9 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.9 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $2,787.00
Model: $0.00
Work: Skipped because line 4 is yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.9 — 6 — This is your earned income credit
Status: **AGREE**

Value: $2,787.00

### case classm.eic.10 — prompt sha256 eb64e867e2d407080fa55d34663f43a530f786ccf1f8f2d0835b822d00cbb915; branches: eic.qc_of_another:true, eic.born_before_2001:true, eic.born_after_1960:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.separated_box:false, eic.clergy:false

### classm.eic.10 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $48,342.00
Model: $0.00
Work: Not reached: Step 1 Q1, no child with valid SSN and line 11b $48,598 is not less than $19,104, so STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.10 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.10 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $48,598.00
Model: $0.00
Work: Not reached: Step 1 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; where the model fills line 6 it agrees with the project, and where a step stops (for example Form 2555 at Step 1, question 3) the project's line 6 is figured but Form 1040 line 27a is zero or refused. [dropped]

### classm.eic.10 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.10 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.10 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

```yaml
lines:
  - printed: "1"
    value: "32936.00"
    work: "Step 5 worksheet: line 1z $32,936 - $0 Medicaid waiver payments + $0 combat pay = $32,936"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row $32,900–$32,950, head of household column, 1 qualifying child with a valid SSN (dep_c) = $2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040, line 11b = $32,936"
  - printed: "4"
    value: "yes"
    work: "Line 3 $32,936 equals line 1 $32,936; skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "6"
    value: "2798.00"
    work: "Amount from line 2 = $2,798"
```

### classm.eic.2

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5 worksheet: 1040 line 1z $0 - $0 Medicaid waiver + $0 combat pay = $0. Note: you can't take the credit. Step 1 Q1 stops it: no children with valid SSNs and AGI $64,140 is not under $19,104. Step 2 also stops it: investment income $0+$0+$51,989+$12,151 = $64,140, over $11,950, with no Form 4797. Step 4 Q1 stops it too because the status is married filing separately."
  - printed: "2"
    value: "0.00"
    work: "EIC Table, single/HOH/QSS★ column (used for married filing separately), 0 children: $0 is below the first $1 row, so the credit is $0. Line 2 is zero, so STOP; check box 27c."
  - printed: "3"
    value: "blank"
    work: "Not reached: STOP at line 2 because line 2 is zero."
  - printed: "4"
    value: "blank"
    work: "Not reached: STOP at line 2 because line 2 is zero."
  - printed: "5"
    value: "blank"
    work: "Not reached: STOP at line 2 because line 2 is zero."
  - printed: "6"
    value: "0.00"
    work: "Not eligible (STOP at Step 1, Step 2, Step 4 and worksheet line 2), so the earned income credit is $0. Enter $0 on 1040 line 27a and check box 27c."
```

### classm.eic.3

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5 worksheet: line 1z 0.00 − Medicaid waiver 0.00 + nontaxable combat pay 0.00 = 0.00 earned income"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, Single, 2 qualifying children with valid SSNs (dep_a, dep_c): $0 is below the first row ($1–$50), so credit = 0; line 2 is zero, so STOP: you can't take the credit; check box 27c"
  - printed: "3"
    value: "blank"
    work: "Not reached: the worksheet stopped at line 2 because line 2 is zero"
  - printed: "4"
    value: "blank"
    work: "Not reached: the worksheet stopped at line 2 because line 2 is zero"
  - printed: "5"
    value: "blank"
    work: "Not reached: the worksheet stopped at line 2 because line 2 is zero"
  - printed: "6"
    value: "0.00"
    work: "Line 2 is zero, so no credit is allowed and the earned income credit is 0.00"
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children with valid SSNs and line 11b $45,880 is not less than $19,104, so STOP; the worksheet is not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; the Step 1 STOP means you can't take the credit"
  - printed: "3"
    value: "blank"
    work: "Not reached; the Step 1 STOP means you can't take the credit"
  - printed: "4"
    value: "blank"
    work: "Not reached; the Step 1 STOP means you can't take the credit"
  - printed: "5"
    value: "blank"
    work: "Not reached; the Step 1 STOP means you can't take the credit"
  - printed: "6"
    value: "0.00"
    work: "No EIC allowed (Step 1 STOP; Step 4 Q2 and Q5 would also STOP), so the credit is $0"
```
```

### classm.eic.5

```yaml
lines:
  - printed: "1"
    value: ""
    work: "Blank. Step 1 Q1 says STOP: with no qualifying children, line 11b ($66,558) is not under $26,214 (MFJ). Q2 also says STOP because there is no valid SSN. Worksheet A is not reached."
  - printed: "2"
    value: ""
    work: "Blank. The Step 1 STOP means you can't take the credit, so there is no table lookup."
  - printed: "3"
    value: ""
    work: "Blank. The Step 1 STOP means you can't take the credit."
  - printed: "4"
    value: ""
    work: "Blank. The Step 1 STOP means you can't take the credit."
  - printed: "5"
    value: ""
    work: "Blank. The Step 1 STOP means you can't take the credit."
  - printed: "6"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP on line 11b and on SSN; check box 27c), so the earned income credit is $0."
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: 0 qualifying children with valid SSNs and line 11b $33,704 is not under $19,104; STOP, worksheet not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; Step 1 STOP (also no valid SSN at Q2 and filing Form 2555 at Q3)"
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
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP); EIC = 0"
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no children with valid SSNs and line 11b $25,686 is not less than $19,104, so STOP; Worksheet A is not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; the credit is barred at Step 1 Q1"
  - printed: "3"
    value: "blank"
    work: "Not reached; the credit is barred at Step 1 Q1"
  - printed: "4"
    value: "blank"
    work: "Not reached; the credit is barred at Step 1 Q1"
  - printed: "5"
    value: "blank"
    work: "Not reached; the credit is barred at Step 1 Q1"
  - printed: "6"
    value: "blank"
    work: "Not reached; no EIC is allowed (Step 4 Q3, main home not in the U.S., would also STOP)"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q3: filing Form 2555 = yes, so STOP, you can't take the credit; Worksheet A is not completed"
  - printed: "2"
    value: "blank"
    work: "Not reached: credit barred at Step 1 Q3 (Form 2555)"
  - printed: "3"
    value: "blank"
    work: "Not reached: credit barred at Step 1 Q3 (Form 2555)"
  - printed: "4"
    value: "blank"
    work: "Not reached: credit barred at Step 1 Q3 (Form 2555)"
  - printed: "5"
    value: "blank"
    work: "Not reached: credit barred at Step 1 Q3 (Form 2555)"
  - printed: "6"
    value: "blank"
    work: "No EIC allowed because the filer is filing Form 2555; nothing is entered on Form 1040 line 27a"
```
```

### classm.eic.9

```yaml
```yaml
lines:
  - printed: "1"
    value: "44084.00"
    work: "Step 5 earned income = Form 1040 line 1z 44,084.00 - 0 Medicaid waiver + 0 combat pay"
  - printed: "2"
    value: "2787.00"
    work: "EIC Table row 44,050-44,100, Single/HOH/QSS★ column (used for MFS), 2 children with valid SSNs (dep_b, dep_c) = 2,787"
  - printed: "3"
    value: "44084.00"
    work: "Form 1040 line 11b = 44,084.00"
  - printed: "4"
    value: "yes"
    work: "Line 3 44,084 = line 1 44,084, so skip line 5 and enter the line 2 amount on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is yes"
  - printed: "6"
    value: "2787.00"
    work: "Amount from line 2 = 2,787"
```
```

### classm.eic.10

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Not reached: Step 1 Q1, no child with valid SSN and line 11b $48,598 is not less than $19,104, so STOP"
  - printed: "2"
    value: "blank"
    work: "Not reached: Step 1 STOP, you can't take the credit (Step 4 Q5 would also STOP)"
  - printed: "3"
    value: "blank"
    work: "Not reached: Step 1 STOP"
  - printed: "4"
    value: "blank"
    work: "Not reached: Step 1 STOP"
  - printed: "5"
    value: "blank"
    work: "Not reached: Step 1 STOP"
  - printed: "6"
    value: "0.00"
    work: "Not eligible under Step 1 STOP, so earned income credit is $0"
```
```
