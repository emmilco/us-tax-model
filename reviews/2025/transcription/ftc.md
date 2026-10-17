# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3b6a842de3641503007052640802dce9d4ad712773c49b50350de633e67a1115 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### ftc.credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "ftc.all_passive"}, {"input": "ftc.elect"}, {"input": "ftc.eligible"}, {"input": "ftc.statements"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"input": "ftc.taxes"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"input": "ftc.all_passive"}], "test": "not"}, {"args": [{"input": "ftc.elect"}], "test": "not"}, {"args": [{"input": "ftc.eligible"}], "test": "not"}, {"args": [{"input": "ftc.statements"}], "test": "not"}], "test": "any"}, {"args": [{"input": "ftc.taxes"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The text does not say what happens when the election conditions are not met or the election is not made; in that case Form 1116 would be filed, which this model does not cover. I chose a zero credit for that case, so the Form 1116 route must be screened out elsewhere. The no-carryover rule is only an acknowledgment captured by ftc.elect and has no arithmetic effect here.

Ruling: refusal representation; project retained. The project gives the credit as the smaller of creditable foreign taxes and the tax on line 16 when any foreign tax exists, and refuses the return through the election gates (not all passive, no election, not eligible, statements not received, taxes over the no-Form-1116 limit, i1116 pp. 1–2) rather than returning zero. The second transcription folds those conditions into the credit as zero. Within the non-refused scope the values agree.

## Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_zero
    printed: "(helper)"
    label: "No credit amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
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
    note: "The text keys the limit only to 'married filing a joint return'. The parameter ftc.limit is keyed by filing status, and its non-MFJ values are $300, which matches. Qualifying surviving spouse is treated as $300 because it is not a joint return."
  - id: ftc.h_election_valid
    printed: "(helper)"
    label: "This election is available only if you meet all of the following conditions, and you make the election"
    type: Bool
    expr: {op: test, all: [ftc.all_passive, ftc.statements, ftc.h_within_limit, ftc.eligible, ftc.elect]}
  - id: ftc.h_has_tax
    printed: "(helper)"
    label: "Any creditable foreign tax"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {const: 0}]}
  - id: ftc.h_applies
    printed: "(helper)"
    label: "Election made and valid, with foreign tax to credit"
    type: Bool
    expr: {op: test, all: [ftc.h_election_valid, ftc.h_has_tax]}
  - id: ftc.h_regular_tax
    printed: "(helper)"
    label: "Your regular tax (see the instructions for line 20)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line16}
    note: "The election text points to the Form 1116 line 20 instructions for how to figure regular tax, but that text is not in the provided pages. I chose Form 1040 line 16 (tax before AMT and credits). This should be confirmed against the line 20 instructions."
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
        - guard: ftc.h_applies
          then: ftc.h_smaller
        - guard: {op: test, not: ftc.h_applies}
          then: ftc.h_zero
    note: "The text does not say what happens when the election conditions are not met or the election is not made; in that case Form 1116 would be filed, which this model does not cover. I chose a zero credit for that case, so the Form 1116 route must be screened out elsewhere. The no-carryover rule is only an acknowledgment captured by ftc.elect and has no arithmetic effect here."
```
```
