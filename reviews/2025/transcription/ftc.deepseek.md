# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
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
{"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}
```

Second transcription's note: The IRS instructions say the credit is the smaller of total foreign tax or regular tax. The supplied interface gives Form 1040 line 16 as the tax line; the Schedule 2 Part I line 1z and Form 4972 adjustments named in the Form 1116 line 20 instructions are not separately provided, so this transcription uses Form 1040 line 16 as regular tax.

Ruling: model error; i1116 p. 25, Line 20, "Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972", and p. 2, "the smaller of (a) your total foreign tax, or (b) your regular tax". The reply takes regular tax as Form 1040 line 16 alone, saying Schedule 2 line 1z was not provided; it is a line of another form the project reads (s2.line1z), and leaving it out understates the limit wherever Schedule 2 line 1z is not zero. With no foreign tax both give $0. The Form 4972 subtraction is refused by scope.other_line16. Same disagreement as the Claude pass of this round.
Reviewed in: pass d9bfe3c08a2f

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.h_election_unavailable | ftc.h_election_unavailable |

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
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d9bfe3c08a2f3d0294ff8d6c278f86f210e53eb5c15962917aef1d043c4aef78 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | 343df4d45441ef5d1a3e765b7e88846d6739c25f248a6d18e3b9acb0b94f7d24 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e100f2be4e23b4a1b216cfd5590909830e3a3abc62464dbcd998755e21d3fe56 |
| receipt | .transcription/ftc.deepseek.lines-3d3f5d872abc |
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
lines:
  - id: ftc.h_election_unavailable
    printed: "(helper)"
    label: "Election without Form 1116 is unavailable because a condition is not met"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [ftc.all_passive, {const: false}]
        - op: test
          eq: [ftc.statements, {const: false}]
        - op: test
          eq: [ftc.eligible, {const: false}]
        - op: test
          eq: [ftc.elect, {const: false}]
        - op: test
          not:
            op: test
            le: [ftc.taxes, {param: ftc.limit}]
  - id: ftc.credit
    printed: "(helper)"
    label: "Foreign tax credit allowed by the election without Form 1116"
    type: Dollars
    expr:
      op: smaller_of
      of: [ftc.taxes, f1040.line16]
    refuses: [ftc.h_election_unavailable]
    note: "The IRS instructions say the credit is the smaller of total foreign tax or regular tax. The supplied interface gives Form 1040 line 16 as the tax line; the Schedule 2 Part I line 1z and Form 4972 adjustments named in the Form 1116 line 20 instructions are not separately provided, so this transcription uses Form 1040 line 16 as regular tax."
```

## Raw second transcription

```yaml
lines:
  - id: ftc.h_limit
    printed: "(helper)"
    label: "Limit on creditable foreign taxes for the election without Form 1116"
    type: NonNegDollars
    expr: {op: param, ref: ftc.limit}
  - id: ftc.h_regular_raw
    printed: "(helper)"
    label: "Regular tax before the zero floor"
    type: Dollars
    expr: {op: sum, of: [f1040.line16, s2.line1z]}
  - id: ftc.h_regular
    printed: "(helper)"
    label: "Regular tax, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ftc.h_regular_raw, take: {const: 0}}
  - id: ftc.h_tax_cap
    printed: "(helper)"
    label: "Smaller of total foreign tax and regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular]}
  - id: ftc.h_conditions
    printed: "(helper)"
    label: "Election without Form 1116 conditions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, le: [ftc.taxes, ftc.h_limit]}
  - id: ftc.h_zero
    printed: "(helper)"
    label: "Zero credit amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ftc.taxes, take: ftc.taxes}
  - id: ftc.credit
    printed: "(helper)"
    label: "Foreign tax credit under the election without Form 1116"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ftc.h_conditions, {const: true}]}
          then: ftc.h_tax_cap
        - guard: {op: test, eq: [ftc.h_conditions, {const: false}]}
          then: ftc.h_zero
    refuses: [scope.other_line16]
    note: "The archived text defines the election credit as the smaller of total foreign tax and regular tax. Regular tax is read as Form 1040 line 16 plus Schedule 2 Part I line 1z, floored at zero; scope.other_line16 is refused because the closed interface does not supply the Form 4972 and other line-16 adjustments the instructions require. The line returns zero when the election conditions are not met."
```
