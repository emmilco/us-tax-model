# Review record bbcae8a5c1c4 — transcription ny_it201

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "ny_it201",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "438ddb6f569252434d9a81ff69948a0b8e8bed4bb63e60f7b63122a09081a39d",
 "response_sha256": "5d96c32d52240de72374a945bef1625eb05c151300ebbdaf9c3b68ff76d32c56",
 "scope": [
  "59",
  "81"
 ],
 "subjects": {
  "59": "193df1d3a43eb245378cbde9dcd2de252860e1ddbd678b3cf84db51dcc0c65a3",
  "81": "c3f27a0aa29fa51ebdca02373ce9c26da2735dd784f9d7338c16ac97443b16b4"
 }
}
```

<!-- part block -->
#### Pass 438ddb6f5692

| field | value |
| --- | --- |
| date | 2026-11-09 |
| review scope | lines 59, 81 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 438ddb6f569252434d9a81ff69948a0b8e8bed4bb63e60f7b63122a09081a39d |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 34f6a569fc6e2b3607f7585fd6eae1e1f0938556b870daca7a9ef604737929d6 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 91504d00ddeaa2f8bfaaac4b3b8c927968a47cd5d48e1bb8b7c9c115294e3531 |
| receipt | .transcription/ny_it201.lines-24661e922c03 |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 9, 18, 19, 22, 23 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 9, 18, 19, 22, 23 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_rs, ny_tcw, ny_tcw_first |
| named lines: f1040.line11a, f1040.line27a, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line6b, f1040.line7a | f1040 |
| named lines: s1.line1, s1.line26, s1.line2a, s1.line3 | s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: ny_it201.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}

  - id: ny_it201.h_sut_owed
    printed: "(helper)"
    label: "Sales and use tax from the sales and use tax chart (when you owe sales or use tax)"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.sut.chart}
    refuses: [ny_it201.ask.use_tax_st141, ny_it201.ask.abode_part_year]
    note: "Form ST-141 cases are refused: an item of $1,000 or more, business, rental or royalty purchases, or choosing the exact calculation. Part-year abode cases are refused: the chart amount times months of abode divided by 12. The interface has no input for the ST-141 amount or the number of months. The refusal sits on this branch only, so a filer who owes no use tax still gets 0."

  - id: ny_it201.line59
    printed: "59"
    label: "Sales or use tax (do not leave blank)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: true}]}
          then: ny_it201.h_sut_owed
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: false}]}
          then: ny_it201.h_zero
    note: "If you do not owe any sales or use tax, enter 0. Otherwise enter the amount from the sales and use tax chart (by federal AGI, line 19)."

  - id: ny_it201.h_est_safe
    printed: "(helper)"
    label: "2025 prepayments equal at least 100% (110% if 2024 NY AGI was over $150,000/$75,000) of 2024 New York income tax"
    type: Bool
    expr: {op: test, ge: [ny_it201.prepayments, ny_it201.safe_harbor]}

  - id: ny_it201.h_est_tax_shown
    printed: "(helper)"
    label: "Income tax shown on your 2025 return"
    type: Dollars
    expr: {op: sum, of: [ny_it201.line46, ny_it201.line58]}
    note: "The text does not define 'income tax shown on your 2025 return'. Chosen reading: total New York State taxes (line 46) plus total NYC/Yonkers taxes and MCTMT (line 58). Sales or use tax and voluntary contributions are excluded, and refundable credits are not subtracted."

  - id: ny_it201.h_est_tenth
    printed: "(helper)"
    label: "10% of the income tax shown on your 2025 return"
    type: Dollars
    expr: {op: multiply_rate, amount: ny_it201.h_est_tax_shown, rate: {param: ny.est.share}}

  - id: ny_it201.h_est_due_test
    printed: "(helper)"
    label: "Line 80 is $300 or more and represents more than 10% of the income tax shown on your 2025 return"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [ny_it201.tax_due, {param: ny.est.min_due}]}
        - {op: test, gt: [ny_it201.tax_due, ny_it201.h_est_tenth]}
    note: "Line 80 is read as the amount owed before any estimated tax penalty (ny_it201.tax_due)."

  - id: ny_it201.h_est_may_owe
    printed: "(helper)"
    label: "You may owe an estimated tax penalty"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_est_safe, {const: false}]}
        - op: test
          any:
            - {op: test, eq: [ny_it201.h_est_due_test, {const: true}]}
            - {op: test, eq: [ny_it201.ask.est_late, {const: true}]}

  - id: ny_it201.h_est_penalty_refused
    printed: "(helper)"
    label: "Estimated tax penalty (Form IT-2105.9)"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.h_zero}
    refuses: [ny_it201.h_est_may_owe]
    note: "The penalty amount is figured on Form IT-2105.9, which is not supplied. Where a penalty may be owed, the tool refuses and names Form IT-2105.9. It does not compute or assume an amount."

  - id: ny_it201.line81
    printed: "81"
    label: "Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_est_may_owe, {const: true}]}
          then: ny_it201.h_est_penalty_refused
        - guard: {op: test, eq: [ny_it201.h_est_may_owe, {const: false}]}
          then: ny_it201.h_zero
    note: "Chosen reading of the open text: there is no penalty when 2025 prepayments meet the prior-year safe harbor, or when neither 'may owe' condition holds. The two conditions are line 80 at least $300 and more than 10% of the tax, or an installment underpaid or paid late. Otherwise the line is refused for Form IT-2105.9."
```
```
<!-- part section 59 -->
59 — Sales or use tax (do not leave blank)
Status: **AGREE**
Reviewed in: pass 438ddb6f5692

<!-- part section 81 -->
81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"param": "ny.est.min_due"}, {"line": "(80)"}], "test": "le"}, {"args": [{"amount": {"of": [{"line": "46"}, {"line": "58"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "ny.est.share"}}, {"line": "(80)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.est_late)"}], "test": "eq"}], "test": "any"}, {"args": [{"line": "(81) (ny_it201.prepayments)"}, {"line": "(81) (ny_it201.safe_harbor)"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"line": "(80)"}, {"amount": {"of": [{"line": "46"}, {"line": "58"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "ny.est.share"}}], "test": "le"}, {"args": [{"line": "(80)"}, {"param": "ny.est.min_due"}], "test": "lt"}], "test": "any"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.est_late)"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "(81) (ny_it201.safe_harbor)"}, {"line": "(81) (ny_it201.prepayments)"}], "test": "le"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Chosen reading of the open text: there is no penalty when 2025 prepayments meet the prior-year safe harbor, or when neither 'may owe' condition holds. The two conditions are line 80 at least $300 and more than 10% of the tax, or an installment underpaid or paid late. Otherwise the line is refused for Form IT-2105.9.

Ruling: open
Reviewed in: pass 438ddb6f5692

<!-- part gate 59 -->
| 59 | ny_it201.ask.abode_part_year, ny_it201.ask.use_tax_st141 | ny_it201.ask.abode_part_year, ny_it201.ask.use_tax_st141 |
<!-- part gate 81 -->
| 81 | ny_it201.h_est_may_owe | ny_it201.h_est_may_owe |
<!-- end -->
