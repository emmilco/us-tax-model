# Class M hand-work — sli

`Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 5 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.sli.1 — prompt sha256 38724804ac6fd459c777e27c8f1408141fb289292a47354b0b7908ed43d8962f; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#3, sli.over:false, sli.divisor#3, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

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
Work: Line 4 (32,936.00) is not more than line 5 (85,000.00): No, so skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.1 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.1 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.2 — prompt sha256 ad8c883cd31130a50470b21c980544345d009850f89ec495ece009feff578b7e; branches: sli.has:true, sli.claimed:false, sli.line1:right, sli.line5#2, sli.over:true, sli.divisor#2, sli.line8#0, sli.line9:positive, sli.eligible:false, sli.allowed#1, sli.deduction#0

### classm.sli.2 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $2,500.00

### classm.sli.2 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $13,294.00

### classm.sli.2 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $13,294.00

### classm.sli.2 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $0.00

### classm.sli.2 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $13,294.00
Model: $0.00
Work: Skipped because line 5 has no amount for married filing separately

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.2 — 8 — Multiply line 1 by line 7
Status: **DISAGREE**

Project: $2,215.00
Model: $0.00
Work: Skipped because the phaseout doesn't apply; the deduction isn't allowed for married filing separately

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.2 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **DISAGREE**

Project: $285.00
Model: $0.00
Work: Line 21 instructions: no deduction if married filing separately, so $0 goes to Schedule 1, line 21

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### case classm.sli.3 — prompt sha256 c4a367c87980bc5e1ff5e15917f1049c9a4f1c98b2df2a8401a740aace548897; branches: sli.has:false, sli.claimed:true, sli.line1:left, sli.line5#4, sli.over:false, sli.divisor#4, sli.line8#1, sli.line9:floor, sli.eligible:false, sli.allowed#1, sli.deduction#1

### classm.sli.3 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $62,208.00

### classm.sli.3 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $62,208.00

### classm.sli.3 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.3 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-22,792.00
Model: $0.00
Work: Line 4 (62,208) is not more than line 5 (85,000): No, so skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.3 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.3 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.4 — prompt sha256 7a1193d5f6156ec4fb44d133f58558fdbf13ee2b1c4493e7cdd3e2d7f0936dc5; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#0, sli.over:false, sli.divisor#0, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.4 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $40,807.00

### classm.sli.4 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $40,807.00

### classm.sli.4 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $85,000.00

### classm.sli.4 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-44,193.00
Model: $0.00
Work: Line 4 (40,807) is not more than line 5 (85,000), so No: skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.4 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.4 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

### case classm.sli.5 — prompt sha256 3d701ad445735884924a5caeab5b8e842de4fca2628381cec088a1ba3a18d2ad; branches: sli.has:false, sli.claimed:false, sli.line1:left, sli.line5#1, sli.over:false, sli.divisor#1, sli.line8#1, sli.line9:floor, sli.eligible:true, sli.allowed#0, sli.deduction#1

### classm.sli.5 — 1 — Enter the total interest you paid in 2025 on qualified student loans (see the in
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

Value: $6,724.00

### classm.sli.5 — 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 4 — Subtract line 3 from line 2
Status: **AGREE**

Value: $6,724.00

### classm.sli.5 — 5 — Enter the amount shown below for your filing status. Single, head of household, 
Status: **AGREE**

Value: $170,000.00

### classm.sli.5 — 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project: $-163,276.00
Model: $0.00
Work: Line 4 (6,724) not more than line 5 (170,000); No: skip lines 6 and 7

Ruling: representation; project retained; model value dropped from the fixture. The project figures every worksheet line: line 6 (line 4 less line 5) also when line 4 is not more than line 5, where the worksheet skips it, and the worksheet lines for a married filer filing separately, who cannot take the deduction. Line 8 uses line 6 only when line 4 is more than line 5, and the deduction (sli.deduction, which Schedule 1 line 21 copies) is zero for a married filer filing separately; on every case the model and the project agree on the deduction. [dropped]

### classm.sli.5 — 8 — Multiply line 1 by line 7
Status: **AGREE**

Value: $0.00

### classm.sli.5 — 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result h
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.sli.1

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00, which is under the $2,500 cap"
  - printed: "2"
    value: "32936.00"
    work: "Form 1040 line 9 = 32,936.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 line 11 0.00 + line 13 0.00; no other lines 11-20, 23, 25 given = 0.00"
  - printed: "4"
    value: "32936.00"
    work: "32,936.00 - 0.00 = 32,936.00"
  - printed: "5"
    value: "85000.00"
    work: "Head of household = $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (32,936.00) is not more than line 5 (85,000.00): No, so skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answer No, so enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```

### classm.sli.2

```yaml
```yaml
lines:
  - printed: "1"
    value: "2500.00"
    work: "Smaller of interest paid $2,690.00 or the $2,500 cap"
  - printed: "2"
    value: "13294.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1 lines 11–20, 23, 25: line 11 $0 + line 13 $0; no other amounts given = $0"
  - printed: "4"
    value: "13294.00"
    work: "13,294.00 − 0.00"
  - printed: "5"
    value: "blank"
    work: "The worksheet lists no amount for married filing separately; this status can't take the deduction"
  - printed: "6"
    value: "blank"
    work: "Skipped because line 5 has no amount for married filing separately"
  - printed: "8"
    value: "blank"
    work: "Skipped because the phaseout doesn't apply; the deduction isn't allowed for married filing separately"
  - printed: "9"
    value: "0.00"
    work: "Line 21 instructions: no deduction if married filing separately, so $0 goes to Schedule 1, line 21"
```
```

### classm.sli.3

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Qualified student loan interest paid is $0.00 (under the $2,500 cap). You also can't take this deduction because someone else claims you as a dependent."
  - printed: "2"
    value: "62208.00"
    work: "Form 1040, line 9 = 62,208.00"
  - printed: "3"
    value: "0.00"
    work: "Schedule 1, lines 11 (0.00) + 13 (0.00); no amounts were given for the other lines, so they count as 0 = 0.00"
  - printed: "4"
    value: "62208.00"
    work: "62,208.00 - 0.00 = 62,208.00"
  - printed: "5"
    value: "85000.00"
    work: "Qualifying surviving spouse = $85,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (62,208) is not more than line 5 (85,000): No, so skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "The No answer on line 6 says to enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00; goes on Schedule 1, line 21"
```

### classm.sli.4

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid $0.00; that is under the $2,500 cap"
  - printed: "2"
    value: "40807.00"
    work: "Form 1040, line 9"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11 through 20, 23 and 25: line 11 0 + line 13 0, no other amounts given = 0.00"
  - printed: "4"
    value: "40807.00"
    work: "40,807.00 - 0.00"
  - printed: "5"
    value: "85000.00"
    work: "Single filer, so $85,000"
  - printed: "6"
    value: ""
    work: "Line 4 (40,807) is not more than line 5 (85,000), so No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "Line 6 answered No, so enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00, carried to Schedule 1, line 21"
```

### classm.sli.5

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Interest paid on qualified student loans $0.00; not more than $2,500"
  - printed: "2"
    value: "6724.00"
    work: "Form 1040 line 9 = $6,724.00"
  - printed: "3"
    value: "0.00"
    work: "Sch 1 lines 11 ($0) + 13 ($0); no other amounts given for lines 11-20, 23, 25 = $0.00"
  - printed: "4"
    value: "6724.00"
    work: "6,724.00 - 0.00 = 6,724.00"
  - printed: "5"
    value: "170000.00"
    work: "Married filing jointly = $170,000"
  - printed: "6"
    value: "blank"
    work: "Line 4 (6,724) not more than line 5 (170,000); No: skip lines 6 and 7"
  - printed: "8"
    value: "0.00"
    work: "No on line 6: enter -0- on line 8"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00; to Schedule 1, line 21"
```
```
