# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ecb3301b4cca5e40ed9bd8a9787ad4b9e34d943d93f1d32d96cd1799b9a4feb0 |
| cases | 6 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 9, 10, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 9, 10, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.sa.1 — prompt sha256 8f3c37737390893ccef104a7c321f371ffb58e3c5d255842e9ce6bb0b8a59af7; branches: sa.unsupported:false, sa.gifts:true, sa.no:false, sa.charity_limited:false, sa.charity_limited_if_gifts#0, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line11_if_gifts#0, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:left, sa.line16#1, sa.line12#0, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.1 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $20,000.00

### classm.sa.1 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $7,586.00

### classm.sa.1 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $568.95

### classm.sa.1 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $4,726.00

### classm.sa.1 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $4,726.00

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

Value: $4,726.00

### classm.sa.1 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $20,887.00

### classm.sa.1 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $20,887.00

### classm.sa.1 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $0.00

### classm.sa.1 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,000.00

### classm.sa.1 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $45,613.00

### case classm.sa.2 — prompt sha256 4d70285602c16954557eb371b762141859133234e8c663bb8938a568567012eb; branches: sa.unsupported:false, sa.gifts:false, sa.no:false, sa.charity_limited_if_gifts#1, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.elect_itemize:false, sa.line11_if_gifts#1, sa.agi_floor:floor, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.line12#1, sa.form8283:false, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $22,395.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $2,908.00

### classm.sa.2 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $2,908.00

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

Value: $2,908.00

### classm.sa.2 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $25,303.00

### case classm.sa.3 — prompt sha256 d2bafc4970ab5626295d62c95eb865d588ee7d89ee1874f74487dec14e1d4830; branches: sa.unsupported:false, sa.gifts:true, sa.no:false, sa.charity_limited:false, sa.charity_limited_if_gifts#0, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.elect_itemize:false, sa.line11_if_gifts#0, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.line16#1, sa.line12#0, sa.form8283:true, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $651,919.10

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $48,893.93

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $14,659.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $10,000.00

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

Value: $10,000.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $4,826.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $7,096.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $11,922.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $3,675.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $3,675.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $25,597.00

### case classm.sa.4 — prompt sha256 52ad6cceeb220f0ad0ab52eab72e320d22e70b2464e24474dd1e257dc92f5189; branches: sa.unsupported:false, sa.gifts:true, sa.no:false, sa.charity_limited:false, sa.charity_limited_if_gifts#0, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.elect_itemize:true, sa.line11_if_gifts#0, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.line12#0, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $3,265.00

### classm.sa.4 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $61,676.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $4,625.70

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $9,229.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $9,229.00

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

Value: $9,229.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $6,880.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $46,880.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $17,251.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,516.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $76,625.00

### case classm.sa.5 — prompt sha256 ceb2be89bfc18a1dcff5e2584dc01f7933ab66625a21cafe5c6a5202ba574eec; branches: sa.unsupported:false, sa.gifts:false, sa.no:false, sa.charity_limited_if_gifts#1, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:true, sa.mfs_spouse_extra:false, sa.line11_if_gifts#1, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.line16#1, sa.line12#1, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $71,000.85

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $5,325.06

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $67,014.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $40,000.00

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

Value: $40,000.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,000.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $80,000.00

### case classm.sa.6 — prompt sha256 c38dbaa4897098a3fad4012e8fd04b6ebbc094fead01f0b7a2f1d56eaa04c7cd; branches: sa.unsupported:false, sa.gifts:false, sa.no:false, sa.charity_limited_if_gifts#1, sa.charity_limited_if_gifts:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.elect_itemize:false, sa.line11_if_gifts#1, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.line12#1, sa.form8283:false, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity an
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $26,295.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $1,972.13

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $9,336.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $9,336.00

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

Value: $9,336.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $34.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $34.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits (zero when you and your s
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $9,370.00

## Raw responses

### classm.sa.1

```yaml
```yaml
lines:
  - printed: "11"
    value: "20000.00"
    work: "Cash/check gifts $20,000.00 as supplied; filer says no income limit or carryover applies"
  - printed: "2"
    value: "7586.00"
    work: "Form 1040 line 11b = 7,586.00"
  - printed: "3"
    value: "568.95"
    work: "7,586.00 × 0.075 = 568.95"
  - printed: "4"
    value: "0.00"
    work: "0.00 − 568.95 is less than zero, so enter -0-"
  - printed: "5d"
    value: "4726.00"
    work: "4,726.00 + 0.00 + 0.00 = 4,726.00"
  - printed: "5e"
    value: "4726.00"
    work: "AGI 7,586 ≤ $250,000 (MFS) and no Form 2555/4563/Puerto Rico exclusion; smaller of 4,726.00 or 20,000 = 4,726.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or generation-skipping tax reported"
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
    work: "No line 16 items; no gambling winnings, so no gambling losses"
  - printed: "7"
    value: "4726.00"
    work: "4,726.00 + 0.00 = 4,726.00"
  - printed: "8e"
    value: "20887.00"
    work: "20,887.00 + 0.00 + 0.00 = 20,887.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "20887.00"
    work: "20,887.00 + 0.00 = 20,887.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts supplied"
  - printed: "14"
    value: "20000.00"
    work: "20,000.00 + 0.00 + 0.00 = 20,000.00"
  - printed: "17"
    value: "45613.00"
    work: "0.00 + 4,726.00 + 20,887.00 + 20,000.00 + 0.00 + 0.00 = 45,613.00"
```
```

### classm.sa.2

```yaml
```yaml
lines:
  - printed: "11"
    value: "0.00"
    work: "No charitable contributions and no carryover, so 0"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 11b is -30,851.03; this line takes no amount below zero, so 0"
  - printed: "3"
    value: "0.00"
    work: "0.00 x 0.075 = 0.00"
  - printed: "4"
    value: "22395.00"
    work: "22,395.00 - 0.00 = 22,395.00"
  - printed: "5d"
    value: "2908.00"
    work: "1,803.00 + 1,105.00 + 0.00 = 2,908.00"
  - printed: "5e"
    value: "2908.00"
    work: "Line 11b is not over $500,000 and there is no Form 2555, Form 4563 or Puerto Rico exclusion; smaller of 2,908.00 or 40,000 = 2,908.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction, so 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098, so 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098, so 0"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover, so 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss, so 0"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings and no other listed deductions, so 0"
  - printed: "7"
    value: "2908.00"
    work: "2,908.00 + 0.00 = 2,908.00"
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
    work: "No charitable contributions and no carryover, so 0"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "25303.00"
    work: "22,395.00 + 2,908.00 + 0.00 + 0.00 + 0.00 + 0.00 = 25,303.00"
```
```

### classm.sa.3

```yaml
```yaml
lines:
  - printed: "11"
    value: "0.00"
    work: "Filer's deductible cash/check gifts = $0.00"
  - printed: "2"
    value: "651919.10"
    work: "Form 1040 line 11b"
  - printed: "3"
    value: "48893.93"
    work: "651,919.10 x 0.075 = 48,893.9325"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 48,893.93 is less than zero, so enter -0-"
  - printed: "5d"
    value: "14659.00"
    work: "0.00 + 14,659.00 + 0.00"
  - printed: "5e"
    value: "10000.00"
    work: "AGI over $500,000, so use SALT worksheet: 40,000 - 0.30 x (651,919.10 - 500,000) = -5,575.73; larger of that or 10,000 = 10,000; smaller of 10,000 or 14,659 = 10,000"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes"
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
    work: "No gambling winnings and no other listed deductions"
  - printed: "7"
    value: "10000.00"
    work: "10,000.00 + 0.00"
  - printed: "8e"
    value: "4826.00"
    work: "4,826.00 + 0.00 + 0.00"
  - printed: "9"
    value: "7096.00"
    work: "Form 4952 line 8"
  - printed: "10"
    value: "11922.00"
    work: "4,826.00 + 7,096.00"
  - printed: "12"
    value: "3675.00"
    work: "Noncash gift item_a = 3,675.00; no income limits apply"
  - printed: "14"
    value: "3675.00"
    work: "0.00 + 3,675.00 + 0.00"
  - printed: "17"
    value: "25597.00"
    work: "0 + 10,000 + 11,922 + 3,675 + 0 + 0"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "11"
    value: "3265.00"
    work: "Charitable contributions = yes, no income limits; cash/check gifts $3,265.00"
  - printed: "2"
    value: "61676.00"
    work: "Form 1040 line 11b = 61,676.00"
  - printed: "3"
    value: "4625.70"
    work: "61,676.00 x 0.075 = 4,625.70"
  - printed: "4"
    value: "0.00"
    work: "197.00 - 4,625.70 < 0, enter -0-"
  - printed: "5d"
    value: "9229.00"
    work: "2,680.00 + 6,549.00 + 0.00 = 9,229.00"
  - printed: "5e"
    value: "9229.00"
    work: "AGI <= 500,000, no 2555/4563/PR; smaller of 9,229.00 or 40,000 = 9,229.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes"
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
    work: "No gambling winnings; no other line 16 items"
  - printed: "7"
    value: "9229.00"
    work: "9,229.00 + 0.00 = 9,229.00"
  - printed: "8e"
    value: "40000.00"
    work: "40,000.00 + 0.00 + 0.00 = 40,000.00"
  - printed: "9"
    value: "6880.00"
    work: "Form 4952 line 8 = 6,880.00"
  - printed: "10"
    value: "46880.00"
    work: "40,000.00 + 6,880.00 = 46,880.00"
  - printed: "12"
    value: "17251.00"
    work: "Noncash gifts 4,087.00 + 13,164.00 = 17,251.00, no limits"
  - printed: "14"
    value: "20516.00"
    work: "3,265.00 + 17,251.00 + 0.00 = 20,516.00"
  - printed: "17"
    value: "76625.00"
    work: "0.00 + 9,229.00 + 46,880.00 + 20,516.00 + 0.00 + 0.00 = 76,625.00"
```
```

### classm.sa.5

```yaml
```yaml
lines:
  - printed: "11"
    value: "0.00"
    work: "No charitable contributions and no carryover, so zero"
  - printed: "2"
    value: "71000.85"
    work: "Form 1040 line 11b = 71,000.85"
  - printed: "3"
    value: "5325.06"
    work: "71,000.85 x 0.075 = 5,325.06"
  - printed: "4"
    value: "0.00"
    work: "4,556.00 - 5,325.06 is less than zero, so -0-"
  - printed: "5d"
    value: "67014.00"
    work: "49,293.00 + 17,721.00 + 0.00 = 67,014.00"
  - printed: "5e"
    value: "40000.00"
    work: "AGI <= 500,000 and no Form 2555/4563/Puerto Rico exclusion; smaller of 67,014.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction, so zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098, so zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098, so zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings and no other listed deductions, so zero"
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
    value: "0.00"
    work: "No noncash gifts, so zero"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "80000.00"
    work: "0.00 + 40,000.00 + 40,000.00 + 0.00 + 0.00 + 0.00 = 80,000.00"
```
```

### classm.sa.6

```yaml
lines:
  - printed: "11"
    value: "0.00"
    work: "No charitable contributions and no carryover; zero"
  - printed: "2"
    value: "26295.00"
    work: "Form 1040 line 11b = 26,295.00"
  - printed: "3"
    value: "1972.13"
    work: "26,295.00 x 0.075 = 1,972.125, rounded to 1,972.13"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 1,972.13 is less than zero; enter -0-"
  - printed: "5d"
    value: "9336.00"
    work: "6,933.00 + 0.00 + 2,403.00 = 9,336.00"
  - printed: "5e"
    value: "9336.00"
    work: "AGI not over $500,000 and no Form 2555/4563/PR exclusion; smaller of 9,336.00 or 40,000 = 9,336.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes; zero"
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
    work: "No casualty or theft loss; zero"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so gambling losses are limited to 0; no other listed deductions"
  - printed: "7"
    value: "9336.00"
    work: "9,336.00 + 0.00 = 9,336.00"
  - printed: "8e"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "9"
    value: "34.00"
    work: "Form 4952 line 8 = 34.00"
  - printed: "10"
    value: "34.00"
    work: "0.00 + 34.00 = 34.00"
  - printed: "12"
    value: "0.00"
    work: "No charitable contributions and no carryover; zero"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "9370.00"
    work: "0.00 + 9,336.00 + 34.00 + 0.00 + 0.00 + 0.00 = 9,370.00"
```
