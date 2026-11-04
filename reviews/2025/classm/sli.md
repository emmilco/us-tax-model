# Class M hand-work — sli

`Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d344ef928f6efc85fb5b9c35363e8d96ec246fed61396452a72a3ef34cd1cf7e |
| cases | 5 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sli.1 — prompt sha256 1e5adb7ff2208c4d6bfe23e2f609127d03dfcee7d24d7f1d42ef46d9bb5dd1c8; branches: sli.has:false, sli.line1:left, sli.line5#2, sli.over:true, sli.divisor#2, sli.line8#0, sli.line9:floor, sli.eligible:false, sli.allowed#1, sli.deduction#1

### classm.sli.1 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $51,731.00

### classm.sli.1 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $51,731.00

### classm.sli.1 — 5 — Enter the amount shown below for your filing status. Single, head of household,
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 6 — Subtract line 5 from line 4
Status: **AGREE**

Value: $51,731.00

### classm.sli.1 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.2 — prompt sha256 a8e2b93dc77464d577a8ff991f3f698f2093b088081801773e4da2424b6bc4ff; branches: sli.has:true, sli.line1:right, sli.line5#1, sli.over:false, sli.divisor#1, sli.line8#1, sli.line9:positive, sli.eligible:true, sli.allowed#0, sli.deduction#0

### classm.sli.2 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $2,500.00

### classm.sli.2 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $95,460.00

### classm.sli.2 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $95,460.00

### classm.sli.2 — 5 — Enter the amount shown below for your filing status. Single, head of household,
Status: **AGREE**

Value: $170,000.00

### classm.sli.2 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: line 4 95,460.00 not more than line 5 170,000.00 -> No: skip lines 6 and 7

No numeric assertion or class M credit: the model left this line blank.

### classm.sli.2 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $2,500.00

### case classm.sli.3 — prompt sha256 d21c10693651b6b241a1cd29f2243620bf1e636b72e9010ba7788da5a68a9f5d; branches: sli.has:false, sli.line1:left, sli.line5#3, sli.over:false, sli.divisor#3, sli.line8#1, sli.line9:floor, sli.deduction#1

### classm.sli.3 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $32,936.00

### classm.sli.3 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $32,936.00

### classm.sli.3 — 5 — Enter the amount shown below for your filing status. Single, head of household,
Status: **AGREE**

Value: $85,000.00

### classm.sli.3 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 4 (32,936) not more than line 5 (85,000): No, skip lines 6 and 7

No numeric assertion or class M credit: the model left this line blank.

### classm.sli.3 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.4 — prompt sha256 aaa9864bb838dbf4d4b9579c38e6617f7108990dc597f250331f85194d959b20; branches: sli.has:false, sli.line1:left, sli.line5#0, sli.over:false, sli.divisor#0, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.4 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $50,121.00

### classm.sli.4 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $50,121.00

### classm.sli.4 — 5 — Enter the amount shown below for your filing status. Single, head of household,
Status: **AGREE**

Value: $85,000.00

### classm.sli.4 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 4 (50,121.00) not more than line 5 (85,000): No; skip lines 6 and 7

No numeric assertion or class M credit: the model left this line blank.

### classm.sli.4 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.5 — prompt sha256 eec877c7afc4bb72a2f1c640dd0938b8c2168eb889b06575d213db030376e7df; branches: sli.has:false, sli.line1:left, sli.line5#4, sli.over:false, sli.divisor#4, sli.line8#1, sli.line9:floor, sli.deduction#1

### classm.sli.5 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $2,137.00

### classm.sli.5 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $2,137.00

### classm.sli.5 — 5 — Enter the amount shown below for your filing status. Single, head of household,
Status: **AGREE**

Value: $85,000.00

### classm.sli.5 — 6 — Subtract line 5 from line 4
Status: **SKIPPED**

Model: blank
Work: Line 4 (2,137.00) not more than line 5 (85,000): No, so skip lines 6 and 7

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
    work: "Qualified student loan interest paid $0.00; under the $2,500 cap"
  - printed: "2"
    value: "51731.00"
    work: "Form 1040 line 9 = 51,731.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 given: 0+0+0+0+0+0+0+0+0 = 0.00 (lines 12, 14, 23 not given, taken as 0)"
  - printed: "4"
    value: "51731.00"
    work: "51,731.00 - 0.00 = 51,731.00"
  - printed: "5"
    value: "0.00"
    work: "No amount is printed for married filing separately (MFS can't take this deduction), so 0"
  - printed: "6"
    value: "51731.00"
    work: "Line 4 is more than line 5, so Yes: 51,731.00 - 0.00 = 51,731.00"
  - printed: "8"
    value: "0.00"
    work: "Line 7 = 51,731/15,000, capped at 1.000; 0.00 x 1.000 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00; also not allowed for married filing separately"
```
```

### classm.sli.2

```yaml
lines:
  - printed: "1"
    value: "2500.00"
    work: "smaller of interest paid 3,000.00 and cap 2,500.00 = 2,500.00"
  - printed: "2"
    value: "95460.00"
    work: "Form 1040 line 9 = 95,460.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 all 0.00 (line 23 not given; treated as 0) = 0.00"
  - printed: "4"
    value: "95460.00"
    work: "95,460.00 - 0.00 = 95,460.00"
  - printed: "5"
    value: "170000.00"
    work: "Married filing jointly = 170,000.00"
  - printed: "6"
    value: ""
    work: "line 4 95,460.00 not more than line 5 170,000.00 -> No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "No on line 6 -> enter -0- on line 8"
  - printed: "9"
    value: "2500.00"
    work: "2,500.00 - 0.00 = 2,500.00"
```

### classm.sli.3

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Qualified student loan interest paid $0.00 (cap $2,500)"
  - printed: "2"
    value: "32936.00"
    work: "Form 1040 line 9 = 32,936.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 = 0+0+0+0+0+0+0+0+0 = 0.00"
  - printed: "4"
    value: "32936.00"
    work: "32,936.00 - 0.00 = 32,936.00"
  - printed: "5"
    value: "85000.00"
    work: "Head of household = $85,000"
  - printed: "6"
    value: ""
    work: "Line 4 (32,936) not more than line 5 (85,000): No, skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer No: enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```

### classm.sli.4

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Qualified student loan interest paid $0.00; not more than $2,500"
  - printed: "2"
    value: "50121.00"
    work: "Form 1040, line 9 = $50,121.00"
  - printed: "3"
    value: "0.00"
    work: "Sched 1 lines 11-20, 23, 25 = 0+0+0+0+0+0+0+0+0+0 = $0.00"
  - printed: "4"
    value: "50121.00"
    work: "50,121.00 - 0.00 = 50,121.00"
  - printed: "5"
    value: "85000.00"
    work: "Single = $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (50,121.00) not more than line 5 (85,000): No; skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answered No: enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```
```

### classm.sli.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Qualified student loan interest paid $0.00 (limit $2,500)"
  - printed: "2"
    value: "2137.00"
    work: "Form 1040, line 9 = $2,137.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11-20, 23, 25 = 0+0+0+0+0+0+0+0+0+0 = $0.00"
  - printed: "4"
    value: "2137.00"
    work: "2,137.00 - 0.00 = 2,137.00"
  - printed: "5"
    value: "85000.00"
    work: "Qualifying surviving spouse = $85,000"
  - printed: "6"
    value: ""
    work: "Line 4 (2,137.00) not more than line 5 (85,000): No, so skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answered No, so enter -0-"
  - printed: "9"
    value: "0.00"
    work: "Line 1 minus line 8: 0.00 - 0.00 = 0.00"
```
```
