# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4e4108fe32cd75f163d71440faabdd5eefb5bd8127098be8dcca8048cfc2c8d4 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 34d956bec83ff11f47d845cd69d82c056896b202e58f119d8142fe5698a1259f |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cd458f24d1c949329c6a326dc5b045e301aaf00c64812cc29091f29995c51206 |
| printed lines compared | 2 |
| agree / disagree / missing | 0 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 23, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 23, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22, 23 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22, 23 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### 22(ii) — QPVLI deducted elsewhere on your return (the qualifying part of the interest deducted on S
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "carloan.col_ii_input"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "lt"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}], "op": "choose"}}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.refi_balance"}, {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.nonqualifying"}}], "op": "choose"}}], "op": "smaller_of"}}], "op": "choose"}, "places": 3, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 110, Schedule 1-A, Line 22: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)." fr-2025-24154 p. 23, proposed § 1.163-16(g)(1): "Independently deductible interest is limited to interest that is QPVLI ... and that is otherwise deductible by the taxpayer as a different type of interest"; (g)(2): the QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI". fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis", and (d)(4): "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis". The candidate enters the smaller of the whole Schedule C interest and the loan's QPVLI, so on a partly qualifying loan it treats the business-use interest as QPVLI first; the text allocates every payment of interest pro rata between the qualifying and nonqualifying parts and gives no ordering that puts the deducted interest in the qualifying part. It also asks column (ii) of every loan, and prorates refinancings and mixed loans with a three-place ratio. Triage executable-triage-v2 (triage/carloan.deepseek.json; 1,111 fixtures, 500 generated returns seed 20261026, 74 partial records): 114 of 151 agree; 34 candidate-unknown (17 on completed returns), 3 value. Value witnesses: stage12.car.mixed_sc_interest_prorated (ratio 0.8, Schedule C $106.00): project $84.80, candidate $106.00; classm.carloan.3 (ratio 0.256638, Schedule C $2,149.00): project $551.52, candidate $2,149.00 (all of it, against QPVLI $2,209.17); classm.carloan.2: project $0.00, candidate $1,268.00, column (ii) supplied without a Schedule C (not an interview record). The candidate-unknown are returns without a Schedule C where it still needs carloan.col_ii_input (representation, as in the Claude log). BUG-0175 check: the fix is right. The Schedule C interest is a share of the whole loan's interest, and (d)(2)(iii)(A)/(d)(4) spread every payment of interest pro rata over the qualifying and nonqualifying parts, so the QPVLI part of it is the same ratio times it; (g)(1) admits only that part to column (ii) (p. 23 Example 1: $400 of $1,000 deducted as business interest leaves $600 of QPVLI, pp. 23-24). The refinanced branch uses the (d)(4) ratio and an inherited loan the (d)(2)(iii) ratio, both the ratios that carloan.qpvli uses, and an ineligible loan has no QPVLI, so zero. Regression stage12.car.mixed_sc_interest_prorated (interest $424.00, loan $20,000.00, $4,000.00 nonqualifying, Schedule C $106.00): column (ii) $84.80, column (iii) $254.40 = 0.8 x ($424.00 - $106.00). Project stands.

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "lt"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}], "op": "choose"}}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.refi_balance"}, {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.nonqualifying"}}], "op": "choose"}}], "op": "smaller_of"}}], "op": "choose"}, "places": 3, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Ruling: model error; i1040gi p. 110, Line 22: "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)." fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis", and (d)(4): "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis"; fr-2025-24154 p. 21, (d)(2)(iii)(A): the allocation applies only "if a taxpayer incurs indebtedness described in both paragraphs (d)(2)(i) and (ii) of this section as part of the same transaction". The candidate prorates every loan by carloan.financed (zero when it is zero), so on a loan that financed only the vehicle it needs the amount financed, which the text does not; it inherits column (ii)'s min-not-prorate reading; and its three-place ratio is the register's third reading (amb.2025.carloan_ratio_places (chosen: ratio rounded half-up to six places; recorded alternatives: exact ratio, three places)). Triage executable-triage-v2 (triage/carloan.deepseek.json): 106 of 151 agree; 27 candidate-unknown (17 on completed returns), 18 value. Witnesses: stage12.car.basic (completed, carloan.mixed false) candidate unknown on carloan.financed, as in round 1; stage12.car.mixed_sc_interest_prorated project $254.40, candidate $233.20 and classm.carloan.3 project $1,654.54, candidate $60.17 (column (ii) not prorated); classm.f5695.6 (refinanced, ratio 43,108/60,468) project $6,996.46, candidate $6,997.38 and generated 317 (mixed) project $6,899.95, candidate $6,898.17 (three-place ratio, ambiguity). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 22(ii) | carloan.h_refi_bad | carloan.h_refi_bad |
| 22(iii) | carloan.h_refi_bad | carloan.h_refi_bad |

## Raw second transcription

```yaml
lines:
  - id: carloan.col_ii
    printed: "22(ii)"
    label: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)."
    type: NonNegDollars
    expr: {op: copy, from: carloan.h_col_ii_capped}
    refuses: [carloan.h_refi_bad]
  - id: carloan.col_iii
    printed: "22(iii)"
    label: "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.h_qpvli, take: carloan.col_ii}
    refuses: [carloan.h_refi_bad]
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: carloan.h_nonqual_after_down
    printed: "(helper)"
    label: "Nonqualifying purchase amounts after applying the down payment"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}
  - id: carloan.h_mixed_nonqual_debt
    printed: "(helper)"
    label: "Nonqualifying indebtedness after applying the down payment, only for a mixed loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_nonqual_after_down
        - guard: {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.h_zero
  - id: carloan.h_qual_debt_original
    printed: "(helper)"
    label: "Qualifying principal on an original or death-transferred loan"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_mixed_nonqual_debt}
  - id: carloan.h_refi_nonqual
    printed: "(helper)"
    label: "Nonqualifying amount financed by a refinancing"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.nonqualifying
        - guard: {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.h_zero
  - id: carloan.h_refi_after_nonqual
    printed: "(helper)"
    label: "Refinancing amount remaining after nonqualifying amounts"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_refi_nonqual}
  - id: carloan.h_refi_qual_debt
    printed: "(helper)"
    label: "Qualifying principal on a refinanced loan"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.h_refi_after_nonqual, carloan.refi_balance]}
  - id: carloan.h_qual_debt
    printed: "(helper)"
    label: "Qualifying principal on this loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.kind, {const: "original"}]}
          then: carloan.h_qual_debt_original
        - guard: {op: test, eq: [carloan.kind, {const: "death"}]}
          then: carloan.h_qual_debt_original
        - guard: {op: test, eq: [carloan.kind, {const: "refinanced"}]}
          then: carloan.h_refi_qual_debt
  - id: carloan.h_eligible
    printed: "(helper)"
    label: "Loan and vehicle meet the QPVLI requirements"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}
  - id: carloan.h_refi_bad
    printed: "(helper)"
    label: "The refinanced loan was not wholly qualifying, so its qualifying share is not supplied"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
        - {op: test, eq: [carloan.refi_whole, {const: false}]}
  - id: carloan.h_prorated
    printed: "(helper)"
    label: "Interest allocated to the qualifying principal"
    type: NonNegDollars
    expr:
      op: prorate
      amount: carloan.interest
      part: carloan.h_qual_debt
      whole: carloan.financed
      places: 3
    note: "The proposed regulations require a pro rata allocation but do not state a decimal precision; three decimal places were chosen."
  - id: carloan.h_qpvli_raw
    printed: "(helper)"
    label: "QPVLI before applying the eligibility gate"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.financed, {const: 0}]}
          then: carloan.h_zero
        - guard: {op: test, gt: [carloan.financed, {const: 0}]}
          then: carloan.h_prorated
  - id: carloan.h_qpvli
    printed: "(helper)"
    label: "Total QPVLI paid or accrued on this loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_eligible, {const: true}]}
          then: carloan.h_qpvli_raw
        - guard: {op: test, eq: [carloan.h_eligible, {const: false}]}
          then: carloan.h_zero
    refuses: [carloan.h_refi_bad]
    note: "If the refinanced loan was not wholly a qualifying vehicle loan, the share of the refinanced balance that was qualifying is not supplied; the line refuses instead of guessing."
  - id: carloan.h_col_ii_capped
    printed: "(helper)"
    label: "QPVLI deducted elsewhere, limited to total QPVLI"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.col_ii_input, carloan.h_qpvli]}
    refuses: [carloan.h_refi_bad]
```
