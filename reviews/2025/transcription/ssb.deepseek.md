# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b040ecec1aa71741bda4cd6a104352da44999f30cf8a1991a97afc8774b0d80f |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9c382a2bae7e78308ff9d2411b1e6225c16f6c599b0bd1817a98ce6b2e0f59a0 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | b93a8941c8753854e2828567250e8d13c5651ceddaca932ec87f5c4ec81c8d22 |
| printed lines compared | 19 |
| agree / disagree / missing | 15 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### ssb.has_benefits — Any social security benefits (otherwise the worksheet is not needed)
Status: **AGREE**

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

Second transcription's note: Sums the supplied Schedule 1 adjustment lines; refuses when scope.schedule1 is true. Schedule 1 lines 12, 14 and 23 are not supplied as separate lines.

Ruling: ambiguity (+ scope); amb.2025.ira_ssb_copy; i1040gi p. 32, worksheet line 6: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"; i1040gi p. 31, Exception: "You made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub. 590-A". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,024 of 2,038 agree; 12 candidate-unknown (10 completed), 1 candidate-refuses (none completed), 1 project-refuses (none completed). The reply reads Schedule 1 line 20 literally, the text at issue of the register. All 10 completed candidate-unknown are IRA-deduction returns with $0 benefits (stage16.ira.i1 to i5, i8 and others; project $7,000.00 to $15,000.00), where line 20 reaches the reply's line 18, which refuses ssb.pub915 on every return and so needs it. The project-refuses is ira.cov_gate and the candidate-refuses ira.less_gate on a return the project refuses at s1.line20: scope. Project stands. under the register.

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
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "ssb.base_single"}}], "op": "choose"}
```

Ruling: model error and scope; i1040gi p. 32, worksheet line 8: "Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,864 of 2,038 agree; 128 value (none completed), 46 project-unknown (none completed). The reply gives $25,000 to every status other than joint, including married filing separately having lived with the spouse, where the source skips the line; all 128 values are such returns (lived_apart false: classm.clcw26.3.deepseek, classm.eic.2.deepseek) and all are refused (s3.mfs, scope.ready), so no completed return differs. The 46 project-unknown are separate returns without the lived-apart answer, also refused: scope. Its line 16 takes line 7 times 85% for that case, so line 18 would match. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "ssb.adjust_single"}}], "op": "choose"}
```

Ruling: model error and scope; i1040gi p. 32, worksheet line 10, and line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,864 of 2,038 agree; 128 value (none completed), 46 project-unknown (none completed). The reply gives $9,000 to every status other than joint, including married filing separately having lived with the spouse, where the source skips the line; all 128 values are such returns (lived_apart false: classm.clcw26.3.deepseek, classm.eic.2.deepseek) and all are refused (s3.mfs, scope.ready), so no completed return differs. The 46 project-unknown are separate returns without the lived-apart answer, also refused: scope. Its line 16 takes line 7 times 85% for that case, so line 18 would match. Project stands.

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

Second transcription's note: Refused when ssb.pub915 or ssb.lump_sum is true; the worksheet cannot be used for the Pub. 915 exceptions or the lump-sum election.

Ruling: model error (+ scope); i1040gi p. 31, Lines 6a and 6b: "Use the Social Security Benefits Worksheet in these instructions to see if any of your benefits are taxable."; i1040gi p. 31, Line 6c: "If any of your benefits are taxable for 2025 and they include a lump-sum benefit payment that was for an earlier year, you may be able to reduce the taxable amount with the lump-sum election". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 652 of 2,038 agree; 1,161 candidate-unknown (514 completed), 222 candidate-refuses (4 completed), 3 project-refuses (none completed). No zero-benefit guard and unconditional refusals ssb.pub915 and ssb.lump_sum on line 18 (and ssb.terror_disability on line 1), so it asks the Pub. 915 screens of every return: of the 514 completed candidate-unknown, all on returns with $0 benefits (project $0.00), 490 need ssb.pub915 (classm.f2441.1.deepseek) and 24 are partial records withholding lump_sum or terror_disability; the 4 completed candidate-refuses supply ssb.pub915 true with $0 benefits, an answer the interview never asks (classm.s3.3, classm.f5695.8 and their deepseek twins). The other candidate-refuses are returns the project refuses elsewhere and the 3 project-refuses are ira.cov_gate and sb.fbar_required: scope. Same reply as earlier rounds. BUG-0249 reworded ssb.terror_disability only (eligibility for September 11 Victim Compensation Fund coverage, "whether or not you made a claim"), which matches i1040gi p. 31, Disability payments: "In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack."; no ssb expression changed. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ssb.has_benefits | ssb.terror_disability | ssb.terror_disability |
| 1 | ssb.terror_disability | ssb.terror_disability |
| 2 | ssb.terror_disability | - |
| 5 | ssb.terror_disability | - |
| 6 | scope.schedule1 | - |
| 7 | scope.schedule1, ssb.terror_disability | - |
| 9 | scope.schedule1, ssb.terror_disability | - |
| 11 | scope.schedule1, ssb.terror_disability | - |
| 12 | scope.schedule1, ssb.terror_disability | - |
| 13 | scope.schedule1, ssb.terror_disability | - |
| 14 | scope.schedule1, ssb.terror_disability | - |
| 15 | scope.schedule1, ssb.terror_disability | - |
| 16 | scope.schedule1, ssb.terror_disability | - |
| 17 | ssb.terror_disability | ssb.terror_disability |
| 18 | scope.schedule1, ssb.lump_sum, ssb.pub915, ssb.terror_disability | - |

## Raw second transcription

```yaml
lines:
  - id: ssb.line1
    printed: "1"
    label: "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099. Also enter this amount on Form 1040 or 1040-SR, line 6a."
    type: NonNegDollars
    expr:
      op: copy
      from: ssb.benefits
    refuses:
      - ssb.terror_disability
    note: "Refused when ssb.terror_disability is true because the nontaxable portion of terrorist-attack disability benefits is not a supplied amount."
  - id: ssb.line2
    printed: "2"
    label: "Multiply line 1 by 50% (0.50)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ssb.line1
      rate:
        param: ssb.half
  - id: ssb.line3
    printed: "3"
    label: "Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8"
    type: Dollars
    expr:
      op: sum
      of:
        - f1040.line1z
        - f1040.line2b
        - f1040.line3b
        - f1040.line4b
        - f1040.line5b
        - f1040.line7a
        - f1040.line8
  - id: ssb.line4
    printed: "4"
    label: "Enter the amount, if any, from Form 1040 or 1040-SR, line 2a"
    type: NonNegDollars
    expr:
      op: copy
      from: f1040.line2a
  - id: ssb.line5
    printed: "5"
    label: "Combine lines 2, 3, and 4"
    type: Dollars
    expr:
      op: sum
      of:
        - ssb.line2
        - ssb.line3
        - ssb.line4
  - id: ssb.line6
    printed: "6"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - s1.line11
        - s1.line13
        - s1.line15
        - s1.line16
        - s1.line17
        - s1.line18
        - s1.line19a
        - s1.line20
        - s1.line25
    refuses:
      - scope.schedule1
    note: "Sums the supplied Schedule 1 adjustment lines; refuses when scope.schedule1 is true. Schedule 1 lines 12, 14 and 23 are not supplied as separate lines."
  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? Yes. Subtract line 6 from line 5"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: ssb.line5
      take: ssb.line6
    note: "If line 6 is not less than line 5, the worksheet stops with no taxable benefits; subtract_floor0 makes line 7 zero and downstream lines zero."
  - id: ssb.line8
    printed: "8"
    label: "Enter $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq:
              - f1040.status
              - const: "mfj"
          then: ssb.h_base_joint
        - guard:
            op: test
            not:
              op: test
              eq:
                - f1040.status
                - const: "mfj"
          then: ssb.h_base_single
    shown_when: ssb.h_show_8_15
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? Yes. Subtract line 8 from line 7"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: ssb.line7
      take: ssb.line8
    shown_when: ssb.h_show_8_15
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq:
              - f1040.status
              - const: "mfj"
          then: ssb.h_adjust_joint
        - guard:
            op: test
            not:
              op: test
              eq:
                - f1040.status
                - const: "mfj"
          then: ssb.h_adjust_single
    shown_when: ssb.h_show_8_15
  - id: ssb.line11
    printed: "11"
    label: "Subtract line 10 from line 9. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: ssb.line9
      take: ssb.line10
    shown_when: ssb.h_show_8_15
  - id: ssb.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 10"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ssb.line9
        - ssb.line10
    shown_when: ssb.h_show_8_15
  - id: ssb.line13
    printed: "13"
    label: "Enter one-half of line 12"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ssb.line12
      rate:
        param: ssb.half
    shown_when: ssb.h_show_8_15
  - id: ssb.line14
    printed: "14"
    label: "Enter the smaller of line 2 or line 13"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ssb.line2
        - ssb.line13
    shown_when: ssb.h_show_8_15
  - id: ssb.line15
    printed: "15"
    label: "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ssb.line11
      rate:
        param: ssb.rate85
    shown_when: ssb.h_show_8_15
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq:
              - ssb.h_show_8_15
              - const: false
          then: ssb.h_mfs_16
        - guard:
            op: test
            eq:
              - ssb.h_show_8_15
              - const: true
          then: ssb.h_16_normal
    note: "For married filing separately who lived with spouse at any time in 2025, the worksheet skips lines 8 through 15 and line 16 is 85% of line 7; otherwise it is lines 14 plus 15."
  - id: ssb.line17
    printed: "17"
    label: "Multiply line 1 by 85% (0.85)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ssb.line1
      rate:
        param: ssb.rate85
  - id: ssb.line18
    printed: "18"
    label: "Taxable social security benefits. Enter the smaller of line 16 or line 17. Also enter this amount on Form 1040 or 1040-SR, line 6b"
    type: NonNegDollars
    expr:
      op: smaller_of
      of:
        - ssb.line16
        - ssb.line17
    refuses:
      - ssb.pub915
      - ssb.lump_sum
    note: "Refused when ssb.pub915 or ssb.lump_sum is true; the worksheet cannot be used for the Pub. 915 exceptions or the lump-sum election."
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "Constant helper: $32,000 base amount for married filing jointly"
    type: NonNegDollars
    expr:
      op: param
      ref: ssb.base_joint
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "Constant helper: $25,000 base amount for other statuses or married filing separately lived apart"
    type: NonNegDollars
    expr:
      op: param
      ref: ssb.base_single
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "Constant helper: $12,000 adjustment for married filing jointly"
    type: NonNegDollars
    expr:
      op: param
      ref: ssb.adjust_joint
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "Constant helper: $9,000 adjustment for other statuses or married filing separately lived apart"
    type: NonNegDollars
    expr:
      op: param
      ref: ssb.adjust_single
  - id: ssb.h_mfs_16
    printed: "(helper)"
    label: "Helper: line 7 multiplied by 85% for married filing separately who lived with spouse"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: ssb.line7
      rate:
        param: ssb.rate85
  - id: ssb.h_16_normal
    printed: "(helper)"
    label: "Helper: sum of lines 14 and 15"
    type: NonNegDollars
    expr:
      op: sum
      of:
        - ssb.line14
        - ssb.line15
  - id: ssb.h_show_8_15
    printed: "(helper)"
    label: "Helper: true unless married filing separately and did not live apart from spouse all year"
    type: Bool
    expr:
      op: test
      not:
        op: test
        all:
          - op: test
            eq:
              - f1040.status
              - const: "mfs"
          - op: test
            eq:
              - ssb.lived_apart
              - const: false
  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Whether any social security benefits are reported on line 1"
    type: Bool
    expr:
      op: test
      gt:
        - ssb.line1
        - const: 0
    note: "The IRS pages do not define a separate has_benefits flag; read as line 1 greater than zero (any benefits), not whether the benefits are taxable."
```
