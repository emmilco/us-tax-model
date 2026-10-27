# Transcription agreement — sdtw

Second transcription of `Schedule D Tax Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/sdtw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 78b9ac7527b71b2c3a5e21f7e2e97ecf726c31b5c019e67c7918e9be5c4d96a3 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | da6a2a4f05e277b8dba47912a2eb0a55b4513e284b6c103d5051ab014b02898f |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cb0e91b7d153d0a32b27a4d832d94568504fe02e5a5484bc8f24319203eb5fed |
| printed lines compared | 47 |
| agree / disagree / missing | 22 / 25 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- model changed a published result type
- model changed a published result type

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

Second transcription's note: Footnote * says to enter instead the smaller amount written on the dotted line next to Form 4952 line 4e, if applicable. No input carries that dotted-line amount. The alternative-allocation case is refused through f4952.alternative_allocation.

Ruling: model error; i1040sd p. 15, line 4: "Enter the amount from Form 4952, line 4e*"; the worksheet is for a filer who has Schedule D gains "or if you file Form 4952 and you have an amount on line 4g". The candidate copies f4952.line4e on every return; the project (BUG-0160) enters it only when sd.filing4952 and 0 otherwise. f4952.line4e is figured whether or not Form 4952 is filed, so the candidate enters an amount from a form that is not filed. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. Line 4: 1,379 of 1,599 agree; 139 value (34 on completed returns), 81 project-refuses. Witnesses: classm.f5695.5 (completed; f4952.exception true, f4952.required false) project $0.00, candidate $13,526.00; classm.f4952.2 (f4952.line1 $0, no investment interest) $0.00 against $37,231.00. No amount changes: line 3 is 0 on those returns, so lines 5 and 8 are 0 either way; the error is a shown amount on a line with no source. The 81 project-refuses are scope: f4952.required refuses on the cited f4952.carryover gate ("Prior-year investment-interest carryovers are outside scope", f4952 pp. 1, 3-4; classm.w2.1.deepseek), all on returns the project refuses.

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
Status: **DISAGREE**

Project:

```json
{"param": "qdcg.zero_rate_ceiling"}
```

Second:

```json
{"from": {"param": "qdcg.zero_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. A zero floor, which never changes these positive amounts, establishes the NonNegDollars type.

Ruling: representation; i1040sd p. 15, line 15: "Enter: $48,350 if single or married filing separately; $96,700 if married filing jointly or qualifying surviving spouse; or $64,750 if head of household." The candidate floors the positive parameter qdcg.zero_rate_ceiling at zero (its note: to establish NonNegDollars), which never binds. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,599 of 1,599 agree.

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

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 23 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,558 of 1,599 agree; 39 value (13 on completed returns), 2 project-refuses. Witness: classm.dependent.5 (completed; lines 1 and 16 equal) project $0.00, candidate $52,797.20; classm.sdtw.2 $0.00 against $10,429.58. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Second transcription's note: Line 22 is always computed in this model, so it is never blank.

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 24 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,558 of 1,599 agree; 39 value (13 on completed returns), 2 project-refuses. Witness: classm.dependent.5 project $0.00, candidate $52,797.20 (line 22 copied onto a skipped line); classm.sdtw.2 $0.00 against $10,429.58. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Ruling: scope; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." On a skip return the candidate's line 25 = line 23 - line 24 floored = min(line 1, line 13) - line 22 is 0 by derivation: when lines 1 and 16 are equal, line 22 equals min(line 1, line 13), so the only differences are refusals. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

### 26 — 15-percent ceiling by filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"param": "qdcg.fifteen_rate_ceiling"}}], "op": "choose"}
```

Second:

```json
{"from": {"param": "qdcg.fifteen_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. A zero floor, which never changes these positive amounts, establishes the NonNegDollars type.

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate enters the 15-percent ceiling (qdcg.fifteen_rate_ceiling floored at zero) with no skip, a nonzero amount on a skipped line. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 364 of 1,599 agree; 516 value (355 on completed returns), 572 project-refuses, 147 project-unknown. Witness: classm.f2441.2.deepseek (completed, lines 1 and 16 both $53,500) project $0.00, candidate $600,050.00. The project-refuses (scope) and project-unknown (representation) come from line 1, which the project's skip test reads (taxable income refused by a cited upstream gate, or unknown on records that withhold an answer the interview asks, such as classm.f8889.3.deepseek); the candidate's constant does not read it.

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

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 27 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,265 of 1,599 agree; 332 value (257 on completed returns), 2 project-refuses. Witness: classm.f2441.1.deepseek (completed) project $0.00, candidate $26,375.00 (= line 1). The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 28 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,265 of 1,599 agree; 332 value (257 on completed returns), 2 project-refuses. Witness: classm.f2441.1.deepseek (completed) project $0.00, candidate $26,375.00 (lines 21 + 22). The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Ruling: scope; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." On a skip return line 29 = line 27 - line 28 floored, and line 28 (lines 21 + 22) is at least line 27 (smaller of line 1 and line 26) when lines 1 and 16 are equal, so it is 0 by derivation. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

### 30 — Smaller of lines 25 and 29
Status: **AGREE**

### 31 — Multiply line 30 by 15 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}
```

Ruling: scope; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." Line 31 is 15 percent of line 30 = min(line 25, line 29), both 0 on skip returns, so 0 by derivation. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

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

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate figures line 32 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,558 of 1,599 agree; 39 value (13 on completed returns), 2 project-refuses. Witness: classm.dependent.5 project $0.00, candidate $52,797.20; classm.sdtw.2 $0.00 against $10,429.58. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

### 33 — Subtract line 32 from line 23
Status: **AGREE**

### 34 — Multiply line 33 by 20 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate20"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate20"}}
```

Ruling: scope; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." Line 34 is 20 percent of line 33, which is not open (the candidate's line 33 agrees with the project's 0 on every skip return), so 0 by derivation. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

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

Ruling: model error; i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate enters the smaller of line 9 and Schedule D line 19 whenever line 19 is positive, ignoring the earlier skips after lines 22 and 32. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,147 of 1,599 agree; 9 value (4 on completed returns), 441 project-refuses, 2 project-unknown. Witness: classm.s8812.2 (completed; lines 1 and 32 equal, Schedule D line 19 $1,585) project $0.00, candidate $1,585.00. The 441 project-refuses are scope: the project's skip test reads line 1, which is refused by cited upstream gates on returns the project refuses (classm.w2.1.deepseek, f2441.line14_bad), while the candidate's line 9 does not read line 1. The 2 project-unknown (classm.g28.2, classm.u1250.2) are records that withhold an answer the interview asks, so taxable income is unknown (representation).

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

Ruling: model error; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate figures line 36 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 779 of 1,599 agree; 709 value (433 on completed returns), 109 candidate-unknown, 2 project-refuses. Witness: classm.f2441.1.deepseek (completed; Schedule D line 19 zero and lines 1 and 16 equal) project $0.00, candidate $26,375.00. The 109 candidate-unknown are records that withhold an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone and the candidate needs taxable income (representation). The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Ruling: model error; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate figures line 37 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 814 of 1,599 agree; 674 value (417 on completed returns), 109 candidate-unknown, 2 project-refuses. Witness: classm.f2441.1.deepseek project $0.00, candidate $26,375.00 (line 1 copied). The 109 candidate-unknown are records that withhold an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone and the candidate needs taxable income (representation). The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

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

Ruling: model error; i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate figures line 38 with no skip, so it shows a nonzero amount on a skipped line, which the README skipped-line rule makes a defect of the side that produces it; the project enters 0 there. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,416 of 1,599 agree; 72 value (37 on completed returns), 109 candidate-unknown, 2 project-refuses. Witness: classm.f5695.7 (completed; lines 1 and 32 equal at $213,385) project $0.00, candidate $31,500.00. The 109 candidate-unknown are records that withhold an answer the interview asks of every filer (f1040.line13a and 13b unknown, for example classm.f4952.1), where the project settles the skip from Schedule D line 19 alone and the candidate needs taxable income (representation). The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

### 39 — Subtract line 38 from line 35; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "38"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "38"}}}, {"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Skipped lines are treated as blank, that is zero, both on line 40 and where line 41 adds line 39.

Ruling: scope; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." The candidate gates line 39 on Schedule D line 19 (u1250.line18 through sd.line17) and the line 22 and line 32 skips, giving 0 when the worksheet skips it, as the project does. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

### 40 — Multiply line 39 by 25 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}
```

Ruling: scope; i1040sd p. 16, after line 34: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41. Otherwise, go to line 35." Line 40 is 25 percent of line 39, which is 0 on every skip return in both readings. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,597 of 1,599 agree; no value difference. The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses, where the candidate cannot evaluate line 1. Project stands.

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

Ruling: model error; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." The candidate adds lines 21, 22, 30, 33 and 39 on every return (its line 42 note: "Line 41 is not gated separately"), so it shows amounts where the source skips lines 41 to 43; the project hides line 41 when Schedule D line 18 is zero (sdtw.show41_43, BUG-0150) and enters 0 after the line 22 and line 32 skips. Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 377 of 1,599 agree; 668 candidate-shows-skipped (414 on completed returns), 7 value, 435 candidate-refuses, 110 candidate-unknown, 2 project-refuses. Witnesses: classm.f2441.1.deepseek (completed, line 18 zero) hidden, candidate $26,375.00; stage4.sdtw.skip22 (line 18 positive, a skip return: sdtw.after32 false) project $0.00, candidate $40,000.00. The 435 candidate-refuses are scope: the sum reads line 21, hence line 1, which is refused by cited gates (for example f2441.line14_bad on classm.w2.1.deepseek) on returns the project refuses, where the project's line is hidden or 0 without reading line 1. The 110 candidate-unknown are records withholding an answer the interview asks (representation); The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses (scope).

### 42 — Subtract line 41 from line 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}}, {"guard": {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Skipped lines are treated as blank, that is zero. Line 41 is not gated separately because line 42 is the only line that reads it.

Ruling: scope; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." The candidate gates line 42 on Schedule D line 18 (g28.line7 through sd.line17) and the line 22 and line 32 skips, as the project does (BUG-0150 fix: sdtw.show41_43 and sdtw.use28). Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,162 of 1,599 agree; no value difference; 435 candidate-refuses, 2 project-refuses. The candidate refusals come from its gate reading line 1, refused by cited project gates (f2441.line14_bad on classm.w2.1.deepseek, the same gate in its line 42 skip helper) on returns the project refuses; The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses. Project stands.

### 43 — Multiply line 42 by 28 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}}, {"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}
```

Ruling: scope; i1040sd p. 16, after line 40: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44. Otherwise, go to line 41." i1040sd p. 15, after line 22: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44. Otherwise, go to line 23." i1040sd p. 16, after line 32: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44. Otherwise, go to line 33." The candidate's line 43 is 28 percent of its line 42, which is gated on Schedule D line 18 (g28.line7 through sd.line17) and the line 22 and line 32 skips, so it is 0 wherever the source skips it, as the project's line is (BUG-0150 fix: sdtw.show41_43 and sdtw.use28). Triage: triage/sdtw.json is state "invalid" (sdtw.line44 and sdtw.line46 declared NonNegDollars where the published type is Dollars), so nothing was recorded. Evidence here is a read-only scratch rerun of tools/transcription/triage.mjs on the same bank (1,099 fixtures, 500 generated returns seed 20261026, no partial records; 1,599 comparisons) with those two declarations evaluated as the published Dollars and lines 44 to 47 excluded; it is not a triage record, the raw reply is unchanged, and the reading below decides the line. The candidate expressions for lines 15, 23 to 38, 40, 41 and 43 are identical to the round 2 Claude reply, whose executed counts match. 1,162 of 1,599 agree; no value difference; 435 candidate-refuses, 2 project-refuses. The candidate refusals come from its gate reading line 1, refused by cited project gates (f2441.line14_bad on classm.w2.1.deepseek, the same gate in its line 42 skip helper) on returns the project refuses; The 2 project-refuses (stage16.cleanup.refuse.f8889.screen_no_amounts, stage16.cleanup.refuse.retirement.special_first) are cited project gates on line 1 (person[taxpayer].f8889[hsa].unsupported, retirement[p].special) on returns the project refuses. Project stands.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"line": "21"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"line": "21"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "tax_table"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "21"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "21"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"line": "21"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"line": "21"}], "test": "lt"}, "then": {"from": {"amount": {"line": "21"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"line": "21"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"line": "21"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "tax_table"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sdtw.line44", "message": "model changed a published result type"}]}
```

Second transcription's note: The shared tax_on_amount result is declared Dollars. A zero floor establishes the declared NonNegDollars type, since tax on a nonnegative amount is never negative.

Ruling: model error; on the validation failure: the host type check rejects sdtw.line44, declared NonNegDollars where the published type is Dollars ("model changed a published result type"). i1040sd p. 16, line 44: "Figure the tax on the amount on line 21. If the amount on line 21 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 21 is $100,000 or more, use the Tax Computation Worksheet". This ruling adjudicates the declaration, not the tax reading: triage cannot execute a reply with a validation error (triage/sdtw.json state "invalid"). By reading, the candidate figures the tax on the amount with the shared tax_on_amount definition and floors it at zero, which never binds because tax on a nonnegative amount is nonnegative.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "31"}, {"line": "34"}, {"line": "40"}, {"line": "43"}, {"line": "44"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "31"}, {"line": "34"}, {"line": "40"}, {"line": "43"}, {"line": "44"}], "op": "sum"}, "invalid_model_types": [{"line": "sdtw.line44", "message": "model changed a published result type"}]}
```

Ruling: model error; on the validation failure in its dependency closure: the candidate's line 45 expression (sum of lines 31, 34, 40, 43 and 44) is the project's, but it reads sdtw.line44, which fails the host type check (NonNegDollars declared where the published type is Dollars). i1040sd p. 16, line 45: "Add lines 31, 34, 40, 43, and 44". This ruling adjudicates the declaration, not the tax reading; triage cannot execute the reply (triage/sdtw.json state "invalid"). By reading, lines 31, 34 and 40 are 0 on skip returns (above), while the candidate's line 43 is gated as the project's.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"line": "1"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"line": "1"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "tax_table"}}], "op": "choose"}
```

Second:

```json
{"expression": {"from": {"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"line": "1"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"line": "1"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"line": "1"}], "test": "lt"}, "then": {"from": {"amount": {"line": "1"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"line": "1"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"line": "1"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "tax_table"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, "invalid_model_types": [{"line": "sdtw.line46", "message": "model changed a published result type"}]}
```

Second transcription's note: The shared tax_on_amount result is declared Dollars. A zero floor establishes the declared NonNegDollars type.

Ruling: model error; on the validation failure: the host type check rejects sdtw.line46, declared NonNegDollars where the published type is Dollars ("model changed a published result type"). i1040sd p. 16, line 46: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet". This ruling adjudicates the declaration, not the tax reading: triage cannot execute a reply with a validation error (triage/sdtw.json state "invalid"). By reading, the candidate figures the tax on the amount with the shared tax_on_amount definition and floors it at zero, which never binds because tax on a nonnegative amount is nonnegative.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "45"}, {"line": "46"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "45"}, {"line": "46"}], "op": "smaller_of"}, "invalid_model_types": [{"line": "sdtw.line44", "message": "model changed a published result type"}, {"line": "sdtw.line46", "message": "model changed a published result type"}]}
```

Ruling: model error; on the validation failure in its dependency closure: the candidate's line 47 expression (smaller of lines 45 and 46) is the project's, but it reads sdtw.line44 (through line 45) and sdtw.line46, both failing the host type check (NonNegDollars declared where the published type is Dollars). i1040sd p. 16, line 47: "Tax on all taxable income (including capital gains and qualified dividends). Enter the smaller of line 45 or line 46." This ruling adjudicates the declaration, not the tax reading; triage cannot execute the reply (triage/sdtw.json state "invalid").

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | sa.excluded_income | - |
| 4 | f4952.alternative_allocation | - |
| 5 | f4952.alternative_allocation | - |
| 6 | f4952.alternative_allocation | - |
| 8 | f4952.alternative_allocation | - |
| 9 | f4952.alternative_allocation | - |
| 10 | f4952.alternative_allocation | - |
| 12 | f4952.alternative_allocation | - |
| 13 | f4952.alternative_allocation | - |
| 14 | f4952.alternative_allocation, sa.excluded_income | - |
| 16 | sa.excluded_income | - |
| 17 | f4952.alternative_allocation, sa.excluded_income | - |
| 18 | f4952.alternative_allocation, sa.excluded_income | - |
| 19 | sa.excluded_income | - |
| 20 | f4952.alternative_allocation, sa.excluded_income | - |
| 21 | f4952.alternative_allocation, sa.excluded_income | - |
| 22 | f4952.alternative_allocation, sa.excluded_income | - |
| 23 | f4952.alternative_allocation, sa.excluded_income | - |
| 24 | f4952.alternative_allocation, sa.excluded_income | - |
| 25 | f4952.alternative_allocation, sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 28 | f4952.alternative_allocation, sa.excluded_income | - |
| 29 | f4952.alternative_allocation, sa.excluded_income | - |
| 30 | f4952.alternative_allocation, sa.excluded_income | - |
| 31 | f4952.alternative_allocation, sa.excluded_income | - |
| 32 | f4952.alternative_allocation, sa.excluded_income | - |
| 33 | f4952.alternative_allocation, sa.excluded_income | - |
| 34 | f4952.alternative_allocation, sa.excluded_income | - |
| 35 | f4952.alternative_allocation | - |
| 36 | f4952.alternative_allocation, sa.excluded_income | - |
| 37 | sa.excluded_income | - |
| 38 | f4952.alternative_allocation, sa.excluded_income | - |
| 39 | f4952.alternative_allocation, sa.excluded_income | - |
| 40 | f4952.alternative_allocation, sa.excluded_income | - |
| 41 | f4952.alternative_allocation, sa.excluded_income | - |
| 42 | f4952.alternative_allocation, sa.excluded_income | - |
| 43 | f4952.alternative_allocation, sa.excluded_income | - |
| 44 | f4952.alternative_allocation, sa.excluded_income | - |
| 45 | f4952.alternative_allocation, sa.excluded_income | - |
| 46 | sa.excluded_income | - |
| 47 | f4952.alternative_allocation, sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sdtw.line1
    printed: "1"
    label: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    refuses: [sa.excluded_income]
    note: "The Form 2555 case (and the ** footnote on lines 6, 9 and 11) is outside this tool. It is refused through the screening input sa.excluded_income, which asks about Form 2555 and Form 4563."
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
    refuses: [f4952.alternative_allocation]
    note: "Footnote * says to enter instead the smaller amount written on the dotted line next to Form 4952 line 4e, if applicable. No input carries that dotted-line amount. The alternative-allocation case is refused through f4952.alternative_allocation."
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
  - id: sdtw.h_zero_ceiling
    printed: "(helper)"
    label: "$48,350 if single or married filing separately; $96,700 if married filing jointly or qualifying surviving spouse; $64,750 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}
  - id: sdtw.line15
    printed: "15"
    label: "Enter: $48,350 if single or married filing separately; $96,700 if married filing jointly or qualifying surviving spouse; or $64,750 if head of household."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_zero_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. A zero floor, which never changes these positive amounts, establishes the NonNegDollars type."
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
  - id: sdtw.h_ordinary_ceiling
    printed: "(helper)"
    label: "$197,300 if single or married filing separately; $394,600 if married filing jointly or qualifying surviving spouse; $197,300 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: sdtw.ordinary_ceiling}
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
    label: "Subtract line 17 from line 16. This amount is taxed at 0%"
    type: Dollars
    expr: {op: subtract, from: sdtw.line16, take: sdtw.line17}
  - id: sdtw.h_zero
    printed: "(helper)"
    label: "Zero, for a line the worksheet skips"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sdtw.h_skip_a
    printed: "(helper)"
    label: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44"
    type: Bool
    expr: {op: test, eq: [sdtw.line1, sdtw.line16]}
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
    note: "Line 22 is always computed in this model, so it is never blank."
  - id: sdtw.line25
    printed: "25"
    label: "Subtract line 24 from line 23. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line23, take: sdtw.line24}
  - id: sdtw.h_fifteen_ceiling
    printed: "(helper)"
    label: "$533,400 if single; $300,000 if married filing separately; $600,050 if married filing jointly or qualifying surviving spouse; $566,700 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}
  - id: sdtw.line26
    printed: "26"
    label: "Enter: $533,400 if single; $300,000 if married filing separately; $600,050 if married filing jointly or qualifying surviving spouse; or $566,700 if head of household."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_fifteen_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. A zero floor, which never changes these positive amounts, establishes the NonNegDollars type."
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
  - id: sdtw.h_line30_raw
    printed: "(helper)"
    label: "The smaller of line 25 or line 29"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line25, sdtw.line29]}
  - id: sdtw.line30
    printed: "30"
    label: "Enter the smaller of line 25 or line 29"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip_a, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip_a, {const: false}]}
          then: sdtw.h_line30_raw
    note: "Skipped lines are treated as blank, that is zero. The skip after line 22 makes this line zero, and so line 31 is zero too."
  - id: sdtw.line31
    printed: "31"
    label: "Multiply line 30 by 15% (0.15)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line30, rate: {param: sdtw.rate15}}
  - id: sdtw.line32
    printed: "32"
    label: "Add lines 24 and 30"
    type: Dollars
    expr: {op: sum, of: [sdtw.line24, sdtw.line30]}
  - id: sdtw.h_skip_b
    printed: "(helper)"
    label: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44"
    type: Bool
    expr: {op: test, eq: [sdtw.line1, sdtw.line32]}
  - id: sdtw.h_skip_33
    printed: "(helper)"
    label: "Lines 33 and 34 are skipped (by the instruction after line 22 or after line 32)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sdtw.h_skip_a, {const: true}]}
        - {op: test, eq: [sdtw.h_skip_b, {const: true}]}
  - id: sdtw.h_line33_raw
    printed: "(helper)"
    label: "Line 23 minus line 32"
    type: Dollars
    expr: {op: subtract, from: sdtw.line23, take: sdtw.line32}
  - id: sdtw.line33
    printed: "33"
    label: "Subtract line 32 from line 23"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip_33, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip_33, {const: false}]}
          then: sdtw.h_line33_raw
    note: "Skipped lines are treated as blank, that is zero."
  - id: sdtw.line34
    printed: "34"
    label: "Multiply line 33 by 20% (0.20)"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line33, rate: {param: sdtw.rate20}}
  - id: sdtw.h_no19
    printed: "(helper)"
    label: "Schedule D, line 19, is zero or blank"
    type: Bool
    expr: {op: test, eq: [sd.line19, {const: 0}]}
  - id: sdtw.h_no18
    printed: "(helper)"
    label: "Schedule D, line 18, is zero or blank"
    type: Bool
    expr: {op: test, eq: [sd.line18, {const: 0}]}
  - id: sdtw.h_skip_39
    printed: "(helper)"
    label: "Lines 35 through 40 are skipped"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sdtw.h_skip_a, {const: true}]}
        - {op: test, eq: [sdtw.h_skip_b, {const: true}]}
        - {op: test, eq: [sdtw.h_no19, {const: true}]}
  - id: sdtw.h_skip_42
    printed: "(helper)"
    label: "Lines 41 through 43 are skipped"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sdtw.h_skip_a, {const: true}]}
        - {op: test, eq: [sdtw.h_skip_b, {const: true}]}
        - {op: test, eq: [sdtw.h_no18, {const: true}]}
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
  - id: sdtw.h_line39_raw
    printed: "(helper)"
    label: "Line 35 minus line 38, zero if zero or less"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line35, take: sdtw.line38}
  - id: sdtw.line39
    printed: "39"
    label: "Subtract line 38 from line 35. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip_39, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip_39, {const: false}]}
          then: sdtw.h_line39_raw
    note: "Skipped lines are treated as blank, that is zero, both on line 40 and where line 41 adds line 39."
  - id: sdtw.line40
    printed: "40"
    label: "Multiply line 39 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line39, rate: {param: sdtw.rate25}}
  - id: sdtw.line41
    printed: "41"
    label: "Add lines 21, 22, 30, 33, and 39"
    type: Dollars
    expr: {op: sum, of: [sdtw.line21, sdtw.line22, sdtw.line30, sdtw.line33, sdtw.line39]}
  - id: sdtw.h_line42_raw
    printed: "(helper)"
    label: "Line 1 minus line 41"
    type: Dollars
    expr: {op: subtract, from: sdtw.line1, take: sdtw.line41}
  - id: sdtw.line42
    printed: "42"
    label: "Subtract line 41 from line 1"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip_42, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip_42, {const: false}]}
          then: sdtw.h_line42_raw
    note: "Skipped lines are treated as blank, that is zero. Line 41 is not gated separately because line 42 is the only line that reads it."
  - id: sdtw.line43
    printed: "43"
    label: "Multiply line 42 by 28% (0.28)"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line42, rate: {param: sdtw.rate28}}
  - id: sdtw.h_tax21
    printed: "(helper)"
    label: "Tax on the amount on line 21 (Tax Table if less than $100,000; otherwise Tax Computation Worksheet)"
    type: Dollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line21, status: f1040.status}, line: tax}}
  - id: sdtw.line44
    printed: "44"
    label: "Figure the tax on the amount on line 21. If the amount on line 21 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 21 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_tax21, take: {const: 0}}
    note: "The shared tax_on_amount result is declared Dollars. A zero floor establishes the declared NonNegDollars type, since tax on a nonnegative amount is never negative."
  - id: sdtw.line45
    printed: "45"
    label: "Add lines 31, 34, 40, 43, and 44"
    type: Dollars
    expr: {op: sum, of: [sdtw.line31, sdtw.line34, sdtw.line40, sdtw.line43, sdtw.line44]}
  - id: sdtw.h_tax1
    printed: "(helper)"
    label: "Tax on the amount on line 1 (Tax Table if less than $100,000; otherwise Tax Computation Worksheet)"
    type: Dollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line1, status: f1040.status}, line: tax}}
  - id: sdtw.line46
    printed: "46"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.h_tax1, take: {const: 0}}
    note: "The shared tax_on_amount result is declared Dollars. A zero floor establishes the declared NonNegDollars type."
  - id: sdtw.line47
    printed: "47"
    label: "Tax on all taxable income (including capital gains and qualified dividends). Enter the smaller of line 45 or line 46. Also, include this amount on Form 1040, 1040-SR, or 1040-NR, line 16."
    type: Dollars
    expr: {op: smaller_of, of: [sdtw.line45, sdtw.line46]}
```
```
