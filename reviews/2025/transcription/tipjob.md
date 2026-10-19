# Transcription agreement — tipjob

Second transcription of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/tipjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e47c9a8d8678d2abdd6f57954f493600d2b99b98b1e59861335c6dcb507d4ee7 |
| printed lines compared | 3 |
| agree / disagree / missing | 1 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tipjob.one — One employer
Status: **AGREE**

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"input": "Form 4137, column 1(c), the qualified tips included for this"}
```

Ruling: scope; project retained, with the refusal now on the line. Form 4137 is outside this tool (s2.other, which names Form 4137), so column (c) is zero within scope; the line now carries that refusal.

### 1(d) — Enter the greater of column (b) or column (c)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "1(b)"}, {"line": "1(c)"}], "op": "larger_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "tipjob.qualified"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "tipjob.qualified"}], "test": "eq"}, "then": {"of": [{"line": "1(b)"}, {"line": "1(c)"}], "op": "larger_of"}}], "op": "choose"}
```

Second transcription's note: The IRS text says 'Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c.' The text does not say how to treat a row whose counted tips are not all from a listed occupation. Reading chosen: column (d) is the greater of columns (b) and (c) only when the filer confirms that all the tips counted for this employer were received in a listed occupation. Otherwise this row contributes zero.

Ruling: owner's ruling; project retained. An employer whose counted tips are not all qualified tips is refused (tipjob.mixed, on column (b)): the owner chose refusal over dropping the employer or splitting its tips. The second reads such a row as contributing zero. Both keep nonqualified tips off line 4c; the project does not silently drop the employer's qualified tips.

## Raw second transcription

```yaml
```yaml
lines:
  - id: tipjob.one
    printed: "(helper)"
    label: "One employer"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "Counts this worksheet row as one employer. The IRS text gives no constant for this, so the year parameter sales.one (value 1) is used."
  - id: tipjob.line1(c)
    printed: "1(c)"
    label: "Qualified tips reported on Form 4137, column 1(c), for this employer"
    type: NonNegDollars
    expr: {op: input, source: "Form 4137, column 1(c), the qualified tips included for this employer (enter zero if no Form 4137 amount for this employer)"}
  - id: tipjob.h_zero
    printed: "(helper)"
    label: "No amount for this employer"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: tipjob.h_greater
    printed: "(helper)"
    label: "The greater of column (b) or column (c)"
    type: NonNegDollars
    expr: {op: larger_of, of: [tipjob.amount, tipjob.line1(c)]}
  - id: tipjob.line1(d)
    printed: "1(d)"
    label: "Enter the greater of column (b) or column (c)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [tipjob.qualified, {const: true}]}
          then: tipjob.h_greater
        - guard: {op: test, eq: [tipjob.qualified, {const: false}]}
          then: tipjob.h_zero
    note: "The IRS text says 'Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c.' The text does not say how to treat a row whose counted tips are not all from a listed occupation. Reading chosen: column (d) is the greater of columns (b) and (c) only when the filer confirms that all the tips counted for this employer were received in a listed occupation. Otherwise this row contributes zero."
```
```
