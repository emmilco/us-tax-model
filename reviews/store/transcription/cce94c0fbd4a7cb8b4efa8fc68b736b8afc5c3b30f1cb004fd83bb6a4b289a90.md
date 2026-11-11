# Review record cce94c0fbd4a — transcription ny_it201

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
 "prompt_sha256": "de6745da83907beaa75df82fbdfe18b8aed212f826e5b0a5ecc0907a59875d20",
 "response_sha256": "fad30a8b2a61147f4a61a3dd522645fa9f1e91c58ec8045f24036be01b448c23",
 "scope": [
  "1",
  "20",
  "21",
  "22",
  "23",
  "25",
  "28",
  "30",
  "31",
  "41",
  "45",
  "51",
  "59"
 ],
 "subjects": {
  "1": "b69e7f8bf90a93c2298f2f5c2e75f838dd34566f817988cae5a7a87213bc8cd3",
  "20": "a70fd352cffd469dd02216e53f6030c4c592d7097b582436693dbacd4607d484",
  "21": "c452cb7f9ef191f09f292f3e97b9afa1bc936efb8bba7524856454dd236f0593",
  "22": "52b6c31794f0fdf5e934dc00ae9ac8f2d894a2d53727983f013ce1a3eff86d80",
  "23": "61aa6b4bda933cc879dfdd7550a3481d5042edbd63d4fbc30b03d8c20f109797",
  "25": "f20a8e20de22673af7a9b17cdef6edfc61df6c1488b7cc80cd568e421aa9d114",
  "28": "7fd68f93cf749ca15ba16a6446e53452ccb6af569fc8540e28edeebc5ca718c8",
  "30": "cd0a47fa35d4c3d4ac18c2496986bd0737cd83482e1ad50d48144aa73be228c0",
  "31": "25fd35723def188075cb71b8421dc520ad0c65c8f339f83543586f24756c3db3",
  "41": "db68b3036514ca6332f00aa780fb04e11528a5da6cb371ad5b4bf66e93057f07",
  "45": "5e0d2901469d0eeb2614db86bbb072adb09ca472975076f6659be5dc70b87322",
  "51": "46d8b6f8f55f709aa6969669dc82ebc0d20b3f5338e7f0e86941cc03f481ecc6",
  "59": "9ab65759cd41d1fdc722cc931fdc64908d52d54e78130aa6a7efbc0bd6d1e6e6"
 }
}
```

<!-- part block -->
#### Pass de6745da8390

| field | value |
| --- | --- |
| date | 2026-11-10 |
| review scope | lines 1, 20, 21, 22, 23, 25, 28, 30, 31, 41, 45, 51, 59 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | de6745da83907beaa75df82fbdfe18b8aed212f826e5b0a5ecc0907a59875d20 |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | bc96bb43e7c547c33ff4b1067971f2c29348fe0c79d95f9674d86b9ece0f712e |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7386c939c369b65c52b39fef3b0a279008b8c9144b6817d453fb7df62b552b43 |
| receipt | .transcription/ny_it201.lines-a24e4d3e7024 |
| printed lines compared | 13 |
| agree / disagree / missing | 12 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 7, 8, 9, 10, 13, 14, 18, 19, 30, 31 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 7, 8, 9, 10, 18, 19, 30, 31 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_rs, ny_tcw, ny_tcw_first |
| named lines: f1040.line11a, f1040.line15, f1040.line1z, f1040.line27a, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line6b, f1040.line7a, f1040.status | f1040 |
| named lines: s1.line1, s1.line26, s1.line2a, s1.line3, s1.line7, s1.line9 | s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: ny_it201.line1
    printed: "1"
    label: "Wages, salaries, tips, etc."
    type: NonNegDollars
    expr: {op: copy, from: f1040.line1z}
    note: "The instructions say line 1 should be the same as federal Form 1040, line 1z."

  - id: ny_it201.line20
    printed: "20"
    label: "Interest income on state and local bonds and obligations (but not those of NYS or its local governments)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.out_of_state_bond_interest]
    note: "If the answer is No, the instructions say go to line 21, so no amount is entered. If Yes, the amount is outside this slice's closed inputs, so the line refuses."

  - id: ny_it201.line21
    printed: "21"
    label: "Public employee 414(h) retirement contributions from your wage and tax statements"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.414h]
    note: "If the filer is not a member public employee, the instructions say go to line 22. The W-2 414(h) amount is not among the provided inputs, so the line refuses."

  - id: ny_it201.line22
    printed: "22"
    label: "New York's 529 college savings program distributions"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.529_nonqualified]
    note: "With no nonqualified withdrawal, the instructions say go to line 23. Otherwise the Line 22 worksheet needs amounts that are not provided, so the line refuses."

  - id: ny_it201.line23
    printed: "23"
    label: "Other (Form IT-225, line 9)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.it225, ny_it201.ask.special_accrual]
    note: "This amount comes from Form IT-225, line 9. Special accruals go through IT-225 addition A-115, so that question also refuses."

  - id: ny_it201.line25
    printed: "25"
    label: "Taxable refunds, credits, or offsets of state and local income taxes (from line 4)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.inflation_check]
    note: "The 2025 instructions put only an inflation refund check included in federal AGI on line 25. Its amount is not a provided input, so the line refuses when one was received."

  - id: ny_it201.line28
    printed: "28"
    label: "Interest income on U.S. government bonds"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.us_obligation_interest]
    note: "If the answer is No, the instructions say go to line 29. The U.S. obligation interest amount is not provided, so the line refuses."

  - id: ny_it201.line30
    printed: "30"
    label: "New York's 529 college savings program deduction/earnings"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.529_owner]
    note: "With no NY 529 contribution or withdrawal (as owner or beneficiary), the instructions say go to line 31. The Line 30 worksheet amounts are not provided, so the line refuses."

  - id: ny_it201.line31
    printed: "31"
    label: "Other (Form IT-225, line 18)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.it225, ny_it201.ask.special_accrual]
    note: "This amount comes from Form IT-225, line 18. Special accruals go through IT-225 subtraction S-129, so that question also refuses."

  - id: ny_it201.line41
    printed: "41"
    label: "Resident credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.resident_credit]
    note: "If the answer is No, the instructions say go to line 42. Form IT-112-R and IT-112-C are not computed here, so the line refuses."

  - id: ny_it201.line45
    printed: "45"
    label: "Net other NYS taxes (Form IT-201-ATT, line 30)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_taxes]

  - id: ny_it201.h_line51_split
    printed: "(helper)"
    label: "Married filing a joint New York State return and only one spouse was a New York City resident for all of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [ny_it201.ask.spouse_resident, {const: false}]}

  - id: ny_it201.line51
    printed: "51"
    label: "Other NYC taxes (Form IT-201-ATT, line 34)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_taxes, ny_it201.h_line51_split]
    note: "This amount comes from Form IT-201-ATT, Part 3, line 34, which is refused through other_taxes. On a joint return where only one spouse was a full-year NYC resident, the combined separate-sheet and IT-360.1 tax goes on line 51. That is not computed, so it refuses. I read filing status from f1040.status, since item A follows the federal status."

  - id: ny_it201.h_zero
    printed: "(helper)"
    label: "Zero (no sales or use tax owed)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}

  - id: ny_it201.line59
    printed: "59"
    label: "Sales or use tax (do not leave blank)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: false}]}
          then: ny_it201.h_zero
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: true}]}
          then: ny_it201.sut.chart
    refuses: [ny_it201.ask.use_tax_st141, ny_it201.ask.abode_part_year]
    note: "If no sales or use tax is owed, enter 0. Otherwise use the sales and use tax chart amount from the separately reviewed ny_it201.sut.chart. Form ST-141 cases (items of $1,000 or more, business, rental or royalty purchases, or choosing to compute the exact amount) refuse. A part-year permanent place of abode needs a months-maintained count that is not provided, so it also refuses."
```
```
<!-- part section 1 -->
1 — Wages, salaries, tips, etc.
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line1z"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line1z"}
```

Second transcription's note: The instructions say line 1 should be the same as federal Form 1040, line 1z.

Ruling: open
Reviewed in: pass de6745da8390

<!-- part section 20 -->
20 — Interest income on state and local bonds and obligations (but not those of NYS or its loca
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 21 -->
21 — Public employee 414(h) retirement contributions from your wage and tax statements
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 22 -->
22 — New York’s 529 college savings program distributions
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 23 -->
23 — Other (Form IT-225, line 9)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 25 -->
25 — Taxable refunds, credits, or offsets of state and local income taxes (from line 4)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 28 -->
28 — Interest income on U.S. government bonds
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 30 -->
30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 31 -->
31 — Other (Form IT-225, line 18)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 41 -->
41 — Resident credit
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 45 -->
45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 51 -->
51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part section 59 -->
59 — Sales or use tax (do not leave blank)
Status: **AGREE**
Reviewed in: pass de6745da8390

<!-- part gate 20 -->
| 20 | ny_it201.ask.out_of_state_bond_interest | ny_it201.ask.out_of_state_bond_interest |
<!-- part gate 21 -->
| 21 | ny_it201.ask.414h | ny_it201.ask.414h |
<!-- part gate 22 -->
| 22 | ny_it201.ask.529_nonqualified | ny_it201.ask.529_nonqualified |
<!-- part gate 23 -->
| 23 | ny_it201.ask.it225, ny_it201.ask.special_accrual | ny_it201.ask.it225, ny_it201.ask.special_accrual |
<!-- part gate 25 -->
| 25 | ny_it201.ask.inflation_check | ny_it201.ask.inflation_check |
<!-- part gate 28 -->
| 28 | ny_it201.ask.us_obligation_interest | ny_it201.ask.us_obligation_interest |
<!-- part gate 30 -->
| 30 | ny_it201.ask.529_owner | ny_it201.ask.529_owner |
<!-- part gate 31 -->
| 31 | ny_it201.ask.it225, ny_it201.ask.special_accrual | ny_it201.ask.it225, ny_it201.ask.special_accrual |
<!-- part gate 41 -->
| 41 | ny_it201.ask.resident_credit | ny_it201.ask.resident_credit |
<!-- part gate 45 -->
| 45 | ny_it201.ask.other_taxes | ny_it201.ask.other_taxes |
<!-- part gate 51 -->
| 51 | ny_it201.ask.other_taxes, ny_it201.h_line51_split | ny_it201.ask.other_taxes, ny_it201.h_line51_split |
<!-- part gate 59 -->
| 59 | ny_it201.ask.abode_part_year, ny_it201.ask.use_tax_st141 | ny_it201.ask.abode_part_year, ny_it201.ask.use_tax_st141 |
<!-- end -->
