# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a24cabf2883ba31c4d541c673572e9edfa609714d79bcf8a01eb15c7ea71b13b |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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
{"of": [{"input": "ftc.taxes"}, {"of": [{"const": 0}, {"ref": "f1040.line16"}], "op": "larger_of"}], "op": "smaller_of"}
```

Second transcription's note: The election instructions say to enter the smaller of total foreign tax or regular tax. The election conditions are all_passive, statements, eligible, elect, and taxes not more than the $300/$600 limit; when any fails the filer needs Form 1116, so this line refuses.

Ruling: model error; i1116 (2025) pp.1-2 gives the election/min rule, and Who should file requires foreign taxes paid/accrued when claiming the credit. The reply refuses whenever elect=false, including a completed zero-foreign-tax record where no credit is claimed. The project correctly returns zero when taxes=0 without requiring an election. The bounded source witness .transcription/ftc-zero-tax-source-witness.json confirms the reply produces a model-declared refusal on that zero-tax/no-election case. This rules on over-refusal, not a project value defect or new Form1116 support.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.election_unavailable, scope.other_line16 | ftc.election_unavailable |

## Raw second transcription

```yaml
lines:
  - id: ftc.zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: "ss.zero"}

  - id: ftc.regular_tax
    printed: "(helper)"
    label: "Regular tax for the foreign tax credit, floored at zero"
    type: Dollars
    expr: {op: larger_of, of: [f1040.line16, ftc.zero]}
    note: "The Form 1116 line 20 instructions define regular tax as Form 1040 line 16 plus Schedule 2 Part I line 1z less any Form 4972 tax included on line 16, and say to enter -0- if zero or less. Only f1040.line16 is available in this interface; additional line 16 tax is refused through scope.other_line16."

  - id: ftc.election_ok
    printed: "(helper)"
    label: "All conditions for the election without Form 1116 are met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, le: [ftc.taxes, {param: ftc.limit}]}

  - id: ftc.election_unavailable
    printed: "(helper)"
    label: "The election without Form 1116 is not available"
    type: Bool
    expr: {op: test, not: {op: test, eq: [ftc.election_ok, {const: true}]}}

  - id: ftc.credit
    printed: "(helper)"
    label: "Foreign tax credit — election without Form 1116"
    type: Dollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.regular_tax]}
    refuses: [ftc.election_unavailable, scope.other_line16]
    note: "The election instructions say to enter the smaller of total foreign tax or regular tax. The election conditions are all_passive, statements, eligible, elect, and taxes not more than the $300/$600 limit; when any fails the filer needs Form 1116, so this line refuses."
```
