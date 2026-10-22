# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f41355c9c83df54d090f76ccf99ffb78e2d71a01c88e34df2880e2c7d325fbb3 |
| subject sha256 | 077c16edad21104b88f065fbd2cf4fbbd3cf53d86ebb73906d8a5a5d89fd0d82 |
| printed lines compared | 16 |
| agree / disagree / missing | 12 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

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
Status: **AGREE**

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: project retained. The difference the earlier ruling on this line settled, now from the other side: for a Simplified Method annuity whose cost has been recovered (worksheet line 7 zero), the second still shows box 1 on line 5a when box 5 is nonzero; the project shows nothing, since the payments are then fully taxable. i1040gi p. 28, Fully Taxable Pensions and Annuities, "you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don't make an entry on line 5a". Box 5 counts only for a plan distribution outside the Simplified Method (stage10.smw.cost_recovered_box5). The rollover and Roth conditions agree.

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Form 8880 line 4 counts the total distribution, excluding amounts not taxable because of a rollover. Chosen reading: box 1 less the amount rolled over (the whole distribution for code G). The other exclusions (excess contributions, returned contributions, plan loans, Roth conversions, in-plan rollovers) are assumed to fall under the retirement.special screen.

Ruling: representation and binding reading; project retained. The project applies the military-plan and section 404(k) exclusions to plan distributions and the inherited exclusion to IRA distributions only; the second applies all three to every entry. An IRA is neither a military retirement plan nor an ESOP, so the first two agree on every entry. For an inherited employer plan the second excludes the distribution; the project counts it, the binding reading amb.2025.savers_inherited_plans (owner decision 4): f8880 p. 2, Line 4, "Distributions from an inherited IRA by a nonspousal beneficiary" names no inherited plan. Box 1 less the amount rolled over (all of it for code G) on both sides (amb.2025.savers_line4_gross).

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

Second transcription's note: Each division is done with multiply_rate by 1/N, so it is rounded half-up to the cent. The IRS text does not say how to round.

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
| retirement.taxable | retirement.h_annuity_rollover, retirement.h_bad_code, retirement.h_roth_8606, retirement.special | retirement.h_annuity_rollover, retirement.h_bad_code, retirement.h_roth_8606 |
| (SMW 9) | retirement.special | retirement.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.line(SMW 1)
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}

  - id: retirement.line(SMW 2)
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
    note: "The Before-you-begin note says to include any death benefit exclusion (up to $5,000) for beneficiaries of employees who died before August 21, 1996. No input covers it. Chosen reading: line 2 is the cost the filer enters, and any such exclusion is assumed to be included in retirement.cost."

  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_360}}

  - id: retirement.h_t1_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1, age 56-60)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_310}}

  - id: retirement.h_t1_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1, age 61-65)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_260}}

  - id: retirement.h_t1_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1, age 66-70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_210}}

  - id: retirement.h_t1_160
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1, age 71 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table1_160}}

  - id: retirement.h_t2_410
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2, combined ages 110 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_410}}

  - id: retirement.h_t2_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2, combined ages 111-120)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_360}}

  - id: retirement.h_t2_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2, combined ages 121-130)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_310}}

  - id: retirement.h_t2_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2, combined ages 131-140)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.line(SMW 2), rate: {param: smw.table2_260}}

  - id: retirement.h_t2_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2, combined ages 141 or older)"
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
    note: "Table 1 has two columns: annuity starting date before November 19, 1996, and after November 18, 1996. No input gives the starting date, and only the after-November-18-1996 numbers are year parameters. A filer who did not complete the worksheet last year must use the Simplified Method only when the starting date is after November 18, 1996. Chosen reading: the after-November-18-1996 column."

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

  - id: retirement.h_line4_new
    printed: "(helper)"
    label: "Line 2 divided by the number on line 3 (Table 2 if the annuity starting date was after 1997 and the payments are for your life and that of your beneficiary; otherwise Table 1)"
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
          then: retirement.h_line4_new
    note: "Each division is done with multiply_rate by 1/N, so it is rounded half-up to the cent. The IRS text does not say how to round."

  - id: retirement.line(SMW 5)
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.line(SMW 4), count: retirement.months}
    note: "The worksheet says that if the annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. No input gives a starting date before 1987. Chosen reading: the starting date is after 1986, so lines 6 and 7 are always completed (line 10 answers No)."

  - id: retirement.line(SMW 6)
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
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
    note: "The retired public safety officer exclusion that this line mentions is not computed. It is assumed to fall under the retirement.special screen."

  - id: retirement.line(SMW 10)
    printed: "(SMW 10)"
    label: "Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.line(SMW 6), retirement.line(SMW 8)]}

  - id: retirement.line(SMW 11)
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.line(SMW 2), take: retirement.line(SMW 10)}

  - id: retirement.h_zero
    printed: "(helper)"
    label: "No amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: retirement.one
    printed: "(helper)"
    label: "One distribution"
    type: Count
    expr: {op: param, ref: sales.one}

  - id: retirement.is_ira
    printed: "(helper)"
    label: "IRA distribution (lines 4a and 4b)"
    type: Bool
    expr: {op: test, ne: [retirement.account, {const: "plan"}]}

  - id: retirement.h_roth
    printed: "(helper)"
    label: "Roth IRA distribution"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.h_direct
    printed: "(helper)"
    label: "Direct rollover (code G)"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}

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

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - {op: test, eq: [retirement.h_direct, {const: true}]}

  - id: retirement.h_not_rolled
    printed: "(helper)"
    label: "Box 1 less the amount rolled over (the part not rolled over)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.h_bad_code
    printed: "(helper)"
    label: "Distribution code the tool does not compute (any other code or two codes, or code Q on a distribution that is not from a Roth IRA)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "other"}]}
        - {op: test, all: [{op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}, {op: test, ne: [retirement.account, {const: "roth_ira"}]}]}
    note: "The text gives no rule for code Q on a plan distribution (designated Roth account), and code Q on a traditional IRA is inconsistent. Chosen reading: both are refused."

  - id: retirement.h_roth_8606
    printed: "(helper)"
    label: "Roth IRA distribution without code Q (Exception 2: see Form 8606 to figure line 4b)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_roth, {const: true}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
    note: "Exception 2 sends a Roth IRA distribution to Form 8606 unless code T (with a Roth contribution for 2020 or earlier) or code Q is shown. Code T is not an enum value, so only code Q is computed (line 4b -0-). Everything else is refused, including Roth-to-Roth rollovers."

  - id: retirement.h_annuity_rollover
    printed: "(helper)"
    label: "A pension or annuity figured by the Simplified Method of which part or all was rolled over"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.is_ira, {const: false}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
    note: "The text does not say how to combine the Simplified Method with a rollover. Chosen reading: refuse."

  - id: retirement.h_cost_left
    printed: "(helper)"
    label: "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)"
    type: Bool
    expr: {op: test, gt: [retirement.line(SMW 7), {const: 0}]}

  - id: retirement.h_annuity_with_cost
    printed: "(helper)"
    label: "The Simplified Method applies and some cost is left to recover"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - {op: test, eq: [retirement.h_cost_left, {const: true}]}

  - id: retirement.h_annuity_taxable
    printed: "(helper)"
    label: "Taxable annuity amount: Simplified Method line 9, or the whole of box 1 when you got your entire cost back tax free before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_cost_left, {const: true}]}
          then: retirement.line(SMW 9)
        - guard: {op: test, eq: [retirement.h_cost_left, {const: false}]}
          then: retirement.box1
    note: "The text says payments are fully taxable if you got your entire cost back tax free before 2025. Chosen reading: no cost left (line 7 zero or less) means fully taxable, which avoids a negative line 8 raising line 9."

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "Taxable IRA amount: the part not rolled over (traditional IRA), or -0- for a Roth IRA distribution with code Q"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_roth, {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.h_roth, {const: false}]}
          then: retirement.h_not_rolled
    note: "Exception 2 (nondeductible traditional IRA contributions, conversions, returned or recharacterized contributions), Exception 3 (QCD) and Exception 4 (HFD) are not computed. They are assumed to fall under the retirement.special screen."

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
    note: "The Rollovers text subtracts box 5 contributions and then the rollover from box 1, without a stated floor. Chosen reading: floor at zero (the text says to enter -0- when nothing remains). The same formula is used for plan distributions that are not Simplified Method annuities. With box 5 and the rollover both zero it equals box 1 (fully taxable)."

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Taxable pension or annuity amount (the Simplified Method for an annuity with after-tax cost; otherwise box 1 less box 5 and any rollover)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.h_annuity_taxable
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
    refuses: [retirement.special, retirement.h_bad_code, retirement.h_roth_8606, retirement.h_annuity_rollover]

  - id: retirement.h_show_a
    printed: "(helper)"
    label: "An exception applies or the distribution is partially taxable, so the total distribution goes on line 4a or 5a"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [retirement.is_ira, {const: true}]}
            - op: test
              any:
                - {op: test, eq: [retirement.has_rollover, {const: true}]}
                - {op: test, eq: [retirement.h_roth, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [retirement.is_ira, {const: false}]}
            - op: test
              any:
                - {op: test, eq: [retirement.has_rollover, {const: true}]}
                - {op: test, eq: [retirement.h_annuity_with_cost, {const: true}]}
                - {op: test, gt: [retirement.box5, {const: 0}]}
    note: "IRA: line 4a is entered under Exception 1 (rollover) or Exception 2 (Roth IRA). Plan: line 5a is entered for a rollover or a partially taxable pension. A positive box 5 is read as making the distribution partially taxable."

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

  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "A distribution Form 8880 line 4 does not count (from a military retirement plan other than the TSP, section 404(k) ESOP dividends, or an inherited IRA received by a nonspousal beneficiary)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.sav_military, {const: true}]}
        - {op: test, eq: [retirement.sav_404k, {const: true}]}
        - {op: test, eq: [retirement.sav_inherited, {const: true}]}

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "This distribution's amount on Form 8880 line 4"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_sav_excluded, {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.h_sav_excluded, {const: false}]}
          then: retirement.h_not_rolled
    note: "Form 8880 line 4 counts the total distribution, excluding amounts not taxable because of a rollover. Chosen reading: box 1 less the amount rolled over (the whole distribution for code G). The other exclusions (excess contributions, returned contributions, plan loans, Roth conversions, in-plan rollovers) are assumed to fall under the retirement.special screen."
```
```
