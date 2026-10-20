# Transcription agreement — mq

Second transcription of `Mid-quarter convention test for property placed in service in 2025` by an isolated model (spec 6.5), compared line by line with `forms/2025/mq.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | eac391d4193d23a7e6d221377ff4cb7743d4d8e874e8cbb07b333a49963869cc |
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
```yaml
lines:
  - id: mq.h_q4
    printed: "(helper)"
    label: "Total depreciable bases of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_q4}
    note: "Pub. 946 compares bases over all MACRS property placed in service in the year. The text does not say whether the test is per business or per return. Chosen reading: total across every person's Schedules C, using the per-person mq_q4 totals, which already roll up assets and vehicles. The Caution says the basis reflects the section 179 reduction and excludes personal-use basis but not the special allowance. The exclusions (real property, railroad grading or tunnel bore, property disposed of in the same year, non-MACRS property) are taken as already reflected in the per-entry mq_q4 basis."
  - id: mq.h_total
    printed: "(helper)"
    label: "Total depreciable bases of all MACRS property placed in service during the entire year"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.mq_total}
  - id: mq.h_five
    printed: "(helper)"
    label: "Five"
    type: Count
    expr: {op: param, ref: sc.count5}
  - id: mq.h_two
    printed: "(helper)"
    label: "Two"
    type: Count
    expr: {op: param, ref: sc.count2}
  - id: mq.h_q4x5
    printed: "(helper)"
    label: "Fourth-quarter bases times 5"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_q4, count: mq.h_five}
  - id: mq.h_totalx2
    printed: "(helper)"
    label: "All-year bases times 2"
    type: NonNegDollars
    expr: {op: multiply_count, amount: mq.h_total, count: mq.h_two}
  - id: mq.applies
    printed: "(helper)"
    label: "Use the mid-quarter convention if the total depreciable bases of MACRS property placed in service during the last 3 months of the tax year are more than 40% of the total depreciable bases of all MACRS property placed in service during the entire year"
    type: Bool
    expr: {op: test, gt: [mq.h_q4x5, mq.h_totalx2]}
    note: "'More than 40%' is written as Q4 × 5 > total × 2. This is the same comparison done exactly in cents, with no rounding of a 40% product. 'More than' is read as strict, so exactly 40% does not trigger the convention. With no 2025 property, both sides are zero and the test is false, so the half-year convention applies."
```
```
