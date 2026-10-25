# Render comparison — mq

The rendered English of every printed line of `Mid-quarter convention test for property placed in service in 2025` (`rendered/2025/mq.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f655a770540ca468631c88415c0ec70833874d0aa9f3e39e9b0aa6f0c11b9e12 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 86bffe68cb283040dd41dc7e6fa521e2be2eb6bf380631710c0ccacb172dcca2 |
| lines judged | 7 |
| match / mismatch / unclear / missing | 5 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| p946 | For use in preparing 2025 returns | 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### q4 — Depreciable bases of property placed in service October to December 2025
Status: **MISMATCH**

Restated: Add person.mq_q4 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS test uses the total depreciable bases of MACRS property placed in service during the last 3 months, excluding nonresidential real property, residential rental property, railroad grading/tunnel bore, property placed in service and disposed of in the same year, and non-MACRS property; the helper merely adds person.mq_q4 and does not apply those exclusions or the personal-use basis reduction.

Ruling: open

### total — Depreciable bases of all property placed in service in 2025
Status: **MISMATCH**

Restated: Add person.mq_total over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS denominator is the total depreciable bases of all MACRS property placed in service during the entire year, with the same exclusions and personal-use reduction; the helper adds person.mq_total without those limitations.

Ruling: open

### five — Five
Status: **MATCH**

Model: Entering 5 is a correct scaling for the more-than-40% test when paired with 2 (5×Q4 > 2×total is equivalent to Q4 > 40% of total).

### two — Two
Status: **MATCH**

Model: Entering 2 is a correct scaling for the more-than-40% test when paired with 5 (5×Q4 > 2×total is equivalent to Q4 > 40% of total).

### q4x5 — Five times the October to December bases
Status: **MATCH**

Model: Multiplying the October-December bases by 5 gives the left side of the equivalent comparison 5×Q4 > 2×total for the more-than-40% test.

### totalx2 — Two times all 2025 bases
Status: **MATCH**

Model: Multiplying all 2025 bases by 2 gives the right side of the equivalent comparison 5×Q4 > 2×total for the more-than-40% test.

### applies — The mid-quarter convention applies: the October to December bases are more than 40% of all
Status: **MATCH**

Model: The strict comparison 5×Q4 > 2×total is equivalent to the IRS requirement that the last-3-month bases be more than 40% of all-year bases.

## Raw response

```yaml
lines:
  - key: "q4"
    status: MISMATCH
    reason: "The IRS test uses the total depreciable bases of MACRS property placed in service during the last 3 months, excluding nonresidential real property, residential rental property, railroad grading/tunnel bore, property placed in service and disposed of in the same year, and non-MACRS property; the helper merely adds person.mq_q4 and does not apply those exclusions or the personal-use basis reduction."
  - key: "total"
    status: MISMATCH
    reason: "The IRS denominator is the total depreciable bases of all MACRS property placed in service during the entire year, with the same exclusions and personal-use reduction; the helper adds person.mq_total without those limitations."
  - key: "five"
    status: MATCH
    reason: "Entering 5 is a correct scaling for the more-than-40% test when paired with 2 (5×Q4 > 2×total is equivalent to Q4 > 40% of total)."
  - key: "two"
    status: MATCH
    reason: "Entering 2 is a correct scaling for the more-than-40% test when paired with 5 (5×Q4 > 2×total is equivalent to Q4 > 40% of total)."
  - key: "q4x5"
    status: MATCH
    reason: "Multiplying the October-December bases by 5 gives the left side of the equivalent comparison 5×Q4 > 2×total for the more-than-40% test."
  - key: "totalx2"
    status: MATCH
    reason: "Multiplying all 2025 bases by 2 gives the right side of the equivalent comparison 5×Q4 > 2×total for the more-than-40% test."
  - key: "applies"
    status: MATCH
    reason: "The strict comparison 5×Q4 > 2×total is equivalent to the IRS requirement that the last-3-month bases be more than 40% of all-year bases."
```
