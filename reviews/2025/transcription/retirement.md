# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2550e4f0bdeca38bb62e6f8e55bc4ba178471e2313a0ddf7fe0e879a8fdcfa71 |
| printed lines compared | 13 |
| agree / disagree / missing | 8 / 5 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}
```

Second:

```json
{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}
```

Ruling: equivalent; project retained. The account kind has three values (traditional_ira, roth_ira, plan), so 'not plan' and 'roth_ira or traditional_ira' are the same test.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: project retained. The second sends every Simplified Method annuity to worksheet line 9; the project first applies the p. 28 rule that payments are fully taxable once 'you got your entire cost back tax free before 2025' (worksheet line 7 not more than zero gives box 1), which keeps line 5b from exceeding box 1 when the recovered amount reaches the cost (the class M finding on classm.retirement.11 of the first run). The IRA and plan branches otherwise agree.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: project changed to the second's reading after this run. For a Simplified Method annuity whose cost has been recovered, the project still showed box 1 on line 5a when box 5 was nonzero; the payments are fully taxable then ('don't make an entry on line 5a', p. 28), so box 5 now counts only for a plan distribution outside the Simplified Method (retirement.show_a), and stage10.smw.cost_recovered_box5 asserts it. The guards otherwise agree.

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

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.taxable | retirement.h_annuity_rollover, retirement.h_bad_code, retirement.special | retirement.h_annuity_rollover, retirement.h_bad_code |
| (SMW 9) | retirement.special | retirement.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.line(SMW 1)
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}

  - id: retirement.line(SMW 2)
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
    note: "The worksheet's 'Before you begin' death benefit exclusion (deaths before August 21, 1996) is not given as a separate input. It is taken to be included in retirement.cost if it applies."

  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_360}}

  - id: retirement.h_t1_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_310}}

  - id: retirement.h_t1_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_260}}

  - id: retirement.h_t1_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_210}}

  - id: retirement.h_t1_160
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_160}}

  - id: retirement.h_t2_410
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_410}}

  - id: retirement.h_t2_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_360}}

  - id: retirement.h_t2_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_310}}

  - id: retirement.h_t2_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_260}}

  - id: retirement.h_t2_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_210}}

  - id: retirement.h_table1
    printed: "(helper)"
    label: "Line 2 divided by the Table 1 number for the age at the annuity starting date"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.age, {const: 55}]}
          then: retirement.h_t1_360
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 55}]}, {op: test, le: [retirement.age, {const: 60}]}]}
          then: retirement.h_t1_310
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 60}]}, {op: test, le: [retirement.age, {const: 65}]}]}
          then: retirement.h_t1_260
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 65}]}, {op: test, le: [retirement.age, {const: 70}]}]}
          then: retirement.h_t1_210
        - guard: {op: test, gt: [retirement.age, {const: 70}]}
          then: retirement.h_t1_160
    note: "Table 1 has two columns, split by an annuity starting date before November 19, 1996 or after November 18, 1996. There is no parameter for the earlier column and no input for the starting date. I used the 'after November 18, 1996' column. Line 3 is only reached for an annuity not on the worksheet last year, and the Simplified Method text requires such an annuity to start after November 18, 1996."

  - id: retirement.h_table2
    printed: "(helper)"
    label: "Line 2 divided by the Table 2 number for the combined ages at the annuity starting date"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.combined_age, {const: 110}]}
          then: retirement.h_t2_410
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 110}]}, {op: test, le: [retirement.combined_age, {const: 120}]}]}
          then: retirement.h_t2_360
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 120}]}, {op: test, le: [retirement.combined_age, {const: 130}]}]}
          then: retirement.h_t2_310
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 130}]}, {op: test, le: [retirement.combined_age, {const: 140}]}]}
          then: retirement.h_t2_260
        - guard: {op: test, gt: [retirement.combined_age, {const: 140}]}
          then: retirement.h_t2_210

  - id: retirement.h_new
    printed: "(helper)"
    label: "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.joint_life, {const: true}]}
          then: retirement.h_table2
        - guard: {op: test, eq: [retirement.joint_life, {const: false}]}
          then: retirement.h_table1

  - id: retirement.line(SMW 4)
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.used_last_year, {const: true}]}
          then: retirement.last_line4
        - guard: {op: test, eq: [retirement.used_last_year, {const: false}]}
          then: retirement.h_new

  - id: retirement.line(SMW 5)
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.line(SMW 4), count: retirement.months}
    note: "Line 5 says that for an annuity starting before 1987 you skip lines 6 and 7 and enter this amount on line 8. There is no input for a pre-1987 starting date, so lines 6 to 8 always follow the post-1986 path. For a pre-1987 annuity, enter zero for retirement.recovered so the result is unchanged unless line 7 would limit it."

  - id: retirement.line(SMW 6)
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}

  - id: retirement.line(SMW 7)
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.line(SMW 2), take: retirement.line(SMW 6)}

  - id: retirement.line(SMW 8)
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: [retirement.line(SMW 5), retirement.line(SMW 7)]}

  - id: retirement.line(SMW 9)
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.line(SMW 1), take: retirement.line(SMW 8)}
    refuses: [retirement.special]
    note: "The retired public safety officer exclusion that line 9 mentions is not computed. It is taken to be covered by the retirement.special screen."

  - id: retirement.one
    printed: "(helper)"
    label: "One distribution"
    type: Count
    expr: {op: param, ref: dependent.one}
    note: "No retirement-specific parameter equal to one is listed, so this uses dependent.one, whose value is 1."

  - id: retirement.h_zero
    printed: "(helper)"
    label: "No amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: retirement.is_ira
    printed: "(helper)"
    label: "IRA distribution (lines 4a and 4b)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.h_is_roth
    printed: "(helper)"
    label: "Roth IRA distribution"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.h_direct
    printed: "(helper)"
    label: "Direct rollover (code G)"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - retirement.h_direct

  - id: retirement.h_rolled
    printed: "(helper)"
    label: "Amount rolled over (the whole distribution for a direct rollover, code G)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_direct, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_direct, {const: false}]}
          then: retirement.rollover

  - id: retirement.h_bad_code
    printed: "(helper)"
    label: "Distribution code or account combination the tool does not compute"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "other"}]}
        - {op: test, all: [retirement.h_is_roth, {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}]}
        - {op: test, all: [{op: test, not: retirement.h_is_roth}, {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}]}
    note: "Exception 2(2) sends a Roth IRA distribution to Form 8606 unless code Q (or code T with an early contribution) applies. Only code Q is computed (zero on line 4b), so any other code on a Roth IRA is refused. Code Q on a non-Roth account is a designated Roth account case that this text does not cover, so it is refused too."

  - id: retirement.h_annuity_rollover
    printed: "(helper)"
    label: "A pension or annuity figured by the Simplified Method of which part or all was rolled over"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "plan"}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - retirement.has_rollover
    note: "The text does not say how a rollover combines with the Simplified Method, so this case is refused."

  - id: retirement.h_ira_not_rolled
    printed: "(helper)"
    label: "Box 1 less the amount rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA distribution, code Q)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_roth, {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.h_is_roth, {const: false}]}
          then: retirement.h_ira_not_rolled
    note: "A traditional IRA is fully taxable except for the amount rolled over (Exception 1). Exception 2 cases that need Form 8606 (nondeductible contributions, conversions, returned or recharacterized contributions), QCDs (Exception 3) and HFDs (Exception 4) are taken to be covered by the retirement.special screen."

  - id: retirement.h_plan_excluded
    printed: "(helper)"
    label: "Taxable contributions (box 5) and the amount rolled over"
    type: NonNegDollars
    expr: {op: sum, of: [retirement.box5, retirement.h_rolled]}

  - id: retirement.h_plan_simple
    printed: "(helper)"
    label: "Box 1 less taxable contributions (box 5) and the amount rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_plan_excluded}
    note: "The Rollovers instruction says to subtract box 5 contributions and then the rollover. For a non-annuity plan distribution with no rollover, the same subtraction of box 5 is used. This was a choice: the text points to Pub. 575 for lump sums."

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Taxable pension or annuity amount (the Simplified Method for an annuity, otherwise box 1 less box 5 and the rollover)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.line(SMW 9)
        - guard: {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_plan_simple

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.is_ira, {const: true}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, eq: [retirement.is_ira, {const: false}]}
          then: retirement.h_plan_taxable
    refuses: [retirement.special, retirement.h_bad_code, retirement.h_annuity_rollover]

  - id: retirement.h_cost_left
    printed: "(helper)"
    label: "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)"
    type: Bool
    expr: {op: test, gt: [retirement.line(SMW 7), {const: 0}]}

  - id: retirement.h_show_a
    printed: "(helper)"
    label: "An exception applies, so the total distribution goes on line 4a or 5a"
    type: Bool
    expr:
      op: test
      any:
        - retirement.has_rollover
        - retirement.h_is_roth
        - {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: true}]}, retirement.h_cost_left]}
        - {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: false}]}, {op: test, gt: [retirement.box5, {const: 0}]}]}
    note: "Line 1 of the worksheet says always to enter box 1 on line 5a. But 'Fully Taxable Pensions and Annuities' says not to make a line 5a entry when there is no cost or the whole cost was recovered before 2025. I read cost as left when line 7 is more than zero."

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Total distribution entered on line 4a or 5a (none when fully taxable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_show_a, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_show_a, {const: false}]}
          then: retirement.h_zero
```
```
