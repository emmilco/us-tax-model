# Transcription agreement — qbi

Second transcription of `Section 199A dividend-only deduction and form selection` by an isolated model (spec 6.5), compared line by line with `forms/2025/qbi.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 8bdb5707c89c4386ce37d880ab9410291ad69050102b95fa5d90c456e3a3cbbb |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | bfdf022f2a6af7d4bc0be6b72286aa5dc86aa8f0ddab24c4ad8ccce36f5e8683 |

## Lines

### qbi.zero — Year parameter sales.zero
Status: **AGREE**

### qbi.eligible — Amount from qbi.dividends
Status: **AGREE**

### qbi.taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **DISAGREE**

Project:

```json
{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}
```

Second:

```json
{"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}
```

Second transcription's note: Open: the corrected line 11 instructions (post-release correction, 2026-02-13) say to subtract only. They do not say to floor the result at zero. Chosen: floor at zero, as the helper specification requires. This does not change line 13 of Form 8995 or line 35 of Form 8995-A, which floor at zero anyway.

Ruling: representation; project retained. The project reads Form 1040 line 11b (line 11a for a filer without the Schedule 1-A deduction, which is refused) and subtracts the Schedule A choice plus line 13b, the zero behind the Schedule 1-A refusal, as the corrected instruction reads (i8995-correction); the second subtracts lines 12e and 13b from line 11a directly, equal in value within the slice. Both floor at zero where the instruction states no floor; the deduction is unchanged because Form 8995 line 13 floors at zero itself. No change to the data.

### qbi.net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **AGREE**

### qbi.deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.age65"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": true}, {"input": "sa.blind"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Second transcription's note: Open: the printed threshold is filing-status-keyed (qbi.threshold). The cooperative-patron condition and other QBI or PTP items are left to the qbi.unsupported screen, which this selection does not test. Chosen: compare against the threshold only. Use Form 8995 line 15 at or below it and Form 8995-A line 39 above it.

Ruling: representation; project retained. The deduction before the QBI deduction now adds Form 1040 line 13b, the zero parameter behind the Schedule 1-A refusal (BUG-0007), to the Schedule A choice; the second transcription, told that Schedule 1-A is refused, omitted the term. Equal in value in this slice; the term is kept so the line 13b refusal propagates and the expression reads as the corrected instruction ("Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b", i8995-correction). No change to the data.

## Raw second transcription

```yaml
lines:
  - id: qbi.zero
    printed: "(helper)"
    label: "Year parameter sales.zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: qbi.eligible
    printed: "(helper)"
    label: "Amount from qbi.dividends"
    type: NonNegDollars
    expr: {op: copy, from: qbi.dividends}
    note: "Open: the text says qualified REIT dividends are reported on Form 1099-DIV, line 5, but does not say how to combine them with PTP income or carryforwards on Form 8995 line 6. Chosen: in this dividend-only scope (other items are screened by qbi.unsupported), only the box 5 section 199A dividends count."

  - id: qbi.h_line12e_13b
    printed: "(helper)"
    label: "Add Form 1040 lines 12e and 13b"
    type: NonNegDollars
    expr: {op: sum, of: [f1040.line12e, f1040.line13b]}

  - id: qbi.taxable_before
    printed: "(helper)"
    label: "Enter your taxable income figured before any QBI deduction, computed as follows. Form 1040 or 1040-SR filers: Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line11a, take: qbi.h_line12e_13b}
    note: "Open: the corrected line 11 instructions (post-release correction, 2026-02-13) say to subtract only. They do not say to floor the result at zero. Chosen: floor at zero, as the helper specification requires. This does not change line 13 of Form 8995 or line 35 of Form 8995-A, which floor at zero anyway."

  - id: qbi.net_capital_gain
    printed: "(helper)"
    label: "Enter your net capital gain, if any, increased by any qualified dividends: Form 1040, 1040-SR, or 1040-NR, line 3a, plus your net capital gain"
    type: NonNegDollars
    expr: {op: sum, of: [sd.net_gain, f1040.line3a]}
    note: "Open: the line 12 instructions give two cases. Without Schedule D, net capital gain is Form 1040 line 7a. With Schedule D, it is the smaller of Schedule D line 15 or 16, and nothing is added if either line is zero or less. Chosen: rely on sd.net_gain (the nonnegative net capital gain helper) for both cases and add Form 1040 line 3a, as the helper specification says."

  - id: qbi.h_within_threshold
    printed: "(helper)"
    label: "Taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly)"
    type: Bool
    expr: {op: test, le: [qbi.taxable_before, {param: qbi.threshold}]}

  - id: qbi.h_above_threshold
    printed: "(helper)"
    label: "Taxable income before the qualified business income deduction is above the Form 8995 threshold"
    type: Bool
    expr: {op: test, not: qbi.h_within_threshold}

  - id: qbi.deduction
    printed: "(helper)"
    label: "Qualified business income deduction. Use Form 8995 if your taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly), and you aren't a patron of an agricultural or horticultural cooperative; otherwise Form 8995-A"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: qbi.h_within_threshold, then: f8995.line15}
        - {guard: qbi.h_above_threshold, then: f8995a.line39}
    note: "Open: the printed threshold is filing-status-keyed (qbi.threshold). The cooperative-patron condition and other QBI or PTP items are left to the qbi.unsupported screen, which this selection does not test. Chosen: compare against the threshold only. Use Form 8995 line 15 at or below it and Form 8995-A line 39 above it."
```
