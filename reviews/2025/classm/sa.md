# Class M hand-work — sa

`Schedule A — supported itemized deductions and standard comparison` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f44e5dfe0d9ef02a6953b4ecdf2d9967906e0a91c8afb438f1d743b53be76e92 |
| cases | 8 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.sa.1 — prompt sha256 3c004711fd7f80c33a8f31aa3e2b5a52fe35e32e2de2910269faf0431ebf5096; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

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

### case classm.sa.2 — prompt sha256 1035a5f29cbd33eb5aa84e607d18021221b30d048911e4857a035a689ee6ff55; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:positive, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16#1, sa.form8283:true, sa.standard#1, sa.itemizes:false, sa.deduction#1, sa.mfs_spouse_itemizes:false

### classm.sa.2 — 2 — Amount from sa.agi_floor
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

### case classm.sa.3 — prompt sha256 714f8ff00cf48e056689b2fca8d8622e1dc3424a3a36b3fda2ba67dd11b9d8a6; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.age65:false, sa.spouse_itemizes:true, sa.elect_itemize:false, sa.agi_floor:floor, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16#1, sa.form8283:false, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:true

### classm.sa.3 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $29,744.00

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

### classm.sa.3 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $20,000.00

### classm.sa.3 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $18,753.00

### classm.sa.3 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $18,753.00

### classm.sa.3 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.3 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $18,999.00

### classm.sa.3 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $57,752.00

### case classm.sa.4 — prompt sha256 b8222fbc7f919dc9956beb1b006ddc56916d5d58878ce16357bd1f026547f80f; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.age65:false, sa.elect_itemize:true, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16#1, sa.form8283:false, sa.itemizes:true, sa.deduction#0

### classm.sa.4 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $51,731.00

### classm.sa.4 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $3,879.83

### classm.sa.4 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.4 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $26,362.00

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

### classm.sa.4 — 16 — Other—from list in instructions. List type and amount:
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

Value: $2,204.00

### classm.sa.4 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $22,204.00

### case classm.sa.5 — prompt sha256 14c0868a5a1204ee4ac63387987598bbffae28f3035e1e462d20b024d8549c50; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:true, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:positive, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.5 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $80,962.00

### classm.sa.5 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $6,072.15

### classm.sa.5 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $11,725.85

### classm.sa.5 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $20,401.00

### classm.sa.5 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $20,000.00

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

Value: $20,000.00

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

Value: $14,187.00

### classm.sa.5 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $45,912.85

### case classm.sa.6 — prompt sha256 64381bd2f83d249bd0540762097705f8fa6669959f50c4e7ab6b3bf2261d34be; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:true, sa.mfs_spouse_extra:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.form8283:false, sa.mfs_spouse_itemizes:false

### classm.sa.6 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $50,121.00

### classm.sa.6 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $3,759.08

### classm.sa.6 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.sa.6 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $121.00

### classm.sa.6 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $121.00

### classm.sa.6 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.6 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $280.00

### classm.sa.6 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $401.00

### case classm.sa.7 — prompt sha256 525f3ba9a7ec68c02ee47dcd0bbe2c2a988d0fd7fd83702a7ed1e3237dec4885; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.spouse_extra:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.spouse_itemizes:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:positive, sa.saltremaining:floor, sa.saltfloor_applied:right, sa.mfs:true, sa.saltlimit#0, sa.line5e:right, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.7 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $409,258.00

### classm.sa.7 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $30,694.35

### classm.sa.7 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $62,123.00

### classm.sa.7 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $5,000.00

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

Value: $5,000.00

### classm.sa.7 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $38,012.00

### classm.sa.7 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $38,012.00

### classm.sa.7 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $0.00

### classm.sa.7 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $43,012.00

### case classm.sa.8 — prompt sha256 439bc9067c70d02d0921fa5a11cdc2e74831f2d5f5549900c2bf9bb36442bb0f; branches: sa.unsupported:false, sa.charity_limited:false, sa.excluded_income:false, sa.dependent:false, sa.mfs_spouse_extra:false, sa.age65:false, sa.elect_itemize:false, sa.agi_floor:positive, sa.line4:floor, sa.saltexcess:floor, sa.saltremaining:positive, sa.saltfloor_applied:left, sa.mfs:false, sa.saltlimit#1, sa.line5e:left, sa.line16#1, sa.form8283:false, sa.standard#1, sa.itemizes:true, sa.deduction#0, sa.mfs_spouse_itemizes:false

### classm.sa.8 — 2 — Amount from sa.agi_floor
Status: **AGREE**

Value: $372,102.00

### classm.sa.8 — 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

Value: $27,907.65

### classm.sa.8 — 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

Value: $29,076.00

### classm.sa.8 — 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

Value: $29,076.00

### classm.sa.8 — 6 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 8b — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 8c — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 13 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 15 — Amount from sa.zero
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 16 — Other—from list in instructions. List type and amount:
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 7 — Add sa.line5e, sa.line6
Status: **AGREE**

Value: $29,076.00

### classm.sa.8 — 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

Value: $16,385.00

### classm.sa.8 — 9 — Amount from f4952.line8
Status: **AGREE**

Value: $3,124.00

### classm.sa.8 — 10 — Add sa.line8e, sa.line9
Status: **AGREE**

Value: $19,509.00

### classm.sa.8 — 12 — Total supported noncash donations before income limits
Status: **AGREE**

Value: $0.00

### classm.sa.8 — 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

Value: $3,930.00

### classm.sa.8 — 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

Value: $52,515.00

## Raw responses

### classm.sa.1

```yaml
lines:
  - printed: "2"
    value: "32936.00"
    work: "Form 1040 line 11b AGI = 32,936.00"
  - printed: "3"
    value: "2470.20"
    work: "32,936.00 x 0.075 = 2,470.20"
  - printed: "4"
    value: "0.00"
    work: "Line 1 0.00 - 2,470.20 is less than zero, so enter -0-"
  - printed: "5d"
    value: "39994.00"
    work: "39,994.00 + 0.00 + 0.00 = 39,994.00"
  - printed: "5e"
    value: "39994.00"
    work: "AGI not over $500,000 and no Form 2555/4563/PR exclusion; smaller of 39,994.00 or 40,000 = 39,994.00"
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
    work: "No prior-year carryover, so 0"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss, so 0"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings and no other listed deductions, so 0"
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
    work: "Gift item_a 0.00 + item_b 0.00 = 0.00"
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
    work: "MFS and AGI over 250,000, so use SALT worksheet: L1 40,000; L4 375,980; L6 125,980; L7 37,794; L8 2,206; L9 larger of L8 or 10,000 = 10,000; L10 smaller of half (5,000) or 5d (10,673) = 5,000"
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
    work: "No line 16 items; no gambling winnings"
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
    work: "Noncash gift item_a = 1,943.00"
  - printed: "14"
    value: "5418.00"
    work: "3,475.00 + 1,943.00 + 0.00 = 5,418.00"
  - printed: "17"
    value: "10418.00"
    work: "0.00 + 5,000.00 + 0.00 + 5,418.00 + 0.00 + 0.00 = 10,418.00"
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
    work: "0.00 x 7.5% = 0.00"
  - printed: "4"
    value: "0.00"
    work: "line 1 0.00 - line 3 0.00 = 0.00"
  - printed: "5d"
    value: "29744.00"
    work: "12293.00 + 17451.00 + 0.00 = 29744.00"
  - printed: "5e"
    value: "20000.00"
    work: "MFS, line 11b not over 250000, no 2555/4563/PR: smaller of 29744.00 or 20000.00"
  - printed: "6"
    value: "0.00"
    work: "no foreign or GST tax"
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
    work: "no gambling winnings and no other listed deductions"
  - printed: "7"
    value: "20000.00"
    work: "20000.00 + 0.00 = 20000.00"
  - printed: "8e"
    value: "18753.00"
    work: "18753.00 + 0.00 + 0.00 = 18753.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "18753.00"
    work: "18753.00 + 0.00 = 18753.00"
  - printed: "12"
    value: "0.00"
    work: "no noncash gifts supplied"
  - printed: "14"
    value: "18999.00"
    work: "18999.00 + 0.00 + 0.00 = 18999.00"
  - printed: "17"
    value: "57752.00"
    work: "0.00 + 20000.00 + 18753.00 + 18999.00 + 0.00 + 0.00 = 57752.00"
```
```

### classm.sa.4

```yaml
```yaml
lines:
  - printed: "2"
    value: "51731.00"
    work: "Form 1040 line 11b = 51,731.00"
  - printed: "3"
    value: "3879.83"
    work: "51,731.00 x 0.075 = 3,879.825, rounded to 3,879.83"
  - printed: "4"
    value: "0.00"
    work: "1,945.00 - 3,879.83 < 0, so enter -0-"
  - printed: "5d"
    value: "26362.00"
    work: "6,362.00 + 20,000.00 + 0.00"
  - printed: "5e"
    value: "20000.00"
    work: "Smaller of 26,362.00 or 20,000 (MFS cap); line 11b <= 250,000 and no Form 2555/4563/Puerto Rico exclusion"
  - printed: "6"
    value: "0.00"
    work: "No foreign or generation-skipping tax"
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
    work: "No gambling winnings and no other listed deductions"
  - printed: "7"
    value: "20000.00"
    work: "20,000.00 + 0.00"
  - printed: "8e"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "9"
    value: "0.00"
    work: "Form 4952 line 8 = 0.00"
  - printed: "10"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts given"
  - printed: "14"
    value: "2204.00"
    work: "2,204.00 + 0.00 + 0.00"
  - printed: "17"
    value: "22204.00"
    work: "0.00 + 20,000.00 + 0.00 + 2,204.00 + 0.00 + 0.00"
```
```

### classm.sa.5

```yaml
```yaml
lines:
  - printed: "2"
    value: "80962.00"
    work: "Form 1040 line 11b = 80,962.00"
  - printed: "3"
    value: "6072.15"
    work: "80,962.00 x 0.075 = 6,072.15"
  - printed: "4"
    value: "11725.85"
    work: "17,798.00 - 6,072.15 = 11,725.85"
  - printed: "5d"
    value: "20401.00"
    work: "20,401.00 + 0.00 + 0.00 = 20,401.00"
  - printed: "5e"
    value: "20000.00"
    work: "MFS, line 11b 80,962 <= 250,000, no Form 2555/4563 or Puerto Rico exclusion; smaller of 20,401.00 or 20,000 = 20,000.00"
  - printed: "6"
    value: "0.00"
    work: "No foreign tax or generation-skipping tax deduction"
  - printed: "8b"
    value: "0.00"
    work: "No mortgage interest outside Form 1098"
  - printed: "8c"
    value: "0.00"
    work: "No points outside Form 1098"
  - printed: "13"
    value: "0.00"
    work: "No charitable carryover from a prior year"
  - printed: "15"
    value: "0.00"
    work: "No casualty or theft loss"
  - printed: "16"
    value: "0.00"
    work: "No gambling winnings (Schedule 1 line 8b = 0) and no other listed deductions"
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
    work: "No noncash gifts supplied"
  - printed: "14"
    value: "14187.00"
    work: "14,187.00 + 0.00 + 0.00 = 14,187.00"
  - printed: "17"
    value: "45912.85"
    work: "11,725.85 + 20,000.00 + 0.00 + 14,187.00 + 0.00 + 0.00 = 45,912.85"
```
```

### classm.sa.6

```yaml
```yaml
lines:
  - printed: "2"
    value: "50121.00"
    work: "Form 1040 line 11b = 50,121.00"
  - printed: "3"
    value: "3759.08"
    work: "50,121.00 x 0.075 = 3,759.075, rounded to 3,759.08"
  - printed: "4"
    value: "0.00"
    work: "0.00 - 3,759.08 is less than zero, so enter -0-"
  - printed: "5d"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "5e"
    value: "0.00"
    work: "Smaller of 0.00 or $40,000; AGI is not over $500,000 and there is no Form 2555/4563 or Puerto Rico income"
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
    work: "No gambling winnings, so no gambling losses; no other line 16 items"
  - printed: "7"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "8e"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "9"
    value: "121.00"
    work: "Form 4952 line 8 = 121.00"
  - printed: "10"
    value: "121.00"
    work: "0.00 + 121.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash gifts given"
  - printed: "14"
    value: "280.00"
    work: "280.00 + 0.00 + 0.00"
  - printed: "17"
    value: "401.00"
    work: "0.00 + 0.00 + 121.00 + 280.00 + 0.00 + 0.00"
```
```

### classm.sa.7

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
    work: "MFS and AGI over 250,000, so SALT worksheet: L6 159,258; L7 47,777.40; L8 40,000-47,777.40 = -7,777.40; L9 larger of L8 or 10,000 = 10,000; L10 smaller of half (5,000) or 62,123 = 5,000"
  - printed: "6"
    value: "0.00"
    work: "No foreign or GST tax, so 0"
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
    work: "gift item_a deduction 0.00, so total 0.00"
  - printed: "14"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 = 0.00"
  - printed: "17"
    value: "43012.00"
    work: "0.00 + 5,000.00 + 38,012.00 + 0.00 + 0.00 + 0.00 = 43,012.00"
```

### classm.sa.8

```yaml
```yaml
lines:
  - printed: "2"
    value: "372102.00"
    work: "Form 1040 line 11b = 372,102.00"
  - printed: "3"
    value: "27907.65"
    work: "372,102.00 x 0.075 = 27,907.65"
  - printed: "4"
    value: "0.00"
    work: "18,190.00 - 27,907.65 < 0, so enter -0-"
  - printed: "5d"
    value: "29076.00"
    work: "23,278.00 + 1,360.00 + 4,438.00 = 29,076.00"
  - printed: "5e"
    value: "29076.00"
    work: "AGI <= 500,000, no Form 2555/4563/PR exclusion, so smaller of 29,076.00 or 40,000 = 29,076.00"
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
    work: "No gambling winnings and no other listed deductions"
  - printed: "7"
    value: "29076.00"
    work: "29,076.00 + 0.00 = 29,076.00"
  - printed: "8e"
    value: "16385.00"
    work: "16,385.00 + 0.00 + 0.00 = 16,385.00"
  - printed: "9"
    value: "3124.00"
    work: "Form 4952 line 8 = 3,124.00"
  - printed: "10"
    value: "19509.00"
    work: "16,385.00 + 3,124.00 = 19,509.00"
  - printed: "12"
    value: "0.00"
    work: "No noncash donations given"
  - printed: "14"
    value: "3930.00"
    work: "3,930.00 + 0.00 + 0.00 = 3,930.00"
  - printed: "17"
    value: "52515.00"
    work: "0.00 + 29,076.00 + 19,509.00 + 3,930.00 + 0.00 + 0.00 = 52,515.00"
```
```
