# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 14be893889613c275e411636a9c4f8908e0bbbd991bb3b1aa4077f5205b9fbaf |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 1af68fa859be9173089a0c6113845cd71f854e0b6a1e3407d0da674587242431 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | db1543ebd2f331ad735d7efc1b1ec2f167dca06d6045bc946d2835324faaefa0 |
| printed lines compared | 22 |
| agree / disagree / missing | 16 / 6 / 0 |
| extra printed lines in second | none |

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

### sa.age65 — Were you born before January 2, 1961?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}], "test": "lt"}
```

Ruling: model error; f1040s1a (2025), line 36a: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35", with the spouse on line 36b; i1040gi p. 33, Line 12d, separates the boxes for you and for your spouse. sa.age65 is the published question "Were you born before January 2, 1961?" for you alone (its consumer is Schedule 1-A line 36a); the candidate reads it as whether any person entry, yours or your spouse's, was born before January 2, 1961. The 16 completed-return value differences (project false, candidate true) are returns where you were not born before January 2, 1961 but your joint spouse was: classm.f8962.5.deepseek (spouse age 65 or older, you not), classm.f8962.5.gpt, classm.scveh.1, mutation.t2.f8962_months_asset3, generated returns 208, 254, 255, 290, 366, 373, 395 and 476, and four partial records of classm.f8962.5.gpt (sa.spouse_extra, sa.spouse_itemizes, sa.elect_itemize or sa.gambling_losses withheld). Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 2,475 agree; differences 45 value; on completed returns 16 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### sa.agi — Form 1040 line 11b adjusted gross income
Status: **AGREE**

### sa.itemizes — Itemize if elected, required, or itemized total exceeds standard
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Ruling: model error; i1040gi p. 33, Line 12d: "Death of spouse in 2025. If your spouse was born before January 2, 1961, but died in 2025 before reaching age 65, don’t check the box that says “Spouse was born before January 2, 1961.”"; i1040gi p. 33, Line 12b: "If your filing status is married filing separately and your spouse itemizes deductions on their return, check the box on line 12b"; p. 14: "You also can’t take the standard deduction if your spouse itemizes deductions" (Married Filing Separately); i1040sca p. 11, Line 16: "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets) but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." The candidate's standard deduction counts every person entry born before January 2, 1961 without the died-before-65 rule, applies sa.spouse_itemizes without the married-filing-separately condition, and its line 17 needs sa.gambling_losses without winnings. The one completed-return value record is classm.f5695.8.deepseek: classm.f5695.8.deepseek is a single return whose record answers sa.spouse_itemizes Yes ("Married filing separately with a spouse who itemizes?"); the project's sa.mfs_spouse_itemizes requires married filing separately, so it takes the $15,750.00 standard deduction against line 17 of $7,874.00, where the candidate itemizes. The interview cannot produce that record (a single filer answers No to a question that opens "Married filing separately"), and married filing separately is itself refused (s3.mfs). The completed-return candidate-unknown (165: sa.gambling_losses 124, f4952.unsupported 13, sa.spouse_extra 12, sa.spouse_itemizes 12, sa.elect_itemize 4) and candidate-refuses (13: f4952.unsupported 10, f4952.alternative_allocation 3, through its line 9, ruled interface gap there) are answers or screens the source does not need on those returns. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 1,374 agree; differences 53 candidate-refuses, 1090 candidate-unknown, 1 project-unknown, 2 value; on completed returns 13 candidate-refuses, 165 candidate-unknown, 1 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error; inherited from sa.itemizes. i1040gi p. 34, Line 12e: "your federal income tax will be less if you take the larger of your standard deduction or itemized deductions". The one completed-return value record is classm.f5695.8.deepseek (classm.f5695.8.deepseek is a single return whose record answers sa.spouse_itemizes Yes ("Married filing separately with a spouse who itemizes?"); the project's sa.mfs_spouse_itemizes requires married filing separately, so it takes the $15,750.00 standard deduction against line 17 of $7,874.00, where the candidate itemizes. The interview cannot produce that record (a single filer answers No to a question that opens "Married filing separately"), and married filing separately is itself refused (s3.mfs)). Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 1,369 agree; differences 58 candidate-refuses, 1088 candidate-unknown, 2 project-refuses, 1 project-unknown, 2 value; on completed returns 13 candidate-refuses, 165 candidate-unknown, 1 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 2 — Amount from sa.agi_floor
Status: **AGREE**

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"ref": "f1040.line11b"}, {"param": "sa.salt_threshold"}], "test": "le"}, "then": {"param": "sa.salt_base"}}, {"guard": {"args": [{"param": "sa.salt_threshold"}, {"ref": "f1040.line11b"}], "test": "lt"}, "then": {"of": [{"from": {"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"param": "sa.salt_floor"}}, {"param": "sa.salt_floor"}], "op": "sum"}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"ref": "f1040.line11b"}, {"param": "sa.salt_threshold"}], "test": "le"}, "then": {"param": "sa.salt_base"}}, {"guard": {"args": [{"param": "sa.salt_threshold"}, {"ref": "f1040.line11b"}], "test": "lt"}, "then": {"of": [{"from": {"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"param": "sa.salt_floor"}}, {"param": "sa.salt_floor"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}
```

Second transcription's note: The SALT worksheet is applied as printed: the $40,000 base and $10,000 floor are halved for married filing separately at the final step.

Ruling: scope; i1040sca p. 7, State and Local Tax Deduction Worksheet, line 10: "State and local tax deduction. Enter the smaller of the amount on line 9 (half the amount on line 9 if married filing separately) or the amount from Schedule A, line 5d". The candidate's worksheet (the $40,000 base reduced by 30% of the excess over the threshold, floored at $10,000, halved at the last step for married filing separately) gives the project's amount; no value differs. The differences are its own sa.excluded_income refusal (worksheet lines 3a to 3d, Puerto Rico and Form 2555/4563 exclusions), which the project refuses elsewhere on the return, and project refusals on upstream screens; every witness is a refused or incomplete return, and married filing separately is refused (s3.mfs). Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 2,463 agree; differences 17 candidate-refuses, 31 candidate-unknown, 9 project-refuses; on completed returns no difference. Project stands.

### 6 — Amount from sa.zero
Status: **AGREE**

### 8b — Amount from sa.zero
Status: **AGREE**

### 8c — Amount from sa.zero
Status: **AGREE**

### 13 — Amount from sa.zero
Status: **AGREE**

### 15 — Amount from sa.zero
Status: **AGREE**

### 16 — Other—from list in instructions. List type and amount:
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "s1.gambling_winnings"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "s1.gambling_winnings"}], "test": "lt"}, "then": {"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}
```

Ruling: model error; i1040sca p. 11, Line 16: "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets) but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." The project enters zero without gambling winnings and the smaller of sa.gambling_losses and Schedule 1 line 8b otherwise; the candidate takes the smaller of the two always, so it needs sa.gambling_losses on every return though the amount is zero without winnings (all 143 completed-return differences are candidate-unknown for sa.gambling_losses). No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 1,027 agree; differences 1395 candidate-unknown, 58 project-refuses, 40 project-unknown; on completed returns 143 candidate-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **DISAGREE**

Project:

```json
{"ref": "f4952.line8"}
```

Second:

```json
{"of": [{"ref": "f4952.line3"}, {"ref": "f4952.line6"}], "op": "smaller_of"}
```

Ruling: interface gap; f4952 (2025) p. 3, Who Must File: "you must file Form 4952 to claim a deduction for your investment interest expense"; i1040sca p. 9, Line 9: "Complete and attach Form 4952 to figure your deduction." The deduction on Schedule A line 9 is Form 4952 line 8, as the project has it; since PENDING-6 of the credits-misc package, line 8 is zero without reaching the Form 4952 screens when Form 4952 is not used (f4952.used: an election, a carryforward or line 1 above zero). The candidate rebuilds line 8 as the smaller of lines 3 and 6, which carry those screens, so it refuses at f4952.unsupported or f4952.alternative_allocation, or is unknown for f4952.unsupported, on returns that do not use Form 4952 (13 completed-return candidate-refuses, e.g. classm.f8962.1.deepseek, classm.clcw.2; 13 candidate-unknown, e.g. classm.s3.2, classm.sc.1, each with project $0.00). The log's Source pages table shows the reviewer received f1040sa p. 1, i1040gi pp. 33-35, i1040sca pp. 1, 2, 3, 6, 7, 11 and p502, i8962, p969 and p525 pages: no Form 4952 page and not i1040sca p. 9, so the guard was not visible. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 525 partial records from 40 bases; 2,520 comparisons): 2,304 agree; differences 111 candidate-refuses, 105 candidate-unknown; on completed returns 13 candidate-refuses, 13 candidate-unknown. Project stands.

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits
Status: **AGREE**

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sa.itemizes | f4952.alternative_allocation, f4952.unsupported, sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| sa.deduction | f4952.alternative_allocation, f4952.unsupported, sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| 5e | sa.excluded_income | - |
| 6 | sa.unsupported | - |
| 8b | sa.unsupported | - |
| 8c | sa.unsupported | - |
| 13 | sa.charity_limited | - |
| 15 | sa.unsupported | - |
| 16 | sa.unsupported | - |
| 7 | sa.excluded_income, sa.unsupported | - |
| 8e | sa.unsupported | - |
| 9 | f4952.alternative_allocation, f4952.unsupported | - |
| 10 | f4952.alternative_allocation, f4952.unsupported, sa.unsupported | - |
| 12 | sa.charity_limited | - |
| 14 | sa.charity_limited | - |
| 17 | f4952.alternative_allocation, f4952.unsupported, sa.charity_limited, sa.excluded_income, sa.unsupported | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sa.age65 | 768f14dd86250bfb0df776167739722ee3b518315715c3b6282afb7074c8541b |
| sa.agi | 7ac40a0d224f103b5668b2d9b355ac1ecb9b68c3d5235bd8ae09b20888315bc8 |
| sa.itemizes | ad4db0f95ab83183ecdedb3a2b0d58c4d33534be64ba6ab315ad5cad220949be |
| sa.deduction | cadc70373beef251c7ce5e4a979aafa7485532c86652393a759e1036cc0ef0cc |
| 2 | 6ed9e8826b6917afade8428ad8ba0ef06fdbb723500482b53bce904f69e95014 |
| 3 | 4606a9bdca74892e9959452bafe144fe3a9c24d25b48c83ee961469221a4b4c3 |
| 4 | 3e76ff364e4e11c3472e01259f76b707dfc78422a8c93abe7d4e9deb5d8fafbe |
| 5d | fb4eee7436051e32595ede198f689933a427b0f7416511f9c4194a0cfb7febdf |
| 5e | 0762d68e00b9d72f8d0f0038205ed4ce3626ba29164c5743fb3d673cc4d286ef |
| 6 | 8e7cfae2b9add8293cde806261e2967eec63604ca5d8c96c919f57e050d97b0f |
| 8b | 08e60f0d38ae0fe9c5aa02875e5b98f24cb3d837d65ca474ee364f3f1c3ce5db |
| 8c | ed964e2d8103bb043e16af84ffda146b310095768d2bf3ba5affbf75c73bbc22 |
| 13 | 3b2f227fc6f9276a14fc2e95225c3ce6ebb2e6540eec1675158b44b73d4e78ff |
| 15 | 6f20b2760034d6da2085c4c5eaeaf6ec12bb56641fefcb87dfec425ea5466ba1 |
| 16 | bc94551e3e016b4a7a61a6231b190fb8b3e57cad86bee2639e9ec4e5d7fac4a7 |
| 7 | f01dc441865ba4d227e6810328f38376b883f341b25679842cfe8a31fbf9aee0 |
| 8e | 5f6bb65fc20292add3f19c02137e4eab05e81a61f2a1e8da6bec29434b678658 |
| 9 | 6afefd4a342b5f5749c93d7aab8c5b7494cd95445e619cb164a79b29df97b69b |
| 10 | 320b71964696452137d0967c5995c1f6bc29fe3f800b4d8feff670ecdcf79f8a |
| 12 | f7798b1da5cd3cbbdaece0aa7f693e350ece6c4141530d0cd53593556cbd3b7a |
| 14 | c37b1e535791ea619bf78cfdf3ffcf20d537bef0eb764479222f46493ccda43b |
| 17 | 1627818731b5bbf9dd5e60d5830e64f50beb2c702503544e409ba1b280568c1c |
| (rest of the document) | 4ab44412ed063c2bc602f385d7b58b759dbf415cd3a4e78f694db4b2cde08b0a |

## Raw second transcription

```yaml
lines:
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sa.agi
      take: {const: 0}
    note: "The interface declares line 2 as NonNegDollars; Form 1040 line 11b is copied with a zero floor if it is negative."
  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: sa.line2
      rate: {param: sa.medical_rate}
  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sa.line1
      take: sa.line3
  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line5a, sa.line5b, sa.line5c]
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [sa.h_salt_final_cap, sa.line5d]
    refuses: [sa.excluded_income]
    note: "The SALT worksheet is applied as printed: the $40,000 base and $10,000 floor are halved for married filing separately at the final step."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount:"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    refuses: [sa.unsupported]
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098. See instructions if limited. If paid to the person from whom you bought the home, see instructions and show that person’s name, identifying no., and address"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    refuses: [sa.unsupported]
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098. See instructions for special rules"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    refuses: [sa.unsupported]
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    refuses: [sa.charity_limited]
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form. See instructions"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    refuses: [sa.unsupported]
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount:"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [sa.gambling_losses, s1.line8b]
    refuses: [sa.unsupported]
  - id: sa.line7
    printed: "7"
    label: "Add lines 5e and 6"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line5e, sa.line6]
  - id: sa.line8e
    printed: "8e"
    label: "Add lines 8a through 8c"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line8a, sa.line8b, sa.line8c]
  - id: sa.line9
    printed: "9"
    label: "Investment interest. Attach Form 4952 if required. See instructions"
    type: NonNegDollars
    expr:
      op: copy
      from: f4952.deduction
    refuses: [f4952.unsupported, f4952.alternative_allocation]
  - id: sa.line10
    printed: "10"
    label: "Add lines 8e and 9"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line8e, sa.line9]
  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made any gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: gift
      field: gift.allowed
    refuses: [sa.charity_limited]
  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line11, sa.line12, sa.line13]
    refuses: [sa.charity_limited]
  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]
  - id: sa.age65
    printed: "(helper)"
    label: "Whether you or your spouse was born before January 2, 1961 (age 65 or older at the end of 2025)"
    type: Bool
    expr:
      op: test
      gt: [sa.h_age65_count, {const: 0, type: Count}]
  - id: sa.agi
    printed: "(helper)"
    label: "Adjusted gross income from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr:
      op: copy
      from: f1040.line11b
  - id: sa.itemizes
    printed: "(helper)"
    label: "Whether you itemize deductions on Schedule A for 2025"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_std]}
  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions from Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard:
            op: test
            not:
              op: test
              eq: [sa.itemizes, {const: true}]
          then: sa.h_std
  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: sa.h_age65_count
    printed: "(helper)"
    label: "Number of persons on the return age 65 or older"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: [person.age65, {const: true}]
  - id: sa.h_blind_box_count
    printed: "(helper)"
    label: "Number of persons on the return blind at the end of 2025"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: [person.blind, {const: true}]
  - id: sa.h_box_count
    printed: "(helper)"
    label: "Total age and blindness boxes checked for the taxpayer and spouse"
    type: Count
    expr:
      op: sum
      of: [sa.h_age65_count, sa.h_blind_box_count]
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction base amount for the filing status"
    type: NonNegDollars
    expr:
      op: param
      ref: sa.standard_base
  - id: sa.h_std_extra_line
    printed: "(helper)"
    label: "Additional standard deduction per age or blindness box"
    type: NonNegDollars
    expr:
      op: param
      ref: sa.standard_extra
  - id: sa.h_extra_amount
    printed: "(helper)"
    label: "Additional standard deduction for age and blindness boxes"
    type: NonNegDollars
    expr:
      op: multiply_count
      amount: sa.h_std_extra_line
      count: sa.h_box_count
  - id: sa.h_std_normal
    printed: "(helper)"
    label: "Standard deduction before the married filing separately spouse-itemizes rule"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.h_std_base, sa.h_extra_amount]
  - id: sa.h_std
    printed: "(helper)"
    label: "Standard deduction for 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard:
            op: test
            not:
              op: test
              eq: [sa.spouse_itemizes, {const: true}]
          then: sa.h_std_normal
    refuses: [sa.dependent, sa.spouse_extra]
  - id: sa.h_salt_threshold
    printed: "(helper)"
    label: "SALT phaseout threshold for the filing status"
    type: NonNegDollars
    expr:
      op: param
      ref: sa.salt_threshold
  - id: sa.h_salt_cap
    printed: "(helper)"
    label: "SALT worksheet line 1 cap"
    type: NonNegDollars
    expr:
      op: param
      ref: sa.salt_base
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT worksheet line 9 floor"
    type: NonNegDollars
    expr:
      op: param
      ref: sa.salt_floor
  - id: sa.h_salt_over
    printed: "(helper)"
    label: "Whether AGI exceeds the SALT phaseout threshold"
    type: Bool
    expr:
      op: test
      gt: [sa.agi, sa.h_salt_threshold]
  - id: sa.h_salt_excess
    printed: "(helper)"
    label: "AGI in excess of the SALT phaseout threshold"
    type: Dollars
    expr:
      op: subtract
      from: sa.agi
      take: sa.h_salt_threshold
  - id: sa.h_salt_phase
    printed: "(helper)"
    label: "SALT phaseout reduction"
    type: Dollars
    expr:
      op: multiply_rate
      amount: sa.h_salt_excess
      rate: {param: sa.salt_rate}
  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT worksheet line 8"
    type: Dollars
    expr:
      op: subtract
      from: sa.h_salt_cap
      take: sa.h_salt_phase
  - id: sa.h_salt_floor_diff
    printed: "(helper)"
    label: "SALT worksheet line 8 over the floor, floored at zero"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sa.h_salt_line8
      take: sa.h_salt_floor
  - id: sa.h_salt_line9_over
    printed: "(helper)"
    label: "SALT worksheet line 9 when AGI exceeds the threshold"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.h_salt_floor, sa.h_salt_floor_diff]
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT worksheet line 9"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_salt_over, {const: true}]}
          then: sa.h_salt_line9_over
        - guard:
            op: test
            not:
              op: test
              eq: [sa.h_salt_over, {const: true}]
          then: sa.h_salt_cap
  - id: sa.h_is_mfs
    printed: "(helper)"
    label: "Whether the filing status is married filing separately"
    type: Bool
    expr:
      op: test
      eq: [f1040.status, {const: "mfs"}]
  - id: sa.h_salt_half
    printed: "(helper)"
    label: "Half of SALT worksheet line 9 for married filing separately"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: sa.h_salt_line9
      rate: {param: sa.half}
  - id: sa.h_salt_final_cap
    printed: "(helper)"
    label: "SALT cap after applying the married filing separately halving"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}
          then: sa.h_salt_half
        - guard:
            op: test
            not:
              op: test
              eq: [sa.h_is_mfs, {const: true}]
          then: sa.h_salt_line9
```
