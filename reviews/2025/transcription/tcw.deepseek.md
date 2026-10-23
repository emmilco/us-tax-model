# Transcription agreement — tcw

Second transcription of `Tax Computation Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/tcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | deepseek-v4-pro |
| model reported | deepseek-v4-pro |
| prompt sha256 | 4171cc47bc78c5e2e4c50f1c5e84d8a90cadbeee658d468044d0ff3be81b6587 |
| subject sha256 | 55f4a8183a7cb641f369cd46f1f803f53d3b00535d950def877a8b757e4c5d15 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tax — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: single.row1.product
    printed: "(c) (single.row1.product)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.single.b1.rate
  - id: single.row1.tax
    printed: "Tax (single.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: single.row1.product
      take:
        param: tcw.single.b1.subtract
  - id: single.row2.product
    printed: "(c) (single.row2.product)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.single.b2.rate
  - id: single.row2.tax
    printed: "Tax (single.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: single.row2.product
      take:
        param: tcw.single.b2.subtract
  - id: single.row3.product
    printed: "(c) (single.row3.product)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.single.b3.rate
  - id: single.row3.tax
    printed: "Tax (single.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: single.row3.product
      take:
        param: tcw.single.b3.subtract
  - id: single.row4.product
    printed: "(c) (single.row4.product)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.single.b4.rate
  - id: single.row4.tax
    printed: "Tax (single.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: single.row4.product
      take:
        param: tcw.single.b4.subtract
  - id: single.row5.product
    printed: "(c) (single.row5.product)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.single.b5.rate
  - id: single.row5.tax
    printed: "Tax (single.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: single.row5.product
      take:
        param: tcw.single.b5.subtract
  - id: single.result
    printed: "Tax (single.result)"
    label: "Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                ge: [amount, {param: ordinary.table_boundary}]
              - op: test
                le: [amount, {param: tcw.single.b1.upper}]
          then: single.row1.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.single.b1.upper}]
              - op: test
                le: [amount, {param: tcw.single.b2.upper}]
          then: single.row2.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.single.b2.upper}]
              - op: test
                le: [amount, {param: tcw.single.b3.upper}]
          then: single.row3.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.single.b3.upper}]
              - op: test
                le: [amount, {param: tcw.single.b4.upper}]
          then: single.row4.tax
        - guard:
            op: test
            gt: [amount, {param: tcw.single.b4.upper}]
          then: single.row5.tax
  - id: mfj.row1.product
    printed: "(c) (mfj.row1.product)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfj.b1.rate
  - id: mfj.row1.tax
    printed: "Tax (mfj.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfj.row1.product
      take:
        param: tcw.mfj.b1.subtract
  - id: mfj.row2.product
    printed: "(c) (mfj.row2.product)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfj.b2.rate
  - id: mfj.row2.tax
    printed: "Tax (mfj.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfj.row2.product
      take:
        param: tcw.mfj.b2.subtract
  - id: mfj.row3.product
    printed: "(c) (mfj.row3.product)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfj.b3.rate
  - id: mfj.row3.tax
    printed: "Tax (mfj.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfj.row3.product
      take:
        param: tcw.mfj.b3.subtract
  - id: mfj.row4.product
    printed: "(c) (mfj.row4.product)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfj.b4.rate
  - id: mfj.row4.tax
    printed: "Tax (mfj.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfj.row4.product
      take:
        param: tcw.mfj.b4.subtract
  - id: mfj.row5.product
    printed: "(c) (mfj.row5.product)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfj.b5.rate
  - id: mfj.row5.tax
    printed: "Tax (mfj.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfj.row5.product
      take:
        param: tcw.mfj.b5.subtract
  - id: mfj.result
    printed: "Tax (mfj.result)"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                ge: [amount, {param: ordinary.table_boundary}]
              - op: test
                le: [amount, {param: tcw.mfj.b1.upper}]
          then: mfj.row1.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfj.b1.upper}]
              - op: test
                le: [amount, {param: tcw.mfj.b2.upper}]
          then: mfj.row2.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfj.b2.upper}]
              - op: test
                le: [amount, {param: tcw.mfj.b3.upper}]
          then: mfj.row3.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfj.b3.upper}]
              - op: test
                le: [amount, {param: tcw.mfj.b4.upper}]
          then: mfj.row4.tax
        - guard:
            op: test
            gt: [amount, {param: tcw.mfj.b4.upper}]
          then: mfj.row5.tax
  - id: mfs.row1.product
    printed: "(c) (mfs.row1.product)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfs.b1.rate
  - id: mfs.row1.tax
    printed: "Tax (mfs.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfs.row1.product
      take:
        param: tcw.mfs.b1.subtract
  - id: mfs.row2.product
    printed: "(c) (mfs.row2.product)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfs.b2.rate
  - id: mfs.row2.tax
    printed: "Tax (mfs.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfs.row2.product
      take:
        param: tcw.mfs.b2.subtract
  - id: mfs.row3.product
    printed: "(c) (mfs.row3.product)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfs.b3.rate
  - id: mfs.row3.tax
    printed: "Tax (mfs.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfs.row3.product
      take:
        param: tcw.mfs.b3.subtract
  - id: mfs.row4.product
    printed: "(c) (mfs.row4.product)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfs.b4.rate
  - id: mfs.row4.tax
    printed: "Tax (mfs.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfs.row4.product
      take:
        param: tcw.mfs.b4.subtract
  - id: mfs.row5.product
    printed: "(c) (mfs.row5.product)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.mfs.b5.rate
  - id: mfs.row5.tax
    printed: "Tax (mfs.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: mfs.row5.product
      take:
        param: tcw.mfs.b5.subtract
  - id: mfs.result
    printed: "Tax (mfs.result)"
    label: "Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                ge: [amount, {param: ordinary.table_boundary}]
              - op: test
                le: [amount, {param: tcw.mfs.b1.upper}]
          then: mfs.row1.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfs.b1.upper}]
              - op: test
                le: [amount, {param: tcw.mfs.b2.upper}]
          then: mfs.row2.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfs.b2.upper}]
              - op: test
                le: [amount, {param: tcw.mfs.b3.upper}]
          then: mfs.row3.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.mfs.b3.upper}]
              - op: test
                le: [amount, {param: tcw.mfs.b4.upper}]
          then: mfs.row4.tax
        - guard:
            op: test
            gt: [amount, {param: tcw.mfs.b4.upper}]
          then: mfs.row5.tax
  - id: hoh.row1.product
    printed: "(c) (hoh.row1.product)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.hoh.b1.rate
  - id: hoh.row1.tax
    printed: "Tax (hoh.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: hoh.row1.product
      take:
        param: tcw.hoh.b1.subtract
  - id: hoh.row2.product
    printed: "(c) (hoh.row2.product)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.hoh.b2.rate
  - id: hoh.row2.tax
    printed: "Tax (hoh.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: hoh.row2.product
      take:
        param: tcw.hoh.b2.subtract
  - id: hoh.row3.product
    printed: "(c) (hoh.row3.product)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.hoh.b3.rate
  - id: hoh.row3.tax
    printed: "Tax (hoh.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: hoh.row3.product
      take:
        param: tcw.hoh.b3.subtract
  - id: hoh.row4.product
    printed: "(c) (hoh.row4.product)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.hoh.b4.rate
  - id: hoh.row4.tax
    printed: "Tax (hoh.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: hoh.row4.product
      take:
        param: tcw.hoh.b4.subtract
  - id: hoh.row5.product
    printed: "(c) (hoh.row5.product)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: amount
      rate:
        param: tcw.hoh.b5.rate
  - id: hoh.row5.tax
    printed: "Tax (hoh.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: subtract
      from: hoh.row5.product
      take:
        param: tcw.hoh.b5.subtract
  - id: hoh.result
    printed: "Tax (hoh.result)"
    label: "Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                ge: [amount, {param: ordinary.table_boundary}]
              - op: test
                le: [amount, {param: tcw.hoh.b1.upper}]
          then: hoh.row1.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.hoh.b1.upper}]
              - op: test
                le: [amount, {param: tcw.hoh.b2.upper}]
          then: hoh.row2.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.hoh.b2.upper}]
              - op: test
                le: [amount, {param: tcw.hoh.b3.upper}]
          then: hoh.row3.tax
        - guard:
            op: test
            all:
              - op: test
                gt: [amount, {param: tcw.hoh.b3.upper}]
              - op: test
                le: [amount, {param: tcw.hoh.b4.upper}]
          then: hoh.row4.tax
        - guard:
            op: test
            gt: [amount, {param: tcw.hoh.b4.upper}]
          then: hoh.row5.tax
  - id: tax
    printed: "Tax (tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [status, {const: "single"}]
          then: single.result
        - guard:
            op: test
            eq: [status, {const: "mfj"}]
          then: mfj.result
        - guard:
            op: test
            eq: [status, {const: "qss"}]
          then: mfj.result
        - guard:
            op: test
            eq: [status, {const: "mfs"}]
          then: mfs.result
        - guard:
            op: test
            eq: [status, {const: "hoh"}]
          then: hoh.result
```
```
