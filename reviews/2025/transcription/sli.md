# Transcription agreement — sli

Second transcription of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` by an isolated model (spec 6.5), compared line by line with `forms/2025/sli.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ada1e00081a339e48011ffcfb86521129bd791cc10b620b3665df8d0f4f57923 |
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

Second transcription's note: The text lists the conditions for taking the deduction, but it doesn't say what to enter when they aren't met. This reads 'can't take the deduction' as zero on Schedule 1, line 21. The text also requires modified AGI under $100,000 ($200,000 if married filing jointly). That limit isn't a separate test here, because the worksheet's phase-out already brings the deduction to zero at that level.

Ruling: equivalent; project retained. The second omits the 'interest more than zero' guard; with no interest line 1 and line 9 are zero, so the value is the same, and the project's guard keeps a filer without student loan interest from being asked whether they are claimed as a dependent. The eligibility tests (not married filing separately, not claimed as a dependent) agree.

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

Second transcription's note: Line 5 shows no amount for married filing separately, because that status can't take the deduction. To keep the guards exhaustive, every status other than married filing jointly takes the $85,000 amount. For a married-filing-separately filer, sli.deduction is then forced to zero.

Ruling: representation; project retained. The worksheet gives no amount for married filing separately, which cannot take the deduction; the project enters zero there and the second enters $85,000. Neither reaches Schedule 1 line 21: sli.deduction is zero for married filing separately.

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

Second transcription's note: When the answer is No, the IRS text skips lines 6 and 7 and puts -0- on line 8. This line is written as a subtraction with a floor of zero, so in the No case it is 0. Line 7 is then 0 and line 8 is 0, which is the same result as the printed skip.

Ruling: equivalent; project retained. Line 6 is used only when line 4 is more than line 5 (line 8 skips it otherwise), where the signed difference and the floored one are the same.

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

Second transcription's note: Line 7 ('Divide line 6 by $15,000 ($30,000 if married filing jointly). Enter the result as a decimal (rounded to at least three places). If the result is 1.000 or more, enter 1.000') is built into this prorate atom rather than written as a separate line. 'At least three places' leaves the precision open; this uses exactly three places, rounded half-up, following amb.2025.sli_ratio_places.

Ruling: equivalent; project retained. The project skips to zero when line 4 is not more than line 5, as the worksheet says; the second always applies the ratio, which then has a part of zero or less, and prorate keeps the ratio at 0 or more, so it also gives zero (the same argument as the classified mutant on sli.line8).

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

Ruling: equivalent; project retained. Line 8 never exceeds line 1: prorate's ratio is at most 1.000 (Lean lemma prorate_le_amount), so the floor at zero never applies.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sli.deduction | sa.excluded_income | - |
| 1 | sa.excluded_income | - |
| 3 | scope.schedule1 | scope.schedule1 |
| 4 | scope.schedule1 | - |
| 6 | scope.schedule1 | - |
| 8 | sa.excluded_income | - |
| 9 | sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sli.h_max
    printed: "(helper)"
    label: "Year parameter sli.max ($2,500)"
    type: NonNegDollars
    expr: {op: param, ref: sli.max}
  - id: sli.line1
    printed: "1"
    label: "Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don't enter more than $2,500"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sli.interest, sli.h_max]}
    refuses: [sa.excluded_income]
    note: "Under the Exception in the line 21 instructions, you use Pub. 970 instead of this worksheet if you file Form 2555 or 4563 or exclude income from sources within Puerto Rico. This line refuses through the screening input sa.excluded_income, which asks exactly that question."
  - id: sli.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9"
    type: Dollars
    expr: {op: copy, from: f1040.line9}
  - id: sli.line3
    printed: "3"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr: {op: sum, of: [s1.line11, s1.line13]}
    refuses: [scope.schedule1]
    note: "Of Schedule 1 lines 11 through 20, 23 and 25, the tool computes only line 11 (educator expenses) and line 13 (HSA deduction). The other lines, and any line 24z write-in mentioned in 'Before you begin', fall under the screening input scope.schedule1. This line lists that input under refuses rather than entering those amounts as zero."
  - id: sli.line4
    printed: "4"
    label: "Subtract line 3 from line 2"
    type: Dollars
    expr: {op: subtract, from: sli.line2, take: sli.line3}
  - id: sli.h_base_other
    printed: "(helper)"
    label: "Line 5 amount: single, head of household, or qualifying surviving spouse—$85,000"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_other}
  - id: sli.h_base_joint
    printed: "(helper)"
    label: "Line 5 amount: married filing jointly—$170,000"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_joint}
  - id: sli.line5
    printed: "5"
    label: "Enter the amount shown below for your filing status. Single, head of household, or qualifying surviving spouse—$85,000. Married filing jointly—$170,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sli.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: sli.h_base_other
    note: "Line 5 shows no amount for married filing separately, because that status can't take the deduction. To keep the guards exhaustive, every status other than married filing jointly takes the $85,000 amount. For a married-filing-separately filer, sli.deduction is then forced to zero."
  - id: sli.line6
    printed: "6"
    label: "Is the amount on line 4 more than the amount on line 5? No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9. Yes. Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sli.line4, take: sli.line5}
    note: "When the answer is No, the IRS text skips lines 6 and 7 and puts -0- on line 8. This line is written as a subtraction with a floor of zero, so in the No case it is 0. Line 7 is then 0 and line 8 is 0, which is the same result as the printed skip."
  - id: sli.h_divisor_other
    printed: "(helper)"
    label: "Line 7 divisor: $15,000"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_other}
  - id: sli.h_divisor_joint
    printed: "(helper)"
    label: "Line 7 divisor if married filing jointly: $30,000"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_joint}
  - id: sli.h_divisor
    printed: "(helper)"
    label: "Divide line 6 by $15,000 ($30,000 if married filing jointly) — divisor for line 7"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sli.h_divisor_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: sli.h_divisor_other
  - id: sli.line8
    printed: "8"
    label: "Multiply line 1 by line 7"
    type: NonNegDollars
    expr: {op: prorate, amount: sli.line1, part: sli.line6, whole: sli.h_divisor, places: 3}
    note: "Line 7 ('Divide line 6 by $15,000 ($30,000 if married filing jointly). Enter the result as a decimal (rounded to at least three places). If the result is 1.000 or more, enter 1.000') is built into this prorate atom rather than written as a separate line. 'At least three places' leaves the precision open; this uses exactly three places, rounded half-up, following amb.2025.sli_ratio_places."
  - id: sli.line9
    printed: "9"
    label: "Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on Schedule 1, line 21"
    type: NonNegDollars
    expr: {op: subtract, from: sli.line1, take: sli.line8}
  - id: sli.h_zero
    printed: "(helper)"
    label: "No deduction"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sli.h_ineligible
    printed: "(helper)"
    label: "Can't take the deduction: filing status is married filing separately, or you are claimed as a dependent on someone else's 2025 tax return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sli.claimed, {const: true}]}
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
    note: "The instructions say the deduction requires a filing status other than married filing separately, and that 'You, or your spouse if filing jointly, aren't claimed as a dependent'. The only input available, sli.claimed, asks about you alone, so this test can't check whether a joint filer's spouse is claimed."
  - id: sli.deduction
    printed: "(helper)"
    label: "Student loan interest deduction (Schedule 1, line 21)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sli.h_ineligible, {const: true}]}
          then: sli.h_zero
        - guard: {op: test, eq: [sli.h_ineligible, {const: false}]}
          then: sli.line9
    note: "The text lists the conditions for taking the deduction, but it doesn't say what to enter when they aren't met. This reads 'can't take the deduction' as zero on Schedule 1, line 21. The text also requires modified AGI under $100,000 ($200,000 if married filing jointly). That limit isn't a separate test here, because the worksheet's phase-out already brings the deduction to zero at that level."
```
```
