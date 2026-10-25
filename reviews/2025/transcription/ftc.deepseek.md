# Transcription agreement — ftc

Second transcription of `Foreign tax credit — election without Form 1116` by an isolated model (spec 6.5), compared line by line with `forms/2025/ftc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 21360d2bbb1d549a931aeea5f817f5e608d2265db8c098305c42c2982a58390d |
| prompt policy | source-only-computation-v2 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "eq"}, {"args": [{"input": "ftc.taxes"}, {"param": "ftc.limit"}], "test": "le"}], "test": "all"}, "then": {"of": [{"input": "ftc.taxes"}, {"ref": "f1040.line16"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"param": "ftc.limit"}, {"input": "ftc.taxes"}], "test": "lt"}, {"args": [{"const": true}, {"input": "ftc.all_passive"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.elect"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.eligible"}], "test": "ne"}, {"args": [{"const": true}, {"input": "ftc.statements"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope/representation on completed supported returns; i1116 (2025) pp.1-2 lists the conditions for the election without Form1116, which removes that form's limitation. The present disagreement concerns the condition guards, not the min expression shared by both transcriptions. With positive foreign tax the project ftc.needs1116 refuses a failed election condition; on an admitted case both select the same min(taxes,f1040.line16). With zero tax (NonNegDollars), the project returns zero directly and the second either returns zero or min(0,nonnegative regular tax)=0. Stand-alone excluded cases and partial-input order are not asserted equivalent. This ruling does not separately establish the shared min from the waived Form1116 limitation.

## Raw second transcription

```yaml
lines:
  - id: ftc.h_election_allowed
    printed: "(helper)"
    label: "All conditions for the election without Form 1116 are met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ftc.elect, {const: true}]}
        - {op: test, eq: [ftc.all_passive, {const: true}]}
        - {op: test, eq: [ftc.statements, {const: true}]}
        - {op: test, eq: [ftc.eligible, {const: true}]}
        - {op: test, le: [ftc.taxes, {param: ftc.limit}]}
  - id: ftc.h_credit_amount
    printed: "(helper)"
    label: "Smaller of total creditable foreign taxes and regular tax"
    type: Dollars
    expr:
      op: smaller_of
      of: [ftc.taxes, f1040.line16]
  - id: ftc.h_zero
    printed: "(helper)"
    label: "No foreign tax credit without Form 1116"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ftc.credit
    printed: "(helper)"
    label: "Foreign tax credit claimed without Form 1116"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ftc.h_election_allowed, {const: true}]}
          then: ftc.h_credit_amount
        - guard: {op: test, eq: [ftc.h_election_allowed, {const: false}]}
          then: ftc.h_zero
```
