# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 0099469aa8a176b6e45be6d6d348fd51ffa79d040da5d64b4f2e454dc23aa972 |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3d1839a5961d586ed8ea1688552d168314cadad6f4df5befd5d12ad3cb9d56e2 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 751108ec4c41850b335669f75e9972b5db8bc92528d64f610f2457fe4a31e888 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 242f7244bf2433fd7b9d62a477efcd1831165cee975a648155aba2c673a2494a |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"line": "22(ii)"}}], "op": "choose"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"of": [{"line": "22(ii)"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}}
```

Ruling: representation; i1040gi p. 110, Schedule 1-A line 22: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)." Schedules E and F are refused by scope.schedule1, so within scope column (ii) is nonzero only with a Schedule C; the project asks carloan.col_ii_input then (s1.has_sc) and uses zero otherwise, while the candidate asks it of every loan, which the text also permits. Triage executable-triage-v1 (triage/carloan.json): 111 of 141 comparisons agree; the 28 candidate-unknown records are returns without a Schedule C, where the interview does not ask column (ii); the 2 value differences (classm.carloan.4, classm.s179.3) supply carloan.col_ii_input with no Schedule C, a record the interview cannot produce. Column (iii) agrees on every reachable return; project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 22(iii) | carloan.h_financed_zero, carloan.h_ii_over, carloan.h_refi_nested | carloan.h_financed_zero, carloan.h_ii_over, carloan.h_refi_nested |

## Raw second transcription

```yaml
```yaml
lines:
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero (no qualified passenger vehicle loan interest)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: carloan.h_eligible
    printed: "(helper)"
    label: "The loan is a specified passenger vehicle loan (originated after December 31, 2024, used to purchase an applicable passenger vehicle for personal use, secured by a first lien, not related-party) and the vehicle is an applicable passenger vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}

  - id: carloan.h_refi_nested
    printed: "(helper)"
    label: "Refinanced loan whose refinanced loan was not itself wholly a specified passenger vehicle loan"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
        - {op: test, eq: [carloan.refi_whole, {const: false}]}
    note: "The instructions and proposed regulation 1.163-16(d)(4) limit a refinancing to the outstanding balance of the refinanced loan. They do not say how to treat a refinanced loan that was itself only partly a specified passenger vehicle loan, so the tool refuses that case."

  - id: carloan.h_financed_zero
    printed: "(helper)"
    label: "Consistency check: the amount financed is zero, so no pro rata allocation can be made"
    type: Bool
    expr: {op: test, eq: [carloan.financed, {const: 0}]}

  - id: carloan.h_nonq_debt
    printed: "(helper)"
    label: "Indebtedness not incurred for the purchase of the APV (non-qualifying amounts after the down payment is applied first against them)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}

  - id: carloan.h_mixed_part
    printed: "(helper)"
    label: "Portion of the indebtedness incurred for the purchase of the APV and items customarily financed with it (the SPVL portion)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_nonq_debt}

  - id: carloan.h_mixed_interest
    printed: "(helper)"
    label: "Interest allocated pro rata to the SPVL portion of a loan that also financed non-qualifying amounts"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.interest, part: carloan.h_mixed_part, whole: carloan.financed, places: 9}
    refuses:
      - {when: carloan.h_financed_zero, when_known: true}
    note: "Proposed regulation 1.163-16(d)(2)(iii)(A) allocates interest 'on a pro rata basis' and states no rounding of the ratio. Chose to round the ratio to 9 decimal places, the maximum the atom allows."

  - id: carloan.h_refi_part
    printed: "(helper)"
    label: "Amount of the new loan that is an SPVL, limited to the outstanding balance of the refinanced loan on the date of refinancing"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.refi_balance, carloan.financed]}

  - id: carloan.h_refi_interest
    printed: "(helper)"
    label: "Interest on a refinanced loan allocated pro rata to the refinanced amount"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.interest, part: carloan.h_refi_part, whole: carloan.financed, places: 9}
    refuses:
      - carloan.h_refi_nested
      - {when: carloan.h_financed_zero, when_known: true}
    note: "For a refinanced loan, the balance limit is applied in place of the mixed-purpose allocation, because any cash-out or other excess is already excluded by the limit. Ratio rounding is not stated; chose 9 places."

  - id: carloan.h_qpvli
    printed: "(helper)"
    label: "Total qualified passenger vehicle loan interest paid or accrued on this loan during the taxable year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_eligible, {const: false}]}
          then: carloan.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
          then: carloan.h_refi_interest
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, ne: [carloan.kind, {const: "refinanced"}]}
              - {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_mixed_interest
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, ne: [carloan.kind, {const: "refinanced"}]}
              - {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.interest
    note: "A loan acquired by reason of a previous obligor's death ('death') is treated like an original loan. Its qualification at origination is covered by the requirements input."

  - id: carloan.h_ii_over
    printed: "(helper)"
    label: "Consistency check: the interest deducted on Schedule C is more than the total interest on this loan"
    type: Bool
    expr: {op: test, gt: [carloan.col_ii_input, carloan.interest]}

  - id: carloan.h_col_ii
    printed: "(helper)"
    label: "Amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.col_ii_input, carloan.h_qpvli]}
    refuses:
      - {when: carloan.h_ii_over, when_known: true}
    note: "Column (ii) is the QPVLI deducted elsewhere, but the input is the loan's interest deducted on Schedule C. The text does not say how that amount is split between qualifying and non-qualifying debt. Chose to treat it as QPVLI up to the QPVLI total."

  - id: carloan.col_iii
    printed: "22(iii)"
    label: "Enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.h_qpvli, take: carloan.h_col_ii}
```
```
