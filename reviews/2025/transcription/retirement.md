# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cddd23c6c05e4c358056e5bd35bebf55e9015dbd23ec62cbd84ed67fb2242453 |
| subject sha256 | 749c206d7dded76f8927dfff5e415400bb2a0822c820d5a882a0571aaec1ef7a |
| printed lines compared | 15 |
| agree / disagree / missing | 11 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### retirement.one — One distribution
Status: **AGREE**

### retirement.is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

### retirement.has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a direct rollov
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}
```

Ruling: equivalent; project retained. The amount rolled over is box 1 for code G and the rollover input otherwise; with code G tested first on both sides, 'code G or rolled amount above zero' and 'code G or rollover above zero' agree on every input.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}
```

Second transcription's note: Roth IRA: only code Q is computed. Exception 2(2)(b) says enter -0- on line 4b. Other Roth cases are refused through retirement.h_unsupported. Exception 2 items for traditional IRAs (nondeductible contributions, conversions, returned or recharacterized contributions), QCDs and HFDs are assumed to fall under the retirement.special screen.

Ruling: equivalent; project retained. For a plan distribution outside the Simplified Method the project subtracts box 5 and the rollover together, floored at zero; the second subtracts box 5, floors at zero, then subtracts the rollover and floors again. With non-negative amounts the two are equal: when box 5 is at least box 1 both give zero, and otherwise both give box 1 less box 5 less the rollover, floored at zero. The other branches agree.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: equivalent; project retained. The project's rollover amount is box 1 under code G and the rollover input otherwise, and every guard pairs it with 'code is not G' (or adds 'code is G'), so it reduces to the second's rollover input. The project's plan condition, (A and B) or not-a-plan, where A is 'box 5 is zero or this is a worksheet annuity' and B is 'worksheet line 7 is zero or less, or this is not a worksheet annuity', equals the second's (A or not-a-plan) and (B or not-a-plan) by distribution; the Roth condition is the same.

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 56}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": 56}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 61}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 66}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 71}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 111}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": 111}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 121}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 131}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 141}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 60}], "test": "le"}, {"args": [{"const": 55}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 65}], "test": "le"}, {"args": [{"const": 60}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 70}], "test": "le"}, {"args": [{"const": 65}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"input": "retirement.age"}, {"const": 55}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"const": 70}, {"input": "retirement.age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 120}], "test": "le"}, {"args": [{"const": 110}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 130}], "test": "le"}, {"args": [{"const": 120}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 140}], "test": "le"}, {"args": [{"const": 130}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"input": "retirement.combined_age"}, {"const": 110}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"const": 140}, {"input": "retirement.combined_age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second transcription's note: Open: how to round the division. Chosen: line 2 times the rate 1/N, rounded half-up to the cent as multiply_rate does.

Ruling: equivalent; project retained. Ages are whole numbers, so the bands '56 to 60' written as 55 < age <= 60 and as 56 <= age < 61 are the same; Table 2 likewise.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

### (SMW 7) — Subtract line 6 from line 2
Status: **AGREE**

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **AGREE**

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **AGREE**

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.taxable | retirement.h_unsupported, retirement.special | retirement.h_unsupported |
| retirement.amount_a | retirement.h_unsupported, retirement.special | retirement.h_unsupported |

## Raw second transcription

```yaml
```yaml
lines:
  - id: "retirement.line(SMW 1)"
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: "retirement.box1"}

  - id: "retirement.line(SMW 2)"
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: "retirement.cost"}
    note: "Open: the Before-you-begin note says to include any death benefit exclusion (up to $5,000) for a beneficiary of an employee who died before August 21, 1996. There is no separate input for it. Chosen: the filer includes it in retirement.cost."

  - id: "retirement.h_t1_360"
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table1_360}}

  - id: "retirement.h_t1_310"
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1, age 56-60)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table1_310}}

  - id: "retirement.h_t1_260"
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1, age 61-65)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table1_260}}

  - id: "retirement.h_t1_210"
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1, age 66-70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table1_210}}

  - id: "retirement.h_t1_160"
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1, age 71 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table1_160}}

  - id: "retirement.h_t2_410"
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2, combined ages 110 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table2_410}}

  - id: "retirement.h_t2_360"
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2, combined ages 111-120)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table2_360}}

  - id: "retirement.h_t2_310"
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2, combined ages 121-130)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table2_310}}

  - id: "retirement.h_t2_260"
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2, combined ages 131-140)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table2_260}}

  - id: "retirement.h_t2_210"
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2, combined ages 141 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: "retirement.line(SMW 2)", rate: {param: smw.table2_210}}

  - id: "retirement.h_table1"
    printed: "(helper)"
    label: "Line 2 divided by the Table 1 number for the age at the annuity starting date"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: ["retirement.age", {const: 55}]}
          then: "retirement.h_t1_360"
        - guard: {op: test, all: [{op: test, gt: ["retirement.age", {const: 55}]}, {op: test, le: ["retirement.age", {const: 60}]}]}
          then: "retirement.h_t1_310"
        - guard: {op: test, all: [{op: test, gt: ["retirement.age", {const: 60}]}, {op: test, le: ["retirement.age", {const: 65}]}]}
          then: "retirement.h_t1_260"
        - guard: {op: test, all: [{op: test, gt: ["retirement.age", {const: 65}]}, {op: test, le: ["retirement.age", {const: 70}]}]}
          then: "retirement.h_t1_210"
        - guard: {op: test, gt: ["retirement.age", {const: 70}]}
          then: "retirement.h_t1_160"
    note: "Open: Table 1 has a column for annuity starting dates before November 19, 1996 (300/260/240/170/120). There is no input for the starting date and no year parameter for that column. Chosen: only the after-November-18-1996 column is encoded. A filer with an earlier starting date would normally have last year's line 4 (retirement.used_last_year)."

  - id: "retirement.h_table2"
    printed: "(helper)"
    label: "Line 2 divided by the Table 2 number for the combined ages at the annuity starting date"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: ["retirement.combined_age", {const: 110}]}
          then: "retirement.h_t2_410"
        - guard: {op: test, all: [{op: test, gt: ["retirement.combined_age", {const: 110}]}, {op: test, le: ["retirement.combined_age", {const: 120}]}]}
          then: "retirement.h_t2_360"
        - guard: {op: test, all: [{op: test, gt: ["retirement.combined_age", {const: 120}]}, {op: test, le: ["retirement.combined_age", {const: 130}]}]}
          then: "retirement.h_t2_310"
        - guard: {op: test, all: [{op: test, gt: ["retirement.combined_age", {const: 130}]}, {op: test, le: ["retirement.combined_age", {const: 140}]}]}
          then: "retirement.h_t2_260"
        - guard: {op: test, gt: ["retirement.combined_age", {const: 140}]}
          then: "retirement.h_t2_210"

  - id: "retirement.h_line4_new"
    printed: "(helper)"
    label: "Line 2 divided by the number on line 3 (Table 2 if the annuity starting date was after 1997 and the payments are for your life and that of your beneficiary; otherwise Table 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.joint_life", {const: true}]}
          then: "retirement.h_table2"
        - guard: {op: test, eq: ["retirement.joint_life", {const: false}]}
          then: "retirement.h_table1"

  - id: "retirement.line(SMW 4)"
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.used_last_year", {const: true}]}
          then: "retirement.last_line4"
        - guard: {op: test, eq: ["retirement.used_last_year", {const: false}]}
          then: "retirement.h_line4_new"
    note: "Open: how to round the division. Chosen: line 2 times the rate 1/N, rounded half-up to the cent as multiply_rate does."

  - id: "retirement.line(SMW 5)"
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: "retirement.line(SMW 4)", count: "retirement.months"}

  - id: "retirement.line(SMW 6)"
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: "retirement.recovered"}

  - id: "retirement.line(SMW 7)"
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: "retirement.line(SMW 2)", take: "retirement.line(SMW 6)"}

  - id: "retirement.line(SMW 8)"
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: ["retirement.line(SMW 5)", "retirement.line(SMW 7)"]}
    note: "Open: line 5 says that if the annuity starting date was before 1987, skip lines 6 and 7 and enter line 5 on line 8. There is no input for a pre-1987 starting date. Chosen: lines 6 and 7 are always used."

  - id: "retirement.line(SMW 9)"
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: "retirement.line(SMW 1)", take: "retirement.line(SMW 8)"}

  - id: "retirement.line(SMW 10)"
    printed: "(SMW 10)"
    label: "Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: ["retirement.line(SMW 6)", "retirement.line(SMW 8)"]}

  - id: "retirement.line(SMW 11)"
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: "retirement.line(SMW 2)", take: "retirement.line(SMW 10)"}

  - id: "retirement.one"
    printed: "(helper)"
    label: "One distribution"
    type: Count
    expr: {op: param, ref: person.one}
    note: "No retirement-specific parameter for 1 exists. Chosen: person.one (value 1)."

  - id: "retirement.h_zero"
    printed: "(helper)"
    label: "No amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: "retirement.is_ira"
    printed: "(helper)"
    label: "IRA distribution (lines 4a and 4b)"
    type: Bool
    expr: {op: test, ne: ["retirement.account", {const: "plan"}]}

  - id: "retirement.has_rollover"
    printed: "(helper)"
    label: "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: ["retirement.rollover", {const: 0}]}
        - {op: test, eq: ["retirement.code", {const: "direct_rollover_G"}]}

  - id: "retirement.h_unsupported"
    printed: "(helper)"
    label: "Distribution this tool does not compute: an unsupported box 7 code; code Q other than from a Roth IRA; a Roth IRA distribution without code Q (Form 8606); or a Simplified Method annuity that was rolled over"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: ["retirement.code", {const: "other"}]}
        - {op: test, all: [{op: test, eq: ["retirement.code", {const: "qualified_roth_Q"}]}, {op: test, ne: ["retirement.account", {const: "roth_ira"}]}]}
        - {op: test, all: [{op: test, eq: ["retirement.account", {const: "roth_ira"}]}, {op: test, ne: ["retirement.code", {const: "qualified_roth_Q"}]}]}
        - {op: test, all: [{op: test, eq: ["retirement.account", {const: "plan"}]}, {op: test, eq: ["retirement.annuity", {const: true}]}, {op: test, eq: ["retirement.has_rollover", {const: true}]}]}
    note: "Exception 2(2) sends a Roth IRA distribution to Form 8606 unless code Q (or code T with a pre-2021 contribution, which the code enum cannot express) applies. The text given covers code Q only for a Roth IRA, so code Q from a plan is refused. Rolling over Simplified Method periodic payments is not addressed by the text, so it is refused."

  - id: "retirement.h_rolled"
    printed: "(helper)"
    label: "Amount rolled over (the whole distribution for a direct rollover, code G)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.code", {const: "direct_rollover_G"}]}
          then: "retirement.box1"
        - guard: {op: test, ne: ["retirement.code", {const: "direct_rollover_G"}]}
          then: "retirement.rollover"

  - id: "retirement.h_ira_not_rolled"
    printed: "(helper)"
    label: "Traditional IRA: the part not rolled over (box 1 less the amount rolled over); -0- if the total was rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: "retirement.box1", take: "retirement.h_rolled"}

  - id: "retirement.h_plan_less_box5"
    printed: "(helper)"
    label: "Box 1 less contributions (box 5) that were taxable to you when made"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: "retirement.box1", take: "retirement.box5"}

  - id: "retirement.h_plan_simple"
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover. Enter the remaining amount on line 5b (-0- if zero)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: "retirement.h_plan_less_box5", take: "retirement.h_rolled"}
    note: "Open: the Rollovers text gives box 1 less box 5 less the rollover. The text does not separately cover a nonperiodic distribution with box 5 and no rollover (General Rule, Pub. 575). Chosen: the same subtraction for every pension that is not a Simplified Method annuity, floored at zero."

  - id: "retirement.h_cost_left"
    printed: "(helper)"
    label: "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)"
    type: Bool
    expr: {op: test, gt: ["retirement.line(SMW 7)", {const: 0}]}

  - id: "retirement.h_annuity_taxable"
    printed: "(helper)"
    label: "Taxable annuity amount: Simplified Method line 9, or the whole of box 1 when the entire cost was recovered tax free before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.h_cost_left", {const: true}]}
          then: "retirement.line(SMW 9)"
        - guard: {op: test, eq: ["retirement.h_cost_left", {const: false}]}
          then: "retirement.box1"
    note: "The fully taxable rule covers a filer who 'got your entire cost back tax free before 2025'. Chosen: when line 7 is zero or less, the whole of box 1 is taxable. This also keeps a negative line 7 from pushing line 9 above box 1."

  - id: "retirement.h_plan_taxable"
    printed: "(helper)"
    label: "Taxable pension or annuity amount (Simplified Method for a periodic annuity with cost, otherwise box 1 less box 5 and the rollover)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.annuity", {const: true}]}
          then: "retirement.h_annuity_taxable"
        - guard: {op: test, eq: ["retirement.annuity", {const: false}]}
          then: "retirement.h_plan_simple"

  - id: "retirement.taxable"
    printed: "(helper)"
    label: "Taxable amount of this distribution (line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.account", {const: "roth_ira"}]}
          then: "retirement.h_zero"
        - guard: {op: test, eq: ["retirement.account", {const: "traditional_ira"}]}
          then: "retirement.h_ira_not_rolled"
        - guard: {op: test, eq: ["retirement.account", {const: "plan"}]}
          then: "retirement.h_plan_taxable"
    refuses: ["retirement.special", "retirement.h_unsupported"]
    note: "Roth IRA: only code Q is computed. Exception 2(2)(b) says enter -0- on line 4b. Other Roth cases are refused through retirement.h_unsupported. Exception 2 items for traditional IRAs (nondeductible contributions, conversions, returned or recharacterized contributions), QCDs and HFDs are assumed to fall under the retirement.special screen."

  - id: "retirement.h_show_a"
    printed: "(helper)"
    label: "An exception applies or the payments are partially taxable, so the total distribution goes on line 4a or 5a"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: ["retirement.has_rollover", {const: true}]}
        - {op: test, eq: ["retirement.account", {const: "roth_ira"}]}
        - {op: test, all: [{op: test, eq: ["retirement.account", {const: "plan"}]}, {op: test, eq: ["retirement.annuity", {const: true}]}, {op: test, eq: ["retirement.h_cost_left", {const: true}]}]}
        - {op: test, all: [{op: test, eq: ["retirement.account", {const: "plan"}]}, {op: test, eq: ["retirement.annuity", {const: false}]}, {op: test, gt: ["retirement.box5", {const: 0}]}]}
    note: "Line 4a: Exception 1 (rollover) and Exception 2 (Roth IRA) put the total on line 4a. Otherwise a fully taxable IRA distribution goes only on line 4b. Line 5a: a rollover, a Simplified Method annuity with cost left, or a distribution reduced by box 5 is partially taxable, so the total goes on line 5a. A fully taxable pension goes only on line 5b."

  - id: "retirement.amount_a"
    printed: "(helper)"
    label: "Total distribution entered on line 4a or 5a (none when fully taxable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.h_show_a", {const: true}]}
          then: "retirement.box1"
        - guard: {op: test, eq: ["retirement.h_show_a", {const: false}]}
          then: "retirement.h_zero"
    refuses: ["retirement.special", "retirement.h_unsupported"]
```
```
