# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "eq"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"from": {"of": [{"ref": "f1040.line16"}, {"ref": "s2.line1z"}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The text does not say what happens if the filer meets the conditions but does not make the election. I read that as the filer not claiming the credit by this route, so the credit is 0. A deduction or Form 1116 is outside this slice. If foreign taxes exist but the conditions are not met, the tool refuses and points to Form 1116.

Ruling: model error; on the zero-tax evaluation, with scope for the not-elected return. i1116 p. 2, "To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax."; p. 2, Who should file, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and: ... You paid or accrued certain foreign taxes"; p. 25, Line 20, "Individuals. Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." Triage executable-triage-v2 (triage/ftc.json; 1,228 fixtures, 500 generated returns seed 20261026, 200 partial records): 1,229 of 1,928 comparisons agree; kinds {"candidate-refuses": 454, "candidate-unknown": 244, "project-refuses": 1}; by return {"completed": {"candidate-unknown": 70}, "incomplete": {"candidate-unknown": 86}, "refused": {"candidate-refuses": 454, "candidate-unknown": 88, "project-refuses": 1}}. Both sides now read regular tax as Form 1040 line 16 plus Schedule 2 line 1z (the BUG-0190 fix), so the limit itself is not in dispute; the candidate's zero floor is redundant, since both terms are NonNegDollars and the Form 8978 and Form 4972 adjustments are refused (scope.other_line16, scope.credits). (1) candidate-unknown (70 on completed returns): with no foreign tax (ftc.taxes $0.00) the candidate still evaluates the election conditions and smaller_of(ftc.taxes, regular tax), so it needs Form 1040 line 16 and the answers below it (witness stage10.ira.fully_taxable, incomplete: project $0.00, candidate unknown for s1a.tips). With no foreign tax the credit is zero whatever the regular tax ("the smaller of (a) your total foreign tax"), so this is an answer the source does not need: a model error. (2) candidate-refuses: every one is on a return the project refuses anyway (for example classm.f8889.5.deepseek, gate scope.schedule1; classm.f4952.3.deepseek, gate sa.dependent): the candidate reaches a refused line 16 on a zero-tax return where the project shows $0.00. No tax quantity differs on a completed return. (3) project-refuses, scope: stage4.refuse.ftc.election (foreign tax with the conditions met and ftc.elect false): the project refuses with gate ftc.needs1116 ("The small-tax election is unavailable or not chosen. Form 1116 is deferred, not dropped"), the candidate enters $0.00. Without the election the credit is claimed on Form 1116 (p. 2, Who should file), which this tool does not prepare; the project's refusal is a cited screen, and the candidate's $0.00 would drop a credit the source allows.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.h_needs_1116, scope.other_line16 | ftc.h_needs_1116 |

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
