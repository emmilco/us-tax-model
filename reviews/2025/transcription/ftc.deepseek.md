# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "eq"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"from": {"of": [{"ref": "f1040.line16"}, {"ref": "s2.line1z"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "ne"}], "test": "any"}, "then": {"from": {"input": "ftc.taxes"}, "op": "subtract_floor0", "take": {"input": "ftc.taxes"}}}], "op": "choose"}
```

Second transcription's note: The archived text defines the election credit as the smaller of total foreign tax and regular tax. Regular tax is read as Form 1040 line 16 plus Schedule 2 Part I line 1z, floored at zero; scope.other_line16 is refused because the closed interface does not supply the Form 4972 and other line-16 adjustments the instructions require. The line returns zero when the election conditions are not met.

Ruling: model error; on the zero-tax evaluation, with scope for the failed-election returns. i1116 p. 2, "To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax."; p. 2, Who should file, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and: ... You paid or accrued certain foreign taxes"; p. 25, Line 20, "Individuals. Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." Triage executable-triage-v2 (triage/ftc.deepseek.json; 1,228 fixtures, 500 generated returns seed 20261026, 200 partial records): 1,166 of 1,928 comparisons agree; kinds {"candidate-refuses": 456, "candidate-unknown": 244, "project-refuses": 62}; by return {"completed": {"candidate-unknown": 70}, "incomplete": {"candidate-unknown": 86}, "refused": {"candidate-refuses": 456, "candidate-unknown": 88, "project-refuses": 62}}. Both sides now read regular tax as Form 1040 line 16 plus Schedule 2 line 1z (the BUG-0190 fix), so the limit itself is not in dispute; the candidate's zero floor is redundant, since both terms are NonNegDollars and the Form 8978 and Form 4972 adjustments are refused (scope.other_line16, scope.credits). (1) candidate-unknown (70 on completed returns): with no foreign tax (ftc.taxes $0.00) the candidate still evaluates the election conditions and smaller_of(ftc.taxes, regular tax), so it needs Form 1040 line 16 and the answers below it (witness stage10.ira.fully_taxable, incomplete: project $0.00, candidate unknown for s1a.tips). With no foreign tax the credit is zero whatever the regular tax ("the smaller of (a) your total foreign tax"), so this is an answer the source does not need: a model error. (2) candidate-refuses: every one is on a return the project refuses anyway (for example classm.f8889.5.deepseek, gate scope.schedule1; classm.f4952.3.deepseek, gate sa.dependent): the candidate reaches a refused line 16 on a zero-tax return where the project shows $0.00. No tax quantity differs on a completed return. (3) project-refuses, scope (62, all on refused returns): with positive foreign tax and an election condition failed or not elected (classm.f8889.4.deepseek, classm.asset.4, classm.gift.1, classm.retirement.2, classm.s1.2, classm.s1.3), the project refuses with gate ftc.needs1116 and the candidate returns $0.00 (its ftc.h_zero). The source sends that filer to Form 1116 (p. 2, Who should file), which this tool defers; the project's refusal is a cited screen, and the candidate's $0.00 would drop a credit the source allows. The candidate also refuses only on scope.other_line16, which is redundant: f1040.line16 already refuses on it.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | scope.other_line16 | - |

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
