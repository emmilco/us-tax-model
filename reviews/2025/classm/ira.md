# Class M hand-work — ira

`IRA Deduction Worksheet — Schedule 1, Line 20` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | b7e1195daee08526596198e4e2d251f05bd13391afc1b51fad9da5be1c1b12eb |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 95, 96, 97, 98 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 95, 96, 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p590a | 2025 | 6, 7, 16, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 7, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |

## Lines

### case classm.ira.1 — prompt sha256 92396b7fece1b111927b514e82d89aaecdc0aa427b5debedb84d09245991db02; branches: ira.joint:false, ira.joint_type:false, ira.any_trad:false, ira.anyone_covered:false, ira.lines2to6:false, ira.cov_gate:false, ira.line1a:false, ira.line1b:false, ira.line2a#1, ira.line2b#1, ira.line6a#1, ira.line6b#1, ira.line7a#1, ira.line7b#1, ira.kbh_amount#0, ira.kbh_short:false, ira.both_kinds:false, ira.over_comp:false, ira.special:false, ira.se_capital:false, ira.se_capital_gate:false, ira.special_gate:false, ira.combat_gate:false, ira.excl_gate:false, ira.deduct_less:false, ira.less_gate:false

### classm.ira.1 — 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan
Status: **AGREE**

Value: no

### classm.ira.1 — 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **SKIPPED**

Model: blank
Work: Not married filing jointly (head of household); line does not apply

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 2a — Enter the amount shown below that applies to you (your IRA)
Status: **SKIPPED**

Model: blank
Work: Line 1a is No (and 1b does not apply), so skip lines 2 through 6

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **SKIPPED**

Model: blank
Work: Skipped per the instruction after line 1; no spouse column

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **SKIPPED**

Model: blank
Work: Skipped: line 1a is No

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 an
Status: **SKIPPED**

Model: blank
Work: Skipped: line 1a is No

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both
Status: **SKIPPED**

Model: blank
Work: Skipped: line 1a is No

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 
Status: **SKIPPED**

Model: blank
Work: Skipped: line 1a is No

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 
Status: **SKIPPED**

Model: blank
Work: Skipped: line 1a is No

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple 
Status: **DISAGREE**

Project: $0.00
Model: $7,000.00
Work: Lines 2-6 skipped; applicable amount for under age 50 is $7,000

Ruling: representation; project retained; model value dropped from the fixture. The filer made no traditional IRA contributions for 2025 (line 11a $0.00, on which the model agrees), and the worksheet is for figuring the deduction for such contributions (i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction ... Use the IRA Deduction Worksheet to figure the amount, if any, of your IRA deduction"); the project shows the printed lines 7a and 7b as $0.00 for a return without traditional contributions (ira.any_trad) and the applicable amount, $7,000, otherwise (person.ira_line7). The model entered the applicable amount by the line 1 instruction (p. 97, "enter the applicable amount below on line 7a ... $7,000 if under age 50 at the end of 2025"). Line 12a, the smallest of lines 7a, 10 and 11a, is $0.00 either way, and the model agrees on it. No change to the data. [dropped]

### classm.ira.1 — 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple 
Status: **SKIPPED**

Model: blank
Work: Not applicable; not filing jointly

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, 
Status: **AGREE**

Value: $32,936.00

### classm.ira.1 — 9 — Enter the earned income you (and your spouse if filing jointly) received as a se
Status: **AGREE**

Value: $0.00

### classm.ira.1 — 10 — Add lines 8 and 9
Status: **AGREE**

Value: $32,936.00

### classm.ira.1 — 11a — Enter traditional IRA contributions made, or that will be made by the due date o
Status: **AGREE**

Value: $0.00

### classm.ira.1 — 11b — Enter traditional IRA contributions made, or that will be made by the due date o
Status: **SKIPPED**

Model: blank
Work: No spouse IRA; not filing jointly

No numeric assertion or class M credit: the model left this line blank.


### classm.ira.1 — 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your
Status: **AGREE**

Value: $0.00

### classm.ira.1 — 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your
Status: **SKIPPED**

Model: blank
Work: Not applicable; not filing jointly

No numeric assertion or class M credit: the model left this line blank.


### case classm.ira.2 — prompt sha256 968a3f457c3f412123c057f133abf0b9298f304d2137690657469faea6181cce; branches: ira.joint:true, ira.joint_type:true, ira.any_trad:false, ira.anyone_covered:true, ira.lines2to6:false, ira.cov_gate:false, ira.line1a:false, ira.line1b:false, ira.line2a#1, ira.line2b#1, ira.line6a#1, ira.line6b#1, ira.line7a#1, ira.line7b#1, ira.kbh_amount#0, ira.kbh_short:false, ira.both_kinds:false, ira.over_comp:false, ira.special:false, ira.se_capital:false, ira.se_capital_gate:false, ira.special_gate:false, ira.combat_gate:false, ira.excl_gate:false, ira.deduct_less:false, ira.less_gate:false

### classm.ira.2 — 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan
Status: **AGREE**

Value: no

### classm.ira.2 — 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **DISAGREE**

Project: no
Model: yes
Work: MFJ; spouse covered by a retirement plan, so go to line 2

Ruling: representation; project retained; model value dropped from the fixture. No one on this joint return made traditional IRA contributions for 2025 (lines 11a and 11b $0.00, on which the model agrees), so the worksheet figures no deduction (i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"). The project's printed line 1b answers Yes only on a return with traditional contributions (ira.any_trad); it is shown on the values sheet and nothing reads it, the deduction reading each person's coverage (person.ira_cov, Yes for the spouse here). The model answered from the spouse's coverage. Lines 6, 7 and 12 are $0.00 in both. No change to the data. [dropped]

### classm.ira.2 — 2a — Enter the amount shown below that applies to you (your IRA)
Status: **DISAGREE**

Project: $0.00
Model: $246,000.00
Work: MFJ; taxpayer answered No on 1a, so enter $246,000 for the uncovered person

Ruling: representation; project retained; model value dropped from the fixture. No one on this joint return made traditional IRA contributions for 2025 (lines 11a and 11b $0.00, on which the model agrees; i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"), and the project shows lines 2 through 6 only when there are traditional contributions and someone is covered (ira.lines2to6), $0.00 otherwise. The model worked the line as if contributions had been made ($246,000 for the person not covered, p. 97, line 2, "But if you checked 'No' on either line 1a or 1b, enter $246,000 for the person who wasn't covered by a plan"). Line 6a is $0.00 in both (line 5, $384,470.80, is not less than line 2), as are lines 7a and 12a. No change to the data. [dropped]

### classm.ira.2 — 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **DISAGREE**

Project: $0.00
Model: $146,000.00
Work: MFJ; spouse covered, so enter $146,000

Ruling: representation; project retained; model value dropped from the fixture. No one on this joint return made traditional IRA contributions for 2025 (lines 11a and 11b $0.00, on which the model agrees; i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"), and the project shows lines 2 through 6 only when there are traditional contributions and someone is covered (ira.lines2to6), $0.00 otherwise. The model worked the line as if contributions had been made ($146,000, p. 97, line 2, "Married filing jointly, enter $146,000 in both columns"). Line 6b is $0.00 in both (line 5, $384,470.80, is not less than line 2), as are lines 7b and 12b. No change to the data. [dropped]

### classm.ira.2 — 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $384,470.80

### classm.ira.2 — 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 an
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both
Status: **AGREE**

Value: $384,470.80

### classm.ira.2 — 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple 
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple 
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, 
Status: **AGREE**

Value: $390,996.00

### classm.ira.2 — 9 — Enter the earned income you (and your spouse if filing jointly) received as a se
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 10 — Add lines 8 and 9
Status: **AGREE**

Value: $390,996.00

### classm.ira.2 — 11a — Enter traditional IRA contributions made, or that will be made by the due date o
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 11b — Enter traditional IRA contributions made, or that will be made by the due date o
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your
Status: **AGREE**

Value: $0.00

### classm.ira.2 — 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.ira.1

```yaml
```yaml
lines:
  - printed: "1a"
    value: "no"
    work: "Taxpayer not covered by a retirement plan"
  - printed: "1b"
    value: ""
    work: "Not married filing jointly (head of household); line does not apply"
  - printed: "2a"
    value: ""
    work: "Line 1a is No (and 1b does not apply), so skip lines 2 through 6"
  - printed: "2b"
    value: ""
    work: "Skipped per the instruction after line 1; no spouse column"
  - printed: "3"
    value: ""
    work: "Skipped: line 1a is No"
  - printed: "4"
    value: ""
    work: "Skipped: line 1a is No"
  - printed: "5"
    value: ""
    work: "Skipped: line 1a is No"
  - printed: "6a"
    value: ""
    work: "Skipped: line 1a is No"
  - printed: "6b"
    value: ""
    work: "Skipped: line 1a is No"
  - printed: "7a"
    value: "7000.00"
    work: "Lines 2-6 skipped; applicable amount for under age 50 is $7,000"
  - printed: "7b"
    value: ""
    work: "Not applicable; not filing jointly"
  - printed: "8"
    value: "32936.00"
    work: "W-2 box 1 wages $32,936 + alimony $0 + combat pay $0"
  - printed: "9"
    value: "0.00"
    work: "No Schedule C or self-employment income; $0 - $0 (lines 15 and 16) = $0"
  - printed: "10"
    value: "32936.00"
    work: "$32,936 + $0"
  - printed: "11a"
    value: "0.00"
    work: "Traditional IRA contributions for 2025 = $0"
  - printed: "11b"
    value: ""
    work: "No spouse IRA; not filing jointly"
  - printed: "12a"
    value: "0.00"
    work: "Smallest of $7,000, $32,936, $0 = $0"
  - printed: "12b"
    value: ""
    work: "Not applicable; not filing jointly"
```
```

### classm.ira.2

```yaml
```yaml
lines:
  - printed: "1a"
    value: "no"
    work: "Taxpayer not covered by a retirement plan"
  - printed: "1b"
    value: "yes"
    work: "MFJ; spouse covered by a retirement plan, so go to line 2"
  - printed: "2a"
    value: "246000.00"
    work: "MFJ; taxpayer answered No on 1a, so enter $246,000 for the uncovered person"
  - printed: "2b"
    value: "146000.00"
    work: "MFJ; spouse covered, so enter $146,000"
  - printed: "3"
    value: "384470.80"
    work: "Form 1040 line 9"
  - printed: "4"
    value: "0.00"
    work: "Sch 1 lines 11-19a + 23 + 25 = 0 (line 23 not given; treated as 0)"
  - printed: "5"
    value: "384470.80"
    work: "384,470.80 - 0; MFJ, so the same amount goes in both columns"
  - printed: "6a"
    value: "0.00"
    work: "384,470.80 is not less than 246,000; No, none deductible"
  - printed: "6b"
    value: "0.00"
    work: "384,470.80 is not less than 146,000; No, none deductible"
  - printed: "7a"
    value: "0.00"
    work: "Line 6 answered No (STOP); no deductible amount"
  - printed: "7b"
    value: "0.00"
    work: "Line 6 answered No (STOP); no deductible amount"
  - printed: "8"
    value: "390996.00"
    work: "W-2 box 1: 358,653 + 32,343; alimony 0; combat pay 0"
  - printed: "9"
    value: "0.00"
    work: "Self-employment earned income parts 0 - Sch 1 lines 15/16 (0) = 0"
  - printed: "10"
    value: "390996.00"
    work: "390,996 + 0"
  - printed: "11a"
    value: "0.00"
    work: "Taxpayer traditional IRA contributions = 0"
  - printed: "11b"
    value: "0.00"
    work: "Spouse traditional IRA contributions = 0"
  - printed: "12a"
    value: "0.00"
    work: "Smallest of 0, 390,996, 0 = 0"
  - printed: "12b"
    value: "0.00"
    work: "Smallest of 0, 390,996, 0 = 0"
```
```
