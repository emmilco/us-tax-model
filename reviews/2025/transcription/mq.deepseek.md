# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e67dda52503f308269033e4883ef713d2091d915482b0dc6e3cd445a3f5e63d6 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 701c77584bb3315c9633ab00c7c024cbc2fafce6c82e60815070312746c57459 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 076c50a4031857c718e8a7a9b9429bb8766193a78a28d6be71ccd45e5ce73442 |
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

Ruling: model error; p946 p. 34, Which Convention Applies?, Mid-quarter convention: the convention applies if "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year (...) are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". executable-triage-v2 (`reviews/2025/transcription/triage/mq.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 0 partial records; 1,995 comparisons): 1,995 of 1,995 agree; differences none; on returns the full interview completes: none. No difference on the sample, but the reply multiplies the total by the parameter sc.bonus_rate_40 (40%) with multiply_rate, which rounds the product to cents before the strict comparison. Counterexample (as ruled before on the same expression): total $1,000.02 and fourth quarter $400.01; exactly 40% is $400.008, so the source test is true (5 x 40,001 > 2 x 100,002), while the rounded $400.01 is not less than $400.01. Project stands.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| mq.applies | 841640d8b5aa7843d721d3614eedbbc4d662a791d25eccdf20f1951055d6619b |
| (rest of the document) | 176aa12f2dffc5143614105feaac9bce99368c09a467cee0c5571a7675dfbc40 |

## Raw second transcription

```yaml
lines:
  - id: mq.h_q4_basis
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
    cite: "Pub. 946 (2025), p. 34, Which Convention Applies? (mid-quarter convention)"
  - id: mq.h_total_basis
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property placed in service during the entire year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
    cite: "Pub. 946 (2025), p. 34, Which Convention Applies? (mid-quarter convention)"
  - id: mq.h_threshold
    printed: "(helper)"
    label: "40% of the total depreciable bases of all MACRS property placed in service during the entire year"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mq.h_total_basis, rate: {param: sc.bonus_rate_40}}
    cite: "Pub. 946 (2025), p. 34, Which Convention Applies? (mid-quarter convention)"
    note: "The only 40% Rate in the supplied parameter catalog is sc.bonus_rate_40; its value is 40/100 and it is used here for the 40% mid-quarter threshold."
  - id: mq.applies
    printed: "(helper)"
    label: "Mid-quarter convention applies"
    type: Bool
    expr: {op: test, gt: [mq.h_q4_basis, mq.h_threshold]}
    cite: "Pub. 946 (2025), p. 34, Which Convention Applies? (mid-quarter convention)"
```
