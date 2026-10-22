# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | dd446ef9a1cac14f5fd495878367b91a5f0a65a7cff1a8b5169fe16dd29f7082 |
| cases | 14 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.sa.1 — prompt sha256 868b50a115081712c184747e4f6f36c75a02e039df7c8533acac4b1a3a19fe82; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

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

### case classm.sa.2 — prompt sha256 61a96c0c0a22a3f69e922404aabe710c4b08d97d98fd6cdb19ebc462b2f2774e; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:positive, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $375,980.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $28,198.50

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $10,673.00

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

Value: $1,943.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $5,418.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $10,418.00

### case classm.sa.3 — prompt sha256 4015a96f3bd24cd0733618aa97b28bc85e904c2b3ff56f2c3b5c8d64796d91be; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:true, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $425,525.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $31,914.38

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $31,612.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $31,612.00

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

Value: $31,612.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $415.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,415.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,000.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $92,027.00

### case classm.sa.4 — prompt sha256 60c2c01109efd0c649437ff4e8a8b023e1aa0cb85a927bd284360e10415301dc; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $171,456.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $12,859.20

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $2,875.80

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $27,909.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $70.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $27,979.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $9,258.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $21,561.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $52,415.80

### case classm.sa.5 — prompt sha256 f3e2c35e00f799450e14e3f39d3028930b86eef0dc66fa731c2fd96b7b211899; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $409,258.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $30,694.35

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $62,123.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $5,000.00

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

Value: $5,000.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $38,012.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $38,012.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $43,012.00

### case classm.sa.6 — prompt sha256 b5544744d91e404e659f0ceaff1449074c254a42963a047166392c54763ccbcf; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $-67,320.70

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $-5,049.05

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $19,058.05

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $42,613.00

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

### classm.sa.6 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $2,432.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $272.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $2,704.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $18,821.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $80,583.05

### case classm.sa.7 — prompt sha256 b5e022cb5a7f59da9fdda69146edc7828a1c27721863953186ee6c42ab773ea6; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.7 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $50,053.00

### classm.sa.7 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $3,753.98

### classm.sa.7 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $18,271.00

### classm.sa.7 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $18,271.00

### classm.sa.7 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $3,981.00

### classm.sa.7 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $13,048.00

### classm.sa.7 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $48,691.00

### case classm.sa.1 — prompt sha256 868b50a115081712c184747e4f6f36c75a02e039df7c8533acac4b1a3a19fe82; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

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

### case classm.sa.2 — prompt sha256 61a96c0c0a22a3f69e922404aabe710c4b08d97d98fd6cdb19ebc462b2f2774e; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:positive, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $375,980.00

### classm.sa.2 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $28,198.50

### classm.sa.2 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.2 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $10,673.00

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

Value: $1,943.00

### classm.sa.2 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $5,418.00

### classm.sa.2 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $10,418.00

### case classm.sa.3 — prompt sha256 4015a96f3bd24cd0733618aa97b28bc85e904c2b3ff56f2c3b5c8d64796d91be; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.spouse_extra:true, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.3 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $425,525.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $31,914.38

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $31,612.00

### classm.sa.3 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $31,612.00

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

Value: $31,612.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $40,000.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $415.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $40,415.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $20,000.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $92,027.00

### case classm.sa.4 — prompt sha256 60c2c01109efd0c649437ff4e8a8b023e1aa0cb85a927bd284360e10415301dc; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:true, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.4 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $171,456.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $12,859.20

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $2,875.80

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.sa.4 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $27,909.00

### classm.sa.4 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $70.00

### classm.sa.4 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $27,979.00

### classm.sa.4 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $9,258.00

### classm.sa.4 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $21,561.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $52,415.80

### case classm.sa.5 — prompt sha256 f3e2c35e00f799450e14e3f39d3028930b86eef0dc66fa731c2fd96b7b211899; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $409,258.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $30,694.35

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $62,123.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $5,000.00

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

Value: $5,000.00

### classm.sa.5 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $38,012.00

### classm.sa.5 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $38,012.00

### classm.sa.5 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $43,012.00

### case classm.sa.6 — prompt sha256 b5544744d91e404e659f0ceaff1449074c254a42963a047166392c54763ccbcf; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:right, sa.line16_gambling:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $-67,320.70

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $-5,049.05

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $19,058.05

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $42,613.00

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

### classm.sa.6 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $40,000.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $2,432.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $272.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $2,704.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $18,821.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $80,583.05

### case classm.sa.7 — prompt sha256 b5e022cb5a7f59da9fdda69146edc7828a1c27721863953186ee6c42ab773ea6; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16_gambling:left, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.7 — 2 — Amount from sa.agi
Status: **AGREE**

Value: $50,053.00

### classm.sa.7 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $3,753.98

### classm.sa.7 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $17,372.00

### classm.sa.7 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $18,271.00

### classm.sa.7 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $18,271.00

### classm.sa.7 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $3,981.00

### classm.sa.7 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $13,048.00

### classm.sa.7 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $48,691.00

## Raw responses

### classm.sa.1

```yaml
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
    work: "smaller of 39,994.00 or 40,000 (HOH; AGI not over 500,000; no 2555/4563/PR) = 39,994.00"
  - printed: "6"
    value: "0.00"
    work: "no foreign tax or GST deduction = 0.00"
  - printed: "8b"
    value: "0.00"
    work: "no mortgage interest outside Form 1098 = 0.00"
  - printed: "8c"
    value: "0.00"
    work: "no points outside Form 1098 = 0.00"
  - printed: "13"
    value: "0.00"
    work: "no carryover from a prior year = 0.00"
  - printed: "15"
    value: "0.00"
    work: "no casualty or theft loss = 0.00"
  - printed: "16"
    value: "0.00"
    work: "no gambling winnings (Sch 1 line 8b = 0) and no other listed deductions = 0.00"
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
    work: "gift item_a 0.00 + item_b 0.00 = 0.00"
  - printed: "14"
    value: "15119.00"
    work: "15,119.00 + 0.00 + 0.00 = 15,119.00"
  - printed: "17"
    value: "56191.00"
    work: "0.00 + 39,994.00 + 1,078.00 + 15,119.00 + 0.00 + 0.00 = 56,191.00"
```
```

### classm.sa.2

```yaml
lines:
  - printed: "2"
    value: "375980.00"
    work: "Form 1040 line 11b = 375,980.00"
  - printed: "3"
    value: "28198.50"
    work: "375,980.00 x 0.075 = 28,198.50"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 28,198.50 is less than zero, so enter -0-"
  - printed: "5d"
    value: "10673.00"
    work: "1,866.00 + 8,807.00 + 0.00 = 10,673.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS and AGI over 250,000, so use SALT worksheet: L1 40,000; L4 375,980; L6 125,980; L7 37,794; L8 2,206; L9 larger of 2,206 or 10,000 = 10,000; L10 smaller of half (5,000) or 10,673 = 5,000"
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
    work: "No carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so no gambling loss deduction; no other listed items"
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
    value: "1943.00"
    work: "Supported noncash gift item_a = 1,943.00"
  - printed: "14"
    value: "5418.00"
    work: "3,475.00 + 1,943.00 + 0.00 = 5,418.00"
  - printed: "17"
    value: "10418.00"
    work: "0.00 + 5,000.00 + 0.00 + 5,418.00 + 0.00 + 0.00 = 10,418.00"
```

### classm.sa.3

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
    work: "Line 3 (31,914.38) is more than line 1 (30,000.00), so enter -0-"
  - printed: "5d"
    value: "31612.00"
    work: "31,612.00 + 0.00 + 0.00 = 31,612.00"
  - printed: "5e"
    value: "31612.00"
    work: "AGI 425,525 is not over 500,000 and no Form 2555/4563/PR exclusion; smaller of 31,612 or 40,000 = 31,612.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other listed items = 0"
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
    work: "No noncash donations given = 0"
  - printed: "14"
    value: "20000.00"
    work: "20,000.00 + 0.00 + 0.00 = 20,000.00"
  - printed: "17"
    value: "92027.00"
    work: "0 + 31,612 + 40,415 + 20,000 + 0 + 0 = 92,027.00"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "171456.00"
    work: "Form 1040 line 11b = 171,456.00"
  - printed: "3"
    value: "12859.20"
    work: "171,456.00 x 0.075 = 12,859.20"
  - printed: "4"
    value: "2875.80"
    work: "15,735.00 - 12,859.20 = 2,875.80"
  - printed: "5d"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "5e"
    value: "0.00"
    work: "AGI <= 500,000 and no 2555/4563/PR; smaller of 0 or 40,000 = 0"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other listed items = 0"
  - printed: "7"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "8e"
    value: "27909.00"
    work: "27,909.00 + 0 + 0 = 27,909.00"
  - printed: "9"
    value: "70.00"
    work: "Form 4952 line 8 = 70.00"
  - printed: "10"
    value: "27979.00"
    work: "27,909.00 + 70.00 = 27,979.00"
  - printed: "12"
    value: "9258.00"
    work: "Noncash gift item_a = 9,258.00"
  - printed: "14"
    value: "21561.00"
    work: "12,303.00 + 9,258.00 + 0 = 21,561.00"
  - printed: "17"
    value: "52415.80"
    work: "2,875.80 + 0 + 27,979.00 + 21,561.00 + 0 + 0 = 52,415.80"
```
```

### classm.sa.5

```yaml
```yaml
lines:
  - printed: "2"
    value: "409258.00"
    work: "Form 1040 line 11b = 409,258.00"
  - printed: "3"
    value: "30694.35"
    work: "409,258.00 x 0.075 = 30,694.35"
  - printed: "4"
    value: "0.00"
    work: "10,465.00 - 30,694.35 < 0, so enter -0-"
  - printed: "5d"
    value: "62123.00"
    work: "44,859.00 + 17,264.00 + 0.00 = 62,123.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS and AGI over $250,000, so the SALT worksheet applies: 40,000 - 0.30 x (409,258 - 250,000) = -7,777.40; the larger of that or 10,000 is 10,000; half for MFS is 5,000; the smaller of 5,000 or 62,123 is 5,000"
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
    work: "No charitable carryover"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so no gambling losses are allowed; no other listed items"
  - printed: "7"
    value: "5000.00"
    work: "5,000.00 + 0.00 = 5,000.00"
  - printed: "8e"
    value: "38012.00"
    work: "38,012.00 + 0.00 + 0.00 = 38,012.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "38012.00"
    work: "38,012.00 + 0.00 = 38,012.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts (gift item_a = 0.00)"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "43012.00"
    work: "0.00 + 5,000.00 + 38,012.00 + 0.00 + 0.00 + 0.00 = 43,012.00"
```
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "-67320.70"
    work: "Form 1040 line 11b = -67,320.70"
  - printed: "3"
    value: "-5049.05"
    work: "-67,320.70 x 0.075 = -5,049.0525, rounded to -5,049.05"
  - printed: "4"
    value: "19058.05"
    work: "14,009.00 - (-5,049.05) = 19,058.05; line 3 is not more than line 1, so no -0- entry"
  - printed: "5d"
    value: "42613.00"
    work: "28,069.00 + 14,544.00 + 0.00 = 42,613.00"
  - printed: "5e"
    value: "40000.00"
    work: "Line 11b is not over $500,000 and there is no Form 2555/4563/Puerto Rico exclusion; smaller of 42,613.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other line 16 items = 0"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "2432.00"
    work: "2,432.00 + 0.00 + 0.00 = 2,432.00"
  - printed: "9"
    value: "272.00"
    work: "Form 4952 line 8 = 272.00"
  - printed: "10"
    value: "2704.00"
    work: "2,432.00 + 272.00 = 2,704.00"
  - printed: "12"
    value: "0.00"
    work: "No supported noncash donations given = 0"
  - printed: "14"
    value: "18821.00"
    work: "18,821.00 + 0.00 + 0.00 = 18,821.00"
  - printed: "17"
    value: "80583.05"
    work: "19,058.05 + 40,000.00 + 2,704.00 + 18,821.00 + 0.00 + 0.00 = 80,583.05"
```
```

### classm.sa.7

```yaml
```yaml
lines:
  - printed: "2"
    value: "50053.00"
    work: "Form 1040 line 11b AGI = 50,053.00"
  - printed: "3"
    value: "3753.98"
    work: "50,053.00 x 0.075 = 3,753.975, rounded to 3,753.98"
  - printed: "4"
    value: "0.00"
    work: "Line 1 0.00 - 3,753.98 is less than zero, so enter -0-"
  - printed: "5d"
    value: "17372.00"
    work: "17,372.00 + 0.00 + 0.00 = 17,372.00"
  - printed: "5e"
    value: "17372.00"
    work: "HOH, AGI not over $500,000, no Form 2555/4563/PR exclusion; smaller of 17,372.00 or 40,000 = 17,372.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction; enter zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; enter zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; enter zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year; enter zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; enter zero"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0.00 are limited to Schedule 1 line 8b winnings of 0.00; no other line 16 items"
  - printed: "7"
    value: "17372.00"
    work: "17,372.00 + 0.00 = 17,372.00"
  - printed: "8e"
    value: "18271.00"
    work: "18,271.00 + 0.00 + 0.00 = 18,271.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "18271.00"
    work: "18,271.00 + 0.00 = 18,271.00"
  - printed: "12"
    value: "3981.00"
    work: "Noncash gifts 296.00 + 3,685.00 = 3,981.00"
  - printed: "14"
    value: "13048.00"
    work: "9,067.00 + 3,981.00 + 0.00 = 13,048.00"
  - printed: "17"
    value: "48691.00"
    work: "0.00 + 17,372.00 + 18,271.00 + 13,048.00 + 0.00 + 0.00 = 48,691.00"
```
```

### classm.sa.1

```yaml
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
    work: "smaller of 39,994.00 or 40,000 (HOH; AGI not over 500,000; no 2555/4563/PR) = 39,994.00"
  - printed: "6"
    value: "0.00"
    work: "no foreign tax or GST deduction = 0.00"
  - printed: "8b"
    value: "0.00"
    work: "no mortgage interest outside Form 1098 = 0.00"
  - printed: "8c"
    value: "0.00"
    work: "no points outside Form 1098 = 0.00"
  - printed: "13"
    value: "0.00"
    work: "no carryover from a prior year = 0.00"
  - printed: "15"
    value: "0.00"
    work: "no casualty or theft loss = 0.00"
  - printed: "16"
    value: "0.00"
    work: "no gambling winnings (Sch 1 line 8b = 0) and no other listed deductions = 0.00"
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
    work: "gift item_a 0.00 + item_b 0.00 = 0.00"
  - printed: "14"
    value: "15119.00"
    work: "15,119.00 + 0.00 + 0.00 = 15,119.00"
  - printed: "17"
    value: "56191.00"
    work: "0.00 + 39,994.00 + 1,078.00 + 15,119.00 + 0.00 + 0.00 = 56,191.00"
```
```

### classm.sa.2

```yaml
lines:
  - printed: "2"
    value: "375980.00"
    work: "Form 1040 line 11b = 375,980.00"
  - printed: "3"
    value: "28198.50"
    work: "375,980.00 x 0.075 = 28,198.50"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 28,198.50 is less than zero, so enter -0-"
  - printed: "5d"
    value: "10673.00"
    work: "1,866.00 + 8,807.00 + 0.00 = 10,673.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS and AGI over 250,000, so use SALT worksheet: L1 40,000; L4 375,980; L6 125,980; L7 37,794; L8 2,206; L9 larger of 2,206 or 10,000 = 10,000; L10 smaller of half (5,000) or 10,673 = 5,000"
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
    work: "No carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so no gambling loss deduction; no other listed items"
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
    value: "1943.00"
    work: "Supported noncash gift item_a = 1,943.00"
  - printed: "14"
    value: "5418.00"
    work: "3,475.00 + 1,943.00 + 0.00 = 5,418.00"
  - printed: "17"
    value: "10418.00"
    work: "0.00 + 5,000.00 + 0.00 + 5,418.00 + 0.00 + 0.00 = 10,418.00"
```

### classm.sa.3

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
    work: "Line 3 (31,914.38) is more than line 1 (30,000.00), so enter -0-"
  - printed: "5d"
    value: "31612.00"
    work: "31,612.00 + 0.00 + 0.00 = 31,612.00"
  - printed: "5e"
    value: "31612.00"
    work: "AGI 425,525 is not over 500,000 and no Form 2555/4563/PR exclusion; smaller of 31,612 or 40,000 = 31,612.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other listed items = 0"
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
    work: "No noncash donations given = 0"
  - printed: "14"
    value: "20000.00"
    work: "20,000.00 + 0.00 + 0.00 = 20,000.00"
  - printed: "17"
    value: "92027.00"
    work: "0 + 31,612 + 40,415 + 20,000 + 0 + 0 = 92,027.00"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "171456.00"
    work: "Form 1040 line 11b = 171,456.00"
  - printed: "3"
    value: "12859.20"
    work: "171,456.00 x 0.075 = 12,859.20"
  - printed: "4"
    value: "2875.80"
    work: "15,735.00 - 12,859.20 = 2,875.80"
  - printed: "5d"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "5e"
    value: "0.00"
    work: "AGI <= 500,000 and no 2555/4563/PR; smaller of 0 or 40,000 = 0"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST taxes = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other listed items = 0"
  - printed: "7"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "8e"
    value: "27909.00"
    work: "27,909.00 + 0 + 0 = 27,909.00"
  - printed: "9"
    value: "70.00"
    work: "Form 4952 line 8 = 70.00"
  - printed: "10"
    value: "27979.00"
    work: "27,909.00 + 70.00 = 27,979.00"
  - printed: "12"
    value: "9258.00"
    work: "Noncash gift item_a = 9,258.00"
  - printed: "14"
    value: "21561.00"
    work: "12,303.00 + 9,258.00 + 0 = 21,561.00"
  - printed: "17"
    value: "52415.80"
    work: "2,875.80 + 0 + 27,979.00 + 21,561.00 + 0 + 0 = 52,415.80"
```
```

### classm.sa.5

```yaml
```yaml
lines:
  - printed: "2"
    value: "409258.00"
    work: "Form 1040 line 11b = 409,258.00"
  - printed: "3"
    value: "30694.35"
    work: "409,258.00 x 0.075 = 30,694.35"
  - printed: "4"
    value: "0.00"
    work: "10,465.00 - 30,694.35 < 0, so enter -0-"
  - printed: "5d"
    value: "62123.00"
    work: "44,859.00 + 17,264.00 + 0.00 = 62,123.00"
  - printed: "5e"
    value: "5000.00"
    work: "MFS and AGI over $250,000, so the SALT worksheet applies: 40,000 - 0.30 x (409,258 - 250,000) = -7,777.40; the larger of that or 10,000 is 10,000; half for MFS is 5,000; the smaller of 5,000 or 62,123 is 5,000"
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
    work: "No charitable carryover"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings, so no gambling losses are allowed; no other listed items"
  - printed: "7"
    value: "5000.00"
    work: "5,000.00 + 0.00 = 5,000.00"
  - printed: "8e"
    value: "38012.00"
    work: "38,012.00 + 0.00 + 0.00 = 38,012.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "38012.00"
    work: "38,012.00 + 0.00 = 38,012.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts (gift item_a = 0.00)"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "43012.00"
    work: "0.00 + 5,000.00 + 38,012.00 + 0.00 + 0.00 + 0.00 = 43,012.00"
```
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "-67320.70"
    work: "Form 1040 line 11b = -67,320.70"
  - printed: "3"
    value: "-5049.05"
    work: "-67,320.70 x 0.075 = -5,049.0525, rounded to -5,049.05"
  - printed: "4"
    value: "19058.05"
    work: "14,009.00 - (-5,049.05) = 19,058.05; line 3 is not more than line 1, so no -0- entry"
  - printed: "5d"
    value: "42613.00"
    work: "28,069.00 + 14,544.00 + 0.00 = 42,613.00"
  - printed: "5e"
    value: "40000.00"
    work: "Line 11b is not over $500,000 and there is no Form 2555/4563/Puerto Rico exclusion; smaller of 42,613.00 or 40,000 = 40,000.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction = 0"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098 = 0"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098 = 0"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year = 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss = 0"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0, limited to winnings 0; no other line 16 items = 0"
  - printed: "7"
    value: "40000.00"
    work: "40,000.00 + 0.00 = 40,000.00"
  - printed: "8e"
    value: "2432.00"
    work: "2,432.00 + 0.00 + 0.00 = 2,432.00"
  - printed: "9"
    value: "272.00"
    work: "Form 4952 line 8 = 272.00"
  - printed: "10"
    value: "2704.00"
    work: "2,432.00 + 272.00 = 2,704.00"
  - printed: "12"
    value: "0.00"
    work: "No supported noncash donations given = 0"
  - printed: "14"
    value: "18821.00"
    work: "18,821.00 + 0.00 + 0.00 = 18,821.00"
  - printed: "17"
    value: "80583.05"
    work: "19,058.05 + 40,000.00 + 2,704.00 + 18,821.00 + 0.00 + 0.00 = 80,583.05"
```
```

### classm.sa.7

```yaml
```yaml
lines:
  - printed: "2"
    value: "50053.00"
    work: "Form 1040 line 11b AGI = 50,053.00"
  - printed: "3"
    value: "3753.98"
    work: "50,053.00 x 0.075 = 3,753.975, rounded to 3,753.98"
  - printed: "4"
    value: "0.00"
    work: "Line 1 0.00 - 3,753.98 is less than zero, so enter -0-"
  - printed: "5d"
    value: "17372.00"
    work: "17,372.00 + 0.00 + 0.00 = 17,372.00"
  - printed: "5e"
    value: "17372.00"
    work: "HOH, AGI not over $500,000, no Form 2555/4563/PR exclusion; smaller of 17,372.00 or 40,000 = 17,372.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or GST deduction; enter zero"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098; enter zero"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098; enter zero"
  - printed: "13"
    value: "0.00"
    work: "No carryover from a prior year; enter zero"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss; enter zero"
  - printed: "16"
    value: "0.00"
    work: "Gambling losses 0.00 are limited to Schedule 1 line 8b winnings of 0.00; no other line 16 items"
  - printed: "7"
    value: "17372.00"
    work: "17,372.00 + 0.00 = 17,372.00"
  - printed: "8e"
    value: "18271.00"
    work: "18,271.00 + 0.00 + 0.00 = 18,271.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "18271.00"
    work: "18,271.00 + 0.00 = 18,271.00"
  - printed: "12"
    value: "3981.00"
    work: "Noncash gifts 296.00 + 3,685.00 = 3,981.00"
  - printed: "14"
    value: "13048.00"
    work: "9,067.00 + 3,981.00 + 0.00 = 13,048.00"
  - printed: "17"
    value: "48691.00"
    work: "0.00 + 17,372.00 + 18,271.00 + 13,048.00 + 0.00 + 0.00 = 48,691.00"
```
```
