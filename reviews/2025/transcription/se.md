# Transcription agreement — se

Second transcription of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/se.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 26f02e26b8410c2229524f98959a269c21c61b0e9a9a59444903a3105b5ec266 |
| subject sha256 | 0c850519b95a0d9a45ff9abb2ddb129d2a5755507a6929f64bfcc1024f606a73 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### line13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **DISAGREE**

Project:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"input": "line8a"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"input": "line8a"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: equivalent; project retained. Both multiply line 12 by 50%. The project floors line 2 at zero inside the 92.35% branch and floors the $400-tested amount at zero, where the second does not; both floors sit in branches whose guards already require line 2 above zero or line 4c of $400 or more, so they never bind. The second's line 5b (church employee income) is zero, refused in the project through person.se_screen (i1040sse, Line 5a), and its line 8d is line 8a, Form 4137 tips and Form 8919 wages being refused (person.se_screen). The values agree for every amount on line 2.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| line13 | f8959.unsupported | f8959.unsupported |

## Raw second transcription

```yaml
```yaml
lines:
  - id: se.line3
    printed: "3"
    label: "Combine lines 1a, 1b, and 2"
    type: Dollars
    expr: {op: copy, from: line2}
    note: "Lines 1a (farm profit or loss) and 1b (Conservation Reserve Program payments) have no input and no screening input in this tool; only line 2 (Schedule C) is bound. Line 3 is therefore line 2 alone. Farm income and CRP payments are outside the tool, but no refusal input was supplied to name for them."

  - id: se.h_4a_product
    printed: "(helper)"
    label: "Line 3 multiplied by 92.35% (0.9235)"
    type: Dollars
    expr: {op: multiply_rate, amount: se.line3, rate: {param: se.rate_9235}}
    note: "The form does not state a rounding rule. The multiply_rate atom rounds half-up to the cent."

  - id: se.line4a
    printed: "4a"
    label: "If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [se.line3, {const: 0}]}
          then: se.h_4a_product
        - guard: {op: test, le: [se.line3, {const: 0}]}
          then: se.line3

  - id: se.line4b
    printed: "4b"
    label: "If you elect one or both of the optional methods, enter the total of lines 15 and 17"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Part II (farm and nonfarm optional methods, lines 14-17) is not part of this transcription. No input or screening input exists for electing them, so line 4b is the case with no election, which is zero."

  - id: se.line4c
    printed: "4c"
    label: "Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax"
    type: Dollars
    expr: {op: sum, of: [se.line4a, se.line4b]}
    note: "The church employee income exception ('enter -0- and continue') is not computed; church employee income is refused at line 5b. The stop rule is applied in helper se.h_4c_taxable."

  - id: se.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: se.h_4c_taxable
    printed: "(helper)"
    label: "Line 4c when it is $400 or more; otherwise stop (no self-employment tax), zero"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ge: [se.line4c, {param: se.floor}]}
          then: se.line4c
        - guard: {op: test, lt: [se.line4c, {param: se.floor}]}
          then: se.h_zero
    note: "'If less than $400, stop; you don't owe self-employment tax' is read as making lines 6 through 13 zero when line 4c is under $400."

  - id: se.line5b
    printed: "5b"
    label: "Multiply line 5a by 92.35% (0.9235)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [f8959.unsupported]
    note: "Line 5a (church employee income) has no input. Church employee income is covered by the screening input f8959.unsupported, so this line refuses on it and otherwise computes the case without church employee income, which is zero. The 'if less than $100, enter -0-' rule is moot in that case."

  - id: se.line6
    printed: "6"
    label: "Add lines 4c and 5b"
    type: NonNegDollars
    expr: {op: sum, of: [se.h_4c_taxable, se.line5b]}

  - id: se.line7
    printed: "7"
    label: "Maximum amount of combined wages and self-employment earnings subject to social security tax for 2025"
    type: NonNegDollars
    expr: {op: param, ref: se.wage_base}

  - id: se.line8d
    printed: "8d"
    label: "Add lines 8a, 8b, and 8c"
    type: NonNegDollars
    expr: {op: copy, from: line8a}
    refuses: [f8959.unsupported]
    note: "Line 8b (Form 4137 unreported tips) and line 8c (Form 8919 wages) have no inputs. The screening input f8959.unsupported covers Form 4137 tips and Form 8919 wages, so this line refuses on it and otherwise is line 8a alone. The 8a instruction to skip lines 8b-10 at $176,100 or more gives the same result, because line 9 floors at zero."

  - id: se.line9
    printed: "9"
    label: "Subtract line 8d from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: se.line7, take: se.line8d}

  - id: se.h_10_base
    printed: "(helper)"
    label: "The smaller of line 6 or line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [se.line6, se.line9]}

  - id: se.line10
    printed: "10"
    label: "Multiply the smaller of line 6 or line 9 by 12.4% (0.124)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.h_10_base, rate: {param: se.rate_124}}

  - id: se.line11
    printed: "11"
    label: "Multiply line 6 by 2.9% (0.029)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.line6, rate: {param: se.rate_029}}

  - id: se.line12
    printed: "12"
    label: "Self-employment tax. Add lines 10 and 11"
    type: NonNegDollars
    expr: {op: sum, of: [se.line10, se.line11]}

  - id: se.line13
    printed: "13"
    label: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.line12, rate: {param: se.rate_50}}

  - id: line13
    printed: "(helper)"
    label: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: copy, from: se.line13}
```
```
