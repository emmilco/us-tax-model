# Transcription agreement — aqee

Second transcription of `Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student` by an isolated model (spec 6.5), compared line by line with `forms/2025/aqee.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 834ac13506d91db107b1e75c73cdc6c6eedc18f8a38edfc969cf656132494510 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 8413d4a1b4749d2b2c6d49babcf85ee3e703a77171751d440d72a0914ff47034 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 295917039b59519098258d4955b3f383a2c177683a1b8d1019e6973af3bd62a3 |
| printed lines compared | 3 |
| agree / disagree / missing | 3 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8863 | 2025 | 3, 4, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 3, 4, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |

## Lines

### ws4_llc — Worksheet line 4 for the lifetime learning credit: the expenses required to be paid to the
Status: **AGREE**

### zero — Zero
Status: **AGREE**

### line30 — If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on
Status: **AGREE**

## Raw second transcription

```yaml
lines:
  - id: line27
    printed: "27"
    label: "Adjusted qualified education expenses (see instructions). Don't enter more than $4,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [aqee.h_ws4_aoc, aqee.h_aoc_cap]}
  - id: line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: line27, take: {param: aoc.full_band}}
  - id: line29
    printed: "29"
    label: "Multiply line 28 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: line28, rate: {param: aoc.second_rate}}
  - id: line30
    printed: "30"
    label: "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29 and enter the result. Skip line 31. Include the total of all amounts from all Parts III, line 30, on Part I, line 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [line28, {const: 0}]}
          then: line27
        - guard: {op: test, ne: [line28, {const: 0}]}
          then: aqee.h_line30_else
  - id: ws4_llc
    printed: "(helper)"
    label: "Adjusted qualified education expenses worksheet line 4 for the lifetime learning credit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: inst, take: adj}
    note: "Chosen reading: line 4 for the lifetime learning credit reduces expenses required to be paid to the institution (inst) by the combined adjustments (adj); other course materials (mat) count only for the American opportunity credit."
  - id: zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: aqee.h_total_aoc
    printed: "(helper)"
    label: "Total qualified education expenses for the American opportunity credit"
    type: NonNegDollars
    expr: {op: sum, of: [inst, mat]}
  - id: aqee.h_ws4_aoc
    printed: "(helper)"
    label: "Adjusted qualified education expenses worksheet line 4 for the American opportunity credit"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: aqee.h_total_aoc, take: adj}
  - id: aqee.h_aoc_cap
    printed: "(helper)"
    label: "American opportunity credit expense cap"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}
  - id: aqee.h_2000
    printed: "(helper)"
    label: "Amount added to line 29 on line 30"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}
  - id: aqee.h_line30_else
    printed: "(helper)"
    label: "Line 30 amount when line 28 is not zero"
    type: NonNegDollars
    expr: {op: sum, of: [line29, aqee.h_2000]}
```
