# Transcription agreement — qdcg

Second transcription of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/qdcg.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 40fc2376a6e1a9a2d7729b4689f0af01df0e88777dc6578f08bed3cccbef1c76 |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 81d2f1dd22ed930c869f4c72dfaede472cb7aa0aeceefbe5d68a09b628d819b5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6100db164f445104624c5ab49f073f2d2b4eb2678169223aa3bbcc859f9a3f82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0ec80da435463402c2d8e70745618a3a4b8e2d8949ed1b76192d41f26ba57324 |
| printed lines compared | 26 |
| agree / disagree / missing | 23 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (question) — Are you filing Schedule D?
Status: **AGREE**

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555
Status: **AGREE**

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **AGREE**

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"ref": "sd.distributions"}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"ref": "f1040.line7a"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"of": [{"from": {"ref": "sd.line15"}, "op": "subtract_floor0", "take": {"const": 0}}, {"from": {"ref": "sd.line16"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: representation; i1040gi p.38 QDCG worksheet line3 uses Form1040 line7a when ScheduleD is not filed; in the supported distribution-only route that amount is sd.distributions, while all direct sales/loss routes require ScheduleD. On the filed route, max(min(SD15,SD16),0) equals min(max(SD15,0),max(SD16,0)), the printed loss-to-zero rule. This compares the prepared, supported-return quantities; it does not claim arbitrary inconsistent supplied cross-form subtotals or all partial-input paths are equivalent.

### 4 — Add lines 2 and 3
Status: **AGREE**

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **DISAGREE**

Project:

```json
{"param": "qdcg.zero_rate_ceiling"}
```

Second:

```json
{"from": {"param": "qdcg.zero_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged.

Ruling: representation; i1040gi p.38 line6 prints positive filing-status ceilings. The matching year parameter is always positive in every declared status; subtract_floor0(parameter,0) leaves that amount unchanged and adds no missing filer input. The extra floor does not change the printed quantity.

### 7 — Enter the smaller of line 1 or line 6
Status: **AGREE**

### 8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **AGREE**

### 10 — Enter the smaller of line 1 or line 4
Status: **AGREE**

### 11 — Enter the amount from line 9
Status: **AGREE**

### 12 — Subtract line 11 from line 10
Status: **AGREE**

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **DISAGREE**

Project:

```json
{"param": "qdcg.fifteen_rate_ceiling"}
```

Second:

```json
{"from": {"param": "qdcg.fifteen_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged.

Ruling: representation; i1040gi p.38 line13 prints positive filing-status ceilings. The matching year parameter is always positive in every declared status; subtract_floor0(parameter,0) leaves that amount unchanged and adds no missing filer input. The extra floor does not change the printed quantity.

### 14 — Enter the smaller of line 1 or line 13
Status: **AGREE**

### 15 — Add lines 5 and 9
Status: **AGREE**

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **AGREE**

### 17 — Enter the smaller of line 12 or line 16
Status: **AGREE**

### 18 — Multiply line 17 by 15% (0.15)
Status: **AGREE**

### 19 — Add lines 9 and 17
Status: **AGREE**

### 20 — Subtract line 19 from line 10
Status: **AGREE**

### 21 — Multiply line 20 by 20% (0.20)
Status: **AGREE**

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **AGREE**

### 23 — Add lines 18, 21, and 22
Status: **AGREE**

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **AGREE**

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | sa.excluded_income | - |
| 5 | sa.excluded_income | - |
| 7 | sa.excluded_income | - |
| 8 | sa.excluded_income | - |
| 9 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 11 | sa.excluded_income | - |
| 12 | sa.excluded_income | - |
| 14 | sa.excluded_income | - |
| 15 | sa.excluded_income | - |
| 16 | sa.excluded_income | - |
| 17 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 19 | sa.excluded_income | - |
| 20 | sa.excluded_income | - |
| 21 | sa.excluded_income | - |
| 22 | sa.excluded_income | - |
| 23 | sa.excluded_income | - |
| 24 | sa.excluded_income | - |
| 25 | sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: qdcg.schedule_d_filed
    printed: "(question)"
    label: "Are you filing Schedule D?"
    type: Bool
    expr: {op: copy, from: sd.filed}
    note: "The interface is closed, so this question is not a new input. It is read from the project's Schedule D filing determination (sd.filed)."

  - id: qdcg.line1
    printed: "1"
    label: "Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    refuses: [sa.excluded_income]
    note: "The Form 2555 case (Foreign Earned Income Tax Worksheet, also the footnote to lines 2 and 3) is not computed. The screening input sa.excluded_income (filing Form 2555) refuses it instead."

  - id: qdcg.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}

  - id: qdcg.h_sd15_pos
    printed: "(helper)"
    label: "Schedule D, line 15; -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: {const: 0}}

  - id: qdcg.h_sd16_pos
    printed: "(helper)"
    label: "Schedule D, line 16; -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line16, take: {const: 0}}

  - id: qdcg.h_sd_smaller
    printed: "(helper)"
    label: "Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.h_sd15_pos, qdcg.h_sd16_pos]}

  - id: qdcg.h_line7a_pos
    printed: "(helper)"
    label: "No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line7a, take: {const: 0}}
    note: "Without Schedule D, line 7a holds only capital gain distributions, which cannot be negative. The zero floor only proves the type and does not change any value on that path."

  - id: qdcg.line3
    printed: "3"
    label: "Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: true}]}
          then: qdcg.h_sd_smaller
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: false}]}
          then: qdcg.h_line7a_pos

  - id: qdcg.line4
    printed: "4"
    label: "Add lines 2 and 3"
    type: NonNegDollars
    expr: {op: sum, of: [qdcg.line2, qdcg.line3]}

  - id: qdcg.line5
    printed: "5"
    label: "Subtract line 4 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.line1, take: qdcg.line4}

  - id: qdcg.h_zero_ceiling
    printed: "(helper)"
    label: "$48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}

  - id: qdcg.line6
    printed: "6"
    label: "Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_zero_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged."

  - id: qdcg.line7
    printed: "7"
    label: "Enter the smaller of line 1 or line 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line6]}

  - id: qdcg.line8
    printed: "8"
    label: "Enter the smaller of line 5 or line 7"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line5, qdcg.line7]}

  - id: qdcg.line9
    printed: "9"
    label: "Subtract line 8 from line 7. This amount is taxed at 0%"
    type: Dollars
    expr: {op: subtract, from: qdcg.line7, take: qdcg.line8}

  - id: qdcg.line10
    printed: "10"
    label: "Enter the smaller of line 1 or line 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line4]}

  - id: qdcg.line11
    printed: "11"
    label: "Enter the amount from line 9"
    type: Dollars
    expr: {op: copy, from: qdcg.line9}

  - id: qdcg.line12
    printed: "12"
    label: "Subtract line 11 from line 10"
    type: Dollars
    expr: {op: subtract, from: qdcg.line10, take: qdcg.line11}

  - id: qdcg.h_fifteen_ceiling
    printed: "(helper)"
    label: "$533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}

  - id: qdcg.line13
    printed: "13"
    label: "Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_fifteen_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged."

  - id: qdcg.line14
    printed: "14"
    label: "Enter the smaller of line 1 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line13]}

  - id: qdcg.line15
    printed: "15"
    label: "Add lines 5 and 9"
    type: Dollars
    expr: {op: sum, of: [qdcg.line5, qdcg.line9]}

  - id: qdcg.line16
    printed: "16"
    label: "Subtract line 15 from line 14. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.line14, take: qdcg.line15}

  - id: qdcg.line17
    printed: "17"
    label: "Enter the smaller of line 12 or line 16"
    type: Dollars
    expr: {op: smaller_of, of: [qdcg.line12, qdcg.line16]}

  - id: qdcg.line18
    printed: "18"
    label: "Multiply line 17 by 15% (0.15)"
    type: Dollars
    expr: {op: multiply_rate, amount: qdcg.line17, rate: {param: qdcg.rate_15}}

  - id: qdcg.line19
    printed: "19"
    label: "Add lines 9 and 17"
    type: Dollars
    expr: {op: sum, of: [qdcg.line9, qdcg.line17]}

  - id: qdcg.line20
    printed: "20"
    label: "Subtract line 19 from line 10"
    type: Dollars
    expr: {op: subtract, from: qdcg.line10, take: qdcg.line19}

  - id: qdcg.line21
    printed: "21"
    label: "Multiply line 20 by 20% (0.20)"
    type: Dollars
    expr: {op: multiply_rate, amount: qdcg.line20, rate: {param: qdcg.rate_20}}

  - id: qdcg.line22
    printed: "22"
    label: "Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 5 is $100,000 or more, use the Tax Computation Worksheet"
    type: Dollars
    expr:
      op: copy
      from: {def: tax_on_amount, bind: {amount: qdcg.line5, status: f1040.status}, line: tax}
    note: "The shared tax_on_amount definition applies the $100,000 boundary: the Tax Table below it, the Tax Computation Worksheet at or above it."

  - id: qdcg.line23
    printed: "23"
    label: "Add lines 18, 21, and 22"
    type: Dollars
    expr: {op: sum, of: [qdcg.line18, qdcg.line21, qdcg.line22]}

  - id: qdcg.line24
    printed: "24"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet"
    type: Dollars
    expr:
      op: copy
      from: {def: tax_on_amount, bind: {amount: qdcg.line1, status: f1040.status}, line: tax}

  - id: qdcg.line25
    printed: "25"
    label: "Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amount on the entry space on Form 1040 or 1040-SR, line 16. If you are filing Form 2555, don't enter this amount on the entry space on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet"
    type: Dollars
    expr: {op: smaller_of, of: [qdcg.line23, qdcg.line24]}
    note: "The Form 2555 routing is not computed; it is refused at line 1 through sa.excluded_income. Whether this worksheet applies at all is decided on Form 1040 (f1040.gate.qdcg_applies), not here."
```
```
