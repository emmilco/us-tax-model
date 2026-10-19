# Class M hand-work — otjob

`Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### case classm.otjob.1 — prompt sha256 0ca5fd773e809c572c5ec2500013bcec6a3bbb3c667f985941401aa7443c7156; branches: otjob.flsa:false, otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#1, otjob.col_b#0, otjob.col_b#1

### classm.otjob.1 — otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.1 — otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $5,301.00

### classm.otjob.1 — otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $5,301.00

### classm.otjob.1 — otjob[ot_2].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $0.00

### case classm.otjob.2 — prompt sha256 22bf53c71137d87c3295c8421c3f28426c0b272e28096cce2a1675bf354db8dc; branches: otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#0, otjob.figured#2, otjob.col_b#1

### classm.otjob.2 — otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.2 — otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $0.00

### classm.otjob.2 — otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $0.00

### classm.otjob.2 — otjob[ot_2].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.2 — otjob[ot_2].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $8,548.00

### classm.otjob.2 — otjob[ot_2].by_third — Method 2. Divide the total pay for overtime hours by three (3)
Status: **AGREE**

Value: $8,548.00

### classm.otjob.2 — otjob[ot_2].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $8,548.00

### case classm.otjob.3 — prompt sha256 22f707d783f69572853d834044cdd158b01ac09616944708254bbf8d238ff740; branches: otjob.flsa:true, otjob.special_rule:false, otjob.refused:false, otjob.figured#3, otjob.figured#4, otjob.col_b#1

### classm.otjob.3 — otjob[ot_1].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.3 — otjob[ot_1].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $0.00

### classm.otjob.3 — otjob[ot_1].by_quarter — Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
Status: **AGREE**

Value: $0.00

### classm.otjob.3 — otjob[ot_1].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $0.00

### classm.otjob.3 — otjob[ot_2].refused — Overtime figured by a method, rate or rule outside this tool
Status: **AGREE**

Value: no

### classm.otjob.3 — otjob[ot_2].figured — FLSA Overtime Premium from this employer, by the method chosen
Status: **AGREE**

Value: $411.00

### classm.otjob.3 — otjob[ot_2].by_half — Method 3 at double time. Multiply the pay above the regular rate for overtime ho
Status: **AGREE**

Value: $411.00

### classm.otjob.3 — otjob[ot_2].col_b — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

Value: $411.00

## Raw responses

### classm.otjob.1

```yaml
lines:
  - printed: "otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible employee under general rule in section 7(a) (no other overtime rule); premium method is within the instructions"
  - printed: "otjob[ot_1].figured"
    value: "5301.00"
    work: "Method 1 / Notice 2025-69 (A): FLSA Overtime Premium separately shown = $5,301.00"
  - printed: "otjob[ot_1].col_b"
    value: "5301.00"
    work: "Qualified overtime included in W-2 box 1 from this employer = figured amount $5,301.00"
  - printed: "otjob[ot_2].col_b"
    value: "0.00"
    work: "Not an FLSA-eligible employee; overtime is not qualified overtime compensation, so enter 0"
```

### classm.otjob.2

```yaml
lines:
  - printed: "otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible, general section 7(a) rule, employer-reported amount (Method 1, or a statement given on request): the tool covers this case"
  - printed: "otjob[ot_1].figured"
    value: "0.00"
    work: "Employer-reported FLSA Overtime Premium is $0.00, and you can rely on the employer's figure"
  - printed: "otjob[ot_1].col_b"
    value: "0.00"
    work: "Column (b) is the qualified overtime figured for this employer: $0.00"
  - printed: "otjob[ot_2].refused"
    value: "no"
    work: "FLSA-eligible, general section 7(a) rule, total pay for overtime hours at time-and-a-half (Method 2): the tool covers this case"
  - printed: "otjob[ot_2].by_third"
    value: "8548.00"
    work: "Method 2: $25,644.00 / 3 = $8,548.00"
  - printed: "otjob[ot_2].figured"
    value: "8548.00"
    work: "FLSA Overtime Premium under Method 2 = $8,548.00"
  - printed: "otjob[ot_2].col_b"
    value: "8548.00"
    work: "Column (b) is the qualified overtime figured for this employer: $8,548.00"
```

### classm.otjob.3

```yaml
```yaml
lines:
  - printed: "otjob[ot_1].refused"
    value: "no"
    work: "FLSA-eligible, general section 7(a) rule, Method 4 (double time) chosen; method is handled here"
  - printed: "otjob[ot_1].figured"
    value: "0.00"
    work: "Method 4 result: by_quarter = 0.00"
  - printed: "otjob[ot_1].by_quarter"
    value: "0.00"
    work: "Total pay for overtime hours 0.00 x 1/4 = 0.00"
  - printed: "otjob[ot_1].col_b"
    value: "0.00"
    work: "Column (b) = FLSA Overtime Premium figured, 0.00"
  - printed: "otjob[ot_2].refused"
    value: "no"
    work: "FLSA-eligible, general section 7(a) rule, Method 3 (double time) chosen; method is handled here"
  - printed: "otjob[ot_2].figured"
    value: "411.00"
    work: "Method 3 result: by_half = 411.00"
  - printed: "otjob[ot_2].by_half"
    value: "411.00"
    work: "Pay above the regular rate for overtime hours 822.00 x 1/2 = 411.00"
  - printed: "otjob[ot_2].col_b"
    value: "411.00"
    work: "Column (b) = FLSA Overtime Premium figured, 411.00; the joint-return requirement for married filers is applied on Schedule 1-A"
```
```
