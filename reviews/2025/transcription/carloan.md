# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.col_ii_input"}}, {"guard": {"args": [{"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"input": "carloan.col_ii_input"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.financed"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}}], "op": "choose"}, "places": 9, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Only interest deducted on Schedule C is within scope (the interface gives no Schedule E or F amount). Interest on a loan that is not QPVLI is not QPVLI deducted elsewhere, so column (ii) is zero for such a loan.

Ruling: ambiguity; amb.2025.carloan_ratio_places (chosen: ratio rounded half-up to six places; recorded alternatives: exact ratio, three places) on the value difference; representation on the rest. i1040gi p. 110, Schedule 1-A, Line 22: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)." fr-2025-24154 p. 23, proposed § 1.163-16(g)(1): "Independently deductible interest is limited to interest that is QPVLI ... and that is otherwise deductible by the taxpayer as a different type of interest"; (g)(2): the QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI". fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis", and (d)(4): "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis". Triage executable-triage-v2 (triage/carloan.json; 1,111 fixtures, 500 generated returns seed 20261026, 74 partial records): 128 of 151 comparisons agree; 21 candidate-unknown (13 on completed returns), 2 value. The candidate reads the source as the project does after BUG-0175: zero unless the loan and vehicle qualify, the Schedule C interest as reported on a loan that financed nothing else, and otherwise the Schedule C interest prorated by the loan's qualifying ratio (refinancing: smaller of the refinanced balance and the loan, over the loan). Differences: (1) value, classm.carloan.3 (refinanced; $8,596.00 interest, $2,149.00 Schedule C, $3,151.00 balance over a $12,278.00 loan): project $551.52 (ratio 0.256638), candidate $551.51 (ratio to nine places, 0.256637889) -- the register's exact-ratio alternative. (2) value, classm.carloan.2 (death; $1,268.00 entered on carloan.col_ii_input with no Schedule C): project $0.00, candidate $1,268.00; the interview asks carloan.col_ii_input only when s1.has_sc, so the record is not one the interview produces (representation). (3) The 21 candidate-unknown (stage12.car.basic, stage12.car.two_loans_cap, classm.tipjob.1) are returns without a Schedule C where the candidate still needs column (ii); Schedules E and F are refused by scope.schedule1, so without a Schedule C the QPVLI deducted elsewhere is zero, and the source itself asks the question of every filer (representation, as ruled in round 1). The candidate's extra refusal when the Schedule C interest exceeds the loan's interest (carloan.h_bus_over) fires on no record. BUG-0175 check: the fix is right. The Schedule C interest is a share of the whole loan's interest, and (d)(2)(iii)(A)/(d)(4) spread every payment of interest pro rata over the qualifying and nonqualifying parts, so the QPVLI part of it is the same ratio times it; (g)(1) admits only that part to column (ii) (p. 23 Example 1: $400 of $1,000 deducted as business interest leaves $600 of QPVLI, pp. 23-24). The refinanced branch uses the (d)(4) ratio and an inherited loan the (d)(2)(iii) ratio, both the ratios that carloan.qpvli uses, and an ineligible loan has no QPVLI, so zero. Regression stage12.car.mixed_sc_interest_prorated (interest $424.00, loan $20,000.00, $4,000.00 nonqualifying, Schedule C $106.00): column (ii) $84.80, column (iii) $254.40 = 0.8 x ($424.00 - $106.00). Project stands.

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}], "test": "any"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"input": "carloan.financed"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}}], "op": "choose"}, "places": 9, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Second transcription's note: The floor at zero is only a guard. With the consistency check passed, column (ii) cannot exceed the QPVLI, because both use the same pro rata ratio. The VIN (column (i)) and the requirement to report it are not modeled.

Ruling: ambiguity; amb.2025.carloan_ratio_places (chosen: ratio rounded half-up to six places; recorded alternatives: exact ratio, three places) on the value difference; representation on the rest. i1040gi p. 110, Line 22: "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)." fr-2025-24154 p. 23, proposed § 1.163-16(g)(1): "Independently deductible interest is limited to interest that is QPVLI ... and that is otherwise deductible by the taxpayer as a different type of interest"; (g)(2): the QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI". fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis", and (d)(4): "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis". Triage executable-triage-v2 (triage/carloan.json): 131 of 151 comparisons agree; 18 candidate-unknown (13 on completed returns), 2 value. Both subtract column (ii) from the loan's prorated QPVLI. classm.carloan.3: project $1,654.54 ($2,206.06 - $551.52), candidate $1,654.55 ($2,206.06 - $551.51), the nine-place ratio on column (ii) (register alternative). classm.carloan.2: project $5,073.00, candidate $3,805.00, only through the column (ii) amount supplied without a Schedule C (a record the interview does not produce). The candidate-unknown are column (ii)'s, on returns without a Schedule C (representation, as on 22(ii)). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 22(ii) | carloan.h_bus_over, carloan.h_refi_partial | carloan.h_bus_over, carloan.h_refi_partial |
| 22(iii) | carloan.h_bus_over, carloan.h_refi_partial | carloan.h_bus_over, carloan.h_refi_partial |

## Raw second transcription

```yaml
```yaml
lines:
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: carloan.h_eligible
    printed: "(helper)"
    label: "The loan meets the loan requirements (requirements 1 through 5, or the change in obligor by reason of a previous obligor's death) and the vehicle is an applicable passenger vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}
  - id: carloan.h_is_refi
    printed: "(helper)"
    label: "Refinanced loan: your prior loan that had QPVLI is later refinanced"
    type: Bool
    expr: {op: test, eq: [carloan.kind, {const: "refinanced"}]}
  - id: carloan.h_refi_partial
    printed: "(helper)"
    label: "Refinanced loan whose refinanced loan was not wholly a qualifying vehicle loan"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.h_eligible, {const: true}]}
        - {op: test, eq: [carloan.h_is_refi, {const: true}]}
        - {op: test, eq: [carloan.refi_whole, {const: false}]}
    note: "The text limits the refinanced amount to the outstanding balance of the refinanced loan, but does not say how to find the qualifying part of a refinanced loan that was itself only partly qualifying. The tool refuses that case (col_ii and col_iii list this line under refuses) instead of computing it."
  - id: carloan.h_nonq_net
    printed: "(helper)"
    label: "Indebtedness not incurred for the purchase of the APV, after applying any down payment first against negative equity and other nonqualifying amounts"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}
  - id: carloan.h_qual_debt_purchase
    printed: "(helper)"
    label: "Portion of the indebtedness incurred for the purchase of the APV and items customarily financed with it and directly related to it"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_nonq_net}
  - id: carloan.h_qual_debt_refi
    printed: "(helper)"
    label: "The loan amount is limited to the outstanding balance of the refinanced loan as of the date of the refinancing"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.financed, carloan.refi_balance]}
  - id: carloan.h_qual_debt
    printed: "(helper)"
    label: "Amount of the indebtedness that is a specified passenger vehicle loan"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_is_refi, {const: true}]}
          then: carloan.h_qual_debt_refi
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_qual_debt_purchase
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.financed
    note: "For a refinanced loan only the balance limit is applied; cash proceeds on refinancing are the excess over the refinanced balance (Example 3). The mixed-financing allocation is applied to original-purchase and death-of-obligor loans."
  - id: carloan.h_int_alloc
    printed: "(helper)"
    label: "Interest allocated pro rata to the portion of the indebtedness that is a specified passenger vehicle loan"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.interest, part: carloan.h_qual_debt, whole: carloan.financed, places: 9}
    note: "The proposed regulations say only to allocate interest 'on a pro rata basis' and give no rounding for the ratio. The ratio is kept to 9 decimal places, which is close to exact."
  - id: carloan.h_bus_alloc
    printed: "(helper)"
    label: "Schedule C interest allocated pro rata to the portion of the indebtedness that is a specified passenger vehicle loan"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.col_ii_input, part: carloan.h_qual_debt, whole: carloan.financed, places: 9}
    note: "The text does not say how interest deducted on Schedule C splits between the qualifying and nonqualifying parts of a mixed or refinanced loan. The reading chosen applies the same pro rata allocation used for payments of interest."
  - id: carloan.h_bus_over
    printed: "(helper)"
    label: "Consistency check: the interest deducted on Schedule C is more than the total interest on this loan"
    type: Bool
    expr: {op: test, gt: [carloan.col_ii_input, carloan.interest]}
  - id: carloan.h_int_qual
    printed: "(helper)"
    label: "QPVLI paid or accrued on this loan (before eligibility)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.interest
        - guard:
            op: test
            any:
              - {op: test, eq: [carloan.h_is_refi, {const: true}]}
              - {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_int_alloc
  - id: carloan.h_bus_qual
    printed: "(helper)"
    label: "QPVLI deducted on Schedule C (before eligibility)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_is_refi, {const: false}]}
              - {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.col_ii_input
        - guard:
            op: test
            any:
              - {op: test, eq: [carloan.h_is_refi, {const: true}]}
              - {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_bus_alloc
  - id: carloan.h_qpvli
    printed: "(helper)"
    label: "Total amount of the QPVLI paid or accrued on the loan during the taxable year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_eligible, {const: true}]}
          then: carloan.h_int_qual
        - guard: {op: test, eq: [carloan.h_eligible, {const: false}]}
          then: carloan.h_zero
  - id: carloan.col_ii
    printed: "22(ii)"
    label: "Enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_eligible, {const: true}]}
          then: carloan.h_bus_qual
        - guard: {op: test, eq: [carloan.h_eligible, {const: false}]}
          then: carloan.h_zero
    refuses: [carloan.h_refi_partial, {when: carloan.h_bus_over, when_known: true}]
    note: "Only interest deducted on Schedule C is within scope (the interface gives no Schedule E or F amount). Interest on a loan that is not QPVLI is not QPVLI deducted elsewhere, so column (ii) is zero for such a loan."
  - id: carloan.col_iii
    printed: "22(iii)"
    label: "Enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.h_qpvli, take: carloan.col_ii}
    refuses: [carloan.h_refi_partial, {when: carloan.h_bus_over, when_known: true}]
    note: "The floor at zero is only a guard. With the consistency check passed, column (ii) cannot exceed the QPVLI, because both use the same pro rata ratio. The VIN (column (i)) and the requirement to report it are not modeled."
```
```
