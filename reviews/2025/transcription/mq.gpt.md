# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | gpt-6-astra |
| model reported | gpt-6-astra |
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
{"args": [{"of": [{"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}], "op": "sum"}, {"of": [{"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}], "op": "sum"}], "test": "lt"}
```

Second transcription's note: Applies to the supported property for which the mid-month convention does not apply. The comparison is strictly more than 40%; equality, including zero total basis, yields false.

Ruling: representation; p946 p. 34, Which Convention Applies?, Mid-quarter convention: the convention applies if "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year (...) are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year". The reply compares total + total with five times the fourth-quarter sum, that is 2 x total < 5 x fourth quarter, the project's test written as sums. executable-triage-v2 (`reviews/2025/transcription/triage/mq.gpt.json`; 1,495 fixtures, 500 generated returns seed 20261026, 0 partial records; 1,995 comparisons): 1,995 of 1,995 agree; differences none; on returns the full interview completes: none. No difference on any compared record.

## Raw second transcription

```yaml
lines:
  - id: mq.h_last_three_months
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.mq_q4
    cite: "Publication 946 (2025), page 34, The mid-quarter convention."
    note: "Uses the published per-person mid-quarter basis aggregates within the declared scope. Bases exclude personal use and amounts expensed under section 179, but are not reduced by any special depreciation allowance."

  - id: mq.h_entire_year
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property you placed in service during the entire year"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.mq_total
    cite: "Publication 946 (2025), page 34, The mid-quarter convention."

  - id: mq.h_last_three_months_times_five
    printed: "(helper)"
    label: "Five times the total depreciable bases for the last 3 months"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - mq.h_last_three_months
        - mq.h_last_three_months
        - mq.h_last_three_months
        - mq.h_last_three_months
        - mq.h_last_three_months
    cite: "Publication 946 (2025), page 34, The mid-quarter convention."
    note: "Cross-multiplication expresses the strict 40% comparison exactly, without rounding a monetary threshold."

  - id: mq.h_entire_year_times_two
    printed: "(helper)"
    label: "Twice the total depreciable bases for the entire year"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - mq.h_entire_year
        - mq.h_entire_year
    cite: "Publication 946 (2025), page 34, The mid-quarter convention."

  - id: mq.applies
    printed: "(helper)"
    label: "The mid-quarter convention"
    type: Bool
    expr:
      op: test
      gt:
        - mq.h_last_three_months_times_five
        - mq.h_entire_year_times_two
    cite: "Publication 946 (2025), page 34, The mid-quarter convention."
    note: "Applies to the supported property for which the mid-month convention does not apply. The comparison is strictly more than 40%; equality, including zero total basis, yields false."
```
