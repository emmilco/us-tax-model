# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 83b7208aafbda50b78badb5a09ce0db28fe11aecdcefcbcd4257fe04a0e4b475 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 233d34af8788f07ed9c930fdfedc03fa88f550fd9fa5ffc3e4de3e1f3c883d82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 2b65b38ab5b3b60fe9ee7aea0c8532c37fcc95869af6ec9a1e0705376cd919ec |
| printed lines compared | 22 |
| agree / disagree / missing | 18 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
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
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}], "test": "lt"}], "test": "any"}
```

Second transcription's note: Open point: the pages do not define this interface. It is read as 'an age box on line 12d is checked' (you, or your spouse on a joint return, born before January 2, 1961), excluding a person who died in 2025 before reaching 65. Blindness is not included.

Ruling: model error; sa.age65 is the taxpayer's box, "Were you born before January 2, 1961?" (f1040 line 12d, "You: Were born before January 2, 1961"). The candidate adds the spouse on a joint return, which is a separate box. Triage executable-triage-v2 (triage/sa.json): 2429 of 2487 comparisons agree; on completed returns {"value": 21}.

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The instructions say to take the larger of the standard deduction or itemized deductions. A tie is treated as not itemizing unless the line 18 election is made; the deduction amount is the same either way.

Ruling: model error; i1040gi p. 34, line 12e). The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/sa.json): 1451 of 2487 comparisons agree; on completed returns {"candidate-unknown": 118}.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error; The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/sa.json): 1449 of 2487 comparisons agree; on completed returns {"candidate-unknown": 118}.

### 2 — Amount from sa.agi_floor
Status: **AGREE**

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

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

Second transcription's note: Only gambling losses are computed. They are allowed 'only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'. All other line 16 items are screened by sa.unsupported.

Ruling: model error; amb.2025. The candidate needs answers, applies screens or shows amounts on completed returns where the source does not require them. Triage executable-triage-v2 (triage/sa.json): 1111 of 2487 comparisons agree; on completed returns {"candidate-unknown": 102}.

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **AGREE**

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
| sa.itemizes | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| sa.deduction | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| 5d | sa.unsupported | sa.unsupported |
| 5e | sa.excluded_income, sa.unsupported | sa.unsupported |
| 6 | sa.unsupported | - |
| 8b | sa.unsupported | - |
| 8c | sa.unsupported | - |
| 13 | sa.charity_limited | - |
| 15 | sa.unsupported | - |
| 16 | sa.unsupported | - |
| 7 | sa.excluded_income, sa.unsupported | - |
| 8e | sa.unsupported | - |
| 10 | sa.unsupported | - |
| 12 | sa.charity_limited | - |
| 14 | sa.charity_limited | - |
| 17 | sa.charity_limited, sa.excluded_income, sa.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.agi
    printed: "(helper)"
    label: "Amount from Form 1040 or 1040-SR, line 11b (adjusted gross income)"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
    note: "Schedule A line 2 and SALT worksheet line 2 both say to enter the amount from Form 1040 or 1040-SR, line 11b. This keeps the signed value, which the SALT worksheet uses."

  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {const: 0}}
    note: "Open point: the form does not say what to do when line 11b is negative. The required type is NonNegDollars, so a negative AGI is entered as zero. Line 3 is then zero and line 4 equals line 1."

  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}

  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.line1, take: sa.line3}

  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5a, sa.line5b, sa.line5c]}
    refuses: [sa.unsupported]
    note: "The general sales tax election on line 5a is outside the tool and is screened by sa.unsupported. Line 5a holds income taxes only."

  - id: sa.h_salt_base
    printed: "(helper)"
    label: "SALT worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}

  - id: sa.h_salt_excess
    printed: "(helper)"
    label: "SALT worksheet line 6: Subtract line 5 ($500,000; $250,000 if married filing separately) from line 4 (if not more, skip lines 7 and 8)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {param: sa.salt_threshold}}
    note: "Worksheet line 4 is line 2 plus line 3e (lines 3a to 3d are excluded Puerto Rico, Form 2555 and Form 4563 amounts). Those amounts are refused through sa.excluded_income, so line 4 equals AGI. When line 4 is not more than line 5 the result is zero, so line 8 equals line 1. That matches 'skip lines 7 and 8 and enter the amount from line 1 on line 9'."

  - id: sa.h_salt_reduce
    printed: "(helper)"
    label: "SALT worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_excess, rate: {param: sa.salt_rate}}

  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT worksheet line 8: Subtract line 7 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_base, take: sa.h_salt_reduce}
    note: "The worksheet subtracts without a floor. Line 9 takes the larger of line 8 and $10,000, so flooring at zero here does not change line 9."

  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT worksheet line 9 floor: $10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}

  - id: sa.h_salt_half
    printed: "(helper)"
    label: "Half the amount on SALT worksheet line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}

  - id: sa.h_salt_limit
    printed: "(helper)"
    label: "SALT worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_half
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.h_salt_limit, sa.line5d]}
    refuses: [sa.excluded_income]
    note: "The worksheet path is used for every case. When AGI is not over the threshold it gives the smaller of line 5d or $40,000 ($20,000 MFS), as line 5e says. When line 5d is at most $10,000 ($5,000 MFS) it gives line 5d, as the 'Before you begin' rule says. Form 2555, Form 4563 and Puerto Rico exclusions are refused because the worksheet's lines 3a to 3d have no inputs."

  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "A zero-valued money parameter from the catalog, used for lines whose only nonzero cases are refused."

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "Line 6 holds foreign income taxes and generation-skipping tax. Both are screened by sa.unsupported, so the computed case is zero."

  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.charity_limited]

  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "Only gambling losses are computed. They are allowed 'only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'. All other line 16 items are screened by sa.unsupported."

  - id: sa.line7
    printed: "7"
    label: "Add lines 5e and 6"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5e, sa.line6]}

  - id: sa.line8e
    printed: "8e"
    label: "Add lines 8a through 8c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8a, sa.line8b, sa.line8c]}

  - id: sa.line9
    printed: "9"
    label: "Investment interest. Attach Form 4952 if required"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line8}
    note: "The supplied pages do not include the line 9 instructions that name the source line. The interface has no investment interest input, so this copies the deductible investment interest from Form 4952, line 8 (in the catalog). That is assumed to be zero when there is no investment interest."

  - id: sa.line10
    printed: "10"
    label: "Add lines 8e and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8e, sa.line9]}

  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made any gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}
    refuses: [sa.charity_limited]

  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
    refuses: [sa.charity_limited]

  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}

  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for your filing status (amounts to the left of Form 1040 line 12e)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}

  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked on line 12d ($2,000 single or head of household; $1,600 otherwise), from the Standard Deduction Chart"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
    note: "The chart amounts equal the base plus the number of boxes times $2,000 (single, HOH) or $1,600 (MFJ, QSS, MFS). Checked: single 17,750/19,750; MFJ 33,100 to 37,900; QSS 33,100/34,700; MFS 17,350 to 22,150; HOH 25,625/27,625."

  - id: sa.h_tp_age
    printed: "(helper)"
    label: "Box checked: You were born before January 2, 1961"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, not: {op: test, eq: [person.died_before_65, {const: true}]}}
    note: "The death rule in the pages is stated for a spouse who died before reaching 65. For a deceased taxpayer the text refers to Pub. 501, which is not supplied. The per-person question person.died_before_65 asks about any person, so the same rule is applied to the taxpayer."

  - id: sa.h_tp_blind
    printed: "(helper)"
    label: "Box checked: You are blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.blind, {const: true}]}

  - id: sa.h_sp_age
    printed: "(helper)"
    label: "Box checked: Spouse was born before January 2, 1961 (not if spouse died in 2025 before reaching age 65)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, not: {op: test, eq: [person.died_before_65, {const: true}]}}

  - id: sa.h_sp_blind
    printed: "(helper)"
    label: "Box checked: Spouse is blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.blind, {const: true}]}

  - id: sa.h_tp_age_amt
    printed: "(helper)"
    label: "Additional amount for your age box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_tp_age}

  - id: sa.h_tp_blind_amt
    printed: "(helper)"
    label: "Additional amount for your blindness box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_tp_blind}

  - id: sa.h_sp_age_amt
    printed: "(helper)"
    label: "Additional amount for spouse's age box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_sp_age}

  - id: sa.h_sp_blind_amt
    printed: "(helper)"
    label: "Additional amount for spouse's blindness box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_sp_blind}

  - id: sa.h_tp_extra
    printed: "(helper)"
    label: "Additional standard deduction for your boxes"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_tp_age_amt, sa.h_tp_blind_amt]}

  - id: sa.h_sp_extra
    printed: "(helper)"
    label: "Additional standard deduction for spouse's boxes"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_sp_age_amt, sa.h_sp_blind_amt]}

  - id: sa.h_sp_counted
    printed: "(helper)"
    label: "Spouse's boxes counted (joint return only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sa.h_sp_extra
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: sa.h_zero
    note: "Spouse boxes are not checked on a head of household return, and the QSS chart has only 1 or 2 boxes. The married-filing-separately spouse-box case is refused through sa.spouse_extra, so spouse boxes count only on a joint return."

  - id: sa.h_std_full
    printed: "(helper)"
    label: "Standard deduction (base amount plus Standard Deduction Chart additions for boxes checked on line 12d)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_tp_extra, sa.h_sp_counted]}

  - id: sa.h_spouse_itemizes_mfs
    printed: "(helper)"
    label: "Line 12b: married filing separately and your spouse itemizes deductions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, eq: [f1040.status, {const: "mfs"}]}

  - id: sa.h_std
    printed: "(helper)"
    label: "Standard deduction (zero if the box on line 12b is checked)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_spouse_itemizes_mfs, {const: true}]}
          then: sa.h_zero
        - guard: {op: test, eq: [sa.h_spouse_itemizes_mfs, {const: false}]}
          then: sa.h_std_full
    refuses: [sa.dependent, sa.spouse_extra]
    note: "Two cases are refused. Line 12a dependents use the Standard Deduction Worksheet for Dependents, which needs earned income not in this interface; the same question also covers line 12c dual-status aliens. For married filing separately with spouse boxes, the spouse_extra input does not say which boxes (age, blindness) apply, so it is refused."

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize: itemized deductions (line 17) are larger than the standard deduction, or you elect to itemize (line 18)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.line17, sa.h_std]}
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
    note: "The instructions say to take the larger of the standard deduction or itemized deductions. A tie is treated as not itemizing unless the line 18 election is made; the deduction amount is the same either way."

  - id: sa.deduction
    printed: "(helper)"
    label: "Form 1040 or 1040-SR, line 12e: standard deduction or itemized deductions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_std

  - id: sa.age65
    printed: "(helper)"
    label: "Line 12d age box checked: you (or your spouse on a joint return) were born before January 2, 1961"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.h_tp_age, {const: 0, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, gt: [sa.h_sp_age, {const: 0, type: Count}]}
    note: "Open point: the pages do not define this interface. It is read as 'an age box on line 12d is checked' (you, or your spouse on a joint return, born before January 2, 1961), excluding a person who died in 2025 before reaching 65. Blindness is not included."
```
```
