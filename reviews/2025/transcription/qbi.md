# Transcription agreement — qbi

Second transcription of `Section 199A dividend-only deduction and form selection` by an isolated model (spec 6.5), compared line by line with `forms/2025/qbi.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 960421b21cc1fafe4306bc736521535c0e67ca3fcd6bcbd101fadf60b3296b88 |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

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
{"from": {"from": {"ref": "f1040.line11a"}, "op": "subtract", "take": {"ref": "f1040.line12e"}}, "op": "subtract_floor0", "take": {"ref": "f1040.line13b"}}
```

Second transcription's note: The i8995 line 11 text says 'minus lines 12e and 13b' and gives no floor. The floor at zero comes from the requested definition of this helper, and it matches the NonNegDollars type.

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
{"alternatives": [{"guard": {"args": [{"from": {"from": {"ref": "f1040.line11a"}, "op": "subtract", "take": {"ref": "f1040.line12e"}}, "op": "subtract_floor0", "take": {"ref": "f1040.line13b"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"from": {"ref": "f1040.line11a"}, "op": "subtract", "take": {"ref": "f1040.line12e"}}, "op": "subtract_floor0", "take": {"ref": "f1040.line13b"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Second transcription's note: Form 8995 says to use it when taxable income before the QBI deduction is 'at or below' the threshold, so equality goes to Form 8995. Above the threshold, the dividend-only Form 8995-A total (line 39) is used. The text also excludes cooperative patrons from Form 8995. That case, along with any other QBI or PTP items, is screened out by qbi.unsupported, so it is not tested here.

Ruling: representation; project retained. The deduction before the QBI deduction now adds Form 1040 line 13b, the zero parameter behind the Schedule 1-A refusal (BUG-0007), to the Schedule A choice; the second transcription, told that Schedule 1-A is refused, omitted the term. Equal in value in this slice; the term is kept so the line 13b refusal propagates and the expression reads as the corrected instruction ("Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b", i8995-correction). No change to the data.

## Raw second transcription

```yaml
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
    note: "Form 8995 line 6 and the i8995 text treat qualified REIT dividends as the amount in Form 1099-DIV box 5. Qualified PTP income is screened out by qbi.unsupported. So the eligible amount is just qbi.dividends."

  - id: qbi.h_11a_less_12e
    printed: "(helper)"
    label: "Form 1040 line 11a minus line 12e"
    type: Dollars
    expr: {op: subtract, from: f1040.line11a, take: f1040.line12e}
    note: "This is the first step of the corrected i8995 line 11 instruction (line 11a minus lines 12e and 13b). It is a signed intermediate, and the zero floor is applied only to the final result."

  - id: qbi.taxable_before
    printed: "(helper)"
    label: "Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floored at zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qbi.h_11a_less_12e, take: f1040.line13b}
    note: "The i8995 line 11 text says 'minus lines 12e and 13b' and gives no floor. The floor at zero comes from the requested definition of this helper, and it matches the NonNegDollars type."

  - id: qbi.net_capital_gain
    printed: "(helper)"
    label: "Add sd.net_gain, f1040.line3a"
    type: NonNegDollars
    expr: {op: sum, of: [sd.net_gain, f1040.line3a]}
    note: "Line 12 in i8995 has two cases. If you are not required to file Schedule D, net capital gain is Form 1040 line 7a. If you file Schedule D, it is the smaller of lines 15 and 16, or zero if either is zero or less. As the helper definition directs, sd.net_gain is used here for net capital gain. I'm assuming sd.net_gain already covers the case where no Schedule D is filed."

  - id: qbi.h_threshold
    printed: "(helper)"
    label: "Form 8995 taxable-income threshold: $197,300 ($394,600 if married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: qbi.threshold}

  - id: qbi.deduction
    printed: "(helper)"
    label: "Select Form 8995 or dividend-only Form 8995-A"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [qbi.taxable_before, qbi.h_threshold]}
          then: f8995.line15
        - guard: {op: test, gt: [qbi.taxable_before, qbi.h_threshold]}
          then: f8995a.line39
    note: "Form 8995 says to use it when taxable income before the QBI deduction is 'at or below' the threshold, so equality goes to Form 8995. Above the threshold, the dividend-only Form 8995-A total (line 39) is used. The text also excludes cooperative patrons from Form 8995. That case, along with any other QBI or PTP items, is screened out by qbi.unsupported, so it is not tested here."
```
```
