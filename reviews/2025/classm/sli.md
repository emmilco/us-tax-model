# Class M hand-work — sli

`Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 8a2bb2e41ef56332a720dab595e17e506650a0235792f20528e07020eec8807b |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sli.1 — prompt sha256 5274de8e029e6cd2e6c5c4d958f926d7bbc185e6211e926952b88223539c8b2c; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#3, sli.over:false, sli.divisor#3, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.1 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $32,936.00

### classm.sli.1 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $32,936.00

### classm.sli.1 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.1 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-52,064.00
Model: $0.00
Work: Line 4 (32,936) is not more than line 5 (85,000), so No: skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.1 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.2 — prompt sha256 a4a9e20907496524c5ba368342057da68f1c71e0a8f677ce97daf1fffffe93f3; branches: sli.has:true, sli.claimed:false, sli.line1:right, sli.line5#2, sli.over:true, sli.divisor#2, sli.line8#0, sli.line9:positive, sli.eligible:false, sli.allowed#1, sli.deduction#0

### classm.sli.2 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **DISAGREE**

Project: $2,500.00
Model: $0.00
Work: Married filing separately cannot take this deduction, so $3,000 of interest counts as 0

Ruling: representation; project retained; model value dropped from the fixture. A married filer filing separately cannot take the deduction (i1040gi p. 98, 'Your filing status is any status except married filing separately') and does not use the worksheet; the project figures every worksheet line for such a filer and applies the bar in sli.eligible, so sli.deduction, which Schedule 1 line 21 copies, is 0.00, as the model's line 9; the model wrote the bar into the lines instead. The project's line 1 is the interest 3,000.00 limited to 2,500.00 (p. 99, line 1). Dropped from the fixture as not evidence. [dropped]

### classm.sli.2 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $2,584.00

### classm.sli.2 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $2,584.00

### classm.sli.2 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $2,584.00
Model: $0.00
Work: No line 5 amount for married filing separately; skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. A married filer filing separately cannot take the deduction (i1040gi p. 98, 'Your filing status is any status except married filing separately') and does not use the worksheet; the project figures every worksheet line for such a filer and applies the bar in sli.eligible, so sli.deduction, which Schedule 1 line 21 copies, is 0.00, as the model's line 9; the model wrote the bar into the lines instead. With no line 5 amount printed for this status the project's line 5 is 0.00, so line 4 is more than line 5 and line 6 is 2,584.00 less 0.00 = 2,584.00. Dropped from the fixture as not evidence. [dropped]

### classm.sli.2 — 8 — Multiply line 1 by line 7
Status: **DISAGREE**

Project: $430.00
Model: $0.00
Work: Lines 6 and 7 skipped, so enter -0-

Ruling: representation; project retained; model value dropped from the fixture. A married filer filing separately cannot take the deduction (i1040gi p. 98, 'Your filing status is any status except married filing separately') and does not use the worksheet; the project figures every worksheet line for such a filer and applies the bar in sli.eligible, so sli.deduction, which Schedule 1 line 21 copies, is 0.00, as the model's line 9; the model wrote the bar into the lines instead. The project's line 8 is 2,500.00 x 0.172 (2,584.00/15,000.00 = 0.17227, three places, amb.2025.sli_ratio_places) = 430.00. Dropped from the fixture as not evidence. [dropped]

### classm.sli.2 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **DISAGREE**

Project: $2,070.00
Model: $0.00
Work: 0.00 - 0.00; no deduction for married filing separately

Ruling: representation; project retained; model value dropped from the fixture. A married filer filing separately cannot take the deduction (i1040gi p. 98, 'Your filing status is any status except married filing separately') and does not use the worksheet; the project figures every worksheet line for such a filer and applies the bar in sli.eligible, so sli.deduction, which Schedule 1 line 21 copies, is 0.00, as the model's line 9; the model wrote the bar into the lines instead. The project's line 9 is 2,500.00 less 430.00 = 2,070.00; the amount carried to Schedule 1 line 21 is sli.deduction, 0.00. Dropped from the fixture as not evidence. [dropped]

### case classm.sli.3 — prompt sha256 2f3ce6742eb6009a263d99000940013817cdc27ad8117fa1a62ae0a69c92b2d7; branches: sli.has:false, sli.claimed:true, sli.line1:left, sli.line5#0, sli.over:false, sli.divisor#0, sli.line8#1, sli.line9:floor, sli.eligible:false, sli.allowed#1, sli.deduction#1

### classm.sli.3 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $-10,817.72

### classm.sli.3 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $-10,817.72

### classm.sli.3 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.3 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-95,817.72
Model: $0.00
Work: Line 4 (-10,817.72) is not more than line 5 (85,000), so No: skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet says 'No. Skip lines 6 and 7, enter -0- on line 8' (i1040gi p. 99); line 8 reads line 6 only when line 4 is more than line 5 (sli.over), so lines 8 and 9 agree. Here line 4 is -10,817.72 and line 5 85,000.00, so the project's line 6 is -95,817.72; lines 8 and 9 are 0.00 in both. Dropped from the fixture as not evidence. [dropped]

### classm.sli.3 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.4 — prompt sha256 4ad9e6f95b17c085c66dd6cc344578e11c28be98a77903358be0604ce725b775; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#1, sli.over:false, sli.divisor#1, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.4 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $6,724.00

### classm.sli.4 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $6,724.00

### classm.sli.4 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $170,000.00

### classm.sli.4 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-163,276.00
Model: $0.00
Work: Line 4 (6724.00) is not more than line 5 (170000.00), so No: skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet says 'No. Skip lines 6 and 7, enter -0- on line 8' (i1040gi p. 99); line 8 reads line 6 only when line 4 is more than line 5 (sli.over), so lines 8 and 9 agree. Here line 4 is 6,724.00 and line 5 170,000.00, so the project's line 6 is -163,276.00; lines 8 and 9 are 0.00 in both. Dropped from the fixture as not evidence. [dropped]

### classm.sli.4 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.5 — prompt sha256 29482894b866d1190a7ffd8d5d5744371a324360f1fb51fcab7e5221d420dfa4; branches: sli.has:true, sli.claimed:false, sli.line1:right, sli.line5#4, sli.over:true, sli.divisor#4, sli.line8#0, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#0

### classm.sli.5 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $2,500.00

### classm.sli.5 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $272,822.00

### classm.sli.5 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $272,822.00

### classm.sli.5 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.5 — 6 — Subtract line 5 from line 4
Status: **AGREE**

Value: $187,822.00

### classm.sli.5 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $2,500.00

### classm.sli.5 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.sli.1

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00, under the $2,500 cap"
  - printed: "2"
    value: "32936.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 are all 0; other lines in 11-20, 23, 25 not provided, taken as 0"
  - printed: "4"
    value: "32936.00"
    work: "32,936.00 - 0.00"
  - printed: "5"
    value: "85000.00"
    work: "Head of household amount is $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (32,936) is not more than line 5 (85,000), so No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer is No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00"
```

### classm.sli.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Married filing separately cannot take this deduction, so $3,000 of interest counts as 0"
  - printed: "2"
    value: "2584.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 all 0; no other amounts given"
  - printed: "4"
    value: "2584.00"
    work: "2584.00 - 0.00"
  - printed: "5"
    value: "blank"
    work: "Worksheet lists no amount for married filing separately"
  - printed: "6"
    value: "blank"
    work: "No line 5 amount for married filing separately; skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Lines 6 and 7 skipped, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00; no deduction for married filing separately"
```
```

### classm.sli.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00 (not over $2,500 cap); also claimed as a dependent, so no deduction allowed"
  - printed: "2"
    value: "-10817.72"
    work: "Form 1040 line 9 = -10,817.72"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11 through 20, 23, 25: 0 + 0 + 0 + 0 + 0 (others none) = 0.00"
  - printed: "4"
    value: "-10817.72"
    work: "-10,817.72 - 0.00 = -10,817.72"
  - printed: "5"
    value: "85000.00"
    work: "Single filing status = $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (-10,817.72) is not more than line 5 (85,000), so No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer is No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```
```

### classm.sli.4

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00, which is under the $2,500 cap"
  - printed: "2"
    value: "6724.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1 lines 11-20, 23, 25: 0+0+0+0+0 = 0.00"
  - printed: "4"
    value: "6724.00"
    work: "6724.00 - 0.00"
  - printed: "5"
    value: "170000.00"
    work: "Married filing jointly amount is $170,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (6724.00) is not more than line 5 (170000.00), so No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer was No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00"
```

### classm.sli.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "2500.00"
    work: "Interest paid $3,000.00; capped at $2,500"
  - printed: "2"
    value: "272822.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1 lines 11, 13, 15, 16, 17 are all 0; no other lines in 11-20, 23, 25 were given, so treated as 0"
  - printed: "4"
    value: "272822.00"
    work: "272822.00 - 0.00"
  - printed: "5"
    value: "85000.00"
    work: "Qualifying surviving spouse: $85,000"
  - printed: "6"
    value: "187822.00"
    work: "Line 4 is more than line 5 (Yes): 272822.00 - 85000.00"
  - printed: "8"
    value: "2500.00"
    work: "Line 7: 187822 / 15000 = 12.521, 1.000 or more, so 1.000; 2500.00 x 1.000"
  - printed: "9"
    value: "0.00"
    work: "2500.00 - 2500.00"
```
```
