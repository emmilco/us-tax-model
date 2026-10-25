# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b09049415da39682518ec5285559be2812d54b63fbbc0d6ba097cb7b523bd792 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | max |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7a635868298039249c562405cd29bd2de3cef651b51f0bf258cd0dd44a40e55b |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| p946 | For use in preparing 2025 returns | 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### mq.applies — The mid-quarter convention applies: the October to December bases are more than 40% of all
Status: **DISAGREE**

Project:

```json
{"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}
```

Second:

```json
{"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}, {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}], "test": "lt"}
```

Second transcription's note: The archived text does not say whether separate Schedule C businesses or spouses on a joint return are tested separately; this line aggregates the person entries on the return for one test.

Ruling: model error; archived p946 (2025) p. 34 requires fourth-quarter bases to be more than 40% of the annual bases. The returned multiply_rate rounds the 40% product to cents under the shared IR, which changes this strict comparison. Counterexample: annual basis $1000.02 and Q4 basis $400.01. Exact 40% is $400.008, so the source test is true (5*40001 > 2*100002); the returned rate multiplication rounds to $400.01 and its strict comparison is false. This arithmetic failure remains even if its collection aggregation is supplied correctly. One model error out of one judged line exceeds the noise limit; this run earns no assertion.

## Raw second transcription

```yaml
lines:
  - id: mq.h_q4
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property placed in service during the last 3 months of 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
  - id: mq.h_total
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property placed in service during 2025"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
  - id: mq.h_threshold
    printed: "(helper)"
    label: "40% of total depreciable bases of all MACRS property placed in service during 2025"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mq.h_total, rate: {param: sc.bonus_rate_40}}
    note: "The archived text states a 40% test; no dedicated mid-quarter rate parameter is provided, so this line uses sc.bonus_rate_40, the pinned 40% rate."
  - id: mq.applies
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [mq.h_q4, mq.h_threshold]}
    note: "The archived text does not say whether separate Schedule C businesses or spouses on a joint return are tested separately; this line aggregates the person entries on the return for one test."
```
