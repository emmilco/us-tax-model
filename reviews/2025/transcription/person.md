# Transcription agreement — person

Second transcription of `Excess Social Security credit — separately per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/person.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ec80a360f9adba7ae36d545b9d331db288ea16e71246142f083e917db7d0fd19 |
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
{"alternatives": [{"guard": {"args": [{"line": "eligible"}, {"args": [{"line": "over"}], "test": "not"}], "test": "all"}, "then": {"line": "excess"}}, {"guard": {"args": [{"line": "over"}, {"args": [{"line": "eligible"}], "test": "not"}], "test": "any"}, "then": {"line": "zero"}}], "op": "choose"}
```

Second transcription's note: The text says that if any one employer withheld more than $10,918.20 'you can't claim the excess on your return' and the employer should adjust it. It does not say whether this bars only that employer's overcollection or the whole credit. Read as barring the whole credit for this person (credit zero, Form 843 route). Tier 1 RRTA tax is outside the tool, so the line refuses when person.rrta is true.

Ruling: refusal representation; project retained. The instruction says that if any one employer withheld more than $10,918.20 the excess cannot be claimed on the return and the employer should adjust it, otherwise Form 843 (i1040gi p. 117). The project refuses the return on that condition and on railroad (RRTA) compensation through the line's `refuses` entries; the second transcription returns a zero credit. The project's reading is the spec's refusal policy (spec 2.2, 2.5); within the non-refused scope the credit agrees (eligible: more than one employer and wages over the base; excess over the limit).

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| credit | person.rrta | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: person.lineemployers
    printed: "employers"
    label: "Total w2.one for this person"
    type: Count
    expr: {op: sum_over, collection: w2, field: w2.one}

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

  - id: person.h_multi
    printed: "(helper)"
    label: "More than one employer for 2025"
    type: Bool
    expr: {op: test, gt: [person.lineemployers, {param: ss.one}]}

  - id: person.h_wages_over
    printed: "(helper)"
    label: "Total wages of more than $176,100"
    type: Bool
    expr: {op: test, gt: [person.linewages, {param: ss.base}]}
    note: "The instructions say 'total wages of more than $176,100' without naming boxes; read as total social security wages and tips (W-2 boxes 3 and 7, i.e. w2.wages), per the printed line label."

  - id: person.lineeligible
    printed: "eligible"
    label: "More than one employer and total social security wages over $176,100"
    type: Bool
    expr: {op: test, all: [person.h_multi, person.h_wages_over]}

  - id: person.lineexcess
    printed: "excess"
    label: "Withholding above $10,918.20, if any"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: person.linewithheld, take: {param: ss.limit}}

  - id: person.linezero
    printed: "zero"
    label: "No excess credit"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: person.h_claim
    printed: "(helper)"
    label: "Eligible for the credit and no one employer withheld more than $10,918.20"
    type: Bool
    expr: {op: test, all: [person.lineeligible, {op: test, not: person.lineover}]}

  - id: person.linecredit
    printed: "credit"
    label: "Excess social security tax withheld, figured separately for this person"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [person.h_claim, {const: true}]}
          then: person.lineexcess
        - guard: {op: test, eq: [person.h_claim, {const: false}]}
          then: person.linezero
    refuses: [person.rrta]
    note: "The text says that if any one employer withheld more than $10,918.20 'you can't claim the excess on your return' and the employer should adjust it. It does not say whether this bars only that employer's overcollection or the whole credit. Read as barring the whole credit for this person (credit zero, Form 843 route). Tier 1 RRTA tax is outside the tool, so the line refuses when person.rrta is true."

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
