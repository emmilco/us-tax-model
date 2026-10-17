# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9dfb2f9ca24491bdee1db4ed7116ecb682430822b7430b102713d4b02ded7f7e |
| printed lines compared | 18 |
| agree / disagree / missing | 17 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

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
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"of": [{"const": 0}, {"ref": "f1040.line11b"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"of": [{"const": 0}, {"ref": "f1040.line11b"}], "op": "sum"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second transcription's note: This implements worksheet line 10: the smaller of the line 9 limit (halved if MFS) or Schedule A line 5d. sa.h_salt_limit stands in for the task's sa.saltlimit.

Ruling: equivalent representation; project retained. Both transcriptions compute the State and Local Tax Deduction Worksheet limit (i1040sca p. 7): the $40,000 base reduced by 30% of the excess of modified AGI over $500,000, not below $10,000, halved for married filing separately, then the smaller of that limit and line 5d. Two differences remain, neither affecting the value: the project floors the reduction at zero before the $10,000 floor is applied, which the $10,000 floor makes immaterial; and the second transcription adds a zero excluded-income term to AGI for the worksheet's modified AGI, which the project omits because the excluded-income cases are refused (`sa.excluded_income`, spec 2.2). No change to the data.

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
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
    note: "The task listing says 'Amount from sa.agi', but no line sa.agi is defined in the supplied material. The IRS form says the amount comes from Form 1040 or 1040-SR, line 11b, so this line copies f1040.line11b. Adjusted gross income can be negative, so the type is Dollars."
  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: Dollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}
    note: "The IRS text does not say how to round a fractional cent, so rounding is left to the multiply_rate atom. If line 2 is negative, this product is negative; the form gives no floor here, so none is applied."
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
  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero amount for lines outside the supported scope"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The task names sa.zero, but no line by that id is defined. This helper supplies the zero value from the year parameter sales.zero."
  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "State and Local Tax Deduction Worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
    note: "The worksheet's 'Before you begin' check and its line 1 'No' branch (line 5d is $10,000, or $5,000 if MFS, or less) are not encoded separately. In that case line 9 is at least $10,000 (half is at least $5,000 if MFS), so line 10 already equals line 5d. Likewise, when line 11b is $500,000 or less ($250,000 MFS), the worksheet yields the smaller of line 5d or $40,000 ($20,000 MFS), which matches the instruction on the face of the form. So the worksheet is computed unconditionally."
  - id: sa.h_salt_line2
    printed: "(helper)"
    label: "Worksheet line 2: Enter the amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.h_salt_line3e
    printed: "(helper)"
    label: "Worksheet line 3e: Add lines 3a through 3d (excluded Puerto Rico income, Form 2555 lines 45 and 50, Form 4563 line 15)"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "The supplied inputs include only the Bool sa.excluded_income, not the amounts for lines 3a through 3d. Line 3e is therefore taken as zero, which is valid only when sa.excluded_income is false (the supported scope)."
  - id: sa.h_salt_line4
    printed: "(helper)"
    label: "Worksheet line 4: Add lines 2 and 3e"
    type: Dollars
    expr: {op: sum, of: [sa.h_salt_line2, sa.h_salt_line3e]}
  - id: sa.h_salt_line5
    printed: "(helper)"
    label: "Worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
    note: "This parameter is keyed by filing status (f1040.status)."
  - id: sa.h_salt_line6
    printed: "(helper)"
    label: "Worksheet line 6: Is the amount on line 4 more than the amount on line 5? Yes. Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_line4, take: sa.h_salt_line5}
    note: "On the 'No' branch, lines 7 and 8 are skipped and line 1 goes to line 9. Using a floor at zero here gives line 7 = 0 and line 8 = line 1, which is the same result."
  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "Worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line6, rate: {param: sa.salt_rate}}
  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "Worksheet line 8: Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_salt_line1, take: sa.h_salt_line7}
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "Worksheet line 9 floor: $10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "Worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}
  - id: sa.h_is_mfs
    printed: "(helper)"
    label: "Filing status is married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: sa.h_not_mfs
    printed: "(helper)"
    label: "Filing status is not married filing separately"
    type: Bool
    expr: {op: test, not: sa.h_is_mfs}
  - id: sa.h_salt_half
    printed: "(helper)"
    label: "Worksheet line 10: half the amount on line 9"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
    note: "The IRS text does not say how to round a half cent, so rounding is left to the multiply_rate atom."
  - id: sa.h_salt_limit
    printed: "(helper)"
    label: "Worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: sa.h_is_mfs, then: sa.h_salt_half}
        - {guard: sa.h_not_mfs, then: sa.h_salt_line9}
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.h_salt_limit]}
    note: "This implements worksheet line 10: the smaller of the line 9 limit (halved if MFS) or Schedule A line 5d. sa.h_salt_limit stands in for the task's sa.saltlimit."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.unsupported."
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.unsupported."
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.unsupported."
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.charity_limited."
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.unsupported."
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    note: "This is zero within the supported scope, which is screened by sa.unsupported."
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
    note: "The IRS text does not identify which gift field is the deductible amount. This line sums gift.allowed (described as the amount from gift.deduction) over all Form 8283 groups. Income limits are excluded by the sa.charity_limited screen."
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
```
```
