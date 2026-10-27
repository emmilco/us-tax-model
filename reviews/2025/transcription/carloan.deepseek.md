# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 081898376be21e650078f05608b78803881a3c2b5b9c7a3972c50682829a905d |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 751108ec4c41850b335669f75e9972b5db8bc92528d64f610f2457fe4a31e888 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.refi_whole"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "carloan.refi_whole"}], "test": "eq"}, "then": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}}], "op": "choose"}, "places": 6, "whole": {"of": [{"const": 1}, {"input": "carloan.financed"}], "op": "larger_of"}}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: If the refinanced loan was only partly a qualifying vehicle loan, the interface does not supply the qualifying portion of the refinanced balance; the line refuses rather than guessing the allocation. For a wholly qualifying refinancing, the qualifying principal is the smaller of the new amount financed and the outstanding balance of the refinanced loan. For an original or death-transferred loan, the down payment is applied first against nonqualifying amounts. The pro rata interest allocation is rounded to six decimal places because the proposed regulations do not state a precision.

Ruling: model error; fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): only "if a taxpayer incurs indebtedness described in both paragraphs (d)(2)(i) and (ii) of this section as part of the same transaction, the indebtedness must be allocated". The candidate never reads carloan.mixed and prorates every original loan by carloan.financed, carloan.down and carloan.nonqualifying, so on a loan that financed only the vehicle it requires the amount financed, which the text does not need (all interest on such a loan is QPVLI). Triage executable-triage-v1 (triage/carloan.deepseek.json): 102 of 141 comparisons agree; 32 candidate-unknown records are interview-produced loans with carloan.mixed false and no amount financed (stage12.car.basic, stage12.car.two_loans_cap); the value differences supply allocation amounts with carloan.mixed false (classm.f5695.6: $3,527.00 against $1,037.10) or column (ii) without a Schedule C (classm.carloan.4, as in the Claude log, where that difference alone is representation). The 4 project-unknown records withhold carloan.mixed, which the project asks before any allocation amount. Column (ii) handling is as ruled in the Claude log.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 22(iii) | carloan.h_refi_partial | carloan.h_refi_partial |

## Raw second transcription

```yaml
lines:
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: carloan.h_one_cent
    printed: "(helper)"
    label: "One cent"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: carloan.h_eligible
    printed: "(helper)"
    label: "Loan meets the requirements and the vehicle is an applicable passenger vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}
  - id: carloan.h_nonqual_after_down
    printed: "(helper)"
    label: "Nonqualifying amount remaining after applying the down payment"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}
  - id: carloan.h_qp_original
    printed: "(helper)"
    label: "Qualifying principal for an original or death-transferred loan"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_nonqual_after_down}
  - id: carloan.h_qp_refi_limit
    printed: "(helper)"
    label: "Refinanced loan amount limited to the outstanding balance of the refinanced loan"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.financed, carloan.refi_balance]}
  - id: carloan.h_qp_refi
    printed: "(helper)"
    label: "Qualifying principal for a refinanced loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.refi_whole, {const: true}]}
          then: carloan.h_qp_refi_limit
        - guard: {op: test, eq: [carloan.refi_whole, {const: false}]}
          then: carloan.h_zero
  - id: carloan.h_qp
    printed: "(helper)"
    label: "Qualifying principal of the loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.kind, {const: "refinanced"}]}
          then: carloan.h_qp_refi
        - guard: {op: test, ne: [carloan.kind, {const: "refinanced"}]}
          then: carloan.h_qp_original
  - id: carloan.h_financed_safe
    printed: "(helper)"
    label: "Amount financed, not less than one cent, to avoid division by zero"
    type: NonNegDollars
    expr: {op: larger_of, of: [carloan.financed, carloan.h_one_cent]}
  - id: carloan.h_qpvli_prorated
    printed: "(helper)"
    label: "Interest allocated pro rata to the qualifying principal"
    type: NonNegDollars
    expr:
      op: prorate
      amount: carloan.interest
      part: carloan.h_qp
      whole: carloan.h_financed_safe
      places: 6
  - id: carloan.h_qpvli_after_colii
    printed: "(helper)"
    label: "QPVLI after subtracting the amount deducted elsewhere"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.h_qpvli_prorated, take: carloan.col_ii_input}
  - id: carloan.h_refi_partial
    printed: "(helper)"
    label: "Eligible refinanced loan where the loan refinanced was only partly a qualifying vehicle loan"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.h_eligible, {const: true}]}
        - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
        - {op: test, eq: [carloan.refi_whole, {const: false}]}
  - id: carloan.col_iii
    printed: "22(iii)"
    label: "Enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_eligible, {const: true}]}
          then: carloan.h_qpvli_after_colii
        - guard: {op: test, eq: [carloan.h_eligible, {const: false}]}
          then: carloan.h_zero
    refuses: [carloan.h_refi_partial]
    note: "If the refinanced loan was only partly a qualifying vehicle loan, the interface does not supply the qualifying portion of the refinanced balance; the line refuses rather than guessing the allocation. For a wholly qualifying refinancing, the qualifying principal is the smaller of the new amount financed and the outstanding balance of the refinanced loan. For an original or death-transferred loan, the down payment is applied first against nonqualifying amounts. The pro rata interest allocation is rounded to six decimal places because the proposed regulations do not state a precision."
```
