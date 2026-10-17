# Transcription agreement — person

Second transcription of `Excess Social Security credit — separately per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f438e3baabb9431cf318b97e9aaeea315506d2915cec298b718cad9893364b0a |
| printed lines compared | 13 |
| agree / disagree / missing | 12 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### person.box1 — Total W-2 box 1 for this person
Status: **AGREE**

### person.box2 — Total W-2 box 2 for this person
Status: **AGREE**

### person.medicare5 — Total W-2 box 5 for this person
Status: **AGREE**

### person.medicare6 — Total W-2 box 6 for this person
Status: **AGREE**

### employers — Total w2.one for this person
Status: **AGREE**

### overcount — Number of employers that withheld more than the limit
Status: **AGREE**

### over — Any employer withheld more than the limit
Status: **AGREE**

### wages — Total w2.wages for this person
Status: **AGREE**

### withheld — Total w2.box4 for this person
Status: **AGREE**

### eligible — More than one employer and total social security wages over $176,100
Status: **AGREE**

### excess — Withholding above $10,918.20, if any
Status: **AGREE**

### zero — No excess credit
Status: **AGREE**

### credit — Excess social security tax withheld, figured separately for this person
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "zero"}}, {"guard": {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}, "then": {"line": "excess"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "over"}], "test": "eq"}, {"args": [{"const": true}, {"line": "eligible"}], "test": "eq"}], "test": "all"}, "then": {"line": "excess"}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "eligible"}], "test": "eq"}, {"args": [{"const": true}, {"line": "over"}], "test": "eq"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second transcription's note: The text says: 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.' I read this as making the whole credit zero for this person, not only that employer's share. The text also allows excess tier 1 RRTA tax withheld, which is reported in W-2 box 14. No tier 1 inputs exist, so this line uses W-2 box 4 only. RRTA cases (person.rrta true) are assumed to be screened out elsewhere, and person.rrta is not used in the guards.

Ruling: refusal representation; project retained. The instruction says that if any one employer withheld more than $10,918.20 the excess cannot be claimed on the return and the employer should adjust it, otherwise Form 843 (i1040gi p. 117). The project refuses the return on that condition and on railroad (RRTA) compensation through the line's `refuses` entries; the second transcription returns a zero credit. The project's reading is the spec's refusal policy (spec 2.2, 2.5); within the non-refused scope the credit agrees (eligible: more than one employer and wages over the base; excess over the limit).

## Raw second transcription

```yaml
```yaml
lines:
  - id: person.lineemployers
    printed: "employers"
    label: "Total w2.one for this person"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}
    note: "The IRS text says 'more than one employer'. Each Form W-2 entry is counted as one employer through w2.one. Several W-2s from one employer are not combined here. The text does not say how to handle them, and I chose one W-2 per employer."

  - id: person.lineovercount
    printed: "overcount"
    label: "Number of employers that withheld more than the limit"
    type: Count
    expr:
      op: sum_over
      collection: w2
      field: w2.one
      where: {op: test, eq: [w2.over, {const: true}]}

  - id: person.lineover
    printed: "over"
    label: "Any employer withheld more than the limit"
    type: Bool
    expr: {op: test, gt: [person.lineovercount, {param: ss.zero}]}

  - id: person.linewages
    printed: "wages"
    label: "Total w2.wages for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.wages}

  - id: person.linewithheld
    printed: "withheld"
    label: "Total w2.box4 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box4}

  - id: person.lineeligible
    printed: "eligible"
    label: "More than one employer and total social security wages over $176,100"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [person.lineemployers, {param: ss.one}]}
        - {op: test, gt: [person.linewages, {param: ss.base}]}
    note: "The Form 1040 instructions say 'total wages of more than $176,100' without naming a measure of wages. I read this as social security wages plus social security tips (W-2 boxes 3 and 7, totaled as w2.wages). The $176,100 wage base in the W-2 instructions applies to that measure."

  - id: person.lineexcess
    printed: "excess"
    label: "Withholding above $10,918.20, if any"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.linewithheld, take: {param: ss.limit}}

  - id: person.linezero
    printed: "zero"
    label: "No excess credit"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: person.linecredit
    printed: "credit"
    label: "Excess social security tax withheld, figured separately for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [person.lineeligible, {const: true}]}
              - {op: test, eq: [person.lineover, {const: false}]}
          then: person.lineexcess
        - guard:
            op: test
            any:
              - {op: test, eq: [person.lineeligible, {const: false}]}
              - {op: test, eq: [person.lineover, {const: true}]}
          then: person.linezero
    note: "The text says: 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.' I read this as making the whole credit zero for this person, not only that employer's share. The text also allows excess tier 1 RRTA tax withheld, which is reported in W-2 box 14. No tier 1 inputs exist, so this line uses W-2 box 4 only. RRTA cases (person.rrta true) are assumed to be screened out elsewhere, and person.rrta is not used in the guards."

  - id: person.box1
    printed: "(helper)"
    label: "Total W-2 box 1 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box1}

  - id: person.box2
    printed: "(helper)"
    label: "Total W-2 box 2 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box2}

  - id: person.medicare5
    printed: "(helper)"
    label: "Total W-2 box 5 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box5}

  - id: person.medicare6
    printed: "(helper)"
    label: "Total W-2 box 6 for this person"
    type: NonNegDollars
    expr: {op: sum_over, collection: w2, field: w2.box6}
```
```
