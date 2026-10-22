# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4832ac61714b63de68eba91cc30a786b5e5cd62c2e1977cd43a4593351438628 |
| subject sha256 | 75bfec5dc24f26e9741c3462da47524b30152c4b52c7f20ad6b305b75ab8848a |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### ftc.credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ftc.credit | ftc.h_needs_1116 | ftc.h_needs_1116 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ftc.h_limit
    printed: "(helper)"
    label: "$300 ($600 if married filing a joint return)"
    type: NonNegDollars
    expr: {op: param, ref: ftc.limit}
    note: "The text gives $600 only for married filing jointly and $300 otherwise. The parameter is keyed by filing status with those values."
  - id: ftc.h_within_limit
    printed: "(helper)"
    label: "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)"
    type: Bool
    expr: {op: test, le: [ftc.taxes, ftc.h_limit]}
  - id: ftc.h_has_tax
    printed: "(helper)"
    label: "Any creditable foreign tax"
    type: Bool
    expr: {op: test, gt: [ftc.taxes, {const: 0}]}
  - id: ftc.h_qualifies
    printed: "(helper)"
    label: "All conditions met and election made: all foreign source gross income was passive category income; all income and foreign taxes were reported on a qualified payee statement; total creditable foreign taxes within the limit; creditability and line 12 reduction rules applied; election made"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, eq: [ftc.h_within_limit, {const: true}]}
  - id: ftc.h_not_qualifies
    printed: "(helper)"
    label: "The election without Form 1116 doesn't apply"
    type: Bool
    expr: {op: test, not: ftc.h_qualifies}
  - id: ftc.h_needs_1116
    printed: "(helper)"
    label: "File Form 1116 to claim the foreign tax credit if the election doesn't apply"
    type: Bool
    expr: {op: test, all: [ftc.h_has_tax, ftc.h_not_qualifies]}
    note: "If there is foreign tax and the election conditions are not met, or the election is not made, Form 1116 is needed (or the tax can be deducted instead). The tool computes neither, so it stops here."
  - id: ftc.h_smaller
    printed: "(helper)"
    label: "The smaller of (a) your total foreign tax, or (b) your regular tax"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ftc.taxes, f1040.line16]}
    note: "The text sends you to the line 20 instructions for how to figure regular tax, but those instructions are not in the supplied text. I used Form 1040 line 16 as regular tax. I did not use line 18, because it adds Schedule 2 line 3, which is not regular tax; that amount is zero after the s2.amt screen anyway."
  - id: ftc.h_zero
    printed: "(helper)"
    label: "No foreign tax credit"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: ftc.credit
    printed: "(helper)"
    label: "To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ftc.h_has_tax, {const: true}]}, then: ftc.h_smaller}
        - {guard: {op: test, not: ftc.h_has_tax}, then: ftc.h_zero}
    refuses: [ftc.h_needs_1116]
    note: "The credit is zero when there is no foreign tax. The text does not say this directly. I read it from 'the smaller of total foreign tax or regular tax', which gives zero when foreign tax is zero."
```
```
