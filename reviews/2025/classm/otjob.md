# Class M hand-work — otjob

`Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### case classm.otjob.1 — prompt sha256 a66a30b4b3e8332af540a9fae180545934a7e6bc55b586d83e39c30476f9b326; branches: otjob.flsa:false, otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#0, otjob.figured#1, otjob.figured#5, otjob.col_b#0, otjob.col_b#1

### classm.otjob.1 — person[spouse].otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.1 — person[spouse].otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[spouse].otjob[ot_1].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[spouse].otjob[ot_1].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[spouse].otjob[ot_1].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[spouse].otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[taxpayer].otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **DISAGREE**

Project: no
Model: yes
Work: Method 'other' is outside the tool; the filer is also FLSA-ineligible

Ruling: representation; project retained; model value dropped from the fixture. An employee who is not FLSA-eligible has no qualified overtime compensation (Notice 2025-69, pp. 22-25; i1040gi p. 106), so the project enters $0 for this employer and the method question does not arise; the model also refused the method. The employer's column (b) and line 14a agree. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[taxpayer].otjob[ot_1].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **DISAGREE**

Project: $10,977.00
Model: $0.00
Work: Method 2 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_1].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **DISAGREE**

Project: $16,465.50
Model: $0.00
Work: Method 3 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_1].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **DISAGREE**

Project: $8,232.75
Model: $0.00
Work: Method 4 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $0.00

### classm.otjob.1 — person[taxpayer].otjob[ot_2].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.1 — person[taxpayer].otjob[ot_2].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $11,471.00

### classm.otjob.1 — person[taxpayer].otjob[ot_2].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **DISAGREE**

Project: $3,823.67
Model: $0.00
Work: Method 2 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_2].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **DISAGREE**

Project: $5,735.50
Model: $0.00
Work: Method 3 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_2].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **DISAGREE**

Project: $2,867.75
Model: $0.00
Work: Method 4 not chosen; no amount

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.1 — person[taxpayer].otjob[ot_2].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $11,471.00

### case classm.otjob.2 — prompt sha256 036f133a24f84eaada6ea637012622af98255f2ae8be09c93bdc1cd1fd31800b; branches: otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#2, otjob.figured#3, otjob.col_b#1

### classm.otjob.2 — person[taxpayer].otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.2 — person[taxpayer].otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $1,722.00

### classm.otjob.2 — person[taxpayer].otjob[ot_1].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **AGREE**

Value: $1,722.00

### classm.otjob.2 — person[taxpayer].otjob[ot_1].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **DISAGREE**

Project: $2,583.00
Model: $0.00
Work: Method 3 not chosen for this employer

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.2 — person[taxpayer].otjob[ot_1].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **DISAGREE**

Project: $1,291.50
Model: $0.00
Work: Method 4 not chosen for this employer

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.2 — person[taxpayer].otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $1,722.00

### classm.otjob.2 — person[taxpayer].otjob[ot_2].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.2 — person[taxpayer].otjob[ot_2].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $9,550.50

### classm.otjob.2 — person[taxpayer].otjob[ot_2].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **DISAGREE**

Project: $6,367.00
Model: $0.00
Work: Method 2 not chosen for this employer

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.2 — person[taxpayer].otjob[ot_2].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **AGREE**

Value: $9,550.50

### classm.otjob.2 — person[taxpayer].otjob[ot_2].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **DISAGREE**

Project: $4,775.25
Model: $0.00
Work: Method 4 not chosen for this employer

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.2 — person[taxpayer].otjob[ot_2].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $9,550.50

### case classm.otjob.3 — prompt sha256 4ce9e4bc0a81ef0ef2d215259663d3fb80b3b593b8cba3cb2f43c701e83f1855; branches: otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#4, otjob.col_b#1

### classm.otjob.3 — person[taxpayer].otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.3 — person[taxpayer].otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $4,600.75

### classm.otjob.3 — person[taxpayer].otjob[ot_1].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **DISAGREE**

Project: $6,134.33
Model: $0.00
Work: Method 2 not chosen (filer chose total_double)

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.3 — person[taxpayer].otjob[ot_1].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **DISAGREE**

Project: $9,201.50
Model: $0.00
Work: Method 3 not chosen (filer chose total_double)

Ruling: representation; project retained; model value dropped from the fixture. The line is the amount under a method the filer did not choose for this employer; the project figures every method's helper and column (b) reads only the chosen one (Notice 2025-69 Section III.B.2, pp. 22-25). Column (b) agrees. [dropped]

### classm.otjob.3 — person[taxpayer].otjob[ot_1].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **AGREE**

Value: $4,600.75

### classm.otjob.3 — person[taxpayer].otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $4,600.75

## Raw responses

### classm.otjob.1

```yaml
```yaml
lines:
  - printed: "person[spouse].otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible, general 7(a) rule, premium method (paragraph 1) is within the tool"
  - printed: "person[spouse].otjob[ot_1].figured"
    value: "0.00"
    work: "Paragraph 1: separately shown FLSA Overtime Premium = $0.00"
  - printed: "person[spouse].otjob[ot_1].by_third"
    value: "0.00"
    work: "Method 2 not chosen; no amount"
  - printed: "person[spouse].otjob[ot_1].by_half"
    value: "0.00"
    work: "Method 3 not chosen; no amount"
  - printed: "person[spouse].otjob[ot_1].by_quarter"
    value: "0.00"
    work: "Method 4 not chosen; no amount"
  - printed: "person[spouse].otjob[ot_1].col_b"
    value: "0.00"
    work: "Column (b) = figured premium $0.00"
  - printed: "person[taxpayer].otjob[ot_1].refused"
    value: "yes"
    work: "Method 'other' is outside the tool; the filer is also FLSA-ineligible"
  - printed: "person[taxpayer].otjob[ot_1].figured"
    value: "0.00"
    work: "FLSA-ineligible employee: overtime is not qualified overtime compensation"
  - printed: "person[taxpayer].otjob[ot_1].by_third"
    value: "0.00"
    work: "Method 2 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_1].by_half"
    value: "0.00"
    work: "Method 3 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_1].by_quarter"
    value: "0.00"
    work: "Method 4 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_1].col_b"
    value: "0.00"
    work: "Not FLSA-eligible, so none of the $32,931.00 is qualified overtime"
  - printed: "person[taxpayer].otjob[ot_2].refused"
    value: "no"
    work: "FLSA-eligible, general 7(a) rule, employer-reported amount may be relied on"
  - printed: "person[taxpayer].otjob[ot_2].figured"
    value: "11471.00"
    work: "Employer-provided FLSA Overtime Premium (W-2 box 14 or employer statement) relied on: $11,471.00"
  - printed: "person[taxpayer].otjob[ot_2].by_third"
    value: "0.00"
    work: "Method 2 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_2].by_half"
    value: "0.00"
    work: "Method 3 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_2].by_quarter"
    value: "0.00"
    work: "Method 4 not chosen; no amount"
  - printed: "person[taxpayer].otjob[ot_2].col_b"
    value: "11471.00"
    work: "Column (b) = employer-reported qualified overtime $11,471.00"
```
```

### classm.otjob.2

```yaml
lines:
  - printed: "person[taxpayer].otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible = yes; no rule other than 7(a); method 2 (total pay for OT hours at time-and-a-half) is a listed method"
  - printed: "person[taxpayer].otjob[ot_1].figured"
    value: "1722.00"
    work: "Method 2 result = by_third = 1722.00"
  - printed: "person[taxpayer].otjob[ot_1].by_third"
    value: "1722.00"
    work: "Method 2: 5166.00 / 3 = 1722.00"
  - printed: "person[taxpayer].otjob[ot_1].by_half"
    value: "0.00"
    work: "Method 3 not chosen for this employer"
  - printed: "person[taxpayer].otjob[ot_1].by_quarter"
    value: "0.00"
    work: "Method 4 not chosen for this employer"
  - printed: "person[taxpayer].otjob[ot_1].col_b"
    value: "1722.00"
    work: "Worksheet line 1, column (b) = figured qualified overtime 1722.00"
  - printed: "person[taxpayer].otjob[ot_2].refused"
    value: "no"
    work: "FLSA-eligible = yes; no rule other than 7(a); method 3 at double time is a listed method"
  - printed: "person[taxpayer].otjob[ot_2].figured"
    value: "9550.50"
    work: "Method 3 result = by_half = 9550.50"
  - printed: "person[taxpayer].otjob[ot_2].by_third"
    value: "0.00"
    work: "Method 2 not chosen for this employer"
  - printed: "person[taxpayer].otjob[ot_2].by_half"
    value: "9550.50"
    work: "Method 3 at double time: 19101.00 x 1/2 = 9550.50"
  - printed: "person[taxpayer].otjob[ot_2].by_quarter"
    value: "0.00"
    work: "Method 4 not chosen for this employer"
  - printed: "person[taxpayer].otjob[ot_2].col_b"
    value: "9550.50"
    work: "Worksheet line 1, column (b) = figured qualified overtime 9550.50"
```

### classm.otjob.3

```yaml
lines:
  - printed: "person[taxpayer].otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible employee, general section 7(a) rule applies, and the chosen method (paragraph 4, double time) is one of the listed methods"
  - printed: "person[taxpayer].otjob[ot_1].figured"
    value: "4600.75"
    work: "Method 4 at double time: 18,403.00 x 1/4 = 4,600.75"
  - printed: "person[taxpayer].otjob[ot_1].by_third"
    value: "0.00"
    work: "Method 2 not chosen (filer chose total_double)"
  - printed: "person[taxpayer].otjob[ot_1].by_half"
    value: "0.00"
    work: "Method 3 not chosen (filer chose total_double)"
  - printed: "person[taxpayer].otjob[ot_1].by_quarter"
    value: "4600.75"
    work: "Total pay for overtime hours at double time 18,403.00 x 1/4 = 4,600.75 (para 4; Notice 2025-69 (D))"
  - printed: "person[taxpayer].otjob[ot_1].col_b"
    value: "4600.75"
    work: "Qualified overtime from this employer = figured amount 4,600.75"
```
