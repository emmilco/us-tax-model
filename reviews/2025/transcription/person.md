# Transcription agreement — person

Second transcription of `Excess Social Security credit — separately per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 74b41da69142473b167a0899aa023ecee9fab2ebe8b42b88d06642617c737f95 |
| printed lines compared | 26 |
| agree / disagree / missing | 23 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 18, 19, 41, 93, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 18, 19, 41, 93, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### person.one — One entry for this person
Status: **AGREE**

### person.educator_deduction — This person's educator expense deduction
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "person.educator_expenses"}, {"const": 0}], "test": "le"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": 0}, {"input": "person.educator_expenses"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "person.eligible_educator"}], "test": "eq"}, "then": {"of": [{"input": "person.educator_expenses"}, {"param": "s1.educator_max"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: representation; project retained. The project returns zero without reading the eligibility question when the expenses are zero; the second reads eligibility first. With zero expenses the smaller of the expenses and $300 is zero either way (i1040gi p. 93, Schedule 1, line 11).

### person.hsa_forms — Number of Forms 8889 entered for this person
Status: **AGREE**

### person.hsa_split — This persons Form 8889 uses the spouse rule of line 6
Status: **AGREE**

### person.hsa_agreed — This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
Status: **AGREE**

### person.hsa_step1 — This persons Step 1 limit under the spouse rule of line 6
Status: **AGREE**

### person.hsa_share — This persons part of the Step 1 limit under the spouse rule of line 6
Status: **DISAGREE**

Project:

```json
{"collection": "f8889", "field": "f8889.share_raw", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "f8889", "field": "f8889.share", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "family"}, {"input": "f8889.dec_coverage"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "none"}, {"input": "f8889.dec_coverage"}], "test": "eq"}, {"args": [{"const": true}, {"input": "f8889.last_month"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "f8889.months_family"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}], "test": "all"}}
```

Ruling: representation; project retained. The project sums f8889.share_raw, the second f8889.share, which copies it and carries the allocation refusal; the refusal's condition reads this total, so summing the copy would make the refusal depend on itself. The values are the same, and the refusal still applies on line 6 (i8889 p. 7, Steps 2 and 3).

### person.hsa_deduction — Form 8889 line 13 for this person
Status: **AGREE**

### person.tip_employers — Number of employers that paid this person qualified tips
Status: **AGREE**

### person.tip_total — This person's worksheet column (d) total
Status: **AGREE**

### person.tip_reported — This person's worksheet column (b) total
Status: **AGREE**

### person.ot_employers — Number of employers that paid this person qualified overtime compensation
Status: **AGREE**

### person.ot_total — This person's overtime worksheet column (b) total
Status: **AGREE**

### person.box1 — Total W-2 box 1 for this person
Status: **AGREE**

### person.box2 — Total W-2 box 2 for this person
Status: **AGREE**

### person.medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

### person.medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

### employers — Total w2.one for this person
Status: **AGREE**

### overcount — Number of employers that withheld more than the limit
Status: **AGREE**

### over — Any employer withheld more than the limit
Status: **AGREE**

### wages — Total w2.wages for this person
Status: **AGREE**

### withheld — Total w2.box4 for this person
Status: **AGREE**

### eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

### excess — Withholding above $10,918.20, if any
Status: **AGREE**

### zero — No excess credit
Status: **AGREE**

### credit — Excess social security tax withheld, figured separately for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "excess"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "over"}], "test": "eq"}, {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}], "test": "all"}, "then": {"line": "excess"}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "over"}], "test": "ne"}, {"args": [{"const": true}, {"line": "eligible"}], "test": "ne"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second transcription's note: Two points were open. First, the text does not say whether an employer that over-withheld bars the whole credit or only its own share. It says 'you can't claim the excess on your return', so I chose to allow this person no credit at all. Second, tier 1 RRTA tax is screened out through person.rrta rather than computed.

Ruling: refusal representation; project retained. The instruction says that if any one employer withheld more than $10,918.20 the excess cannot be claimed on the return and the employer should adjust it, otherwise Form 843 (i1040gi p. 117). The project refuses the return on that condition and on railroad (RRTA) compensation through the line's `refuses` entries; the second transcription returns a zero credit. The project's reading is the spec's refusal policy (spec 2.2, 2.5); within the non-refused scope the credit agrees (eligible: more than one employer and wages over the base; excess over the limit). Stage 13 re-run: the credit is figured separately for each spouse from that spouse's Forms W-2 (i1040gi p. 117), as both transcriptions do.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| credit | person.rrta | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: person.lineemployers
    printed: "employers"
    label: "Total w2.one for this person (number of employers for 2025)"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
    note: "Line 11 says 'had more than one employer'. Each Form W-2 entry for this person counts as one employer. I chose that reading over merging entries from the same employer, because the entries carry no employer identifier."

  - id: person.lineovercount
    printed: "overcount"
    label: "Number of employers that withheld more than the limit"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one, where: {op: test, eq: [w2.over, {const: true}]}}

  - id: person.lineover
    printed: "over"
    label: "Any employer withheld more than the limit ($10,918.20)"
    type: Bool
    expr: {op: test, gt: [person.lineovercount, {param: ss.zero}]}

  - id: person.linewages
    printed: "wages"
    label: "Total w2.wages for this person (social security wages plus social security tips)"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.wages}
    note: "Line 11 says 'total wages of more than $176,100' but does not name the boxes. I chose the sum of social security wages and tips (boxes 3 and 7) from each Form W-2. This matches the $176,100 wage base that the W-2 instructions apply to boxes 3 and 7."

  - id: person.linewithheld
    printed: "withheld"
    label: "Total w2.box4 for this person (social security tax withheld)"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box4}

  - id: person.lineeligible
    printed: "eligible"
    label: "If you, or your spouse if filing a joint return, had more than one employer for 2025 and total wages of more than $176,100"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [person.lineemployers, {param: ss.one}]}
        - {op: test, gt: [person.linewages, {param: ss.base}]}

  - id: person.lineexcess
    printed: "excess"
    label: "You can take a credit on this line for the amount withheld in excess of $10,918.20"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.linewithheld, take: {param: ss.limit}}

  - id: person.linezero
    printed: "zero"
    label: "No excess credit"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: person.linecredit
    printed: "credit"
    label: "Excess social security tax withheld. Figure this amount separately for you and your spouse. But if any one employer withheld more than $10,918.20, you can't claim the excess on your return."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [person.lineeligible, {const: true}]}
              - {op: test, eq: [person.lineover, {const: false}]}
          then: person.lineexcess
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [person.lineeligible, {const: true}]}
                - {op: test, eq: [person.lineover, {const: false}]}
          then: person.linezero
    refuses: [person.rrta]
    note: "Two points were open. First, the text does not say whether an employer that over-withheld bars the whole credit or only its own share. It says 'you can't claim the excess on your return', so I chose to allow this person no credit at all. Second, tier 1 RRTA tax is screened out through person.rrta rather than computed."

  - id: person.one
    printed: "(helper)"
    label: "One entry for this person"
    type: Count
    expr: {op: param, ref: person.one}

  - id: person.h_educator_max
    printed: "(helper)"
    label: "Year parameter s1.educator_max ($300)"
    type: NonNegDollars
    expr: {op: param, ref: s1.educator_max}

  - id: person.h_educator_limited
    printed: "(helper)"
    label: "Up to $300 of qualified expenses you paid in 2025"
    type: NonNegDollars
    expr: {op: smaller_of, of: [person.educator_expenses, person.h_educator_max]}

  - id: person.h_educator_zero
    printed: "(helper)"
    label: "No educator expense deduction"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: person.educator_deduction
    printed: "(helper)"
    label: "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025. Neither spouse can deduct more than $300 of their qualified expenses."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.eligible_educator, {const: true}]}
          then: person.h_educator_limited
        - guard: {op: test, eq: [person.eligible_educator, {const: false}]}
          then: person.h_educator_zero

  - id: person.hsa_forms
    printed: "(helper)"
    label: "Number of Forms 8889 entered for this person"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one}

  - id: person.hsa_split
    printed: "(helper)"
    label: "This person's Form 8889 uses the spouse rule of line 6"
    type: Count
    expr: {op: sum_over, collection: f8889, field: f8889.one, where: {op: test, eq: [f8889.split, {const: true}]}}

  - id: person.hsa_agreed
    printed: "(helper)"
    label: "This person's Form 8889 uses an agreed allocation under the spouse rule of line 6"
    type: Count
    expr:
      op: sum_over
      collection: f8889
      field: f8889.one
      where:
        op: test
        all:
          - {op: test, eq: [f8889.split, {const: true}]}
          - {op: test, eq: [f8889.allocation, {const: "agreed"}]}

  - id: person.hsa_step1
    printed: "(helper)"
    label: "This person's Step 1 limit under the spouse rule of line 6"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.step1, where: {op: test, eq: [f8889.split, {const: true}]}}

  - id: person.hsa_share
    printed: "(helper)"
    label: "This person's part of the Step 1 limit under the spouse rule of line 6"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.share, where: {op: test, eq: [f8889.split, {const: true}]}}

  - id: person.hsa_deduction
    printed: "(helper)"
    label: "Form 8889 line 13 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: f8889, field: f8889.line13}

  - id: person.tip_employers
    printed: "(helper)"
    label: "Number of employers that paid this person qualified tips"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one}

  - id: person.tip_total
    printed: "(helper)"
    label: "This person's Qualified Tips From More Than One Employer Worksheet column (d) total"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_d}

  - id: person.tip_reported
    printed: "(helper)"
    label: "This person's worksheet column (b) total: amount of qualified tips reported by each employer on Form W-2, or reported to the employer on Form(s) 4070"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.amount}

  - id: person.ot_employers
    printed: "(helper)"
    label: "Number of employers that paid this person qualified overtime compensation"
    type: Count
    expr: {op: sum_over, collection: otjob, field: otjob.one}

  - id: person.ot_total
    printed: "(helper)"
    label: "This person's Qualified Overtime Compensation From More Than One Employer Worksheet column (b) total"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}

  - id: person.box1
    printed: "(helper)"
    label: "Total Form W-2 box 1 (wages, tips, other compensation) for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box1}

  - id: person.box2
    printed: "(helper)"
    label: "Total Form W-2 box 2 (federal income tax withheld) for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}

  - id: person.medicare5
    printed: "(helper)"
    label: "Medicare wages and tips from Form W-2, box 5, total for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}

  - id: person.medicare6
    printed: "(helper)"
    label: "Medicare tax withheld from Form W-2, box 6, total for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}
```
```
