# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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
Work: Not self-employed, clergy, church employee or statutory employee; Step 5 Q2 No, so use Worksheet A and leave Worksheet B blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

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
Status: **MISSING**

Project: $31,939.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 1)" and asks for the whole handle exactly as given; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is blank: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit." That is the source reading (i1040gi p. 40, Step 1, question 1, with no qualifying child: "less than $19,104 ($26,214 if married filing jointly)? ... No. STOP"). The project's value is $31,939.00 (eic.reached_step5 false, eic.credit $0.00): the Step 5 helper lines are figured and shown on a return that never reaches Step 5, the open T-067 (BUG-0151; shown_when does not apply to helpers). Not a new finding, and the credit is $0.00 on both sides. Dropped: a line the flow chart never reaches is not evidence for the fixture. [dropped]

### classm.eic.2 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 2)" and asks for the whole handle exactly as given; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is blank: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit." That is the source reading (i1040gi p. 40, Step 1, question 1, with no qualifying child: "less than $19,104 ($26,214 if married filing jointly)? ... No. STOP"). The project's value is $0.00 (eic.reached_step5 false, eic.credit $0.00): the Step 5 helper lines are figured and shown on a return that never reaches Step 5, the open T-067 (BUG-0151; shown_when does not apply to helpers). Not a new finding, and the credit is $0.00 on both sides. Dropped: a line the flow chart never reaches is not evidence for the fixture. [dropped]

### classm.eic.2 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $31,939.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 3)" and asks for the whole handle exactly as given; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is blank: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit." That is the source reading (i1040gi p. 40, Step 1, question 1, with no qualifying child: "less than $19,104 ($26,214 if married filing jointly)? ... No. STOP"). The project's value is $31,939.00 (eic.reached_step5 false, eic.credit $0.00): the Step 5 helper lines are figured and shown on a return that never reaches Step 5, the open T-067 (BUG-0151; shown_when does not apply to helpers). Not a new finding, and the credit is $0.00 on both sides. Dropped: a line the flow chart never reaches is not evidence for the fixture. [dropped]

### classm.eic.2 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 4)" and asks for the whole handle exactly as given; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is blank: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit." That is the source reading (i1040gi p. 40, Step 1, question 1, with no qualifying child: "less than $19,104 ($26,214 if married filing jointly)? ... No. STOP"). The project's value is $0.00 (eic.reached_step5 false, eic.credit $0.00): the Step 5 helper lines are figured and shown on a return that never reaches Step 5, the open T-067 (BUG-0151; shown_when does not apply to helpers). Not a new finding, and the credit is $0.00 on both sides. Dropped: a line the flow chart never reaches is not evidence for the fixture. [dropped]

### classm.eic.2 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $31,939.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 5)" and asks for the whole handle exactly as given; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is blank: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit." That is the source reading (i1040gi p. 40, Step 1, question 1, with no qualifying child: "less than $19,104 ($26,214 if married filing jointly)? ... No. STOP"). The project's value is $31,939.00 (eic.reached_step5 false, eic.credit $0.00): the Step 5 helper lines are figured and shown on a return that never reaches Step 5, the open T-067 (BUG-0151; shown_when does not apply to helpers). Not a new finding, and the credit is $0.00 on both sides. Dropped: a line the flow chart never reaches is not evidence for the fixture. [dropped]

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; the credit was disallowed at Step 1.

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

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
Work: Line 4 is yes, so skip line 5

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.3 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $4,910.00

### case classm.eic.4 — prompt sha256 60f126faf7f84feb08c9618673a18384791c153959f8fc9e826973677100a2c0; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#4, eic.line5_blank:true, eic.show5:false, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.4 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.4.prompt.txt) lists the line as "line (Step 5, 1)" and asks for the whole handle exactly as given; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $5,137.00 ("Form 1040 line 1z = 5,137.00"; Medicaid waiver payments and combat pay zero in this tool); the project's is $5,137.00. They are equal, and Step 5 is reached (eic.reached_step5 true, eic.credit $1,743.00, which the reply's line 6 agrees with), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.4 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.4.prompt.txt) lists the line as "line (Step 5, 2)" and asks for the whole handle exactly as given; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 ("Form 1040 line 1z = 5,137.00"; Medicaid waiver payments and combat pay zero in this tool); the project's is $0.00. They are equal, and Step 5 is reached (eic.reached_step5 true, eic.credit $1,743.00, which the reply's line 6 agrees with), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.4 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.4.prompt.txt) lists the line as "line (Step 5, 3)" and asks for the whole handle exactly as given; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $5,137.00 ("Form 1040 line 1z = 5,137.00"; Medicaid waiver payments and combat pay zero in this tool); the project's is $5,137.00. They are equal, and Step 5 is reached (eic.reached_step5 true, eic.credit $1,743.00, which the reply's line 6 agrees with), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.4 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.4.prompt.txt) lists the line as "line (Step 5, 4)" and asks for the whole handle exactly as given; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 ("Form 1040 line 1z = 5,137.00"; Medicaid waiver payments and combat pay zero in this tool); the project's is $0.00. They are equal, and Step 5 is reached (eic.reached_step5 true, eic.credit $1,743.00, which the reply's line 6 agrees with), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.4 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.4.prompt.txt) lists the line as "line (Step 5, 5)" and asks for the whole handle exactly as given; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $5,137.00 ("Form 1040 line 1z = 5,137.00"; Medicaid waiver payments and combat pay zero in this tool); the project's is $5,137.00. They are equal, and Step 5 is reached (eic.reached_step5 true, eic.credit $1,743.00, which the reply's line 6 agrees with), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not self-employed, no clergy/church/statutory income; Step 5 Q2 answer is No, so use Worksheet A and leave Worksheet B blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used

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
Work: 1 qualifying child; line 3 of 16,019 is less than 23,350, so leave line 5 blank and enter line 2 on line 6

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $1,743.00

### case classm.eic.5 — prompt sha256 56c6a40aa252e36592aa4bad3f25cbcf397a3581342f61224073148dc0d63b81; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#1, eic.step1_income:true, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:false, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:true, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2: SSNs not valid for EIC -> STOP, can't take the credit; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1 Q2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **DISAGREE**

Project: $4,080.00
Model: $0.00
Work: No valid SSNs for EIC -> can't take the credit (check box 27c); EIC = 0

Ruling: representation; project retained; model value dropped from the fixture. i1040gi p. 40, Step 1, question 2: "Do you, and your spouse if filing a joint return, have a valid SSN? ... No. STOP You can't take the credit." The case has no valid SSN for the EIC (eic.step1_ssn false, eic.eligible false); the reply stops there and enters $0.00 ("No valid SSNs for EIC -> can't take the credit (check box 27c); EIC = 0"), its other Worksheet A lines blank. The project hides Worksheet A line 6 (shown_when eic.eligible, false), the credit eic.credit is $0.00 and line 27c is checked (eic.check_27c true), so both sides file no credit. The $4,080.00 in the log is the hidden line's internal value, compared because the class M fill of a non-collection document ignores shown_when (T-079 (1)). Not caused by the BUG-0195 wording (eic.us_home is Yes on this case). Dropped: a hidden line's internal value is not evidence. [dropped]

### case classm.eic.6 — prompt sha256 1dc893df8ef83d795e0dca51d4cd3b3b1ea02a033207b76d21fc7f738d89adef; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.6 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.6.prompt.txt) lists the line as "line (Step 5, 1)" and asks for the whole handle exactly as given; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 (Form 1040 line 1z $0.00); the project's is $0.00. They are equal. The return is refused (sa.excluded_income, excluded foreign or possession income; i1040gi p. 40, Step 1, question 3, "Are you filing Form 2555?"), and eic.us_home, the BUG-0195 question, is answered No here, which does not enter these lines. Nothing to drop: the values agree and neither side shows a nonzero amount.

### classm.eic.6 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.6.prompt.txt) lists the line as "line (Step 5, 2)" and asks for the whole handle exactly as given; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 (Form 1040 line 1z $0.00); the project's is $0.00. They are equal. The return is refused (sa.excluded_income, excluded foreign or possession income; i1040gi p. 40, Step 1, question 3, "Are you filing Form 2555?"), and eic.us_home, the BUG-0195 question, is answered No here, which does not enter these lines. Nothing to drop: the values agree and neither side shows a nonzero amount.

### classm.eic.6 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.6.prompt.txt) lists the line as "line (Step 5, 3)" and asks for the whole handle exactly as given; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 (Form 1040 line 1z $0.00); the project's is $0.00. They are equal. The return is refused (sa.excluded_income, excluded foreign or possession income; i1040gi p. 40, Step 1, question 3, "Are you filing Form 2555?"), and eic.us_home, the BUG-0195 question, is answered No here, which does not enter these lines. Nothing to drop: the values agree and neither side shows a nonzero amount.

### classm.eic.6 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.6.prompt.txt) lists the line as "line (Step 5, 4)" and asks for the whole handle exactly as given; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 (Form 1040 line 1z $0.00); the project's is $0.00. They are equal. The return is refused (sa.excluded_income, excluded foreign or possession income; i1040gi p. 40, Step 1, question 3, "Are you filing Form 2555?"), and eic.us_home, the BUG-0195 question, is answered No here, which does not enter these lines. Nothing to drop: the values agree and neither side shows a nonzero amount.

### classm.eic.6 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading (T-070 (1)). The prompt (.classm/classm.eic.6.prompt.txt) lists the line as "line (Step 5, 5)" and asks for the whole handle exactly as given; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading "line " before matching, and the log records no answer (the replies for classm.eic.1, .3, .5 and .8 write "(Step 5, n)" and classm.eic.7 "line (Step 5, n)", and were read). The reply's value is $0.00 (Form 1040 line 1z $0.00); the project's is $0.00. They are equal. The return is refused (sa.excluded_income, excluded foreign or possession income; i1040gi p. 40, Step 1, question 3, "Are you filing Form 2555?"), and eic.us_home, the BUG-0195 question, is answered No here, which does not enter these lines. Nothing to drop: the values agree and neither side shows a nonzero amount.

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not self-employed, so Step 5 Q2 is No; Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Line 2 is zero, STOP; not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Line 2 is zero, STOP; not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Line 2 is zero, STOP; not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 30c2ed71b94888cb0249caf897533d8328f99392f3feaa8f9554a46e0a5f91c2; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q1: no children with valid SSNs; line 11b $50,354 is not less than $19,104, so STOP and Step 5 is never reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used: not self-employed, and stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

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
Work: Not self-employed, so Step 5 Q2 = No; use Worksheet A and leave Worksheet B blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used; blank

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
    work: "No Medicaid waiver payments excluded (zero in this tool)"
  - printed: "(Step 5, 3)"
    value: "32936.00"
    work: "32,936.00 - 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected (zero in this tool)"
  - printed: "(Step 5, 5)"
    value: "32936.00"
    work: "32,936.00 + 0.00 = earned income"
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, clergy, church employee or statutory employee; Step 5 Q2 No, so use Worksheet A and leave Worksheet B blank"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used"
  - printed: "1"
    value: "32936.00"
    work: "Worksheet A line 1 = Step 5 earned income 32,936.00"
  - printed: "2"
    value: "2798.00"
    work: "EIC Table row 32,900-32,950, HOH column, 1 child with valid SSN (dep_c) = 2,798"
  - printed: "3"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936.00"
  - printed: "4"
    value: "yes"
    work: "Line 3 32,936 = line 1 32,936; skip line 5 and enter line 2 on line 6"
  - printed: "5"
    value: "blank"
    work: "Skipped because line 4 is Yes"
  - printed: "6 (eic.line6)"
    value: "2798.00"
    work: "Amount from line 2"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "blank"
    work: "Not reached. Step 1 Q1: no qualifying children and line 11b $65,538.15 is not less than $19,104, so STOP, you can't take the credit."
  - printed: "Step 5, 2"
    value: "blank"
    work: "Not reached; the credit was disallowed at Step 1."
  - printed: "Step 5, 3"
    value: "blank"
    work: "Not reached; the credit was disallowed at Step 1."
  - printed: "Step 5, 4"
    value: "blank"
    work: "Not reached; the credit was disallowed at Step 1."
  - printed: "Step 5, 5"
    value: "blank"
    work: "Not reached; the credit was disallowed at Step 1."
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not reached; the credit was disallowed at Step 1."
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not reached; the credit was disallowed at Step 1."
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached; the credit was disallowed at Step 1."
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached; the credit was disallowed at Step 1."
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached; the credit was disallowed at Step 1."
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached; the credit was disallowed at Step 1."
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached; the credit was disallowed at Step 1."
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "No credit. Step 1 STOP (AGI $65,538.15 is at least $19,104 with no children). Step 2 investment income is also over $11,950 (21,941 + 51,204 + 9,641 = $82,786). Step 4 Q1 also stops MFS filers without a qualifying child."
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
    work: "13,709.00 - 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "13709.00"
    work: "13,709.00 + 0.00 = earned income"
  - printed: "4b"
    value: "12259.68"
    work: "Parts 1-2 (Schedule C) -1,449.32 + Part 3 0 + 4a 13,709.00 = 12,259.68"
  - printed: "6 (eic.wsb_6)"
    value: "12259.68"
    work: "Line 4b is positive and below the $57,310 limit (2 children with valid SSNs), so 12,259.68"
  - printed: "1"
    value: "12259.68"
    work: "Self-employed (Schedule C), so use Worksheet B line 6 = 12,259.68"
  - printed: "2"
    value: "4910.00"
    work: "EIC Table row 12,250-12,300, Single column, 2 children with valid SSNs (dep_a, dep_c) = 4,910"
  - printed: "3"
    value: "12259.68"
    work: "Form 1040 line 11b = 12,259.68"
  - printed: "4"
    value: "yes"
    work: "Line 3 (12,259.68) equals line 1 (12,259.68)"
  - printed: "5"
    value: ""
    work: "Line 4 is yes, so skip line 5"
  - printed: "6 (eic.line6)"
    value: "4910.00"
    work: "Line 4 is yes, so enter line 2 = 4,910"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "5137.00"
    work: "Form 1040 line 1z = 5,137.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded on Schedule 1 line 8s; zero in this tool"
  - printed: "Step 5, 3"
    value: "5137.00"
    work: "5,137.00 - 0.00 = 5,137.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "5137.00"
    work: "5,137.00 + 0.00 = 5,137.00 earned income"
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, no clergy/church/statutory income; Step 5 Q2 answer is No, so use Worksheet A and leave Worksheet B blank"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used"
  - printed: "1"
    value: "5137.00"
    work: "Earned income from Step 5, line 5 = 5,137.00"
  - printed: "2"
    value: "1743.00"
    work: "EIC Table row 5,100-5,150, QSS column, 1 child with valid SSN (dep_a) = 1,743"
  - printed: "3"
    value: "16019.00"
    work: "Form 1040 line 11b = 16,019.00"
  - printed: "4"
    value: "no"
    work: "Line 3 (16,019) is not equal to line 1 (5,137); go to line 5"
  - printed: "5"
    value: "blank"
    work: "1 qualifying child; line 3 of 16,019 is less than 23,350, so leave line 5 blank and enter line 2 on line 6"
  - printed: "6 (eic.line6)"
    value: "1743.00"
    work: "Line 6 = line 2 = 1,743.00"
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Step 1 Q2: SSNs not valid for EIC -> STOP, can't take the credit; Step 5 not reached"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached; stopped at Step 1 Q2"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached; stopped at Step 1 Q2"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached; stopped at Step 1 Q2"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached; stopped at Step 1 Q2"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used; stopped at Step 1 Q2"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used; stopped at Step 1 Q2"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1 Q2"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1 Q2"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1 Q2"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1 Q2"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1 Q2"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "No valid SSNs for EIC -> can't take the credit (check box 27c); EIC = 0"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "0.00"
    work: "Form 1040 line 1z = 0.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded in this tool"
  - printed: "Step 5, 3"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected in this tool"
  - printed: "Step 5, 5"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00 earned income"
  - printed: "4b"
    value: ""
    work: "Not self-employed, so Step 5 Q2 is No; Worksheet B not used"
  - printed: "6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used"
  - printed: "1"
    value: "0.00"
    work: "Earned income from Step 5 line 5 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "Disqualified: Form 2555/4563 Yes (Step 1 Q3); married HOH without a qualifying child (Step 4 Q1); also 0 earned income gives 0 credit; STOP"
  - printed: "3"
    value: ""
    work: "Line 2 is zero, STOP; not reached"
  - printed: "4"
    value: ""
    work: "Line 2 is zero, STOP; not reached"
  - printed: "5"
    value: ""
    work: "Line 2 is zero, STOP; not reached"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "No credit allowed; check box on line 27c"
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "line (Step 5, 1)"
    value: "blank"
    work: "Step 1 Q1: no children with valid SSNs; line 11b $50,354 is not less than $19,104, so STOP and Step 5 is never reached"
  - printed: "line (Step 5, 2)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "line (Step 5, 3)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "line (Step 5, 4)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "line (Step 5, 5)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "line 4b"
    value: "blank"
    work: "Worksheet B not used: not self-employed, and stopped at Step 1"
  - printed: "line 6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used"
  - printed: "line 1"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "line 2"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "line 3"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "line 4"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "line 5"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "Step 1 STOP (AGI $50,354 >= $19,104 with no qualifying children): you can't take the credit, so EIC = 0"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "25118.00"
    work: "Form 1040 line 1z = 25,118.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded on Schedule 1 line 8s; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "25118.00"
    work: "25,118.00 - 0.00 = 25,118.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "25118.00"
    work: "25,118.00 + 0.00 = 25,118.00 earned income"
  - printed: "4b"
    value: ""
    work: "Not self-employed, so Step 5 Q2 = No; use Worksheet A and leave Worksheet B blank"
  - printed: "6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used; blank"
  - printed: "1"
    value: "25118.00"
    work: "Earned income from Step 5 line 5 = 25,118.00"
  - printed: "2"
    value: "4044.00"
    work: "EIC Table, Single/HOH/QSS column (used for MFS under the separated-spouse rule), 1 child; 25,100-25,150 row = 4,044"
  - printed: "3"
    value: "23618.00"
    work: "Form 1040 line 11b = 23,618.00"
  - printed: "4"
    value: "no"
    work: "23,618 is not equal to 25,118"
  - printed: "5"
    value: "4284.00"
    work: "1 child and line 3 of 23,618 is not under 23,350; EIC Table 23,600-23,650 row, 1-child column = 4,284"
  - printed: "6 (eic.line6)"
    value: "4044.00"
    work: "Smaller of line 5 (4,284) and line 2 (4,044) = 4,044"
```
```
