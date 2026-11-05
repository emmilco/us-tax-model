# Transcription agreement — ssb

Second transcription of `Social Security Benefits Worksheet—Lines 6a and 6b` by an isolated model (spec 6.5), compared line by line with `forms/2025/ssb.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 1027671bb973b7314ee64c4fc9691d23bc43e0171870bc504f443ca96d4ce18a |
| printed lines compared | 19 |
| agree / disagree / missing | 6 / 13 / 0 |
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

Second transcription's note: The catalog does not supply Schedule 1 lines 12, 14 and 23. Adjustments on those lines are refused by scope.schedule1, so the line adds only the supplied lines 11, 13, 15 to 20 (19a) and 25.

Ruling: ambiguity (+ model error, scope); amb.2025.ira_ssb_copy; i1040gi p. 32, worksheet line 6: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"; i1040gi p. 31, Exception (traditional IRA with plan coverage: "use the worksheets in Pub. 590-A"). executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 128 partial records from 40 bases; 2,193 comparisons): 2,179 agree; 12 candidate-unknown, 1 candidate-refuses, 1 project-refuses (none on a completed return). Project and reply are the same as at the before-catalog-refresh ruling (fixr2), which stands: the reply reads s1.line20 literally, the text at issue of the register, and its differences are the register's cycle and refused IRA returns; none is on a completed return. Project stands.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"from": {"line": "5"}, "op": "subtract_floor0", "take": {"line": "6"}}}
```

Second:

```json
{"shown_when": {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}, "value": {"from": {"line": "5"}, "op": "subtract_floor0", "take": {"line": "6"}}}
```

Second transcription's note: On the No answer (STOP) this line is zero. All later lines then figure zero, and line 18 is set to zero explicitly.

Ruling: representation and scope; i1040gi p. 32, worksheet line 7; i1040gi p. 32, lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. STOP"; owner's decision (2026-10-26) that a worksheet after a STOP counts as skipped. executable-triage-v2 (`reviews/2025/transcription/triage/ssb.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 128 partial records from 40 bases; 2,193 comparisons): 2,170 agree; 18 project-unknown, 4 project-refuses, 1 candidate-refuses (on completed returns: 10 project-unknown). Both subtract line 6 from line 5 floored at zero; the reply hides the line on the STOP where the project shows $0 (the STOP is met by line 18's $0). The project-unknown witnesses are partial records withholding ssb.lump_sum, the project's line 2 gate (i1040gi p. 31, Line 6c: "you may be able to reduce the taxable amount with the lump-sum election"), which the interview asks whenever there are benefits; the project-refuses are that gate (stage10.refuse.lump_sum) and ira.cov_gate (stage16.refuse.ira.ssb_covered), the candidate-refuses ira.less_gate on stage16.refuse.ira.deduct_less, a return the project refuses at s1.line20: scope. Project stands.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"param": "ssb.base_single"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.base_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.base_joint"}}], "op": "choose"}
```

Second transcription's note: Lines 8-15 are skipped for married filing separately living with spouse; the skipped lines carry zero (not shown) and line 16 uses line 7 x 85% directly.

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's amounts are the project's ($32,000 joint; $25,000 single, head of household, qualifying surviving spouse or separate living apart; zero for separate living together) and its display condition (not stopped at line 7, not separate living together) is the project's ssb.show8_9 (lines 8 to 15 not skipped and line 7 above zero), the round-2 display fix (A2, SSB-L1). The earlier model error (the $25,000 shown for a separate filer living together) is gone. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "8"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "8"}}}
```

Second transcription's note: On the STOP branch (line 8 not less than line 7) the line is not shown and its value is zero; the STOP is carried to line 18 as zero through ssb.h_show16.

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply shows line 9 only when line 6 is less than line 5 and line 8 less than line 7; the project shows it under ssb.show8_9, so on the line 9 No branch the project shows $0 where the reply hides the line. Both values are $0 there and no nonzero amount is shown past a STOP (the owner's rule); line 7 above zero is the same test as line 6 less than line 5. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}, "then": {"param": "ssb.adjust_single"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "ssb.adjust_single"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "ssb.adjust_joint"}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "all"}, "value": {"from": {"line": "9"}, "op": "subtract_floor0", "take": {"line": "10"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"from": {"line": "9"}, "op": "subtract_floor0", "take": {"line": "10"}}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 12 — Enter the smaller of line 9 or line 10
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "all"}, "value": {"of": [{"line": "10"}, {"line": "9"}], "op": "smaller_of"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"of": [{"line": "10"}, {"line": "9"}], "op": "smaller_of"}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 13 — Enter one-half of line 12
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "all"}, "value": {"amount": {"line": "12"}, "op": "multiply_rate", "rate": {"param": "ssb.half"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"amount": {"line": "12"}, "op": "multiply_rate", "rate": {"param": "ssb.half"}}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 14 — Enter the smaller of line 2 or line 13
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "all"}, "value": {"of": [{"line": "13"}, {"line": "2"}], "op": "smaller_of"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"of": [{"line": "13"}, {"line": "2"}], "op": "smaller_of"}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "all"}, "value": {"amount": {"line": "11"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"amount": {"line": "11"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply's value is the project's and its display condition (not separate living together, line 6 less than line 5, line 8 less than line 7) is the project's ssb.show10_15 (ssb.show8_9 and line 9 above zero): line 7 above zero is line 6 less than line 5, line 9 above zero is line 8 less than line 7. This is the round-2 display fix (A2, SSB-L1); the refresh round's low finding (amounts shown after the line 9 STOP) is resolved. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse at any ti
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "7"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"line": "14"}, {"line": "15"}], "op": "sum"}}], "op": "choose"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}], "test": "any"}, "value": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"line": "7"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"line": "14"}, {"line": "15"}], "op": "sum"}}], "op": "choose"}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". Value as the project; the reply shows the line when (line 6 less than line 5 and line 8 less than line 7, not separate living together) or (separate living together and line 6 less than line 5), the project's ssb.show16_18 (line 7 above zero, and line 9 above zero or married separately living together). The refresh round's SSB-L1 low (line 17 shown after a STOP) is fixed by ssb.show16_18 and the reply agrees. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 17 — Multiply line 1 by 85% (0.85)
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0}, {"line": "9"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0}, {"line": "7"}], "test": "lt"}], "test": "all"}, "value": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}], "test": "any"}, "value": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "ssb.rate85"}}}
```

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". Value as the project; the reply shows the line when (line 6 less than line 5 and line 8 less than line 7, not separate living together) or (separate living together and line 6 less than line 5), the project's ssb.show16_18 (line 7 above zero, and line 9 above zero or married separately living together). The refresh round's SSB-L1 low (line 17 shown after a STOP) is fixed by ssb.show16_18 and the reply agrees. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"line": "17"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"line": "5"}, {"line": "6"}], "test": "le"}], "test": "any"}, {"args": [{"line": "7"}, {"line": "8"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "5"}, {"line": "6"}], "test": "le"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "8"}, {"line": "7"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "ssb.lived_apart"}], "test": "eq"}], "test": "all"}, {"args": [{"line": "6"}, {"line": "5"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"of": [{"line": "16"}, {"line": "17"}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: The STOPs at lines 7 and 9 ('None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b') are carried here as zero. The Exception (use Pub. 590-A or Pub. 915 instead of this worksheet) and the lump-sum election (Pub. 915), which may reduce the taxable amount, are refused rather than computed.

Ruling: representation; i1040gi p. 32, worksheet lines 7 and 9: "No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b." (STOP); line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16". The reply enters zero on the two STOP branches and the smaller of lines 16 and 17 otherwise; the project enters zero when line 1 is zero and the smaller otherwise. On a STOP branch lines 9 to 16 are zero (line 7 or line 9 is zero), so the smaller is zero too, and with no benefits line 17 is zero; the values are the same on every supported return. Both refuse on ssb.lump_sum and ssb.pub915. Married filing separately is refused for the return (scope, s3.mfs), so the married-separately branches differ only on refused returns.
Reviewed in: pass 487053a95b5c

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ssb.has_benefits | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 1 | ssb.pub915, ssb.terror_disability | ssb.pub915, ssb.terror_disability |
| 2 | ssb.pub915, ssb.terror_disability | - |
| 5 | ssb.pub915, ssb.terror_disability | - |
| 6 | scope.schedule1 | - |
| 7 | scope.schedule1, ssb.pub915, ssb.terror_disability | - |
| 18 | ssb.lump_sum, ssb.pub915 | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| ssb.has_benefits | 93481a8c549c4df9d5ce12871063ca88c64c3091e445ec5c540a5cecdd71d515 |
| 1 | 45def37aa3aecf4ad79cefdd2a4005e6ea916f8744e6dea254afc3e46094b96f |
| 2 | d095b9bc8aac89a330dd5fec26f41ce3fa3595a093d7e5907468418c1b8f14af |
| 3 | a2cdc624483dc3839e03343dd07ddfb7623427bbf7aa11fb62374dee4811a8b2 |
| 4 | 42300b844db21a635dc8e82a1e4d71f9b7283c6a1e2bd8fb6ec5a74033fc97ab |
| 5 | 3e4a2531fb2be20399d6f85aba35256f4eca403025eb075ec52e40d16a4e1c80 |
| 6 | deef4de6a4fd25a945cf3bb74ce0fc578c5e58a3c5210654fb0dd898ab3cacdc |
| 7 | e59f41f1df031a58a03a97e996219fd4851157b0c87f3affa2facb6e5a6d158c |
| 8 | 07bd8d386352cb80119681401d350cadf1e8702210b7b1eae3783510c18edaf0 |
| 9 | a1397e2d3a2d1417aabe2c15e3acf1eded91578a4dac7e7083f2d8703f67ab84 |
| 10 | bf089b8baa1a5eab694945a6842b1102675a6cc4dcf302431bc60d5ef95f403a |
| 11 | 837116c091ede57b6e1a4c3219f9ecfe1d6c60bb2af8fc84100a07dc8dd626c8 |
| 12 | dd2ce693f367b125bb1a8e984aeca4ae5f90dd5c94ea5f0661c865d02f33749b |
| 13 | b6305733ed989d29dbf805295e74fb2d5893ac48131b5de372488c910c6d9ec5 |
| 14 | 54eaa7d1fa6b7a4015d4aab54b93a21eb8e96e307ae1c58951bbaa959171ea96 |
| 15 | 447d8b45e08fc9c639a34804ef26dfafab56aa2ddd15bbf0b8f720dff325792d |
| 16 | a5eefa5809260ba328f3bd31fdfed11347fa431cff136ca1a473b43e6e69693c |
| 17 | 73c01263ad0ade3d851f94d83baa381a2e2b90609fdad1c53b5c0169bbeb69b3 |
| 18 | 35cccd5d4989fa7e6594636cd1ad40729702d27805e1f6d2e4fd2d9a95afb556 |
| (rest of the document) | f27ed8c32596d66063a07d65a0895977e0afa69acc647b72c1b05da4f85fa713 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 8 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 9 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 10 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 11 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 12 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 13 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 14 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 15 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 16 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 17 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |
| 18 | ad8e00727a9a39754a9c3e95d414cca1d549dfbefe2fa2bdbdc509bb3fbcc411 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 487053a95b5c

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 487053a95b5c85583184c4e1139fbb1b394ea8189c449669decf20acbd2486cd |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 8d72724d7c7830c32125dc113854b12aa74511e1f09b9abf8b793012fe7f75f3 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7c3730bc8de043be939dd70f32c31bfe079358aa5e4729e359bf859a5ffc547b |
| receipt | .transcription/ssb.lines-38ff4c33403d |
| printed lines compared | 11 |
| agree / disagree / missing | 0 / 11 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, g28, household, s1, sales, scope, sdtw, u1250 |
| named line | eic, f8960, sa |
| shared page | f1040, ira, person, retirement, sd |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: ssb.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "$32,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
  - id: ssb.h_base_single
    printed: "(helper)"
    label: "$25,000 (single, head of household, qualifying surviving spouse, or married filing separately and lived apart from spouse all of 2025)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "$12,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "$9,000 (single, head of household, qualifying surviving spouse, or married filing separately and lived apart from spouse all of 2025)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
  - id: ssb.h_mfs_with
    printed: "(helper)"
    label: "Married filing separately and you lived with your spouse at any time in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [ssb.lived_apart, {const: false}]}
  - id: ssb.h_stop7
    printed: "(helper)"
    label: "Line 7: Is the amount on line 6 less than the amount on line 5? No (STOP: none of your social security benefits are taxable)"
    type: Bool
    expr: {op: test, ge: [ssb.line6, ssb.line5]}
  - id: ssb.h_show8
    printed: "(helper)"
    label: "Lines 8 through 15 are reached (not stopped at line 7, and not married filing separately living with spouse)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.h_stop7, {const: false}]}
        - {op: test, eq: [ssb.h_mfs_with, {const: false}]}
  - id: ssb.h_show9
    printed: "(helper)"
    label: "Line 9: Is the amount on line 8 less than the amount on line 7? Yes (lines 9 through 15 are reached)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.h_show8, {const: true}]}
        - {op: test, lt: [ssb.line8, ssb.line7]}
  - id: ssb.h_show16
    printed: "(helper)"
    label: "Lines 16 through 18 are reached (no STOP at line 7 or line 9)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ssb.h_show9, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [ssb.h_stop7, {const: false}]}
            - {op: test, eq: [ssb.h_mfs_with, {const: true}]}
  - id: ssb.line8
    printed: "8"
    label: "If you are: Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_base_joint
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "single"}]}
              - {op: test, eq: [f1040.status, {const: "hoh"}]}
              - {op: test, eq: [f1040.status, {const: "qss"}]}
              - op: test
                all:
                  - {op: test, eq: [f1040.status, {const: "mfs"}]}
                  - {op: test, eq: [ssb.lived_apart, {const: true}]}
          then: ssb.h_base_single
        - guard: {op: test, eq: [ssb.h_mfs_with, {const: true}]}
          then: ssb.h_zero
    shown_when: ssb.h_show8
    note: "Lines 8-15 are skipped for married filing separately living with spouse; the skipped lines carry zero (not shown) and line 16 uses line 7 x 85% directly."
  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? No. STOP None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. Yes. Subtract line 8 from line 7"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
    shown_when: ssb.h_show9
    note: "On the STOP branch (line 8 not less than line 7) the line is not shown and its value is zero; the STOP is carried to line 18 as zero through ssb.h_show16."
  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: ssb.h_adjust_joint
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "single"}]}
              - {op: test, eq: [f1040.status, {const: "hoh"}]}
              - {op: test, eq: [f1040.status, {const: "qss"}]}
              - op: test
                all:
                  - {op: test, eq: [f1040.status, {const: "mfs"}]}
                  - {op: test, eq: [ssb.lived_apart, {const: true}]}
          then: ssb.h_adjust_single
        - guard: {op: test, eq: [ssb.h_mfs_with, {const: true}]}
          then: ssb.h_zero
    shown_when: ssb.h_show9
  - id: ssb.line11
    printed: "11"
    label: "Subtract line 10 from line 9. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line9, take: ssb.line10}
    shown_when: ssb.h_show9
  - id: ssb.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line9, ssb.line10]}
    shown_when: ssb.h_show9
  - id: ssb.line13
    printed: "13"
    label: "Enter one-half of line 12"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line12, rate: {param: ssb.half}}
    shown_when: ssb.h_show9
  - id: ssb.line14
    printed: "14"
    label: "Enter the smaller of line 2 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line2, ssb.line13]}
    shown_when: ssb.h_show9
  - id: ssb.line15
    printed: "15"
    label: "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line11, rate: {param: ssb.rate85}}
    shown_when: ssb.h_show9
  - id: ssb.h_line16_mfs
    printed: "(helper)"
    label: "Married filing separately and lived with spouse at any time in 2025: multiply line 7 by 85% (0.85)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
  - id: ssb.h_line16_sum
    printed: "(helper)"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
  - id: ssb.line16
    printed: "16"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_mfs_with, {const: true}]}
          then: ssb.h_line16_mfs
        - guard: {op: test, eq: [ssb.h_mfs_with, {const: false}]}
          then: ssb.h_line16_sum
    shown_when: ssb.h_show16
  - id: ssb.line17
    printed: "17"
    label: "Multiply line 1 by 85% (0.85)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.rate85}}
    shown_when: ssb.h_show16
  - id: ssb.h_line18_figured
    printed: "(helper)"
    label: "The smaller of line 16 or line 17"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line16, ssb.line17]}
  - id: ssb.line18
    printed: "18"
    label: "Taxable social security benefits. Enter the smaller of line 16 or line 17. Also enter this amount on Form 1040 or 1040-SR, line 6b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_show16, {const: true}]}
          then: ssb.h_line18_figured
        - guard: {op: test, eq: [ssb.h_show16, {const: false}]}
          then: ssb.h_zero
    refuses: [ssb.pub915, ssb.lump_sum]
    shown_when: ssb.h_show16
    note: "The STOPs at lines 7 and 9 ('None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b') are carried here as zero. The Exception (use Pub. 590-A or Pub. 915 instead of this worksheet) and the lump-sum election (Pub. 915), which may reduce the taxable amount, are refused rather than computed."
```
```

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
    cite: "i1040gi 2025 p. 32, Social Security Benefits Worksheet line 1; p. 31 Exception and Disability payments"
    note: "The Exception says not to use this worksheet when the Pub. 915 / Pub. 590-A situations apply. Terrorist-attack disability payments must be left out of income, which this worksheet does not figure. Both screening inputs refuse here."

  - id: ssb.line2
    printed: "2"
    label: "Multiply line 1 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.half}}
    cite: "i1040gi 2025 p. 32, line 2"

  - id: ssb.line3
    printed: "3"
    label: "Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8"
    type: Dollars
    expr: {op: sum, of: [f1040.line1z, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line7a, f1040.line8]}
    cite: "i1040gi 2025 p. 32, line 3"

  - id: ssb.line4
    printed: "4"
    label: "Enter the amount, if any, from Form 1040 or 1040-SR, line 2a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line2a}
    cite: "i1040gi 2025 p. 32, line 4"

  - id: ssb.line5
    printed: "5"
    label: "Combine lines 2, 3, and 4"
    type: Dollars
    expr: {op: sum, of: [ssb.line2, ssb.line3, ssb.line4]}
    cite: "i1040gi 2025 p. 32, line 5"

  - id: ssb.line6
    printed: "6"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr: {op: sum, of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line20, s1.line25]}
    refuses: [scope.schedule1]
    cite: "i1040gi 2025 p. 32, line 6"
    note: "The catalog does not supply Schedule 1 lines 12, 14 and 23. Adjustments on those lines are refused by scope.schedule1, so the line adds only the supplied lines 11, 13, 15 to 20 (19a) and 25."

  - id: ssb.h_reach7
    printed: "(helper)"
    label: "Is the amount on line 6 less than the amount on line 5?"
    type: Bool
    expr: {op: test, lt: [ssb.line6, ssb.line5]}
    cite: "i1040gi 2025 p. 32, line 7"

  - id: ssb.line7
    printed: "7"
    label: "Is the amount on line 6 less than the amount on line 5? No. STOP None of your social security benefits are taxable. Yes. Subtract line 6 from line 5"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line5, take: ssb.line6}
    shown_when: ssb.h_reach7
    cite: "i1040gi 2025 p. 32, line 7"
    note: "On the No answer (STOP) this line is zero. All later lines then figure zero, and line 18 is set to zero explicitly."

  - id: ssb.h_mfs_together
    printed: "(helper)"
    label: "Married filing separately and you lived with your spouse at any time in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [ssb.lived_apart, {const: false}]}
    cite: "i1040gi 2025 p. 32, line 8, third bullet"

  - id: ssb.h_show8
    printed: "(helper)"
    label: "Line 8 is reached and not skipped"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.h_reach7, {const: true}]}
        - {op: test, not: {op: test, eq: [ssb.h_mfs_together, {const: true}]}}
    cite: "i1040gi 2025 p. 32, lines 7 and 8"

  - id: ssb.h_is_mfj
    printed: "(helper)"
    label: "Married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}
    cite: "i1040gi 2025 p. 32, lines 8 and 10"

  - id: ssb.h_base_joint
    printed: "(helper)"
    label: "$32,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_joint}
    cite: "i1040gi 2025 p. 32, line 8"

  - id: ssb.h_base_single
    printed: "(helper)"
    label: "$25,000 (single, head of household, qualifying surviving spouse, or married filing separately and lived apart all year)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.base_single}
    cite: "i1040gi 2025 p. 32, line 8"

  - id: ssb.line8
    printed: "8"
    label: "If you are: Married filing jointly, enter $32,000; Single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025, enter $25,000; Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_is_mfj, {const: true}]}
          then: ssb.h_base_joint
        - guard: {op: test, eq: [ssb.h_is_mfj, {const: false}]}
          then: ssb.h_base_single
    shown_when: ssb.h_show8
    cite: "i1040gi 2025 p. 32, line 8"
    note: "When married filing separately and living together, the line is skipped. Its value is computed but not used, because line 16 takes the 85% branch."

  - id: ssb.h_reach9
    printed: "(helper)"
    label: "Is the amount on line 8 less than the amount on line 7? (Yes)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ssb.h_show8, {const: true}]}
        - {op: test, lt: [ssb.line8, ssb.line7]}
    cite: "i1040gi 2025 p. 32, line 9"

  - id: ssb.line9
    printed: "9"
    label: "Is the amount on line 8 less than the amount on line 7? No. STOP None of your social security benefits are taxable. Yes. Subtract line 8 from line 7"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line7, take: ssb.line8}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 9"

  - id: ssb.h_adjust_joint
    printed: "(helper)"
    label: "$12,000 (married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_joint}
    cite: "i1040gi 2025 p. 32, line 10"

  - id: ssb.h_adjust_single
    printed: "(helper)"
    label: "$9,000 (other statuses)"
    type: NonNegDollars
    expr: {op: param, ref: ssb.adjust_single}
    cite: "i1040gi 2025 p. 32, line 10"

  - id: ssb.line10
    printed: "10"
    label: "Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and you lived apart from your spouse for all of 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_is_mfj, {const: true}]}
          then: ssb.h_adjust_joint
        - guard: {op: test, eq: [ssb.h_is_mfj, {const: false}]}
          then: ssb.h_adjust_single
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 10"

  - id: ssb.line11
    printed: "11"
    label: "Subtract line 10 from line 9. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ssb.line9, take: ssb.line10}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 11"

  - id: ssb.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line9, ssb.line10]}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 12"

  - id: ssb.line13
    printed: "13"
    label: "Enter one-half of line 12"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line12, rate: {param: ssb.half}}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 13"

  - id: ssb.line14
    printed: "14"
    label: "Enter the smaller of line 2 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line2, ssb.line13]}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 14"

  - id: ssb.line15
    printed: "15"
    label: "Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line11, rate: {param: ssb.rate85}}
    shown_when: ssb.h_reach9
    cite: "i1040gi 2025 p. 32, line 15"

  - id: ssb.h_line16_sum
    printed: "(helper)"
    label: "Add lines 14 and 15"
    type: NonNegDollars
    expr: {op: sum, of: [ssb.line14, ssb.line15]}
    cite: "i1040gi 2025 p. 32, line 16"

  - id: ssb.h_line16_mfs
    printed: "(helper)"
    label: "Multiply line 7 by 85% (0.85) (married filing separately, lived with spouse)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line7, rate: {param: ssb.rate85}}
    cite: "i1040gi 2025 p. 32, line 8, third bullet"

  - id: ssb.h_show16
    printed: "(helper)"
    label: "Line 16 is reached (no STOP at line 7 or line 9)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ssb.h_reach9, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [ssb.h_reach7, {const: true}]}
            - {op: test, eq: [ssb.h_mfs_together, {const: true}]}
    cite: "i1040gi 2025 p. 32, lines 7 to 9"

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
    shown_when: ssb.h_show16
    cite: "i1040gi 2025 p. 32, lines 8 and 16"

  - id: ssb.line17
    printed: "17"
    label: "Multiply line 1 by 85% (0.85)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ssb.line1, rate: {param: ssb.rate85}}
    shown_when: ssb.h_show16
    cite: "i1040gi 2025 p. 32, line 17"

  - id: ssb.h_line18_figured
    printed: "(helper)"
    label: "The smaller of line 16 or line 17"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ssb.line16, ssb.line17]}
    cite: "i1040gi 2025 p. 32, line 18"

  - id: ssb.h_zero
    printed: "(helper)"
    label: "Zero (STOP: none of your social security benefits are taxable)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    cite: "i1040gi 2025 p. 32, lines 7 and 9 (STOP)"

  - id: ssb.line18
    printed: "18"
    label: "Taxable social security benefits. Enter the smaller of line 16 or line 17. Also enter this amount on Form 1040 or 1040-SR, line 6b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ssb.h_show16, {const: true}]}
          then: ssb.h_line18_figured
        - guard: {op: test, eq: [ssb.h_show16, {const: false}]}
          then: ssb.h_zero
    refuses: [ssb.lump_sum]
    shown_when: ssb.h_show16
    cite: "i1040gi 2025 p. 32, line 18 and TIP; p. 31 line 6c"
    note: "A STOP at line 7 or 9 carries zero to this result, which is entered on line 6b. The lump-sum election (Pub. 915) can reduce the taxable amount and is not figured here, so it refuses."

  - id: ssb.has_benefits
    printed: "(helper)"
    label: "Are there social security or railroad retirement benefits to report (line 1 more than zero)?"
    type: Bool
    expr: {op: test, gt: [ssb.line1, {const: 0}]}
    cite: "i1040gi 2025 p. 31, lines 6a and 6b; p. 32, line 1"
    note: "The IRS pages do not define this interface. Read as: the worksheet's line 1 (Form 1040 line 6a) is more than zero."
```
```
