# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 236b0e937365531016b767add8caed4055bdc0c5ba614b489645e3ec0521721d |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |

## Lines

### case classm.sa.1 — prompt sha256 a2b86fa72d5095e728decbc9777292c635c7bc68a449e9a1024bff39a0ca6fab; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.1 — 2 — Amount from sa.agi
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

### case classm.sa.2 — prompt sha256 5c52036864557916152d3f2b81846d51f9e200090bfb76063765f95bed0a61a0; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:true, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $778,718.20

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $58,403.87

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $4,822.00

### classm.sa.2 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $4,822.00

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

Value: $4,822.00

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

Value: $1,038.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $14,068.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $18,890.00

### case classm.sa.3 — prompt sha256 d7f9f66da78b497971b96ce328773c591c8f56e713b62406d55bdbe8e447b538; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:true, sa.mfs_spouse_extra:true, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $219,999.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $16,499.93

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $43,049.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $20,000.00

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

Value: $20,000.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $38,476.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $38,476.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $58,476.00

### case classm.sa.4 — prompt sha256 64f4154bc2f83687c98d3cb66900cabf7dcca3729b8de6623fd7f8a7510ff641; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:true, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $-5,479.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **DISAGREE**

Project: $-410.92
Model: $-410.93
Work: -5,479.00 x 0.075 = -410.925, rounded to -410.93

Ruling: genuine ambiguity (amb.2025.multiplication_subcent); project retained; model value dropped from the fixture. With a negative AGI, 7.5% of -$5,479.00 is -$410.925; the project's half-up rounding goes toward the larger value (-$410.92), the model's away from zero (-$410.93). The register entry governs the rounding of a product to the cent; the one-cent difference carries to lines 4 and 17. [dropped]

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **DISAGREE**

Project: $2,727.92
Model: $2,727.93
Work: Line 3 is not more than line 1, so 2,317.00 - (-410.93) = 2,727.93

Ruling: genuine ambiguity (amb.2025.multiplication_subcent); project retained; model value dropped from the fixture. With a negative AGI, 7.5% of -$5,479.00 is -$410.925; the project's half-up rounding goes toward the larger value (-$410.92), the model's away from zero (-$410.93). The register entry governs the rounding of a product to the cent; the one-cent difference carries to lines 4 and 17. [dropped]

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $60,000.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $40,000.00

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

Value: $40,000.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $19,546.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $19,546.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **DISAGREE**

Project: $62,273.92
Model: $62,273.93
Work: 2,727.93 + 40,000.00 + 19,546.00 + 0.00 + 0.00 + 0.00 = 62,273.93

Ruling: genuine ambiguity (amb.2025.multiplication_subcent); project retained; model value dropped from the fixture. With a negative AGI, 7.5% of -$5,479.00 is -$410.925; the project's half-up rounding goes toward the larger value (-$410.92), the model's away from zero (-$410.93). The register entry governs the rounding of a product to the cent; the one-cent difference carries to lines 4 and 17. [dropped]

### case classm.sa.5 — prompt sha256 a7aba60a8515eb7ed69287d3a16fc48ba5c96ff5670ae5ae444ff07a428671f2; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $152,310.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $11,423.25

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $9,614.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $9,614.00

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

Value: $9,614.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $10,301.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $3,173.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $13,474.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,000.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $43,088.00

### case classm.sa.6 — prompt sha256 eb3fc959f4dbab83f5a7a91d28a886b04585fa91fecfd39304eb987ba1cef9bb; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $297,443.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $22,308.23

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $4,361.77

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $34,216.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $34,216.00

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

Value: $34,216.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $37,021.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $37,021.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $75,598.77

## Raw responses

### classm.sa.1

```yaml
lines:
  - printed: "2"
    value: "32936.00"
    work: "From Form 1040 line 11b = 32,936.00"
  - printed: "3"
    value: "2470.20"
    work: "32,936.00 x 0.075 = 2,470.20"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 2,470.20 is below zero, so enter -0-"
  - printed: "5d"
    value: "51164.00"
    work: "47,577.00 + 3,587.00 + 0.00 = 51,164.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI is not over $500,000 and no Form 2555/4563/Puerto Rico; smaller of 51,164.00 or 40,000 (HOH) = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes (no foreign tax or GST deduction)"
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
    work: "No other itemized deductions"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "8729.00"
    work: "8,729.00 + 0.00 + 0.00 = 8,729.00"
  - printed: "9"
    value: "0.00"
    work: "From Form 4952 line 8 = 0.00"
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
```yaml
lines:
  - printed: "2"
    value: "778718.20"
    work: "Form 1040 line 11b = 778,718.20"
  - printed: "3"
    value: "58403.87"
    work: "778,718.20 x 0.075 = 58,403.865, rounded to 58,403.87"
  - printed: "4"
    value: "0.00"
    work: "30,000.00 - 58,403.87 < 0; line 3 is more than line 1, enter -0-"
  - printed: "5d"
    value: "4822.00"
    work: "0.00 + 4,822.00 + 0.00 = 4,822.00"
  - printed: "5e"
    value: "4822.00"
    work: "AGI > $500,000, so use the SALT worksheet; 5d 4,822 <= $10,000, so enter 5d"
  - printed: "6"
    value: "0.00"
    work: "No other taxes"
  - printed: "8b"
    value: "0.00"
    work: "None"
  - printed: "8c"
    value: "0.00"
    work: "None"
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
    value: "4822.00"
    work: "4,822.00 + 0.00 = 4,822.00"
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
    value: "1038.00"
    work: "Noncash gifts: item_a 1,038.00"
  - printed: "14"
    value: "14068.00"
    work: "13,030.00 + 1,038.00 + 0.00 = 14,068.00"
  - printed: "17"
    value: "18890.00"
    work: "0.00 + 4,822.00 + 0.00 + 14,068.00 + 0.00 + 0.00 = 18,890.00"
```
```

### classm.sa.3

```yaml
lines:
  - printed: "2"
    value: "219999.00"
    work: "Form 1040 line 11b = 219,999.00"
  - printed: "3"
    value: "16499.93"
    work: "219,999.00 × 0.075 = 16,499.925, rounded to 16,499.93"
  - printed: "4"
    value: "0.00"
    work: "0.00 − 16,499.93 is less than zero, so enter -0-"
  - printed: "5d"
    value: "43049.00"
    work: "40,723.00 + 2,326.00 + 0.00 = 43,049.00"
  - printed: "5e"
    value: "20000.00"
    work: "MFS, line 11b 219,999 ≤ 250,000, no 2555/4563/PR; smaller of 43,049.00 or 20,000 = 20,000.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST tax; enter zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; enter zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; enter zero"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover; enter zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; enter zero"
  - printed: "16"
    value: "0.00"
    work: "No line 16 deductions; enter zero"
  - printed: "7"
    value: "20000.00"
    work: "20,000.00 + 0.00 = 20,000.00"
  - printed: "8e"
    value: "38476.00"
    work: "38,476.00 + 0.00 + 0.00 = 38,476.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "38476.00"
    work: "38,476.00 + 0.00 = 38,476.00"
  - printed: "12"
    value: "0.00"
    work: "No supported noncash donations given; enter zero"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "58476.00"
    work: "0.00 + 20,000.00 + 38,476.00 + 0.00 + 0.00 + 0.00 = 58,476.00"
```

### classm.sa.4

```yaml
lines:
  - printed: "2"
    value: "-5479.00"
    work: "Form 1040 line 11b = -5,479.00"
  - printed: "3"
    value: "-410.93"
    work: "-5,479.00 x 0.075 = -410.925, rounded to -410.93"
  - printed: "4"
    value: "2727.93"
    work: "Line 3 is not more than line 1, so 2,317.00 - (-410.93) = 2,727.93"
  - printed: "5d"
    value: "60000.00"
    work: "60,000.00 + 0.00 + 0.00 = 60,000.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI is not over 500,000 and no Form 2555, Form 4563 or Puerto Rico exclusion; Single; smaller of 60,000.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes (foreign tax or GST) reported"
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
    work: "No other itemized deductions"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "19546.00"
    work: "19,546.00 + 0.00 + 0.00 = 19,546.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "19546.00"
    work: "19,546.00 + 0.00 = 19,546.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations given"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "62273.93"
    work: "2,727.93 + 40,000.00 + 19,546.00 + 0.00 + 0.00 + 0.00 = 62,273.93"
```

### classm.sa.5

```yaml
lines:
  - printed: "2"
    value: "152310.00"
    work: "Form 1040 line 11b = 152,310.00"
  - printed: "3"
    value: "11423.25"
    work: "152,310.00 x 0.075 = 11,423.25"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 11,423.25 < 0; line 3 more than line 1, enter -0-"
  - printed: "5d"
    value: "9614.00"
    work: "7,847.00 + 1,767.00 + 0.00 = 9,614.00"
  - printed: "5e"
    value: "9614.00"
    work: "AGI <= 500,000, no 2555/4563/PR; smaller of 9,614.00 or 40,000 = 9,614.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes (filer answered no); zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest not on Form 1098; zero"
  - printed: "8c"
    value: "0.00"
    work: "No points not on Form 1098; zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover from prior year; zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; zero"
  - printed: "16"
    value: "0.00"
    work: "No other itemized deductions; zero"
  - printed: "7"
    value: "9614.00"
    work: "9,614.00 + 0.00 = 9,614.00"
  - printed: "8e"
    value: "10301.00"
    work: "10,301.00 + 0.00 + 0.00 = 10,301.00"
  - printed: "9"
    value: "3173.00"
    work: "Form 4952 line 8 = 3,173.00"
  - printed: "10"
    value: "13474.00"
    work: "10,301.00 + 3,173.00 = 13,474.00"
  - printed: "12"
    value: "0.00"
    work: "No supported noncash donations given; zero"
  - printed: "14"
    value: "20000.00"
    work: "20,000.00 + 0.00 + 0.00 = 20,000.00"
  - printed: "17"
    value: "43088.00"
    work: "0.00 + 9,614.00 + 13,474.00 + 20,000.00 + 0.00 + 0.00 = 43,088.00"
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "297443.00"
    work: "Form 1040 line 11b = 297,443.00"
  - printed: "3"
    value: "22308.23"
    work: "297,443.00 x 0.075 = 22,308.225, rounded to 22,308.23"
  - printed: "4"
    value: "4361.77"
    work: "26,670.00 - 22,308.23 = 4,361.77"
  - printed: "5d"
    value: "34216.00"
    work: "34,216.00 + 0.00 + 0.00 = 34,216.00"
  - printed: "5e"
    value: "34216.00"
    work: "AGI 297,443 <= 500,000, no Form 2555/4563/PR; smaller of 34,216.00 or 40,000 = 34,216.00"
  - printed: "6"
    value: "0.00"
    work: "No other taxes"
  - printed: "8b"
    value: "0.00"
    work: "None reported"
  - printed: "8c"
    value: "0.00"
    work: "None reported"
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
    value: "34216.00"
    work: "34,216.00 + 0.00 = 34,216.00"
  - printed: "8e"
    value: "37021.00"
    work: "37,021.00 + 0.00 + 0.00 = 37,021.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "37021.00"
    work: "37,021.00 + 0.00 = 37,021.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations given"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "75598.77"
    work: "4,361.77 + 34,216.00 + 37,021.00 + 0.00 + 0.00 + 0.00 = 75,598.77"
```
```
