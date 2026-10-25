# Class M hand-work — sli

`Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 2631c87fc3c9d52313fa0771b0cd63a7a482cffd68f3b03f8442c6cfe662aa49 |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sli.1 — prompt sha256 7e4d82041a33236044e1cfcf525007fe7ac9286c563ce8b8b5001a27a317469b; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#3, sli.over:false, sli.divisor#3, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

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
Status: **SKIPPED**

Model: blank
Work: Line 4 (32,936) is not more than line 5 (85,000), so line 6 is skipped

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.1 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.2 — prompt sha256 495a0862380dbf3b8cfa8cd409b389d294317d742df084d9166ffaeba08f4c1f; branches: sli.has:true, sli.claimed:true, sli.line1:right, sli.line5#4, sli.over:true, sli.divisor#4, sli.line8#0, sli.line9:positive, sli.eligible:false, sli.allowed#1, sli.deduction#0

### classm.sli.2 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **SKIPPED**

Model: blank
Work: Filer is claimed as a dependent on another's 2025 return, so not eligible for the deduction; worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 4 — Subtract line 3 from line 2
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 8 — Multiply line 1 by line 7
Status: **SKIPPED**

Model: blank
Work: Not eligible (claimed as a dependent); worksheet not completed

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.2 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **DISAGREE**

Project: $2,045.00
Model: $0.00
Work: Deduction allowed only if not claimed as a dependent; filer is claimed, so deduction is 0 (Schedule 1, line 21 = 0)

Ruling: representation; project retained; model value dropped from the fixture. The filer (qualifying surviving spouse) is claimed as a dependent on someone else's return and cannot take the deduction (i1040gi p. 98, Line 21, "You can take this deduction only if all of the following apply ... You, or your spouse if filing jointly, aren't claimed as a dependent on someone else's (such as your parent's) 2025 tax return"); the model left the worksheet blank, and the project figures every worksheet line (line 9 is $2,500.00 less $455.00 = $2,045.00; the amount carried to Schedule 1 line 21 is sli.deduction) and applies the bar in sli.eligible, so sli.deduction, which Schedule 1 line 21 copies, is $0.00, as the model's line 9. A blank is not the number zero. Dropped from the fixture as not evidence. No change to the data. [dropped]

### case classm.sli.3 — prompt sha256 c94ec96bd17760570157b64b9d9f537c8117f42b400622ad25a028f6a054560e; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#0, sli.over:false, sli.divisor#0, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.3 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $16,046.00

### classm.sli.3 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $16,046.00

### classm.sli.3 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.3 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 4 (16,046) is not more than line 5 (85,000), so answer No and skip lines 6 and 7

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.3 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.4 — prompt sha256 86e74e8220d843d66495e34efd0ede9cfe5b0e6bb8265109e114ac6fcd912d23; branches: sli.has:true, sli.claimed:false, sli.line1:left, sli.line5#1, sli.over:false, sli.divisor#1, sli.line8#1, sli.line9:positive, sli.eligible:true, sli.allowed#0, sli.deduction#0

### classm.sli.4 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $164.00

### classm.sli.4 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $-103,568.92

### classm.sli.4 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $-103,568.92

### classm.sli.4 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $170,000.00

### classm.sli.4 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 4 is not more than line 5, so No: skip lines 6 and 7

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.4 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $164.00

### case classm.sli.5 — prompt sha256 db9b7d249343f9d12a2215bd9f44f8c1e2d88fce3b1428398dfd1e9aee39c524; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#2, sli.over:true, sli.divisor#2, sli.line8#0, sli.line9:floor, sli.eligible:false, sli.allowed#1, sli.deduction#1

### classm.sli.5 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $21,750.13

### classm.sli.5 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $21,750.13

### classm.sli.5 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **SKIPPED**

Model: blank
Work: The form prints no amount for married filing separately (that status is not eligible), so left blank.

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.5 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 5 has no amount for married filing separately, so line 6 can't be figured. Skip lines 6-7 and go to line 8 as 0.

No numeric assertion or class M credit: the model left this line blank.


### classm.sli.5 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.sli.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00 (not more than $2,500)"
  - printed: "2"
    value: "32936.00"
    work: "Form 1040 line 9 = 32,936.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11–20, 23, 25 total 0.00"
  - printed: "4"
    value: "32936.00"
    work: "32,936.00 - 0.00 = 32,936.00"
  - printed: "5"
    value: "85000.00"
    work: "Head of household amount is $85,000"
  - printed: "6"
    value: ""
    work: "Line 4 (32,936) is not more than line 5 (85,000), so line 6 is skipped"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer was No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```
```

### classm.sli.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "blank"
    work: "Filer is claimed as a dependent on another's 2025 return, so not eligible for the deduction; worksheet not completed"
  - printed: "2"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "3"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "4"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "5"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "6"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "8"
    value: "blank"
    work: "Not eligible (claimed as a dependent); worksheet not completed"
  - printed: "9"
    value: "0.00"
    work: "Deduction allowed only if not claimed as a dependent; filer is claimed, so deduction is 0 (Schedule 1, line 21 = 0)"
```
```

### classm.sli.3

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid on qualified student loans is $0.00, which is under the $2,500 cap"
  - printed: "2"
    value: "16046.00"
    work: "Form 1040, line 9 = 16,046.00"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1, lines 11 through 20, 23 and 25 add to 0.00"
  - printed: "4"
    value: "16046.00"
    work: "16,046.00 - 0.00 = 16,046.00"
  - printed: "5"
    value: "85000.00"
    work: "Filing status is Single, so enter $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (16,046) is not more than line 5 (85,000), so answer No and skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 was answered No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```

### classm.sli.4

```yaml
lines:
  - printed: "1"
    value: "164.00"
    work: "Interest paid $164.00, not more than $2,500"
  - printed: "2"
    value: "-103568.92"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 total 0 (line 23 not given, taken as 0)"
  - printed: "4"
    value: "-103568.92"
    work: "-103,568.92 - 0.00"
  - printed: "5"
    value: "170000.00"
    work: "Married filing jointly amount"
  - printed: "6"
    value: "blank"
    work: "Line 4 is not more than line 5, so No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "No on line 6, so enter -0-"
  - printed: "9"
    value: "164.00"
    work: "164.00 - 0.00"
```

### classm.sli.5

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid is $0.00. Married filing separately can't take this deduction anyway, so line 1 is 0."
  - printed: "2"
    value: "21750.13"
    work: "Form 1040, line 9 = 21,750.13"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 are all 0 = 0.00"
  - printed: "4"
    value: "21750.13"
    work: "21,750.13 - 0.00 = 21,750.13"
  - printed: "5"
    value: "blank"
    work: "The form prints no amount for married filing separately (that status is not eligible), so left blank."
  - printed: "6"
    value: "blank"
    work: "Line 5 has no amount for married filing separately, so line 6 can't be figured. Skip lines 6-7 and go to line 8 as 0."
  - printed: "8"
    value: "0.00"
    work: "Line 6 is skipped, so the form says enter -0- on line 8."
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00. Married filing separately can't take the deduction."
```
