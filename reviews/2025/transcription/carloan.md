# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5741a5e0508d52c071bac0e2154fcc5c153be0f16228474c9857a49dca119379 |
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
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"line": "22(ii)"}}], "op": "choose"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Second transcription's note: The instructions say to enter the total QPVLI paid or accrued minus column (ii), with no floor. Column (ii) is the QPVLI deducted elsewhere, so it should not exceed the QPVLI. The input, however, is the Schedule C interest on this loan, which could exceed the qualifying part. This transcription floors the result at zero.

Ruling: equivalent; project retained. Both subtract column (ii) from the qualified interest. The project asks column (ii), the interest deducted on Schedule C, only when the return has a Schedule C (carloan.col_ii is zero otherwise); the second reads the entry directly. Equal wherever the entry is asked; Schedules E and F remain refused.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 22(iii) | carloan.h_refi_nested | carloan.h_refi_nested |

## Raw second transcription

```yaml
```yaml
lines:
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero (no qualified passenger vehicle loan interest)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: carloan.h_eligible
    printed: "(helper)"
    label: "The loan meets the loan requirements and the vehicle is an applicable passenger vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}

  - id: carloan.h_is_refi
    printed: "(helper)"
    label: "This loan refinanced a specified passenger vehicle loan"
    type: Bool
    expr: {op: test, eq: [carloan.kind, {const: "refinanced"}]}

  - id: carloan.h_refi_nested
    printed: "(helper)"
    label: "The refinanced loan was itself only partly a specified passenger vehicle loan"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
        - {op: test, not: {op: test, eq: [carloan.refi_whole, {const: true}]}}
    note: "The IRS text limits the qualifying part of a refinancing loan to the outstanding balance of the refinanced loan. It does not say how to handle a refinanced loan that was itself only partly an SPVL. This case is refused rather than computed."

  - id: carloan.h_nonqualifying_debt
    printed: "(helper)"
    label: "Amounts that do not qualify, less any down payment, which is applied first against them"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}

  - id: carloan.h_mixed_qualifying
    printed: "(helper)"
    label: "Part of the indebtedness incurred for the purchase of the APV and items customarily financed with it (an SPVL)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_nonqualifying_debt}

  - id: carloan.h_mixed_interest
    printed: "(helper)"
    label: "Interest allocated pro rata to the SPVL part of the indebtedness"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.interest, part: carloan.h_mixed_qualifying, whole: carloan.financed, places: 6}
    note: "The text says interest is allocated 'on a pro rata basis' but states no rounding of the ratio. This transcription uses 6 decimal places. It assumes the amount financed is more than zero whenever the loan financed nonqualifying amounts."

  - id: carloan.h_refi_qualifying
    printed: "(helper)"
    label: "Amount of the new loan that is an SPVL, limited to the outstanding balance of the refinanced loan as of the date of the refinancing"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.financed, carloan.refi_balance]}

  - id: carloan.h_refi_interest
    printed: "(helper)"
    label: "Interest allocated pro rata to the SPVL part of the new loan"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.interest, part: carloan.h_refi_qualifying, whole: carloan.financed, places: 6}
    note: "The text says principal and interest are allocated pro rata but states no rounding of the ratio. This transcription uses 6 decimal places. When the amount financed is not more than the refinanced balance, the ratio is 1."

  - id: carloan.h_qpvli
    printed: "(helper)"
    label: "Qualified passenger vehicle loan interest paid or accrued on this loan during the taxable year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, not: {op: test, eq: [carloan.h_eligible, {const: true}]}}
          then: carloan.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.h_is_refi, {const: true}]}
          then: carloan.h_refi_interest
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_mixed_interest
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.interest
    refuses: [carloan.h_refi_nested]
    note: "A loan acquired by reason of a previous obligor's death ('death') is treated like an original loan: the requirements were met when the loan was originated, and the same allocation of nonqualifying amounts applies. For a refinancing loan, the qualifying amount is figured only under the refinanced-balance limit."

  - id: carloan.line22(iii)
    printed: "22(iii)"
    label: "Qualified passenger vehicle loan interest less the amount in column (ii)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.h_qpvli, take: carloan.col_ii_input}
    refuses: [carloan.h_refi_nested]
    note: "The instructions say to enter the total QPVLI paid or accrued minus column (ii), with no floor. Column (ii) is the QPVLI deducted elsewhere, so it should not exceed the QPVLI. The input, however, is the Schedule C interest on this loan, which could exceed the qualifying part. This transcription floors the result at zero."
```
```
