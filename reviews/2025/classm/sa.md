# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | 7f4c8c493a59613863198e30bb448788826a174558e6089ec0810eefe3b25334 |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 34 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### case classm.sa.1 — prompt sha256 a112343da7dd5f81ad98c30b42f546342bfd20ef05e92667e6a890dce9f3e40a; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#1, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

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

### case classm.sa.2 — prompt sha256 21afc501cdf4dfe2aac620a5180923bcc0df608894c2e887d1ba04b11781adb2; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:left, sa.form8283:false, sa.extra_age65#1, sa.extra_blind#1, sa.standard#0, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:true

### classm.sa.2 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $401,587.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $30,119.03

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $3,848.00

### classm.sa.2 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $3,848.00

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

Value: $3,848.00

### classm.sa.2 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $405.00

### classm.sa.2 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $405.00

### classm.sa.2 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $4,481.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $8,734.00

### case classm.sa.3 — prompt sha256 5183161217e88a2e799b339001e2aa48f1666374719da555866bda09f3c41c4c; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:true, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:true, sa.extra_age65#0, sa.extra_blind#1, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $56,858.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $4,264.35

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $24,242.65

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $70,703.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $40,000.00

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

Value: $40,000.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $3,838.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $14,051.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $78,293.65

### case classm.sa.4 — prompt sha256 30aaa420f708fc8640a18f16c711065ebbab60e82ff2f983d18b5dac62e7c7a2; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:false, sa.age65:false, sa.blind:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:true, sa.extra_age65#1, sa.extra_blind#0, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $348,843.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $26,163.23

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $20,000.00

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

Value: $5,810.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $5,810.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $8,153.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $22,275.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $48,085.00

### case classm.sa.5 — prompt sha256 1fb8cfa46f65171065138356b84f80486e4e9846cbf80ec9a4b1f2cee1d19c86; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.age65:false, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:true, sa.extra_age65#1, sa.extra_blind#1, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $68,176.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $5,113.20

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $1,385.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $3,784.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $3,784.00

### case classm.sa.6 — prompt sha256 987014fc7ba9bb76d7c2f5238603e5513cf9a66a8fa8383102ed0df4bbfd5970; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:true, sa.age65:false, sa.blind:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:true, sa.extra_age65#1, sa.extra_blind#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $522,631.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $39,197.33

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $2,057.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $2,057.00

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

Value: $2,057.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $39,317.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $39,317.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $5,000.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $23,034.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $64,408.00

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
    work: "Line 11b is not over $500,000 and there is no 2555/4563/PR income; smaller of 51,164.00 or 40,000 = 40,000.00"
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
    work: "No carryover"
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
    work: "No noncash donations given"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "48729.00"
    work: "0.00 + 40,000.00 + 8,729.00 + 0.00 + 0.00 + 0.00 = 48,729.00"
```

### classm.sa.2

```yaml
lines:
  - printed: "2"
    value: "401587.00"
    work: "Form 1040 line 11b = 401,587.00"
  - printed: "3"
    value: "30119.03"
    work: "401,587.00 x 0.075 = 30,119.025, rounded to 30,119.03"
  - printed: "4"
    value: "0.00"
    work: "Line 1 (0.00) - line 3 (30,119.03) is less than zero, so enter -0-"
  - printed: "5d"
    value: "3848.00"
    work: "3,848.00 + 0.00 + 0.00 = 3,848.00"
  - printed: "5e"
    value: "3848.00"
    work: "AGI over $250,000 (MFS) sends you to the SALT worksheet; line 5d is $5,000 or less, so enter line 5d"
  - printed: "6"
    value: "0.00"
    work: "No foreign or generation-skipping tax was reported; zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; zero"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover; zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; zero"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions; zero"
  - printed: "7"
    value: "3848.00"
    work: "3,848.00 + 0.00 = 3,848.00"
  - printed: "8e"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "9"
    value: "405.00"
    work: "Form 4952 line 8 = 405.00"
  - printed: "10"
    value: "405.00"
    work: "0.00 + 405.00 = 405.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts were given; zero"
  - printed: "14"
    value: "4481.00"
    work: "4,481.00 + 0.00 + 0.00 = 4,481.00; no income limits apply"
  - printed: "17"
    value: "8734.00"
    work: "0.00 + 3,848.00 + 405.00 + 4,481.00 + 0.00 + 0.00 = 8,734.00"
```

### classm.sa.3

```yaml
```yaml
lines:
  - printed: "2"
    value: "56858.00"
    work: "Form 1040 line 11b = 56,858.00"
  - printed: "3"
    value: "4264.35"
    work: "56,858.00 x 0.075 = 4,264.35"
  - printed: "4"
    value: "24242.65"
    work: "28,507.00 - 4,264.35 = 24,242.65"
  - printed: "5d"
    value: "70703.00"
    work: "59,644.00 + 11,059.00 + 0.00 = 70,703.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI <= 500,000 and no 2555/4563/PR exclusion; smaller of 70,703.00 or 40,000 = 40,000.00"
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
    work: "No carryover"
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
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "12"
    value: "3838.00"
    work: "gift[item_a] 3,838.00"
  - printed: "14"
    value: "14051.00"
    work: "10,213.00 + 3,838.00 + 0.00 = 14,051.00"
  - printed: "17"
    value: "78293.65"
    work: "24,242.65 + 40,000.00 + 0.00 + 14,051.00 + 0.00 + 0.00 = 78,293.65"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "348843.00"
    work: "Form 1040 line 11b = 348,843.00"
  - printed: "3"
    value: "26163.23"
    work: "348,843.00 x 0.075 = 26,163.225, rounded to 26,163.23"
  - printed: "4"
    value: "0.00"
    work: "16,883.00 - 26,163.23 is less than zero; line 3 is more than line 1, so enter -0-"
  - printed: "5d"
    value: "20000.00"
    work: "0.00 + 20,000.00 + 0.00 = 20,000.00"
  - printed: "5e"
    value: "20000.00"
    work: "AGI <= 500,000 and no 2555/4563/PR exclusion; smaller of 20,000.00 or 40,000 = 20,000.00"
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
    value: "20000.00"
    work: "20,000.00 + 0.00 = 20,000.00"
  - printed: "8e"
    value: "5810.00"
    work: "5,810.00 + 0.00 + 0.00 = 5,810.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "5810.00"
    work: "5,810.00 + 0.00 = 5,810.00"
  - printed: "12"
    value: "8153.00"
    work: "6,769.00 + 1,384.00 = 8,153.00"
  - printed: "14"
    value: "22275.00"
    work: "14,122.00 + 8,153.00 + 0.00 = 22,275.00"
  - printed: "17"
    value: "48085.00"
    work: "0.00 + 20,000.00 + 5,810.00 + 22,275.00 + 0.00 + 0.00 = 48,085.00"
```
```

### classm.sa.5

```yaml
lines:
  - printed: "2"
    value: "68176.00"
    work: "Form 1040 line 11b = 68,176.00"
  - printed: "3"
    value: "5113.20"
    work: "68,176.00 x 0.075 = 5,113.20"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 5,113.20 < 0, enter -0-"
  - printed: "5d"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "5e"
    value: "0.00"
    work: "smaller of 0.00 or 40,000 (MFJ, AGI not over 500,000, no 2555/4563/PR) = 0.00"
  - printed: "6"
    value: "0.00"
    work: "no other taxes (filer: no foreign tax/GST deduction) = 0.00"
  - printed: "8b"
    value: "0.00"
    work: "no mortgage interest not on Form 1098 = 0.00"
  - printed: "8c"
    value: "0.00"
    work: "no points not on Form 1098 = 0.00"
  - printed: "13"
    value: "0.00"
    work: "no prior-year charitable carryover = 0.00"
  - printed: "15"
    value: "0.00"
    work: "no casualty/theft loss = 0.00"
  - printed: "16"
    value: "0.00"
    work: "no other itemized deductions = 0.00"
  - printed: "7"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
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
    value: "1385.00"
    work: "sum of noncash gifts: item_a 1,385.00 = 1,385.00"
  - printed: "14"
    value: "3784.00"
    work: "2,399.00 + 1,385.00 + 0.00 = 3,784.00"
  - printed: "17"
    value: "3784.00"
    work: "0.00 + 0.00 + 0.00 + 3,784.00 + 0.00 + 0.00 = 3,784.00"
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "522631.00"
    work: "Form 1040 line 11b = 522,631.00"
  - printed: "3"
    value: "39197.33"
    work: "522,631.00 x 0.075 = 39,197.325, rounded to 39,197.33"
  - printed: "4"
    value: "0.00"
    work: "2,814.00 - 39,197.33 is less than zero, so enter -0-"
  - printed: "5d"
    value: "2057.00"
    work: "0.00 + 2,057.00 + 0.00 = 2,057.00"
  - printed: "5e"
    value: "2057.00"
    work: "AGI > 500,000, so use the SALT worksheet; line 5d of 2,057 is not over 10,000, so enter line 5d"
  - printed: "6"
    value: "0.00"
    work: "No other taxes, so zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098, so zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098, so zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover, so zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss, so zero"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions, so zero"
  - printed: "7"
    value: "2057.00"
    work: "2,057.00 + 0.00 = 2,057.00"
  - printed: "8e"
    value: "39317.00"
    work: "39,317.00 + 0.00 + 0.00 = 39,317.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "39317.00"
    work: "39,317.00 + 0.00 = 39,317.00"
  - printed: "12"
    value: "5000.00"
    work: "Sum of noncash gifts: item_a 5,000.00"
  - printed: "14"
    value: "23034.00"
    work: "18,034.00 + 5,000.00 + 0.00 = 23,034.00"
  - printed: "17"
    value: "64408.00"
    work: "0.00 + 2,057.00 + 39,317.00 + 23,034.00 + 0.00 + 0.00 = 64,408.00"
```
```
