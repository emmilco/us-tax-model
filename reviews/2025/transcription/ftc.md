# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fa8a446c8ce4e783cc68085a9772f18afb31b50a9dd4b4e0497ee74b5f0ac469 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff |

## Lines

### ftc.credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "eq"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}, {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}, {"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The credit is zero when there is no foreign tax, and also when the election is unavailable or not made. Form 1116 is outside this worksheet.

Ruling: refusal representation; project retained. The project gives the credit as the smaller of creditable foreign taxes and the tax on line 16 when any foreign tax exists, and refuses the return through the election gates (not all passive, no election, not eligible, statements not received, taxes over the no-Form-1116 limit, i1116 pp. 1–2) rather than returning zero. The second transcription folds those conditions into the credit as zero. Within the non-refused scope the values agree.

## Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_limit
    printed: "(helper)"
    label: "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)"
    type: NonNegDollars
    expr: {op: param, ref: ftc.limit}
    note: "The parameter is keyed by filing status. The text gives $600 only for married filing jointly, so every other status, including qss, uses $300. This matches the supplied parameter values."
  - id: ftc.h_within_limit
    printed: "(helper)"
    label: "Total creditable foreign taxes aren't more than the election limit"
    type: Bool
    expr: {op: test, le: [ftc.taxes, ftc.h_limit]}
  - id: ftc.h_has_tax
    printed: "(helper)"
    label: "There is creditable foreign tax"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {const: 0}]}
  - id: ftc.h_applies
    printed: "(helper)"
    label: "Election to claim the foreign tax credit without filing Form 1116 is available, is made, and there is foreign tax"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.h_within_limit, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, eq: [ftc.h_has_tax, {const: true}]}
    note: "The text lists three availability conditions: passive category income only, qualified payee statements, and taxes within the $300/$600 limit. It also says the election must actually be made. The creditability and line-12 reduction rules still apply under the election, so ftc.eligible is required as well. If the election is unavailable, the text sends the taxpayer to Form 1116, which this worksheet does not model; in that case the credit here is zero."
  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Your regular tax (see the instructions for line 20 for how to figure your regular tax)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line16}
    note: "Open point: regular tax is defined in the Form 1116 line 20 instructions, and that text is not in the provided pages. I chose Form 1040 line 16, the tax on taxable income, without any AMT, as the regular tax."
  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular_tax]}
  - id: ftc.h_zero
    printed: "(helper)"
    label: "No foreign tax credit claimed under the election"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: ftc.credit
    printed: "(helper)"
    label: "Enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ftc.h_applies, {const: true}]}
          then: ftc.h_smaller
        - guard: {op: test, not: {op: test, eq: [ftc.h_applies, {const: true}]}}
          then: ftc.h_zero
    note: "The credit is zero when there is no foreign tax, and also when the election is unavailable or not made. Form 1116 is outside this worksheet."
```
```
