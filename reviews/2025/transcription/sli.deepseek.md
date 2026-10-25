# Transcription agreement — sli

Second transcription of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` by an isolated model (spec 6.5), compared line by line with `forms/2025/sli.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 283b44fbd9eb86179e568ecfdf72a4d08af1b788245a45deb74ffae171d3354f |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ff76da6d126a9abdc6f51becc98940ac3a40b516122237f06b10ea1df0276faf |
| printed lines compared | 9 |
| agree / disagree / missing | 4 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sli.deduction — Student loan interest deduction (Schedule 1, line 21)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "sli.interest"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "sli.interest"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "sli.claimed"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "sli.claimed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sli.claimed"}], "test": "ne"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sli.claimed"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The printed line 9 is the worksheet result before the eligibility conditions. This result interface returns zero when the taxpayer (or spouse on a joint return) is claimed as a dependent or the filing status is married filing separately, because the IRS says the deduction can be taken only if those conditions are met.

Ruling: open

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **AGREE**

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **AGREE**

### 4 — Subtract line 3 from line 2
Status: **AGREE**

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "sli.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.base_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sli.base_other"}}], "op": "choose"}
```

Second transcription's note: The worksheet gives no line 5 amount for married filing separately because the deduction is not allowed for that status. Line 5 uses the non-MFJ amount for every status other than MFJ; sli.deduction returns zero when the filing status is MFS or the taxpayer is claimed as a dependent.

Ruling: open

### 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project:

```json
{"from": {"line": "4"}, "op": "subtract", "take": {"line": "5"}}
```

Second:

```json
{"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Ruling: open

### 8 — Multiply line 1 by line 7
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4"}, {"line": "5"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "5"}, {"line": "4"}], "test": "lt"}, "then": {"amount": {"line": "1"}, "op": "prorate", "part": {"line": "6"}, "places": 3, "whole": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "sli.divisor_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.divisor_joint"}}], "op": "choose"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "1"}, "op": "prorate", "part": {"line": "6"}, "places": 3, "whole": {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.divisor_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sli.divisor_other"}}], "op": "choose"}}
```

Ruling: open

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **DISAGREE**

Project:

```json
{"from": {"line": "1"}, "op": "subtract_floor0", "take": {"line": "8"}}
```

Second:

```json
{"from": {"line": "1"}, "op": "subtract", "take": {"line": "8"}}
```

Ruling: open

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 3 | scope.schedule1 | scope.schedule1 |
| 4 | scope.schedule1 | - |
| 6 | scope.schedule1 | - |

## Raw second transcription

```yaml
lines:
  - id: sli.line1
    printed: "1"
    label: "Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don’t enter more than $2,500"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sli.interest, {param: sli.max}]}
  - id: sli.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9"
    type: Dollars
    expr: {op: copy, from: f1040.line9}
  - id: sli.line3
    printed: "3"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr:
      op: sum
      of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line20, s1.line25]
    refuses: [scope.schedule1]
    note: "The sum uses the supported Schedule 1 adjustment lines in the printed range. scope.schedule1 refuses the line when an unsupported adjustment in that range, such as line 12, 14 or 23, is present."
  - id: sli.line4
    printed: "4"
    label: "Subtract line 3 from line 2"
    type: Dollars
    expr: {op: subtract, from: sli.line2, take: sli.line3}
  - id: sli.line5
    printed: "5"
    label: "Enter the amount shown below for your filing status. Single, head of household, or qualifying surviving spouse—$85,000. Married filing jointly—$170,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sli.h_base_joint
        - guard: {op: test, not: {op: test, eq: [f1040.status, {const: "mfj"}]}}
          then: sli.h_base_other
    note: "The worksheet gives no line 5 amount for married filing separately because the deduction is not allowed for that status. Line 5 uses the non-MFJ amount for every status other than MFJ; sli.deduction returns zero when the filing status is MFS or the taxpayer is claimed as a dependent."
  - id: sli.line6
    printed: "6"
    label: "Is the amount on line 4 more than the amount on line 5? No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9. Yes. Subtract line 5 from line 4"
    type: Dollars
    expr: {op: subtract_floor0, from: sli.line4, take: sli.line5}
  - id: sli.line8
    printed: "8"
    label: "Multiply line 1 by line 7"
    type: NonNegDollars
    expr: {op: prorate, amount: sli.line1, part: sli.line6, whole: sli.h_divisor, places: 3}
  - id: sli.line9
    printed: "9"
    label: "Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on Schedule 1, line 21. Don’t include this amount in figuring any other deduction on your return (such as on Schedule A, C, E, etc.)"
    type: NonNegDollars
    expr: {op: subtract, from: sli.line1, take: sli.line8}
  - id: sli.h_base_joint
    printed: "(helper)"
    label: "Base amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_joint}
  - id: sli.h_base_other
    printed: "(helper)"
    label: "Base amount for filing statuses other than married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_other}
  - id: sli.h_div_joint
    printed: "(helper)"
    label: "Divisor for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_joint}
  - id: sli.h_div_other
    printed: "(helper)"
    label: "Divisor for filing statuses other than married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_other}
  - id: sli.h_divisor
    printed: "(helper)"
    label: "Divisor used in line 7"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sli.h_div_joint
        - guard: {op: test, not: {op: test, eq: [f1040.status, {const: "mfj"}]}}
          then: sli.h_div_other
  - id: sli.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sli.h_ineligible
    printed: "(helper)"
    label: "Whether the student loan interest deduction is disallowed by the filing status or dependent rule"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sli.claimed, {const: true}]}
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: sli.deduction
    printed: "(helper)"
    label: "Student loan interest deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sli.h_ineligible, {const: true}]}
          then: sli.h_zero
        - guard: {op: test, eq: [sli.h_ineligible, {const: false}]}
          then: sli.line9
    note: "The printed line 9 is the worksheet result before the eligibility conditions. This result interface returns zero when the taxpayer (or spouse on a joint return) is claimed as a dependent or the filing status is married filing separately, because the IRS says the deduction can be taken only if those conditions are met."
```
