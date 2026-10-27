# Transcription agreement — sdtw

Second transcription of `Schedule D Tax Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/sdtw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 78b9ac7527b71b2c3a5e21f7e2e97ecf726c31b5c019e67c7918e9be5c4d96a3 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f36787d2b0bf99cc79ba782e26a4ab91c88fb92c4c1500f0af715519c3777fb0 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cb0e91b7d153d0a32b27a4d832d94568504fe02e5a5484bc8f24319203eb5fed |
| printed lines compared | 47 |
| agree / disagree / missing | 26 / 21 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Taxable income
Status: **AGREE**

### 2 — Qualified dividends
Status: **AGREE**

### 3 — Form 4952 line 4g election
Status: **AGREE**

### 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form 4952 is fi
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"ref": "f4952.line4c"}, {"ref": "f4952.line1"}], "test": "le"}, {"args": [{"const": 0}, {"ref": "f4952.line5"}], "test": "lt"}, {"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f4952.line1"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}], "test": "any"}, "then": {"ref": "f4952.line4e"}}], "op": "choose"}
```

Second:

```json
{"ref": "f4952.line4e"}
```

Second transcription's note: The footnote's dotted-line smaller amount is not modeled; the expression copies Form 4952 line 4e.

Ruling: model error; i1040sd p. 15, line 4: "Enter the amount from Form 4952, line 4e*"; the worksheet is for a filer who has Schedule D gains "or if you file Form 4952 and you have an amount on line 4g" The candidate copies f4952.line4e on every return (its note: the dotted-line amount is not modeled); the project enters it only when sd.filing4952 (BUG-0160). f4952.line4e is figured whether or not Form 4952 is filed, so the candidate shows an amount from a form that is not filed. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,361 of 1,599 agree; 139 value (34 on completed returns), 99 project-refuses. Witnesses: classm.f5695.5 (completed; f4952.required false) project $0.00, candidate $13,526.00; classm.f4952.2 (f4952.line1 $0) $0.00 against $37,231.00. No amount changes (line 3 is 0 there, so lines 5 and 8 are 0). The project-refuses are scope: f4952.required refuses on the cited f4952.carryover gate (classm.w2.1.deepseek), all on returns the project refuses.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

### 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

### 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

### 8 — Smaller of lines 3 and 4
Status: **AGREE**

### 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

### 10 — Add lines 6 and 9
Status: **AGREE**

### 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

### 12 — Smaller of lines 9 and 11
Status: **AGREE**

### 13 — Subtract line 12 from line 10
Status: **AGREE**

### 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

### 15 — Zero-rate ceiling by filing status
Status: **AGREE**

### 16 — Smaller of lines 1 and 15
Status: **AGREE**

### 17 — Smaller of lines 14 and 16
Status: **AGREE**

### 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

### 20 — Smaller of lines 14 and 19
Status: **AGREE**

### 21 — Larger of lines 18 and 20
Status: **AGREE**

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

### 23 — Smaller of lines 1 and 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "1"}, {"line": "13"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "1"}, {"line": "13"}], "op": "smaller_of"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 23 with no skip, a nonzero amount on a skipped line (README skipped-line rule); the project enters 0. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,560 of 1,599 agree; 39 value (13 on completed returns). Witness: classm.dependent.5 (completed; lines 1 and 16 equal) project $0.00, candidate $52,797.20. classm.sdtw.2 $0.00 against $10,429.58.

### 24 — Amount from line 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"line": "22"}}], "op": "choose"}
```

Second:

```json
{"line": "22"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 24 with no skip, a nonzero amount on a skipped line (README skipped-line rule); the project enters 0. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,560 of 1,599 agree; 39 value (13 on completed returns). Witness: classm.dependent.5 project $0.00, candidate $52,797.20 (line 22 copied). classm.sdtw.2 $0.00 against $10,429.58.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"from": {"line": "23"}, "op": "subtract_floor0", "take": {"line": "24"}}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "23"}, "op": "subtract_floor0", "take": {"line": "24"}}
```

Ruling: representation; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." On a skip return line 25 is 0 by derivation (line 23 less line 22 floored). Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 26 — 15-percent ceiling by filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"param": "qdcg.fifteen_rate_ceiling"}}], "op": "choose"}
```

Second:

```json
{"param": "qdcg.fifteen_rate_ceiling"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate enters the 15-percent ceiling with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 364 of 1,599 agree; 516 value (355 on completed returns), 572 project-refuses, 147 project-unknown. Witness: classm.f2441.2.deepseek (completed) project $0.00, candidate $600,050.00. The project-refuses (scope) and project-unknown (representation) come from line 1, which the project's skip test reads: refused by cited upstream gates on refused returns, or unknown on records that withhold an answer the interview asks.

### 27 — Smaller of lines 1 and 26
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "1"}, {"line": "26"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "1"}, {"line": "26"}], "op": "smaller_of"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures the smaller of lines 1 and 26 with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,267 of 1,599 agree; 332 value (257 on completed returns). Witness: classm.f2441.1.deepseek (completed) project $0.00, candidate $26,375.00.

### 28 — Add lines 21 and 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "21"}, {"line": "22"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "21"}, {"line": "22"}], "op": "sum"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate adds lines 21 and 22 with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,267 of 1,599 agree; 332 value (257 on completed returns). Witness: classm.f2441.1.deepseek (completed) project $0.00, candidate $26,375.00.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"from": {"line": "27"}, "op": "subtract_floor0", "take": {"line": "28"}}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "27"}, "op": "subtract_floor0", "take": {"line": "28"}}
```

Ruling: representation; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." On a skip return line 28 (lines 21 + 22) is at least line 27, so line 29 is 0 by derivation. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 30 — Smaller of lines 25 and 29
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "25"}, {"line": "29"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "25"}, {"line": "29"}], "op": "smaller_of"}
```

Ruling: representation; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." Line 30 is the smaller of lines 25 and 29, both 0 on skip returns. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 31 — Multiply line 30 by 15 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: Returns zero when lines 1 and 16 are the same, because lines 23 through 43 are skipped.

Ruling: representation; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate applies the line 22 skip itself (choose on lines 1 and 16) and floors at zero, a no-op. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 32 — Add lines 24 and 30
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "24"}, {"line": "30"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "24"}, {"line": "30"}], "op": "sum"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 32 with no skip, a nonzero amount on a skipped line (README skipped-line rule); the project enters 0. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,560 of 1,599 agree; 39 value (13 on completed returns). Witness: classm.dependent.5 project $0.00, candidate $52,797.20. classm.sdtw.2 $0.00 against $10,429.58.

### 33 — Subtract line 32 from line 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "23"}, "op": "subtract", "take": {"line": "32"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "23"}, "op": "subtract", "take": {"line": "32"}}
```

Ruling: representation; i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." Line 33 = line 23 - line 32; line 32 = line 24 + min(line 25, line 29) is at most line 23, which is at most line 1, so when lines 1 and 32 are equal (the line 32 skip) line 33 is 0, and on line 22 skip returns lines 23 and 32 are equal by derivation. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 34 — Multiply line 33 by 20 percent
Status: **AGREE**

### 35 — Smaller of line 9 and Schedule D line 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "9"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "9"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate enters the smaller of line 9 and Schedule D line 19 with no skip. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,129 of 1,599 agree; 9 value (4 on completed returns), 459 project-refuses, 2 project-unknown. Witness: classm.s8812.2 (completed; lines 1 and 32 equal) project $0.00, candidate $1,585.00. The project-refuses are scope (the project's skip test reads line 1, refused by cited upstream gates on refused returns; the candidate does not read it); the 2 project-unknown (classm.g28.2, classm.u1250.2) withhold an answer the interview asks (representation).

### 36 — Add lines 10 and 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "10"}, {"line": "21"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "10"}, {"line": "21"}], "op": "sum"}
```

Ruling: model error; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate adds lines 10 and 21 with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 781 of 1,599 agree; 709 value (433 on completed returns), 109 candidate-unknown. Witness: classm.f2441.1.deepseek (completed; Schedule D line 19 zero) project $0.00, candidate $26,375.00. The 109 candidate-unknown are records withholding an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone (representation).

### 37 — Amount from line 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"line": "1"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "1"}
```

Ruling: model error; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate copies line 1 with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 816 of 1,599 agree; 674 value (417 on completed returns), 109 candidate-unknown. Witness: classm.f2441.1.deepseek project $0.00, candidate $26,375.00. The 109 candidate-unknown are records withholding an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone (representation).

### 38 — Subtract line 37 from line 36; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "36"}, "op": "subtract_floor0", "take": {"line": "37"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "36"}, "op": "subtract_floor0", "take": {"line": "37"}}
```

Ruling: model error; i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate subtracts line 37 from line 36 with no skip, a nonzero amount on a skipped line. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,418 of 1,599 agree; 72 value (37 on completed returns), 109 candidate-unknown. Witness: classm.f5695.7 (completed; lines 1 and 32 equal) project $0.00, candidate $31,500.00. The 109 candidate-unknown are records withholding an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone (representation).

### 39 — Subtract line 38 from line 35; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "38"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "38"}}
```

Ruling: representation; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate's line 39 (line 35 less line 38, floored) has no skip, but line 35 is 0 whenever Schedule D line 19 is zero and the floored difference is then 0, so no value differs; its line 35 error is ruled on line 35. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,490 of 1,599 agree; no value difference; 109 candidate-unknown. The unknowns are records withholding an answer the interview asks of every filer (f1040.line13a and 13b unknown, taxable income unknown; classm.f4952.1), where the project settles the skip from Schedule D line 19 alone; on every record with taxable income known the values agree.

### 40 — Multiply line 39 by 25 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}}, {"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: Returns zero when lines 1 and 16 are the same, lines 1 and 32 are the same, or Schedule D line 19 is zero.

Ruling: representation; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate gates line 40 on Schedule D line 19 and the skips after lines 22 and 32, as the project does. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,599 of 1,599 agree. Observed equivalence on the sample, consistent with the derivation.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"of": [{"line": "21"}, {"line": "22"}, {"line": "30"}, {"line": "33"}, {"line": "39"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "21"}, {"line": "22"}, {"line": "30"}, {"line": "33"}, {"line": "39"}], "op": "sum"}
```

Ruling: model error; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate adds lines 21, 22, 30, 33 and 39 on every return, so it shows amounts where the source skips lines 41 to 43; the project hides line 41 when Schedule D line 18 is zero (sdtw.show41_43) and enters 0 after the line 22 and 32 skips. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 379 of 1,599 agree; 668 candidate-shows-skipped (414 on completed returns), 7 value, 435 candidate-refuses, 110 candidate-unknown. Witnesses: classm.f8889.2.deepseek (line 18 zero, lines 35-40 skipped) hidden, candidate $324,872.80; stage4.sdtw.skip22 (line 18 positive, a skip return: sdtw.after32 false) project $0.00, candidate $40,000.00. The candidate-refuses are scope (line 21 reads line 1, refused by cited gates such as f2441.line14_bad on classm.w2.1.deepseek, on returns the project refuses); the unknowns are records withholding an answer the interview asks (representation).

### 42 — Subtract line 41 from line 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}
```

Ruling: scope; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." The candidate subtracts line 41 from line 1 with no skip; triage finds no shown amount that differs (no candidate-shows-skipped): on every sampled return where the project hides line 42 (Schedule D line 18 zero), the candidate's line 1 less line 41 is 0, consistent with line 42 being the 28-percent remainder; observed on the sample, not proved. Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,054 of 1,599 agree; no value and no candidate-shows-skipped; 435 candidate-refuses, 110 candidate-unknown. The candidate refusals read line 1, refused by cited project gates (f2441.line14_bad on classm.w2.1.deepseek; f8959.2) on returns the project refuses; the unknowns are records withholding an answer the interview asks of every filer (classm.f4952.1; representation). Project stands.

### 43 — Multiply line 42 by 28 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}}, {"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Returns zero when the worksheet skips lines 41 through 43.

Ruling: scope; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." The candidate gates line 43 on Schedule D line 18 (g28.line7) and the skips after lines 22 and 32, as the project does (BUG-0150). Triage executable-triage-v2 (triage/sdtw.deepseek.json; 1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons): 1,164 of 1,599 agree; no value difference; 435 candidate-refuses. The candidate refusals read line 1 through line 42, refused by cited project gates (f2441.line14_bad on classm.w2.1.deepseek) on returns the project refuses. Project stands.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **AGREE**

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **AGREE**

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

## Raw second transcription

```yaml
lines:
  - id: sdtw.line1
    printed: "1"
    label: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555, enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    note: "The Form 2555 branch is not modeled; the expression uses Form 1040 line 15."
  - id: sdtw.line2
    printed: "2"
    label: "Enter your qualified dividends from Form 1040, 1040-SR, or 1040-NR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}
  - id: sdtw.line3
    printed: "3"
    label: "Enter the amount from Form 4952 (used to figure investment interest expense deduction), line 4g"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
  - id: sdtw.line4
    printed: "4"
    label: "Enter the amount from Form 4952, line 4e*"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4e}
    note: "The footnote's dotted-line smaller amount is not modeled; the expression copies Form 4952 line 4e."
  - id: sdtw.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line3, take: sdtw.line4}
  - id: sdtw.line6
    printed: "6"
    label: "Subtract line 5 from line 2. If zero or less, enter -0-**"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line2, take: sdtw.line5}
  - id: sdtw.line7
    printed: "7"
    label: "Enter the smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
  - id: sdtw.line8
    printed: "8"
    label: "Enter the smaller of line 3 or line 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line3, sdtw.line4]}
  - id: sdtw.line9
    printed: "9"
    label: "Subtract line 8 from line 7. If zero or less, enter -0-**"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line7, take: sdtw.line8}
  - id: sdtw.line10
    printed: "10"
    label: "Add lines 6 and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sdtw.line6, sdtw.line9]}
  - id: sdtw.line11
    printed: "11"
    label: "Add lines 18 and 19 of Schedule D**"
    type: NonNegDollars
    expr: {op: sum, of: [sd.line18, sd.line19]}
  - id: sdtw.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line9, sdtw.line11]}
  - id: sdtw.line13
    printed: "13"
    label: "Subtract line 12 from line 10"
    type: Dollars
    expr: {op: subtract, from: sdtw.line10, take: sdtw.line12}
  - id: sdtw.line14
    printed: "14"
    label: "Subtract line 13 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line1, take: sdtw.line13}
  - id: sdtw.line15
    printed: "15"
    label: "Enter: $48,350 if single or married filing separately; $96,700 if married filing jointly or qualifying surviving spouse; or $64,750 if head of household."
    type: NonNegDollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}
  - id: sdtw.line16
    printed: "16"
    label: "Enter the smaller of line 1 or line 15"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line15]}
  - id: sdtw.line17
    printed: "17"
    label: "Enter the smaller of line 14 or line 16"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line14, sdtw.line16]}
  - id: sdtw.line18
    printed: "18"
    label: "Subtract line 10 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line1, take: sdtw.line10}
  - id: sdtw.line19
    printed: "19"
    label: "Enter the smaller of line 1 or: $197,300 if single or married filing separately; $394,600 if married filing jointly or qualifying surviving spouse; or $197,300 if head of household."
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.h_ordinary_ceiling]}
  - id: sdtw.line20
    printed: "20"
    label: "Enter the smaller of line 14 or line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line14, sdtw.line19]}
  - id: sdtw.line21
    printed: "21"
    label: "Enter the larger of line 18 or line 20"
    type: NonNegDollars
    expr: {op: larger_of, of: [sdtw.line18, sdtw.line20]}
  - id: sdtw.line22
    printed: "22"
    label: "Subtract line 17 from line 16. This amount is taxed at 0%. If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23."
    type: Dollars
    expr: {op: subtract, from: sdtw.line16, take: sdtw.line17}
  - id: sdtw.line23
    printed: "23"
    label: "Enter the smaller of line 1 or line 13"
    type: Dollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line13]}
  - id: sdtw.line24
    printed: "24"
    label: "Enter the amount from line 22. (If line 22 is blank, enter -0-.)"
    type: Dollars
    expr: {op: copy, from: sdtw.line22}
  - id: sdtw.line25
    printed: "25"
    label: "Subtract line 24 from line 23. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line23, take: sdtw.line24}
  - id: sdtw.line26
    printed: "26"
    label: "Enter: $533,400 if single; $300,000 if married filing separately; $600,050 if married filing jointly or qualifying surviving spouse; or $566,700 if head of household."
    type: NonNegDollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}
  - id: sdtw.line27
    printed: "27"
    label: "Enter the smaller of line 1 or line 26"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line26]}
  - id: sdtw.line28
    printed: "28"
    label: "Add lines 21 and 22"
    type: Dollars
    expr: {op: sum, of: [sdtw.line21, sdtw.line22]}
  - id: sdtw.line29
    printed: "29"
    label: "Subtract line 28 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line27, take: sdtw.line28}
  - id: sdtw.line30
    printed: "30"
    label: "Enter the smaller of line 25 or line 29"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line25, sdtw.line29]}
  - id: sdtw.line31
    printed: "31"
    label: "Multiply line 30 by 15% (0.15)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_line31_choice, take: {const: 0}}
    note: "Returns zero when lines 1 and 16 are the same, because lines 23 through 43 are skipped."
  - id: sdtw.line32
    printed: "32"
    label: "Add lines 24 and 30. If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33."
    type: Dollars
    expr: {op: sum, of: [sdtw.line24, sdtw.line30]}
  - id: sdtw.line33
    printed: "33"
    label: "Subtract line 32 from line 23"
    type: Dollars
    expr: {op: subtract, from: sdtw.line23, take: sdtw.line32}
  - id: sdtw.line34
    printed: "34"
    label: "Multiply line 33 by 20% (0.20). If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [sdtw.line1, sdtw.line16]}, {op: test, eq: [sdtw.line1, sdtw.line32]}]}
          then: sdtw.h_zero
        - guard: {op: test, all: [{op: test, ne: [sdtw.line1, sdtw.line16]}, {op: test, ne: [sdtw.line1, sdtw.line32]}]}
          then: sdtw.h_line34_amount
    note: "Returns zero when the worksheet skips lines 33 through 43."
  - id: sdtw.line35
    printed: "35"
    label: "Enter the smaller of line 9 above or Schedule D, line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line9, sd.line19]}
  - id: sdtw.line36
    printed: "36"
    label: "Add lines 10 and 21"
    type: NonNegDollars
    expr: {op: sum, of: [sdtw.line10, sdtw.line21]}
  - id: sdtw.line37
    printed: "37"
    label: "Enter the amount from line 1 above"
    type: NonNegDollars
    expr: {op: copy, from: sdtw.line1}
  - id: sdtw.line38
    printed: "38"
    label: "Subtract line 37 from line 36. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line36, take: sdtw.line37}
  - id: sdtw.line39
    printed: "39"
    label: "Subtract line 38 from line 35. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line35, take: sdtw.line38}
  - id: sdtw.line40
    printed: "40"
    label: "Multiply line 39 by 25% (0.25). If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_line40_choice, take: {const: 0}}
    note: "Returns zero when lines 1 and 16 are the same, lines 1 and 32 are the same, or Schedule D line 19 is zero."
  - id: sdtw.line41
    printed: "41"
    label: "Add lines 21, 22, 30, 33, and 39"
    type: Dollars
    expr: {op: sum, of: [sdtw.line21, sdtw.line22, sdtw.line30, sdtw.line33, sdtw.line39]}
  - id: sdtw.line42
    printed: "42"
    label: "Subtract line 41 from line 1"
    type: Dollars
    expr: {op: subtract, from: sdtw.line1, take: sdtw.line41}
  - id: sdtw.line43
    printed: "43"
    label: "Multiply line 42 by 28% (0.28)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [sdtw.line1, sdtw.line16]}, {op: test, eq: [sdtw.line1, sdtw.line32]}, {op: test, eq: [sd.line18, {const: 0}]}]}
          then: sdtw.h_zero
        - guard: {op: test, all: [{op: test, ne: [sdtw.line1, sdtw.line16]}, {op: test, ne: [sdtw.line1, sdtw.line32]}, {op: test, ne: [sd.line18, {const: 0}]}]}
          then: sdtw.h_line43_amount
    note: "Returns zero when the worksheet skips lines 41 through 43."
  - id: sdtw.line44
    printed: "44"
    label: "Figure the tax on the amount on line 21. If the amount on line 21 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 21 is $100,000 or more, use the Tax Computation Worksheet."
    type: Dollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line21, status: f1040.status}, line: tax}}
  - id: sdtw.line45
    printed: "45"
    label: "Add lines 31, 34, 40, 43, and 44"
    type: Dollars
    expr: {op: sum, of: [sdtw.line31, sdtw.line34, sdtw.line40, sdtw.line43, sdtw.line44]}
  - id: sdtw.line46
    printed: "46"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet."
    type: Dollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line1, status: f1040.status}, line: tax}}
  - id: sdtw.line47
    printed: "47"
    label: "Tax on all taxable income (including capital gains and qualified dividends). Enter the smaller of line 45 or line 46. Also, include this amount on Form 1040, 1040-SR, or 1040-NR, line 16. (If you are filing Form 2555, don't enter this amount on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet in the Instructions for Form 1040.)"
    type: Dollars
    expr: {op: smaller_of, of: [sdtw.line45, sdtw.line46]}
  - id: sdtw.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sdtw.h_ordinary_ceiling
    printed: "(helper)"
    label: "Worksheet threshold for line 19"
    type: NonNegDollars
    expr: {op: param, ref: sdtw.ordinary_ceiling}
  - id: sdtw.h_line31_amount
    printed: "(helper)"
    label: "Line 30 multiplied by 15%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line30, rate: {param: sdtw.rate15}}
  - id: sdtw.h_line31_choice
    printed: "(helper)"
    label: "Line 31 amount, or zero when lines 23 through 43 are skipped"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.line1, sdtw.line16]}
          then: sdtw.h_zero
        - guard: {op: test, ne: [sdtw.line1, sdtw.line16]}
          then: sdtw.h_line31_amount
  - id: sdtw.h_line34_amount
    printed: "(helper)"
    label: "Line 33 multiplied by 20%"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line33, rate: {param: sdtw.rate20}}
  - id: sdtw.h_line40_amount
    printed: "(helper)"
    label: "Line 39 multiplied by 25%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line39, rate: {param: sdtw.rate25}}
  - id: sdtw.h_line40_choice
    printed: "(helper)"
    label: "Line 40 amount, or zero when the worksheet skips lines 35 through 40"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [sdtw.line1, sdtw.line16]}, {op: test, eq: [sdtw.line1, sdtw.line32]}, {op: test, eq: [sd.line19, {const: 0}]}]}
          then: sdtw.h_zero
        - guard: {op: test, all: [{op: test, ne: [sdtw.line1, sdtw.line16]}, {op: test, ne: [sdtw.line1, sdtw.line32]}, {op: test, ne: [sd.line19, {const: 0}]}]}
          then: sdtw.h_line40_amount
  - id: sdtw.h_line43_amount
    printed: "(helper)"
    label: "Line 42 multiplied by 28%"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line42, rate: {param: sdtw.rate28}}
```
