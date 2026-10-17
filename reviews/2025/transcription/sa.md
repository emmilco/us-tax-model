# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9b9899c4f6120096ee9a91e2411b6be5de6e5a849ce2637ffdbb4130622bd97b |
| printed lines compared | 21 |
| agree / disagree / missing | 18 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The instructions say tax is usually less with the larger of the two. On a tie, I chose the standard deduction; both amounts are equal, so line 12e is unaffected. I treated a spouse who itemizes on a separate return as requiring itemizing. The text provided says only that the standard deduction is zero in that case.

Ruling: scope; project retained. The only difference is the condition for a spouse who itemizes on a separate return: the project requires married-filing-separately status together with the spouse-itemizes answer; the second transcription applies the answer alone. Married filing separately is refused (`s3.married`, spec 2.2), so within scope the two conditions agree, and the other two conditions (the election to itemize, and itemized deductions exceeding the standard deduction with the age and blindness additions) are identical.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
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
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"args": [{"ref": "f1040.line11b"}, {"param": "sa.salt_threshold"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.excluded_income"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.excluded_income"}], "test": "eq"}, {"args": [{"param": "sa.salt_threshold"}, {"ref": "f1040.line11b"}], "test": "lt"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_floor"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_floor"}}], "op": "choose"}], "test": "le"}, "then": {"line": "5d"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_floor"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_floor"}}], "op": "choose"}, {"line": "5d"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}
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
    label: "Zero amount for lines outside the supported scope"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Lines 6, 8b, 8c, 13, 15 and 16 are entered as zero. This is valid only because sa.unsupported (other taxes, casualty/theft losses, other itemized deductions, mortgage interest or points not on Form 1098, sales-tax election) and sa.charity_limited (carryovers or income limits) are screened elsewhere. Neither screen is encoded on these lines."

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
    note: "The text does not say what to do if line 2 is negative or what rounding to use. I chose a plain multiplication with no rounding. A negative line 3 then increases line 4 above line 1. That result is not addressed by the text."

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

  # --- State and Local Tax Deduction limit (line 5e instructions and worksheet) ---
  - id: sa.h_is_mfs
    printed: "(helper)"
    label: "Filing status is married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}

  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "SALT Worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}

  - id: sa.h_salt_base_half
    printed: "(helper)"
    label: "$20,000 (half of $40,000) if married filing separately"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line1, rate: {param: sa.half}}

  - id: sa.h_salt_cap
    printed: "(helper)"
    label: "$40,000 ($20,000 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}, then: sa.h_salt_base_half}
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: false}]}, then: sa.h_salt_line1}

  - id: sa.h_salt_line2
    printed: "(helper)"
    label: "SALT Worksheet line 2: Enter the amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: sa.agi}

  - id: sa.h_salt_line3e
    printed: "(helper)"
    label: "SALT Worksheet line 3e: Add lines 3a through 3d (excluded Puerto Rico income, Form 2555 lines 45 and 50, Form 4563 line 15)"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    note: "Only a Bool (sa.excluded_income) is available, not the amounts for lines 3a through 3d. I entered zero. This is correct only when sa.excluded_income is false. When it is true, the amounts are needed and that case must be screened as unsupported."

  - id: sa.h_salt_line4
    printed: "(helper)"
    label: "SALT Worksheet line 4: Add lines 2 and 3e"
    type: Dollars
    expr: {op: sum, of: [sa.h_salt_line2, sa.h_salt_line3e]}

  - id: sa.h_salt_line5
    printed: "(helper)"
    label: "SALT Worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold, status: f1040.status}

  - id: sa.h_salt_line6
    printed: "(helper)"
    label: "SALT Worksheet line 6: Is line 4 more than line 5? Yes. Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_line4, take: sa.h_salt_line5}
    note: "On 'No', the worksheet says to skip lines 7 and 8 and enter line 1 on line 9. A floor at zero gives the same result: line 7 is 0, line 8 equals line 1, and line 9 is the larger of line 1 and $10,000, which is line 1."

  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "SALT Worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line6, rate: {param: sa.salt_rate}}

  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT Worksheet line 8: Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_salt_line1, take: sa.h_salt_line7}

  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT Worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}

  - id: sa.h_salt_line9_half
    printed: "(helper)"
    label: "Half the amount on line 9"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
    note: "The text does not say how to round the halved amount. I applied no rounding."

  - id: sa.h_salt_line9_adj
    printed: "(helper)"
    label: "Amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}, then: sa.h_salt_line9_half}
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: false}]}, then: sa.h_salt_line9}

  - id: sa.h_salt_floor_half
    printed: "(helper)"
    label: "$5,000 (half of $10,000) if married filing separately"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_floor, rate: {param: sa.half}}

  - id: sa.h_salt_small_limit
    printed: "(helper)"
    label: "$10,000 ($5,000 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: true}]}, then: sa.h_salt_floor_half}
        - {guard: {op: test, eq: [sa.h_is_mfs, {const: false}]}, then: sa.h_salt_floor}

  - id: sa.h_salt_small
    printed: "(helper)"
    label: "Before you begin / line 1: Schedule A, line 5d is $10,000 ($5,000 if married filing separately) or less"
    type: Bool
    expr: {op: test, le: [sa.line5d, sa.h_salt_small_limit]}

  - id: sa.h_salt_ws_limit
    printed: "(helper)"
    label: "Limit from the State and Local Tax Deduction Worksheet (line 10 compares this with line 5d)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_salt_small, {const: true}]}, then: sa.line5d}
        - {guard: {op: test, eq: [sa.h_salt_small, {const: false}]}, then: sa.h_salt_line9_adj}

  - id: sa.h_salt_worksheet
    printed: "(helper)"
    label: "Form 1040 line 11b is more than $500,000 ($250,000 if married filing separately), or you completed Form 2555, Form 4563, or excluded income from Puerto Rico"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.agi, sa.h_salt_line5]}
        - {op: test, eq: [sa.excluded_income, {const: true}]}

  - id: sa.saltlimit
    printed: "(helper)"
    label: "Amount compared with line 5d on line 5e: $40,000 ($20,000 MFS), or the State and Local Tax Deduction Worksheet limit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_salt_worksheet, {const: true}]}, then: sa.h_salt_ws_limit}
        - {guard: {op: test, eq: [sa.h_salt_worksheet, {const: false}]}, then: sa.h_salt_cap}

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
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
    note: "The text does not give a filter for this total. I summed gift.allowed over all gift entries with no filter."

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

  # --- Standard deduction (Form 1040 line 12e instructions) and selection ---
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for filing status: $15,750 single or MFS, $31,500 MFJ or QSS, $23,625 HOH"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base, status: f1040.status}

  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked: $2,000 single or HOH, $1,600 otherwise"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra, status: f1040.status}

  - id: sa.h_std_age
    printed: "(helper)"
    label: "Additional amount for box: You were born before January 2, 1961"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.age65, {const: true}]}, then: sa.h_std_extra}
        - {guard: {op: test, eq: [sa.age65, {const: false}]}, then: sa.zero}

  - id: sa.h_std_blind
    printed: "(helper)"
    label: "Additional amount for box: You are blind"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.blind, {const: true}]}, then: sa.h_std_extra}
        - {guard: {op: test, eq: [sa.blind, {const: false}]}, then: sa.zero}

  - id: sa.h_std_chart
    printed: "(helper)"
    label: "Standard deduction per the chart for people born before January 2, 1961, or blind (base plus amount per box checked)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_age, sa.h_std_blind]}
    note: "Three points are open. First, the chart's amounts equal the base plus a fixed amount per box. I encoded that rather than a table. Second, spouse boxes cannot be counted (one or two) from the Bool sa.spouse_extra, so spouse boxes are not added; sa.spouse_extra true must be screened as unsupported. Third, the Standard Deduction Worksheet for Dependents needs earned income, which is not supplied. Dual-status aliens get zero. The model assumes sa.dependent is false and screened elsewhere; this line does not encode that case."

  - id: sa.h_standard
    printed: "(helper)"
    label: "Standard deduction (zero if spouse itemizes on a separate return, line 12b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}, then: sa.zero}
        - {guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}, then: sa.h_std_chart}

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize if elected (line 18), required (spouse itemizes on separate return), or itemized total exceeds standard deduction"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_standard]}
    note: "The instructions say tax is usually less with the larger of the two. On a tie, I chose the standard deduction; both amounts are equal, so line 12e is unaffected. I treated a spouse who itemizes on a separate return as requiring itemizing. The text provided says only that the standard deduction is zero in that case."

  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions (from Schedule A) for Form 1040 line 12e"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.itemizes, {const: true}]}, then: sa.line17}
        - {guard: {op: test, eq: [sa.itemizes, {const: false}]}, then: sa.h_standard}
```
```
