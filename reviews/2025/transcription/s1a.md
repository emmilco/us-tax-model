# Transcription agreement — s1a

Second transcription of `Schedule 1-A (Form 1040) — Additional Deductions` by an isolated model (spec 6.5), compared line by line with `forms/2025/s1a.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 69ab7c4a9411332727b383dba4a432824016b56ab989b95bc0b5729df05352eb |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"collection": "tipjob", "field": "tipjob.amount", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"collection": "tipjob", "field": "tipjob.amount", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "tipjob.qualified"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: With more than one employer the form says to enter -0- on lines 4a and 4b. With one employer, the amount is the tipjob entry's W-2/Form 4070 amount, counted only when that entry is marked qualified.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 4b — Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"collection": "tipjob", "field": "tipjob.col_c", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "tipjob.qualified"}], "test": "eq"}}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 4c — If you only received qualified tips as an employee with respect to employment with one emp
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "tipjob", "field": "tipjob.col_d", "op": "sum_over", "where": null}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}, {"const": 1}], "test": "le"}], "test": "all"}, "then": {"of": [{"line": "4a"}, {"line": "4b"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "tipjob", "field": "tipjob.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "all"}, "then": {"collection": "tipjob", "field": "tipjob.col_d", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "tipjob.qualified"}], "test": "eq"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Part II applies only to qualified tips, so employee tips count only when s1a.tips is yes. With more than one employer, the amount comes from the multi-employer worksheet total of column (d).

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 5 — Qualified tips received in the course of a trade or business
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"input": "Qualified tip amount included in Form 1099-NEC, box 1; Form "}
```

Second transcription's note: None of the given collections or screening inputs covers the net income limitation, so the filer enters the limited amount.

Ruling: scope; project retained. Qualified tips in a trade or business need Schedule C, E or F and the net income limitation, refused through scope.schedule1, which line 5 carries; the second takes the limited amount as a filer's entry.

### 6 — Add lines 4c and 5
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "4c"}, {"line": "5"}], "op": "sum"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 7 — Enter the smaller of the amount on line 6 or $25,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "6"}, {"param": "s1a.tips_max"}], "op": "smaller_of"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 8 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 9 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 10 — Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "8"}, "op": "subtract", "take": {"line": "9"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 12 — Multiply line 11 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "8"}, "op": "subtract_floor0", "take": {"line": "9"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "10"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 13 — Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.tips"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "8"}, {"line": "9"}], "test": "le"}, "then": {"line": "7"}}, {"guard": {"args": [{"line": "9"}, {"line": "8"}], "test": "lt"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.h_tips_ssn"}], "test": "eq"}, {"args": [{"line": "10"}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "7"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.h_tips_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "10"}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "7"}, "op": "subtract_floor0", "take": {"line": "12"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.h_tips_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The caution says that if married you must file jointly, and that the person who received the tips must have a valid SSN. Married filing separately is read as the only married status that fails; a failed requirement gives zero.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding. The conditions agree: married filing separately and no valid SSN give zero.

### 14a — Qualified overtime compensation included in Form W-2, box 1. If you received qualified ove
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"collection": "otjob", "field": "otjob.col_b", "op": "sum_over", "where": null}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"collection": "otjob", "field": "otjob.col_b", "op": "sum_over", "where": null}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The total over otjob entries is used for one employer as well as for several. It is zero when s1a.overtime is no.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 14b — Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"input": "Qualified overtime compensation included in Form 1099-NEC, b"}
```

Second transcription's note: s1a.overtime asks only about employee overtime, so it does not gate this nonemployee amount.

Ruling: scope; project retained. Overtime reported on Form 1099-NEC or 1099-MISC is nonemployee compensation, refused through scope.schedule1, which line 14b carries.

### 14c — Add lines 14a and 14b
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14a"}, {"line": "14b"}], "op": "sum"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 15 — Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.ot_max_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "14c"}, {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.ot_max_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.ot_max_other"}}], "op": "choose"}], "op": "smaller_of"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 16 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 17 — Enter $150,000 ($300,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 18 — Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "16"}, "op": "subtract", "take": {"line": "17"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 20 — Multiply line 19 by $100
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"of": {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"line": "17"}}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"of": {"line": "18"}, "op": "round", "rule": "down", "unit": 100000}, "op": "multiply_rate", "rate": {"param": "s1a.hundred_per_thousand"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 21 — Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.overtime"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "16"}, {"line": "17"}], "test": "le"}, "then": {"line": "15"}}, {"guard": {"args": [{"line": "17"}, {"line": "16"}], "test": "lt"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.h_ot_ssn"}], "test": "eq"}, {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "15"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.h_ot_ssn"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "18"}], "test": "lt"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "15"}, "op": "subtract_floor0", "take": {"line": "20"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.h_ot_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Same reading as line 13: married filing separately, or no valid SSN, gives zero.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding. The conditions agree: married filing separately and no valid SSN give zero.

### 23 — Add lines 22a and 22b, column (iii)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": null}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "eq"}, "then": {"collection": "carloan", "field": "carloan.col_iii", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}}}, {"guard": {"args": [{"const": true}, {"input": "s1a.carloan"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The instructions say to attach a statement when there are more than two VINs, so all entries are added, not just rows a and b. Only entries whose loan and vehicle qualify are counted.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

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
{"alternatives": [{"guard": {"args": [{"line": "27"}, {"const": 0}], "test": "le"}, "then": {"line": "24"}}, {"guard": {"args": [{"const": 0}, {"line": "27"}], "test": "lt"}, "then": {"from": {"line": "24"}, "op": "subtract_floor0", "take": {"line": "29"}}}], "op": "choose"}
```

Second transcription's note: Unlike Parts II, III and V, the Part IV text has no joint-filing requirement, so no filing status restriction is encoded.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding. Both encode no filing-status restriction in Part IV.

### 31 — Enter the amount from line 3
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "3"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "3"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 32 — Enter $75,000 ($150,000 if married filing jointly)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "s1a.senior_base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "s1a.senior_base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "s1a.senior_base_other"}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 33 — Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "31"}, "op": "subtract", "take": {"line": "32"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 34 — Multiply line 33 by 6% (0.06)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"from": {"line": "31"}, "op": "subtract_floor0", "take": {"line": "32"}}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "s1a.senior_rate"}}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 35 — Subtract line 34 from $6,000. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"line": "31"}, {"line": "32"}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"line": "32"}, {"line": "31"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"const": 0}], "test": "le"}, "then": {"param": "s1a.senior_amount"}}, {"guard": {"args": [{"const": 0}, {"line": "33"}], "test": "lt"}, "then": {"from": {"param": "s1a.senior_amount"}, "op": "subtract_floor0", "take": {"line": "34"}}}], "op": "choose"}
```

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding.

### 36a — If you have a valid social security number (see instructions) and were born before January
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sa.age65"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, "then": {"line": "35"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "s1a.died_before_65"}], "test": "ne"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "sa.age65"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Valid SSN is read as an SSN valid for employment issued before the due date (household.taxpayer_work_ssn). The married-must-file-jointly caution excludes married filing separately. s1a.died_before_65 does not say whether it refers to the taxpayer or the spouse, so it is applied to both lines 36a and 36b.

Ruling: owner's ruling; project retained. Each printed line of Parts II to V is $0 unless its part applies (Schedule 1-A, 'Fill out Part N only if'; the owner chose this strictly accurate reading after class M); the second figures the line whether or not the part applies. Where the part applies the two agree: class M agreed on all 344 values of 8 cases on this encoding. The conditions agree (household.taxpayer_work_ssn; married filing separately excluded). s1a.died_before_65 concerns the filer, the one person represented.

### 36b — If you are married filing jointly, your spouse has a valid social security number (see ins
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.h_spouse_age65"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.h_spouse_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"input": "s1a.died_before_65"}], "test": "ne"}], "test": "all"}, "then": {"line": "35"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "s1a.died_before_65"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "s1a.h_spouse_age65"}], "test": "ne"}, {"args": [{"const": true}, {"input": "s1a.h_spouse_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: s1a.died_before_65 does not name which person died; it is applied here as well as on line 36a.

Ruling: scope; project retained. A spouse born before January 2, 1961, is claimed through the spouse's standard-deduction box, refused through sa.spouse_extra, which line 36b carries; the spouse is not otherwise represented, so a spouse's death before 65 does not arise.

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
| 8 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 13 | sa.excluded_income | - |
| 16 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 21 | sa.excluded_income | - |
| 25 | sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 30 | sa.excluded_income | - |
| 31 | sa.excluded_income | - |
| 33 | sa.excluded_income | - |
| 34 | sa.excluded_income | - |
| 35 | sa.excluded_income | - |
| 36a | sa.excluded_income | - |
| 36b | sa.excluded_income | sa.excluded_income |
| 37 | sa.excluded_income | - |
| 38 | sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: s1a.h_zero
    printed: "(helper)"
    label: "No amount (year parameter sales.zero)"
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
    note: "The tool does not compute excluded Puerto Rico income, so this line is encoded as zero, with a refusal when the filer has such income."

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
    label: "Number of employers from which you received tips as an employee"
    type: Count
    expr: {op: sum_over, collection: tipjob, field: tipjob.one}

  - id: s1a.h_tips_w2_sum
    printed: "(helper)"
    label: "Qualified tips reported by the employer on Form W-2 (or on Forms 4070)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.amount
      where: {op: test, eq: [tipjob.qualified, {const: true}]}

  - id: s1a.line4a
    printed: "4a"
    label: "Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_tips_w2_sum
        - guard: {op: test, gt: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_zero
    note: "With more than one employer the form says to enter -0- on lines 4a and 4b. With one employer, the amount is the tipjob entry's W-2/Form 4070 amount, counted only when that entry is marked qualified."

  - id: s1a.h_tips_4137_sum
    printed: "(helper)"
    label: "Qualified tips reported on Form 4137, column 1(c), for the employer"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.col_c
      where: {op: test, eq: [tipjob.qualified, {const: true}]}

  - id: s1a.line4b
    printed: "4b"
    label: "Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_tips_4137_sum
        - guard: {op: test, gt: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_zero

  - id: s1a.h_4c_one
    printed: "(helper)"
    label: "The larger of line 4a or line 4b"
    type: NonNegDollars
    expr: {op: larger_of, of: [s1a.line4a, s1a.line4b]}

  - id: s1a.h_4c_multi
    printed: "(helper)"
    label: "Qualified Tips From More Than One Employer Worksheet, line 2: add lines 1A through 1E, column (d)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: tipjob
      field: tipjob.col_d
      where: {op: test, eq: [tipjob.qualified, {const: true}]}

  - id: s1a.line4c
    printed: "4c"
    label: "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, not: {op: test, eq: [s1a.tips, {const: true}]}}
          then: s1a.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.tips, {const: true}]}
              - {op: test, le: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_4c_one
        - guard:
            op: test
            all:
              - {op: test, eq: [s1a.tips, {const: true}]}
              - {op: test, gt: [s1a.h_tip_employers, {const: 1}]}
          then: s1a.h_4c_multi
    note: "Part II applies only to qualified tips, so employee tips count only when s1a.tips is yes. With more than one employer, the amount comes from the multi-employer worksheet total of column (d)."

  - id: s1a.line5
    printed: "5"
    label: "Qualified tips received in the course of a trade or business"
    type: NonNegDollars
    expr: {op: input, source: "Qualified tip amount included in Form 1099-NEC, box 1; Form 1099-MISC, box 3; or Form 1099-K, box 1a, not more than the net profit from the trade or business (Multiple Trades or Businesses Worksheet, line 2, if more than one)"}
    note: "None of the given collections or screening inputs covers the net income limitation, so the filer enters the limited amount."

  - id: s1a.line6
    printed: "6"
    label: "Add lines 4c and 5"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line4c, s1a.line5]}

  - id: s1a.h_tips_max
    printed: "(helper)"
    label: "$25,000 (year parameter s1a.tips_max)"
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
    label: "$150,000 (year parameter s1a.base_other)"
    type: NonNegDollars
    expr: {op: param, ref: s1a.base_other}

  - id: s1a.h_base_joint
    printed: "(helper)"
    label: "$300,000 (year parameter s1a.base_joint)"
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
    label: "Line 11 times $1,000: line 10 rounded down to the next lower whole multiple of $1,000 (Divide line 10 by $1,000 ... decrease the result to the next lower whole number)"
    type: Dollars
    expr: {op: round, of: s1a.line10, unit: 100000, rule: down}
    note: "Line 11 (a whole number) is held as a multiple of $1,000 in cents, so line 12 is this amount times 1/10. This helper is used only when line 10 is more than zero."

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

  - id: s1a.h_tips_ssn
    printed: "(helper)"
    label: "Do you (or your spouse, if filing jointly) who received the qualified tips have a valid social security number (valid for employment and issued by the SSA before the due date of your 2025 return, including extensions)?"
    type: Bool
    expr: {op: input, source: "Interview question: valid SSN of the person who received qualified tips"}

  - id: s1a.line13
    printed: "13"
    label: "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "mfs"}]}
              - {op: test, not: {op: test, eq: [s1a.h_tips_ssn, {const: true}]}}
          then: s1a.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [s1a.h_tips_ssn, {const: true}]}
              - {op: test, le: [s1a.line10, {const: 0}]}
          then: s1a.line7
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [s1a.h_tips_ssn, {const: true}]}
              - {op: test, gt: [s1a.line10, {const: 0}]}
          then: s1a.h_line13_reduced
    note: "The caution says that if married you must file jointly, and that the person who received the tips must have a valid SSN. Married filing separately is read as the only married status that fails; a failed requirement gives zero."

  - id: s1a.h_ot_employers_sum
    printed: "(helper)"
    label: "Qualified Overtime Compensation From More Than One Employer Worksheet, line 2: add lines 1A through 1E, column (b)"
    type: NonNegDollars
    expr: {op: sum_over, collection: otjob, field: otjob.col_b}

  - id: s1a.line14a
    printed: "14a"
    label: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.overtime, {const: true}]}
          then: s1a.h_ot_employers_sum
        - guard: {op: test, not: {op: test, eq: [s1a.overtime, {const: true}]}}
          then: s1a.h_zero
    note: "The total over otjob entries is used for one employer as well as for several. It is zero when s1a.overtime is no."

  - id: s1a.line14b
    printed: "14b"
    label: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"
    type: NonNegDollars
    expr: {op: input, source: "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3 (Qualified Overtime Compensation From More Than One Payor Worksheet, line 2, if more than one payor); not the total box amount"}
    note: "s1a.overtime asks only about employee overtime, so it does not gate this nonemployee amount."

  - id: s1a.line14c
    printed: "14c"
    label: "Add lines 14a and 14b"
    type: NonNegDollars
    expr: {op: sum, of: [s1a.line14a, s1a.line14b]}

  - id: s1a.h_ot_max_other
    printed: "(helper)"
    label: "$12,500 (year parameter s1a.ot_max_other)"
    type: NonNegDollars
    expr: {op: param, ref: s1a.ot_max_other}

  - id: s1a.h_ot_max_joint
    printed: "(helper)"
    label: "$25,000 (year parameter s1a.ot_max_joint)"
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
    label: "Line 19 times $1,000: line 18 rounded down to the next lower whole multiple of $1,000 (Divide line 18 by $1,000 ... decrease the result to the next lower whole number)"
    type: Dollars
    expr: {op: round, of: s1a.line18, unit: 100000, rule: down}
    note: "Line 19 is held as a multiple of $1,000 in cents. This helper is used only when line 18 is more than zero."

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

  - id: s1a.h_ot_ssn
    printed: "(helper)"
    label: "Do you (or your spouse, if filing jointly) who received the qualified overtime compensation have a valid social security number (valid for employment and issued by the SSA before the due date of your 2025 return, including extensions)?"
    type: Bool
    expr: {op: input, source: "Interview question: valid SSN of the person who received qualified overtime compensation"}

  - id: s1a.line21
    printed: "21"
    label: "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "mfs"}]}
              - {op: test, not: {op: test, eq: [s1a.h_ot_ssn, {const: true}]}}
          then: s1a.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [s1a.h_ot_ssn, {const: true}]}
              - {op: test, le: [s1a.line18, {const: 0}]}
          then: s1a.line15
        - guard:
            op: test
            all:
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [s1a.h_ot_ssn, {const: true}]}
              - {op: test, gt: [s1a.line18, {const: 0}]}
          then: s1a.h_line21_reduced
    note: "Same reading as line 13: married filing separately, or no valid SSN, gives zero."

  - id: s1a.h_carloan_sum
    printed: "(helper)"
    label: "Total of column (iii) over all qualifying loans (line 22 rows and any attached statement)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: carloan
      field: carloan.col_iii
      where: {op: test, eq: [carloan.eligible, {const: true}]}

  - id: s1a.line23
    printed: "23"
    label: "Add lines 22a and 22b, column (iii)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [s1a.carloan, {const: true}]}
          then: s1a.h_carloan_sum
        - guard: {op: test, not: {op: test, eq: [s1a.carloan, {const: true}]}}
          then: s1a.h_zero
    note: "The instructions say to attach a statement when there are more than two VINs, so all entries are added, not just rows a and b. Only entries whose loan and vehicle qualify are counted."

  - id: s1a.h_car_max
    printed: "(helper)"
    label: "$10,000 (year parameter s1a.car_max)"
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
    label: "$100,000 (year parameter s1a.car_base_other)"
    type: NonNegDollars
    expr: {op: param, ref: s1a.car_base_other}

  - id: s1a.h_car_base_joint
    printed: "(helper)"
    label: "$200,000 (year parameter s1a.car_base_joint)"
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
    label: "Line 28 times $1,000: line 27 rounded up to the next higher whole multiple of $1,000 (Divide line 27 by $1,000 ... increase the result to the next higher whole number)"
    type: Dollars
    expr: {op: round, of: s1a.line27, unit: 100000, rule: up}
    note: "Line 28 is held as a multiple of $1,000 in cents, so line 29 is this amount times 1/5. This helper is used only when line 27 is more than zero."

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
        - guard: {op: test, le: [s1a.line27, {const: 0}]}
          then: s1a.line24
        - guard: {op: test, gt: [s1a.line27, {const: 0}]}
          then: s1a.h_line30_reduced
    note: "Unlike Parts II, III and V, the Part IV text has no joint-filing requirement, so no filing status restriction is encoded."

  - id: s1a.line31
    printed: "31"
    label: "Enter the amount from line 3"
    type: Dollars
    expr: {op: copy, from: s1a.line3}

  - id: s1a.h_senior_base_other
    printed: "(helper)"
    label: "$75,000 (year parameter s1a.senior_base_other)"
    type: NonNegDollars
    expr: {op: param, ref: s1a.senior_base_other}

  - id: s1a.h_senior_base_joint
    printed: "(helper)"
    label: "$150,000 (year parameter s1a.senior_base_joint)"
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
    label: "$6,000 (year parameter s1a.senior_amount)"
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

  - id: s1a.h_spouse_ssn
    printed: "(helper)"
    label: "Does your spouse have a valid social security number (valid for employment and issued by the SSA before the due date of your 2025 return, including extensions)?"
    type: Bool
    expr: {op: input, source: "Interview question: spouse's valid SSN for the enhanced deduction for seniors"}

  - id: s1a.h_spouse_age65
    printed: "(helper)"
    label: "Was your spouse born before January 2, 1961?"
    type: Bool
    expr: {op: input, source: "Interview question: spouse's date of birth"}

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
              - {op: test, eq: [household.taxpayer_work_ssn, {const: true}]}
              - {op: test, eq: [sa.age65, {const: true}]}
              - {op: test, not: {op: test, eq: [s1a.died_before_65, {const: true}]}}
              - {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: s1a.line35
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [household.taxpayer_work_ssn, {const: true}]}
                - {op: test, eq: [sa.age65, {const: true}]}
                - {op: test, not: {op: test, eq: [s1a.died_before_65, {const: true}]}}
                - {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: s1a.h_zero
    note: "Valid SSN is read as an SSN valid for employment issued before the due date (household.taxpayer_work_ssn). The married-must-file-jointly caution excludes married filing separately. s1a.died_before_65 does not say whether it refers to the taxpayer or the spouse, so it is applied to both lines 36a and 36b."

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
              - {op: test, eq: [s1a.h_spouse_ssn, {const: true}]}
              - {op: test, eq: [s1a.h_spouse_age65, {const: true}]}
              - {op: test, not: {op: test, eq: [s1a.died_before_65, {const: true}]}}
          then: s1a.line35
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [f1040.status, {const: "mfj"}]}
                - {op: test, eq: [s1a.h_spouse_ssn, {const: true}]}
                - {op: test, eq: [s1a.h_spouse_age65, {const: true}]}
                - {op: test, not: {op: test, eq: [s1a.died_before_65, {const: true}]}}
          then: s1a.h_zero
    note: "s1a.died_before_65 does not name which person died; it is applied here as well as on line 36a."

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
