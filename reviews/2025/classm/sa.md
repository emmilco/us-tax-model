# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | f44e5dfe0d9ef02a6953b4ecdf2d9967906e0a91c8afb438f1d743b53be76e92 |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.sa.1 — prompt sha256 116e745b5e0a652a54252cc13697f50c71fcf773a73b7b79886196afad72da88; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.1 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $32,936.00

### classm.sa.1 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $2,470.20

### classm.sa.1 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $39,994.00

### classm.sa.1 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $39,994.00

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

### classm.sa.1 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $39,994.00

### classm.sa.1 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $1,078.00

### classm.sa.1 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $1,078.00

### classm.sa.1 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $15,119.00

### classm.sa.1 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $56,191.00

### case classm.sa.2 — prompt sha256 d0b3c8441f67b78cc545096f89d82e0706929ecd9da06c3de65b6ddc0dc19027; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $448,512.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $33,638.40

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $51,026.00

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

### classm.sa.2 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $5,000.00

### classm.sa.2 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $5,000.00

### case classm.sa.3 — prompt sha256 8fe57031b7b8e09c0c02aae5ee16bbf584304c69a8d4784da48a3615042e90b7; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:floor, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $482.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $47,026.00

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

### classm.sa.3 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $40,000.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,000.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $5,941.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $12,663.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $93,145.00

### case classm.sa.4 — prompt sha256 b53350077b091b59f9ba3d34b1b801686c4840c9936ab47122f1643b640f46ea; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:true, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $425,525.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $31,914.38

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $31,612.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $31,612.00

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

### classm.sa.4 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $31,612.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $415.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,415.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,000.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $92,027.00

### case classm.sa.5 — prompt sha256 64290ec4a0184d3c2997581f84c8850fa3421b6db4de3e9172b083d7c1861edb; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.agi_floor:positive, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $14,748.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $1,106.10

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $2,005.90

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

### classm.sa.5 — 16 — Other—from list in instructions. List type and amount:
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

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $1,043.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $3,048.90

### case classm.sa.6 — prompt sha256 d83fa94c9a3d6f0afc2cef0a7b49ea51a23bab4d490a77547095c0ce380519de; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $50,053.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $3,753.98

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $17,372.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $17,372.00

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

### classm.sa.6 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $17,372.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $18,271.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $18,271.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $3,981.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $13,048.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $48,691.00

## Raw responses

### classm.sa.1

```yaml
lines:
  - printed: "2"
    value: "32936.00"
    work: "Form 1040 line 11b = 32,936.00"
  - printed: "3"
    value: "2470.20"
    work: "32,936.00 x 0.075 = 2,470.20"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 2,470.20 is less than zero, so enter -0-"
  - printed: "5d"
    value: "39994.00"
    work: "39,994.00 + 0.00 + 0.00 = 39,994.00"
  - printed: "5e"
    value: "39994.00"
    work: "AGI is not over $500,000 and there is no Form 2555/4563 or Puerto Rico exclusion; smaller of 39,994.00 or 40,000 = 39,994.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so gambling losses are capped at 0; no other listed deductions"
  - printed: "7"
    value: "39994.00"
    work: "39,994.00 + 0.00 = 39,994.00"
  - printed: "8e"
    value: "1078.00"
    work: "1,078.00 + 0.00 + 0.00 = 1,078.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "1078.00"
    work: "1,078.00 + 0.00 = 1,078.00"
  - printed: "12"
    value: "0.00"
    work: "Noncash gifts item_a 0.00 + item_b 0.00 = 0.00"
  - printed: "14"
    value: "15119.00"
    work: "15,119.00 + 0.00 + 0.00 = 15,119.00"
  - printed: "17"
    value: "56191.00"
    work: "0.00 + 39,994.00 + 1,078.00 + 15,119.00 + 0.00 + 0.00 = 56,191.00"
```

### classm.sa.2

```yaml
```yaml
lines:
  - printed: "2"
    value: "448512.00"
    work: "Form 1040 line 11b AGI = 448,512.00"
  - printed: "3"
    value: "33638.40"
    work: "448,512.00 x 0.075 = 33,638.40"
  - printed: "4"
    value: "0.00"
    work: "10,585.00 - 33,638.40 < 0, so enter 0"
  - printed: "5d"
    value: "51026.00"
    work: "48,082.00 + 2,944.00 + 0.00 = 51,026.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS and AGI over 250,000, so use SALT worksheet; ws6 448,512-250,000=198,512; ws7 x0.30=59,553.60; ws8 40,000-59,553.60=-19,553.60; ws9 larger of that or 10,000=10,000; ws10 smaller of half (5,000) or 51,026 = 5,000"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes; enter 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; enter 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; enter 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year; enter 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; enter 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other listed items; enter 0"
  - printed: "7"
    value: "5000.00"
    work: "5,000.00 + 0.00 = 5,000.00"
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
    work: "No supported noncash gifts; enter 0"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "5000.00"
    work: "0 + 5,000.00 + 0 + 0 + 0 + 0 = 5,000.00"
```
```

### classm.sa.3

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 11b = 0.00"
  - printed: "3"
    value: "0.00"
    work: "0.00 x 0.075 = 0.00"
  - printed: "4"
    value: "482.00"
    work: "482.00 - 0.00 = 482.00"
  - printed: "5d"
    value: "47026.00"
    work: "40644.00 + 6382.00 + 0.00 = 47026.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI not over 500,000, no Form 2555, Form 4563 or Puerto Rico exclusion; smaller of 47026.00 or 40000.00"
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
    work: "No gambling winnings; gambling losses 0.00 limited to winnings 0.00; no other listed items"
  - printed: "7"
    value: "40000.00"
    work: "40000.00 + 0.00 = 40000.00"
  - printed: "8e"
    value: "40000.00"
    work: "40000.00 + 0.00 + 0.00 = 40000.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "40000.00"
    work: "40000.00 + 0.00 = 40000.00"
  - printed: "12"
    value: "5941.00"
    work: "4279.00 + 1662.00 = 5941.00"
  - printed: "14"
    value: "12663.00"
    work: "6722.00 + 5941.00 + 0.00 = 12663.00"
  - printed: "17"
    value: "93145.00"
    work: "482.00 + 40000.00 + 40000.00 + 12663.00 + 0.00 + 0.00 = 93145.00"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "425525.00"
    work: "Form 1040 line 11b = 425,525.00"
  - printed: "3"
    value: "31914.38"
    work: "425,525.00 x 0.075 = 31,914.375, rounded to 31,914.38"
  - printed: "4"
    value: "0.00"
    work: "30,000.00 - 31,914.38 is less than zero, so enter -0-"
  - printed: "5d"
    value: "31612.00"
    work: "31,612.00 + 0.00 + 0.00 = 31,612.00"
  - printed: "5e"
    value: "31612.00"
    work: "AGI 425,525 is not over 500,000 and no Form 2555/4563/PR exclusion, so smaller of 31,612.00 or 40,000 = 31,612.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No other deductions; gambling losses 0 and winnings 0"
  - printed: "7"
    value: "31612.00"
    work: "31,612.00 + 0.00 = 31,612.00"
  - printed: "8e"
    value: "40000.00"
    work: "40,000.00 + 0.00 + 0.00 = 40,000.00"
  - printed: "9"
    value: "415.00"
    work: "Form 4952 line 8 = 415.00"
  - printed: "10"
    value: "40415.00"
    work: "40,000.00 + 415.00 = 40,415.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations supplied"
  - printed: "14"
    value: "20000.00"
    work: "20,000.00 + 0.00 + 0.00 = 20,000.00"
  - printed: "17"
    value: "92027.00"
    work: "0.00 + 31,612.00 + 40,415.00 + 20,000.00 + 0.00 + 0.00 = 92,027.00"
```
```

### classm.sa.5

```yaml
lines:
  - printed: "2"
    value: "14748.00"
    work: "Form 1040 line 11b = 14,748.00"
  - printed: "3"
    value: "1106.10"
    work: "14,748.00 x 0.075 = 1,106.10"
  - printed: "4"
    value: "2005.90"
    work: "3,112.00 - 1,106.10 = 2,005.90"
  - printed: "5d"
    value: "0.00"
    work: "0 + 0 + 0 = 0.00"
  - printed: "5e"
    value: "0.00"
    work: "The smaller of line 5d (0.00) or $40,000 is 0.00; AGI is not over $500,000 and there is no Form 2555, Form 4563 or Puerto Rico exclusion"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax and no generation-skipping tax was given, so 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 was given, so 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 were given, so 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year was given, so 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss was given, so 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses are 0 and winnings are 0, and there are no other line 16 items, so 0"
  - printed: "7"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "8e"
    value: "0.00"
    work: "0 + 0 + 0 = 0.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00 = 0.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations were given, so 0"
  - printed: "14"
    value: "1043.00"
    work: "1,043.00 + 0 + 0 = 1,043.00"
  - printed: "17"
    value: "3048.90"
    work: "2,005.90 + 0 + 0 + 1,043.00 + 0 + 0 = 3,048.90; filer elects to itemize"
```

### classm.sa.6

```yaml
lines:
  - printed: "2"
    value: "50053.00"
    work: "From Form 1040, line 11b (AGI) = 50,053.00"
  - printed: "3"
    value: "3753.98"
    work: "50,053.00 × 0.075 = 3,753.975, rounded to 3,753.98"
  - printed: "4"
    value: "0.00"
    work: "Line 1 (0.00) minus line 3 (3,753.98) is less than zero, so enter -0-"
  - printed: "5d"
    value: "17372.00"
    work: "17,372.00 + 0.00 + 0.00 = 17,372.00"
  - printed: "5e"
    value: "17372.00"
    work: "Smaller of 17,372.00 or 40,000 (head of household; AGI not over 500,000; no Form 2555/4563 or Puerto Rico exclusion)"
  - printed: "6"
    value: "0.00"
    work: "No other taxes (no foreign tax or GST)"
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
    work: "No gambling winnings, so gambling losses are limited to 0; no other listed deductions"
  - printed: "7"
    value: "17372.00"
    work: "17,372.00 + 0.00 = 17,372.00"
  - printed: "8e"
    value: "18271.00"
    work: "18,271.00 + 0.00 + 0.00 = 18,271.00"
  - printed: "9"
    value: "0.00"
    work: "From Form 4952, line 8 = 0.00"
  - printed: "10"
    value: "18271.00"
    work: "18,271.00 + 0.00 = 18,271.00"
  - printed: "12"
    value: "3981.00"
    work: "Noncash gifts: 296.00 + 3,685.00 = 3,981.00"
  - printed: "14"
    value: "13048.00"
    work: "9,067.00 + 3,981.00 + 0.00 = 13,048.00"
  - printed: "17"
    value: "48691.00"
    work: "0.00 + 17,372.00 + 18,271.00 + 13,048.00 + 0.00 + 0.00 = 48,691.00"
```
