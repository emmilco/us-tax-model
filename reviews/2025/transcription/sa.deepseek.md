# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b4532df4d457f2ad6d8e7a15598ddee33601f9f3dbe758207a2ac3b6c98e9bc0 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d10c9467bfa24ad06502ce549bd3362049153559d5a74950ef5289f3973ec7c1 |
| printed lines compared | 22 |
| agree / disagree / missing | 18 / 4 / 0 |
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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: Uses the larger of itemized and standard, or itemized if the election is made; dependent or dual-status standard deduction is refused.

Ruling: open

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}}], "op": "choose"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second transcription's note: Standard deduction for dependents or dual-status aliens is outside this slice, so sa.dependent is refused.

Ruling: open

### 2 — Amount from sa.agi_floor
Status: **DISAGREE**

Project:

```json
{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"ref": "f1040.line11b"}
```

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"input": "s1.gambling_winnings"}, {"param": "sales.zero"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sales.zero"}, {"input": "s1.gambling_winnings"}], "test": "lt"}, "then": {"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}
```

Second transcription's note: Supported case is gambling losses limited to gambling winnings; other line 16 items are refused.

Ruling: open

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
| sa.itemizes | gift.special, sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | gift.special |
| sa.deduction | gift.special, sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | gift.special |
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
| 12 | gift.special, sa.charity_limited | gift.special |
| 14 | gift.special, sa.charity_limited | gift.special |
| 17 | gift.special, sa.charity_limited, sa.excluded_income, sa.unsupported | gift.special |

## Raw second transcription

```yaml
lines:
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: copy, from: sa.agi}
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
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.h_salt_cap]}
    refuses: [sa.excluded_income]
    note: "Computes the State and Local Tax Deduction Worksheet for supported cases, including the 30% reduction above the threshold."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "Supported case has no other taxes; foreign tax and generation-skipping tax deductions are refused via sa.unsupported."
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098. See instructions if limited. If paid to the person from whom you bought the home, see instructions and show that person’s name, identifying no., and address"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "No input is provided for mortgage interest not reported on Form 1098; supported case is zero."
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098. See instructions for special rules"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "No input is provided for points not reported on Form 1098; supported case is zero."
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.charity_limited]
    note: "Carryovers are outside the supported charitable-contribution case."
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form. See instructions"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "Casualty and theft losses are refused via sa.unsupported; supported case is zero."
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "Supported case is gambling losses limited to gambling winnings; other line 16 items are refused."
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
    label: "Investment interest. Attach Form 4952 if required. See instructions"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line8}
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
    refuses: [sa.charity_limited, gift.special]
    note: "Aggregates supported noncash gifts from the Form 8283 collection; income-limited or carried-over gifts and appraisal/special-treatment gifts are refused."
  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}

  - id: sa.agi
    printed: "(helper)"
    label: "Adjusted gross income from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.h_taxpayer_age65_count
    printed: "(helper)"
    label: "Count of taxpayer age-65 boxes"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, all: [{op: test, eq: [person.role, {const: "taxpayer"}]}, {op: test, eq: [person.age65, {const: true}]}]}}
  - id: sa.age65
    printed: "(helper)"
    label: "Taxpayer is age 65 or older"
    type: Bool
    expr: {op: test, gt: [sa.h_taxpayer_age65_count, {const: 0}]}
    note: "Chosen reading: the taxpayer's own age-65 box, not the spouse's."
  - id: sa.h_taxpayer_blind_count
    printed: "(helper)"
    label: "Count of taxpayer blindness boxes"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, all: [{op: test, eq: [person.role, {const: "taxpayer"}]}, {op: test, eq: [person.blind, {const: true}]}]}}
  - id: sa.h_spouse_allowed
    printed: "(helper)"
    label: "Spouse age or blindness boxes may be claimed"
    type: Bool
    expr: {op: test, any: [{op: test, ne: [f1040.status, {const: "mfs"}]}, {op: test, eq: [sa.spouse_extra, {const: true}]}]}
  - id: sa.h_zero_count
    printed: "(helper)"
    label: "Zero count"
    type: Count
    expr: {op: param, ref: hsa.no_months}
  - id: sa.h_spouse_age65_figured
    printed: "(helper)"
    label: "Count of spouse age-65 boxes before the MFS allowance"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, all: [{op: test, eq: [person.role, {const: "spouse"}]}, {op: test, eq: [person.age65, {const: true}]}]}}
  - id: sa.h_spouse_age65_count
    printed: "(helper)"
    label: "Count of spouse age-65 boxes allowed"
    type: Count
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [sa.h_spouse_allowed, {const: true}]}, then: sa.h_spouse_age65_figured}, {guard: {op: test, not: {op: test, eq: [sa.h_spouse_allowed, {const: true}]}}, then: sa.h_zero_count}]}
  - id: sa.h_spouse_blind_figured
    printed: "(helper)"
    label: "Count of spouse blindness boxes before the MFS allowance"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, all: [{op: test, eq: [person.role, {const: "spouse"}]}, {op: test, eq: [person.blind, {const: true}]}]}}
  - id: sa.h_spouse_blind_count
    printed: "(helper)"
    label: "Count of spouse blindness boxes allowed"
    type: Count
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [sa.h_spouse_allowed, {const: true}]}, then: sa.h_spouse_blind_figured}, {guard: {op: test, not: {op: test, eq: [sa.h_spouse_allowed, {const: true}]}}, then: sa.h_zero_count}]}
  - id: sa.h_boxes
    printed: "(helper)"
    label: "Total age and blindness boxes for the standard deduction"
    type: Count
    expr: {op: sum, of: [sa.h_taxpayer_age65_count, sa.h_taxpayer_blind_count, sa.h_spouse_age65_count, sa.h_spouse_blind_count]}
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction base amount"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}
  - id: sa.h_std_extra_unit
    printed: "(helper)"
    label: "Standard deduction extra amount per age or blindness box"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Standard deduction additional amount for age and blindness boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra_unit, count: sa.h_boxes}
  - id: sa.h_std_raw
    printed: "(helper)"
    label: "Standard deduction before the MFS spouse-itemizes exception"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_extra]}
  - id: sa.h_zero_money
    printed: "(helper)"
    label: "Zero dollars"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sa.h_std_final
    printed: "(helper)"
    label: "Standard deduction after the MFS spouse-itemizes exception"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}, then: sa.h_zero_money}, {guard: {op: test, not: {op: test, eq: [sa.spouse_itemizes, {const: true}]}}, then: sa.h_std_raw}]}
  - id: sa.h_itemized_greater
    printed: "(helper)"
    label: "Itemized deductions exceed the standard deduction"
    type: Bool
    expr: {op: test, gt: [sa.line17, sa.h_std_final]}
  - id: sa.itemizes
    printed: "(helper)"
    label: "Taxpayer itemizes deductions"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [sa.h_itemized_greater, {const: true}]}, {op: test, eq: [sa.elect_itemize, {const: true}]}]}
    refuses: [sa.dependent]
    note: "Uses the larger of itemized and standard, or itemized if the election is made; dependent or dual-status standard deduction is refused."
  - id: sa.deduction
    printed: "(helper)"
    label: "Deduction amount: itemized deductions if itemizing, otherwise the standard deduction"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [sa.itemizes, {const: true}]}, then: sa.line17}, {guard: {op: test, not: {op: test, eq: [sa.itemizes, {const: true}]}}, then: sa.h_std_final}]}
    refuses: [sa.dependent]
    note: "Standard deduction for dependents or dual-status aliens is outside this slice, so sa.dependent is refused."
  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet line 1 amount"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
  - id: sa.h_salt_threshold
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet threshold"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
  - id: sa.h_salt_excess
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet excess over threshold"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_threshold}
  - id: sa.h_salt_reduction
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet reduction"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_excess, rate: {param: sa.salt_rate}}
  - id: sa.h_salt_floor_param
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet floor"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt_after
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet amount after reduction, floored at zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_line1, take: sa.h_salt_reduction}
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet line 9 amount before the MFS half"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_after, sa.h_salt_floor_param]}
  - id: sa.h_salt_line9_mfs
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet line 9 amount halved for married filing separately"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
  - id: sa.h_salt_cap
    printed: "(helper)"
    label: "State and Local Tax deduction cap after the worksheet"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [f1040.status, {const: "mfs"}]}, then: sa.h_salt_line9_mfs}, {guard: {op: test, not: {op: test, eq: [f1040.status, {const: "mfs"}]}}, then: sa.h_salt_line9}]}
```
