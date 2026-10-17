# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### case classm.sa.1 — prompt sha256 1ce75889391d785f45898fbc1669ceb6dae9093da941000a0f53e7162600838d; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#1, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.1 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $388,706.00

### classm.sa.1 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $29,152.95

### classm.sa.1 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $51,164.00

### classm.sa.1 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $40,000.00

### classm.sa.1 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $40,000.00

### classm.sa.1 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $8,729.00

### classm.sa.1 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $8,729.00

### classm.sa.1 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $48,729.00

### case classm.sa.2 — prompt sha256 7ec036dd05b981bd4568c8688bcdd537e942db9a1e6c9644a2246c3212a6c1fc; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.form8283:true, sa.extra_age65#1, sa.extra_blind#1, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $445,816.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $33,436.20

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $9,499.00

### classm.sa.2 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $5,000.00

### classm.sa.2 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $5,000.00

### classm.sa.2 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $6,110.00

### classm.sa.2 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $6,110.00

### classm.sa.2 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $2,433.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $2,433.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $13,543.00

### case classm.sa.3 — prompt sha256 14911f2c8b34fcc708eeb2d693d7a47e27574e7ee1b001639900ad6d09c42c7e; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:true, sa.age65:false, sa.blind:false, sa.spouse_itemizes:true, sa.elect_itemize:true, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $240,235.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $18,017.63

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $6,888.37

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $3,817.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $3,817.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $10,705.37

### case classm.sa.4 — prompt sha256 c5389e2e7c184016042ea877fd5961734f1dce3bd56c149676d2841bb963f9cc; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#1, sa.standard#0, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:true

### classm.sa.4 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $-1,500.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $-112.50

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $581.50

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $51,019.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $20,000.00

### classm.sa.4 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $20,000.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $8,460.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $29,041.50

### case classm.sa.5 — prompt sha256 0cc56632d2e9a3668c85159dcdaab833411f30c730186704915d4ea445ce013d; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#0, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $196,544.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $14,740.80

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $27,813.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $27,813.00

### classm.sa.5 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $27,813.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $10,277.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $10,277.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $38,090.00

### case classm.sa.6 — prompt sha256 7a42e5b732f448565fd6b713608313e95e7e4fd1559695603a5669c031d9c68d; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:true, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:true, sa.extra_age65#0, sa.extra_blind#1, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $70,577.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $5,293.28

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $5,188.72

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $41,571.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 16 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $2,992.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $13,797.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $98,985.72

## Raw responses

### classm.sa.1

```yaml
lines:
  - printed: "2"
    value: "388706.00"
    work: "Form 1040 line 11b = 388,706.00"
  - printed: "3"
    value: "29152.95"
    work: "388,706.00 x 0.075 = 29,152.95"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 29,152.95 is below zero, so enter -0-"
  - printed: "5d"
    value: "51164.00"
    work: "47,577.00 + 3,587.00 + 0.00 = 51,164.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI 388,706 <= 500,000 and no 2555/4563/PR; smaller of 51,164.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "8729.00"
    work: "8,729.00 + 0.00 + 0.00 = 8,729.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "8729.00"
    work: "8,729.00 + 0.00 = 8,729.00"
  - printed: "12"
    value: "0.00"
    work: "No supported noncash donations were given"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "48729.00"
    work: "0.00 + 40,000.00 + 8,729.00 + 0.00 + 0.00 + 0.00 = 48,729.00"
```

### classm.sa.2

```yaml
```yaml
lines:
  - printed: "2"
    value: "445816.00"
    work: "Form 1040 line 11b = 445,816.00"
  - printed: "3"
    value: "33436.20"
    work: "445,816.00 x 0.075 = 33,436.20"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 33,436.20 < 0, enter -0-"
  - printed: "5d"
    value: "9499.00"
    work: "0.00 + 9,499.00 + 0.00 = 9,499.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS AGI 445,816 > 250,000 and 5d > 5,000, so use SALT worksheet: L6 445,816-250,000=195,816; L7 x0.30=58,744.80; L8 40,000-58,744.80=-18,744.80; L9 larger with 10,000=10,000; L10 smaller of half (5,000) or 9,499 = 5,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes, zero"
  - printed: "8b"
    value: "0.00"
    work: "None reported, zero"
  - printed: "8c"
    value: "0.00"
    work: "None reported, zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover, zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty loss, zero"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions, zero"
  - printed: "7"
    value: "5000.00"
    work: "5,000.00 + 0.00 = 5,000.00"
  - printed: "8e"
    value: "6110.00"
    work: "6,110.00 + 0.00 + 0.00 = 6,110.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "6110.00"
    work: "6,110.00 + 0.00 = 6,110.00"
  - printed: "12"
    value: "2433.00"
    work: "0.00 + 2,433.00 = 2,433.00"
  - printed: "14"
    value: "2433.00"
    work: "0.00 + 2,433.00 + 0.00 = 2,433.00"
  - printed: "17"
    value: "13543.00"
    work: "0.00 + 5,000.00 + 6,110.00 + 2,433.00 + 0.00 + 0.00 = 13,543.00"
```
```

### classm.sa.3

```yaml
lines:
  - printed: "2"
    value: "240235.00"
    work: "Form 1040 line 11b = 240,235.00"
  - printed: "3"
    value: "18017.63"
    work: "240,235.00 x 0.075 = 18,017.625, rounded to 18,017.63"
  - printed: "4"
    value: "6888.37"
    work: "24,906.00 - 18,017.63 = 6,888.37"
  - printed: "5d"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "5e"
    value: "0.00"
    work: "smaller of 0 or $40,000 (Single; line 11b not over $500,000) = 0"
  - printed: "6"
    value: "0.00"
    work: "no other taxes reported"
  - printed: "8b"
    value: "0.00"
    work: "no mortgage interest outside Form 1098"
  - printed: "8c"
    value: "0.00"
    work: "no points outside Form 1098"
  - printed: "13"
    value: "0.00"
    work: "no carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "no casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "no other itemized deductions"
  - printed: "7"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "8e"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "9"
    value: "3817.00"
    work: "Form 4952 line 8 = 3,817.00"
  - printed: "10"
    value: "3817.00"
    work: "0 + 3,817.00 = 3,817.00"
  - printed: "12"
    value: "0.00"
    work: "no supported noncash gifts given"
  - printed: "14"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "17"
    value: "10705.37"
    work: "6,888.37 + 0 + 3,817.00 + 0 + 0 + 0 = 10,705.37"
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "-1500.00"
    work: "Form 1040 line 11b = -1,500.00"
  - printed: "3"
    value: "-112.50"
    work: "-1,500.00 x 0.075 = -112.50"
  - printed: "4"
    value: "581.50"
    work: "469.00 - (-112.50) = 581.50; line 3 is not more than line 1"
  - printed: "5d"
    value: "51019.00"
    work: "45,223.00 + 5,796.00 + 0.00 = 51,019.00"
  - printed: "5e"
    value: "20000.00"
    work: "MFS, line 11b not over $250,000, no 2555/4563/PR; smaller of 51,019.00 or 20,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes; zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover; zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty/theft loss; zero"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions; zero"
  - printed: "7"
    value: "20000.00"
    work: "20,000.00 + 0.00 = 20,000.00"
  - printed: "8e"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "12"
    value: "0.00"
    work: "gift[item_a] 0.00 = 0.00"
  - printed: "14"
    value: "8460.00"
    work: "8,460.00 + 0.00 + 0.00 = 8,460.00"
  - printed: "17"
    value: "29041.50"
    work: "581.50 + 20,000.00 + 0.00 + 8,460.00 + 0.00 + 0.00 = 29,041.50"
```
```

### classm.sa.5

```yaml
lines:
  - printed: "2"
    value: "196544.00"
    work: "Form 1040 line 11b = 196,544.00"
  - printed: "3"
    value: "14740.80"
    work: "196,544.00 x 0.075 = 14,740.80"
  - printed: "4"
    value: "0.00"
    work: "Line 1 is 0.00 and line 3 is 14,740.80, so line 3 is more than line 1; enter -0-"
  - printed: "5d"
    value: "27813.00"
    work: "15,883.00 + 11,930.00 + 0.00 = 27,813.00"
  - printed: "5e"
    value: "27813.00"
    work: "AGI of 196,544 is not over 500,000 and no Form 2555, Form 4563 or Puerto Rico income; smaller of 27,813.00 or 40,000 (MFJ) = 27,813.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or generation-skipping tax; 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year; 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; 0"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions; 0"
  - printed: "7"
    value: "27813.00"
    work: "27,813.00 + 0.00 = 27,813.00"
  - printed: "8e"
    value: "10277.00"
    work: "10,277.00 + 0.00 + 0.00 = 10,277.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "10277.00"
    work: "10,277.00 + 0.00 = 10,277.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations were given; 0"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "38090.00"
    work: "0.00 + 27,813.00 + 10,277.00 + 0.00 + 0.00 + 0.00 = 38,090.00"
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "70577.00"
    work: "Form 1040 line 11b = 70,577.00"
  - printed: "3"
    value: "5293.28"
    work: "70,577.00 x 0.075 = 5,293.275, rounded to 5,293.28"
  - printed: "4"
    value: "5188.72"
    work: "10,482.00 - 5,293.28 = 5,188.72"
  - printed: "5d"
    value: "41571.00"
    work: "30,729.00 + 10,842.00 + 0.00 = 41,571.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI <= 500,000 and no 2555/4563/PR; smaller of 41,571.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes = 0"
  - printed: "8b"
    value: "0.00"
    work: "None = 0"
  - printed: "8c"
    value: "0.00"
    work: "None = 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty loss = 0"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions = 0"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "40000.00"
    work: "40,000.00 + 0.00 + 0.00 = 40,000.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "12"
    value: "2992.00"
    work: "Noncash gift item_a = 2,992.00"
  - printed: "14"
    value: "13797.00"
    work: "10,805.00 + 2,992.00 + 0.00 = 13,797.00"
  - printed: "17"
    value: "98985.72"
    work: "5,188.72 + 40,000.00 + 40,000.00 + 13,797.00 + 0 + 0 = 98,985.72"
```
```
