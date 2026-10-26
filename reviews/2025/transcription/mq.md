# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5c25ab081eb597a4d768001c50076f3e338d4b19d0e6e24e7df6077a9bfddde3 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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
  - id: mq.h_q4
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
    cite: "Pub. 946 (2025), ch. 4, Which Convention Applies?, The mid-quarter convention"
    note: "The text speaks of property 'you placed in service'. It does not say whether a joint return combines both spouses' property. I chose to total every person on the return, treating the joint return as one taxpayer. Some items are excluded from the total: nonresidential real property, residential rental property, railroad grading or tunnel bore, property placed in service and disposed of in the same year, and property depreciated under a method other than MACRS. The section 179 and personal-use reductions apply, and no reduction is made for any special depreciation allowance. All of this is taken as already reflected in the per-person aggregate person.mq_q4 and the asset screens. It is not recomputed here."
  - id: mq.h_total
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property you placed in service during the entire year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
    cite: "Pub. 946 (2025), ch. 4, Which Convention Applies?, The mid-quarter convention"
    note: "Same reading as mq.h_q4: totals every person on the return and relies on the per-person aggregate person.mq_total for the exclusions and the basis reductions in the Caution paragraph."
  - id: mq.h_five
    printed: "(helper)"
    label: "The number 5 (to test more than 40% exactly, as 5 × last-quarter bases > 2 × total bases)"
    type: Count
    expr: {op: param, ref: sc.count5}
    cite: "Pub. 946 (2025), ch. 4, The mid-quarter convention ('more than 40%')"
  - id: mq.h_two
    printed: "(helper)"
    label: "The number 2 (to test more than 40% exactly, as 5 × last-quarter bases > 2 × total bases)"
    type: Count
    expr: {op: param, ref: sc.count2}
    cite: "Pub. 946 (2025), ch. 4, The mid-quarter convention ('more than 40%')"
  - id: mq.h_q4_x5
    printed: "(helper)"
    label: "Last-quarter depreciable bases times 5"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_q4, count: mq.h_five}
    cite: "Pub. 946 (2025), ch. 4, The mid-quarter convention"
  - id: mq.h_total_x2
    printed: "(helper)"
    label: "Total-year depreciable bases times 2"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_total, count: mq.h_two}
    cite: "Pub. 946 (2025), ch. 4, The mid-quarter convention"
  - id: mq.applies
    printed: "(helper)"
    label: "The mid-quarter convention applies: the total depreciable bases of MACRS property placed in service during the last 3 months of the tax year are more than 40% of the total depreciable bases of all MACRS property placed in service during the entire year"
    type: Bool
    expr: {op: test, gt: [mq.h_q4_x5, mq.h_total_x2]}
    cite: "Pub. 946 (2025), ch. 4, Which Convention Applies?, The mid-quarter convention"
    note: "'More than 40%' is tested exactly as 5 × last-quarter bases > 2 × total bases. Multiplying by a 40% rate would round to the cent and could give the wrong answer at the boundary. When no property was placed in service, both sides are zero and the test is false, so the half-year convention applies. The condition 'if the mid-month convention does not apply' needs no separate test: property using the mid-month convention (real property) is screened out of this tool by asset.screen."
```
