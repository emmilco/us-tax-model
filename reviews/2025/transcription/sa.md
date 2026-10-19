# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 209600f2e8adaf58d8675ff1301c8ba68017d819d4516801aab6b206d7d8bc8f |
| printed lines compared | 22 |
| agree / disagree / missing | 19 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |

## Lines

### sa.age65 — Were you born before January 2, 1961?
Status: **AGREE**

### sa.agi — Form 1040 line 11b adjusted gross income
Status: **AGREE**

### sa.itemizes — Itemize if elected, required, or itemized total exceeds standard
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Ruling: scope; project retained. The only difference is the condition for a spouse who itemizes on a separate return: the project requires married-filing-separately status together with the spouse-itemizes answer; the second transcription applies the answer alone. Married filing separately is refused (`s3.mfs`, spec 2.2), so within scope the two conditions agree, and the other two conditions (the election to itemize, and itemized deductions exceeding the standard deduction with the age and blindness additions) are identical. Stage 13 re-run: both count the age and blindness boxes of you and, on a joint return, your spouse (i1040gi p. 33, Line 12d).

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: scope; project retained. Both select the itemized total (line 17) when itemizing is elected, when a separate-return spouse itemizes, or when line 17 exceeds the standard deduction, and the standard deduction otherwise, with the standard deduction zero when a separate-return spouse itemizes and increased by the age and blindness additions. As on `sa.itemizes`, the project conditions the spouse-itemizes rule on married-filing-separately status, which the second transcription omits; married filing separately is refused (`s3.mfs`, spec 2.2), so within scope the selections agree (i1040gi pp. 34–35, line 12e and the Standard Deduction Chart). Stage 13 re-run: both count the age and blindness boxes of you and, on a joint return, your spouse (i1040gi p. 33, Line 12d).

### 2 — Amount from sa.agi
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
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second transcription's note: The State and Local Tax Deduction Worksheet is written as a cap (sa.saltlimit). The cap is never less than $10,000 ($5,000 MFS), so the 'line 5d is $10,000 or less' shortcut and worksheet line 10 both come out the same as the smaller of line 5d and the cap. Worksheet lines 3a-3d (excluded income) are refused, so worksheet line 4 equals line 11b.

Ruling: equivalent representation; project retained. The second transcription applies the State and Local Tax Deduction Worksheet only when modified AGI exceeds $500,000 or income was excluded, and otherwise takes the $40,000 base directly; the project computes the worksheet unconditionally, where the reduction is zero at or below the threshold and the excluded-income case is refused (`sa.excluded_income`). Same value within scope (i1040sca p. 7).

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

### 16 — Amount from sa.zero
Status: **AGREE**

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
```yaml
lines:
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: sa.agi}
  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: Dollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}
  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.line1, take: sa.line3}
    note: "Open: the text does not say what to do when line 2 (AGI) is negative, which makes line 3 negative. Chosen: follow the printed arithmetic. Line 1 minus line 3, with a floor at zero."
  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5a, sa.line5b, sa.line5c]}
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.saltlimit]}
    refuses: [sa.excluded_income]
    note: "The State and Local Tax Deduction Worksheet is written as a cap (sa.saltlimit). The cap is never less than $10,000 ($5,000 MFS), so the 'line 5d is $10,000 or less' shortcut and worksheet line 10 both come out the same as the smaller of line 5d and the cap. Worksheet lines 3a-3d (excluded income) are refused, so worksheet line 4 equals line 11b."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.charity_limited]
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
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

  # ---- helpers ----
  - id: sa.zero
    printed: "(helper)"
    label: "Year parameter sales.zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Lines 6, 8b, 8c, 13, 15 and 16 refer to this id, but it was not among the given inputs, so it is defined here."
  - id: sa.agi
    printed: "(helper)"
    label: "Form 1040 line 11b adjusted gross income"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.h_taxpayer_age65_count
    printed: "(helper)"
    label: "Your entry, if you were born before January 2, 1961"
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
    label: "Were you born before January 2, 1961?"
    type: Bool
    expr: {op: test, gt: [sa.h_taxpayer_age65_count, {const: 0}]}
    note: "Taken from the taxpayer's person entry rather than asked again, so the two answers cannot disagree."
  # State and Local Tax Deduction Worksheet
  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "SALT Worksheet line 1. Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
  - id: sa.h_salt_line5
    printed: "(helper)"
    label: "SALT Worksheet line 5. Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
  - id: sa.h_salt_line6
    printed: "(helper)"
    label: "SALT Worksheet line 6. Is the amount on line 4 more than the amount on line 5? Yes. Subtract line 5 from line 4 (No: skip lines 7 and 8)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_line5}
    note: "Worksheet line 4 is line 2 plus line 3e. Line 3e is refused, so line 4 is AGI. In the 'No' case, a zero here makes line 9 the larger of $40,000 and $10,000, which is line 1, as the 'No' branch says."
  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "SALT Worksheet line 7. Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line6, rate: {param: sa.salt_rate}}
  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT Worksheet line 8. Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_salt_line1, take: sa.h_salt_line7}
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT Worksheet line 9 amount, $10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT Worksheet line 9. Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}
  - id: sa.h_salt_half
    printed: "(helper)"
    label: "SALT Worksheet line 10. Half the amount on line 9 if married filing separately"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
  - id: sa.h_is_mfs
    printed: "(helper)"
    label: "Married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: sa.saltlimit
    printed: "(helper)"
    label: "SALT Worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}
          then: sa.h_salt_half
        - guard: {op: test, eq: [sa.h_is_mfs, {const: false}]}
          then: sa.h_salt_line9
    refuses: [sa.excluded_income]
  # Standard deduction (Form 1040 line 12e instructions)
  - id: sa.h_age_boxes
    printed: "(helper)"
    label: "Boxes checked: You were born before January 2, 1961; Spouse was born before January 2, 1961"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.age65, {const: true}]}
          - op: test
            not:
              op: test
              all:
                - {op: test, eq: [person.role, {const: "spouse"}]}
                - {op: test, eq: [person.died_before_65, {const: true}]}
    note: "The text says not to check the spouse box when the spouse died in 2025 before reaching 65. That rule is encoded. For a taxpayer who died in 2025, the text only says 'see Pub. 501', which is not provided, so nothing is encoded for that case. Spouse entries exist only on a joint return, and checking spouse boxes on an MFS return is refused through sa.spouse_extra."
  - id: sa.h_blind_boxes
    printed: "(helper)"
    label: "Boxes checked: You are blind; Spouse is blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.blind, {const: true}]}
  - id: sa.h_boxes
    printed: "(helper)"
    label: "Enter the total number of boxes checked"
    type: Count
    expr: {op: sum, of: [sa.h_age_boxes, sa.h_blind_boxes]}
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for your filing status: Single or married filing separately—$15,750; Married filing jointly—$31,500; Head of household—$23,625"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}
  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked: $1,600 ($2,000 if single or head of household)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
  - id: sa.h_std_additional
    printed: "(helper)"
    label: "Multiply the number of boxes checked by $1,600 ($2,000 if single or head of household)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_boxes}
  - id: sa.h_standard
    printed: "(helper)"
    label: "Standard deduction (amounts to the left of line 12e, or the Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_additional]}
    refuses: [sa.dependent, sa.spouse_extra, sa.unsupported]
    note: "Every chart amount equals the filing-status base plus the per-box amount times the number of boxes. For example, single with 2 boxes: $15,750 + 2 × $2,000 = $19,750. MFS with 4 boxes: $15,750 + 4 × $1,600 = $22,150. The dependent worksheet, dual-status aliens (Exception 3), and the disaster-loss increase (Exception 5) are refused."
  - id: sa.h_standard_allowed
    printed: "(helper)"
    label: "Exception 2—Spouse itemizes on a separate return. If you checked the box on line 12b, your standard deduction is zero"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_standard
  - id: sa.h_itemized_larger
    printed: "(helper)"
    label: "Total itemized deductions are more than the standard deduction"
    type: Bool
    expr: {op: test, gt: [sa.line17, sa.h_standard_allowed]}
    note: "Open: the text says to take the larger of the two but does not say what to do when they are equal. Chosen: on a tie, take the standard deduction unless the line 18 election is checked. The amount is the same either way."
  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize if elected (line 18), required (spouse itemizes on a separate return), or itemized total exceeds standard"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, eq: [sa.h_itemized_larger, {const: true}]}
  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions (from Schedule A), Form 1040 line 12e"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_standard_allowed
```
```
