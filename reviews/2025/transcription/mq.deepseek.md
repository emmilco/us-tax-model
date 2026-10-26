# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5c25ab081eb597a4d768001c50076f3e338d4b19d0e6e24e7df6077a9bfddde3 |
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
| subject sha256 | 7a635868298039249c562405cd29bd2de3cef651b51f0bf258cd0dd44a40e55b |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| p946 | For use in preparing 2025 returns | 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### mq.applies — The mid-quarter convention applies: the October to December bases are more than 40% of all
Status: **AGREE**

## Raw second transcription

```yaml
lines:
  - id: mq.h_count5
    printed: "(helper)"
    label: "Count of five"
    type: Count
    expr: {op: param, ref: sc.count5}
  - id: mq.h_count2
    printed: "(helper)"
    label: "Count of two"
    type: Count
    expr: {op: param, ref: sc.count2}
  - id: mq.h_q4_total
    printed: "(helper)"
    label: "Total depreciable bases placed in service during the last 3 months of 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
  - id: mq.h_total_bases
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
  - id: mq.h_q4_times5
    printed: "(helper)"
    label: "Five times the last-3-month depreciable bases"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_q4_total, count: mq.h_count5}
  - id: mq.h_total_times2
    printed: "(helper)"
    label: "Two times the total depreciable bases"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_total_bases, count: mq.h_count2}
  - id: mq.applies
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [mq.h_q4_times5, mq.h_total_times2]}
    note: "The supplied interface has no printed lines. I derived the result from the existing person-level mq_q4 and mq_total totals. The test is that last-3-month bases exceed 40% of total bases, written as 5 times last-3-month bases greater than 2 times total bases to avoid rounding."
```
