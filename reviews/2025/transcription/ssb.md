# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | b93a8941c8753854e2828567250e8d13c5651ceddaca932ec87f5c4ec81c8d22 |
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

Second transcription's note: The pages do not define this interface. Chosen reading: the total of box 5 entered for line 1 is more than zero.

Ruling: representation; i1040gi p. 31, Lines 6a and 6b: "Use the Social Security Benefits Worksheet in these instructions to see if any of your benefits are taxable.". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,038 of 2,038 agree. The project tests line 1, a copy of ssb.benefits; the candidate tests ssb.benefits. Project stands.

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

Second transcription's note: Schedule 1 lines 12, 14 and 23 are outside the tool's scope (scope.schedule1), so that screen is listed under refuses and they are not added. The catalog has line 19a for line 19. Line 25 is read as the catalog's s1.line25, which is taken to include any line 24z write-in.

Ruling: ambiguity (+ model error, scope); amb.2025.ira_ssb_copy; i1040gi p. 32, worksheet line 6: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"; i1040gi p. 31, Exception: "You made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub. 590-A". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,024 of 2,038 agree; 12 candidate-unknown (10 completed), 1 candidate-refuses (none completed), 1 project-refuses (none completed). The reply reads Schedule 1 line 20 literally, the text at issue of the register; the owner's chosen reading reads the worksheet's own copy (ssb.ira_line20, person.ira_ssb) because line 20 depends on Form 1040 line 9 and so on the taxable benefits. The other operands are the project's (lines 12, 14 and 23 refused by scope.schedule1). All 10 completed candidate-unknown are IRA-deduction returns with $0 benefits, project $7,000.00 to $15,000.00: 4 report the cycle the register resolves ("cycle at ssb.line6": stage16.ira.i1, stage16.ira.i8, stage16.mut.ira_joint_full_edge, audit.ira.covered_age50_joint_phaseout) and 6 reach, through line 20, the IRA worksheet's Form 1040 line 9 and the reply's line 18, which has no zero-benefit guard and needs f1040.tax_exempt_interest (stage16.ira.i2 to i5, audit.ira.covered_age50_single_phaseout, stage19.mut.ira_single_full_edge). The project-refuses is the copy's ira.cov_gate (stage16.refuse.ira.ssb_covered) and the candidate-refuses ira.less_gate on stage16.refuse.ira.deduct_less, a return the project refuses at s1.line20 (checked: Form 1040 line 24 refused on ira.less_gate): scope. Project stands. under the register.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}], "op": "choose"}
```

Second transcription's note: The worksheet gives no value for skipped lines. Chosen reading: lines 8 through 15 are zero on the skip branch, and line 16 reads line 7 directly.

Ruling: representation; i1040gi p. 32, worksheet line 8: "Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,038 of 2,038 agree. $32,000 joint, $25,000 single, head of household, qualifying surviving spouse or separate-and-apart, zero on the skipped line for separate-and-together; guards grouped differently. Project stands.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line
Status: **DISAGREE**

Project:

```json
{"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "8"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "8"}}}], "op": "choose"}
```

Second transcription's note: The STOP on 'No' is carried by the floor: line 9 is zero, so lines 11 through 16 and line 18 are zero.

Ruling: representation and scope; i1040gi p. 32, worksheet line 9; i1040gi p. 32, worksheet line 8: "Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16"; i1040gi p. 31, Lines 6a and 6b: "Use the Social Security Benefits Worksheet in these instructions to see if any of your benefits are taxable.". executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,427 of 2,038 agree; 477 project-unknown (312 completed), 68 project-refuses (4 completed), 65 value (none completed), 1 candidate-refuses (none completed). (1) Completed returns: all 312 project-unknown and the 4 project-refuses are returns with $0 benefits, where the worksheet is not used and line 18 is $0 on both sides through ssb.has_benefits. The project's line 2 carries the refusals ssb.pub915, ssb.lump_sum and ssb.terror_disability, which the interview asks only when there are benefits: 288 are base records without those answers (classm.f2441.1.deepseek and others), 24 are partial records withholding lump_sum (12) or terror_disability (12), and the 4 project-refuses (classm.s3.3, classm.f5695.8 and their deepseek twins) supply ssb.pub915 true with $0 benefits, an answer the interview never asks (checked on classm.s3.3: withheld, the interview completes). The project shows no amount on line 9 there and no printed Form 1040 amount differs. (2) The 65 values are all married filing separately having lived with the spouse (lived_apart false), where the source skips lines 8 through 15: the project shows line 7 less $0, the candidate $0; every one is refused (s3.mfs and other cited gates), as the earlier render ruling found; line 16 takes line 7 times 85% on both. The other project-refuses and project-unknown are on refused or incomplete returns: scope. BUG-0249 reworded ssb.terror_disability only (eligibility for September 11 Victim Compensation Fund coverage, "whether or not you made a claim"), which matches i1040gi p. 31, Disability payments: "In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack."; no ssb expression changed. Project stands.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"param": "ssb.adjust_single"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 32, worksheet line 10. executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,038 of 2,038 agree. Same status mapping ($12,000 / $9,000 / zero on the skipped line); guards grouped differently. Project stands.

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

Ruling: model error and ambiguity (+ scope); i1040gi p. 31, Lines 6a and 6b: "Use the Social Security Benefits Worksheet in these instructions to see if any of your benefits are taxable."; i1040gi p. 31, Line 6c: "If any of your benefits are taxable for 2025 and they include a lump-sum benefit payment that was for an earlier year, you may be able to reduce the taxable amount with the lump-sum election"; amb.2025.ira_ssb_copy. executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`; 1,382 fixtures, 500 generated returns seed 20261026, 156 partial records from 40 bases; 2,038 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,142 of 2,038 agree; 540 candidate-unknown (202 completed), 354 candidate-refuses (none completed), 2 project-refuses (none completed). The reply has no zero-benefit guard, so on a return without benefits it figures the whole worksheet and needs answers the source does not need there: 198 of the 202 completed candidate-unknown need f1040.tax_exempt_interest through line 4 (classm.f5695.5.deepseek and others, all with $0 benefits, project $0.00); the other 4 are the line 6 cycle of the register (stage16.ira.i1, i8, stage16.mut.ira_joint_full_edge, audit.ira.covered_age50_joint_phaseout). The 354 candidate-refuses are returns the project refuses elsewhere, met because the reply reads the Form 1040 income lines on every return (sales.digital, sb.unsupported, sb.line8, plan_screened and others): scope. The 2 project-refuses are ira.cov_gate (stage16.refuse.ira.ssb_covered) and sb.fbar_required on a partial of classm.dcprov.1: scope. BUG-0249 reworded ssb.terror_disability only (eligibility for September 11 Victim Compensation Fund coverage, "whether or not you made a claim"), which matches i1040gi p. 31, Disability payments: "In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack."; no ssb expression changed. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 2 | ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 5 | ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 6 | scope.schedule1 | - |
| 7 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 9 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 11 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 12 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 13 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 14 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 15 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 16 | scope.schedule1, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 17 | ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_pub915_gate, ssb.h_terror_gate |
| 18 | scope.schedule1, ssb.h_lump_gate, ssb.h_pub915_gate, ssb.h_terror_gate | ssb.h_lump_gate, ssb.h_pub915_gate, ssb.h_terror_gate |

## Raw second transcription

```yaml
lines:
  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Any amount in box 5 of your Forms SSA-1099 and RRB-1099"
    type: Bool
    expr: {op: test, gt: [ssb.benefits, {const: 0}]}
    note: "The pages do not define this interface. Chosen reading: the total of box 5 entered for line 1 is more than zero."
  - id: ssb.h_pub915_gate
    printed: "(helper)"
    label: "Benefits were received and an Exception in the line 6a and 6b instructions applies (use Pub. 590-A or Pub. 915 instead of this worksheet)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.has_benefits, {const: true}]}
        - {op: test, eq: [ssb.pub915, {const: true}]}
    note: "The Exception concerns using this worksheet to see whether benefits are taxable, so the refusal is limited to filers with benefits. Otherwise a filer with no benefits who made IRA contributions would be refused. A filer whose repayments exceed benefits and who enters zero is not refused and gets zero taxable, which matches 'None of your benefits are taxable'; the possible deduction or credit for excess repayments is not figured."
  - id: ssb.h_terror_gate
    printed: "(helper)"
    label: "Benefits were received and they include disability payments for injuries incurred as a direct result of a terrorist attack"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.has_benefits, {const: true}]}
        - {op: test, eq: [ssb.terror_disability, {const: true}]}
  - id: ssb.h_lump_gate
    printed: "(helper)"
    label: "Benefits were received and you elect the lump-sum election method (Pub. 915)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.has_benefits, {const: true}]}
        - {op: test, eq: [ssb.lump_sum, {const: true}]}
  - id: ssb.h_mfs_together
    printed: "(helper)"
    label: "Married filing separately and you lived with your spouse at any time in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [ssb.lived_apart, {const: false}]}
  - id: ssb.h_zero
    printed: "(helper)"
    label: "Zero, for lines skipped by a married person filing separately who lived with their spouse"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ssb.line1
    printed: "1"
    label: "Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099. Also enter this amount on Form 1040 or 1040-SR, line 6a"
    type: NonNegDollars
    expr: {op: copy, from: ssb.benefits}
    refuses: [ssb.h_pub915_gate, ssb.h_terror_gate]
    note: "The instructions exclude terrorist-attack disability payments from income, but box 5 may include them. The closed interface has no input for the excluded part, so this case refuses."
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
    note: "Schedule 1 lines 12, 14 and 23 are outside the tool's scope (scope.schedule1), so that screen is listed under refuses and they are not added. The catalog has line 19a for line 19. Line 25 is read as the catalog's s1.line25, which is taken to include any line 24z write-in."
  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? No: None of your social security benefits are taxable; enter -0- on Form 1040 or 1040-SR, line 6b. Yes: Subtract line 6 from line 5"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line5, take: ssb.line6}
    note: "The STOP on 'No' is carried by the floor: line 7 is zero, so every later line, including line 18, is zero."
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "$32,000 if married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "$25,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
  - id: ssb.line8
    printed: "8"
    label: "If you are: Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_base_joint
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: true}]}
          then: ssb.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfj"}]}
              - {op: test, eq: [ssb.h_mfs_together, {const: false}]}
          then: ssb.h_base_single
    note: "The worksheet gives no value for skipped lines. Chosen reading: lines 8 through 15 are zero on the skip branch, and line 16 reads line 7 directly."
  - id: ssb.h_line9_figured
    printed: "(helper)"
    label: "Subtract line 8 from line 7, or zero if line 8 is not less than line 7"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? No: None of your social security benefits are taxable; enter -0- on Form 1040 or 1040-SR, line 6b. If you are married filing separately and you lived apart from your spouse for all of 2025, be sure you checked the box on line 6d. Yes: Subtract line 8 from line 7"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: true}]}
          then: ssb.h_zero
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: false}]}
          then: ssb.h_line9_figured
    note: "The STOP on 'No' is carried by the floor: line 9 is zero, so lines 11 through 16 and line 18 are zero."
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "$12,000 if married filing jointly"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "$9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_adjust_joint
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: true}]}
          then: ssb.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfj"}]}
              - {op: test, eq: [ssb.h_mfs_together, {const: false}]}
          then: ssb.h_adjust_single
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
  - id: ssb.h_line16_sum
    printed: "(helper)"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
  - id: ssb.h_line16_mfs
    printed: "(helper)"
    label: "Multiply line 7 by 85% (0.85) (married filing separately and you lived with your spouse at any time in 2025)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: true}]}
          then: ssb.h_line16_mfs
        - guard: {op: test, eq: [ssb.h_mfs_together, {const: false}]}
          then: ssb.h_line16_sum
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
    refuses: [ssb.h_lump_gate]
```
