# Transcription agreement — tipjob

Second transcription of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/tipjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-24 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 93b2028b3e83c77828f35c6c7fe7f730af87de09ee62dc7cae45f54b87eac109 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | max |
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
| 1(c) | f8959.unsupported | f8959.unsupported |
| 1(d) | f8959.unsupported, tipjob.mixed | f8959.unsupported |

## Raw second transcription

```yaml
lines:
  - id: tipjob.col_c
    printed: "1(c)"
    label: "Qualified tips reported on Form 4137, column 1(c), for this employer"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [f8959.unsupported]
    note: "The closed input interface has no Form 4137 column 1(c) amount. Form 4137 cases are outside the computed scope (f8959.unsupported), so for supported entries this line is zero."
  - id: tipjob.col_d
    printed: "1(d)"
    label: "Enter the greater of column (b) or column (c)"
    type: NonNegDollars
    expr: {op: larger_of, of: [tipjob.amount, tipjob.col_c]}
    refuses: [tipjob.mixed, f8959.unsupported]
  - id: tipjob.one
    printed: "(helper)"
    label: "One employer represented by this worksheet entry"
    type: Count
    expr: {op: param, ref: sc.one}
    note: "The worksheet has one row per employer, so each row contributes one employer to the count."
  - id: tipjob.mixed
    printed: "(gate)"
    label: "The tips counted from this employer are not all in an occupation on the IRS list"
    type: Bool
    expr: {op: test, eq: [tipjob.qualified, {const: false}]}
```
