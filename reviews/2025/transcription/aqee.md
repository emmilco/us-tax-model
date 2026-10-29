# Transcription agreement — aqee

Second transcription of `Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student` by an isolated model (spec 6.5), compared line by line with `forms/2025/aqee.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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
```yaml
lines:
  - id: aqee.h_ws1_aoc
    printed: "(helper)"
    label: "Adjusted Qualified Education Expenses Worksheet, line 1 (American opportunity credit): Total qualified education expenses paid for or on behalf of the student in 2025 for the academic period (tuition, fees and course materials)"
    type: NonNegDollars
    expr: {op: sum, of: [inst, mat]}
    note: "For the American opportunity credit, qualified expenses include course materials needed for a course of study whether or not they are bought from the institution (i8863 p. 4). Line 1 is therefore the expenses paid to the institution plus the other course materials."
  - id: aqee.h_ws4_aoc
    printed: "(helper)"
    label: "Adjusted Qualified Education Expenses Worksheet, line 4 (American opportunity credit): Adjusted qualified education expenses. Subtract line 3 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: aqee.h_ws1_aoc, take: adj}
    note: "Line 3 (total adjustments: lines 2a, 2b and 2c) is the bound input adj. The worksheet is completed for each academic period, but the interface supplies per-student totals, so it is applied once to those totals. The screening input edu_over covers an academic period whose adjustments exceed that period's own expenses."
  - id: ws4_llc
    printed: "(helper)"
    label: "Adjusted Qualified Education Expenses Worksheet, line 4 (lifetime learning credit): Adjusted qualified education expenses. Subtract line 3 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: inst, take: adj}
    note: "For the lifetime learning credit, books, supplies and equipment qualify only if they must be paid to the institution (i8863 p. 4), so worksheet line 1 is inst alone. The text does not say how to split the adjustments between expense types. The full adjustments (adj) are subtracted here, as the worksheet's line 3 directs. This value feeds line 31."
  - id: zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "The pages do not determine what this interface means. It is read as a zero amount (for example the value of lines 27 to 30 when the student does not qualify for the American opportunity credit). It is taken from the zero-valued money parameter ss.zero."
  - id: aqee.h_cap
    printed: "(helper)"
    label: "Don't enter more than $4,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}
  - id: line27
    printed: "27"
    label: "Adjusted qualified education expenses (see instructions). Don't enter more than $4,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [aqee.h_ws4_aoc, aqee.h_cap]}
  - id: aqee.h_full_band
    printed: "(helper)"
    label: "$2,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}
  - id: line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: line27, take: aqee.h_full_band}
  - id: line29
    printed: "29"
    label: "Multiply line 28 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: line28, rate: {param: aoc.second_rate}}
  - id: aqee.h_line29_plus
    printed: "(helper)"
    label: "Add $2,000 to the amount on line 29"
    type: NonNegDollars
    expr: {op: sum, of: [line29, aqee.h_full_band]}
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
          then: aqee.h_line29_plus
```
```
