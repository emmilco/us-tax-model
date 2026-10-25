# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2d6b04884e2fdcbf37062d3d822569a31581cb82e518558d783b38d6124c0289 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | f175d7d2b004e32273f8a05a00bea25f741221a1fc9c0f321ed9026de9666d77 |
| printed lines compared | 19 |
| agree / disagree / missing | 13 / 6 / 0 |
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

Ruling: open

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

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "person", "field": "person.ira_ssb", "op": "sum_over", "where": null}, {"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line25"}], "op": "sum"}
```

Second:

```json
{"of": [{"ref": "s1.line11"}, {"ref": "s1.line13"}, {"ref": "s1.line15"}, {"ref": "s1.line16"}, {"ref": "s1.line17"}, {"ref": "s1.line18"}, {"ref": "s1.line19a"}, {"ref": "s1.line20"}, {"ref": "s1.line25"}], "op": "sum"}
```

Second transcription's note: The worksheet lists Schedule 1 lines 11 through 20, 23 and 25; unsupported Schedule 1 items are refused through scope.schedule1, so this sum uses the supported adjustment lines.

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}], "op": "choose"}
```

Second transcription's note: For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 8 is encoded as zero for that case.

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}], "op": "choose"}
```

Second transcription's note: For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 10 is encoded as zero for that case.

Ruling: open

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "7"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"line": "14"}, {"line": "15"}], "op": "sum"}}], "op": "choose"}
```

Second transcription's note: When married filing separately and the taxpayer lived with their spouse at any time in 2025, the line 8 instruction says to skip lines 8 through 15, multiply line 7 by 85%, and enter that on line 16.

Ruling: open

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

Ruling: open

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
lines:
  - id: ssb.line1
    printed: "1"
    label: "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099. Also enter this amount on Form 1040 or 1040-SR, line 6a."
    type: NonNegDollars
    expr: {op: copy, from: ssb.benefits}
    refuses: [ssb.pub915, ssb.terror_disability]
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
    expr: {op: sum, of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line20, s1.line25]}
    refuses: [scope.schedule1]
    note: "The worksheet lists Schedule 1 lines 11 through 20, 23 and 25; unsupported Schedule 1 items are refused through scope.schedule1, so this sum uses the supported adjustment lines."
  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? Yes. Subtract line 6 from line 5. If no, none of your social security benefits are taxable; enter -0- on Form 1040 or 1040-SR, line 6b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line5, take: ssb.line6}
  - id: ssb.line8
    printed: "8"
    label: "If you are: married filing jointly, enter $32,000; single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16; then go to line 17."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_base_joint
        - guard: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: true}]}]}
          then: ssb.h_base_single
        - guard: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: false}]}]}
          then: ssb.h_zero
        - guard: {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
          then: ssb.h_base_single
    note: "For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 8 is encoded as zero for that case."
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? Yes. Subtract line 8 from line 7. If no, none of your social security benefits are taxable; enter -0- on Form 1040 or 1040-SR, line 6b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_adjust_joint
        - guard: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: true}]}]}
          then: ssb.h_adjust_single
        - guard: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: false}]}]}
          then: ssb.h_zero
        - guard: {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
          then: ssb.h_adjust_single
    note: "For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 10 is encoded as zero for that case."
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
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: false}]}]}
          then: ssb.h_line16_mfs
        - guard: {op: test, any: [{op: test, ne: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: true}]}]}
          then: ssb.h_line16_normal
    note: "When married filing separately and the taxpayer lived with their spouse at any time in 2025, the line 8 instruction says to skip lines 8 through 15, multiply line 7 by 85%, and enter that on line 16."
  - id: ssb.line17
    printed: "17"
    label: "Multiply line 1 by 85% (0.85)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.rate85}}
  - id: ssb.line18
    printed: "18"
    label: "Taxable social security benefits. Enter the smaller of line 16 or line 17. Also enter this amount on Form 1040 or 1040-SR, line 6b."
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line16, ssb.line17]}
    refuses: [ssb.lump_sum]
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "Amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "Amount for single, head of household, qualifying surviving spouse, or married filing separately and lived apart"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "Adjustment amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "Adjustment amount for single, head of household, qualifying surviving spouse, or married filing separately and lived apart"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
  - id: ssb.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ssb.h_line16_mfs
    printed: "(helper)"
    label: "Line 7 multiplied by 85% (0.85) for married filing separately who lived with spouse"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
  - id: ssb.h_line16_normal
    printed: "(helper)"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Has social security benefits"
    type: Bool
    expr: {op: test, gt: [ssb.benefits, {const: 0}]}
```
