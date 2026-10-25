# Transcription agreement — tipjob

Second transcription of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/tipjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d8ec4413d6c8b93df5480033150128189a2d89b533295b5c8c1491beaaf7039c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 2a7723b9953e4329f2d8ffa0fd83943ff543a87316e13e7101d7b84b8aa7ea1d |
| printed lines compared | 3 |
| agree / disagree / missing | 3 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tipjob.one — One employer
Status: **AGREE**

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **AGREE**

### 1(d) — Enter the greater of column (b) or column (c)
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(c) | scope.other_income | scope.other_income |
| 1(d) | scope.other_income, tipjob.mixed | scope.other_income |

## Raw second transcription

```yaml
lines:
  - id: tipjob.col_c
    printed: "1(c)"
    label: "Qualified tips reported on Form 4137, column 1(c), for this employer"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [scope.other_income]
    note: "Form 4137 column 1(c) amounts are not supplied by the closed input interface. Within the supported slice this line is read as zero; cases with tips not on a Form W-2 are excluded by the scope.other_income screen."
  - id: tipjob.col_d
    printed: "1(d)"
    label: "Enter the greater of column (b) or column (c)"
    type: NonNegDollars
    expr: {op: larger_of, of: [tipjob.amount, tipjob.col_c]}
    refuses: [tipjob.mixed]
  - id: tipjob.one
    printed: "(helper)"
    label: "One employer entry (count)"
    type: Count
    expr: {op: param, ref: person.one}
```
