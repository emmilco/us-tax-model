# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c9161516f4026cdc261f6d8c623a8d6b8d72a2a92eb43f79cbf8b75e9a3026ee |
| printed lines compared | 21 |
| agree / disagree / missing | 18 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sa.agi — Form 1040 line 11b adjusted gross income
Status: **AGREE**

### sa.itemizes — Itemize if elected, required, or itemized total exceeds standard
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sa.dependent"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"param": "sa.standard_extra"}, {"param": "sa.standard_extra"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The text says 'take the larger'. When the two are equal I choose the standard deduction. Counting sa.dependent as 'required' is my choice: the text gives a zero standard deduction for dual-status aliens and a worksheet this model cannot compute for dependents.

Ruling: scope; project retained. The only difference is the condition for a spouse who itemizes on a separate return: the project requires married-filing-separately status together with the spouse-itemizes answer; the second transcription applies the answer alone. Married filing separately is refused (`s3.married`, spec 2.2), so within scope the two conditions agree, and the other two conditions (the election to itemize, and itemized deductions exceeding the standard deduction with the age and blindness additions) are identical.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"param": "sa.standard_extra"}, {"param": "sa.standard_extra"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.dependent"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"param": "sa.standard_extra"}, {"param": "sa.standard_extra"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.dependent"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"param": "sa.standard_extra"}, {"param": "sa.standard_extra"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: scope; project retained. Both select the itemized total (line 17) when itemizing is elected, when a separate-return spouse itemizes, or when line 17 exceeds the standard deduction, and the standard deduction otherwise, with the standard deduction zero when a separate-return spouse itemizes and increased by the age and blindness additions. As on `sa.itemizes`, the project conditions the spouse-itemizes rule on married-filing-separately status, which the second transcription omits; married filing separately is refused (`s3.married`, spec 2.2), so within scope the selections agree (i1040gi pp. 34–35, line 12e and the Standard Deduction Chart).

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
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.excluded_income"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.excluded_income"}], "test": "eq"}, "then": {"of": [{"input": "sa.h_ws3a"}, {"input": "sa.h_ws3b"}, {"input": "sa.h_ws3c"}, {"input": "sa.h_ws3d"}], "op": "sum"}}], "op": "choose"}, {"ref": "f1040.line11b"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.excluded_income"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.excluded_income"}], "test": "eq"}, "then": {"of": [{"input": "sa.h_ws3a"}, {"input": "sa.h_ws3b"}, {"input": "sa.h_ws3c"}, {"input": "sa.h_ws3d"}], "op": "sum"}}], "op": "choose"}, {"ref": "f1040.line11b"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

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

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.agi
    printed: "(helper)"
    label: "Form 1040 line 11b adjusted gross income"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}

  - id: sa.zero
    printed: "(helper)"
    label: "No amount on a line outside the supported scope"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The text does not say how unsupported items are excluded. I read the zero lines (6, 8b, 8c, 13, 15, 16) as valid only when sa.unsupported is false and sa.charity_limited is false. The model has no refusal atom, so those screens must be enforced outside this form."

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
    note: "The text gives no rounding rule and does not cover a negative line 2. I take the product as is, and it may be negative."

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

  - id: sa.h_ws1
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
    note: "The worksheet's 'Before you begin' check and line 1 'No' branch (line 5d of $10,000, or $5,000 if MFS, or less) say to enter line 5d on line 5e. Running the full worksheet always gives the same result, because line 9 is at least $10,000 (halved for MFS) and line 10 takes the smaller of that and line 5d. So the branch is not encoded separately."

  - id: sa.h_ws2
    printed: "(helper)"
    label: "Worksheet line 2: Enter the amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: sa.agi}

  - id: sa.h_ws3a
    printed: "(helper)"
    label: "Worksheet line 3a: Enter any income from Puerto Rico that you excluded"
    type: NonNegDollars
    expr: {op: input, source: "Excluded Puerto Rico income (SALT worksheet line 3a)"}

  - id: sa.h_ws3b
    printed: "(helper)"
    label: "Worksheet line 3b: Enter the amount from Form 2555, line 45"
    type: NonNegDollars
    expr: {op: input, source: "Form 2555, line 45"}

  - id: sa.h_ws3c
    printed: "(helper)"
    label: "Worksheet line 3c: Enter the amount from Form 2555, line 50"
    type: NonNegDollars
    expr: {op: input, source: "Form 2555, line 50"}

  - id: sa.h_ws3d
    printed: "(helper)"
    label: "Worksheet line 3d: Enter the amount from Form 4563, line 15"
    type: NonNegDollars
    expr: {op: input, source: "Form 4563, line 15"}

  - id: sa.h_ws3e_entered
    printed: "(helper)"
    label: "Add lines 3a through 3d (as entered)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_ws3a, sa.h_ws3b, sa.h_ws3c, sa.h_ws3d]}

  - id: sa.h_ws3e
    printed: "(helper)"
    label: "Worksheet line 3e: Add lines 3a through 3d"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.excluded_income, {const: true}]}
          then: sa.h_ws3e_entered
        - guard: {op: test, eq: [sa.excluded_income, {const: false}]}
          then: sa.zero
    note: "The existing gate sa.excluded_income decides whether the amounts on lines 3a to 3d count. When it is false, line 3e is zero."

  - id: sa.h_ws4
    printed: "(helper)"
    label: "Worksheet line 4: Add lines 2 and 3e"
    type: Dollars
    expr: {op: sum, of: [sa.h_ws2, sa.h_ws3e]}

  - id: sa.h_ws5
    printed: "(helper)"
    label: "Worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
    note: "Keyed by filing status (f1040.status)."

  - id: sa.h_ws6
    printed: "(helper)"
    label: "Worksheet line 6: Is line 4 more than line 5? Yes. Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_ws4, take: sa.h_ws5}
    note: "On the 'No' branch the worksheet skips lines 7 and 8 and puts line 1 on line 9. Here that branch is a zero line 6, which makes line 7 zero and line 8 equal to line 1, so line 9 comes out the same."

  - id: sa.h_ws7
    printed: "(helper)"
    label: "Worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_ws6, rate: {param: sa.salt_rate}}
    note: "The text gives no rounding rule for this product."

  - id: sa.h_ws8
    printed: "(helper)"
    label: "Worksheet line 8: Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_ws1, take: sa.h_ws7}

  - id: sa.h_ws9_floor
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_ws9
    printed: "(helper)"
    label: "Worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_ws8, sa.h_ws9_floor]}

  - id: sa.h_ws9_half
    printed: "(helper)"
    label: "Half the amount on line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_ws9, rate: {param: sa.half}}
    note: "The text gives no rounding rule for halving."

  - id: sa.h_is_mfs
    printed: "(helper)"
    label: "Filing status is married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}

  - id: sa.saltlimit
    printed: "(helper)"
    label: "Worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}
          then: sa.h_ws9_half
        - guard: {op: test, eq: [sa.h_is_mfs, {const: false}]}
          then: sa.h_ws9
    note: "The form's direct rule (when AGI is at or below $500,000/$250,000 and there are no exclusions, use the smaller of 5d or $40,000/$20,000) gives the same result as this worksheet, so the worksheet is used for every case."

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately); see instructions if line 11b is more than $500,000 ($250,000 MFS) or Form 2555/4563/Puerto Rico exclusion"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.saltlimit]}

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses)"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}

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
    label: "Other than by cash or check. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}
    note: "Assumes no income-limit reduction applies, which means sa.charity_limited is false."

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

  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for filing status (amounts listed to the left of line 12e)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}

  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked on line 12d"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
    note: "Not printed as a separate amount. It is taken from the Standard Deduction Chart: each step equals the chart amount minus the base ($2,000 for single/HOH, $1,600 otherwise)."

  - id: sa.h_std_extra2
    printed: "(helper)"
    label: "Additional amount for two boxes checked"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_extra, sa.h_std_extra]}

  - id: sa.h_std_add
    printed: "(helper)"
    label: "Chart addition for the number of boxes checked (you born before January 2, 1961; you are blind)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [sa.age65, {const: true}]}, {op: test, eq: [sa.blind, {const: true}]}]}
          then: sa.h_std_extra2
        - guard: {op: test, all: [{op: test, eq: [sa.age65, {const: true}]}, {op: test, eq: [sa.blind, {const: false}]}]}
          then: sa.h_std_extra
        - guard: {op: test, all: [{op: test, eq: [sa.age65, {const: false}]}, {op: test, eq: [sa.blind, {const: true}]}]}
          then: sa.h_std_extra
        - guard: {op: test, all: [{op: test, eq: [sa.age65, {const: false}]}, {op: test, eq: [sa.blind, {const: false}]}]}
          then: sa.zero
    note: "Spouse boxes are not modelled. sa.spouse_extra is a single Bool, so it cannot say whether one or two spouse boxes apply, and the chart needs that count. I chose to require sa.spouse_extra to be false, enforced outside this form."

  - id: sa.h_std_amount
    printed: "(helper)"
    label: "Standard deduction from the line 12e amounts or the chart for people born before January 2, 1961, or blind"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_add]}

  - id: sa.h_standard
    printed: "(helper)"
    label: "Standard deduction (zero if spouse itemizes on a separate return)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_std_amount
    note: "Exception 2: if the line 12b box is checked, the standard deduction is zero. The Dependents worksheet (Exception 1) needs earned income, which is not an input here, and dual-status aliens (Exception 3) get zero. Because sa.dependent combines both cases, I treat it as forcing itemization in sa.itemizes instead of computing a standard amount. Exception 5 (net qualified disaster loss) is out of scope because line 15/16 items are screened out."

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize if elected (line 18), required, or itemized total exceeds standard deduction"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, eq: [sa.dependent, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_standard]}
    note: "The text says 'take the larger'. When the two are equal I choose the standard deduction. Counting sa.dependent as 'required' is my choice: the text gives a zero standard deduction for dual-status aliens and a worksheet this model cannot compute for dependents."

  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions for Form 1040 line 12e"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_standard
```
```
