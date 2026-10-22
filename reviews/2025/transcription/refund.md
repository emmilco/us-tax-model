# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f68394f3e91afc533ce947e6a16e6f079a5eafae8c50959edc2cd36753369965 |
| subject sha256 | 19b64f2343c301d334f12697341c4e987cb0338554757fa20f2d9aea79795acc |
| printed lines compared | 11 |
| agree / disagree / missing | 8 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 33, 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 24 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### refund.has — Any state or local income tax refund received in 2025
Status: **AGREE**

### refund.taxable — Taxable part of your refund (zero when you did not itemize for 2024 or deducted general sa
Status: **AGREE**

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **AGREE**

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **AGREE**

### 3 — Subtract line 2 from line 1
Status: **AGREE**

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **AGREE**

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **AGREE**

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"amount": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}, "count": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}], "test": "all"}, "then": {"const": 1}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}], "test": "all"}, "then": {"const": 1}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 1}}], "op": "choose"}], "op": "sum"}, "op": "multiply_count"}
```

Ruling: owner's reading; project retained. The only difference is a 2024 status of qualifying surviving spouse: the project counts the two spouse boxes only for married filing jointly or separately, the second also for qualifying surviving spouse. The worksheet does not say which statuses carry spouse boxes (i1040gi p. 90, State and Local Income Tax Refund Worksheet, line 6, "Check any boxes that apply"); the register's binding reading amb.2025.refund_boxes_2024 takes them from the standard deduction rules (p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return)"), under which a qualifying surviving spouse return has no spouse whose boxes it checks. Everywhere else the two agree: each box adds $1,550, or $1,950 for single or head of household, and the sum of per-box amounts equals the count times the amount.

### 7 — Add lines 5 and 6
Status: **AGREE**

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and 
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}, {"guard": {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}, {"guard": {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"line": "4"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}], "test": "all"}, "then": {"line": "4"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "ne"}], "test": "any"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}], "op": "choose"}
```

Ruling: equivalent; project retained. Both give line 4 when the 2024 status was married filing separately and the spouse itemized, and line 4 less line 7 (not below zero) otherwise (i1040gi p. 90, State and Local Income Tax Refund Worksheet, Note, "skip lines 5 through 7, enter the amount from line 4 on line 8", and line 8, "Yes. Subtract line 7 from line 4"; the No branch, "STOP None of your refund is taxable", is the zero floor). The project splits by each filing status first, which the comparison does not merge.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "2"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "2"}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}
```

Ruling: equivalent; project retained. The project writes the line 3 STOP explicitly (zero when line 1 is not more than line 2), the second leaves it to line 3's zero floor; when line 1 is not more than line 2, line 3 is zero and the smaller of lines 3 and 8 is zero too, so the two agree on every input (i1040gi p. 90, State and Local Income Tax Refund Worksheet, line 3, "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable", and line 9, "Enter the smaller of line 3 or line 8").

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.taxable | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024, refund.other | refund.other |
| 1 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024, refund.other | refund.box8, refund.not_2024, refund.other |
| 3 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024, refund.other | refund.box8, refund.not_2024, refund.other |
| 9 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024, refund.other | refund.box8, refund.not_2024, refund.other |

## Raw second transcription

```yaml
```yaml
lines:
  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.received, refund.line5d_2024]}
    refuses: [refund.other, refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "Open: the cap is 'the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d'. Line 5d is the total of income or sales taxes, real estate taxes and personal property taxes, so the cap could mean only the income-tax part (line 5a). Chosen: cap at the line 5d input, since the text names line 5d and no line 5a input exists. Exception 4 (refund more than the income tax deduction minus the sales tax alternative) is covered by the refund.exc_tax screen and is not computed here."
  - id: refund.line2
    printed: "2"
    label: "Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line5d_2024, take: refund.line5e_2024}
    note: "Open: the line asks 'Is [taxes paid] more than line 5e? No: enter line 1 on line 3'. Chosen: line 2 is zero in the No case, so line 3 equals line 1. Taxes paid in 2024 are taken as the 2024 Schedule A line 5d amount ('generally' that amount)."
  - id: refund.line3
    printed: "3"
    label: "Subtract line 2 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line1, take: refund.line2}
    note: "If line 1 is not more than line 2, the worksheet says STOP, none of the refund is taxable. Chosen: encoded as zero."
  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17"
    type: NonNegDollars
    expr: {op: copy, from: refund.line17_2024}
  - id: refund.h_std_single
    printed: "(helper)"
    label: "$14,600 (single or married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_single}
  - id: refund.h_std_joint
    printed: "(helper)"
    label: "$29,200 (married filing jointly or qualifying surviving spouse)"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_joint}
  - id: refund.h_std_hoh
    printed: "(helper)"
    label: "$21,900 (head of household)"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_hoh}
  - id: refund.line5
    printed: "5"
    label: "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR. Single or married filing separately—$14,600. Married filing jointly or qualifying surviving spouse—$29,200. Head of household—$21,900"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [refund.status, {const: "single"}]}, {op: test, eq: [refund.status, {const: "mfs"}]}]}
          then: refund.h_std_single
        - guard: {op: test, any: [{op: test, eq: [refund.status, {const: "mfj"}]}, {op: test, eq: [refund.status, {const: "qss"}]}]}
          then: refund.h_std_joint
        - guard: {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_std_hoh
  - id: refund.h_one
    printed: "(helper)"
    label: "One box checked"
    type: Count
    expr: {op: param, ref: ss.one}
  - id: refund.h_none
    printed: "(helper)"
    label: "Box not checked"
    type: Count
    expr: {op: param, ref: ss.zero}
  - id: refund.h_has_spouse
    printed: "(helper)"
    label: "2024 filing status allows boxes for a spouse (married filing jointly, qualifying surviving spouse, or married filing separately)"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [refund.status, {const: "mfj"}]}, {op: test, eq: [refund.status, {const: "qss"}]}, {op: test, eq: [refund.status, {const: "mfs"}]}]}
    note: "Open: the worksheet does not say which statuses may check the spouse boxes. Chosen: married statuses and qualifying surviving spouse. Single and head of household are excluded, following the Form 1040 line 12d rule ('Don’t check any boxes for your spouse if your filing status is head of household'). The married-filing-separately conditions are carried by the spouse inputs."
  - id: refund.h_c_you_born
    printed: "(helper)"
    label: "You were born before January 2, 1960 (box)"
    type: Count
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [refund.you_born, {const: true}]}, then: refund.h_one}
        - {guard: {op: test, eq: [refund.you_born, {const: false}]}, then: refund.h_none}
  - id: refund.h_c_you_blind
    printed: "(helper)"
    label: "You are blind (box)"
    type: Count
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [refund.you_blind, {const: true}]}, then: refund.h_one}
        - {guard: {op: test, eq: [refund.you_blind, {const: false}]}, then: refund.h_none}
  - id: refund.h_c_spouse_born
    printed: "(helper)"
    label: "Spouse was born before January 2, 1960 (box)"
    type: Count
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [refund.spouse_born, {const: true}]}, {op: test, eq: [refund.h_has_spouse, {const: true}]}]}
          then: refund.h_one
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [refund.spouse_born, {const: true}]}, {op: test, eq: [refund.h_has_spouse, {const: true}]}]}}
          then: refund.h_none
  - id: refund.h_c_spouse_blind
    printed: "(helper)"
    label: "Spouse is blind (box)"
    type: Count
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [refund.spouse_blind, {const: true}]}, {op: test, eq: [refund.h_has_spouse, {const: true}]}]}
          then: refund.h_one
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [refund.spouse_blind, {const: true}]}, {op: test, eq: [refund.h_has_spouse, {const: true}]}]}}
          then: refund.h_none
  - id: refund.h_boxes
    printed: "(helper)"
    label: "Number of boxes checked"
    type: Count
    expr: {op: sum, of: [refund.h_c_you_born, refund.h_c_you_blind, refund.h_c_spouse_born, refund.h_c_spouse_blind]}
  - id: refund.h_box_unmarried
    printed: "(helper)"
    label: "$1,950 (2024 filing status single or head of household)"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_unmarried}
  - id: refund.h_box_married
    printed: "(helper)"
    label: "$1,550"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_married}
  - id: refund.h_box_amount
    printed: "(helper)"
    label: "Amount per box: $1,550 ($1,950 if your 2024 filing status was single or head of household)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [refund.status, {const: "single"}]}, {op: test, eq: [refund.status, {const: "hoh"}]}]}
          then: refund.h_box_unmarried
        - guard: {op: test, not: {op: test, any: [{op: test, eq: [refund.status, {const: "single"}]}, {op: test, eq: [refund.status, {const: "hoh"}]}]}}
          then: refund.h_box_married
  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household). No boxes checked, enter -0-"
    type: NonNegDollars
    expr: {op: multiply_count, amount: refund.h_box_amount, count: refund.h_boxes}
  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6"
    type: NonNegDollars
    expr: {op: sum, of: [refund.line5, refund.line6]}
  - id: refund.h_line8_sub
    printed: "(helper)"
    label: "Subtract line 7 from line 4 (zero if line 7 is not less than line 4)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line4, take: refund.line7}
    note: "If line 7 is not less than line 4, the worksheet says STOP, none of the refund is taxable. Chosen: encoded as zero, which makes line 9 zero."
  - id: refund.h_mfs_spouse_item
    printed: "(helper)"
    label: "2024 filing status married filing separately and spouse itemized deductions in 2024"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [refund.status, {const: "mfs"}]}, {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}]}
  - id: refund.line8
    printed: "8"
    label: "Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and your spouse itemized deductions in 2024, the amount from line 4)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [refund.h_mfs_spouse_item, {const: true}]}, then: refund.line4}
        - {guard: {op: test, eq: [refund.h_mfs_spouse_item, {const: false}]}, then: refund.h_line8_sub}
  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.line3, refund.line8]}
  - id: refund.has
    printed: "(helper)"
    label: "Any state or local income tax refund received in 2025"
    type: Bool
    expr: {op: test, gt: [refund.received, {const: 0}]}
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable part of your refund (zero when you did not itemize for 2024 or deducted general sales taxes)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [refund.itemized, {const: true}]}, {op: test, eq: [refund.sales, {const: false}]}]}
          then: refund.line9
        - guard: {op: test, not: {op: test, all: [{op: test, eq: [refund.itemized, {const: true}]}, {op: test, eq: [refund.sales, {const: false}]}]}}
          then: refund.h_zero
    note: "Per the Schedule 1 line 1 TIP, none of the refund is taxable if for 2024 you didn’t itemize or elected to deduct general sales taxes. The worksheet, and its screens on line 1, is reached only otherwise."
```
```
