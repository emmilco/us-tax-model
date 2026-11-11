# Review record 47ab5176acee — transcription carloan

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "carloan",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "e0f9669f3e0fc0f37808925c1e84110723cac22d3fc42037cfb0ecff50a9fae5",
 "response_sha256": "4f6e9c6fa7233abf9a741c190424d170c77e851c8f6c562f20e3547eb779bd45",
 "scope": [
  "22(ii)",
  "22(iii)"
 ],
 "subjects": {
  "22(ii)": "703bd7f1a71a389ccdff1812866044de62b6b12918e22a949f9854d7567b93bd",
  "22(iii)": "59180e43d75b52fafb561996558ef7e752f5cbc5da74652ec245e8e2349ff60b"
 }
}
```

<!-- part block -->
#### Pass e0f9669f3e0f

| field | value |
| --- | --- |
| date | 2026-11-10 |
| review scope | lines 22(ii), 22(iii) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e0f9669f3e0fc0f37808925c1e84110723cac22d3fc42037cfb0ecff50a9fae5 |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | c9e64aed6e7ddc3384c129834d8ec7dfb47e294485a3839073bf2273910cc0fc |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 89e28e84a93d07f1be994e4f962a8667002aedddec4f6155e90d9d9391695a68 |
| receipt | .transcription/carloan.lines-ff3a1ab6edb2 |
| printed lines compared | 2 |
| agree / disagree / missing | 0 / 2 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 19, 20, 21, 22, 23 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 19, 20, 21, 22, 23 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: s2.amt, s2.other | s2 |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.gifts, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| shared page | household, person, s1a, sc, scveh |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: carloan.h_eligible
    printed: "(helper)"
    label: "The loan is a specified passenger vehicle loan (requirements 1 to 5, or the death or refinancing rules) and the vehicle is an applicable passenger vehicle"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.requirements, {const: true}]}
        - {op: test, eq: [carloan.vehicle, {const: true}]}
  - id: carloan.h_refi
    printed: "(helper)"
    label: "This loan is a refinancing of a loan that had QPVLI"
    type: Bool
    expr: {op: test, eq: [carloan.kind, {const: "refinanced"}]}
  - id: carloan.h_refi_partial
    printed: "(helper)"
    label: "Refinanced loan was itself only partly a specified passenger vehicle loan (its qualifying part is not determined by the supplied figures)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [carloan.kind, {const: "refinanced"}]}
        - {op: test, eq: [carloan.refi_whole, {const: false}]}
    note: "Prop. Reg. 1.163-16(d)(4) limits the new loan's SPVL amount to the refinanced loan's outstanding balance, which presupposes the refinanced loan was wholly an SPVL. Where it was only partly one, the interface supplies no figure for its qualifying part, so the lines refuse."
  - id: carloan.h_ii_exceeds
    printed: "(helper)"
    label: "Consistency check: the interest deducted on Schedule C is more than the total interest on this loan"
    type: Bool
    expr: {op: test, gt: [carloan.col_ii_input, carloan.interest]}
  - id: carloan.h_has_financed
    printed: "(helper)"
    label: "The loan financed an amount greater than zero"
    type: Bool
    expr: {op: test, gt: [carloan.financed, {const: 0}]}
  - id: carloan.h_nonq_net
    printed: "(helper)"
    label: "Non-SPVL indebtedness: the amounts not incurred for the purchase of the APV or customarily financed items, after the down payment is applied first against them"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.nonqualifying, take: carloan.down}
  - id: carloan.h_purchase_qual_mixed
    printed: "(helper)"
    label: "SPVL portion of a mixed purchase loan: the amount financed minus the non-SPVL indebtedness"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.financed, take: carloan.h_nonq_net}
  - id: carloan.h_purchase_qual
    printed: "(helper)"
    label: "SPVL portion of the indebtedness incurred for the purchase"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.mixed, {const: true}]}
          then: carloan.h_purchase_qual_mixed
        - guard: {op: test, eq: [carloan.mixed, {const: false}]}
          then: carloan.financed
  - id: carloan.h_refi_qual
    printed: "(helper)"
    label: "SPVL amount of a refinancing loan: limited to the outstanding balance of the refinanced loan as of the date of the refinancing"
    type: NonNegDollars
    expr: {op: smaller_of, of: [carloan.financed, carloan.refi_balance]}
  - id: carloan.h_qual
    printed: "(helper)"
    label: "Portion of this loan's indebtedness that is an SPVL"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [carloan.h_refi, {const: true}]}
          then: carloan.h_refi_qual
        - guard: {op: test, eq: [carloan.h_refi, {const: false}]}
          then: carloan.h_purchase_qual
  - id: carloan.h_net_interest
    printed: "(helper)"
    label: "Interest paid or accrued on the loan in 2025 that was not deducted on Schedule C"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.interest, take: carloan.col_ii_input}
  - id: carloan.h_ii_prorated
    printed: "(helper)"
    label: "QPVLI part of the interest deducted on Schedule C (interest allocated pro rata to the SPVL portion)"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.col_ii_input, part: carloan.h_qual, whole: carloan.financed, places: 9}
    note: "The pro rata allocation of interest (Prop. Reg. 1.163-16(d)(2)(iii)(A) and (d)(4)) gives a ratio of qualifying indebtedness to total indebtedness; no rounding is stated, so the ratio is kept to 9 decimal places (exactly 1 when the whole loan qualifies)."
  - id: carloan.h_iii_prorated
    printed: "(helper)"
    label: "QPVLI on the loan not deducted elsewhere (interest not deducted on Schedule C, allocated pro rata to the SPVL portion)"
    type: NonNegDollars
    expr: {op: prorate, amount: carloan.h_net_interest, part: carloan.h_qual, whole: carloan.financed, places: 9}
  - id: carloan.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: carloan.col_ii
    printed: "22(ii)"
    label: "Enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.h_has_financed, {const: true}]}
          then: carloan.h_ii_prorated
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [carloan.h_eligible, {const: true}]}
                - {op: test, eq: [carloan.h_has_financed, {const: true}]}
          then: carloan.h_zero
    refuses: [carloan.h_refi_partial, {when: carloan.h_ii_exceeds, when_known: true}]
    note: "Open: column (ii) asks for the QPVLI deducted elsewhere, and the interface supplies only the loan's interest deducted on Schedule C. For a loan only partly an SPVL, this transcription treats the Schedule C interest as allocated pro rata between the SPVL and non-SPVL portions, as interest payments are under Prop. Reg. 1.163-16(d)(2)(iii)(A), and counts only the SPVL share as QPVLI. A loan that is not an SPVL or whose vehicle is not an APV has no QPVLI, so the column is zero. Only Schedule C is in scope; Schedules E and F are not modeled."
  - id: carloan.col_iii
    printed: "22(iii)"
    label: "Enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [carloan.h_eligible, {const: true}]}
              - {op: test, eq: [carloan.h_has_financed, {const: true}]}
          then: carloan.h_iii_prorated
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [carloan.h_eligible, {const: true}]}
                - {op: test, eq: [carloan.h_has_financed, {const: true}]}
          then: carloan.h_zero
    refuses: [carloan.h_refi_partial, {when: carloan.h_ii_exceeds, when_known: true}]
    note: "Total QPVLI = interest x (SPVL indebtedness / amount financed). Column (iii) = (interest - Schedule C interest) x the same ratio, which equals total QPVLI minus column (ii) under the pro rata reading. The SPVL indebtedness is: the amount financed, less the non-qualifying amounts after the down payment is applied first against them, for a purchase loan or a loan taken over on a prior obligor's death; or the smaller of the amount financed and the refinanced balance for a refinancing. A zero amount financed is treated as having no QPVLI."
```
```
<!-- part section 22(ii) -->
22(ii) — QPVLI deducted elsewhere on your return (the qualifying part of the interest deducted on S
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"input": "carloan.col_ii_input"}}], "op": "choose"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "carloan.col_ii_input"}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.financed"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}}], "op": "choose"}}], "op": "choose"}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "carloan.financed"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: column (ii) asks for the QPVLI deducted elsewhere, and the interface supplies only the loan's interest deducted on Schedule C. For a loan only partly an SPVL, this transcription treats the Schedule C interest as allocated pro rata between the SPVL and non-SPVL portions, as interest payments are under Prop. Reg. 1.163-16(d)(2)(iii)(A), and counts only the SPVL share as QPVLI. A loan that is not an SPVL or whose vehicle is not an APV has no QPVLI, so the column is zero. Only Schedule C is in scope; Schedules E and F are not modeled.

Ruling: open
Reviewed in: pass e0f9669f3e0f

<!-- part section 22(iii) -->
22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"line": "22(ii)"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0}, {"input": "carloan.financed"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"from": {"input": "carloan.interest"}, "op": "subtract_floor0", "take": {"input": "carloan.col_ii_input"}}, "op": "prorate", "part": {"alternatives": [{"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.financed"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}}], "op": "choose"}}], "op": "choose"}, "places": 9, "whole": {"input": "carloan.financed"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "carloan.financed"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Total QPVLI = interest x (SPVL indebtedness / amount financed). Column (iii) = (interest - Schedule C interest) x the same ratio, which equals total QPVLI minus column (ii) under the pro rata reading. The SPVL indebtedness is: the amount financed, less the non-qualifying amounts after the down payment is applied first against them, for a purchase loan or a loan taken over on a prior obligor's death; or the smaller of the amount financed and the refinanced balance for a refinancing. A zero amount financed is treated as having no QPVLI.

Ruling: open
Reviewed in: pass e0f9669f3e0f

<!-- part gate 22(ii) -->
| 22(ii) | carloan.h_ii_exceeds, carloan.h_refi_partial | carloan.h_ii_exceeds, carloan.h_refi_partial |
<!-- part gate 22(iii) -->
| 22(iii) | carloan.h_ii_exceeds, carloan.h_refi_partial | carloan.h_ii_exceeds, carloan.h_refi_partial |
<!-- end -->
