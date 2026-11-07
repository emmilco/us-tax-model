# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f73223874d8e8182b100b69130a62247fa7325bc326dd49eacfcf1374295ea72 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 141bae05e585faca9e2b3004f05b07ee046180249f936a934e15b799de35c842 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | beb5cacabd95cbba4ccd014a203316ee5999866ca21c5cec50467b5a5385aefc |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### ftc.credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}, "then": {"of": [{"input": "ftc.taxes"}, {"of": [{"ref": "f1040.line16"}, {"ref": "s2.line1z"}], "op": "sum"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "eq"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"from": {"ref": "f1040.line16"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The text does not say what happens if the election is not made. I chose zero for that case: the election is the only credit route this slice computes, and Form 1116 is outside it. If the filer elects but any condition fails (passive income, payee statements, creditability and required reductions, or the $300/$600 limit), the line is refused: Form 1116 is needed instead.

Ruling: model error, with scope for the not-elected return; as the prior ruling of this disagreement. i1116 p. 2, "To make the election, just enter on the foreign tax credit line of your tax return ... the smaller of (a) your total foreign tax, or (b) your regular tax"; p. 25, Line 20, "Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z"; p. 2, Who should file, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply". The reply puts the election conditions in the guards and enters $0 when they fail; the project enters $0 without foreign tax and otherwise refuses through ftc.needs1116 (Form 1116 is deferred, not dropped): the prior ruling's scope point. New in this reply: regular tax is Form 1040 line 16 alone, leaving out Schedule 2 line 1z, against p. 25, Line 20: a model error. The gate round changed only which election answers ftc.needs1116 reads (each now behind ftc.has_tax, false without foreign tax), not ftc.credit.
Reviewed in: pass d9bfe3c08a2f

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.h_needs_1116, scope.other_line16 | ftc.h_needs_1116 |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| ftc.credit | 5e13043a75fa0f2b47f421d784159a141514ad9141fb60c6753177782cce0a49 |
| (rest of the document) | 0b27c1db7e23a8e90ed880b6d5e278e7ce96926cdbe182df2a1cfd1afeed920d |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| ftc.credit | cb42de4021aa2818fc3fce716161252aacd39b40b09f928b21d0dad04f02a637 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass d9bfe3c08a2f

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines ftc.credit |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d9bfe3c08a2f3d0294ff8d6c278f86f210e53eb5c15962917aef1d043c4aef78 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | 8a40770f91dfdd3ee0781d48c1842790156e8eb72d1326ae43e279d6e35c536a |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e100f2be4e23b4a1b216cfd5590909830e3a3abc62464dbcd998755e21d3fe56 |
| receipt | .transcription/ftc.lines-3d3f5d872abc |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: div.basis_reconciled, div.box10, div.box12, div.box13, div.box2b, div.box2c, div.box2d, div.box2e, div.box2f, div.box3, div.box9 | div |
| named form, inputs and named lines: f1040.line16, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: s1a.carloan, s1a.line37, s1a.overtime, s1a.tips | s1a |
| named form, inputs and named lines: s2.amt, s2.other | s2 |
| named form, inputs and named lines: s3.line10, s3.line12, s3.line14 | s3 |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: sb.fbar_required, sb.form8938, sb.line7a, sb.line8, sb.ordinary_dividends, sb.unsupported | sb |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named form, inputs and named lines: sd.carryover, sd.distributions, sd.other_forms | sd |
| named line | f4952, qdcg |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Your regular tax (Form 1116, line 20): the total of Form 1040, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972. If the amount of your tax is zero or less, enter -0-."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line16, take: {param: ss.zero}}
    refuses: [scope.other_line16]
    note: "Two points are open. First, the supplied catalog has no Schedule 2, Part I, line 1z line, so this reads Form 1040 line 16 only, and the Schedule 2 line 1z amount is not added. Second, Form 4972 tax and Form 8978 line 14 adjustments are refused through scope.other_line16, so no subtraction or adjustment is made for them. The line 20 instruction 'zero or less, enter -0-' is applied as a floor at zero."
  - id: ftc.h_limit
    printed: "(helper)"
    label: "$300 ($600 if married filing a joint return)"
    type: NonNegDollars
    expr: {op: param, ref: ftc.limit}
  - id: ftc.h_within_limit
    printed: "(helper)"
    label: "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)"
    type: Bool
    expr: {op: test, le: [ftc.taxes, ftc.h_limit]}
  - id: ftc.h_qualifies
    printed: "(helper)"
    label: "This election is available only if you meet all of the following conditions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.h_within_limit, {const: true}]}
  - id: ftc.h_elects_and_qualifies
    printed: "(helper)"
    label: "Election made and available"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, eq: [ftc.h_qualifies, {const: true}]}
  - id: ftc.h_needs_1116
    printed: "(helper)"
    label: "File Form 1116 to claim the foreign tax credit if the election doesn't apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, eq: [ftc.h_qualifies, {const: false}]}
  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular_tax]}
  - id: ftc.credit
    printed: "(helper)"
    label: "To make the election, just enter on the foreign tax credit line of your tax return (Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ftc.h_elects_and_qualifies, {const: true}]}
          then: ftc.h_smaller
        - guard: {op: test, eq: [ftc.h_elects_and_qualifies, {const: false}]}
          then: ftc.h_zero
    refuses: [ftc.h_needs_1116]
    note: "The text does not say what happens if the election is not made. I chose zero for that case: the election is the only credit route this slice computes, and Form 1116 is outside it. If the filer elects but any condition fails (passive income, payee statements, creditability and required reductions, or the $300/$600 limit), the line is refused: Form 1116 is needed instead."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_zero
    printed: "(helper)"
    label: "Zero (no foreign tax credit claimed under the election)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ftc.h_regular_tax_raw
    printed: "(helper)"
    label: "Regular tax: total of Form 1040, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972"
    type: Dollars
    expr: {op: sum, of: [f1040.line16, s2.line1z]}
    refuses: [scope.other_line16]
    note: "The Form 4972 tax is subtracted from line 16. This tool refuses Form 4972 under scope.other_line16, so no Form 4972 tax is in line 16 and nothing is subtracted. Form 8978 adjustments are refused under the same screening input."
  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Regular tax (if zero or less, enter -0-)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ftc.h_regular_tax_raw, take: {const: 0}}
    note: "The election text points to the line 20 instructions to figure regular tax. Those instructions say to enter -0- if the tax is zero or less after adjustment. That floor is applied here."
  - id: ftc.h_over_limit
    printed: "(helper)"
    label: "Total creditable foreign taxes are more than $300 ($600 if married filing a joint return)"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {param: ftc.limit}]}
  - id: ftc.h_qualifies
    printed: "(helper)"
    label: "All conditions for the election to claim the foreign tax credit without filing Form 1116 are met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.h_over_limit, {const: false}]}
  - id: ftc.h_has_taxes
    printed: "(helper)"
    label: "Any creditable foreign taxes"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {const: 0}]}
  - id: ftc.h_needs_1116
    printed: "(gate)"
    label: "Foreign taxes were paid but the election conditions are not met (file Form 1116 to claim the credit)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.h_has_taxes, {const: true}]}
        - {op: test, eq: [ftc.h_qualifies, {const: false}]}
  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular_tax]}
  - id: ftc.credit
    printed: "(helper)"
    label: "Foreign tax credit (Schedule 3 (Form 1040), Part I, line 1) under the election without Form 1116"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ftc.elect, {const: true}]}
              - {op: test, eq: [ftc.h_qualifies, {const: true}]}
          then: ftc.h_smaller
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [ftc.elect, {const: true}]}
                - {op: test, eq: [ftc.h_qualifies, {const: true}]}
          then: ftc.h_zero
    refuses: [ftc.h_needs_1116, scope.other_line16]
    note: "The text does not say what happens if the filer meets the conditions but does not make the election. I read that as the filer not claiming the credit by this route, so the credit is 0. A deduction or Form 1116 is outside this slice. If foreign taxes exist but the conditions are not met, the tool refuses and points to Form 1116."
```
```
