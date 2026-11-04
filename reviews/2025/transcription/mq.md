# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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
{"args": [{"const": 41, "type": "Count"}, {"cap": 40, "op": "percent_floor", "part": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "whole": {"of": [{"const": 1}, {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}], "op": "larger_of"}}], "test": "le"}
```

Second transcription's note: 'More than 40%' is tested exactly: percent_floor returns 41 if and only if 100 x last-quarter bases > 40 x total bases. A rounded 40% product is not used. The mid-month convention does not enter here, because the per-asset totals already exclude real property and railroad grading or tunnel bores.

Ruling: representation; p946 p. 34, Which Convention Applies?, Mid-quarter convention: the convention applies if "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year (...) are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". The project tests 2 x total < 5 x fourth-quarter bases; the reply's percent_floor(fourth-quarter, larger of the constant 1 and the total, cap 40) returns 41 exactly when 100 x fourth-quarter > 40 x the whole (engine percent_floor), the same strict test, and with no basis both give false. executable-triage-v2 (`reviews/2025/transcription/triage/mq.json`; 1,495 fixtures, 500 generated returns seed 20261026, 0 partial records; 1,995 comparisons): 1,995 of 1,995 agree; differences none; on returns the full interview completes: none. No difference on any compared record. The package change to this form only links amb.2025.mq_joint; the expression is unchanged.

## Raw second transcription

```yaml
```yaml
lines:
  - id: mq.h_q4
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property placed in service during the last 3 months of the tax year (excluding nonresidential real property, residential rental property, any railroad grading or tunnel bore, property placed in service and disposed of in the same year, and property depreciated under a method other than MACRS)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
    note: "Pub. 946 states the test in terms of property 'you placed in service' and does not say how a joint return is treated. This reading adds the published per-person totals over everyone on the return. Each published total already reflects the section 179 reduction and the personal-use reduction, and ignores the special depreciation allowance."
  - id: mq.h_total
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property you placed in service during the entire year (same exclusions)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
    note: "This uses the same aggregation reading as mq.h_q4: the per-person totals are added over the whole return."
  - id: mq.h_cent
    printed: "(helper)"
    label: "One cent (keeps the divisor positive when no property was placed in service)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: mq.h_whole
    printed: "(helper)"
    label: "Total depreciable bases for the year, at least one cent"
    type: NonNegDollars
    expr: {op: larger_of, of: [mq.h_total, mq.h_cent]}
    note: "percent_floor needs a positive whole. When the total is zero, the last-quarter amount is also zero, so the percentage is 0 and the convention does not apply. The one-cent floor changes no other result."
  - id: mq.h_pct
    printed: "(helper)"
    label: "Last-quarter bases as a whole-number percentage of the year's bases (41 when more than 40%)"
    type: Count
    expr: {op: percent_floor, part: mq.h_q4, whole: mq.h_whole, cap: 40}
  - id: mq.applies
    printed: "(helper)"
    label: "The mid-quarter convention applies: the total depreciable bases of MACRS property placed in service during the last 3 months of the tax year are more than 40% of the total depreciable bases of all MACRS property placed in service during the entire year"
    type: Bool
    expr: {op: test, ge: [mq.h_pct, {const: 41, type: Count}]}
    note: "'More than 40%' is tested exactly: percent_floor returns 41 if and only if 100 x last-quarter bases > 40 x total bases. A rounded 40% product is not used. The mid-month convention does not enter here, because the per-asset totals already exclude real property and railroad grading or tunnel bores."
```
```
