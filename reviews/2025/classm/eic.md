# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 9 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 1425fd6045577c0bf462037c27be48a2b9236a48454449d7098e8bef9d1bef69; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1

### classm.eic.1 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $32,936.00
Model: $0.00
Work: Step 1 Q1: no qualifying children with valid SSNs; line 11b $32,936 is not less than $19,104, so STOP, no credit and Worksheet A is not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.1 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.1 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $32,936.00
Model: $0.00
Work: Not reached; Step 1 stopped the credit

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.1 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **DISAGREE**

Project: yes
Model: no
Work: Not reached; Step 1 stopped the credit

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.1 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.1 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.2 — prompt sha256 591a190f61d4b524eec37106b7b28efb19df0e4bdb66c2083411965eb5ecddf0; branches: eic.qc_of_another:true, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:true, eic.step2_other:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#1, eic.line2#1, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1

### classm.eic.2 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $7,052.00
Model: $0.00
Work: Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $2,406.00
Model: $0.00
Work: Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.2 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 db5e20b8652e5c7a7a8276348979bc3bc103abe409d6c9f65b63cae6448a96c7; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#1, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.line5#2, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0

### classm.eic.3 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $38,995.00

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $5,361.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $38,995.00

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $5,361.00
Model: $0.00
Work: Skipped because line 4 is yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.3 — 6 — This is your earned income credit
Status: **AGREE**

Value: $5,361.00

### case classm.eic.4 — prompt sha256 769bb73a70d186197b9e21fbfb9555fc86c589b02f47f3a112ceb09996d8e904; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:false, eic.step2_other:true, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.4 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $7,085.00
Model: $0.00
Work: Step 1 Q1: line 11b $41,178.00 is not less than $19,104 (no qualifying children), so STOP; you can't take the credit. Worksheet A is not reached.

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $541.00
Model: $0.00
Work: Not reached. Step 1 Q2 also stops (no valid SSN), as does Step 2 (investment income $35,593 > $11,950) and Step 4 Q1 (MFS with no qualifying child).

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $41,178.00
Model: $0.00
Work: Not reached; the EIC is disallowed at Step 1.

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

### case classm.eic.5 — prompt sha256 e0ed0564c0fb51a860abe05816c606dd3cd343958ebfcf9a5dc0f23b6f31722f; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#4, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#4, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#4, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.5 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $64,864.00
Model: $0.00
Work: Not reached because of the Step 1 STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.5 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 598a4224ca41a445f60f20ab82845b72bfc39128045186dcc4ca3e2af9c154b9; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:true, eic.married:false, eic.has_qc:true, eic.married_rules:false, eic.top_limit#3, eic.below_top:true, eic.limit_other#3, eic.limit_joint#3, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.step5_income:true, eic.eligible:true, eic.line1_in_table:true, eic.line1_table#3, eic.line2#0, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#3, eic.line5_blank:false, eic.line5#3, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#0

### classm.eic.6 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $36,510.00

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $5,271.00

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $36,510.00

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: yes

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $5,271.00
Model: $0.00
Work: Skipped because line 4 is Yes

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.6 — 6 — This is your earned income credit
Status: **AGREE**

Value: $5,271.00

### case classm.eic.7 — prompt sha256 f99a487434ccadb11bc2c85410bc52ab665008989f97d922ec1782c0f6818b15; branches: eic.qc_of_another:false, eic.born_before_2001:true, eic.us_home:false, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:true, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1

### classm.eic.7 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $50,000.00
Model: $0.00
Work: Step 1 Q1: no qualifying children with valid SSNs, and line 11b $50,000.00 is not less than $19,104 = STOP. You can't take the credit, so Worksheet A is not reached. (Step 4 Q3 would also stop it: main home was not in the U.S. for more than half of 2025.)

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $50,000.00
Model: $0.00
Work: Worksheet not reached because Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **DISAGREE**

Project: yes
Model: no
Work: Worksheet not reached because Step 1 says STOP

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.7 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.8 — prompt sha256 bca3065fa4f40c998c87d6f0afc741251b07559d47c1f267d1f68ad0f8967a84; branches: eic.qc_of_another:true, eic.born_before_2001:true, eic.us_home:true, eic.married:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.step3:false, eic.step4:false, eic.step34:false, eic.step5_income:false, eic.eligible:false, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1

### classm.eic.8 — 1 — Enter your earned income from Step 5
Status: **DISAGREE**

Project: $41,256.00
Model: $0.00
Work: Not reached. Step 1 Q1: line 11b $38,256 is not less than $19,104 (no children with valid SSNs), so STOP; the filer also has no valid SSN (Q2).

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $38,256.00
Model: $0.00
Work: Not reached; the Step 1 STOP means Worksheet A is not completed.

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

### case classm.eic.9 — prompt sha256 bcedadbfa68c4050e54a07704d75662dfb74aa06cb72bcbf0fbe6549c8cfce97; branches: eic.qc_of_another:false, eic.born_before_2001:false, eic.us_home:true, eic.married:false, eic.has_qc:false, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#1, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.step5_income:true, eic.eligible:false, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#1, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#1

### classm.eic.9 — 1 — Enter your earned income from Step 5
Status: **AGREE**

Value: $0.00

### classm.eic.9 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.9 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **DISAGREE**

Project: $15,595.00
Model: $0.00
Work: Line 2 is zero, so STOP; line not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.9 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.9 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $649.00
Model: $0.00
Work: Line 2 is zero, so STOP; line not reached

Ruling: representation; project retained; model value dropped from the fixture. Where the printed steps say STOP (Steps 1 to 5) or line 4 is Yes (line 5 skipped) or line 2 is zero, the model leaves the later Worksheet A lines blank; the project computes every line regardless and applies eligibility in eic.credit, which Form 1040 line 27a reads (zero when a step stops). In an ordinary evaluation the worksheet lines are not reached on an ineligible return; line 6 agrees on every case. [dropped]

### classm.eic.9 — 6 — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children with valid SSNs; line 11b $32,936 is not less than $19,104, so STOP, no credit and Worksheet A is not reached"
  - printed: "2"
    value: "blank"
    work: "Not reached; Step 1 stopped the credit"
  - printed: "3"
    value: "blank"
    work: "Not reached; Step 1 stopped the credit"
  - printed: "4"
    value: "blank"
    work: "Not reached; Step 1 stopped the credit"
  - printed: "5"
    value: "blank"
    work: "Not reached; Step 1 stopped the credit"
  - printed: "6"
    value: "0.00"
    work: "No credit allowed (Step 1 STOP: AGI $32,936 >= $19,104 with 0 qualifying children); EIC = 0"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 3 Q6: filer could be a qualifying child of another person, so STOP; no credit and check box 27c. Worksheet A is not reached."
  - printed: "2"
    value: "blank"
    work: "Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC."
  - printed: "3"
    value: "blank"
    work: "Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC."
  - printed: "4"
    value: "blank"
    work: "Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC."
  - printed: "5"
    value: "blank"
    work: "Not reached: Step 3 Q6 STOP, filer is ineligible for the EIC."
  - printed: "6"
    value: "blank"
    work: "No EIC: Step 3 Q6 answer is yes, so STOP and check box 27c."
```
```

### classm.eic.3

```yaml
lines:
  - printed: "1"
    value: "38995.00"
    work: "Step 5 earned income: Form 1040 line 1z 38,995.00 - Medicaid waiver 0 + combat pay 0 = 38,995.00"
  - printed: "2"
    value: "5361.00"
    work: "EIC Table row 38,950 to 39,000, married filing jointly, 2 children with valid SSNs (dep_a, dep_b; dep_c does not qualify) = 5,361"
  - printed: "3"
    value: "38995.00"
    work: "Form 1040 line 11b = 38,995.00"
  - printed: "4"
    value: "yes"
    work: "Line 3 (38,995.00) equals line 1 (38,995.00), so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is yes"
  - printed: "6"
    value: "5361.00"
    work: "Line 4 is yes, so line 6 = line 2 = 5,361.00"
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: line 11b $41,178.00 is not less than $19,104 (no qualifying children), so STOP; you can't take the credit. Worksheet A is not reached."
  - printed: "2"
    value: "blank"
    work: "Not reached. Step 1 Q2 also stops (no valid SSN), as does Step 2 (investment income $35,593 > $11,950) and Step 4 Q1 (MFS with no qualifying child)."
  - printed: "3"
    value: "blank"
    work: "Not reached; the EIC is disallowed at Step 1."
  - printed: "4"
    value: "blank"
    work: "Not reached; the EIC is disallowed at Step 1."
  - printed: "5"
    value: "blank"
    work: "Not reached; the EIC is disallowed at Step 1."
  - printed: "6"
    value: "0.00"
    work: "No credit allowed (STOP at Step 1); enter -0- on line 27a and check the box on line 27c (no valid SSN)."
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "1"
    value: ""
    work: "Step 1 Q1: no qualifying children with valid SSNs, and line 11b $64,864 is not less than $19,104, so STOP, no credit; worksheet not reached"
  - printed: "2"
    value: ""
    work: "Not reached because of the Step 1 STOP (Step 2 investment income $64,864 > $11,950 would also stop)"
  - printed: "3"
    value: ""
    work: "Not reached because of the Step 1 STOP"
  - printed: "4"
    value: ""
    work: "Not reached because of the Step 1 STOP"
  - printed: "5"
    value: ""
    work: "Not reached because of the Step 1 STOP"
  - printed: "6"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP), so EIC = 0"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "1"
    value: "36510.00"
    work: "Step 5 earned income: line 1z 36,510 - Medicaid waiver 0 + combat pay 0 = 36,510"
  - printed: "2"
    value: "5271.00"
    work: "EIC Table row 36,500-36,550, Single/HOH column, 3 children with valid SSNs = 5,271"
  - printed: "3"
    value: "36510.00"
    work: "Form 1040 line 11b = 36,510"
  - printed: "4"
    value: "yes"
    work: "Line 3 (36,510) equals line 1 (36,510), so skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "6"
    value: "5271.00"
    work: "Line 6 = line 2 = 5,271"
```
```

### classm.eic.7

```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Step 1 Q1: no qualifying children with valid SSNs, and line 11b $50,000.00 is not less than $19,104 = STOP. You can't take the credit, so Worksheet A is not reached. (Step 4 Q3 would also stop it: main home was not in the U.S. for more than half of 2025.)"
  - printed: "2"
    value: "blank"
    work: "Worksheet not reached because Step 1 says STOP (the table also says no credit at $19,104 or more with 0 children)"
  - printed: "3"
    value: "blank"
    work: "Worksheet not reached because Step 1 says STOP"
  - printed: "4"
    value: "blank"
    work: "Worksheet not reached because Step 1 says STOP"
  - printed: "5"
    value: "blank"
    work: "Worksheet not reached because Step 1 says STOP"
  - printed: "6"
    value: "blank"
    work: "Not eligible for the EIC: no credit goes on line 27a"
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "1"
    value: ""
    work: "Not reached. Step 1 Q1: line 11b $38,256 is not less than $19,104 (no children with valid SSNs), so STOP; the filer also has no valid SSN (Q2)."
  - printed: "2"
    value: ""
    work: "Not reached; the Step 1 STOP means Worksheet A is not completed."
  - printed: "3"
    value: ""
    work: "Not reached; the Step 1 STOP means Worksheet A is not completed."
  - printed: "4"
    value: ""
    work: "Not reached; the Step 1 STOP means Worksheet A is not completed."
  - printed: "5"
    value: ""
    work: "Not reached; the Step 1 STOP means Worksheet A is not completed."
  - printed: "6"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP), so the EIC is $0; check the box on line 27c."
```
```

### classm.eic.9

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Step 5: Form 1040 line 1z 0.00 - Medicaid waiver 0 + combat pay 0 = 0.00 earned income"
  - printed: "2"
    value: "0.00"
    work: "EIC Table has no row for $0, so credit is 0. Also not eligible: investment income 0+0+1+15,594 = 15,595 > 11,950 with no Form 4797, and filer under 25 (Step 4 Q2 No). Line 2 zero: STOP"
  - printed: "3"
    value: "blank"
    work: "Line 2 is zero, so STOP; line not reached"
  - printed: "4"
    value: "blank"
    work: "Line 2 is zero, so STOP; line not reached"
  - printed: "5"
    value: "blank"
    work: "Line 2 is zero, so STOP; line not reached"
  - printed: "6"
    value: "0.00"
    work: "Cannot take the credit; EIC is 0 (check box on line 27c)"
```
```
