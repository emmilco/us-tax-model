# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ed59b93a375e79c822ab44f8e3c486e192ab1221db969e2468277a3d27781823 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a42afe175a2d5e61db9f7a6f7ca322dfbe0c3b056cfc2cb08651df5b83b01347 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 1027671bb973b7314ee64c4fc9691d23bc43e0171870bc504f443ca96d4ce18a |
| printed lines compared | 19 |
| agree / disagree / missing | 16 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, g28, household, s1, sales, scope, sdtw, u1250 |
| named line | eic, f8960, sa |
| shared page | f1040, ira, person, retirement, sd |

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

Ruling: representation; i1040gi p. 31, Lines 6a and 6b: "Use the Social Security Benefits Worksheet in these instructions to see if any of your benefits are taxable." executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 124 partial records from 40 bases; 2,189 comparisons): 2,189 agree. Same reply and project as the before-catalog-refresh ruling, which stands: both test the box 5 total (the project through ssb.line1, a copy of ssb.benefits). Project stands.

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

Second transcription's note: Schedule 1 line 23 is named by the worksheet but is not in the supplied catalog; this line sums the named Schedule 1 adjustment lines that are present.

Ruling: ambiguity (+ scope); amb.2025.ira_ssb_copy; i1040gi p. 32, worksheet line 6: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"; i1040gi p. 31, Exception. executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 124 partial records from 40 bases; 2,189 comparisons): 2,149 agree; 26 project-refuses, 12 candidate-unknown, 1 candidate-refuses, 1 project-unknown (none on a completed return). Same reply and project as the before-catalog-refresh ruling, which stands: the reply reads s1.line20 literally, the register's text at issue; the differences are the register's cycle and IRA returns refused by ira.cov_gate / ira.less_gate; none on a completed return. Project stands.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line
Status: **AGREE**

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **AGREE**

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line
Status: **AGREE**

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **AGREE**

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
Status: **AGREE**

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

Ruling: model error (+ scope); i1040gi p. 31, Lines 6a and 6b; i1040gi p. 31, Line 6c: "If any of your benefits are taxable for 2025 and they include a lump-sum benefit payment that was for an earlier year, you may be able to reduce the taxable amount with the lump-sum election". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 124 partial records from 40 bases; 2,189 comparisons): 610 agree; 1,346 candidate-unknown, 230 candidate-refuses, 3 project-refuses (on completed returns: 12 candidate-refuses, 167 candidate-unknown). Same reply and project as the before-catalog-refresh ruling, which stands: the reply asks the Pub. 915 screens and the lump-sum election of every return, including those without benefits where the project enters $0; its other refusals are returns the project refuses elsewhere (scope). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 2 | ssb.pub915, ssb.terror_disability | - |
| 5 | ssb.pub915, ssb.terror_disability | - |
| 7 | ssb.pub915, ssb.terror_disability | - |
| 9 | ssb.pub915, ssb.terror_disability | - |
| 11 | ssb.pub915, ssb.terror_disability | - |
| 12 | ssb.pub915, ssb.terror_disability | - |
| 13 | ssb.pub915, ssb.terror_disability | - |
| 14 | ssb.pub915, ssb.terror_disability | - |
| 15 | ssb.pub915, ssb.terror_disability | - |
| 16 | ssb.pub915, ssb.terror_disability | - |
| 17 | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 18 | ssb.lump_sum, ssb.pub915, ssb.terror_disability | - |

## Raw second transcription

```yaml
lines:
  - id: ssb.line1
    printed: "1"
    label: "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099. Also enter this amount on Form 1040 or 1040-SR, line 6a"
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
    note: "Schedule 1 line 23 is named by the worksheet but is not in the supplied catalog; this line sums the named Schedule 1 adjustment lines that are present."
  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? Yes. Subtract line 6 from line 5"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line5, take: ssb.line6}
  - id: ssb.line8
    printed: "8"
    label: "If married filing jointly, enter $32,000. If single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000. If married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: ssb.h_base_mfs
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_base_joint
        - guard: {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
          then: ssb.h_base_single
    shown_when: ssb.show_8_15
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? Yes. Subtract line 8 from line 7"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
    shown_when: ssb.show_8_15
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: ssb.h_adjust_mfs
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_adjust_joint
        - guard: {op: test, any: [{op: test, eq: [f1040.status, {const: "single"}]}, {op: test, eq: [f1040.status, {const: "hoh"}]}, {op: test, eq: [f1040.status, {const: "qss"}]}]}
          then: ssb.h_adjust_single
    shown_when: ssb.show_8_15
  - id: ssb.line11
    printed: "11"
    label: "Subtract line 10 from line 9. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line9, take: ssb.line10}
    shown_when: ssb.show_8_15
  - id: ssb.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line9, ssb.line10]}
    shown_when: ssb.show_8_15
  - id: ssb.line13
    printed: "13"
    label: "Enter one-half of line 12"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line12, rate: {param: ssb.half}}
    shown_when: ssb.show_8_15
  - id: ssb.line14
    printed: "14"
    label: "Enter the smaller of line 2 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line2, ssb.line13]}
    shown_when: ssb.show_8_15
  - id: ssb.line15
    printed: "15"
    label: "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line11, rate: {param: ssb.rate85}}
    shown_when: ssb.show_8_15
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.mfs_lived_together, {const: true}]}
          then: ssb.h_line16_alt
        - guard: {op: test, eq: [ssb.mfs_lived_together, {const: false}]}
          then: ssb.h_line16_normal
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
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "Base amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "Base amount for single, head of household, qualifying surviving spouse, or married filing separately lived apart"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "Adjustment amount for married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "Adjustment amount for single, head of household, qualifying surviving spouse, or married filing separately lived apart"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
  - id: ssb.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ssb.h_base_mfs
    printed: "(helper)"
    label: "Base amount for married filing separately, selected by whether the spouses lived apart for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.lived_apart, {const: true}]}
          then: ssb.h_base_single
        - guard: {op: test, eq: [ssb.lived_apart, {const: false}]}
          then: ssb.h_zero
  - id: ssb.h_adjust_mfs
    printed: "(helper)"
    label: "Adjustment amount for married filing separately, selected by whether the spouses lived apart for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.lived_apart, {const: true}]}
          then: ssb.h_adjust_single
        - guard: {op: test, eq: [ssb.lived_apart, {const: false}]}
          then: ssb.h_zero
  - id: ssb.h_line16_normal
    printed: "(helper)"
    label: "Line 16 from lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
  - id: ssb.h_line16_alt
    printed: "(helper)"
    label: "Line 16 for married filing separately who lived with the spouse at any time in 2025"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
  - id: ssb.mfs_lived_together
    printed: "(helper)"
    label: "Married filing separately and lived with the spouse at any time in 2025"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [f1040.status, {const: "mfs"}]}, {op: test, eq: [ssb.lived_apart, {const: false}]}]}
  - id: ssb.show_8_15
    printed: "(helper)"
    label: "Lines 8 through 15 are shown"
    type: Bool
    expr: {op: test, eq: [ssb.mfs_lived_together, {const: false}]}
  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Whether any social security benefits were received"
    type: Bool
    expr: {op: test, gt: [ssb.benefits, {const: 0}]}
```
