# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a24cabf2883ba31c4d541c673572e9edfa609714d79bcf8a01eb15c7ea71b13b |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 75bfec5dc24f26e9741c3462da47524b30152c4b52c7f20ad6b305b75ab8848a |
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
{"alternatives": [{"guard": {"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ftc.elect"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}, "then": {"of": [{"input": "ftc.taxes"}, {"from": {"ref": "f1040.line16"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: If the filer does not elect, this line gives zero. A filer who elects but fails a condition needs Form 1116, so the line refuses (ftc.h_unavailable). The rule that no carryover goes to or from the election year is captured by the ftc.elect question. The tool computes nothing for it.

Ruling: representation on completed supported returns; i1116 (2025) pp.1-2 Election To Claim ... Without Filing Form1116 explicitly instructs the smaller of total foreign tax and regular tax, despite waiving the Form1116 lines15-23 limitation. That primary text establishes the shared min expression. With positive tax, admitted cases meet the election conditions and both use that min; the reply floors regular tax at zero, redundant for the supported computed nonnegative line16. With zero tax and a completed no-election answer the reply returns zero, as confirmed by .transcription/ftc-zero-tax-source-witness.json. Excluded regimes and absent election answers are not asserted equivalent.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.h_unavailable | ftc.h_unavailable |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_limit
    printed: "(helper)"
    label: "$300 ($600 if married filing a joint return)"
    type: NonNegDollars
    expr: {op: param, ref: ftc.limit}

  - id: ftc.h_within_limit
    printed: "(helper)"
    label: "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)."
    type: Bool
    expr: {op: test, le: [ftc.taxes, ftc.h_limit]}

  - id: ftc.h_conditions
    printed: "(helper)"
    label: "This election is available only if you meet all of the following conditions."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.h_within_limit, {const: true}]}
    note: "The i1116 text lists three conditions: all income is passive, everything was reported on qualified payee statements, and taxes are within the $300/$600 limit. I also included ftc.eligible because the text says the creditability rules and the line 12 reduction rules still apply under the election."

  - id: ftc.h_unavailable
    printed: "(helper)"
    label: "Election chosen but its conditions are not met (Form 1116 required)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, not: {op: test, eq: [ftc.h_conditions, {const: true}]}}
    note: "If the conditions are not met, the IRS text says to file Form 1116. This tool does not prepare Form 1116, so this line makes the credit line refuse instead of computing a credit."

  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Your regular tax: the total of Form 1040, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972 (if zero or less, enter -0-)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line16, take: {const: 0}}
    note: "No line in the catalog represents Schedule 2 line 1z or Form 4972 tax. The screening inputs scope.other_line16 (Form 4972) and s2.other (other Schedule 2 amounts) exclude both, so I read regular tax as Form 1040 line 16. The floor at zero follows the line 20 instruction 'If ... the amount of your tax is zero or less, enter -0-'. Form 8978 adjustments are also excluded by screening."

  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular_tax]}

  - id: ftc.h_zero
    printed: "(helper)"
    label: "No credit claimed under the election"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "There is no zero parameter for this form, so I used the zero-valued money parameter ss.zero from the supplied catalog."

  - id: ftc.credit
    printed: "(helper)"
    label: "To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ftc.elect, {const: true}]}
          then: ftc.h_smaller
        - guard: {op: test, eq: [ftc.elect, {const: false}]}
          then: ftc.h_zero
    refuses: [ftc.h_unavailable]
    note: "If the filer does not elect, this line gives zero. A filer who elects but fails a condition needs Form 1116, so the line refuses (ftc.h_unavailable). The rule that no carryover goes to or from the election year is captured by the ftc.elect question. The tool computes nothing for it."
```
```
