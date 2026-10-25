# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2b4a3748039b2a572901d804ea2fdb3a2b96402e19015afe7135de79c73abd24 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 077c16edad21104b88f065fbd2cf4fbbd3cf53d86ebb73906d8a5a5d89fd0d82 |
| printed lines compared | 16 |
| agree / disagree / missing | 10 / 6 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}
```

Second:

```json
{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}
```

Ruling: representation on the declared retirement_account enumeration; params/2025.yaml permits exactly traditional_ira, roth_ira and plan. Therefore account != plan is exactly (account == traditional_ira OR account == roth_ira). The account question follows f1099r recipient instructions and i1040gi (2025) pp.26-28, which route IRA versus pension/annuity distributions to lines4/5. This is an exhaustive domain identity, not an assertion about unrecognized strings.

### retirement.has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a direct rollov
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}
```

Ruling: open

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"input": "retirement.annuity"}, {"args": [{"const": 0}, {"input": "retirement.cost"}], "test": "lt"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"input": "retirement.cost"}, {"const": 0}], "test": "le"}, {"args": [{"input": "retirement.annuity"}], "test": "not"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "op": "sum"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}}}, {"guard": {"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: open

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"input": "retirement.annuity"}, {"args": [{"const": 0}, {"input": "retirement.cost"}], "test": "lt"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"input": "retirement.cost"}, {"const": 0}], "test": "le"}, {"args": [{"input": "retirement.annuity"}], "test": "not"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "op": "sum"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}}}, {"guard": {"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"input": "retirement.annuity"}, {"args": [{"const": 0}, {"input": "retirement.cost"}], "test": "lt"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"input": "retirement.cost"}, {"const": 0}], "test": "le"}, {"args": [{"input": "retirement.annuity"}], "test": "not"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}], "op": "choose"}}, {"guard": {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "op": "sum"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}}}, {"guard": {"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}, {"input": "retirement.box1"}], "test": "lt"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: open

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"input": "retirement.sav_404k"}], "test": "not"}, {"args": [{"input": "retirement.sav_inherited"}], "test": "not"}, {"args": [{"input": "retirement.sav_military"}], "test": "not"}], "test": "all"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"input": "retirement.sav_404k"}, {"input": "retirement.sav_inherited"}, {"input": "retirement.sav_military"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"of": [{"input": "retirement.box1"}, {"input": "retirement.rollover"}], "op": "smaller_of"}], "test": "lt"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

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

Ruling: representation on nonnegative integer ages; changing age <= n to age < n+1, n < age to n+1 <= age, removing only the nonnegative-domain lower bounds and sorting alternatives makes both canonical trees exactly equal. The proof is .transcription/retirement-age-band-identity.json. Every Table1/Table2 divisor, rate atom, prior-year amount and branch remains unchanged. Source: archived i1040gi (2025) p.29 Simplified Method Worksheet line4 and Tables1/2. Fractional/negative ages are outside the published age question.

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
| retirement.taxable | retirement.bad_code, retirement.roth_bad, retirement.special | retirement.roth_bad |
| retirement.amount_a | retirement.bad_code, retirement.roth_bad, retirement.special | retirement.roth_bad |

## Raw second transcription

```yaml
lines:
  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a."
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date."
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3."
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.used_last_year, {const: true}]}, then: retirement.last_line4}, {guard: {op: test, eq: [retirement.used_last_year, {const: false}]}, then: retirement.smw4_new}]}
  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made."
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet."
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7."
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}
    note: "The IRS text says to skip lines 6 and 7 and enter line 5 on line 8 if the annuity starting date was before 1987; the interface supplies no such date, so this line uses the smaller-of rule for post-1986 annuities."
  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Amount recovered tax free through 2025: add lines 6 and 8. If the annuity starting date was before 1987, stop and do not complete the rest of the worksheet."
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "The IRS text says to STOP if the annuity starting date was before 1987; the interface supplies no such input, so this line computes the 'No' branch (add lines 6 and 8)."
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
  - id: retirement.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: retirement.one
    printed: "(helper)"
    label: "Count of this distribution (one entry)"
    type: Count
    expr: {op: param, ref: person.one}
  - id: retirement.is_ira
    printed: "(helper)"
    label: "Is the account an IRA (traditional or Roth)?"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [retirement.account, {const: "traditional_ira"}]}, {op: test, eq: [retirement.account, {const: "roth_ira"}]}]}
  - id: retirement.roth
    printed: "(helper)"
    label: "Is the account a Roth IRA?"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: retirement.direct
    printed: "(helper)"
    label: "Is the distribution code G (direct rollover)?"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
  - id: retirement.bad_code
    printed: "(helper)"
    label: "Is the distribution code 'other' (unsupported or two codes)?"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}
  - id: retirement.rolled
    printed: "(helper)"
    label: "Amount of this distribution rolled over, not more than the gross distribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.rollover, retirement.box1]}
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Was any amount rolled over?"
    type: Bool
    expr: {op: test, gt: [retirement.rolled, {const: 0}]}
  - id: retirement.roth_q
    printed: "(helper)"
    label: "Is this a qualified Roth distribution (code Q)?"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.account, {const: "roth_ira"}]}, {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}]}
  - id: retirement.roth_fully_rolled
    printed: "(helper)"
    label: "Was the entire Roth distribution rolled over?"
    type: Bool
    expr: {op: test, ge: [retirement.rolled, retirement.box1]}
  - id: retirement.roth_bad
    printed: "(helper)"
    label: "Roth distribution other than a qualified distribution or a full rollover (requires Form 8606)"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.account, {const: "roth_ira"}]}, {op: test, not: retirement.roth_q}, {op: test, not: retirement.roth_fully_rolled}]}
  - id: retirement.cost_left
    printed: "(helper)"
    label: "Is there cost left to recover after 2025?"
    type: Bool
    expr: {op: test, gt: [retirement.smw11, {const: 0}]}
  - id: retirement.annuity_with_cost
    printed: "(helper)"
    label: "Is this a pension or annuity with after-tax cost?"
    type: Bool
    expr: {op: test, all: [retirement.annuity, {op: test, gt: [retirement.cost, {const: 0}]}]}
  - id: retirement.plan_excluded
    printed: "(helper)"
    label: "Plan amount excluded from taxable income before the rollover (box 5 plus rollover)"
    type: NonNegDollars
    expr: {op: sum, of: [retirement.box5, retirement.rolled]}
  - id: retirement.plan_simple
    printed: "(helper)"
    label: "Fully taxable plan amount after excluding box 5 contributions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}
  - id: retirement.annuity_rollover
    printed: "(helper)"
    label: "Taxable amount of a plan distribution with a rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.plan_excluded}
  - id: retirement.annuity_taxable
    printed: "(helper)"
    label: "Taxable amount of a plan distribution without a rollover"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.annuity_with_cost, {const: true}]}, then: retirement.smw9}, {guard: {op: test, eq: [retirement.annuity_with_cost, {const: false}]}, then: retirement.plan_simple}]}
  - id: retirement.plan_taxable
    printed: "(helper)"
    label: "Taxable amount of a plan distribution"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.has_rollover, {const: true}]}, then: retirement.annuity_rollover}, {guard: {op: test, eq: [retirement.has_rollover, {const: false}]}, then: retirement.annuity_taxable}]}
  - id: retirement.ira_not_rolled
    printed: "(helper)"
    label: "Taxable IRA amount after subtracting the rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rolled}
  - id: retirement.ira_taxable
    printed: "(helper)"
    label: "Taxable amount of an IRA distribution"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: retirement.roth_q, then: retirement.zero}, {guard: {op: test, all: [{op: test, not: retirement.roth_q}, {op: test, eq: [retirement.has_rollover, {const: true}]}]}, then: retirement.ira_not_rolled}, {guard: {op: test, all: [{op: test, not: retirement.roth_q}, {op: test, eq: [retirement.has_rollover, {const: false}]}]}, then: retirement.box1}]}
  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount to report on Form 1040 line 4b or 5b"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.is_ira, {const: true}]}, then: retirement.ira_taxable}, {guard: {op: test, eq: [retirement.is_ira, {const: false}]}, then: retirement.plan_taxable}]}
    refuses: [retirement.bad_code, retirement.roth_bad, retirement.special]
  - id: retirement.show_a
    printed: "(helper)"
    label: "Show the gross distribution on Form 1040 line 4a or 5a?"
    type: Bool
    expr: {op: test, lt: [retirement.taxable, retirement.box1]}
  - id: retirement.amount_a
    printed: "(helper)"
    label: "Gross distribution to report on Form 1040 line 4a or 5a"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.show_a, {const: true}]}, then: retirement.box1}, {guard: {op: test, eq: [retirement.show_a, {const: false}]}, then: retirement.zero}]}
    refuses: [retirement.bad_code, retirement.roth_bad, retirement.special]
  - id: retirement.sav_excluded
    printed: "(helper)"
    label: "Is this distribution excluded from Form 8880 line 4?"
    type: Bool
    expr: {op: test, any: [retirement.has_rollover, retirement.direct, retirement.sav_military, retirement.sav_404k, retirement.sav_inherited]}
  - id: retirement.sav_gross
    printed: "(helper)"
    label: "Gross distribution for Form 8880 line 4"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount to include on Form 8880 line 4"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.sav_excluded, {const: true}]}, then: retirement.zero}, {guard: {op: test, eq: [retirement.sav_excluded, {const: false}]}, then: retirement.sav_gross}]}
  - id: retirement.smw4_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
  - id: retirement.smw4_t1_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1, age 56 through 60, after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}
  - id: retirement.smw4_t1_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1, age 61 through 65, after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}
  - id: retirement.smw4_t1_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1, age 66 through 70, after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}
  - id: retirement.smw4_t1_160
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1, age 71 or older, after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}
  - id: retirement.smw4_t2_410
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2, combined ages 110 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}
  - id: retirement.smw4_t2_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2, combined ages 111 through 120)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}
  - id: retirement.smw4_t2_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2, combined ages 121 through 130)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}
  - id: retirement.smw4_t2_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2, combined ages 131 through 140)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}
  - id: retirement.smw4_t2_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2, combined ages 141 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}
  - id: retirement.smw4_table1
    printed: "(helper)"
    label: "Line 4 amount using Table 1 (after November 18, 1996 column)"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, le: [retirement.age, {const: 55}]}, then: retirement.smw4_t1_360}, {guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 55}]}, {op: test, le: [retirement.age, {const: 60}]}]}, then: retirement.smw4_t1_310}, {guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 60}]}, {op: test, le: [retirement.age, {const: 65}]}]}, then: retirement.smw4_t1_260}, {guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 65}]}, {op: test, le: [retirement.age, {const: 70}]}]}, then: retirement.smw4_t1_210}, {guard: {op: test, gt: [retirement.age, {const: 70}]}, then: retirement.smw4_t1_160}]}
    note: "Table 1 also has a column for annuity starting dates before November 19, 1996; no such date is supplied, so this uses the after-November 18, 1996 column."
  - id: retirement.smw4_table2
    printed: "(helper)"
    label: "Line 4 amount using Table 2"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, le: [retirement.combined_age, {const: 110}]}, then: retirement.smw4_t2_410}, {guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 110}]}, {op: test, le: [retirement.combined_age, {const: 120}]}]}, then: retirement.smw4_t2_360}, {guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 120}]}, {op: test, le: [retirement.combined_age, {const: 130}]}]}, then: retirement.smw4_t2_310}, {guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 130}]}, {op: test, le: [retirement.combined_age, {const: 140}]}]}, then: retirement.smw4_t2_260}, {guard: {op: test, gt: [retirement.combined_age, {const: 140}]}, then: retirement.smw4_t2_210}]}
  - id: retirement.smw4_new
    printed: "(helper)"
    label: "Line 4 amount before considering last year's worksheet"
    type: NonNegDollars
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [retirement.joint_life, {const: true}]}, then: retirement.smw4_table2}, {guard: {op: test, eq: [retirement.joint_life, {const: false}]}, then: retirement.smw4_table1}]}
```
