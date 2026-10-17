# Transcription agreement — qdcg

Second transcription of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/qdcg.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | - |
| prompt sha256 | 67fe775f1ed9cbaeee1e2243496a9a3339de781d848817efb5585b9242de810d |
| printed lines compared | 26 |
| agree / disagree / missing | 24 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### (question) — Are you filing Schedule D?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"input": "Interview question: Are you filing Schedule D? (Qualified Di"}
```

Ruling: equivalent representation; project retained. The project derives the answer to “Are you filing Schedule D?” from Schedule D’s own filing test (`sd.filed`: any sale entered, or a 28% rate gain or unrecaptured section 1250 gain), so it cannot contradict the Schedule D the return actually contains; the second transcription asks it as an interview question. No change to the data.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"ref": "f1040.line7a"}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Second transcription's note: Typed as signed Dollars because the 'No' branch copies Form 1040 line 7a, and the text does not state that this value is non-negative. The Form 2555 footnote is not encoded.

Ruling: equivalent representation; project retained. The No branch reads “Enter the amount from Form 1040 or 1040-SR, line 7a” (i1040gi p. 38). When Schedule D is not required, line 7a carries the total capital gain distributions from Form 1099-DIV box 2a (i1040gi p. 33, line 7a, Exception 1), which is the value the project references directly (`sd.distributions`); the second transcription references line 7a literally. No change to the data.

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
```yaml
lines:
  - id: qdcg.line(question)
    printed: "(question)"
    label: "Are you filing Schedule D?"
    type: Bool
    expr: {op: input, source: "Interview question: Are you filing Schedule D? (Qualified Dividends and Capital Gain Tax Worksheet, line 3)"}

  - id: qdcg.line1
    printed: "1"
    label: "Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    note: "Open point: the Form 2555 alternative (line 3 of the Foreign Earned Income Tax Worksheet) has no line id available here. Chosen reading: this transcription covers only returns that do not file Form 2555, so the value is copied from Form 1040 line 15. Form 2555 filers must be screened out elsewhere."

  - id: qdcg.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}
    note: "The footnote for Form 2555 filers is not encoded, which is consistent with line 1."

  - id: qdcg.h_sd_smaller
    printed: "(helper)"
    label: "Smaller of Schedule D line 15 or line 16"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}

  - id: qdcg.h_sd_smaller_floor0
    printed: "(helper)"
    label: "Smaller of Schedule D line 15 or line 16; if either line is blank or a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_sd_smaller, take: {const: 0}}
    note: "Open point: 'blank'. Chosen reading: a blank Schedule D line is treated as zero. If either line is a loss (negative), the smaller value is at most zero, so a floor at zero gives -0-. If either line is zero or blank, the result is also -0-."

  - id: qdcg.line3
    printed: "3"
    label: "Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["qdcg.line(question)", {const: true}]}
          then: qdcg.h_sd_smaller_floor0
        - guard: {op: test, eq: ["qdcg.line(question)", {const: false}]}
          then: f1040.line7a
    note: "Typed as signed Dollars because the 'No' branch copies Form 1040 line 7a, and the text does not state that this value is non-negative. The Form 2555 footnote is not encoded."

  - id: qdcg.line4
    printed: "4"
    label: "Add lines 2 and 3"
    type: Dollars
    expr: {op: sum, of: [qdcg.line2, qdcg.line3]}

  - id: qdcg.line5
    printed: "5"
    label: "Subtract line 4 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.line1, take: qdcg.line4}

  - id: qdcg.line6
    printed: "6"
    label: "Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}
    note: "The parameter is keyed by filing status taken from f1040.status."

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
    type: Dollars
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
    label: "Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}
    note: "The parameter is keyed by filing status taken from f1040.status."

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
    note: "Open point: the worksheet states no rounding rule for this product. Chosen reading: no round atom is applied; the multiply_rate result convention governs."

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
    note: "Open point: the worksheet states no rounding rule for this product. Chosen reading: no round atom is applied."

  - id: qdcg.h_line5_table_tax
    printed: "(helper)"
    label: "Tax on line 5 from the Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: qdcg.line5, status: f1040.status}

  - id: qdcg.h_line5_tcw_tax
    printed: "(helper)"
    label: "Tax on line 5 from the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: qdcg.line5, status: f1040.status}, line: worksheet_tax}}

  - id: qdcg.line22
    printed: "22"
    label: "Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 5 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [qdcg.line5, {param: ordinary.table_boundary}]}
          then: qdcg.h_line5_table_tax
        - guard: {op: test, ge: [qdcg.line5, {param: ordinary.table_boundary}]}
          then: qdcg.h_line5_tcw_tax

  - id: qdcg.line23
    printed: "23"
    label: "Add lines 18, 21, and 22"
    type: Dollars
    expr: {op: sum, of: [qdcg.line18, qdcg.line21, qdcg.line22]}

  - id: qdcg.h_line1_table_tax
    printed: "(helper)"
    label: "Tax on line 1 from the Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: qdcg.line1, status: f1040.status}

  - id: qdcg.h_line1_tcw_tax
    printed: "(helper)"
    label: "Tax on line 1 from the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: qdcg.line1, status: f1040.status}, line: worksheet_tax}}

  - id: qdcg.line24
    printed: "24"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [qdcg.line1, {param: ordinary.table_boundary}]}
          then: qdcg.h_line1_table_tax
        - guard: {op: test, ge: [qdcg.line1, {param: ordinary.table_boundary}]}
          then: qdcg.h_line1_tcw_tax

  - id: qdcg.line25
    printed: "25"
    label: "Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amount on the entry space on Form 1040 or 1040-SR, line 16. If you are filing Form 2555, don't enter this amount on the entry space on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet"
    type: Dollars
    expr: {op: smaller_of, of: [qdcg.line23, qdcg.line24]}
    note: "The routing to Form 1040 line 16 is expressed on that form, not here. The Form 2555 routing is not encoded, which is consistent with line 1."
```
```
