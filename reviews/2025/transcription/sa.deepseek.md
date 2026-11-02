# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 05207ae10d6b53be05f8a3f4cc4756f2c59a442edeaad971454e6d805079a695 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 8a2cf158dc717fdc1609475961788400412aab9968abb6781c3652273bdc7c5d |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 131072 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 020691577e6a177170e9b20d041662f1cabe6c2c88cf306ab0c7a09a508e07cf |
| printed lines compared | 22 |
| agree / disagree / missing | 16 / 6 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### sa.age65 — Were you born before January 2, 1961?
Status: **AGREE**

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, "then": {"param": "sa.standard_extra"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Ruling: model error — the candidate's standard deduction counts people with an age-65 or blindness box rather than boxes (one amount when a person is both), ignores person.died_before_65, and compares with its own line 17; i1040gi p. 33, Line 12d, checks the appropriate box(es) for each of you and your spouse and excludes a spouse born before January 2, 1961 who died in 2025 before age 65. Triage: 2480 comparisons; 26 completed-return value differences; the project follows the source.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, "then": {"param": "sa.standard_extra"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, "then": {"param": "sa.standard_extra"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, "then": {"param": "sa.standard_extra"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error — both of the candidate's deduction amounts are wrong as ruled at sa.itemizes (box count by person, no died-before-65 rule, its own lines 9, 12 and 16), so the selection between them reproduces those errors. i1040gi p. 34, Line 12e: take the larger of the standard deduction or itemized deductions. Triage: 2480 comparisons; 264 value differences.

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
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"from": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"const": 0}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"from": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"const": 0}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: model error — i1040sca p. 7, State and Local Tax Deduction Worksheet, line 1 enters $40,000 for every filing status and applies the married-filing-separately halving once to the line 9 result; the candidate halves $40,000 at line 1 and halves line 9 again, so an MFS filer above $250,000 is held to $5,000. Triage: 2480 comparisons; 52 value differences.

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

Ruling: model error — i1040sca p. 11, Other Itemized Deductions: gambling losses are deductible only to the extent of gambling winnings reported on Schedule 1 line 8b. The project asks sa.gambling_losses only when s1.gambling_winnings is positive (amb.2025.gambling_losses); the candidate's unguarded smaller_of needs it on every return (1278 candidate-unknown).

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
{"ref": "f4952.line6"}
```

Ruling: interface gap — the reviewer's pages were f1040sa p. 1, i1040gi pp. 33–35, i1040sca pp. 1, 7, 11 and p525 p. 33: Form 4952 and i1040sca p. 9 are not among them. The deduction on Schedule A line 9 is Form 4952 line 8 (i1040sca p. 9, "Complete and attach Form 4952 to figure your deduction"), as the project has it; the candidate copies line 7, the carryforward. Triage: 2480 comparisons; 554 value differences, all explained by the missing page.

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits
Status: **AGREE**

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "10"}, {"line": "14"}, {"line": "15"}, {"line": "16"}, {"line": "4"}, {"line": "7"}], "op": "sum"}
```

Second:

```json
{"of": [{"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "15"}, {"line": "16"}, {"line": "4"}, {"line": "5e"}, {"line": "6"}, {"line": "8e"}, {"line": "9"}], "op": "sum"}
```

Ruling: model error — i1040sca p. 12, line 17: "Add lines 4, 7, 10, 14, 15, and 16." The candidate adds a different set (its lines 11, 12, 13, 15, 16, 4, 5e, 6, 8e, 9), so its total differs on 127 completed returns (project $4,616.50 against $4,930.70 on classm.f8889.1.deepseek); 2480 comparisons, 285 value differences.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sa.itemizes | sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | - |
| sa.deduction | sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | - |
| 5e | sa.excluded_income | - |
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
lines:
  - id: sa.line2
    printed: "2"
    label: >-
      Enter amount from Form 1040 or 1040-SR, line 11b
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {const: 0}}
    note: >-
      The printed line says enter Form 1040 or 1040-SR line 11b. The declared
      type is NonNegDollars, so the expression floors a negative AGI at zero.
  - id: sa.line3
    printed: "3"
    label: >-
      Multiply line 2 by 7.5% (0.075)
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}
  - id: sa.line4
    printed: "4"
    label: >-
      Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.line1, take: sa.line3}
  - id: sa.line5d
    printed: "5d"
    label: >-
      Add lines 5a through 5c
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5a, sa.line5b, sa.line5c]}
  - id: sa.line5e
    printed: "5e"
    label: >-
      Enter the smaller of line 5d or $40,000 ($20,000 if married filing
      separately). If Form 1040 or 1040-SR, line 11b is more than $500,000
      ($250,000 if married filing separately), or if you completed Form 2555,
      Form 4563, or excluded income from Puerto Rico, see instructions
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.h_salt_cap, sa.line5d]}
    refuses: [sa.excluded_income]
  - id: sa.line6
    printed: "6"
    label: >-
      Other taxes. List type and amount:
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
  - id: sa.line8b
    printed: "8b"
    label: >-
      Home mortgage interest not reported to you on Form 1098. See
      instructions if limited. If paid to the person from whom you bought the
      home, see instructions and show that person's name, identifying no., and
      address
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
  - id: sa.line8c
    printed: "8c"
    label: >-
      Points not reported to you on Form 1098. See instructions for special
      rules
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
  - id: sa.line13
    printed: "13"
    label: >-
      Carryover from prior year
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.charity_limited]
  - id: sa.line15
    printed: "15"
    label: >-
      Casualty and theft loss(es) from a federally declared disaster (other
      than net qualified disaster losses). Attach Form 4684 and enter the
      amount from line 18 of that form. See instructions
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
  - id: sa.line16
    printed: "16"
    label: >-
      Other—from list in instructions. List type and amount:
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
  - id: sa.line7
    printed: "7"
    label: >-
      Add lines 5e and 6
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5e, sa.line6]}
  - id: sa.line8e
    printed: "8e"
    label: >-
      Add lines 8a through 8c
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8a, sa.line8b, sa.line8c]}
    refuses: [sa.unsupported]
  - id: sa.line9
    printed: "9"
    label: >-
      Investment interest. Attach Form 4952 if required. See instructions
    type: NonNegDollars
    expr: {op: copy, from: f4952.line6}
  - id: sa.line10
    printed: "10"
    label: >-
      Add lines 8e and 9
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8e, sa.line9]}
  - id: sa.line12
    printed: "12"
    label: >-
      Other than by cash or check. If you made any gift of $250 or more, see
      instructions. You must attach Form 8283 if over $500
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}
    refuses: [sa.charity_limited]
  - id: sa.line14
    printed: "14"
    label: >-
      Add lines 11 through 13
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
    refuses: [sa.charity_limited]
  - id: sa.line17
    printed: "17"
    label: >-
      Add the amounts in the far right column for lines 4 through 16. Also,
      enter this amount on Form 1040 or 1040-SR, line 12e
    type: NonNegDollars
    expr:
      op: sum
      of:
        - sa.line4
        - sa.line5e
        - sa.line6
        - sa.line8e
        - sa.line9
        - sa.line11
        - sa.line12
        - sa.line13
        - sa.line15
        - sa.line16
    refuses: [sa.unsupported, sa.charity_limited, sa.excluded_income]
  - id: sa.agi
    printed: "(helper)"
    label: >-
      Adjusted gross income from Form 1040 or 1040-SR, line 11b
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.h_taxpayer_age65_count
    printed: "(helper)"
    label: >-
      Count of taxpayers whose age-65 box is checked
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
  - id: sa.age65
    printed: "(helper)"
    label: >-
      Taxpayer was born before January 2, 1961
    type: Bool
    expr:
      op: test
      gt: [sa.h_taxpayer_age65_count, {const: 0, type: Count}]
    note: >-
      The IRS pages do not define a single taxpayer age-65 flag. Interpreted as
      whether the taxpayer's person.age65 box is checked. The spouse's age and
      blindness are handled in the standard deduction helpers.
  - id: sa.h_zero
    printed: "(helper)"
    label: >-
      Zero amount
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sa.h_mfs
    printed: "(helper)"
    label: >-
      Married filing separately
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: sa.h_extra_per_box
    printed: "(helper)"
    label: >-
      Additional standard deduction per age or blindness box
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
  - id: sa.h_std_base
    printed: "(helper)"
    label: >-
      Basic standard deduction for filing status
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}
  - id: sa.h_boxes_base
    printed: "(helper)"
    label: >-
      Number of age or blindness boxes for persons on the return
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        any:
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.blind, {const: true}]}
  - id: sa.h_boxes_extra_amount
    printed: "(helper)"
    label: >-
      Additional standard deduction for boxes on the return
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_extra_per_box, count: sa.h_boxes_base}
  - id: sa.h_spouse_extra_amount
    printed: "(helper)"
    label: >-
      Additional standard deduction for a separate spouse's age or blindness box
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sa.h_mfs, {const: true}]}
              - {op: test, eq: [sa.spouse_extra, {const: true}]}
          then: sa.h_extra_per_box
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sa.h_mfs, {const: true}]}
                - {op: test, eq: [sa.spouse_extra, {const: true}]}
          then: sa.h_zero
    note: >-
      The input sa.spouse_extra is a single Bool. Interpreted as one additional
      box for the separate spouse, because the interface does not distinguish
      an age box from a blindness box for that spouse.
  - id: sa.h_std_raw
    printed: "(helper)"
    label: >-
      Standard deduction before the spouse-itemizes exception
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_boxes_extra_amount, sa.h_spouse_extra_amount]}
  - id: sa.h_std_after_spouse
    printed: "(helper)"
    label: >-
      Standard deduction after the spouse-itemizes exception
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_std_raw
  - id: sa.h_standard
    printed: "(helper)"
    label: >-
      Standard deduction
    type: NonNegDollars
    expr: {op: copy, from: sa.h_std_after_spouse}
    refuses: [sa.dependent]
  - id: sa.h_salt_base_full
    printed: "(helper)"
    label: >-
      SALT worksheet line 1 full base
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
  - id: sa.h_salt_base_half
    printed: "(helper)"
    label: >-
      SALT worksheet line 1 MFS base
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_base_full, rate: {param: sa.half}}
  - id: sa.h_salt_base
    printed: "(helper)"
    label: >-
      SALT worksheet line 1 base by filing status
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_mfs, {const: true}]}
          then: sa.h_salt_base_half
        - guard: {op: test, eq: [sa.h_mfs, {const: false}]}
          then: sa.h_salt_base_full
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: >-
      SALT worksheet floor
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt_threshold
    printed: "(helper)"
    label: >-
      SALT worksheet AGI threshold
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
  - id: sa.h_salt_excess
    printed: "(helper)"
    label: >-
      SALT worksheet line 6 excess
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_threshold}
  - id: sa.h_salt_reduction
    printed: "(helper)"
    label: >-
      SALT worksheet line 7 reduction
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_excess, rate: {param: sa.salt_rate}}
  - id: sa.h_salt_reduced
    printed: "(helper)"
    label: >-
      SALT worksheet line 8 reduced base
    type: Dollars
    expr: {op: subtract, from: sa.h_salt_base, take: sa.h_salt_reduction}
  - id: sa.h_salt_reduced_pos
    printed: "(helper)"
    label: >-
      SALT worksheet line 8 floored at zero
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_reduced, take: {const: 0}}
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: >-
      SALT worksheet line 9
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_reduced_pos, sa.h_salt_floor]}
  - id: sa.h_salt_line9_mfs_half
    printed: "(helper)"
    label: >-
      SALT worksheet line 9 half for MFS
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
  - id: sa.h_salt_cap
    printed: "(helper)"
    label: >-
      SALT cap before comparing with line 5d
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_mfs, {const: true}]}
          then: sa.h_salt_line9_mfs_half
        - guard: {op: test, eq: [sa.h_mfs, {const: false}]}
          then: sa.h_salt_line9
  - id: sa.itemizes
    printed: "(helper)"
    label: >-
      Itemize deductions
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_standard]}
    refuses: [sa.dependent, sa.unsupported, sa.charity_limited, sa.excluded_income]
  - id: sa.deduction
    printed: "(helper)"
    label: >-
      Standard deduction or itemized deductions, whichever applies
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_standard
    refuses: [sa.dependent, sa.unsupported, sa.charity_limited, sa.excluded_income]
```
