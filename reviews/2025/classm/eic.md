# Class M hand-work — eic

`Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d8cd1e7cfda63ac5ad42f4c11c90f6933c451f95a3d0ca28d3bfc1891171479f |
| cases | 9 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.eic.1 — prompt sha256 97dc9e2a135a1c89f40f551096e35a9f649327e3cae46c4250ab400f41f06f52; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#4, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#4, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:true, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#4, eic.line5_blank:true, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.1 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.1.prompt.txt) lists the line as "line (Step 5, 1)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 1)" and were read). The reply's value is $5,137.00 (Form 1040 line 1z); the project's is $5,137.00. They are equal, and Step 5 is reached on this return (eic.reached_step5 true; Worksheet A line 1 $5,137.00 agrees), so no project defect. No expectation is recorded for a line without a parsed answer; nothing to drop.

### classm.eic.1 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.1.prompt.txt) lists the line as "line (Step 5, 2)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 2)" and were read). The reply's value is $0.00 (no Medicaid waiver payments); the project's is $0.00. They are equal, and Step 5 is reached on this return (eic.reached_step5 true; Worksheet A line 1 $5,137.00 agrees), so no project defect. No expectation is recorded for a line without a parsed answer; nothing to drop.

### classm.eic.1 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.1.prompt.txt) lists the line as "line (Step 5, 3)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 3)" and were read). The reply's value is $5,137.00 (line 1 minus line 2); the project's is $5,137.00. They are equal, and Step 5 is reached on this return (eic.reached_step5 true; Worksheet A line 1 $5,137.00 agrees), so no project defect. No expectation is recorded for a line without a parsed answer; nothing to drop.

### classm.eic.1 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.1.prompt.txt) lists the line as "line (Step 5, 4)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 4)" and were read). The reply's value is $0.00 (no combat pay elected); the project's is $0.00. They are equal, and Step 5 is reached on this return (eic.reached_step5 true; Worksheet A line 1 $5,137.00 agrees), so no project defect. No expectation is recorded for a line without a parsed answer; nothing to drop.

### classm.eic.1 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $5,137.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.1.prompt.txt) lists the line as "line (Step 5, 5)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 5)" and were read). The reply's value is $5,137.00 (lines 3 plus 4); the project's is $5,137.00. They are equal, and Step 5 is reached on this return (eic.reached_step5 true; Worksheet A line 1 $5,137.00 agrees), so no project defect. No expectation is recorded for a line without a parsed answer; nothing to drop.

### classm.eic.1 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Not self-employed, so Step 5 question 2 is No; use Worksheet A, and Worksheet B is not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used

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
Work: Has 1 or more qualifying children and line 3 (2,137) is less than 23,350, so leave line 5 blank

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.1 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $1,743.00

### case classm.eic.2 — prompt sha256 fd48df5c8feb2f35b2eb4cef190385ed09d56334df50ea0eab262f186078569d; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:false, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#2, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:positive, eic.step2_income:false, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:true, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:false, eic.line1#1, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#2, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.2 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 1)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 1)" and were read). The reply's value is blank ("Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"); the project's is $0.00. The reply's blank is right: i1040gi p. 40, Step 1, question 1, "No children who have valid SSNs lived with you, is the amount on Form 1040 or 1040-SR, line 11b, less than $19,104 ...? No. STOP" (eic.reached_step5 false). The project's Step 5 lines are helpers that shown_when cannot hide (TASKS T-067), but every one is $0.00 here, which the skipped-line rule permits; no finding. Nothing to drop.

### classm.eic.2 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 2)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 2)" and were read). The reply's value is blank ("Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"); the project's is $0.00. The reply's blank is right: i1040gi p. 40, Step 1, question 1, "No children who have valid SSNs lived with you, is the amount on Form 1040 or 1040-SR, line 11b, less than $19,104 ...? No. STOP" (eic.reached_step5 false). The project's Step 5 lines are helpers that shown_when cannot hide (TASKS T-067), but every one is $0.00 here, which the skipped-line rule permits; no finding. Nothing to drop.

### classm.eic.2 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 3)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 3)" and were read). The reply's value is blank ("Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"); the project's is $0.00. The reply's blank is right: i1040gi p. 40, Step 1, question 1, "No children who have valid SSNs lived with you, is the amount on Form 1040 or 1040-SR, line 11b, less than $19,104 ...? No. STOP" (eic.reached_step5 false). The project's Step 5 lines are helpers that shown_when cannot hide (TASKS T-067), but every one is $0.00 here, which the skipped-line rule permits; no finding. Nothing to drop.

### classm.eic.2 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 4)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 4)" and were read). The reply's value is blank ("Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"); the project's is $0.00. The reply's blank is right: i1040gi p. 40, Step 1, question 1, "No children who have valid SSNs lived with you, is the amount on Form 1040 or 1040-SR, line 11b, less than $19,104 ...? No. STOP" (eic.reached_step5 false). The project's Step 5 lines are helpers that shown_when cannot hide (TASKS T-067), but every one is $0.00 here, which the skipped-line rule permits; no finding. Nothing to drop.

### classm.eic.2 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.2.prompt.txt) lists the line as "line (Step 5, 5)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 5)" and were read). The reply's value is blank ("Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"); the project's is $0.00. The reply's blank is right: i1040gi p. 40, Step 1, question 1, "No children who have valid SSNs lived with you, is the amount on Form 1040 or 1040-SR, line 11b, less than $19,104 ...? No. STOP" (eic.reached_step5 false). The project's Step 5 lines are helpers that shown_when cannot hide (TASKS T-067), but every one is $0.00 here, which the skipped-line rule permits; no finding. Nothing to drop.

### classm.eic.2 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached: STOP at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.2 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.3 — prompt sha256 3398fd501e9ccfd11b74693ab60dae6f157a6f781e673426096426f45fa64396; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#2, eic.limit_joint#2, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:true, eic.show_wsb4b:true, eic.show_wsb6:true, eic.wsb_6:positive, eic.earned_for_limit#1, eic.step5_income:true, eic.eligible:true, eic.line1#1, eic.line1_in_table:true, eic.line1_table#2, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:true, eic.show5:false, eic.line5#2, eic.smaller:left, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.3 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $77,987.00

### classm.eic.3 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.3 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $77,987.00

### classm.eic.3 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.3 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $77,987.00

### classm.eic.3 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $12,181.20

### classm.eic.3 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $12,181.20

### classm.eic.3 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $12,181.20

### classm.eic.3 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $4,870.00

### classm.eic.3 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $10,228.20

### classm.eic.3 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.3 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: 1+ child with valid SSN and line 3 (10,228.20) < $23,350, so leave blank and use line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.3 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $4,870.00

### case classm.eic.4 — prompt sha256 7ada53fb48b11d9d1017223ce125ec2492f395aec5aa8fcd142371df37b64fbc; branches: eic.qc_of_another:true, eic.age_range:true, eic.us_home:false, eic.has_qc:false, eic.married_rules:true, eic.top_limit#3, eic.below_top:true, eic.limit_other#0, eic.limit_joint#0, eic.limit#3, eic.step1_income:true, eic.step1_ssn:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:true, eic.legally_separated:false, eic.step3_married:false, eic.step3:false, eic.step4:false, eic.step34:false, eic.self_employed:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#0, eic.line2#1, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#3, eic.line5_blank:true, eic.line5#0, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.wsb_4b_positive:false, eic.clergy:false

### classm.eic.4 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.4 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 5 q2 is No (no self-employment, Schedule SE or statutory employee); Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.4 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Skipped: STOP at line 2 (zero credit)

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Skipped: STOP at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Skipped: STOP at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.4 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.5 — prompt sha256 5876a8be31a1917a31203fe8ba51c16471bf82eb07205af19ee4c8b582021768; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#1, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#1, eic.step1_income:false, eic.step1_ssn:false, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:false, eic.line4:true, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#1, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:left, eic.after_line4#1, eic.line6#0, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.5 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q2: no EIC-valid SSN, and AGI $61,693 is not under $57,554 (MFJ, 1 child) -> STOP before Step 5

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: Not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used (no self-employment) and credit barred at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached; stopped at Step 1

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.5 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.6 — prompt sha256 0951cb2ada0433aee4101a79f8da156aa6c5f5c8f86210be849c3d5562e0d048; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:true, eic.top_limit#2, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#2, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:floor, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:false, eic.line1_table#1, eic.line2#1, eic.show3:false, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#2, eic.line5_blank:true, eic.show5:false, eic.line5#1, eic.smaller:right, eic.after_line4#0, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:false, eic.wsb_line5_stop:false, eic.separated_box:true, eic.clergy:false

### classm.eic.6 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $0.00

### classm.eic.6 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.6 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.eic.6 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.6 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $0.00

### classm.eic.6 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 5 q2 is No (no self-employment, Schedule SE or statutory employee), so Worksheet A is used and Worksheet B is not completed

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B is not used

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
Work: Worksheet stopped at line 2 (zero credit)

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: Worksheet stopped at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: Worksheet stopped at line 2

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.6 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.7 — prompt sha256 ad14e2d805c28e72b23836233db7ce59441f02679aedb679b96c8327edb324fc; branches: eic.qc_of_another:false, eic.age_range:false, eic.us_home:true, eic.has_qc:false, eic.married_rules:false, eic.top_limit#0, eic.below_top:false, eic.limit_other#0, eic.limit_joint#0, eic.limit#0, eic.step1_income:false, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:false, eic.step34:false, eic.reached_step5:false, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:false, eic.eligible:false, eic.line1#0, eic.line1_in_table:true, eic.line1_table#0, eic.line2#0, eic.show3:false, eic.line4:false, eic.threshold_other#0, eic.threshold_joint#0, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:false, eic.line5#0, eic.smaller:left, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:false, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.7 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **SKIPPED**

Model: blank
Work: Step 1 Q1: no qualifying children and line 11b $66,664 is not less than $19,104, so STOP; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 3) — Subtract line 2 from line 1
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Step 5 not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **SKIPPED**

Model: blank
Work: STOP at Step 1; Worksheet A not reached

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.7 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

### case classm.eic.8 — prompt sha256 96574154f846362db54e5ae61ba328adc58ebeb09f2bc469d11271d4f7d79c9e; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:false, eic.show_wsb4b:false, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#0, eic.step5_income:true, eic.eligible:true, eic.line1#0, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:true, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:true, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#0, eic.reached_step3:true, eic.check_27c:false, eic.wsb_4b_positive:true, eic.wsb_line5_stop:false, eic.separated_box:false, eic.clergy:false

### classm.eic.8 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **AGREE**

Value: $26,469.00

### classm.eic.8 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **AGREE**

Value: $0.00

### classm.eic.8 — (Step 5, 3) — Subtract line 2 from line 1
Status: **AGREE**

Value: $26,469.00

### classm.eic.8 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **AGREE**

Value: $0.00

### classm.eic.8 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **AGREE**

Value: $26,469.00

### classm.eic.8 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **SKIPPED**

Model: blank
Work: Step 5 Q2 answered No (not self-employed), so Worksheet A is used and Worksheet B is not completed

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **SKIPPED**

Model: blank
Work: Worksheet B not used

No numeric assertion or class M credit: the model left this line blank.

### classm.eic.8 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $26,469.00

### classm.eic.8 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $3,829.00

### classm.eic.8 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $26,360.00

### classm.eic.8 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.8 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $3,845.00

### classm.eic.8 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $3,829.00

### case classm.eic.9 — prompt sha256 9747601dbf4c635c773bffe98b3d4a42b23dfce77d97a5f96508a11930d3072c; branches: eic.qc_of_another:false, eic.age_range:true, eic.us_home:true, eic.has_qc:true, eic.married_rules:false, eic.top_limit#0, eic.below_top:true, eic.limit_other#1, eic.limit_joint#1, eic.limit#0, eic.step1_income:true, eic.step1_ssn:true, eic.step1_foreign:true, eic.step1_resident:true, eic.gain_7a:floor, eic.step2_income:true, eic.step2_other:true, eic.same_home:false, eic.legally_separated:false, eic.step3_married:true, eic.step3:true, eic.step4:true, eic.step34:true, eic.reached_step5:true, eic.self_employed:true, eic.show_wsb4b:true, eic.show_wsb6:false, eic.wsb_6:positive, eic.earned_for_limit#1, eic.step5_income:false, eic.eligible:false, eic.line1#1, eic.line1_in_table:true, eic.line1_table#1, eic.line2#0, eic.show3:false, eic.line4:false, eic.threshold_other#1, eic.threshold_joint#1, eic.line5_threshold#0, eic.line5_blank:false, eic.show5:false, eic.line5#1, eic.smaller:right, eic.after_line4#1, eic.line6#1, eic.credit#1, eic.reached_step3:true, eic.check_27c:true, eic.wsb_4b_positive:true, eic.wsb_line5_stop:true, eic.separated_box:false, eic.clergy:false

### classm.eic.9 — (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MISSING**

Project: $73,579.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.9.prompt.txt) lists the line as "line (Step 5, 1)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 1" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 1)" and were read). The reply's value is $73,579.00 (Form 1040 line 1z); the project's is $73,579.00. They are equal, and Step 5 is reached (eic.reached_step5 true; Worksheet B line 4a reads it and line 4b $55,005.10 agrees), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.9 — (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless cho
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.9.prompt.txt) lists the line as "line (Step 5, 2)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 2" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 2)" and were read). The reply's value is $0.00 (no Medicaid waiver payments); the project's is $0.00. They are equal, and Step 5 is reached (eic.reached_step5 true; Worksheet B line 4a reads it and line 4b $55,005.10 agrees), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.9 — (Step 5, 3) — Subtract line 2 from line 1
Status: **MISSING**

Project: $73,579.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.9.prompt.txt) lists the line as "line (Step 5, 3)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 3" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 3)" and were read). The reply's value is $73,579.00 (line 1 minus line 2); the project's is $73,579.00. They are equal, and Step 5 is reached (eic.reached_step5 true; Worksheet B line 4a reads it and line 4b $55,005.10 agrees), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.9 — (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.9.prompt.txt) lists the line as "line (Step 5, 4)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 4" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 4)" and were read). The reply's value is $0.00 (no combat pay elected); the project's is $0.00. They are equal, and Step 5 is reached (eic.reached_step5 true; Worksheet B line 4a reads it and line 4b $55,005.10 agrees), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.9 — (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MISSING**

Project: $73,579.00
Model: no answer

Ruling: model error; on the reply format, not the tax reading. The prompt (.classm/classm.eic.9.prompt.txt) lists the line as "line (Step 5, 5)" and says each line is "named by its printed number as it appears in the IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole handle, exactly as given)"; the reply names it "Step 5, 5" without the parentheses, the class M parser (tools/transcription/classm.py extract) strips only a leading 'line ' before matching, and the log records no answer (the replies for classm.eic.3 to classm.eic.8 use "(Step 5, 5)" and were read). The reply's value is $73,579.00 (lines 3 plus 4); the project's is $73,579.00. They are equal, and Step 5 is reached (eic.reached_step5 true; Worksheet B line 4a reads it and line 4b $55,005.10 agrees), so the project amount is not a T-067 case. Nothing to drop.

### classm.eic.9 — 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned
Status: **AGREE**

Value: $55,005.10

### classm.eic.9 — 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero i
Status: **AGREE**

Value: $55,005.10

### classm.eic.9 — 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line
Status: **AGREE**

Value: $55,005.10

### classm.eic.9 — 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the colu
Status: **AGREE**

Value: $0.00

### classm.eic.9 — 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **AGREE**

Value: $48,693.10

### classm.eic.9 — 4 — Are the amounts on lines 3 and 1 the same?
Status: **AGREE**

Value: no

### classm.eic.9 — 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the colu
Status: **DISAGREE**

Project: $281.00
Model: $1,819.00
Work: 48,693.10 is not less than 23,350; EIC Table, Single, 1 child: 48,650-48,700 gives 1,819

Ruling: model error; i1040gi p. 46, Worksheet A, line 5: "No. Look up the amount on line 3 in the EIC Table to find the credit. Be sure you use the correct column for your filing status and the number of qualifying children you have who have valid SSNs." Line 3 is $48,693.10, single, one qualifying child with a valid SSN. The EIC Table, i1040gi p. 56, row "48,650 48,700" gives, for single, head of household or qualifying surviving spouse, 0 children $0, 1 child $281, 2 children $1,819, 3 children $2,713. Project $281.00 (tables/2025/eic_1.yaml); model $1,819.00 ("EIC Table, Single, 1 child: 48,650-48,700 gives 1,819"), the two-children column. The model's value is a misread table, not evidence. Also, the line is after a STOP on this return (Worksheet B line 4b $55,005.10 is not less than $50,434, i1040gi p. 47, line 5 "No. STOP"), so the project hides it (eic.show5 false) and the model should have left it blank; line 6 and the credit ($0.00) agree. [dropped]

### classm.eic.9 — 6 (eic.line6) — This is your earned income credit
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.eic.1

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
    work: "Line 1 minus line 2: 5,137.00 - 0 = 5,137.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "5137.00"
    work: "Line 3 plus line 4: 5,137.00 + 0 = 5,137.00; this is earned income"
  - printed: "4b"
    value: "blank"
    work: "Not self-employed, so Step 5 question 2 is No; use Worksheet A, and Worksheet B is not used"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used"
  - printed: "1"
    value: "5137.00"
    work: "Earned income from Step 5 line 5 = 5,137.00"
  - printed: "2"
    value: "1743.00"
    work: "EIC Table row 5,100-5,150, QSS column, 1 qualifying child with valid SSN = 1,743"
  - printed: "3"
    value: "2137.00"
    work: "Form 1040 line 11b = 2,137.00"
  - printed: "4"
    value: "no"
    work: "Line 3 (2,137) differs from line 1 (5,137)"
  - printed: "5"
    value: "blank"
    work: "Has 1 or more qualifying children and line 3 (2,137) is less than 23,350, so leave line 5 blank"
  - printed: "6 (eic.line6)"
    value: "1743.00"
    work: "Enter the line 2 amount on line 6 = 1,743"
```
```

### classm.eic.2

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "blank"
    work: "Step 1 Q1: MFS, no children with valid SSNs, AGI $22,732 is not under $19,104, so STOP and Step 5 is never reached"
  - printed: "Step 5, 2"
    value: "blank"
    work: "Not reached: STOP at Step 1. Investment income of $97,691 exceeds $11,950 with no Form 4797 (Step 2), and MFS with no qualifying child is barred (Step 4 Q1)"
  - printed: "Step 5, 3"
    value: "blank"
    work: "Not reached: STOP at Step 1"
  - printed: "Step 5, 4"
    value: "blank"
    work: "Not reached: STOP at Step 1"
  - printed: "Step 5, 5"
    value: "blank"
    work: "Not reached: STOP at Step 1"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not reached: STOP at Step 1"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not reached: STOP at Step 1"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached: STOP at Step 1"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP), so the EIC is $0"
```
```

### classm.eic.3

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "77987.00"
    work: "Form 1040 line 1z = 77,987.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "77987.00"
    work: "77,987.00 - 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "77987.00"
    work: "77,987.00 + 0.00; Schedule C filed, so Step 5 Q2 = Yes and Worksheet B applies"
  - printed: "4b"
    value: "12181.20"
    work: "Parts 1-2 (-65,805.80) + Step 5 earned income 77,987.00 = 12,181.20"
  - printed: "6 (eic.wsb_6)"
    value: "12181.20"
    work: "4b is positive and below $57,310 (2 children with valid SSNs), so line 6 = line 4b"
  - printed: "1"
    value: "12181.20"
    work: "Worksheet B line 6"
  - printed: "2"
    value: "4870.00"
    work: "EIC Table row 12,150-12,200, Single, 2 children = 4,870"
  - printed: "3"
    value: "10228.20"
    work: "Form 1040 line 11b"
  - printed: "4"
    value: "no"
    work: "10,228.20 is not equal to 12,181.20"
  - printed: "5"
    value: "blank"
    work: "1+ child with valid SSN and line 3 (10,228.20) < $23,350, so leave blank and use line 2"
  - printed: "6 (eic.line6)"
    value: "4870.00"
    work: "Amount from line 2"
```
```

### classm.eic.4

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "0.00"
    work: "Form 1040 line 1z = 0.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded (zero in this tool)"
  - printed: "(Step 5, 3)"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected (zero in this tool)"
  - printed: "(Step 5, 5)"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00 earned income"
  - printed: "4b"
    value: ""
    work: "Step 5 q2 is No (no self-employment, Schedule SE or statutory employee); Worksheet B not used"
  - printed: "6 (eic.wsb_6)"
    value: ""
    work: "Worksheet B not used"
  - printed: "1"
    value: "0.00"
    work: "Earned income from Step 5, line 5 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, HOH column, 0 children: 0 is below the first row (1-50), so credit 0. Line 2 is zero: STOP, check box 27c. Also Step 1 q3: filing Form 2555, STOP."
  - printed: "3"
    value: ""
    work: "Skipped: STOP at line 2 (zero credit)"
  - printed: "4"
    value: ""
    work: "Skipped: STOP at line 2"
  - printed: "5"
    value: ""
    work: "Skipped: STOP at line 2"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Not eligible (Form 2555 filer; zero table credit), so EIC = 0"
```
```

### classm.eic.5

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "blank"
    work: "Step 1 Q2: no EIC-valid SSN, and AGI $61,693 is not under $57,554 (MFJ, 1 child) -> STOP before Step 5"
  - printed: "(Step 5, 2)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "(Step 5, 3)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "(Step 5, 4)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "(Step 5, 5)"
    value: "blank"
    work: "Not reached; stopped at Step 1"
  - printed: "4b"
    value: "blank"
    work: "Worksheet B not used (no self-employment) and credit barred at Step 1"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used"
  - printed: "1"
    value: "blank"
    work: "Worksheet A not reached; stopped at Step 1"
  - printed: "2"
    value: "blank"
    work: "Worksheet A not reached"
  - printed: "3"
    value: "blank"
    work: "Worksheet A not reached"
  - printed: "4"
    value: "blank"
    work: "Worksheet A not reached"
  - printed: "5"
    value: "blank"
    work: "Worksheet A not reached"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Can't take the credit (Step 1 Q2 STOP: SSN not valid for EIC; check box 27c) -> EIC = 0"
```
```

### classm.eic.6

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "0.00"
    work: "Form 1040 line 1z = 0.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "(Step 5, 3)"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "(Step 5, 5)"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00 earned income"
  - printed: "4b"
    value: "blank"
    work: "Step 5 q2 is No (no self-employment, Schedule SE or statutory employee), so Worksheet A is used and Worksheet B is not completed"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B is not used"
  - printed: "1"
    value: "0.00"
    work: "Earned income from Step 5 line 5 = 0.00"
  - printed: "2"
    value: "0.00"
    work: "MFS uses the single column (star note). One qualifying child with valid SSN (dep_a); 0 is below the first table row, so credit = 0. Line 2 is zero: STOP, can't take the credit"
  - printed: "3"
    value: "blank"
    work: "Worksheet stopped at line 2 (zero credit)"
  - printed: "4"
    value: "blank"
    work: "Worksheet stopped at line 2"
  - printed: "5"
    value: "blank"
    work: "Worksheet stopped at line 2"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "Line 2 is zero, so no EIC is allowed; credit = 0"
```
```

### classm.eic.7

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: ""
    work: "Step 1 Q1: no qualifying children and line 11b $66,664 is not less than $19,104, so STOP; Step 5 not reached"
  - printed: "(Step 5, 2)"
    value: ""
    work: "STOP at Step 1; Step 5 not reached"
  - printed: "(Step 5, 3)"
    value: ""
    work: "STOP at Step 1; Step 5 not reached"
  - printed: "(Step 5, 4)"
    value: ""
    work: "STOP at Step 1; Step 5 not reached"
  - printed: "(Step 5, 5)"
    value: ""
    work: "STOP at Step 1; Step 5 not reached"
  - printed: "4b"
    value: ""
    work: "STOP at Step 1; Worksheet B not used"
  - printed: "6 (eic.wsb_6)"
    value: ""
    work: "STOP at Step 1; Worksheet B not used"
  - printed: "1"
    value: ""
    work: "STOP at Step 1; Worksheet A not reached"
  - printed: "2"
    value: ""
    work: "STOP at Step 1; Worksheet A not reached"
  - printed: "3"
    value: ""
    work: "STOP at Step 1; Worksheet A not reached"
  - printed: "4"
    value: ""
    work: "STOP at Step 1; Worksheet A not reached"
  - printed: "5"
    value: ""
    work: "STOP at Step 1; Worksheet A not reached"
  - printed: "6 (eic.line6)"
    value: "0.00"
    work: "You can't take the credit (Step 1 STOP: AGI $66,664 is at least the $19,104 limit for no children), so EIC is $0"
```
```

### classm.eic.8

```yaml
```yaml
lines:
  - printed: "(Step 5, 1)"
    value: "26469.00"
    work: "Form 1040 line 1z = 26,469.00"
  - printed: "(Step 5, 2)"
    value: "0.00"
    work: "No Medicaid waiver payments excluded on Schedule 1 line 8s"
  - printed: "(Step 5, 3)"
    value: "26469.00"
    work: "26,469.00 - 0.00"
  - printed: "(Step 5, 4)"
    value: "0.00"
    work: "No nontaxable combat pay elected"
  - printed: "(Step 5, 5)"
    value: "26469.00"
    work: "26,469.00 + 0.00 = earned income"
  - printed: "4b"
    value: "blank"
    work: "Step 5 Q2 answered No (not self-employed), so Worksheet A is used and Worksheet B is not completed"
  - printed: "6 (eic.wsb_6)"
    value: "blank"
    work: "Worksheet B not used"
  - printed: "1"
    value: "26469.00"
    work: "Earned income from Step 5 line 5"
  - printed: "2"
    value: "3829.00"
    work: "EIC Table row 26,450-26,500, Single, 1 child = 3,829"
  - printed: "3"
    value: "26360.00"
    work: "Form 1040 line 11b = 26,360.00"
  - printed: "4"
    value: "no"
    work: "26,360 is not equal to 26,469"
  - printed: "5"
    value: "3845.00"
    work: "1 child; 26,360 is not less than 23,350; EIC Table row 26,350-26,400, Single, 1 child = 3,845"
  - printed: "6 (eic.line6)"
    value: "3829.00"
    work: "Smaller of line 5 (3,845) and line 2 (3,829)"
```
```

### classm.eic.9

```yaml
```yaml
lines:
  - printed: "Step 5, 1"
    value: "73579.00"
    work: "Form 1040 line 1z = 73,579.00"
  - printed: "Step 5, 2"
    value: "0.00"
    work: "No Medicaid waiver payments excluded; zero in this tool"
  - printed: "Step 5, 3"
    value: "73579.00"
    work: "73,579.00 - 0.00"
  - printed: "Step 5, 4"
    value: "0.00"
    work: "No nontaxable combat pay elected; zero in this tool"
  - printed: "Step 5, 5"
    value: "73579.00"
    work: "73,579.00 + 0.00 = earned income; Schedule C filed, so Step 5 Q2 is Yes and Worksheet B applies"
  - printed: "4b"
    value: "55005.10"
    work: "Parts 1-2 total (-18,573.90) + line 3 (0) + line 4a (73,579.00) = 55,005.10; not less than 50,434 for 1 child, so line 5 says STOP"
  - printed: "line 6 (eic.wsb_6)"
    value: "55005.10"
    work: "Line 4b = 55,005.10 (positive)"
  - printed: "1"
    value: "55005.10"
    work: "Worksheet B line 6 = 55,005.10"
  - printed: "2"
    value: "0.00"
    work: "EIC Table, Single, 1 child: 55,000-55,050 gives 0; line 2 is zero, so STOP"
  - printed: "3"
    value: "48693.10"
    work: "Form 1040 line 11b = 48,693.10"
  - printed: "4"
    value: "no"
    work: "48,693.10 is not equal to 55,005.10"
  - printed: "5"
    value: "1819.00"
    work: "48,693.10 is not less than 23,350; EIC Table, Single, 1 child: 48,650-48,700 gives 1,819"
  - printed: "line 6 (eic.line6)"
    value: "0.00"
    work: "Smaller of line 5 (1,819) and line 2 (0) = 0; no credit allowed (Worksheet B line 5 STOP and line 2 is zero)"
```
```
