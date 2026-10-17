# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 62a88e71a7cd6a66809fadf8fef1a3abb92ac0125c3c603382b59009b4748a8f |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2 | cd35caf7283cb41a304b322a1438a3c7c78d3d692012065b8f15e84dd6340afa |

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

Second transcription's note: When the election conditions are not met, the text says to file Form 1116 instead, and that computation is not covered here. I chose zero for this worksheet's credit in that case. A host should screen that case out of scope rather than treat zero as final.

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
  - id: ftc.h_within_limit
    printed: "(helper)"
    label: "Total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)"
    type: Bool
    expr: {op: test, le: [ftc.taxes, ftc.h_limit]}
  - id: ftc.h_has_tax
    printed: "(helper)"
    label: "Any creditable foreign tax"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {const: 0}]}
  - id: ftc.h_qualifies
    printed: "(helper)"
    label: "This election is available only if you meet all of the following conditions; election made"
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
    note: "The text lists the passive-income, qualified-payee-statement and $300/$600 conditions. It also says creditability and line 12 reductions still apply (ftc.eligible). The taxpayer must make the election (ftc.elect). I treated all of these as required. The $600 limit is read as applying to married filing jointly only, as the ftc.limit parameter encodes it."
  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Your regular tax (see the instructions for line 20, later, for how to figure your regular tax)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line16}
    note: "The definition of regular tax is in the line 20 instructions, which are not in the text provided. I chose Form 1040 line 16 (tax before Schedule 2 additions). This should be checked against the line 20 instructions."
  - id: ftc.h_zero
    printed: "(helper)"
    label: "No foreign tax credit"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, ftc.h_regular_tax]}
  - id: ftc.credit
    printed: "(helper)"
    label: "To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ftc.h_qualifies, {const: true}]}, then: ftc.h_smaller}
        - {guard: {op: test, eq: [ftc.h_qualifies, {const: false}]}, then: ftc.h_zero}
    note: "When the election conditions are not met, the text says to file Form 1116 instead, and that computation is not covered here. I chose zero for this worksheet's credit in that case. A host should screen that case out of scope rather than treat zero as final."
```
```
