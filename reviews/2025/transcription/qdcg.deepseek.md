# Transcription agreement — qdcg

Second transcription of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/qdcg.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 301ee462530f889a138b2fd9d2348f6a1cc6c9e61c43a84672b9630ede486d89 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0ec80da435463402c2d8e70745618a3a4b8e2d8949ed1b76192d41f26ba57324 |
| printed lines compared | 26 |
| agree / disagree / missing | 25 / 1 / 0 |
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
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"ref": "f1040.line7a"}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"of": [{"const": 0}, {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}], "op": "larger_of"}}], "op": "choose"}
```

Second transcription's note: A blank Schedule D line 15 or 16 is treated as zero, as the tool's Schedule D supplies a computed amount on each; a loss, or a smaller-of result below zero, is floored at zero on the helper line.

Ruling: representation; archived i1040gi (2025) p. 38 QDCGT line 3 takes the smaller Schedule D lines 15/16, zero for a loss, or Form 1040 line 7a when no Schedule D is filed. The filed-Schedule-D expressions are definitionally equal: subtract_floor0(min(a,b),0) = max(0,min(a,b)). For a supported complete return with sd.filed=false, sales and special-rate gains are absent, carryovers/unmodeled income are refused, and Schedule D lines 7/15/16 reduce to 0/distributions/distributions. Thus f1040.line7a via sd.to1040 equals the NonNegDollars sd.distributions. This is a completed-return arithmetic proof and does not assert equality of partial/unknown-entry evaluation.

### 4 — Add lines 2 and 3
Status: **AGREE**

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **AGREE**

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
Status: **AGREE**

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

## Raw second transcription

```yaml
lines:
  - id: qdcg.schedule_d_filed
    printed: "(question)"
    label: "Are you filing Schedule D?"
    type: Bool
    expr: {op: copy, from: sd.filed}
    note: "The worksheet prints no separate question; 'Are you filing Schedule D?' is the project-supplied gate for line 3's Yes/No branches, taken from the Schedule D filing indicator."
  - id: qdcg.line1
    printed: "1"
    label: "Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    note: "The Form 2555 alternative is outside this tool's scope; line 15 of Form 1040 is used."
  - id: qdcg.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}
  - id: qdcg.line3
    printed: "3"
    label: "Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: true}]}
          then: qdcg.h_sd_floor
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: false}]}
          then: f1040.line7a
    note: "A blank Schedule D line 15 or 16 is treated as zero, as the tool's Schedule D supplies a computed amount on each; a loss, or a smaller-of result below zero, is floored at zero on the helper line."
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
  - id: qdcg.line6
    printed: "6"
    label: "Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household."
    type: NonNegDollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}
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
  - id: qdcg.line13
    printed: "13"
    label: "Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household."
    type: NonNegDollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}
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
    type: NonNegDollars
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
  - id: qdcg.h_sd_smaller
    printed: "(helper)"
    label: "Smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
  - id: qdcg.h_sd_floor
    printed: "(helper)"
    label: "Smaller of Schedule D lines 15 and 16, but not less than zero"
    type: NonNegDollars
    expr: {op: larger_of, of: [qdcg.h_sd_smaller, {const: 0}]}
```
