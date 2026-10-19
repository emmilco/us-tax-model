# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1b20984030f18e3f7769d72cf668a4f55dd93fa551d55cd9306ff446351c7e8a |
| printed lines compared | 43 |
| agree / disagree / missing | 9 / 34 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1a | 2025; created 2025-11-04 | 1, 2 | whole document | 9212bddf526545414e393e3e0d1e167b124f3753525e18b423716bf49a38bd16 | - | 7b00045023f5d062bee73f9176d9baf0e43f9744899b5fc6a36088fc4dbd9d4b |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104, 105, 106, 108, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104, 106, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
Status: **AGREE**

### 2a — Enter any income from Puerto Rico that you excluded
Status: **AGREE**

### 2b — Enter the amount from Form 2555, line 45
Status: **AGREE**

### 2c — Enter the amount from Form 2555, line 50
Status: **AGREE**

### 2d — Enter the amount from Form 4563, line 15
Status: **AGREE**

### 2e — Add lines 2a, 2b, 2c, and 2d
Status: **AGREE**

### 3 — Add lines 1 and 2e
Status: **AGREE**

### 4a — Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, bo
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1}], "test": "le"}, "then": {"collection": "person", "field": "person.tip_reported", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"collection": "person", "field": "person.tip_reported", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The form says to enter -0- on lines 4a and 4b when there is more than one employer. The employer count is taken across you and your spouse, following the line 4c instructions. The amount uses the per-employer column (b) amount, which covers the W-2 box 7 or Form 4070 methods in the instructions.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"collection": "tipjob", "field": "tipjob.col_c", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: refusal representation; project retained. The line is $0 within scope and carries its own refusal for the forms it would come from (Form 4137 through s2.other; a trade or business, Forms 1099-NEC, 1099-MISC or 1099-K, through scope.schedule1), as ruled in Stage 12 (BUG-0043); the second figures the refused amount, or zero without the refusal.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": null}}], "op": "choose"}
```

Second transcription's note: The instructions for tips received in more than one occupation are not encoded. Only tips from listed occupations are expected in the tipjob entries.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 5 — Qualified tips received in the course of a trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: Tips from a trade or business (Forms 1099-NEC, 1099-MISC, 1099-K, with the net income limitation) are outside the supported income scope. The tool computes only the case with none and refuses otherwise.

Ruling: refusal representation; project retained. The line is $0 within scope and carries its own refusal for the forms it would come from (Form 4137 through s2.other; a trade or business, Forms 1099-NEC, 1099-MISC or 1099-K, through scope.schedule1), as ruled in Stage 12 (BUG-0043); the second figures the refused amount, or zero without the refusal.

### 6 — Add lines 4c and 5
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 8 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 12 — Multiply line 11 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "10"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "10"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"line": "7"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"line": "10"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": null}
```

Second transcription's note: Uses the More Than One Employer Worksheet column (b) total for every case. With one employer this is that employer's amount. Qualified overtime not reported in W-2 box 1 (for example, deferred amounts) has no supported input and is not encoded.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Ruling: refusal representation; project retained. The line is $0 within scope and carries its own refusal for the forms it would come from (Form 4137 through s2.other; a trade or business, Forms 1099-NEC, 1099-MISC or 1099-K, through scope.schedule1), as ruled in Stage 12 (BUG-0043); the second figures the refused amount, or zero without the refusal.

### 14c — Add lines 14a and 14b
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.ot_max_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.ot_max_other"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The project also counts only the tips or overtime of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 16 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 20 — Multiply line 19 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "18"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "18"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"line": "18"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 23 — Add lines 22a and 22b, column (iii)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}}], "op": "choose"}
```

Second:

```json
{"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}
```

Second transcription's note: Column (iii) is summed over all loan entries, which also covers more than two VINs reported on an attached statement. Column (ii), interest deducted on Schedule C, E or F, is outside the supported scope.

Ruling: owner's ruling; project retained. Part IV's printed lines are $0 unless qualified passenger vehicle loan interest was paid or accrued (s1a.carloan; Schedule 1-A, 'Fill out Part IV only if', i1040gi p. 109); the second figures them whether or not Part IV applies. Part IV has no joint-filing or SSN condition in either.

### 24 — Enter the smaller of the amount on line 23 or $10,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "23"}, {"param": "s1a.car_max"}], "op": "smaller_of"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 25 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"line": "3"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 26 — Enter $100,000 ($200,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.car_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.car_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.car_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.car_base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 27 — Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"from": {"line": "25"}, "op": "subtract", "take": {"line": "26"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "25"}, "op": "subtract", "take": {"line": "26"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 29 — Multiply line 28 by $200
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"amount": {"of": {"from": {"line": "25"}, "op": "subtract_floor0", "take": {"line": "26"}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "27"}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "25"}, {"line": "26"}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"line": "26"}, {"line": "25"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, {"args": [{"line": "27"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"line": "24"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "27"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}, {"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The text for Part IV states no joint-filing or SSN requirement, so none is encoded. Part IV is filled out only if QPVLI was paid or accrued (s1a.carloan).

Ruling: owner's ruling; project retained. Part IV's printed lines are $0 unless qualified passenger vehicle loan interest was paid or accrued (s1a.carloan; Schedule 1-A, 'Fill out Part IV only if', i1040gi p. 109); the second figures them whether or not Part IV applies. Part IV has no joint-filing or SSN condition in either.

### 31 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.senior_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.senior_base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 34 — Multiply line 33 by 6% (0.06)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"line": "32"}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"line": "32"}, {"line": "31"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"const": 0}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"const": 0}, {"line": "33"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110).

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1}], "test": "lt"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The Part V caution says 'If married, you must file jointly to claim this deduction.' This is encoded as no amount for married filing separately.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The second gives $0 for a person born before January 2, 1961, who died in 2025 before reaching age 65; the project refuses that case (owner's ruling, Stage 12; i1040gi p. 110, Death of a taxpayer in 2025), for each spouse separately.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"line": "35"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions: Part II and Part III need 'a valid social security number (SSN). If you are married filing a joint return, the spouse who received the qualified tips [overtime] must have a valid SSN' (i1040gi p. 101; p. 106), Part V 'the spouse who is claiming the enhanced deduction for seniors' (p. 110). The second gives $0 for a person born before January 2, 1961, who died in 2025 before reaching age 65; the project refuses that case (owner's ruling, Stage 12; i1040gi p. 110, Death of a taxpayer in 2025), for each spouse separately.

### 37 — Enhanced deduction for seniors. Add lines 36a and 36b
Status: **AGREE**

### 38 — Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 2a | sa.excluded_income | - |
| 2b | sa.excluded_income | sa.excluded_income |
| 2c | sa.excluded_income | sa.excluded_income |
| 2d | sa.excluded_income | sa.excluded_income |
| 2e | sa.excluded_income | - |
| 3 | sa.excluded_income | - |
| 5 | scope.other_income | scope.other_income |
| 6 | scope.other_income | scope.other_income |
| 7 | scope.other_income | scope.other_income |
| 8 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 13 | sa.excluded_income, scope.other_income | - |
| 14b | scope.other_income | scope.other_income |
| 14c | scope.other_income | scope.other_income |
| 15 | scope.other_income | scope.other_income |
| 16 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 21 | sa.excluded_income, scope.other_income | - |
| 25 | sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 30 | sa.excluded_income | - |
| 31 | sa.excluded_income | - |
| 33 | sa.excluded_income | - |
| 34 | sa.excluded_income | - |
| 35 | sa.excluded_income | - |
| 36a | sa.excluded_income | - |
| 36b | sa.excluded_income | - |
| 37 | sa.excluded_income | - |
| 38 | sa.excluded_income, scope.other_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: s1a.h_zero
    printed: "(helper)"
    label: "Zero amount (year parameter sales.zero)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: s1a.line1
    printed: "1"
    label: "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}

  - id: s1a.line2a
    printed: "2a"
    label: "Enter any income from Puerto Rico that you excluded"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [sa.excluded_income]

  - id: s1a.line2b
    printed: "2b"
    label: "Enter the amount from Form 2555, line 45"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [sa.excluded_income]

  - id: s1a.line2c
    printed: "2c"
    label: "Enter the amount from Form 2555, line 50"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [sa.excluded_income]

  - id: s1a.line2d
    printed: "2d"
    label: "Enter the amount from Form 4563, line 15"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [sa.excluded_income]

  - id: s1a.line2e
    printed: "2e"
    label: "Add lines 2a, 2b, 2c, and 2d"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line2a, s1a.line2b, s1a.line2c, s1a.line2d]}

  - id: s1a.line3
    printed: "3"
    label: "Add lines 1 and 2e"
    type: Dollars
    expr: {op: sum, of: [s1a.line1, s1a.line2e]}

  - id: s1a.h_tip_employers
    printed: "(helper)"
    label: "Number of employers that paid you (and your spouse) qualified tips as employees"
    type: Count
    expr: {op: sum_over, collection: person, field: person.tip_employers}

  - id: s1a.h_tip_reported
    printed: "(helper)"
    label: "Qualified tips reported on Form W-2 box 7 (or Forms 4070), worksheet column (b) total"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.tip_reported}

  - id: s1a.h_tip_col_c
    printed: "(helper)"
    label: "Qualified tips included on Form 4137, line 1, column (c), all employers"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_c}
    note: "No person-level column (c) total exists, so the nested tipjob collection is summed across all person entries directly. Used only when there is at most one employer."

  - id: s1a.h_tip_worksheet
    printed: "(helper)"
    label: "Qualified Tips From More Than One Employer Worksheet, line 2 (column (d) total)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.tip_total}

  - id: s1a.line4a
    printed: "4a"
    label: "Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_tip_reported
        - guard: {op: test, gt: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_zero
    note: "The form says to enter -0- on lines 4a and 4b when there is more than one employer. The employer count is taken across you and your spouse, following the line 4c instructions. The amount uses the per-employer column (b) amount, which covers the W-2 box 7 or Form 4070 methods in the instructions."

  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_tip_col_c
        - guard: {op: test, gt: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_zero

  - id: s1a.h_tip_larger
    printed: "(helper)"
    label: "The larger of line 4a or line 4b"
    type: NonNegDollars
    expr: {op: larger_of, of: [s1a.line4a, s1a.line4b]}

  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_tip_larger
        - guard: {op: test, gt: [s1a.h_tip_employers, {param: person.one}]}
          then: s1a.h_tip_worksheet
    note: "The instructions for tips received in more than one occupation are not encoded. Only tips from listed occupations are expected in the tipjob entries."

  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [scope.other_income]
    note: "Tips from a trade or business (Forms 1099-NEC, 1099-MISC, 1099-K, with the net income limitation) are outside the supported income scope. The tool computes only the case with none and refuses otherwise."

  - id: s1a.line6
    printed: "6"
    label: "Add lines 4c and 5"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line4c, s1a.line5]}

  - id: s1a.h_tips_max
    printed: "(helper)"
    label: "$25,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.tips_max}

  - id: s1a.line7
    printed: "7"
    label: "Enter the smaller of the amount on line 6 or $25,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line6, s1a.h_tips_max]}

  - id: s1a.line8
    printed: "8"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.h_base_other
    printed: "(helper)"
    label: "$150,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_other}

  - id: s1a.h_base_joint
    printed: "(helper)"
    label: "$300,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_joint}

  - id: s1a.line9
    printed: "9"
    label: "Enter $150,000 ($300,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_other

  - id: s1a.line10
    printed: "10"
    label: "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"
    type: Dollars
    expr: {op: subtract, from: s1a.line8, take: s1a.line9}

  - id: s1a.h_line11
    printed: "(helper)"
    label: "Divide line 10 by $1,000. If the resulting number isn't a whole number, decrease the result to the next lower whole number"
    type: Dollars
    expr: {op: round, of: s1a.line10, unit: 100000, rule: down}
    note: "Printed line 11 is held as line 10 rounded down to a whole $1,000, so line 12 is that amount times 1/10. This equals the whole number of thousands times $100. It is used only when line 10 is more than zero."

  - id: s1a.line12
    printed: "12"
    label: "Multiply line 11 by $100"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_line11, rate: {param: s1a.hundred_per_thousand}}

  - id: s1a.h_line13_reduced
    printed: "(helper)"
    label: "Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line7, take: s1a.line12}

  - id: s1a.h_tips_ok
    printed: "(helper)"
    label: "Part II applies: qualified tips received, not married filing separately, and a valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.tips, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [household.any_work_ssn, {const: true}]}
    note: "The instructions require the spouse who received the tips to have a valid SSN. Only a household-level check (you or your spouse has a work-valid SSN) is encoded here. The per-recipient requirement is assumed to be met by the tip amounts entered."

  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.h_tips_ok, {const: true}]}
              - {op: test, le: [s1a.line10, {const: 0}]}
          then: s1a.line7
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.h_tips_ok, {const: true}]}
              - {op: test, gt: [s1a.line10, {const: 0}]}
          then: s1a.h_line13_reduced
        - guard: {op: test, eq: [s1a.h_tips_ok, {const: false}]}
          then: s1a.h_zero

  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.ot_total}
    note: "Uses the More Than One Employer Worksheet column (b) total for every case. With one employer this is that employer's amount. Qualified overtime not reported in W-2 box 1 (for example, deferred amounts) has no supported input and is not encoded."

  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [scope.other_income]

  - id: s1a.line14c
    printed: "14c"
    label: "Add lines 14a and 14b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line14a, s1a.line14b]}

  - id: s1a.h_ot_max_other
    printed: "(helper)"
    label: "$12,500"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_other}

  - id: s1a.h_ot_max_joint
    printed: "(helper)"
    label: "$25,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_joint}

  - id: s1a.h_ot_max
    printed: "(helper)"
    label: "$12,500 ($25,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_ot_max_other

  - id: s1a.line15
    printed: "15"
    label: "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line14c, s1a.h_ot_max]}

  - id: s1a.line16
    printed: "16"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.line17
    printed: "17"
    label: "Enter $150,000 ($300,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_base_other

  - id: s1a.line18
    printed: "18"
    label: "Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21"
    type: Dollars
    expr: {op: subtract, from: s1a.line16, take: s1a.line17}

  - id: s1a.h_line19
    printed: "(helper)"
    label: "Divide line 18 by $1,000. If the resulting number isn't a whole number, decrease the result to the next lower whole number"
    type: Dollars
    expr: {op: round, of: s1a.line18, unit: 100000, rule: down}
    note: "Printed line 19 is held as line 18 rounded down to a whole $1,000. Line 20 is that amount times 1/10. It is used only when line 18 is more than zero."

  - id: s1a.line20
    printed: "20"
    label: "Multiply line 19 by $100"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_line19, rate: {param: s1a.hundred_per_thousand}}

  - id: s1a.h_line21_reduced
    printed: "(helper)"
    label: "Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line15, take: s1a.line20}

  - id: s1a.h_ot_ok
    printed: "(helper)"
    label: "Part III applies: qualified overtime received, not married filing separately, and a valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.overtime, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}
        - {op: test, eq: [household.any_work_ssn, {const: true}]}
    note: "The per-recipient SSN requirement is reduced to a household-level check, as for tips."

  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.h_ot_ok, {const: true}]}
              - {op: test, le: [s1a.line18, {const: 0}]}
          then: s1a.line15
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.h_ot_ok, {const: true}]}
              - {op: test, gt: [s1a.line18, {const: 0}]}
          then: s1a.h_line21_reduced
        - guard: {op: test, eq: [s1a.h_ot_ok, {const: false}]}
          then: s1a.h_zero

  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr: {op: sum_over, collection: carloan, field: carloan.col_iii}
    note: "Column (iii) is summed over all loan entries, which also covers more than two VINs reported on an attached statement. Column (ii), interest deducted on Schedule C, E or F, is outside the supported scope."

  - id: s1a.h_car_max
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_max}

  - id: s1a.line24
    printed: "24"
    label: "Enter the smaller of the amount on line 23 or $10,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [s1a.line23, s1a.h_car_max]}

  - id: s1a.line25
    printed: "25"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.h_car_base_other
    printed: "(helper)"
    label: "$100,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_other}

  - id: s1a.h_car_base_joint
    printed: "(helper)"
    label: "$200,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_joint}

  - id: s1a.line26
    printed: "26"
    label: "Enter $100,000 ($200,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_car_base_other

  - id: s1a.line27
    printed: "27"
    label: "Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30"
    type: Dollars
    expr: {op: subtract, from: s1a.line25, take: s1a.line26}

  - id: s1a.h_line28
    printed: "(helper)"
    label: "Divide line 27 by $1,000. If the resulting number isn't a whole number, increase the result to the next higher whole number"
    type: Dollars
    expr: {op: round, of: s1a.line27, unit: 100000, rule: up}
    note: "Printed line 28 is held as line 27 rounded up to a whole $1,000. Line 29 is that amount times 1/5, which equals the whole number of thousands times $200. It is used only when line 27 is more than zero."

  - id: s1a.line29
    printed: "29"
    label: "Multiply line 28 by $200"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.h_line28, rate: {param: s1a.two_hundred_per_thousand}}

  - id: s1a.h_line30_reduced
    printed: "(helper)"
    label: "Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line24, take: s1a.line29}

  - id: s1a.line30
    printed: "30"
    label: "Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.carloan, {const: true}]}
              - {op: test, le: [s1a.line27, {const: 0}]}
          then: s1a.line24
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.carloan, {const: true}]}
              - {op: test, gt: [s1a.line27, {const: 0}]}
          then: s1a.h_line30_reduced
        - guard: {op: test, eq: [s1a.carloan, {const: false}]}
          then: s1a.h_zero
    note: "The text for Part IV states no joint-filing or SSN requirement, so none is encoded. Part IV is filled out only if QPVLI was paid or accrued (s1a.carloan)."

  - id: s1a.line31
    printed: "31"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.h_senior_base_other
    printed: "(helper)"
    label: "$75,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_other}

  - id: s1a.h_senior_base_joint
    printed: "(helper)"
    label: "$150,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_joint}

  - id: s1a.line32
    printed: "32"
    label: "Enter $75,000 ($150,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_joint
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: s1a.h_senior_base_other

  - id: s1a.line33
    printed: "33"
    label: "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"
    type: Dollars
    expr: {op: subtract, from: s1a.line31, take: s1a.line32}

  - id: s1a.line34
    printed: "34"
    label: "Multiply line 33 by 6% (0.06)"
    type: Dollars
    expr: {op: multiply_rate, amount: s1a.line33, rate: {param: s1a.senior_rate}}

  - id: s1a.h_senior_amount
    printed: "(helper)"
    label: "$6,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_amount}

  - id: s1a.h_line35_reduced
    printed: "(helper)"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.h_senior_amount, take: s1a.line34}

  - id: s1a.line35
    printed: "35"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.line33, {const: 0}]}
          then: s1a.h_senior_amount
        - guard: {op: test, gt: [s1a.line33, {const: 0}]}
          then: s1a.h_line35_reduced

  - id: s1a.h_senior_taxpayer
    printed: "(helper)"
    label: "Your entry, if you have a valid SSN and were born before January 2, 1961 (and did not die in 2025 before reaching age 65)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
          - {op: test, eq: [person.died_before_65, {const: false}]}
    note: "The instructions define a valid SSN as one valid for employment and issued before the due date, so person.work_ssn is used. The instructions also exclude a person born before January 2, 1961 who died in 2025 before reaching age 65, so person.died_before_65 is used."

  - id: s1a.h_senior_spouse
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse has a valid SSN and was born before January 2, 1961 (and did not die in 2025 before reaching age 65)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
          - {op: test, eq: [person.died_before_65, {const: false}]}

  - id: s1a.line36a
    printed: "36a"
    label: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, ge: [s1a.h_senior_taxpayer, {param: person.one}]}
          then: s1a.line35
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: [f1040.status, {const: "mfs"}]}
                - {op: test, ge: [s1a.h_senior_taxpayer, {param: person.one}]}
          then: s1a.h_zero
    note: "The Part V caution says 'If married, you must file jointly to claim this deduction.' This is encoded as no amount for married filing separately."

  - id: s1a.line36b
    printed: "36b"
    label: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [f1040.status, {const: "mfj"}]}
              - {op: test, ge: [s1a.h_senior_spouse, {param: person.one}]}
          then: s1a.line35
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [f1040.status, {const: "mfj"}]}
                - {op: test, ge: [s1a.h_senior_spouse, {param: person.one}]}
          then: s1a.h_zero

  - id: s1a.line37
    printed: "37"
    label: "Enhanced deduction for seniors. Add lines 36a and 36b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line36a, s1a.line36b]}

  - id: s1a.line38
    printed: "38"
    label: "Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line13, s1a.line21, s1a.line30, s1a.line37]}
```
```
