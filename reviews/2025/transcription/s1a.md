# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | eb98091d1d930b295524d13c99e284a0b02586640b44c8ce59e9ef766a891e1a |
| printed lines compared | 43 |
| agree / disagree / missing | 10 / 33 / 0 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}], "test": "all"}, "then": {"collection": "person", "field": "person.tip_reported", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "ne"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: how the one-employer case is detected with two people on the return. Chosen: the one-employer route applies only when exactly one employer paid tips to anyone on the return and that recipient has a valid SSN. Otherwise line 4a is -0- and line 4c comes from the More Than One Employer Worksheet, as the form directs for multiple employers. Both routes give the same line 4c.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a. The project also counts only the tips of a person with a valid SSN ('the spouse who received ... must have a valid SSN'); the second sums every person's.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}], "test": "all"}, "then": {"collection": "tipjob", "field": "tipjob.col_c", "op": "sum_over", "where": null}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "ne"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: refusal representation; project retained. The line is $0 within scope and carries its own refusal for the form it would come from (Form 4137, through s2.other), as ruled in Stage 12 (BUG-0043); tips earned in a trade or business are refused on line 5 (scope.schedule1 and, from Stage 14, s1.sc_1a for a Schedule C). The second figures the refused amount, or zero without the refusal.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}, {"const": 1}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "ne"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"collection": "person", "field": "person.tip_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": null}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.tip_employers", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Tips of a person without a valid SSN (valid for employment, issued before the due date) are excluded. The text says the spouse who received the tips must have one. Married filing separately gives zero, since married filers must file jointly to claim this deduction.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

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
{"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}
```

Second transcription's note: When line 10 is zero or less, lines 11 and 12 are zero here, so this gives line 7, as the line 10 instruction directs.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "person", "field": "person.ot_total", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: qualified overtime not included in Form W-2, box 1 (for example, deferred amounts). No input or screen for it is provided, so only the worksheet column (b) amounts are entered.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

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
{"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "otjob", "field": "otjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 23 — Add lines 22a and 22b, column (iii)
Status: **AGREE**

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
{"amount": {"of": {"from": {"line": "25"}, "op": "subtract_floor0", "take": {"line": "26"}}, "op": "round", "rule": "up", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.two_hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 30 — Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zer
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "25"}, {"line": "26"}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"line": "26"}, {"line": "25"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}
```

Second transcription's note: When line 27 is zero or less, lines 28 and 29 are zero, so this gives line 24, as the line 27 instruction directs.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a. Part IV has no joint-filing or SSN condition in either.

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
{"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"line": "32"}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"line": "32"}, {"line": "31"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}
```

Second transcription's note: When line 33 is zero or less, line 34 is zero, so line 35 is $6,000, as the line 33 instruction directs.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading in Stage 12); the second figures the line whether or not the part applies. The Stage 13 conditions are those of the instructions (i1040gi p. 101; p. 106; p. 110). Stage 14 adds no condition here; Schedule C tips and overtime are refused through s1.sc_1a.

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

Second transcription's note: Valid SSN is read as person.work_ssn (valid for employment, issued before the due date). Married filing separately gives zero, since married filers must file jointly. A taxpayer born before January 2, 1961 who died in 2025 before reaching age 65 does not qualify.

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
| 5 | s1.sc_1a | - |
| 6 | s1.sc_1a | - |
| 7 | s1.sc_1a | - |
| 8 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 13 | s1.sc_1a | - |
| 14b | s1.sc_1a | - |
| 14c | s1.sc_1a | - |
| 15 | s1.sc_1a | - |
| 16 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 21 | s1.sc_1a | - |
| 25 | sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 31 | sa.excluded_income | - |
| 33 | sa.excluded_income | - |
| 34 | sa.excluded_income | - |
| 35 | sa.excluded_income | - |
| 36a | sa.excluded_income | - |
| 36b | sa.excluded_income | - |
| 37 | sa.excluded_income | - |
| 38 | s1.sc_1a, sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: s1a.h_zero
    printed: "(helper)"
    label: "Zero"
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

  # ---- Part II helpers ----
  - id: s1a.h_tip_ok
    printed: "(helper)"
    label: "Received qualified tips and not married filing separately (if married, you must file jointly to claim this deduction)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.tips, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.h_tip_emp_valid
    printed: "(helper)"
    label: "Number of employers paying qualified tips to persons with a valid SSN"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.tip_employers
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: s1a.h_tip_emp_all
    printed: "(helper)"
    label: "Number of employers paying qualified tips to anyone on the return"
    type: Count
    expr: {op: sum_over, collection: person, field: person.tip_employers}

  - id: s1a.h_tip_single
    printed: "(helper)"
    label: "Qualified tips as an employee from only one employer (and the recipient has a valid SSN)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.h_tip_ok, {const: true}]}
        - {op: test, eq: [s1a.h_tip_emp_valid, {param: person.one}]}
        - {op: test, eq: [s1a.h_tip_emp_all, {param: person.one}]}

  - id: s1a.h_tip_multi
    printed: "(helper)"
    label: "Qualified tips claimed, but not the one-employer case (worksheet applies)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.h_tip_ok, {const: true}]}
        - {op: test, eq: [s1a.h_tip_single, {const: false}]}

  - id: s1a.h_tip_4a_amt
    printed: "(helper)"
    label: "Qualified tips reported by the one employer (Form W-2, box 7, or Forms 4070)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.tip_reported
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: s1a.h_tip_4b_amt
    printed: "(helper)"
    label: "Qualified tips on Form 4137, column 1(c), for the one employer"
    type: NonNegDollars
    expr: {op: sum_over, collection: tipjob, field: tipjob.col_c}

  - id: s1a.line4a
    printed: "4a"
    label: "Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_tip_single, {const: true}]}, then: s1a.h_tip_4a_amt}
        - {guard: {op: test, eq: [s1a.h_tip_single, {const: false}]}, then: s1a.h_zero}
    note: "Open: how the one-employer case is detected with two people on the return. Chosen: the one-employer route applies only when exactly one employer paid tips to anyone on the return and that recipient has a valid SSN. Otherwise line 4a is -0- and line 4c comes from the More Than One Employer Worksheet, as the form directs for multiple employers. Both routes give the same line 4c."

  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_tip_single, {const: true}]}, then: s1a.h_tip_4b_amt}
        - {guard: {op: test, eq: [s1a.h_tip_single, {const: false}]}, then: s1a.h_zero}

  - id: s1a.h_tip_larger
    printed: "(helper)"
    label: "The larger of line 4a or line 4b"
    type: NonNegDollars
    expr: {op: larger_of, of: [s1a.line4a, s1a.line4b]}

  - id: s1a.h_tip_ws_total
    printed: "(helper)"
    label: "Qualified Tips From More Than One Employer Worksheet, line 2 (column (d) total) for persons with a valid SSN"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.tip_total
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_tip_single, {const: true}]}, then: s1a.h_tip_larger}
        - {guard: {op: test, eq: [s1a.h_tip_multi, {const: true}]}, then: s1a.h_tip_ws_total}
        - {guard: {op: test, eq: [s1a.h_tip_ok, {const: false}]}, then: s1a.h_zero}
    note: "Tips of a person without a valid SSN (valid for employment, issued before the due date) are excluded. The text says the spouse who received the tips must have one. Married filing separately gives zero, since married filers must file jointly to claim this deduction."

  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [s1.sc_1a]

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
        - {guard: {op: test, eq: [f1040.status, {const: "mfj"}]}, then: s1a.h_base_joint}
        - {guard: {op: test, ne: [f1040.status, {const: "mfj"}]}, then: s1a.h_base_other}

  - id: s1a.line10
    printed: "10"
    label: "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"
    type: Dollars
    expr: {op: subtract, from: s1a.line8, take: s1a.line9}

  - id: s1a.h_l10_pos
    printed: "(helper)"
    label: "Line 10 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line8, take: s1a.line9}

  - id: s1a.h_line11
    printed: "(helper)"
    label: "Line 11 times $1,000: line 10 divided by $1,000, decreased to the next lower whole number"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_l10_pos, unit: 100000, rule: down}
    note: "Line 11 is held as $1,000 times the whole number, because there is no division atom. Line 12 multiplies it by 1/10, which gives $100 times line 11 exactly."

  - id: s1a.line12
    printed: "12"
    label: "Multiply line 11 by $100"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_line11, rate: {param: s1a.hundred_per_thousand}}

  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line7, take: s1a.line12}
    note: "When line 10 is zero or less, lines 11 and 12 are zero here, so this gives line 7, as the line 10 instruction directs."

  # ---- Part III ----
  - id: s1a.h_ot_ok
    printed: "(helper)"
    label: "Received qualified overtime compensation and not married filing separately"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [s1a.overtime, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.h_ot_total
    printed: "(helper)"
    label: "Qualified overtime reported on Form W-2, box 1 (worksheet column (b) total), for persons with a valid SSN"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ot_total
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_ot_ok, {const: true}]}, then: s1a.h_ot_total}
        - {guard: {op: test, eq: [s1a.h_ot_ok, {const: false}]}, then: s1a.h_zero}
    note: "Open: qualified overtime not included in Form W-2, box 1 (for example, deferred amounts). No input or screen for it is provided, so only the worksheet column (b) amounts are entered."

  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"
    type: NonNegDollars
    expr: {op: copy, from: s1a.h_zero}
    refuses: [s1.sc_1a]

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
        - {guard: {op: test, eq: [f1040.status, {const: "mfj"}]}, then: s1a.h_ot_max_joint}
        - {guard: {op: test, ne: [f1040.status, {const: "mfj"}]}, then: s1a.h_ot_max_other}

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
        - {guard: {op: test, eq: [f1040.status, {const: "mfj"}]}, then: s1a.h_base_joint}
        - {guard: {op: test, ne: [f1040.status, {const: "mfj"}]}, then: s1a.h_base_other}

  - id: s1a.line18
    printed: "18"
    label: "Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21"
    type: Dollars
    expr: {op: subtract, from: s1a.line16, take: s1a.line17}

  - id: s1a.h_l18_pos
    printed: "(helper)"
    label: "Line 18 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line16, take: s1a.line17}

  - id: s1a.h_line19
    printed: "(helper)"
    label: "Line 19 times $1,000: line 18 divided by $1,000, decreased to the next lower whole number"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_l18_pos, unit: 100000, rule: down}

  - id: s1a.line20
    printed: "20"
    label: "Multiply line 19 by $100"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_line19, rate: {param: s1a.hundred_per_thousand}}

  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line15, take: s1a.line20}

  # ---- Part IV ----
  - id: s1a.h_car_total
    printed: "(helper)"
    label: "Total of line 22, column (iii), for all vehicles"
    type: NonNegDollars
    expr: {op: sum_over, collection: carloan, field: carloan.col_iii}

  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.carloan, {const: true}]}, then: s1a.h_car_total}
        - {guard: {op: test, eq: [s1a.carloan, {const: false}]}, then: s1a.h_zero}
    note: "More than two VINs are included through the attached statement, so all loan entries are summed."

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
        - {guard: {op: test, eq: [f1040.status, {const: "mfj"}]}, then: s1a.h_car_base_joint}
        - {guard: {op: test, ne: [f1040.status, {const: "mfj"}]}, then: s1a.h_car_base_other}

  - id: s1a.line27
    printed: "27"
    label: "Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30"
    type: Dollars
    expr: {op: subtract, from: s1a.line25, take: s1a.line26}

  - id: s1a.h_l27_pos
    printed: "(helper)"
    label: "Line 27 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line25, take: s1a.line26}

  - id: s1a.h_line28
    printed: "(helper)"
    label: "Line 28 times $1,000: line 27 divided by $1,000, increased to the next higher whole number"
    type: NonNegDollars
    expr: {op: round, of: s1a.h_l27_pos, unit: 100000, rule: up}

  - id: s1a.line29
    printed: "29"
    label: "Multiply line 28 by $200"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_line28, rate: {param: s1a.two_hundred_per_thousand}}

  - id: s1a.line30
    printed: "30"
    label: "Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line24, take: s1a.line29}
    note: "When line 27 is zero or less, lines 28 and 29 are zero, so this gives line 24, as the line 27 instruction directs."

  # ---- Part V ----
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
        - {guard: {op: test, eq: [f1040.status, {const: "mfj"}]}, then: s1a.h_senior_base_joint}
        - {guard: {op: test, ne: [f1040.status, {const: "mfj"}]}, then: s1a.h_senior_base_other}

  - id: s1a.line33
    printed: "33"
    label: "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"
    type: Dollars
    expr: {op: subtract, from: s1a.line31, take: s1a.line32}

  - id: s1a.h_l33_pos
    printed: "(helper)"
    label: "Line 33 if more than zero, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.line31, take: s1a.line32}

  - id: s1a.line34
    printed: "34"
    label: "Multiply line 33 by 6% (0.06)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: s1a.h_l33_pos, rate: {param: s1a.senior_rate}}

  - id: s1a.h_senior_amount
    printed: "(helper)"
    label: "$6,000"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_amount}

  - id: s1a.line35
    printed: "35"
    label: "Subtract line 34 from $6,000. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1a.h_senior_amount, take: s1a.line34}
    note: "When line 33 is zero or less, line 34 is zero, so line 35 is $6,000, as the line 33 instruction directs."

  - id: s1a.h_tp_senior
    printed: "(helper)"
    label: "Your entry, if you have a valid SSN, were born before January 2, 1961, and did not die in 2025 before reaching age 65"
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

  - id: s1a.h_sp_senior
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse has a valid SSN, was born before January 2, 1961, and did not die in 2025 before reaching age 65"
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

  - id: s1a.h_36a_ok
    printed: "(helper)"
    label: "You qualify for line 36a (and are not married filing separately)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [s1a.h_tp_senior, {param: person.one}]}
        - {op: test, ne: [f1040.status, {const: "mfs"}]}

  - id: s1a.line36a
    printed: "36a"
    label: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_36a_ok, {const: true}]}, then: s1a.line35}
        - {guard: {op: test, eq: [s1a.h_36a_ok, {const: false}]}, then: s1a.h_zero}
    note: "Valid SSN is read as person.work_ssn (valid for employment, issued before the due date). Married filing separately gives zero, since married filers must file jointly. A taxpayer born before January 2, 1961 who died in 2025 before reaching age 65 does not qualify."

  - id: s1a.h_36b_ok
    printed: "(helper)"
    label: "Married filing jointly and your spouse qualifies for line 36b"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [s1a.h_sp_senior, {param: person.one}]}
        - {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: s1a.line36b
    printed: "36b"
    label: "If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [s1a.h_36b_ok, {const: true}]}, then: s1a.line35}
        - {guard: {op: test, eq: [s1a.h_36b_ok, {const: false}]}, then: s1a.h_zero}

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
