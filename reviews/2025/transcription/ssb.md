# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 28fa18440d40b0b84db20538858e679477f95f62168bb9c851daace9bdd285df |
| printed lines compared | 19 |
| agree / disagree / missing | 14 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### ssb.has_benefits — Any social security benefits (otherwise the worksheet is not needed)
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"line": "1"}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0}, {"input": "ssb.benefits"}], "test": "lt"}
```

Ruling: equivalent; project retained. Worksheet line 1 is a copy of the benefits input, so 'line 1 more than zero' and 'benefits more than zero' are the same test.

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **AGREE**

### 2 — Multiply line 1 by 50% (0.50)
Status: **AGREE**

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **AGREE**

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **AGREE**

### 5 — Combine lines 2, 3, and 4
Status: **AGREE**

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25; zero i
Status: **AGREE**

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 
Status: **AGREE**

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"param": "ssb.base_single"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "ssb.lived_apart"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"input": "ssb.lived_apart"}], "test": "not"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}], "op": "choose"}
```

Second transcription's note: For married filing separately and living together, lines 8 through 15 are skipped. This model has no blank value, so the line is set to zero in that case. Line 16 uses line 7 directly in that case, so the values on lines 8 to 15 do not affect the result.

Ruling: equivalent; project retained. Both give $25,000 to single, head of household, qualifying surviving spouse and to married filing separately having lived apart all year, $32,000 to married filing jointly, and $0 to married filing separately having lived with the spouse; the second writes the $25,000 case as '(lived apart or not mfs) and not mfj'. The project asks the lived-apart question only of a married filer filing separately.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 
Status: **AGREE**

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"param": "ssb.adjust_single"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"input": "ssb.lived_apart"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"input": "ssb.lived_apart"}], "test": "not"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}], "op": "choose"}
```

Second transcription's note: Skipped for married filing separately and living together (line 8 instructions). Set to zero in that case; it does not affect line 16.

Ruling: equivalent; project retained. As line 8, with $9,000 and $12,000.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **AGREE**

### 12 — Enter the smaller of line 9 or line 10
Status: **AGREE**

### 13 — Enter one-half of line 12
Status: **AGREE**

### 14 — Enter the smaller of line 2 or line 13
Status: **AGREE**

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **AGREE**

### 16 — Add lines 14 and 15
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "7"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"line": "14"}, {"line": "15"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"input": "ssb.lived_apart"}], "test": "not"}], "test": "all"}, "then": {"amount": {"line": "7"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}, {"guard": {"args": [{"input": "ssb.lived_apart"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"line": "14"}, {"line": "15"}], "op": "sum"}}], "op": "choose"}
```

Ruling: equivalent; project retained. For a Bool, 'not lived apart' and 'lived apart is false' are the same test; both take 85% of line 7 for a married filer filing separately who lived with the spouse and lines 14 plus 15 otherwise.

### 17 — Multiply line 1 by 85% (0.85)
Status: **AGREE**

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"line": "17"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "16"}, {"line": "17"}], "op": "smaller_of"}
```

Second transcription's note: The TIP says the lump-sum election (Pub. 915) may reduce the taxable amount. This tool does not compute that election, so this line refuses on ssb.lump_sum.

Ruling: equivalent in value; project retained. With no benefits line 17 is $0, and the smaller of line 16 (never negative) and $0 is $0, so the project's zero branch gives the same value; it exists so a filer without benefits is never asked the worksheet's screens.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 2 | ssb.pub915, ssb.terror_disability | - |
| 5 | ssb.pub915, ssb.terror_disability | - |
| 6 | scope.schedule1 | - |
| 7 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 9 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 11 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 12 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 13 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 14 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 15 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 16 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 17 | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 18 | scope.schedule1, ssb.lump_sum, ssb.pub915, ssb.terror_disability | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ssb.line1
    printed: "1"
    label: "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099. Also enter this amount on Form 1040 or 1040-SR, line 6a"
    type: NonNegDollars
    expr: {op: copy, from: ssb.benefits}
    refuses: [ssb.pub915, ssb.terror_disability]
    note: "The Exception in the line 6a and 6b instructions says not to use this worksheet in the Pub. 590-A and Pub. 915 cases. Disability payments for terrorist-attack injuries are left out of income. This tool does not compute either case, so this line refuses on ssb.pub915 and ssb.terror_disability."
  - id: ssb.line2
    printed: "2"
    label: "Multiply line 1 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.half}}
  - id: ssb.line3
    printed: "3"
    label: "Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8"
    type: Dollars
    expr: {op: sum, of: [f1040.line1z, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line7a, f1040.line8]}
  - id: ssb.line4
    printed: "4"
    label: "Enter the amount, if any, from Form 1040 or 1040-SR, line 2a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line2a}
  - id: ssb.line5
    printed: "5"
    label: "Combine lines 2, 3, and 4"
    type: Dollars
    expr: {op: sum, of: [ssb.line2, ssb.line3, ssb.line4]}
  - id: ssb.line6
    printed: "6"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    refuses: [scope.schedule1]
    note: "This tool does not support Schedule 1, so the line is zero only after the Schedule 1 screen (which also covers the line 24z write-in in the Before you begin box). There is no money-typed ssb zero parameter, so this line uses the shared money zero parameter sales.zero."
  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. Yes. Subtract line 6 from line 5"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line5, take: ssb.line6}
    note: "The 'No' branch is a STOP: nothing is taxable. Writing the line as subtract_floor0 gives zero in that case. The zero then carries through lines 9 to 18 and gives 0 on line 18, which is the STOP result."
  - id: ssb.h_mfj
    printed: "(helper)"
    label: "Filing status is married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}
  - id: ssb.h_mfs_together
    printed: "(helper)"
    label: "Married filing separately and you lived with your spouse at any time in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, not: ssb.lived_apart}]}
  - id: ssb.h_other
    printed: "(helper)"
    label: "Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: Bool
    expr: {op: test, all: [{op: test, not: ssb.h_mfj}, {op: test, not: ssb.h_mfs_together}]}
  - id: ssb.h_zero
    printed: "(helper)"
    label: "No amount (line skipped)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "$32,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "$25,000 (single, head of household, qualifying surviving spouse, or MFS lived apart)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
  - id: ssb.line8
    printed: "8"
    label: "If you are: Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: ssb.h_mfj, then: ssb.h_base_joint}
        - {guard: ssb.h_other, then: ssb.h_base_single}
        - {guard: ssb.h_mfs_together, then: ssb.h_zero}
    note: "For married filing separately and living together, lines 8 through 15 are skipped. This model has no blank value, so the line is set to zero in that case. Line 16 uses line 7 directly in that case, so the values on lines 8 to 15 do not affect the result."
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. Yes. Subtract line 8 from line 7"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
    note: "The 'No' branch is a STOP with nothing taxable. subtract_floor0 gives zero in that case, so lines 11 to 16 are zero and line 18 is 0, which is the STOP result."
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "$12,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "$9,000 (single, head of household, qualifying surviving spouse, or MFS lived apart)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: ssb.h_mfj, then: ssb.h_adjust_joint}
        - {guard: ssb.h_other, then: ssb.h_adjust_single}
        - {guard: ssb.h_mfs_together, then: ssb.h_zero}
    note: "Skipped for married filing separately and living together (line 8 instructions). Set to zero in that case; it does not affect line 16."
  - id: ssb.line11
    printed: "11"
    label: "Subtract line 10 from line 9. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line9, take: ssb.line10}
  - id: ssb.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line9, ssb.line10]}
  - id: ssb.line13
    printed: "13"
    label: "Enter one-half of line 12"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line12, rate: {param: ssb.half}}
  - id: ssb.line14
    printed: "14"
    label: "Enter the smaller of line 2 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line2, ssb.line13]}
  - id: ssb.line15
    printed: "15"
    label: "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line11, rate: {param: ssb.rate85}}
  - id: ssb.h_add14_15
    printed: "(helper)"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
  - id: ssb.h_line7_85
    printed: "(helper)"
    label: "Multiply line 7 by 85% (0.85) (married filing separately and lived with spouse at any time in 2025)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: ssb.h_mfs_together, then: ssb.h_line7_85}
        - {guard: {op: test, not: ssb.h_mfs_together}, then: ssb.h_add14_15}
  - id: ssb.line17
    printed: "17"
    label: "Multiply line 1 by 85% (0.85)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.rate85}}
  - id: ssb.line18
    printed: "18"
    label: "Taxable social security benefits. Enter the smaller of line 16 or line 17. Also enter this amount on Form 1040 or 1040-SR, line 6b"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line16, ssb.line17]}
    refuses: [ssb.lump_sum]
    note: "The TIP says the lump-sum election (Pub. 915) may reduce the taxable amount. This tool does not compute that election, so this line refuses on ssb.lump_sum."
  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Any social security benefits (otherwise the worksheet is not needed)"
    type: Bool
    expr: {op: test, gt: [ssb.benefits, {const: 0}]}
```
```
