# Class M hand-work — person

`Excess Social Security credit — separately per person` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### case classm.person.1 — prompt sha256 ee0699c65131123fb3c4c00af0ae8a45174f5f7383432be87904c3a1dc44994c; branches: person.rrta:false, person.over:false, person.eligible:true, person.excess:positive, person.credit#0

### classm.person.1 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 2

### classm.person.1 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.1 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.1 — person[taxpayer].wages — Total w2.wages for this person
Status: **AGREE**

Value: $192,146.00

### classm.person.1 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $11,913.00

### classm.person.1 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $384,468.00

### classm.person.1 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $59,275.00

### classm.person.1 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: yes

### classm.person.1 — person[taxpayer].excess — Withholding above $10,918.20, if any
Status: **AGREE**

Value: $994.80

### classm.person.1 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $994.80

### classm.person.1 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $384,468.00

### classm.person.1 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $7,091.00

### case classm.person.2 — prompt sha256 53aeaaf89a86096139cf1cfbe44559ca7324e0bc06f727b0209c506bba80e44f; branches: person.rrta:false, person.over:false, person.eligible:false, person.credit#1

### classm.person.2 — person[taxpayer].employers — Total w2.one for this person
Status: **AGREE**

Value: 1

### classm.person.2 — person[taxpayer].overcount — Number of employers that withheld more than the limit
Status: **AGREE**

Value: 0

### classm.person.2 — person[taxpayer].over — Any employer withheld more than the limit
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].withheld — Total w2.box4 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].box1 — Total W-2 box 1 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].box2 — Total W-2 box 2 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

Value: no

### classm.person.2 — person[taxpayer].credit — Excess social security tax withheld, figured separately for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

Value: $0.00

### classm.person.2 — person[taxpayer].medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.person.1

```yaml
lines:
  - printed: "person[taxpayer].employers"
    value: "2"
    work: "w2.one totals 1 (emp_a) + 1 (emp_b) = 2"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "Neither emp_a ($995.00) nor emp_b ($10,918.00) withheld more than $10,918.20"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount is 0, so no single employer withheld more than $10,918.20"
  - printed: "person[taxpayer].wages"
    value: "192146.00"
    work: "16,046.00 + 176,100.00 = 192,146.00"
  - printed: "person[taxpayer].withheld"
    value: "11913.00"
    work: "Box 4 total: 995.00 + 10,918.00 = 11,913.00"
  - printed: "person[taxpayer].box1"
    value: "384468.00"
    work: "16,046.00 + 368,422.00 = 384,468.00"
  - printed: "person[taxpayer].box2"
    value: "59275.00"
    work: "4,012.00 + 55,263.00 = 59,275.00"
  - printed: "person[taxpayer].eligible"
    value: "yes"
    work: "2 employers and total wages of 192,146.00, which is more than 176,100 (1040 line 11 instructions)"
  - printed: "person[taxpayer].excess"
    value: "994.80"
    work: "11,913.00 - 10,918.20 = 994.80"
  - printed: "person[taxpayer].credit"
    value: "994.80"
    work: "Eligible, no single employer withheld too much, and there is no railroad pay, so the credit is the excess of 994.80"
  - printed: "person[taxpayer].medicare5"
    value: "384468.00"
    work: "16,046.00 + 368,422.00 = 384,468.00"
  - printed: "person[taxpayer].medicare6"
    value: "7091.00"
    work: "233.00 + 6,858.00 = 7,091.00"
```

### classm.person.2

```yaml
lines:
  - printed: "person[taxpayer].employers"
    value: "1"
    work: "One W-2 entry (emp_a); sum of w2.one = 1"
  - printed: "person[taxpayer].overcount"
    value: "0"
    work: "emp_a did not withhold more than $10,918.20; count = 0"
  - printed: "person[taxpayer].over"
    value: "no"
    work: "overcount 0, so no employer withheld more than $10,918.20"
  - printed: "person[taxpayer].withheld"
    value: "0.00"
    work: "Sum of box 4 = $0.00"
  - printed: "person[taxpayer].box1"
    value: "0.00"
    work: "Sum of box 1 = $0.00"
  - printed: "person[taxpayer].box2"
    value: "0.00"
    work: "Sum of box 2 = $0.00"
  - printed: "person[taxpayer].eligible"
    value: "no"
    work: "1040 line 11 needs more than one employer and wages over $176,100; there is 1 employer and $0 wages"
  - printed: "person[taxpayer].credit"
    value: "0.00"
    work: "Not eligible, so no credit; also $0 withheld is not over $10,918.20"
  - printed: "person[taxpayer].medicare5"
    value: "0.00"
    work: "Sum of box 5 = $0.00"
  - printed: "person[taxpayer].medicare6"
    value: "0.00"
    work: "Sum of box 6 = $0.00"
```
