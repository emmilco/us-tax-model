# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b9fad60c2cb486fce6549dd4131a0f61a33a0ff801abe53050600a48f75d6dee |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 4aeee2b0ebf80bf5881542d2adf94337f2f1917d79e85626ad389a8e5dc71551 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d3c8cb85b9a2327c17d713893d6340974bc276217569a5716b9763a5991be7a2 |
| printed lines compared | 26 |
| agree / disagree / missing | 1 / 25 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 12, 23, 34 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 23, 34 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- model changed a published result type

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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,344 of 2,344 agree. Same set (traditional or Roth IRA). Project stands.

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

Ruling: scope; i1040gi p. 30, Rollovers, and p. 27. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,924 of 2,344 agree; 304 project-refuses (none completed), 116 project-unknown (none completed). The two predicates are the same: with code G both are true, and otherwise both read retirement.rollover. Every difference is on a refused or incomplete return: 304 project-refuses (retirement.bad_code 227, retirement.special 77) and 116 project-unknown (partial records withholding account, special or code). The project-refuses are its cited retirement.bad_code, retirement.special, retirement.annuity_rollover and retirement.screen_refused gates on refused returns, and the project-unknown are partial records withholding a screen the project asks first (account, special, code, code_screen or early_screen): scope. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Second transcription's note: Computed as the Simplified Method line 9 amount when retirement.annuity is true, and otherwise as gross distribution less the effective rollover, with qualified-Roth and direct-rollover overrides.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a." i1040gi p. 29, line 11. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,080 of 2,344 agree; 138 project-refuses (none completed), 70 candidate-unknown (13 completed), 48 project-unknown (none completed), 8 value (1 completed). (1) The reply takes worksheet line 7 signed with no branch for a recovered cost. All 8 value differences have recovered above cost; the completed one is generated 395 r2 (box 1 $0.00, cost $25,183.00, recovered $47,921.41: project $0.00, candidate $22,738.41), and the other 7 are on refused or incomplete returns. (2) It reads retirement.annuity and box 5 on every entry, IRAs included, and the rollover on qualified Roth (code Q) entries. The interview does not ask those there, and p. 27 takes no box 5 for an IRA. Of the 13 completed candidate-unknown, 8 need annuity on traditional IRA entries (classm.tcw.5 r2, classm.tcw.8 r2, classm.tcw.10, classm.tcw.16 r1, classm.f8962.2 r2, stage21.t067.smw_hidden_ira, and partials of generated 15 and 80), 3 need the rollover on Roth IRA code Q entries (classm.tcw.8 r1, classm.tcw.16 r2, partial of classm.f8962.3.deepseek), and 2 need box 5 on IRA entries (partials of generated 15 and 80). The project-refuses are its cited retirement.bad_code, retirement.special, retirement.annuity_rollover and retirement.screen_refused gates on refused returns, and the project-unknown are partial records withholding a screen the project asks first (account, special, code, code_screen or early_screen): scope. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"input": "retirement.box1"}
```

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 672 of 2,344 agree; 976 value (114 completed), 358 project-refuses (none completed), 306 project-unknown (none completed), 32 candidate-unknown (none completed). The reply copies box 1 to line 4a/5a on every entry. Every value difference (976; 114 on completed returns, each checked) is a fully taxable entry: the project makes no entry ($0.00) and the candidate shows box 1. These are 70 non-annuity plan code 7 entries, 41 traditional IRA entries of codes 1, 2, 4, 7 and S, 1 code 2 plan entry and 1 annuity whose cost was recovered, e.g. classm.s2.3.deepseek r1 ($92.00), classm.f8962.3.deepseek r2 ($18,556.00), classm.ira.2 r2 and classm.tcw.5 r1 and r2. The 32 candidate-unknown are on refused or incomplete returns. The project-refuses are its cited retirement.bad_code, retirement.special, retirement.annuity_rollover and retirement.screen_refused gates on refused returns, and the project-unknown are partial records withholding a screen the project asks first (account, special, code, code_screen or early_screen): scope. Project stands.

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

Ruling: model error and scope; f8880 p. 2, Line 4: "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions) from any of the following types of plans. ... Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,000 of 2,344 agree; 217 project-refuses (none completed), 70 candidate-unknown (9 completed), 53 project-unknown (none completed), 4 candidate-refuses (none completed). No value differs. The reply tests sav_404k, sav_military and sav_inherited on every entry; the project asks the first two only for plan entries and sav_inherited only for IRA entries. The 9 completed candidate-unknown are partial records withholding them where they are not asked (classm.f8962.3.deepseek r1 and r2, classm.f8962.1.gpt, generated 15 r2, 80 r1 and 101 r1). The candidate-refuses are retirement.special on refused returns. The project-refuses are its cited retirement.bad_code, retirement.special, retirement.annuity_rollover and retirement.screen_refused gates on refused returns, and the project-unknown are partial records withholding a screen the project asks first (account, special, code, code_screen or early_screen): scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: ambiguity, model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,337 of 2,344 agree; 613 candidate-unknown (25 completed), 202 value (6 completed), 190 candidate-refuses (none completed), 2 project-refuses (none completed). The reply now puts codes 2, 3 and 4 on line 1 and the same amount on line 2, so line 3 and the additional tax are unchanged. That is the second reading of amb.2025.f5329_line1_codes (chosen: the first, line 1 holds only code 1 and S; reason: "The tax is the same either way"; owner's decision D8(a)), which this reply extends to codes 3 and 4, whose exceptions the code also shows (i5329 p. 1, Who Must File, which requires the form only where box 7 doesn't indicate the exception). The 6 completed values are generated 22 r1 (traditional IRA, code 4: $0.00 against $18,218.60), 175 r1 (plan, code 2: $0.00 against $52,095.29), 314 r2 (plan annuity, code 4: $0.00 against $46,209.90), 348 r1 (IRA, code 2: $0.00 against $4,784.11), 381 r1 (IRA, code 4: $0.00 against $42,337.61) and 421 r1 (plan annuity, code 4: $0.00 against $29,413.54). The other 196 (codes 2 and 4) are on refused returns. Separately, the reply declares early_screen and code_screen as refusals of every entry and reads annuity on IRAs (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). Of the 25 completed candidate-unknown, 22 need early_screen on entries of other codes (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 are code_screen partials (classm.f8962.3.deepseek, classm.f8962.1.gpt) and 1 needs annuity on an IRA (stage21.t067.smw_hidden_ira): model error. The candidate-refuses (retirement.special 77, h_roth_unsupported 111, early_screen 2) are all on refused or incomplete returns, and the project-refuses are its cited bad_code and annuity_rollover: scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: ambiguity, model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,282 of 2,344 agree; 659 candidate-unknown (31 completed), 202 value (6 completed), 200 candidate-refuses (none completed), 1 project-refuses (none completed). The reply now puts codes 2, 3 and 4 on line 1 and the same amount on line 2, so line 3 and the additional tax are unchanged. That is the second reading of amb.2025.f5329_line1_codes (chosen: the first, line 1 holds only code 1 and S; reason: "The tax is the same either way"; owner's decision D8(a)), which this reply extends to codes 3 and 4, whose exceptions the code also shows (i5329 p. 1, Who Must File, which requires the form only where box 7 doesn't indicate the exception). The 6 completed values (line 2, equal to line 1 of the same entries) are generated 22 r1 (traditional IRA, code 4: $0.00 against $18,218.60), 175 r1 (plan, code 2: $0.00 against $52,095.29), 314 r2 (plan annuity, code 4: $0.00 against $46,209.90), 348 r1 (IRA, code 2: $0.00 against $4,784.11), 381 r1 (IRA, code 4: $0.00 against $42,337.61) and 421 r1 (plan annuity, code 4: $0.00 against $29,413.54). The other 196 (codes 2 and 4) are on refused returns. The 31 completed candidate-unknown are 22 early_screen, 2 code_screen and 7 exception answers on entries the exception is not asked of (partials of classm.f8962.3.deepseek r1 and r2, classm.f8962.1.gpt, generated 15 r1 and r2, 80 r1 and 101 r1) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): model error. The candidate-refuses are on refused or incomplete returns, and the project-refuses is its cited retirement.wrong_kind: scope. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." i5329 p. 5, exceptions table. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,515 of 2,344 agree; 629 candidate-unknown (31 completed), 200 candidate-refuses (none completed). No value differs. The reply needs early_screen, code_screen and the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The 31 completed candidate-unknown are 22 early_screen (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 code_screen partials and 7 exception partials (classm.f8962.3.deepseek, classm.f8962.1.gpt, generated 15, 80 and 101). The candidate-refuses (retirement.special, h_roth_unsupported, early_screen) are on refused or incomplete returns: scope. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." i5329 p. 5, exceptions table. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,515 of 2,344 agree; 629 candidate-unknown (31 completed), 200 candidate-refuses (none completed). No value differs. The reply needs early_screen, code_screen and the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The 31 completed candidate-unknown are 22 early_screen (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 code_screen partials and 7 exception partials (classm.f8962.3.deepseek, classm.f8962.1.gpt, generated 15, 80 and 101). The candidate-refuses (retirement.special, h_roth_unsupported, early_screen) are on refused or incomplete returns: scope. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." i5329 p. 5, exceptions table. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,517 of 2,344 agree; 627 candidate-unknown (31 completed), 200 candidate-refuses (none completed). No value differs. The reply needs early_screen, code_screen and the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The 31 completed candidate-unknown are 22 early_screen (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 code_screen partials and 7 exception partials (classm.f8962.3.deepseek, classm.f8962.1.gpt, generated 15, 80 and 101). The candidate-refuses (retirement.special, h_roth_unsupported, early_screen) are on refused or incomplete returns: scope. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." i5329 p. 5, exceptions table. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,513 of 2,344 agree; 631 candidate-unknown (31 completed), 200 candidate-refuses (none completed). No value differs. The reply needs early_screen, code_screen and the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The 31 completed candidate-unknown are 22 early_screen (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 code_screen partials and 7 exception partials (classm.f8962.3.deepseek, classm.f8962.1.gpt, generated 15, 80 and 101). The candidate-refuses (retirement.special, h_roth_unsupported, early_screen) are on refused or incomplete returns: scope. Project stands.

### retirement.is_e23 — Exception 23
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}
```

Ruling: model error; p590b p. 28, Emergency personal expense distributions; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,792 of 2,344 agree; 550 candidate-unknown (22 completed), 2 project-unknown (none completed). No value differs. The reply tests retirement.exception = e23 on every entry, so the 22 completed candidate-unknown need the exception answer on entries it is not asked of (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2 r1 and r2, classm.tcw.5 r1 and r2, classm.tcw.7, classm.tcw.8 and others; project false). The 2 project-unknown are partials on incomplete returns. Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." i5329 p. 5, exceptions table. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,515 of 2,344 agree; 629 candidate-unknown (31 completed), 200 candidate-refuses (none completed). No value differs. The reply needs early_screen, code_screen and the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The 31 completed candidate-unknown are 22 early_screen (classm.aqee.1.deepseek, classm.f5695.7, classm.ira.2, classm.tcw.5, classm.tcw.7, classm.tcw.8 and others), 2 code_screen partials and 7 exception partials (classm.f8962.3.deepseek, classm.f8962.1.gpt, generated 15, 80 and 101). The candidate-refuses (retirement.special, h_roth_unsupported, early_screen) are on refused or incomplete returns: scope. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 4; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,539 of 2,344 agree; 604 candidate-unknown (24 completed), 200 candidate-refuses (none completed), 1 project-refuses (none completed). No value differs (on code S entries the reply's share is the project's). The 24 completed candidate-unknown are 22 early_screen on other codes and 2 code_screen partials (classm.f8962.3.deepseek, classm.f8962.1.gpt) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused or incomplete returns, and the project-refuses is its cited bad_code: scope. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i5329 p. 5, Line 4; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,539 of 2,344 agree; 605 candidate-unknown (24 completed), 200 candidate-refuses (none completed). No value differs (on code S entries the reply's share is the project's). The 24 completed candidate-unknown are 22 early_screen on other codes and 2 code_screen partials (classm.f8962.3.deepseek, classm.f8962.1.gpt) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused or incomplete returns: scope. Project stands.

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.box1"}}
```

Second:

```json
{"shown_when": null, "value": {"input": "retirement.box1"}}
```

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 474 of 2,344 agree; 1,777 candidate-shows-skipped (224 completed), 58 candidate-unknown (3 completed), 35 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 224 completed candidate-shows-skipped (99 non-annuity plan entries, 79 traditional IRA, 45 Roth IRA, 1 annuity with its cost recovered: generated 395 r2) and 3 completed candidate-unknown (Roth IRA entries, box 1 unasked). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. Project stands.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.cost"}}
```

Second:

```json
{"shown_when": null, "value": {"input": "retirement.cost"}}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,542 of 2,344 agree; 684 candidate-unknown (19 completed), 77 candidate-refuses (none completed), 22 candidate-shows-skipped (1 completed), 19 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 19 completed candidate-unknown on cost (8 non-annuity plan, 8 traditional IRA, 3 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 56, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 61, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 66, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 71, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 111, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 121, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 131, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 141, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}
```

Second transcription's note: Line 3 is not supplied as a separate line. The Table 1 or Table 2 factor is selected using retirement.age or retirement.combined_age and retirement.joint_life, with the after-November-18-1996 Table 1 column described by retirement.annuity.

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,482 of 2,344 agree; 745 candidate-unknown (32 completed), 77 candidate-refuses (none completed), 21 project-unknown (none completed), 19 candidate-shows-skipped (1 completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 32 completed candidate-unknown (16 non-annuity plan, 12 traditional IRA, 4 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). The Table 1 and Table 2 bands are the project's. No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"amount": {"line": "(SMW 4)"}, "count": {"input": "retirement.months"}, "op": "multiply_count"}}
```

Second:

```json
{"shown_when": null, "value": {"amount": {"line": "(SMW 4)"}, "count": {"input": "retirement.months"}, "op": "multiply_count"}}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,452 of 2,344 agree; 776 candidate-unknown (39 completed), 77 candidate-refuses (none completed), 21 project-unknown (none completed), 18 candidate-shows-skipped (1 completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 39 completed candidate-unknown (20 non-annuity plan, 14 traditional IRA, 5 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.recovered"}}
```

Second:

```json
{"shown_when": null, "value": {"input": "retirement.recovered"}}
```

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,625 of 2,344 agree; 658 candidate-unknown (19 completed), 42 candidate-shows-skipped (1 completed), 19 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 19 completed candidate-unknown on recovered (8 non-annuity plan, 8 traditional IRA, 3 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. Project stands.

### (SMW 7) — Subtract line 6 from line 2
Status: **DISAGREE**

Project:

```json
{"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 6)"}}
```

Second:

```json
{"from": {"line": "(SMW 2)"}, "op": "subtract_floor0", "take": {"line": "(SMW 6)"}}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,521 of 2,344 agree; 714 candidate-unknown (26 completed), 77 candidate-refuses (none completed), 20 candidate-shows-skipped (1 completed), 12 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 26 completed candidate-unknown (12 non-annuity plan, 10 traditional IRA, 4 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "(SMW 5)"}, {"line": "(SMW 7)"}], "op": "smaller_of"}
```

Second:

```json
{"expression": {"of": [{"line": "(SMW 5)"}, {"from": {"line": "(SMW 2)"}, "op": "subtract_floor0", "take": {"line": "(SMW 6)"}}], "op": "smaller_of"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,417 of 2,344 agree; 822 candidate-unknown (50 completed), 77 candidate-refuses (none completed), 16 candidate-shows-skipped (1 completed), 12 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 50 completed candidate-unknown (26 non-annuity plan, 17 traditional IRA, 7 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **DISAGREE**

Project:

```json
{"from": {"line": "(SMW 1)"}, "op": "subtract_floor0", "take": {"line": "(SMW 8)"}}
```

Second:

```json
{"expression": {"from": {"line": "(SMW 1)"}, "op": "subtract_floor0", "take": {"line": "(SMW 8)"}}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 452 of 2,344 agree; 950 candidate-shows-skipped (184 completed), 853 candidate-unknown (51 completed), 77 candidate-refuses (none completed), 12 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 184 completed candidate-shows-skipped (79 non-annuity plan, 63 traditional IRA, 40 Roth IRA, 2 annuities with the cost recovered) and 51 completed candidate-unknown (26 non-annuity plan, 17 traditional IRA, 8 Roth IRA). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "(SMW 6)"}, {"line": "(SMW 8)"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "(SMW 6)"}, {"line": "(SMW 8)"}], "op": "sum"}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Second transcription's note: The pre-1987 STOP branch is not represented because the supplied interface has no annuity-starting-date-before-1987 input; this line computes the 'No' branch by adding lines 6 and 8.

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,415 of 2,344 agree; 822 candidate-unknown (50 completed), 77 candidate-refuses (none completed), 18 candidate-shows-skipped (1 completed), 12 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 50 completed candidate-unknown (26 non-annuity plan, 17 traditional IRA, 7 Roth IRA) and 1 completed candidate-shows-skipped (generated 395 r2). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **DISAGREE**

Project:

```json
{"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 10)"}}
```

Second:

```json
{"expression": {"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 10)"}}, "invalid_model_types": [{"line": "retirement.smw8", "message": "model changed a published result type"}]}
```

Ruling: model error and scope; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 1,066 partial records from 40 bases; 2,344 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,433 of 2,344 agree; 822 candidate-unknown (50 completed), 77 candidate-refuses (none completed), 12 project-unknown (none completed). The comparison has included each line's shown_when since the hardening round (commit a75729f), and this is the first retirement review since then. The project hides the (SMW n) lines unless retirement.smw_shown holds (a plan entry, annuity true, worksheet line 7 above zero); the reply declares no shown_when. The value expression is the project's. Every difference is on an entry the project hides; the uncapped witnesses were rebuilt and read one by one: 50 completed candidate-unknown (26 non-annuity plan, 17 traditional IRA, 7 Roth IRA). No witness has smw_shown true, so no shown value differs. A line the source never reaches must not show an amount (README), so the reply is in error; the needed answers (cost, recovered, used_last_year, age and the like) are asked only when the worksheet is used. The 77 candidate-refuses (retirement.special, which the reply declares on the worksheet) are on refused or incomplete returns where the project hides the line: scope. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.taxable | retirement.special | - |
| retirement.sav_amount | retirement.special | - |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.special | retirement.code_screen, retirement.early_screen |

## Raw second transcription

```yaml
lines:
  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3"
    type: NonNegDollars
    note: "Line 3 is not supplied as a separate line. The Table 1 or Table 2 factor is selected using retirement.age or retirement.combined_age and retirement.joint_life, with the after-November-18-1996 Table 1 column described by retirement.annuity."
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.smw4_t2_410
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}
          then: retirement.smw4_t2_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}
          then: retirement.smw4_t2_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.smw4_t2_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.smw4_t2_210
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.smw4_t1_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 55, type: Count}]}
              - {op: test, le: [retirement.age, {const: 60, type: Count}]}
          then: retirement.smw4_t1_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 60, type: Count}]}
              - {op: test, le: [retirement.age, {const: 65, type: Count}]}
          then: retirement.smw4_t1_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 65, type: Count}]}
              - {op: test, le: [retirement.age, {const: 70, type: Count}]}
          then: retirement.smw4_t1_210
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 70, type: Count}]}
          then: retirement.smw4_t1_160
  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made. If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
  - id: retirement.smw7_nn
    printed: "(helper)"
    label: "Line 7 nonnegative amount (helper)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw2, take: retirement.smw6}
  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: copy, from: retirement.smw7_nn}
  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7_nn]}
  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b. If your Form 1099-R shows a larger amount, use the amount on this line instead of the amount from Form 1099-R. If you are a retired public safety officer, see Insurance Premiums for Retired Public Safety Officers before entering an amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet. No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025. You will need this number if you need to fill out this worksheet next year"
    type: Dollars
    note: "The pre-1987 STOP branch is not represented because the supplied interface has no annuity-starting-date-before-1987 input; this line computes the 'No' branch by adding lines 6 and 8."
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year. The payments you receive next year will generally be fully taxable"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}

  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero amount (helper)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: retirement.one
    printed: "(helper)"
    label: "Count of this Form 1099-R entry (helper)"
    type: Count
    expr: {op: param, ref: ss.one}
  - id: retirement.is_ira
    printed: "(helper)"
    label: "Whether this distribution is from an IRA (helper)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: retirement.h_rollover_effective
    printed: "(helper)"
    label: "Rollover amount effective for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.rollover
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Whether this distribution includes a rollover (helper)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
  - id: retirement.taxable_ira_gross
    printed: "(helper)"
    label: "IRA gross taxable amount before qualified-Roth override (helper)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rollover_effective}
  - id: retirement.taxable_ira
    printed: "(helper)"
    label: "Taxable amount from an IRA distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.h_zero
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.taxable_ira_gross
  - id: retirement.taxable_plan_plain
    printed: "(helper)"
    label: "Fully taxable plan distribution amount (helper)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rollover_effective}
  - id: retirement.taxable_plan_annuity
    printed: "(helper)"
    label: "Plan distribution taxable amount with or without the Simplified Method (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw9
        - guard: {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.taxable_plan_plain
  - id: retirement.taxable_plan_nonG
    printed: "(helper)"
    label: "Plan distribution taxable amount before direct-rollover override (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.h_zero
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.taxable_plan_annuity
  - id: retirement.taxable_plan
    printed: "(helper)"
    label: "Taxable amount from a pension, annuity or plan distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_zero
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.taxable_plan_nonG
  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (helper)"
    type: NonNegDollars
    refuses: [retirement.special]
    note: "Computed as the Simplified Method line 9 amount when retirement.annuity is true, and otherwise as gross distribution less the effective rollover, with qualified-Roth and direct-rollover overrides."
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.is_ira, {const: true}]}
          then: retirement.taxable_ira
        - guard: {op: test, eq: [retirement.is_ira, {const: false}]}
          then: retirement.taxable_plan
  - id: retirement.amount_a
    printed: "(helper)"
    label: "Gross distribution amount for Form 1040 line 4a or 5a (helper)"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.sav_gross
    printed: "(helper)"
    label: "Distribution amount before Form 8880 exclusions (helper)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rollover_effective}
  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Distribution amount counted for Form 8880 line 4 (helper)"
    type: NonNegDollars
    refuses: [retirement.special]
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [retirement.sav_military, {const: true}]}
              - {op: test, eq: [retirement.sav_404k, {const: true}]}
              - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.sav_military, {const: true}]}
                - {op: test, eq: [retirement.sav_404k, {const: true}]}
                - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.sav_gross
  - id: retirement.l1
    printed: "(helper)"
    label: "Early distribution amount includible in income for Form 5329 line 1 (helper)"
    type: NonNegDollars
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen]
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [retirement.code, {const: "early_1"}]}
              - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
              - {op: test, eq: [retirement.code, {const: "simple_S"}]}
              - {op: test, eq: [retirement.code, {const: "disability_3"}]}
              - {op: test, eq: [retirement.code, {const: "death_4"}]}
          then: retirement.taxable
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.code, {const: "early_1"}]}
                - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
                - {op: test, eq: [retirement.code, {const: "simple_S"}]}
                - {op: test, eq: [retirement.code, {const: "disability_3"}]}
                - {op: test, eq: [retirement.code, {const: "death_4"}]}
          then: retirement.h_zero
  - id: retirement.l2_exc
    printed: "(helper)"
    label: "Exception amount before applying the none case (helper)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.l1, retirement.exc_amount]}
  - id: retirement.l2
    printed: "(helper)"
    label: "Exception amount for Form 5329 line 2 (helper)"
    type: NonNegDollars
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen]
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "none"}]}
          then: retirement.h_zero
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "none"}]}
          then: retirement.l2_exc
  - id: retirement.l1_s
    printed: "(helper)"
    label: "SIMPLE IRA early distribution amount for Form 5329 line 1 (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
  - id: retirement.l2_s
    printed: "(helper)"
    label: "SIMPLE IRA exception amount for Form 5329 line 2 (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Exception 05 amount for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero
  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Exception 09 amount for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero
  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Exception 19 amount for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero
  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Exception 22 amount for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero
  - id: retirement.is_e23
    printed: "(helper)"
    label: "Whether exception 23 applies to this distribution (helper)"
    type: Bool
    expr: {op: test, eq: [retirement.exception, {const: "e23"}]}
  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Exception 23 amount for this distribution (helper)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.l2
        - guard:
            op: test
            not: {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.h_zero

  - id: retirement.smw4_t1_360
    printed: "(helper)"
    label: "Line 4 using Table 1 factor 1/360 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
  - id: retirement.smw4_t1_310
    printed: "(helper)"
    label: "Line 4 using Table 1 factor 1/310 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}
  - id: retirement.smw4_t1_260
    printed: "(helper)"
    label: "Line 4 using Table 1 factor 1/260 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}
  - id: retirement.smw4_t1_210
    printed: "(helper)"
    label: "Line 4 using Table 1 factor 1/210 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}
  - id: retirement.smw4_t1_160
    printed: "(helper)"
    label: "Line 4 using Table 1 factor 1/160 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}
  - id: retirement.smw4_t2_410
    printed: "(helper)"
    label: "Line 4 using Table 2 factor 1/410 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}
  - id: retirement.smw4_t2_360
    printed: "(helper)"
    label: "Line 4 using Table 2 factor 1/360 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}
  - id: retirement.smw4_t2_310
    printed: "(helper)"
    label: "Line 4 using Table 2 factor 1/310 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}
  - id: retirement.smw4_t2_260
    printed: "(helper)"
    label: "Line 4 using Table 2 factor 1/260 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}
  - id: retirement.smw4_t2_210
    printed: "(helper)"
    label: "Line 4 using Table 2 factor 1/210 (helper)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}
```
