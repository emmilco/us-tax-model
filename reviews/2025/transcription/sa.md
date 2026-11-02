# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 05207ae10d6b53be05f8a3f4cc4756f2c59a442edeaad971454e6d805079a695 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | d19ac55850f1d8ef60a44b84476defa0db233b903176f18c1991c4688f0f7c68 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 020691577e6a177170e9b20d041662f1cabe6c2c88cf306ab0c7a09a508e07cf |
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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second transcription's note: The interface name does not fix its meaning. Read as: at least one 'born before January 2, 1961' box on line 12d is checked (you or your spouse). Blindness boxes are excluded.

Ruling: model error — i1040gi p. 33, line 12d, checks the box for you and, on a joint return, a separate box for your spouse; sa.age65 is the taxpayer-only box that Schedule 1-A line 36a reads. The candidate counts every person entry with age65, so it counts the spouse twice or on a return where the box is the filer's. Triage: 2480 comparisons; 43 completed-return value differences.

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: When itemized deductions equal the standard deduction, the standard deduction is chosen unless the line 18 election is made.

Ruling: representation — the candidate's itemize test is the project's with the married-filing-separately condition on sa.spouse_itemizes dropped; the input is asked only for MFS, so the two are equal on every reachable return, and the election and line-17 comparison are the same (i1040gi p. 34, line 12e). Triage: 2480 comparisons, no completed-return value difference.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: representation — the line inherits the sa.itemizes equivalence above; the standard-or-itemized selection and both amounts agree on reachable returns. Triage: 2480 comparisons, no completed-return value difference.

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

Second transcription's note: Only gambling losses are supported, limited to the gambling winnings on Schedule 1, line 8b. Every other item on the list, including a net qualified disaster loss, is screened by sa.unsupported.

Ruling: interface gap — the candidate's smaller_of needs sa.gambling_losses on every return; the project asks it only when s1.gambling_winnings is positive (amb.2025.gambling_losses) and enters zero otherwise (i1040sca p. 11, Other Itemized Deductions, gambling losses only to the extent of gambling winnings). The amount agrees when the losses are supplied. Triage: 2480 comparisons; 1277 candidate-unknown, no completed-return value difference.

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
| sa.age65 | sa.spouse_extra | sa.spouse_extra |
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
| 14 | sa.charity_limited | - |
| 17 | sa.charity_limited, sa.excluded_income, sa.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.agi
    printed: "(helper)"
    label: "Adjusted gross income: amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}

  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line11b, take: {const: 0}}
    note: "The schedule says to enter line 11b, but the required type is NonNegDollars. A negative AGI is therefore entered as zero. Line 3 then becomes zero instead of negative, so line 4 can never be more than line 1."

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
    note: "The sales-tax election on line 5a is outside this slice. It is refused here because line 5a is a supplied input."

  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "SALT Worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}

  - id: sa.h_salt_line5
    printed: "(helper)"
    label: "SALT Worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}

  - id: sa.h_salt_line6
    printed: "(helper)"
    label: "SALT Worksheet line 6: Subtract line 5 from line 4 (line 4 = line 11b plus excluded income)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_line5}
    refuses: [sa.excluded_income]
    note: "Worksheet lines 3a-3d (excluded Puerto Rico, Form 2555 and Form 4563 income) are refused, so line 4 equals line 11b. When line 4 is not more than line 5 the worksheet skips lines 7 and 8 and uses line 1 on line 9. Flooring line 6 at zero gives that same result."

  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "SALT Worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line6, rate: {param: sa.salt_rate}}

  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT Worksheet line 8: Subtract line 7 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_line1, take: sa.h_salt_line7}
    note: "Floored at zero to keep the type nonnegative. Line 9 takes the larger of this and $10,000, so the floor never changes the result."

  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT Worksheet line 9 amount: $10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT Worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}

  - id: sa.h_salt_line9_half
    printed: "(helper)"
    label: "SALT Worksheet line 10: half the amount on line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}

  - id: sa.h_salt_limit
    printed: "(helper)"
    label: "SALT Worksheet line 10: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9_half
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.h_salt_limit, sa.line5d]}
    refuses: [sa.excluded_income]
    note: "The State and Local Tax Deduction Worksheet is applied in every case. At or below the AGI threshold it gives the smaller of line 5d or $40,000 ($20,000 MFS), as the line instruction does. The before-you-begin and line 1 'No' shortcuts (line 5d of $10,000, or $5,000 MFS, or less) give the same result, because line 9 is at least $10,000."

  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "Foreign income taxes and generation-skipping tax are screened by sa.unsupported. The supported case has no other taxes."

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
    note: "Only gambling losses are supported, limited to the gambling winnings on Schedule 1, line 8b. Every other item on the list, including a net qualified disaster loss, is screened by sa.unsupported."

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
    note: "Read as the deductible investment interest expense figured on Form 4952, line 8 (catalog line). This assumes that line is zero when there is no investment interest."

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

  - id: sa.h_boxes_age
    printed: "(helper)"
    label: "Line 12d boxes checked for born before January 2, 1961 (not for a person who died in 2025 before reaching age 65)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.died_before_65, {const: false}]}
    refuses: [sa.spouse_extra]
    note: "Counts the people in the person collection. Spouse boxes on a married-filing-separately return (sa.spouse_extra) are refused, because the number of such boxes is not supplied."

  - id: sa.h_boxes_blind
    printed: "(helper)"
    label: "Line 12d boxes checked for blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.blind, {const: true}]}
    refuses: [sa.spouse_extra]

  - id: sa.age65
    printed: "(helper)"
    label: "A box on line 12d is checked for born before January 2, 1961"
    type: Bool
    expr: {op: test, gt: [sa.h_boxes_age, {const: 0, type: Count}]}
    note: "The interface name does not fix its meaning. Read as: at least one 'born before January 2, 1961' box on line 12d is checked (you or your spouse). Blindness boxes are excluded."

  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for filing status (amounts to the left of line 12e)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}

  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked on line 12d (Standard Deduction Chart)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}

  - id: sa.h_std_extra_age
    printed: "(helper)"
    label: "Additional standard deduction for age boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_boxes_age}

  - id: sa.h_std_extra_blind
    printed: "(helper)"
    label: "Additional standard deduction for blindness boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_boxes_blind}

  - id: sa.h_std_full
    printed: "(helper)"
    label: "Standard deduction (Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind, or line 12e amount)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_extra_age, sa.h_std_extra_blind]}
    refuses: [sa.dependent, sa.spouse_extra]
    note: "The chart amounts equal the base amount plus $2,000 (single or HOH) or $1,600 (others) per box checked. The Standard Deduction Worksheet for Dependents and dual-status aliens are refused through sa.dependent."

  - id: sa.h_std
    printed: "(helper)"
    label: "Standard deduction (zero if married filing separately and spouse itemizes)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_std_full

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize deductions on Schedule A (larger than standard deduction, spouse itemizes on separate return, or election on line 18)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_std]}
    note: "When itemized deductions equal the standard deduction, the standard deduction is chosen unless the line 18 election is made."

  - id: sa.deduction
    printed: "(helper)"
    label: "Form 1040, line 12e: standard deduction or itemized deductions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_std
```
```
