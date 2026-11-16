# Review record 3ab49bcfd1e7 — transcription dependent

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "dependent",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "partial-input policy": "source-partial-inputs-v1",
  "prompt policy": "source-only-computation-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "495ae4c3e32d77960ea1242b6af54c674794f5c0379b9afd5d09c20071d26ab3",
 "response_sha256": "6084dab30feb618ce9c551c92830aba2e56cb2eccc1931209f57a4dd23c3a752",
 "scope": "whole",
 "subjects": {
  "2(c)": "16a9974d0484c6192b40db7f99420dd98f450a5849f5949156b0be7362e0655d",
  "2(d)": "fe641f5d9ab66f9418076d13c058fe04f3eaf2561490a3c7920ce0039098186e",
  "27": "eb7869abb2461eec1ffc1a62fb80a425bc51ac320585100abae06448e86cf82c",
  "28": "4059e38fd231416383906352e8fe1ffd7378ea07126c663d91f17c46aee951ca",
  "29": "132eb8b412d2cb39221b4617d30a99fa722fc48dc179d5f02a3843c1a40e9742",
  "30": "ab366392af855359c16c4354d3727ba31c3d20a4fa2670bb24bbce4dec8a79bd",
  "31": "03a9c95eb3e72e597e3bbb67acb94ab715449d20f5e0228645d88b47aa30e09d",
  "dependent.actc_amount": "75827a3c80fddf6f929aba2fd1f995d6ad72acfd6e03f0547e135b47f88bce96",
  "dependent.claimed": "3fdd3a99f5539553112890270689f705225930bf250f65f26803b16468dd86b8",
  "dependent.ctc_amount": "9aa79f6af499104284e5f90476522a7fdc96ea219af6f8e17ff92e3c562abb63",
  "dependent.ctc_child": "4c27a6255c0d31ff716fd0abf6efee2eafb65ebf6cb930e6dbdde0f343df7338",
  "dependent.dc_count": "6e8b475ab185eebd8f897a7b2cceeb2d4e5cd73e196df35ea0733c70f0d819bd",
  "dependent.dc_lived_half": "a036957b722b993a839671d90e9862f346f80b9e77cc96aae9de42ded1e7ca54",
  "dependent.dc_qp": "9e08cf9c9e202c94cf473801e86b32fa362a71c80dde658672d595c1909a5633",
  "dependent.eic_child": "cbc8d4ca266384d8494eddf5ba5c666041f80e718781a5aaf2cd87b7b649404d",
  "dependent.eic_ssn_child": "354f858a488b4e4281890aafc258b74046c72529eeb13d3abe3f6d8e8994899e",
  "dependent.hoh_absence": "90d1d8c9d2f08a8c89e7eafa06d3cf98c151f13d0320ec25618eca30308b8f49",
  "dependent.hoh_test1": "e6dc07b3b40b1c58f3ad54a2651fd405dbf2f9da4eb15bd7b89e4465854c6c01",
  "dependent.hoh_test2": "11950e6e347de2a04a7735654527e6c8a3eb3e9d07ab6709c10bc75277653ca2",
  "dependent.hoh_test2_lived": "9e3f4fdb1b72f90a3e06067126c6a0edc7260aee69cdc166cf4f6448a8d4a724",
  "dependent.odc_amount": "67c05a515b419c132c4668a4560381e029c2832e658a738679e0755882f7e3e5",
  "dependent.odc_person": "aeb8f2021a818dfd7743d83e5542e939c6241132f5882858d4cafd563862dc16",
  "dependent.one": "858660bbf031f30a7be0943c8d565dfd22a05dfea0dff850664c1d7d444819a0",
  "dependent.ptc_magi_counted": "9f06226881817f73216216288d40f94c92b9ea3130724d256d946a9778481bb8"
 }
}
```

<!-- part head -->
# Transcription agreement — dependent

Second transcription of `Dependents — qualifying child and qualifying relative tests, per person listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/dependent.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 495ae4c3e32d77960ea1242b6af54c674794f5c0379b9afd5d09c20071d26ab3 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | c4166f3cbc8c0f599dfd82acfb807a8cecf25abc6c73dab4dcdab61971b44b93 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| partial-input policy | source-partial-inputs-v1 |
| partial-input bank sha256 | 7d044bad0abec95b5ad7515730d486e46a880abc0c22e6ac291d10c91ae68af1 |
| partial-input request context | included |
| partial-input result | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 5bceb793098cafa1df712bf299ab8850dac4d0fd0e93a0abee7e45df34afebed |
| printed lines compared | 24 |
| agree / disagree / missing | 1 / 23 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 15, 17, 18, 19, 20, 21, 22 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 15, 17, 18, 19, 20, 21, 22 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 6, 7, 8, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 6, 7, 8, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 2, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 2, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8962 | 2025 | 8 | cited pages | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 8 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| i8863 | 2025 | 1, 2, 3, 4, 5, 8, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 5, 8, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw_next_year, f1095a, f5329, f8606, g28, ira, refund, rental, retirement, royalty, rprop, s2, s3, sc, sche, scope, scveh, sd, sdtw, u1250 |
| named line | f1116, f1116col, f4137, f4137row, f8919, f8960, ftc, rec, w2 |
| shared page | dcprov, eic, f1040, f2441, f8863, f8962, household, otjob, person, s1, s8812, sa, sales |
| worksheet | sli |

## Source-based partial-input checks

A fixed interpreter evaluates validated declarative IR on synthetic facts; no model-generated code or commands run. These checks earn no numeric evidence credit.

| case | target | expected | observed | result |
| --- | --- | --- | --- | --- |
| P01 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P01 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P02 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P02 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P03 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P03 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P04 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P04 | dependent[sample].dc_line2c | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P05 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P05 | dependent[sample].dc_line2c | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P06 | dependent[sample].dc_qp | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P06 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P07 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P07 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P08 | dependent[sample].dc_qp | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P08 | dependent[sample].dc_line2c | {"kind": "bool", "value": false} | {"kind": "bool", "value": false} | MATCH |
| P09 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P09 | dependent[sample].dc_line2c | {"input": "dependent[sample].dc_over12_care", "kind": "unknown"} | {"input": "dependent[sample].dc_over12_care", "kind": "unknown", "reason": "no input supplied for dependent[sample].dc_over12_care"} | MATCH |
| P10 | dependent[sample].dc_qp | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |
| P10 | dependent[sample].dc_line2c | {"kind": "bool", "value": true} | {"kind": "bool", "value": true} | MATCH |

<!-- part section dependent.dc_lived_half -->
dependent.dc_lived_half — Lived with you more than half of 2025, or, for a person other than a qualifying child born
Status: **DISAGREE**

Project:

```json
{"$shared": "4aae835f34adedb2"}
```

Second:

```json
{"$shared": "46b66a31fd3a3891"}
```

Ruling: open

<!-- part section dependent.one -->
dependent.one — One person listed
Status: **AGREE**

<!-- part section dependent.claimed -->
dependent.claimed — Your dependent
Status: **DISAGREE**

Project:

```json
{"$shared": "6ecfc66c418695cc"}
```

Second:

```json
{"$shared": "17c073aa76ed8007"}
```

Ruling: open

<!-- part section dependent.ctc_child -->
dependent.ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **DISAGREE**

Project:

```json
{"$shared": "13c2c289fa5d65ba"}
```

Second:

```json
{"$shared": "00a9f0bfde6657ef"}
```

Second transcription's note: The filer SSN condition (you, or one spouse on a joint return, with an SSN valid for employment and the other with an SSN or ITIN) is read from household.ctc_ssn.

Ruling: open

<!-- part section dependent.odc_person -->
dependent.odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **DISAGREE**

Project:

```json
{"$shared": "fc7596b76eb6578b"}
```

Second:

```json
{"$shared": "d84abbef9543cefb"}
```

Second transcription's note: Open: Step 5 question 1 also accepts an ITIN applied for by the due date; the filer test is read from household.all_tin as published.

Ruling: open

<!-- part section dependent.ctc_amount -->
dependent.ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "c4cf55482c46be6c"}, {"guard": {"$shared": "079efa16382b8700"}, "then": {"param": "ctc.per_child"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "00a9f0bfde6657ef"}, "then": {"param": "ctc.per_child"}}, {"$shared": "bdca88e8ec20834e"}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.odc_amount -->
dependent.odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"$shared": "fc7596b76eb6578b"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"$shared": "fc7596b76eb6578b"}], "test": "eq"}, "then": {"param": "odc.per_dependent"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "d84abbef9543cefb"}, "then": {"param": "odc.per_dependent"}}, {"guard": {"args": [{"$shared": "00a9f0bfde6657ef"}, {"$shared": "dfe58c4e8e47a8d5"}, {"$shared": "4e94f318a5bfe546"}, {"$shared": "eccaa1db5f6a2443"}, {"$shared": "712d85b2e84d6696"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.actc_amount -->
dependent.actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "c4cf55482c46be6c"}, {"guard": {"$shared": "079efa16382b8700"}, "then": {"param": "actc.per_child"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "00a9f0bfde6657ef"}, "then": {"param": "actc.per_child"}}, {"$shared": "bdca88e8ec20834e"}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.hoh_test2_lived -->
dependent.hoh_test2_lived — A Test 2 person who lived with you more than half the year, or of the part of the year a r
Status: **DISAGREE**

Project:

```json
{"$shared": "b72d1660b2ed1520"}
```

Second:

```json
{"$shared": "2f7093f7d73aee4e"}
```

Ruling: open

<!-- part section dependent.hoh_absence -->
dependent.hoh_absence — A Test 2 person only by counting an absence head of household does not count
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"$shared": "496a1e5bc5a2855e"}, {"$shared": "9b04e8f56ed52305"}, {"$shared": "fb503e6d1d9918ed"}, {"args": {"$shared": "f6f3ee391e049e06"}, "test": "ne"}, {"args": {"$shared": "eff46eef862d78bf"}, "test": "ne"}], "test": "any"}, {"args": [{"args": {"$shared": "ccde53ef36d17372"}, "test": "ne"}, {"$shared": "726b909b48f9c541"}, {"args": {"$shared": "6377ef03fa616477"}, "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "household.no"}}, {"guard": {"$shared": "b72d1660b2ed1520"}, "then": {"input": "dependent.absence_no_return"}}], "op": "choose"}
```

Second:

```json
{"args": [{"$shared": "5ce161e067bbeb7f"}, {"$shared": "2f7093f7d73aee4e"}, {"args": [{"const": true}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}
```

Ruling: open

<!-- part section dependent.hoh_test2 -->
dependent.hoh_test2 — A Test 2 person who lived with you more than half the year, or of the part of the year a r
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "b72d1660b2ed1520"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"$shared": "5ce161e067bbeb7f"}, {"$shared": "2f7093f7d73aee4e"}], "test": "all"}
```

Ruling: open

<!-- part section dependent.hoh_test1 -->
dependent.hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "cae21fd21ef95261"}, {"$shared": "65bcf55411127020"}, {"$shared": "0e836bee5ee949c8"}], "test": "all"}
```

Second:

```json
{"args": [{"$shared": "17c073aa76ed8007"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "65bcf55411127020"}], "test": "all"}
```

Ruling: open

<!-- part section dependent.eic_child -->
dependent.eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **DISAGREE**

Project:

```json
{"$shared": "4b25f00b24d0225a"}
```

Second:

```json
{"$shared": "e8f93269f6d04e24"}
```

Ruling: open

<!-- part section dependent.eic_ssn_child -->
dependent.eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"$shared": "4b25f00b24d0225a"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, "then": {"input": "dependent.eic_ssn"}}, {"$shared": "31ff7178cc6ae312"}], "op": "choose"}}, {"guard": {"args": {"$shared": "7fa7f809880d82f8"}, "test": "ne"}, "then": {"param": "household.no"}}], "op": "choose"}
```

Second:

```json
{"args": [{"$shared": "e8f93269f6d04e24"}, {"args": [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "any"}], "test": "all"}
```

Ruling: open

<!-- part section dependent.dc_qp -->
dependent.dc_qp — A qualifying person for Form 2441 (you have care expenses, and this person is your depende
Status: **DISAGREE**

Project:

```json
{"$shared": "44f668c74751fcb2"}
```

Second:

```json
{"$shared": "0570779a7b59949e"}
```

Ruling: open

<!-- part section dependent.dc_count -->
dependent.dc_count — One, for every entry (counted as a qualifying person only where dependent.dc_qp holds)
Status: **DISAGREE**

Project:

```json
{"const": 1, "type": "Count"}
```

Second:

```json
{"cap": 1, "op": "percent_floor", "part": {"alternatives": [{"$shared": "c8cb73b986218afe"}, {"guard": {"$shared": "0570779a7b59949e"}, "then": {"const": 1}}], "op": "choose"}, "whole": {"const": 100}}
```

Ruling: open

<!-- part section dependent.ptc_magi_counted -->
dependent.ptc_magi_counted — This dependent's modified AGI counted in household income (zero unless required to file be
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "dependent.ptc_files"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "dependent.ptc_files"}], "test": "eq"}, "then": {"input": "dependent.ptc_magi"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "17c073aa76ed8007"}, {"args": [{"const": true}, {"input": "dependent.ptc_files"}], "test": "eq"}], "test": "all"}, "then": {"input": "dependent.ptc_magi"}}, {"guard": {"args": [{"$shared": "eccaa1db5f6a2443"}, {"args": [{"const": true}, {"input": "dependent.ptc_files"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

<!-- part section 2(d) -->
2(d) — Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
Status: **DISAGREE**

Project:

```json
{"input": "dependent.dc_paid"}
```

Second:

```json
{"alternatives": [{"$shared": "c8cb73b986218afe"}, {"guard": {"$shared": "0570779a7b59949e"}, "then": {"input": "dependent.dc_paid"}}], "op": "choose"}
```

Ruling: open

<!-- part section 2(c) -->
2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "44f668c74751fcb2"}, {"args": [{"args": [{"$shared": "49ba61210109901e"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}], "test": "all"}, {"args": [{"param": "dc.child_age"}, {"input": "dependent.age"}], "test": "lt"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"$shared": "0570779a7b59949e"}, {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "dependent.dc_under13"}], "test": "eq"}, {"$shared": "49ba61210109901e"}], "test": "any"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}], "test": "all"}, {"args": [{"param": "dc.child_age"}, {"input": "dependent.age"}], "test": "lt"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}], "test": "all"}
```

Ruling: open

<!-- part section 27 -->
27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "d1808d87c502bc72"}, {"guard": {"$shared": "21147f40fd2ff75a"}, "then": {"$shared": "9d5c34fcba6bddb8"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "3562882b0fd49dab"}, "then": {"of": [{"from": {"$shared": "e2187f51feaa0c68"}, "op": "subtract_floor0", "take": {"$shared": "60a124017e8fbd31"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"$shared": "80564d9f7b2b8617"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Expenses and adjustments are aggregated across academic periods; a period whose adjustments exceed its expenses is refused.

Ruling: open

<!-- part section 28 -->
28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "d1808d87c502bc72"}, {"guard": {"$shared": "21147f40fd2ff75a"}, "then": {"$shared": "cd2c266b576ff107"}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "27"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}
```

Ruling: open

<!-- part section 29 -->
29 — Multiply line 28 by 25% (0.25)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "d1808d87c502bc72"}, {"guard": {"$shared": "21147f40fd2ff75a"}, "then": {"$shared": "3672e84b32d30cca"}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "28"}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}
```

Ruling: open

<!-- part section 30 -->
30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "d1808d87c502bc72"}, {"guard": {"$shared": "21147f40fd2ff75a"}, "then": {"alternatives": [{"guard": {"args": {"$shared": "9c62a754eda4ada1"}, "test": "eq"}, "then": {"$shared": "9d5c34fcba6bddb8"}}, {"guard": {"args": {"$shared": "9c62a754eda4ada1"}, "test": "ne"}, "then": {"of": [{"$shared": "3672e84b32d30cca"}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"line": "28"}, {"const": 0}], "test": "le"}, "then": {"line": "27"}}, {"guard": {"args": [{"const": 0}, {"line": "28"}], "test": "lt"}, "then": {"of": [{"line": "29"}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}
```

Ruling: open

<!-- part section 31 -->
31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "0a77e89c3998d821"}, {"$shared": "e22a9e36be873a00"}], "test": "all"}, "then": {"from": {"input": "dependent.edu_inst"}, "op": "subtract_floor0", "take": {"$shared": "2787d74fabba21e1"}}}, {"guard": {"args": [{"args": {"$shared": "3b3674044e632b92"}, "test": "ne"}, {"args": {"$shared": "7c20e4ec7290e322"}, "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "7de8c1119481c95f"}, {"$shared": "80564d9f7b2b8617"}], "test": "all"}, "then": {"from": {"input": "dependent.edu_inst"}, "op": "subtract_floor0", "take": {"$shared": "60a124017e8fbd31"}}}, {"guard": {"args": [{"$shared": "3562882b0fd49dab"}, {"$shared": "643c616e134e2878"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

<!-- part gate dependent.claimed -->
| dependent.claimed | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.ctc_child -->
| dependent.ctc_child | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate dependent.odc_person -->
| dependent.odc_person | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.ctc_amount -->
| dependent.ctc_amount | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate dependent.odc_amount -->
| dependent.odc_amount | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.actc_amount -->
| dependent.actc_amount | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate dependent.hoh_absence -->
| dependent.hoh_absence | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.hoh_test2 -->
| dependent.hoh_test2 | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.hoh_test1 -->
| dependent.hoh_test1 | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.eic_child -->
| dependent.eic_child | dependent.divorced_rule, dependent.married | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.eic_ssn_child -->
| dependent.eic_ssn_child | dependent.divorced_rule, dependent.married | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.dc_qp -->
| dependent.dc_qp | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate dependent.dc_count -->
| dependent.dc_count | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate dependent.ptc_magi_counted -->
| dependent.ptc_magi_counted | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate 2(d) -->
| 2(d) | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married, dependent.multiple_support |
<!-- part gate 2(c) -->
| 2(c) | dependent.divorced_rule, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.married |
<!-- part gate 27 -->
| 27 | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married |
<!-- part gate 28 -->
| 28 | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married |
<!-- part gate 29 -->
| 29 | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married |
<!-- part gate 30 -->
| 30 | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married |
<!-- part gate 31 -->
| 31 | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_refuse, dependent.married |
<!-- part raw -->

## Raw second transcription

```yaml
```yaml
lines:
  - id: dependent.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: dependent.h_cent
    printed: "(helper)"
    label: "One cent (counting unit)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}
  - id: dependent.h_rel_qc
    printed: "(helper)"
    label: "Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.relationship, {const: "child"}]}
        - {op: test, eq: [dependent.relationship, {const: "sibling"}]}
        - {op: test, eq: [dependent.relationship, {const: "sibling_descendant"}]}
  - id: dependent.h_age_ok
    printed: "(helper)"
    label: "Under age 19 and younger than you (or your spouse if filing jointly); or under age 24, a full-time student, and younger; or any age and permanently and totally disabled"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, lt: [dependent.age, {param: qc.age_limit}]}
            - {op: test, eq: [dependent.younger, {const: true}]}
        - op: test
          all:
            - {op: test, lt: [dependent.age, {param: qc.student_age_limit}]}
            - {op: test, eq: [dependent.student, {const: true}]}
            - {op: test, eq: [dependent.younger, {const: true}]}
        - {op: test, eq: [dependent.disabled, {const: true}]}
  - id: dependent.h_lived_half_qc
    printed: "(helper)"
    label: "Who lived with you for more than half of 2025"
    type: Bool
    expr: {op: test, ge: [dependent.months, {const: 7, type: Count}]}
    note: "Open: the kidnapped-child residency treatment (Pub. 501) is not computed; dependent.kidnapped is not read. The months answer is used as given."
  - id: dependent.h_own_over_half
    printed: "(helper)"
    label: "Provided over half of their own support for 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.own_money, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [dependent.self_support_view, {const: "over_half"}]}
            - op: test
              all:
                - {op: test, eq: [dependent.self_support_view, {const: "unsure"}]}
                - {op: test, eq: [dependent.self_support, {const: true}]}
  - id: dependent.h_qc_tests
    printed: "(helper)"
    label: "Meets the conditions to be your qualifying child (relationship, age, support, joint return, residency)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_rel_qc, {const: true}]}
        - {op: test, eq: [dependent.h_age_ok, {const: true}]}
        - {op: test, eq: [dependent.h_own_over_half, {const: false}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
        - {op: test, eq: [dependent.h_lived_half_qc, {const: true}]}
  - id: dependent.h_qc_mine
    printed: "(helper)"
    label: "Not a qualifying child of another person who takes priority (qualifying child of more than one person)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.other_claimant, {const: false}]}
        - {op: test, eq: [dependent.other_nontaxpayer, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [dependent.other_only_spouse, {const: true}]}
            - op: test
              any:
                - {op: test, eq: [f1040.status, {const: "mfj"}]}
                - {op: test, eq: [dependent.spouse_claims, {const: false}]}
        - op: test
          all:
            - {op: test, eq: [dependent.other_only_spouse, {const: false}]}
            - {op: test, eq: [dependent.filer_parent, {const: true}]}
    note: "Open: the tiebreaker rules depend on AGI comparisons and on who claims, which no input supplies. Chosen reading: you keep the child if no other taxpayer qualifies, if the only other claimant is your spouse on a joint return or a spouse who will not claim, or if you are the child's parent (parent priority, or agreement with the other parent). A non-parent filer facing another taxpayer claimant is treated as not having this qualifying child."
  - id: dependent.h_qc
    printed: "(helper)"
    label: "Your qualifying child"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_tests, {const: true}]}
        - {op: test, eq: [dependent.h_qc_mine, {const: true}]}
  - id: dependent.h_qr_direct
    printed: "(helper)"
    label: "A relative who doesn't have to live with you (including, on a joint return, a relative of your spouse)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.relationship, {const: "child"}]}
        - {op: test, eq: [dependent.relationship, {const: "sibling"}]}
        - {op: test, eq: [dependent.relationship, {const: "parent"}]}
        - {op: test, eq: [dependent.relationship, {const: "parent_relative"}]}
        - {op: test, eq: [dependent.relationship, {const: "in_law"}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [dependent.spouse_relative, {const: true}]}
  - id: dependent.h_qr_member
    printed: "(helper)"
    label: "Member of household or relationship test"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_qr_direct, {const: true}]}
        - {op: test, eq: [dependent.relationship, {const: "household_member"}]}
        - op: test
          all:
            - {op: test, eq: [dependent.qr_all_year, {const: true}]}
            - {op: test, eq: [dependent.lawful, {const: true}]}
  - id: dependent.h_not_qc_any
    printed: "(helper)"
    label: "Who wasn't a qualifying child of any taxpayer for 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_tests, {const: false}]}
        - op: test
          any:
            - {op: test, eq: [dependent.other_claimant, {const: false}]}
            - {op: test, eq: [dependent.other_nontaxpayer, {const: true}]}
  - id: dependent.h_supported
    printed: "(helper)"
    label: "For whom you provided over half of the person's support in 2025"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.supported_view, {const: "over_half"}]}
        - op: test
          all:
            - {op: test, eq: [dependent.supported_view, {const: "unsure"}]}
            - {op: test, eq: [dependent.supported, {const: true}]}
  - id: dependent.h_qr_nogi
    printed: "(helper)"
    label: "Qualifying relative tests other than gross income"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qr_member, {const: true}]}
        - {op: test, eq: [dependent.h_not_qc_any, {const: true}]}
        - {op: test, eq: [dependent.h_supported, {const: true}]}
  - id: dependent.h_qr
    printed: "(helper)"
    label: "Your qualifying relative (gross income less than $5,200)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qr_nogi, {const: true}]}
        - {op: test, lt: [dependent.gross_income, {param: qr.gross_income_limit}]}
    note: "The sheltered-workshop exclusion for a permanently and totally disabled person is not computed; gross income is used as entered."
  - id: dependent.h_cit
    printed: "(helper)"
    label: "U.S. citizen, U.S. national, or U.S. resident alien"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.citizen, {const: true}]}
  - id: dependent.h_cit_cm
    printed: "(helper)"
    label: "U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_cit, {const: true}]}
        - {op: test, eq: [dependent.canada_mexico, {const: true}]}
  - id: dependent.h_tin
    printed: "(helper)"
    label: "Has an SSN, ITIN, or ATIN issued (or applied for) by the due date"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.tin, {const: true}]}
  - id: dependent.h_work
    printed: "(helper)"
    label: "Has an SSN valid for employment issued before the due date"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.work_ssn, {const: true}]}
  - id: dependent.h_eicssn
    printed: "(helper)"
    label: "Has an SSN valid for the EIC"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.eic_ssn, {const: true}]}
  - id: dependent.h_dep_base
    printed: "(helper)"
    label: "Qualifying child or qualifying relative meeting the citizen test"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, eq: [dependent.h_qc, {const: true}]}
            - {op: test, eq: [dependent.h_qr, {const: true}]}
        - {op: test, eq: [dependent.h_cit_cm, {const: true}]}
  - id: dependent.h_dep_wouldbe
    printed: "(helper)"
    label: "Would be your dependent except for gross income of $5,200 or more, a joint return, or your being claimable by another"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, eq: [dependent.h_qc, {const: true}]}
            - {op: test, eq: [dependent.h_qr_nogi, {const: true}]}
        - {op: test, eq: [dependent.h_cit_cm, {const: true}]}
  - id: dependent.h_dc_qp_child
    printed: "(helper)"
    label: "A qualifying child under age 13 whom you can claim as a dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.h_qc, {const: true}]}
        - op: test
          any:
            - {op: test, lt: [dependent.age, {param: dc.child_age}]}
            - op: test
              all:
                - {op: test, eq: [dependent.age, {param: dc.child_age}]}
                - {op: test, eq: [dependent.dc_under13, {const: true}]}
  - id: dependent.h_dc_qp_incapable
    printed: "(helper)"
    label: "A person not able to care for themselves who lived with you more than half the year and is or would be your dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.dc_incapable, {const: true}]}
        - {op: test, eq: [dependent.dc_lived_half, {const: true}]}
        - {op: test, eq: [dependent.h_dep_wouldbe, {const: true}]}
  - id: dependent.h_dc_over12
    printed: "(helper)"
    label: "Over age 12 at the time the care was provided"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [dependent.age, {param: dc.child_age}]}
        - op: test
          all:
            - {op: test, eq: [dependent.age, {param: dc.child_age}]}
            - op: test
              any:
                - {op: test, eq: [dependent.dc_under13, {const: false}]}
                - {op: test, eq: [dependent.dc_over12_care, {const: true}]}
  - id: dependent.h_dc_flag
    printed: "(helper)"
    label: "One cent when this person is a qualifying person, else zero"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.dc_qp, {const: true}]}, then: dependent.h_cent}
        - {guard: {op: test, not: {op: test, eq: [dependent.dc_qp, {const: true}]}}, then: dependent.h_zero}
  - id: dependent.h_hoh_who
    printed: "(helper)"
    label: "A person who can qualify you under Test 2 for head of household"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [dependent.claimed, {const: true}]}
            - op: test
              any:
                - {op: test, eq: [dependent.h_qc, {const: true}]}
                - {op: test, eq: [dependent.h_qr_direct, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [dependent.h_qc, {const: true}]}
            - {op: test, eq: [dependent.claimed, {const: false}]}
    note: "Excludes a dependent only because the person lived with you all year; the divorced-parent, multiple-support and married-child cases are refused on dependent.claimed."
  - id: dependent.h_edu_ws1
    printed: "(helper)"
    label: "AQEE Worksheet line 1 (American opportunity credit): total qualified education expenses"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_inst, dependent.edu_mat]}
  - id: dependent.h_edu_adj
    printed: "(helper)"
    label: "AQEE Worksheet line 3: total adjustments (lines 2a, 2b, 2c)"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_a_this_year, dependent.edu_a_next_year, dependent.edu_refunds]}
  - id: dependent.h_edu_ws4_aoc
    printed: "(helper)"
    label: "AQEE Worksheet line 4 (American opportunity credit). If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.h_edu_ws1, take: dependent.h_edu_adj}
  - id: dependent.h_edu_ws4_llc
    printed: "(helper)"
    label: "AQEE Worksheet line 4 (lifetime learning credit; course materials only if paid to the institution). If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.edu_inst, take: dependent.h_edu_adj}
  - id: dependent.h_aoc_cap
    printed: "(helper)"
    label: "$4,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}
  - id: dependent.h_aoc_band
    printed: "(helper)"
    label: "$2,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}
  - id: dependent.h_edu_aoc_amount
    printed: "(helper)"
    label: "Adjusted qualified education expenses, not more than $4,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [dependent.h_edu_ws4_aoc, dependent.h_aoc_cap]}
  - id: dependent.h_edu_on
    printed: "(helper)"
    label: "Claimed dependent student with qualified expenses, Form 1098-T and a TIN issued by the due date"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.edu, {const: true}]}
        - {op: test, eq: [dependent.edu_1098t, {const: true}]}
        - {op: test, eq: [dependent.edu_tin_issued, {const: true}]}
  - id: dependent.h_edu_over_refuse
    printed: "(helper)"
    label: "Tax-free assistance and refunds exceed an academic period's expenses (per-period worksheet needed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_on, {const: true}]}
        - {op: test, gt: [dependent.h_edu_adj, {const: 0}]}
        - {op: test, eq: [dependent.edu_over, {const: true}]}
  - id: dependent.h_aoc_path
    printed: "(helper)"
    label: "Lines 23 to 26 lead to lines 27 through 30 for this student"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_on, {const: true}]}
        - {op: test, eq: [dependent.edu_line23, {const: false}]}
        - {op: test, eq: [dependent.edu_line24, {const: true}]}
        - {op: test, eq: [dependent.edu_line25, {const: false}]}
        - {op: test, eq: [dependent.edu_line26, {const: false}]}
        - {op: test, eq: [dependent.edu_ein, {const: true}]}
    note: "Open: the form's path (lines 23-26) does not mention the EIN; the instructions require it to claim the American opportunity credit. Chosen: without the EIN the student goes to line 31 (lifetime learning credit)."
  - id: dependent.h_llc_path
    printed: "(helper)"
    label: "Go to line 31 for this student"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_on, {const: true}]}
        - {op: test, eq: [dependent.h_aoc_path, {const: false}]}
  - id: dependent.h_ptc_counts
    printed: "(helper)"
    label: "Dependent required to file an income tax return because of income"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.ptc_files, {const: true}]}
  - id: dependent.h_ctc_per
    printed: "(helper)"
    label: "$2,200"
    type: NonNegDollars
    expr: {op: param, ref: ctc.per_child}
  - id: dependent.h_odc_per
    printed: "(helper)"
    label: "$500"
    type: NonNegDollars
    expr: {op: param, ref: odc.per_dependent}
  - id: dependent.h_actc_per
    printed: "(helper)"
    label: "$1,700"
    type: NonNegDollars
    expr: {op: param, ref: actc.per_child}

  - id: dependent.dc_line2d
    printed: "2(d)"
    label: "Qualified expenses you incurred and paid in 2025 for the person listed in column (a)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.dc_qp, {const: true}]}, then: dependent.dc_paid}
        - {guard: {op: test, not: {op: test, eq: [dependent.dc_qp, {const: true}]}}, then: dependent.h_zero}
    shown_when: dependent.dc_qp
  - id: dependent.dc_line2c
    printed: "2(c)"
    label: "Check here if the qualifying person was over age 12 and was disabled"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.dc_qp, {const: true}]}
        - {op: test, eq: [dependent.dc_incapable, {const: true}]}
        - {op: test, eq: [dependent.h_dc_over12, {const: true}]}
    shown_when: dependent.dc_qp
  - id: dependent.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses (see instructions). Don't enter more than $4,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_aoc_path, {const: true}]}, then: dependent.h_edu_aoc_amount}
        - {guard: {op: test, not: {op: test, eq: [dependent.h_aoc_path, {const: true}]}}, then: dependent.h_zero}
    refuses: [dependent.h_edu_over_refuse]
    shown_when: dependent.h_aoc_path
    note: "Expenses and adjustments are aggregated across academic periods; a period whose adjustments exceed its expenses is refused."
  - id: dependent.edu_line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.edu_line27, take: dependent.h_aoc_band}
    shown_when: dependent.h_aoc_path
  - id: dependent.edu_line29
    printed: "29"
    label: "Multiply line 28 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: dependent.edu_line28, rate: {param: aoc.second_rate}}
    shown_when: dependent.h_aoc_path
  - id: dependent.h_l29_plus
    printed: "(helper)"
    label: "Add $2,000 to the amount on line 29"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_line29, dependent.h_aoc_band]}
  - id: dependent.edu_line30
    printed: "30"
    label: "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29 and enter the result"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.edu_line28, {const: 0}]}, then: dependent.edu_line27}
        - {guard: {op: test, gt: [dependent.edu_line28, {const: 0}]}, then: dependent.h_l29_plus}
    shown_when: dependent.h_aoc_path
  - id: dependent.edu_line31
    printed: "31"
    label: "Adjusted qualified education expenses (see instructions) (lifetime learning credit)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_llc_path, {const: true}]}, then: dependent.h_edu_ws4_llc}
        - {guard: {op: test, not: {op: test, eq: [dependent.h_llc_path, {const: true}]}}, then: dependent.h_zero}
    refuses: [dependent.h_edu_over_refuse]
    shown_when: dependent.h_llc_path

  - id: dependent.dc_lived_half
    printed: "(helper)"
    label: "Lived with you for more than half the year (a person born or who died in 2025: your home was their home more than half the time they were alive)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ge: [dependent.months, {const: 7, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [dependent.born_died, {const: true}]}
            - {op: test, eq: [dependent.part_year_home, {const: true}]}
  - id: dependent.one
    printed: "(helper)"
    label: "One (this person)"
    type: Count
    expr: {op: param, ref: dependent.one}
  - id: dependent.claimed
    printed: "(helper)"
    label: "You can claim this person as a dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_dep_base, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [sa.dependent, {const: false}]}
    refuses: [dependent.divorced_rule, dependent.married, dependent.multiple_support]
  - id: dependent.ctc_child
    printed: "(helper)"
    label: "You can claim the child tax credit for this person"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.h_qc, {const: true}]}
        - {op: test, eq: [dependent.h_tin, {const: true}]}
        - {op: test, eq: [dependent.h_cit, {const: true}]}
        - {op: test, lt: [dependent.age, {param: ctc.age_limit}]}
        - {op: test, eq: [dependent.h_work, {const: true}]}
        - {op: test, eq: [household.ctc_ssn, {const: true}]}
    note: "The filer SSN condition (you, or one spouse on a joint return, with an SSN valid for employment and the other with an SSN or ITIN) is read from household.ctc_ssn."
  - id: dependent.odc_person
    printed: "(helper)"
    label: "You can claim the credit for other dependents for this person"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.ctc_child, {const: false}]}
        - {op: test, eq: [dependent.h_tin, {const: true}]}
        - {op: test, eq: [dependent.h_cit, {const: true}]}
        - {op: test, eq: [household.all_tin, {const: true}]}
    note: "Open: Step 5 question 1 also accepts an ITIN applied for by the due date; the filer test is read from household.all_tin as published."
  - id: dependent.ctc_amount
    printed: "(helper)"
    label: "Schedule 8812 line 5 share: $2,200 for this qualifying child"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_ctc_per}
        - {guard: {op: test, not: {op: test, eq: [dependent.ctc_child, {const: true}]}}, then: dependent.h_zero}
  - id: dependent.odc_amount
    printed: "(helper)"
    label: "Schedule 8812 line 7 share: $500 for this other dependent"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.odc_person, {const: true}]}, then: dependent.h_odc_per}
        - {guard: {op: test, not: {op: test, eq: [dependent.odc_person, {const: true}]}}, then: dependent.h_zero}
  - id: dependent.actc_amount
    printed: "(helper)"
    label: "Schedule 8812 line 16b share: $1,700 for this qualifying child"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_actc_per}
        - {guard: {op: test, not: {op: test, eq: [dependent.ctc_child, {const: true}]}}, then: dependent.h_zero}
  - id: dependent.hoh_test2_lived
    printed: "(helper)"
    label: "Lived in your home for more than half of the year (or of the part alive, or since adoption or placement)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ge: [dependent.months, {const: 7, type: Count}]}
        - op: test
          all:
            - op: test
              any:
                - {op: test, eq: [dependent.born_died, {const: true}]}
                - {op: test, eq: [dependent.placed, {const: true}]}
            - {op: test, eq: [dependent.part_year_home, {const: true}]}
  - id: dependent.hoh_absence
    printed: "(helper)"
    label: "Time counted as lived with you includes an absence from which return was not reasonably expected or during which the home was not kept up"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_hoh_who, {const: true}]}
        - {op: test, eq: [dependent.hoh_test2_lived, {const: true}]}
        - {op: test, eq: [dependent.absence_no_return, {const: true}]}
  - id: dependent.hoh_test2
    printed: "(helper)"
    label: "Head of household Test 2: a qualifying person who lived with you for more than half of the year"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_hoh_who, {const: true}]}
        - {op: test, eq: [dependent.hoh_test2_lived, {const: true}]}
  - id: dependent.hoh_test1
    printed: "(helper)"
    label: "Head of household Test 1: your parent whom you can claim as a dependent, whose main home for all of 2025 you paid over half the cost of keeping up"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.relationship, {const: "parent"}]}
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.parent_home_paid, {const: true}]}
  - id: dependent.eic_child
    printed: "(helper)"
    label: "Qualifying child for the EIC"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_rel_qc, {const: true}]}
        - {op: test, eq: [dependent.h_age_ok, {const: true}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
        - {op: test, eq: [dependent.us_half, {const: true}]}
        - {op: test, eq: [dependent.h_qc_mine, {const: true}]}
    refuses: [dependent.divorced_rule, dependent.married]
  - id: dependent.eic_ssn_child
    printed: "(helper)"
    label: "Qualifying child for the EIC who has a valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.eic_child, {const: true}]}
        - {op: test, eq: [dependent.h_eicssn, {const: true}]}
  - id: dependent.dc_qp
    printed: "(helper)"
    label: "Qualifying person for the credit for child and dependent care expenses"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_dc_qp_child, {const: true}]}
        - {op: test, eq: [dependent.h_dc_qp_incapable, {const: true}]}
  - id: dependent.dc_count
    printed: "(helper)"
    label: "Number of qualifying persons this entry contributes (1 or 0)"
    type: Count
    expr: {op: percent_floor, part: dependent.h_dc_flag, whole: {const: 100}, cap: 1}
  - id: dependent.ptc_magi_counted
    printed: "(helper)"
    label: "Worksheet 1-2: modified AGI of this dependent, included only if required to file a return because of income"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_ptc_counts, {const: true}]}, then: dependent.ptc_magi}
        - {guard: {op: test, not: {op: test, eq: [dependent.h_ptc_counts, {const: true}]}}, then: dependent.h_zero}
```
```

<!-- part shared -->
45b31d0efa71a78e {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}
dbd8d147bac52913 {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}
eb6b9c3b873c1d3b {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}
5090e2054156fd72 {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}
57c9dda812295350 [{"$shared": "dbd8d147bac52913"}, {"$shared": "eb6b9c3b873c1d3b"}, {"$shared": "5090e2054156fd72"}]
259be3591f0d595e {"args": {"$shared": "57c9dda812295350"}, "test": "all"}
2c4a6224f1abc300 {"guard": {"$shared": "259be3591f0d595e"}, "then": {"param": "household.no"}}
cb88768b40471aff {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}
b97208e9b0a8586c {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}
fb503e6d1d9918ed {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}
86b535ae158e8869 [{"$shared": "cb88768b40471aff"}, {"$shared": "b97208e9b0a8586c"}, {"$shared": "fb503e6d1d9918ed"}]
dfe671ee2eedd621 {"args": {"$shared": "86b535ae158e8869"}, "test": "any"}
1381f8ffc1b24aec {"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}
7712fce87bc68862 {"guard": {"$shared": "1381f8ffc1b24aec"}, "then": {"input": "dependent.disabled"}}
7bc7453b71deb151 {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}
c75116fb0afe0e07 {"guard": {"args": [{"const": false}, {"input": "dependent.student"}], "test": "eq"}, "then": {"input": "dependent.disabled"}}
f376b03aa97bfeeb {"guard": {"args": [{"const": false}, {"input": "dependent.younger"}], "test": "eq"}, "then": {"input": "dependent.disabled"}}
25fda3e79e372eb7 {"guard": {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, "then": {"input": "dependent.younger"}}
6bbeda6ace8def4e [{"$shared": "f376b03aa97bfeeb"}, {"$shared": "25fda3e79e372eb7"}]
24d43568b504bcda {"alternatives": {"$shared": "6bbeda6ace8def4e"}, "op": "choose"}
a97ccaac99363331 {"guard": {"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, "then": {"$shared": "24d43568b504bcda"}}
d7dc823ab43d7b43 [{"$shared": "c75116fb0afe0e07"}, {"$shared": "a97ccaac99363331"}]
c87f35be61e52b52 {"alternatives": {"$shared": "d7dc823ab43d7b43"}, "op": "choose"}
2a12d106def17867 {"guard": {"$shared": "7bc7453b71deb151"}, "then": {"$shared": "c87f35be61e52b52"}}
78faf0570731bb14 [{"$shared": "7712fce87bc68862"}, {"$shared": "2a12d106def17867"}]
11ae5e22ec9f90ff {"alternatives": {"$shared": "78faf0570731bb14"}, "op": "choose"}
93effc74df04c4bc {"guard": {"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, "then": {"$shared": "11ae5e22ec9f90ff"}}
157171ca4377a2df {"guard": {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, "then": {"$shared": "24d43568b504bcda"}}
daee4fd02017e85a [{"$shared": "93effc74df04c4bc"}, {"$shared": "157171ca4377a2df"}]
964f5634c0940ab6 {"alternatives": {"$shared": "daee4fd02017e85a"}, "op": "choose"}
d501276bf4779658 [{"const": false}, {"$shared": "964f5634c0940ab6"}]
fccd6788d317a0bb {"args": {"$shared": "d501276bf4779658"}, "test": "eq"}
4c614b4955fbc2e4 {"guard": {"$shared": "fccd6788d317a0bb"}, "then": {"param": "household.no"}}
008b33a2315397a9 [{"const": true}, {"$shared": "964f5634c0940ab6"}]
a92529affa94912e {"args": {"$shared": "008b33a2315397a9"}, "test": "eq"}
5dd0f7b778264284 {"guard": {"args": [{"const": false}, {"input": "dependent.own_money"}], "test": "eq"}, "then": {"param": "household.no"}}
7ca0e4798fffbfc4 {"args": [{"const": "over_half"}, {"input": "dependent.self_support_view"}], "test": "eq"}
0e29877bfff7a320 {"guard": {"$shared": "7ca0e4798fffbfc4"}, "then": {"$shared": "7ca0e4798fffbfc4"}}
3d996a5e0f7cd98e {"args": [{"const": "under_half"}, {"input": "dependent.self_support_view"}], "test": "eq"}
77e3a82e7c29a646 {"guard": {"$shared": "3d996a5e0f7cd98e"}, "then": {"param": "household.no"}}
6bfcd092e376d8ac {"args": [{"const": "unsure"}, {"input": "dependent.self_support_view"}], "test": "eq"}
68a707065903f8ca {"guard": {"$shared": "6bfcd092e376d8ac"}, "then": {"input": "dependent.self_support"}}
8237ead0bb8967d9 [{"$shared": "0e29877bfff7a320"}, {"$shared": "77e3a82e7c29a646"}, {"$shared": "68a707065903f8ca"}]
ab2243fec4f653e2 {"alternatives": {"$shared": "8237ead0bb8967d9"}, "op": "choose"}
a5de992bedf4d3eb {"guard": {"args": [{"const": true}, {"input": "dependent.own_money"}], "test": "eq"}, "then": {"$shared": "ab2243fec4f653e2"}}
4812e2b8e0bc8c05 [{"$shared": "5dd0f7b778264284"}, {"$shared": "a5de992bedf4d3eb"}]
22a92db85e2ea727 {"alternatives": {"$shared": "4812e2b8e0bc8c05"}, "op": "choose"}
91c286c9c4301751 [{"const": false}, {"$shared": "22a92db85e2ea727"}]
8ef0991a03b97900 {"args": {"$shared": "91c286c9c4301751"}, "test": "eq"}
84fd80eb66b34eb8 {"guard": {"args": [{"const": false}, {"input": "dependent.ever_married"}], "test": "eq"}, "then": {"param": "household.no"}}
74f27b4009d598f2 {"guard": {"args": [{"const": true}, {"input": "dependent.ever_married"}], "test": "eq"}, "then": {"input": "dependent.joint_return"}}
0a4e9e4ac7e49e06 [{"$shared": "84fd80eb66b34eb8"}, {"$shared": "74f27b4009d598f2"}]
f0a0ea307fd027da {"alternatives": {"$shared": "0a4e9e4ac7e49e06"}, "op": "choose"}
da631d06c2a5809d [{"const": false}, {"$shared": "f0a0ea307fd027da"}]
00efe0d5f3d5b9f2 {"args": {"$shared": "da631d06c2a5809d"}, "test": "eq"}
ed36511d6154e9df {"args": [{"const": false}, {"input": "dependent.lived_all_year"}], "test": "eq"}
07a070f41524003e {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}
c731a8a06c6461dd {"guard": {"$shared": "ed36511d6154e9df"}, "then": {"$shared": "07a070f41524003e"}}
f668a52c8c67c388 {"args": [{"const": true}, {"input": "dependent.lived_all_year"}], "test": "eq"}
55eda485202777c9 {"guard": {"$shared": "f668a52c8c67c388"}, "then": {"input": "dependent.lived_all_year"}}
b60326e00d27f6a4 [{"$shared": "c731a8a06c6461dd"}, {"$shared": "55eda485202777c9"}]
68017dd572aa517b {"alternatives": {"$shared": "b60326e00d27f6a4"}, "op": "choose"}
4e4dee6c8202bf2d {"guard": {"$shared": "00efe0d5f3d5b9f2"}, "then": {"$shared": "68017dd572aa517b"}}
5ebf600f89d189d2 [{"const": true}, {"$shared": "f0a0ea307fd027da"}]
d93de693f4fa744c {"args": {"$shared": "5ebf600f89d189d2"}, "test": "eq"}
433fe18d3516aefb {"guard": {"$shared": "d93de693f4fa744c"}, "then": {"param": "household.no"}}
893c553957be18a8 [{"$shared": "4e4dee6c8202bf2d"}, {"$shared": "433fe18d3516aefb"}]
339c93f346edb919 {"alternatives": {"$shared": "893c553957be18a8"}, "op": "choose"}
cadbb62ddbdf39f1 {"guard": {"$shared": "8ef0991a03b97900"}, "then": {"$shared": "339c93f346edb919"}}
a44e552c8b186af0 [{"const": true}, {"$shared": "22a92db85e2ea727"}]
73d53ce7b10978aa {"args": {"$shared": "a44e552c8b186af0"}, "test": "eq"}
be6cbed5980b2588 {"guard": {"$shared": "73d53ce7b10978aa"}, "then": {"param": "household.no"}}
4a1f4e6d02b880bf [{"$shared": "cadbb62ddbdf39f1"}, {"$shared": "be6cbed5980b2588"}]
94564d402d9dd02e {"alternatives": {"$shared": "4a1f4e6d02b880bf"}, "op": "choose"}
f35e95748befe7ce {"guard": {"$shared": "a92529affa94912e"}, "then": {"$shared": "94564d402d9dd02e"}}
03dbf00fb0dc1842 [{"$shared": "4c614b4955fbc2e4"}, {"$shared": "f35e95748befe7ce"}]
23a75063a22a6983 {"alternatives": {"$shared": "03dbf00fb0dc1842"}, "op": "choose"}
fe7b09e7394ffa4b {"guard": {"$shared": "dfe671ee2eedd621"}, "then": {"$shared": "23a75063a22a6983"}}
6659f23c791bb14e [{"$shared": "2c4a6224f1abc300"}, {"$shared": "fe7b09e7394ffa4b"}]
f3df59358dcc04fc {"alternatives": {"$shared": "6659f23c791bb14e"}, "op": "choose"}
8fce90f46eada816 [{"const": true}, {"$shared": "f3df59358dcc04fc"}]
726b909b48f9c541 {"args": {"$shared": "8fce90f46eada816"}, "test": "ne"}
d5f93e367e7c7636 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"$shared": "45b31d0efa71a78e"}, {"$shared": "726b909b48f9c541"}]
fab3ac8d14d1e92b {"args": {"$shared": "d5f93e367e7c7636"}, "test": "all"}
6377ef03fa616477 [{"const": true}, {"$shared": "68017dd572aa517b"}]
cb03c1e6c4c3bab4 {"args": {"$shared": "6377ef03fa616477"}, "test": "eq"}
d94096ad1e346ada [{"$shared": "fab3ac8d14d1e92b"}, {"$shared": "cb03c1e6c4c3bab4"}]
4aae835f34adedb2 {"args": {"$shared": "d94096ad1e346ada"}, "test": "any"}
04cf2a1cd8a7bd78 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"$shared": "45b31d0efa71a78e"}]
eb2f25e404a0a870 {"args": {"$shared": "04cf2a1cd8a7bd78"}, "test": "all"}
da884a5a9bffad77 {"args": [{"const": 7, "type": "Count"}, {"input": "dependent.months"}], "test": "le"}
c61f14d9d61d00eb [{"$shared": "eb2f25e404a0a870"}, {"$shared": "da884a5a9bffad77"}]
46b66a31fd3a3891 {"args": {"$shared": "c61f14d9d61d00eb"}, "test": "any"}
909848cd137657d6 {"args": {"$shared": "8fce90f46eada816"}, "test": "eq"}
81fabfa25f6d4fd5 {"guard": {"args": [{"const": false}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, "then": {"input": "dependent.citizen"}}
31ff7178cc6ae312 {"guard": {"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, "then": {"input": "dependent.citizen_ssn"}}
b22e7ba9e475faa3 [{"$shared": "81fabfa25f6d4fd5"}, {"$shared": "31ff7178cc6ae312"}]
2b7ff996bb19ef59 {"alternatives": {"$shared": "b22e7ba9e475faa3"}, "op": "choose"}
496eba45d7241943 [{"const": false}, {"$shared": "2b7ff996bb19ef59"}]
aa9fdf730f1babf9 {"args": {"$shared": "496eba45d7241943"}, "test": "eq"}
0d47e47f23776a22 {"guard": {"$shared": "aa9fdf730f1babf9"}, "then": {"input": "dependent.canada_mexico"}}
2ed264c1638b4b4d [{"const": true}, {"$shared": "2b7ff996bb19ef59"}]
f899dd2da804e8d7 {"args": {"$shared": "2ed264c1638b4b4d"}, "test": "eq"}
7f6893414336fad5 {"guard": {"$shared": "f899dd2da804e8d7"}, "then": {"$shared": "2b7ff996bb19ef59"}}
9dd009938e85bcd7 [{"$shared": "0d47e47f23776a22"}, {"$shared": "7f6893414336fad5"}]
e90c1e89cc9b180f {"alternatives": {"$shared": "9dd009938e85bcd7"}, "op": "choose"}
2b8915f60cc8b154 [{"const": false}, {"$shared": "e90c1e89cc9b180f"}]
17cde2d3c021a307 {"args": {"$shared": "2b8915f60cc8b154"}, "test": "eq"}
9e57f5274fe45bc0 {"guard": {"$shared": "17cde2d3c021a307"}, "then": {"param": "household.no"}}
ba30ef09311c5441 [{"const": true}, {"$shared": "e90c1e89cc9b180f"}]
a71764b3652b3874 {"args": {"$shared": "ba30ef09311c5441"}, "test": "eq"}
2acd47b8266471ba {"guard": {"$shared": "a71764b3652b3874"}, "then": {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}}
8ac79f64962eb12a [{"$shared": "9e57f5274fe45bc0"}, {"$shared": "2acd47b8266471ba"}]
f5013721bd489d9d {"alternatives": {"$shared": "8ac79f64962eb12a"}, "op": "choose"}
26de867d5e4e4604 {"guard": {"$shared": "909848cd137657d6"}, "then": {"$shared": "f5013721bd489d9d"}}
4e43ac992b550985 {"guard": {"$shared": "726b909b48f9c541"}, "then": {"param": "household.no"}}
d4fa1a4aa297e144 [{"$shared": "26de867d5e4e4604"}, {"$shared": "4e43ac992b550985"}]
cd75754270d615d0 {"alternatives": {"$shared": "d4fa1a4aa297e144"}, "op": "choose"}
516fb4028cf64f9f [{"const": false}, {"$shared": "cd75754270d615d0"}]
684faf9e6923f98a {"args": {"$shared": "516fb4028cf64f9f"}, "test": "eq"}
a10e36b275ccac18 {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}
cae21fd21ef95261 {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}
475db94656536733 {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}
82b70661ca566396 [{"$shared": "cb88768b40471aff"}, {"$shared": "a10e36b275ccac18"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "475db94656536733"}, {"$shared": "b97208e9b0a8586c"}]
91a4aae4183f8f2c {"args": {"$shared": "82b70661ca566396"}, "test": "any"}
df298e38774d668f {"guard": {"$shared": "91a4aae4183f8f2c"}, "then": {"$shared": "91a4aae4183f8f2c"}}
9b04e8f56ed52305 {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}
93acefeeff4286eb [{"$shared": "9b04e8f56ed52305"}, {"$shared": "fb503e6d1d9918ed"}]
782ba030bc74113e {"args": {"$shared": "93acefeeff4286eb"}, "test": "any"}
262d147998c405ca {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}
250d38940f4a5462 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"$shared": "262d147998c405ca"}]
458fab87f9dd7601 {"args": {"$shared": "250d38940f4a5462"}, "test": "all"}
c3b0922f65c98601 {"guard": {"$shared": "458fab87f9dd7601"}, "then": {"$shared": "458fab87f9dd7601"}}
797e9b74b4e8e4ec {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "ne"}
79166e1cd7b8e694 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"$shared": "797e9b74b4e8e4ec"}]
61637c12d231a4af {"args": {"$shared": "79166e1cd7b8e694"}, "test": "any"}
a49dfef7758f25b3 {"guard": {"$shared": "ed36511d6154e9df"}, "then": {"input": "dependent.qr_all_year"}}
3a91248e1bcee6d8 [{"$shared": "a49dfef7758f25b3"}, {"$shared": "55eda485202777c9"}]
5ef59dc55ce92244 {"alternatives": {"$shared": "3a91248e1bcee6d8"}, "op": "choose"}
dc63a240158faf17 [{"const": false}, {"$shared": "5ef59dc55ce92244"}]
f5de24c486ce70c8 {"args": {"$shared": "dc63a240158faf17"}, "test": "eq"}
bdf68a5464158b6c {"guard": {"$shared": "f5de24c486ce70c8"}, "then": {"param": "household.no"}}
d948660a72219e1f [{"const": true}, {"$shared": "5ef59dc55ce92244"}]
dc0fef1e6b60aa95 {"args": {"$shared": "d948660a72219e1f"}, "test": "eq"}
c894b9e471cd15ce {"guard": {"$shared": "dc0fef1e6b60aa95"}, "then": {"input": "dependent.lawful"}}
942e73ad5ba8ac73 [{"$shared": "bdf68a5464158b6c"}, {"$shared": "c894b9e471cd15ce"}]
e9899da862973fba {"alternatives": {"$shared": "942e73ad5ba8ac73"}, "op": "choose"}
ad6968fb2fac37aa {"guard": {"$shared": "61637c12d231a4af"}, "then": {"$shared": "e9899da862973fba"}}
623895f2b7c68376 [{"$shared": "c3b0922f65c98601"}, {"$shared": "ad6968fb2fac37aa"}]
3268630b16733842 {"alternatives": {"$shared": "623895f2b7c68376"}, "op": "choose"}
7e2b543675c75599 {"guard": {"$shared": "782ba030bc74113e"}, "then": {"$shared": "3268630b16733842"}}
496a1e5bc5a2855e {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}
bbf5323ab591e5a9 {"guard": {"$shared": "61637c12d231a4af"}, "then": {"$shared": "5ef59dc55ce92244"}}
4479e1d08e39c278 [{"$shared": "c3b0922f65c98601"}, {"$shared": "bbf5323ab591e5a9"}]
f84f679754be8dd5 {"alternatives": {"$shared": "4479e1d08e39c278"}, "op": "choose"}
a3855028fd3faaac {"guard": {"$shared": "496a1e5bc5a2855e"}, "then": {"$shared": "f84f679754be8dd5"}}
b2eaadeb735b54b6 [{"$shared": "df298e38774d668f"}, {"$shared": "7e2b543675c75599"}, {"$shared": "a3855028fd3faaac"}]
d4e958a65f5600b4 {"alternatives": {"$shared": "b2eaadeb735b54b6"}, "op": "choose"}
a1119914915cf882 [{"const": false}, {"$shared": "d4e958a65f5600b4"}]
990c85f4a030f6f8 {"args": {"$shared": "a1119914915cf882"}, "test": "eq"}
6f24ecf0c7876222 {"guard": {"$shared": "990c85f4a030f6f8"}, "then": {"param": "household.no"}}
1e33e8beac615d26 [{"const": true}, {"$shared": "d4e958a65f5600b4"}]
21463e61ce177bb6 {"args": {"$shared": "1e33e8beac615d26"}, "test": "eq"}
c7b89b2404b84b41 {"guard": {"$shared": "909848cd137657d6"}, "then": {"param": "household.no"}}
f5726735e624cfd5 {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}
b94a73b8f71d6d33 {"guard": {"$shared": "f5726735e624cfd5"}, "then": {"param": "household.no"}}
14b7aaa29e3bef3d {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}
81e9b5c4c4ab4c50 {"args": [{"const": "over_half"}, {"input": "dependent.supported_view"}], "test": "eq"}
f96d93cb20bfaaa2 {"guard": {"$shared": "81e9b5c4c4ab4c50"}, "then": {"$shared": "81e9b5c4c4ab4c50"}}
fa2f54058212d581 {"args": [{"const": "under_half"}, {"input": "dependent.supported_view"}], "test": "eq"}
86f72241a30c800f {"guard": {"$shared": "fa2f54058212d581"}, "then": {"param": "household.no"}}
7ee8927420db1540 {"args": [{"const": "unsure"}, {"input": "dependent.supported_view"}], "test": "eq"}
9d3d336043153328 {"guard": {"$shared": "7ee8927420db1540"}, "then": {"input": "dependent.supported"}}
2a875de1ca138afd [{"$shared": "f96d93cb20bfaaa2"}, {"$shared": "86f72241a30c800f"}, {"$shared": "9d3d336043153328"}]
75f834e8f555c7b0 {"alternatives": {"$shared": "2a875de1ca138afd"}, "op": "choose"}
64051695fa6e4a20 {"guard": {"$shared": "14b7aaa29e3bef3d"}, "then": {"$shared": "75f834e8f555c7b0"}}
fc5b61e881bdcd98 [{"$shared": "b94a73b8f71d6d33"}, {"$shared": "64051695fa6e4a20"}]
8814afa4f1dda392 {"alternatives": {"$shared": "fc5b61e881bdcd98"}, "op": "choose"}
c80e1e1fe5d09e89 {"guard": {"$shared": "726b909b48f9c541"}, "then": {"$shared": "8814afa4f1dda392"}}
43fb1d2cd794e9e4 [{"$shared": "c7b89b2404b84b41"}, {"$shared": "c80e1e1fe5d09e89"}]
21cda9b829a93fc8 {"alternatives": {"$shared": "43fb1d2cd794e9e4"}, "op": "choose"}
295e386a8aa61128 {"guard": {"$shared": "21463e61ce177bb6"}, "then": {"$shared": "21cda9b829a93fc8"}}
9b03d2fa16a5428c [{"$shared": "6f24ecf0c7876222"}, {"$shared": "295e386a8aa61128"}]
0f45f15a2f53eb0e {"alternatives": {"$shared": "9b03d2fa16a5428c"}, "op": "choose"}
89275c519317e7a4 [{"const": false}, {"$shared": "0f45f15a2f53eb0e"}]
15d9dbefee5f16cb {"args": {"$shared": "89275c519317e7a4"}, "test": "eq"}
70d0f6df7ec878a2 {"guard": {"$shared": "15d9dbefee5f16cb"}, "then": {"param": "household.no"}}
864f1bf0aa7bac0a [{"const": true}, {"$shared": "0f45f15a2f53eb0e"}]
5cb326e3903c0aed {"args": {"$shared": "864f1bf0aa7bac0a"}, "test": "eq"}
d448659265e908c5 {"guard": {"$shared": "5cb326e3903c0aed"}, "then": {"$shared": "f5013721bd489d9d"}}
4590fa1c756c7e2e [{"$shared": "70d0f6df7ec878a2"}, {"$shared": "d448659265e908c5"}]
bcd1188dd01faa4e {"alternatives": {"$shared": "4590fa1c756c7e2e"}, "op": "choose"}
854ce61c34865fcf {"guard": {"$shared": "684faf9e6923f98a"}, "then": {"$shared": "bcd1188dd01faa4e"}}
e980018b74e8c336 [{"const": true}, {"$shared": "cd75754270d615d0"}]
04706b205e474b59 {"args": {"$shared": "e980018b74e8c336"}, "test": "eq"}
7a895badee7db8c4 {"guard": {"$shared": "04706b205e474b59"}, "then": {"$shared": "cd75754270d615d0"}}
0f8b5f8518fd1984 [{"$shared": "854ce61c34865fcf"}, {"$shared": "7a895badee7db8c4"}]
6ecfc66c418695cc {"alternatives": {"$shared": "0f8b5f8518fd1984"}, "op": "choose"}
f6acbdaf098f42c1 [{"$shared": "6bfcd092e376d8ac"}, {"args": [{"const": true}, {"input": "dependent.self_support"}], "test": "eq"}]
01d833f52e00cf64 {"args": {"$shared": "f6acbdaf098f42c1"}, "test": "all"}
65795f1f22a57c0f [{"$shared": "01d833f52e00cf64"}, {"$shared": "7ca0e4798fffbfc4"}]
7c54607369fbe02f {"args": {"$shared": "65795f1f22a57c0f"}, "test": "any"}
01830f313059cf8a [{"$shared": "7c54607369fbe02f"}, {"args": [{"const": true}, {"input": "dependent.own_money"}], "test": "eq"}]
51cc58eb9e56b329 {"args": {"$shared": "01830f313059cf8a"}, "test": "all"}
f07b4f56dd3d7ee6 [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}]
78ee2dec84d6d953 {"args": {"$shared": "f07b4f56dd3d7ee6"}, "test": "any"}
86ebe37df995ae49 [{"$shared": "1381f8ffc1b24aec"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}]
d07889d0922fd64c {"args": {"$shared": "86ebe37df995ae49"}, "test": "any"}
31a1432bd7aa760e [{"$shared": "78ee2dec84d6d953"}, {"$shared": "d07889d0922fd64c"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}]
912a5a7a234e62fb {"args": {"$shared": "31a1432bd7aa760e"}, "test": "all"}
6b958588ce0c364c {"args": [{"input": "dependent.months"}, {"const": 7, "type": "Count"}], "test": "lt"}
a889a708656a69c0 [{"$shared": "51cc58eb9e56b329"}, {"$shared": "912a5a7a234e62fb"}, {"$shared": "259be3591f0d595e"}, {"$shared": "6b958588ce0c364c"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}]
c3f47436dc98b30f {"args": {"$shared": "a889a708656a69c0"}, "test": "any"}
02a6487023ff1c0e {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}
4d6abd3233e0922b {"args": [{"const": true}, {"input": "dependent.other_nontaxpayer"}], "test": "eq"}
3ab93055c4a8bc36 [{"$shared": "02a6487023ff1c0e"}, {"$shared": "4d6abd3233e0922b"}]
1883b3543934be39 {"args": {"$shared": "3ab93055c4a8bc36"}, "test": "any"}
7e1c75e5496df0ab [{"$shared": "c3f47436dc98b30f"}, {"$shared": "1883b3543934be39"}]
3bba396421cd08e1 {"args": {"$shared": "7e1c75e5496df0ab"}, "test": "all"}
5d1792dbc0ff6ce8 [{"$shared": "7ee8927420db1540"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}]
5cdd94d35e804dbc {"args": {"$shared": "5d1792dbc0ff6ce8"}, "test": "all"}
83306ff2d22fccbf [{"$shared": "5cdd94d35e804dbc"}, {"$shared": "81e9b5c4c4ab4c50"}]
dc6a51f361363ce3 {"args": {"$shared": "83306ff2d22fccbf"}, "test": "any"}
e07497c2d2e787fb [{"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}]
00740b4f0410aeb6 {"args": {"$shared": "e07497c2d2e787fb"}, "test": "all"}
0af63361e4edfb06 [{"$shared": "458fab87f9dd7601"}, {"$shared": "cb88768b40471aff"}, {"$shared": "a10e36b275ccac18"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "475db94656536733"}, {"$shared": "b97208e9b0a8586c"}]
07ff44ec481e8052 {"args": {"$shared": "0af63361e4edfb06"}, "test": "any"}
984601c9dbc5eba5 [{"$shared": "00740b4f0410aeb6"}, {"$shared": "07ff44ec481e8052"}, {"$shared": "496a1e5bc5a2855e"}]
55ebead86d5265e0 {"args": {"$shared": "984601c9dbc5eba5"}, "test": "any"}
56678086844fa1f2 [{"$shared": "3bba396421cd08e1"}, {"$shared": "dc6a51f361363ce3"}, {"$shared": "55ebead86d5265e0"}]
a46d34c741c15e09 {"args": {"$shared": "56678086844fa1f2"}, "test": "all"}
8e034af036d202ea [{"$shared": "a46d34c741c15e09"}, {"$shared": "14b7aaa29e3bef3d"}]
f6e2ff027fe266eb {"args": {"$shared": "8e034af036d202ea"}, "test": "all"}
9dcdae15c6e67517 {"args": [{"const": "unsure"}, {"input": "dependent.self_support_view"}], "test": "ne"}
13728b1761998378 [{"$shared": "9dcdae15c6e67517"}, {"args": [{"const": true}, {"input": "dependent.self_support"}], "test": "ne"}]
2470b8b1a568dde8 {"args": {"$shared": "13728b1761998378"}, "test": "any"}
eb2ea771b53a3d25 {"args": [{"const": "over_half"}, {"input": "dependent.self_support_view"}], "test": "ne"}
ca0b56fdf12d8aa2 [{"$shared": "2470b8b1a568dde8"}, {"$shared": "eb2ea771b53a3d25"}]
65daf24ab2b3f02e {"args": {"$shared": "ca0b56fdf12d8aa2"}, "test": "all"}
182510ac5359404d [{"$shared": "65daf24ab2b3f02e"}, {"args": [{"const": true}, {"input": "dependent.own_money"}], "test": "ne"}]
c1395745df12677d {"args": {"$shared": "182510ac5359404d"}, "test": "any"}
0a2e10cedfae3bfb [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"$shared": "7bc7453b71deb151"}]
33fc981e094611e8 {"args": {"$shared": "0a2e10cedfae3bfb"}, "test": "all"}
638e10d34af6777d [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}]
549d9711fcb0a0d9 {"args": {"$shared": "638e10d34af6777d"}, "test": "all"}
2e05de679cee00c4 [{"$shared": "33fc981e094611e8"}, {"$shared": "549d9711fcb0a0d9"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}]
aae5cb78c743225c {"args": {"$shared": "2e05de679cee00c4"}, "test": "any"}
7beb7bcc8851ec54 [{"$shared": "c1395745df12677d"}, {"$shared": "aae5cb78c743225c"}, {"$shared": "dfe671ee2eedd621"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"$shared": "da884a5a9bffad77"}]
cdeef980fd44dad9 {"args": {"$shared": "7beb7bcc8851ec54"}, "test": "all"}
21de8f70933b8703 {"args": [{"const": false}, {"input": "dependent.spouse_claims"}], "test": "eq"}
932daea67a3f4706 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"$shared": "21de8f70933b8703"}]
b34648d2d17420ab {"args": {"$shared": "932daea67a3f4706"}, "test": "any"}
19d9d483c884fe90 {"args": [{"const": true}, {"input": "dependent.other_only_spouse"}], "test": "eq"}
3c1297996c38f15c [{"$shared": "b34648d2d17420ab"}, {"$shared": "19d9d483c884fe90"}]
e6e30488ea6b250b {"args": {"$shared": "3c1297996c38f15c"}, "test": "all"}
b6381ef197b3b701 {"args": [{"const": false}, {"input": "dependent.other_only_spouse"}], "test": "eq"}
a86fbaaf1cc671fe [{"$shared": "b6381ef197b3b701"}, {"args": [{"const": true}, {"input": "dependent.filer_parent"}], "test": "eq"}]
83a584c9d08b9cc7 {"args": {"$shared": "a86fbaaf1cc671fe"}, "test": "all"}
674a048744f46ddf [{"$shared": "e6e30488ea6b250b"}, {"$shared": "83a584c9d08b9cc7"}, {"$shared": "02a6487023ff1c0e"}, {"$shared": "4d6abd3233e0922b"}]
c3cee0d9721af552 {"args": {"$shared": "674a048744f46ddf"}, "test": "any"}
b43ae14178a09e88 [{"$shared": "cdeef980fd44dad9"}, {"$shared": "c3cee0d9721af552"}]
45a2cd7f5e7f7f9f {"args": {"$shared": "b43ae14178a09e88"}, "test": "all"}
b5ee3a9128744c94 [{"$shared": "f6e2ff027fe266eb"}, {"$shared": "45a2cd7f5e7f7f9f"}]
807e3bee555069ce {"args": {"$shared": "b5ee3a9128744c94"}, "test": "any"}
93ec5473ae5e5158 [{"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}]
1fd77c3d63ad8b8e {"args": {"$shared": "93ec5473ae5e5158"}, "test": "any"}
ee2f97e51aef40ff [{"$shared": "1fd77c3d63ad8b8e"}, {"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}]
d3c7eccf3db4c0cf {"args": {"$shared": "ee2f97e51aef40ff"}, "test": "any"}
14866c29e72d991c [{"$shared": "807e3bee555069ce"}, {"$shared": "d3c7eccf3db4c0cf"}]
a62b18320965560e {"args": {"$shared": "14866c29e72d991c"}, "test": "all"}
e60882f7bb5e1a22 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}]
982ab331e31c3a45 {"args": {"$shared": "e60882f7bb5e1a22"}, "test": "any"}
a908a4b9d8e84ffd [{"$shared": "a62b18320965560e"}, {"$shared": "982ab331e31c3a45"}]
17c073aa76ed8007 {"args": {"$shared": "a908a4b9d8e84ffd"}, "test": "all"}
f3103484a6f14912 {"guard": {"$shared": "684faf9e6923f98a"}, "then": {"param": "household.no"}}
f5d30cab7146da98 {"guard": {"args": [{"const": false}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, "then": {"input": "dependent.tin"}}
c93d7c4bee11f246 [{"$shared": "f5d30cab7146da98"}, {"$shared": "31ff7178cc6ae312"}]
b449cba5462d7812 {"alternatives": {"$shared": "c93d7c4bee11f246"}, "op": "choose"}
7378fd109064c5ad [{"const": false}, {"$shared": "b449cba5462d7812"}]
cd78de32040f7039 {"args": {"$shared": "7378fd109064c5ad"}, "test": "eq"}
725d681bbf866af6 {"guard": {"$shared": "cd78de32040f7039"}, "then": {"param": "household.no"}}
26a3796b76e9f809 [{"const": true}, {"$shared": "b449cba5462d7812"}]
63b6c7aa24bca7a9 {"args": {"$shared": "26a3796b76e9f809"}, "test": "eq"}
b804482ee35038d6 {"guard": {"$shared": "aa9fdf730f1babf9"}, "then": {"param": "household.no"}}
475a509e3d1380c7 {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}
8064bdcd6466520e {"guard": {"$shared": "475a509e3d1380c7"}, "then": {"param": "household.no"}}
3cec84f965d300a6 {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}
dd4d39b06abd576f {"guard": {"args": [{"const": false}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, "then": {"input": "dependent.work_ssn"}}
923f4acaa3d2a896 [{"$shared": "dd4d39b06abd576f"}, {"$shared": "31ff7178cc6ae312"}]
8718b5143fb9495e {"alternatives": {"$shared": "923f4acaa3d2a896"}, "op": "choose"}
ad365246b6689c1e [{"const": false}, {"$shared": "8718b5143fb9495e"}]
250d676b3ec5881e {"args": {"$shared": "ad365246b6689c1e"}, "test": "eq"}
f23debb52c569725 {"guard": {"$shared": "250d676b3ec5881e"}, "then": {"param": "household.no"}}
cde4fd3863004447 [{"const": true}, {"$shared": "8718b5143fb9495e"}]
5d68b2a4b707ee4f {"args": {"$shared": "cde4fd3863004447"}, "test": "eq"}
1284144362fc8e35 {"collection": "person", "field": "person.one", "op": "sum_over", "where": null}
d61268f16b0dd8bb {"guard": {"args": [{"const": false}, {"input": "person.tin"}], "test": "eq"}, "then": {"input": "person.work_ssn"}}
17885559bb9f1a6f {"guard": {"args": [{"const": true}, {"input": "person.tin"}], "test": "eq"}, "then": {"input": "person.tin"}}
51f70f68e0219e63 [{"$shared": "d61268f16b0dd8bb"}, {"$shared": "17885559bb9f1a6f"}]
b72414855ce995c3 {"alternatives": {"$shared": "51f70f68e0219e63"}, "op": "choose"}
03e4b24a02961c31 [{"const": true}, {"$shared": "b72414855ce995c3"}]
50c7615e061dc273 {"args": {"$shared": "03e4b24a02961c31"}, "test": "eq"}
58441ebb5ddd7242 {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"$shared": "50c7615e061dc273"}}
3503b2668d859ed6 [{"$shared": "1284144362fc8e35"}, {"$shared": "58441ebb5ddd7242"}]
53f4458376080d91 {"args": {"$shared": "3503b2668d859ed6"}, "test": "eq"}
ac4b48c317adfa6c {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}
e838b1b389be89f9 [{"const": 0, "type": "Count"}, {"$shared": "ac4b48c317adfa6c"}]
c176015c6ba65da5 {"args": {"$shared": "e838b1b389be89f9"}, "test": "lt"}
8156e5ea73f92986 [{"$shared": "53f4458376080d91"}, {"$shared": "c176015c6ba65da5"}]
78ced2d4a94bd48a {"args": {"$shared": "8156e5ea73f92986"}, "test": "all"}
c866df876b8a6486 {"guard": {"$shared": "5d68b2a4b707ee4f"}, "then": {"$shared": "78ced2d4a94bd48a"}}
e66b11e161b54817 [{"$shared": "f23debb52c569725"}, {"$shared": "c866df876b8a6486"}]
e53ca2928f82fd56 {"alternatives": {"$shared": "e66b11e161b54817"}, "op": "choose"}
70222f4c04fd737d {"guard": {"$shared": "3cec84f965d300a6"}, "then": {"$shared": "e53ca2928f82fd56"}}
5dfa800e4152b4e0 [{"$shared": "8064bdcd6466520e"}, {"$shared": "70222f4c04fd737d"}]
f265775b8b6322e1 {"alternatives": {"$shared": "5dfa800e4152b4e0"}, "op": "choose"}
038bf3853a1324e9 {"guard": {"$shared": "f899dd2da804e8d7"}, "then": {"$shared": "f265775b8b6322e1"}}
a0eed058e85201b6 [{"$shared": "b804482ee35038d6"}, {"$shared": "038bf3853a1324e9"}]
be5f4a6944706a2a {"alternatives": {"$shared": "a0eed058e85201b6"}, "op": "choose"}
67f8f182bcc58fc2 {"guard": {"$shared": "63b6c7aa24bca7a9"}, "then": {"$shared": "be5f4a6944706a2a"}}
5325848a2a7add51 [{"$shared": "725d681bbf866af6"}, {"$shared": "67f8f182bcc58fc2"}]
b63a5fc414621f38 {"alternatives": {"$shared": "5325848a2a7add51"}, "op": "choose"}
d56170244e30565a {"guard": {"$shared": "04706b205e474b59"}, "then": {"$shared": "b63a5fc414621f38"}}
803c08233feb6fac [{"$shared": "f3103484a6f14912"}, {"$shared": "d56170244e30565a"}]
13c2c289fa5d65ba {"alternatives": {"$shared": "803c08233feb6fac"}, "op": "choose"}
312ca0b51e745209 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}]
6f20306cdcff36df {"args": {"$shared": "312ca0b51e745209"}, "test": "any"}
e94a3c209ce97176 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}]
804674facba7ce5d {"args": {"$shared": "e94a3c209ce97176"}, "test": "any"}
e5f7b39bfd3c3178 [{"$shared": "17c073aa76ed8007"}, {"$shared": "45a2cd7f5e7f7f9f"}, {"$shared": "78ced2d4a94bd48a"}, {"$shared": "1fd77c3d63ad8b8e"}, {"$shared": "6f20306cdcff36df"}, {"$shared": "804674facba7ce5d"}, {"$shared": "3cec84f965d300a6"}]
00a9f0bfde6657ef {"args": {"$shared": "e5f7b39bfd3c3178"}, "test": "all"}
0e7d2ad8cd3c20eb [{"const": false}, {"$shared": "6ecfc66c418695cc"}]
3f8a693dbfd55cbd {"args": {"$shared": "0e7d2ad8cd3c20eb"}, "test": "eq"}
7cd70b16f4cff8ee {"guard": {"$shared": "3f8a693dbfd55cbd"}, "then": {"param": "household.no"}}
eff46eef862d78bf [{"const": true}, {"$shared": "6ecfc66c418695cc"}]
0e836bee5ee949c8 {"args": {"$shared": "eff46eef862d78bf"}, "test": "eq"}
472e2a6570444e78 [{"const": false}, {"$shared": "13c2c289fa5d65ba"}]
c2062ef24e1afd8f {"args": {"$shared": "472e2a6570444e78"}, "test": "eq"}
fa1207db79af8c04 {"guard": {"args": [{"const": false}, {"input": "person.tin"}], "test": "eq"}, "then": {"input": "person.itin_applied"}}
e3885fa48a6cd717 [{"$shared": "fa1207db79af8c04"}, {"$shared": "17885559bb9f1a6f"}]
6acfd55cc2ff9a9a {"alternatives": {"$shared": "e3885fa48a6cd717"}, "op": "choose"}
32a1663f70201828 [{"const": true}, {"$shared": "6acfd55cc2ff9a9a"}]
d7f03e40774666a7 {"args": {"$shared": "32a1663f70201828"}, "test": "eq"}
e8a85e87a1237351 {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"$shared": "d7f03e40774666a7"}}
a2641fe84c411e26 [{"$shared": "1284144362fc8e35"}, {"$shared": "e8a85e87a1237351"}]
9ab757132a95133d {"args": {"$shared": "a2641fe84c411e26"}, "test": "eq"}
352677350c6607b6 {"guard": {"$shared": "c2062ef24e1afd8f"}, "then": {"$shared": "9ab757132a95133d"}}
6dc634208bfdb15e [{"const": true}, {"$shared": "13c2c289fa5d65ba"}]
079efa16382b8700 {"args": {"$shared": "6dc634208bfdb15e"}, "test": "eq"}
47de1eaa2fb0dcc8 {"guard": {"$shared": "079efa16382b8700"}, "then": {"param": "household.no"}}
76d8d08528525241 [{"$shared": "352677350c6607b6"}, {"$shared": "47de1eaa2fb0dcc8"}]
ab1f23840d8dabf7 {"alternatives": {"$shared": "76d8d08528525241"}, "op": "choose"}
1b4e8f6d5f7b16d2 {"guard": {"$shared": "f899dd2da804e8d7"}, "then": {"$shared": "ab1f23840d8dabf7"}}
583faa4938ba2b2b [{"$shared": "b804482ee35038d6"}, {"$shared": "1b4e8f6d5f7b16d2"}]
2043697195d8db7a {"alternatives": {"$shared": "583faa4938ba2b2b"}, "op": "choose"}
8b7e494bd98e856b {"guard": {"$shared": "63b6c7aa24bca7a9"}, "then": {"$shared": "2043697195d8db7a"}}
b046b2fcc6e719ff [{"$shared": "725d681bbf866af6"}, {"$shared": "8b7e494bd98e856b"}]
3d7126ffd3118950 {"alternatives": {"$shared": "b046b2fcc6e719ff"}, "op": "choose"}
4e22b940e0f5cd75 {"guard": {"$shared": "0e836bee5ee949c8"}, "then": {"$shared": "3d7126ffd3118950"}}
3367aa13bcf230b6 [{"$shared": "7cd70b16f4cff8ee"}, {"$shared": "4e22b940e0f5cd75"}]
fc7596b76eb6578b {"alternatives": {"$shared": "3367aa13bcf230b6"}, "op": "choose"}
9c72a298f12c5e32 [{"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}]
dfe58c4e8e47a8d5 {"args": {"$shared": "9c72a298f12c5e32"}, "test": "all"}
42e234da23232c52 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}]
4e94f318a5bfe546 {"args": {"$shared": "42e234da23232c52"}, "test": "all"}
6ffafcc965368126 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}]
d970378acdded4c4 {"args": {"$shared": "6ffafcc965368126"}, "test": "all"}
ce1398ec8828bdaa {"args": [{"const": false}, {"input": "dependent.spouse_claims"}], "test": "ne"}
16f2ef0ded9edab2 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"$shared": "ce1398ec8828bdaa"}]
2c483ea3c2873d39 {"args": {"$shared": "16f2ef0ded9edab2"}, "test": "all"}
50cb2527df09a6fd {"args": [{"const": true}, {"input": "dependent.other_only_spouse"}], "test": "ne"}
a463660a1ca1edc6 [{"$shared": "2c483ea3c2873d39"}, {"$shared": "50cb2527df09a6fd"}]
a6d237f1b5fde1c8 {"args": {"$shared": "a463660a1ca1edc6"}, "test": "any"}
096f10caa47b5b8c {"args": [{"const": false}, {"input": "dependent.other_only_spouse"}], "test": "ne"}
ec039f25641db7e5 [{"$shared": "096f10caa47b5b8c"}, {"args": [{"const": true}, {"input": "dependent.filer_parent"}], "test": "ne"}]
c0423f26999a19e2 {"args": {"$shared": "ec039f25641db7e5"}, "test": "any"}
621f1cf2e59a5d98 {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}
74e4038d19cf5802 {"args": [{"const": true}, {"input": "dependent.other_nontaxpayer"}], "test": "ne"}
01dc3c8ecbe942bf [{"$shared": "a6d237f1b5fde1c8"}, {"$shared": "c0423f26999a19e2"}, {"$shared": "621f1cf2e59a5d98"}, {"$shared": "74e4038d19cf5802"}]
6dd9875a885c8e76 {"args": {"$shared": "01dc3c8ecbe942bf"}, "test": "all"}
312ad9161eeb8f6b [{"$shared": "6dd9875a885c8e76"}, {"$shared": "c3f47436dc98b30f"}]
516ab596982ec481 {"args": {"$shared": "312ad9161eeb8f6b"}, "test": "any"}
9aa80cb173938c68 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}]
622f481232897268 {"args": {"$shared": "9aa80cb173938c68"}, "test": "all"}
275fe334c8bcdd5f [{"$shared": "dfe58c4e8e47a8d5"}, {"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}]
4190821ec37110d1 {"args": {"$shared": "275fe334c8bcdd5f"}, "test": "all"}
0c269fa19c46c5ff {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}
80ff27f0aa663eb3 {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}
ba38f057728bc26c {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}
d60b81dfcb10f0cd [{"$shared": "61637c12d231a4af"}, {"$shared": "dbd8d147bac52913"}, {"$shared": "0c269fa19c46c5ff"}, {"$shared": "80ff27f0aa663eb3"}, {"$shared": "ba38f057728bc26c"}, {"$shared": "eb6b9c3b873c1d3b"}]
214586a8ff53516e {"args": {"$shared": "d60b81dfcb10f0cd"}, "test": "all"}
583f2d04a4f94db0 [{"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "ne"}]
5231667c4cc7b53c {"args": {"$shared": "583f2d04a4f94db0"}, "test": "any"}
f4c5aea6dc665ec2 {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}
95d8f723c04c0f60 [{"$shared": "214586a8ff53516e"}, {"$shared": "5231667c4cc7b53c"}, {"$shared": "f4c5aea6dc665ec2"}]
0aa027d14441d2bb {"args": {"$shared": "95d8f723c04c0f60"}, "test": "all"}
8e88e6b668564f1f {"args": [{"const": "unsure"}, {"input": "dependent.supported_view"}], "test": "ne"}
fb2e9f8e4293cda6 [{"$shared": "8e88e6b668564f1f"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}]
5c8093da182190a2 {"args": {"$shared": "fb2e9f8e4293cda6"}, "test": "any"}
f3c71a8f2a5390b3 {"args": [{"const": "over_half"}, {"input": "dependent.supported_view"}], "test": "ne"}
fb8605d4d7745be4 [{"$shared": "5c8093da182190a2"}, {"$shared": "f3c71a8f2a5390b3"}]
df716d0500c208d3 {"args": {"$shared": "fb8605d4d7745be4"}, "test": "all"}
7998acacca13874d [{"$shared": "621f1cf2e59a5d98"}, {"$shared": "74e4038d19cf5802"}]
6a48aff82efb9960 {"args": {"$shared": "7998acacca13874d"}, "test": "all"}
4a66812c6be68709 [{"$shared": "cdeef980fd44dad9"}, {"$shared": "6a48aff82efb9960"}]
4da3bb482d060efd {"args": {"$shared": "4a66812c6be68709"}, "test": "any"}
9789eb7c6080e028 [{"$shared": "0aa027d14441d2bb"}, {"$shared": "df716d0500c208d3"}, {"$shared": "4da3bb482d060efd"}]
2a66e24076dd011a {"args": {"$shared": "9789eb7c6080e028"}, "test": "any"}
fb6f6f74f85edbc4 [{"$shared": "2a66e24076dd011a"}, {"$shared": "f5726735e624cfd5"}]
379fb44b14b50161 {"args": {"$shared": "fb6f6f74f85edbc4"}, "test": "any"}
0600b5d4c80ba0f6 [{"$shared": "516ab596982ec481"}, {"$shared": "379fb44b14b50161"}]
98a6ab6b8e4f7517 {"args": {"$shared": "0600b5d4c80ba0f6"}, "test": "all"}
8a739fe3bea4abad [{"$shared": "4190821ec37110d1"}, {"$shared": "98a6ab6b8e4f7517"}]
aa0ba807de7a7a30 {"args": {"$shared": "8a739fe3bea4abad"}, "test": "any"}
728d4e67cfa35e10 [{"$shared": "622f481232897268"}, {"$shared": "aa0ba807de7a7a30"}]
eccaa1db5f6a2443 {"args": {"$shared": "728d4e67cfa35e10"}, "test": "any"}
bb4ff2cf1e5286e7 [{"$shared": "ac4b48c317adfa6c"}, {"const": 0, "type": "Count"}]
376b69af2e1fafab {"args": {"$shared": "bb4ff2cf1e5286e7"}, "test": "le"}
798a2b9fdc3c220e {"args": {"$shared": "3503b2668d859ed6"}, "test": "ne"}
f456402f77396702 [{"$shared": "376b69af2e1fafab"}, {"$shared": "798a2b9fdc3c220e"}]
39ef0fc4c27afcce {"args": {"$shared": "f456402f77396702"}, "test": "any"}
eab2650e117702f6 [{"$shared": "dfe58c4e8e47a8d5"}, {"$shared": "4e94f318a5bfe546"}, {"$shared": "d970378acdded4c4"}, {"$shared": "516ab596982ec481"}, {"$shared": "eccaa1db5f6a2443"}, {"$shared": "39ef0fc4c27afcce"}, {"$shared": "475a509e3d1380c7"}]
d39f6408cb402236 {"args": {"$shared": "eab2650e117702f6"}, "test": "any"}
b998e01c05226b1e [{"$shared": "17c073aa76ed8007"}, {"$shared": "d39f6408cb402236"}, {"$shared": "1fd77c3d63ad8b8e"}, {"$shared": "6f20306cdcff36df"}, {"$shared": "9ab757132a95133d"}]
d84abbef9543cefb {"args": {"$shared": "b998e01c05226b1e"}, "test": "all"}
c4cf55482c46be6c {"guard": {"$shared": "c2062ef24e1afd8f"}, "then": {"const": 0}}
bdca88e8ec20834e {"guard": {"$shared": "d39f6408cb402236"}, "then": {"const": 0}}
712d85b2e84d6696 {"args": {"$shared": "a2641fe84c411e26"}, "test": "ne"}
8e189786065546db {"guard": {"args": [{"const": true}, {"input": "dependent.ever_married"}], "test": "eq"}, "then": {"input": "dependent.married"}}
c0740862b989e912 [{"$shared": "84fd80eb66b34eb8"}, {"$shared": "8e189786065546db"}]
9e73fa29a3a9153e {"alternatives": {"$shared": "c0740862b989e912"}, "op": "choose"}
ccde53ef36d17372 [{"const": false}, {"$shared": "9e73fa29a3a9153e"}]
e5c553ad21855889 {"args": {"$shared": "ccde53ef36d17372"}, "test": "eq"}
598e1dc3af0f93fa [{"$shared": "e5c553ad21855889"}, {"$shared": "909848cd137657d6"}, {"$shared": "cb03c1e6c4c3bab4"}]
fe55e6678145ddca {"args": {"$shared": "598e1dc3af0f93fa"}, "test": "all"}
8cbf18d3ed3b3e52 [{"const": false}, {"$shared": "68017dd572aa517b"}]
770406361eb405a8 {"args": {"$shared": "8cbf18d3ed3b3e52"}, "test": "eq"}
dcbb9589c9785cc5 {"guard": {"args": [{"const": false}, {"input": "dependent.born_died"}], "test": "eq"}, "then": {"input": "dependent.placed"}}
0df91f5d997d1434 {"guard": {"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, "then": {"input": "dependent.born_died"}}
189a116d3cffb92b [{"$shared": "dcbb9589c9785cc5"}, {"$shared": "0df91f5d997d1434"}]
4a9f44e2239362c8 {"alternatives": {"$shared": "189a116d3cffb92b"}, "op": "choose"}
289a2b0a0877931f [{"const": false}, {"$shared": "4a9f44e2239362c8"}]
b14870e0c947b149 {"args": {"$shared": "289a2b0a0877931f"}, "test": "eq"}
c543559034658e9a {"guard": {"$shared": "b14870e0c947b149"}, "then": {"param": "household.no"}}
c0a74e9a5bc4ecc4 [{"const": true}, {"$shared": "4a9f44e2239362c8"}]
e182b95b28a4bf5a {"args": {"$shared": "c0a74e9a5bc4ecc4"}, "test": "eq"}
d679dd3ed1c7ecb6 {"guard": {"$shared": "e182b95b28a4bf5a"}, "then": {"input": "dependent.part_year_home"}}
3ff356c08bee1f47 [{"$shared": "c543559034658e9a"}, {"$shared": "d679dd3ed1c7ecb6"}]
46dd0611c9ae3cc3 {"alternatives": {"$shared": "3ff356c08bee1f47"}, "op": "choose"}
9a117da84a30caa5 {"guard": {"$shared": "726b909b48f9c541"}, "then": {"$shared": "46dd0611c9ae3cc3"}}
5fc91684ce4541c7 [{"$shared": "c7b89b2404b84b41"}, {"$shared": "9a117da84a30caa5"}]
6e3279cd396eb3cc {"alternatives": {"$shared": "5fc91684ce4541c7"}, "op": "choose"}
94c1771065fcd39f {"guard": {"$shared": "770406361eb405a8"}, "then": {"$shared": "6e3279cd396eb3cc"}}
c246dd924aef673f {"guard": {"$shared": "cb03c1e6c4c3bab4"}, "then": {"$shared": "68017dd572aa517b"}}
825ae8fbac3f8338 [{"$shared": "94c1771065fcd39f"}, {"$shared": "c246dd924aef673f"}]
2ce7f5fbe5723eef {"alternatives": {"$shared": "825ae8fbac3f8338"}, "op": "choose"}
f6f3ee391e049e06 [{"const": true}, {"$shared": "2ce7f5fbe5723eef"}]
3fa0c27493e1acc9 {"args": {"$shared": "f6f3ee391e049e06"}, "test": "eq"}
bd88e482830d2da2 {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}
d9eee7ca93f22c5f [{"$shared": "3fa0c27493e1acc9"}, {"$shared": "0e836bee5ee949c8"}, {"$shared": "f4c5aea6dc665ec2"}, {"$shared": "bd88e482830d2da2"}, {"$shared": "5090e2054156fd72"}]
93c1342988d79793 {"args": {"$shared": "d9eee7ca93f22c5f"}, "test": "all"}
186a3e1b0b0e47af [{"$shared": "fe55e6678145ddca"}, {"$shared": "93c1342988d79793"}]
b72d1660b2ed1520 {"args": {"$shared": "186a3e1b0b0e47af"}, "test": "any"}
87722dbfe6cea1e9 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}]
5a32eb26e872ff34 {"args": {"$shared": "87722dbfe6cea1e9"}, "test": "any"}
61276d911b7b575c [{"$shared": "5a32eb26e872ff34"}, {"$shared": "45b31d0efa71a78e"}]
fad782b1c0f89de1 {"args": {"$shared": "61276d911b7b575c"}, "test": "all"}
18eb08137572186e [{"$shared": "fad782b1c0f89de1"}, {"$shared": "da884a5a9bffad77"}]
2f7093f7d73aee4e {"args": {"$shared": "18eb08137572186e"}, "test": "any"}
b10b9cc6d7f96f87 [{"$shared": "45a2cd7f5e7f7f9f"}, {"$shared": "07ff44ec481e8052"}]
bac06bdd2e9c55ce {"args": {"$shared": "b10b9cc6d7f96f87"}, "test": "any"}
096c34dd22cda0c0 [{"$shared": "17c073aa76ed8007"}, {"$shared": "bac06bdd2e9c55ce"}]
ec235687478bbf83 {"args": {"$shared": "096c34dd22cda0c0"}, "test": "all"}
d4233adc6ed317d1 [{"$shared": "45a2cd7f5e7f7f9f"}, {"$shared": "eccaa1db5f6a2443"}]
fbc40741a7ddd33f {"args": {"$shared": "d4233adc6ed317d1"}, "test": "all"}
d0afd178ca374305 [{"$shared": "ec235687478bbf83"}, {"$shared": "fbc40741a7ddd33f"}]
5ce161e067bbeb7f {"args": {"$shared": "d0afd178ca374305"}, "test": "any"}
65bcf55411127020 {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}
1a4338467d54dec6 {"guard": {"$shared": "00efe0d5f3d5b9f2"}, "then": {"input": "dependent.us_half"}}
83f35ca7297a759d [{"$shared": "1a4338467d54dec6"}, {"$shared": "433fe18d3516aefb"}]
d32e97b448a107cc {"alternatives": {"$shared": "83f35ca7297a759d"}, "op": "choose"}
3ee66109c1dfdace {"guard": {"$shared": "a92529affa94912e"}, "then": {"$shared": "d32e97b448a107cc"}}
efda0b36dfe300b5 [{"$shared": "4c614b4955fbc2e4"}, {"$shared": "3ee66109c1dfdace"}]
adf57518a3c29ed3 {"alternatives": {"$shared": "efda0b36dfe300b5"}, "op": "choose"}
c2d47134a84a5e41 {"guard": {"$shared": "dfe671ee2eedd621"}, "then": {"$shared": "adf57518a3c29ed3"}}
b664c95d7bc4bdc7 [{"$shared": "2c4a6224f1abc300"}, {"$shared": "c2d47134a84a5e41"}]
53cc2a1fa9e0feac {"alternatives": {"$shared": "b664c95d7bc4bdc7"}, "op": "choose"}
7fa7f809880d82f8 [{"const": true}, {"$shared": "53cc2a1fa9e0feac"}]
4b25f00b24d0225a {"args": {"$shared": "7fa7f809880d82f8"}, "test": "eq"}
22969554639d5f7b [{"$shared": "c3cee0d9721af552"}, {"$shared": "aae5cb78c743225c"}, {"$shared": "dfe671ee2eedd621"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}]
e8f93269f6d04e24 {"args": {"$shared": "22969554639d5f7b"}, "test": "all"}
1dc0c64c3a6071c4 [{"$shared": "04706b205e474b59"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}]
c5e2d1b2441460aa {"args": {"$shared": "1dc0c64c3a6071c4"}, "test": "all"}
3c70303a2d0e4cb0 [{"$shared": "c5e2d1b2441460aa"}, {"args": [{"const": true}, {"input": "dependent.dc_under13"}], "test": "eq"}]
ce40836de784404d {"args": {"$shared": "3c70303a2d0e4cb0"}, "test": "all"}
681e349d0682fda7 [{"$shared": "4aae835f34adedb2"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}]
fe9734e3912d82f3 {"args": {"$shared": "681e349d0682fda7"}, "test": "all"}
35a28047ab391a26 [{"$shared": "04706b205e474b59"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "lt"}]
e662e1df06c8cf8a {"args": {"$shared": "35a28047ab391a26"}, "test": "all"}
4ab0553db1dcd0e6 [{"$shared": "ce40836de784404d"}, {"$shared": "fe9734e3912d82f3"}, {"$shared": "e662e1df06c8cf8a"}]
b80d786b1a8c7527 {"args": {"$shared": "4ab0553db1dcd0e6"}, "test": "any"}
ab0d08ae8369cca6 [{"$shared": "b80d786b1a8c7527"}, {"$shared": "0e836bee5ee949c8"}, {"args": [{"const": true}, {"ref": "f2441.care"}], "test": "eq"}]
44f668c74751fcb2 {"args": {"$shared": "ab0d08ae8369cca6"}, "test": "all"}
8d678eec54d07480 [{"args": [{"const": true}, {"input": "dependent.dc_under13"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}]
2ab913452348a2c5 {"args": {"$shared": "8d678eec54d07480"}, "test": "all"}
7d8a9efb1071bcd1 [{"$shared": "2ab913452348a2c5"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "lt"}]
f8784cea50608452 {"args": {"$shared": "7d8a9efb1071bcd1"}, "test": "any"}
e959004104dd5ccb [{"$shared": "17c073aa76ed8007"}, {"$shared": "45a2cd7f5e7f7f9f"}, {"$shared": "f8784cea50608452"}]
fd871b0ba2f73960 {"args": {"$shared": "e959004104dd5ccb"}, "test": "all"}
087958408ad074c8 [{"$shared": "a46d34c741c15e09"}, {"$shared": "45a2cd7f5e7f7f9f"}]
b3e03c3cb3b49cda {"args": {"$shared": "087958408ad074c8"}, "test": "any"}
66ee635b50135402 [{"$shared": "b3e03c3cb3b49cda"}, {"$shared": "d3c7eccf3db4c0cf"}]
701a833b3d7b4c84 {"args": {"$shared": "66ee635b50135402"}, "test": "all"}
9d7b8d4258e17173 [{"$shared": "701a833b3d7b4c84"}, {"$shared": "46b66a31fd3a3891"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}]
0e6ea44471693aa1 {"args": {"$shared": "9d7b8d4258e17173"}, "test": "all"}
33ffb889cf8ce791 [{"$shared": "fd871b0ba2f73960"}, {"$shared": "0e6ea44471693aa1"}]
0570779a7b59949e {"args": {"$shared": "33ffb889cf8ce791"}, "test": "any"}
363446df813d9ff2 {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "ne"}
37f6678bff8e7bc6 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "ne"}, {"$shared": "363446df813d9ff2"}]
cecce6ab0e8ea4c1 {"args": {"$shared": "37f6678bff8e7bc6"}, "test": "any"}
154dbc6f9edd32bc [{"$shared": "cecce6ab0e8ea4c1"}, {"$shared": "6b958588ce0c364c"}]
eae17f71d9814ab1 {"args": {"$shared": "154dbc6f9edd32bc"}, "test": "all"}
20e4e84fdc2d2fb2 [{"$shared": "2a66e24076dd011a"}, {"$shared": "516ab596982ec481"}]
f0c67ce019113f97 {"args": {"$shared": "20e4e84fdc2d2fb2"}, "test": "all"}
3a79d6c506baa5b5 [{"$shared": "4190821ec37110d1"}, {"$shared": "f0c67ce019113f97"}]
c641d66338bb2c0f {"args": {"$shared": "3a79d6c506baa5b5"}, "test": "any"}
4b96fb19fb19372f [{"$shared": "eae17f71d9814ab1"}, {"$shared": "c641d66338bb2c0f"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "ne"}]
aa7076552fb14768 {"args": {"$shared": "4b96fb19fb19372f"}, "test": "any"}
b79fdd45e73cdda7 [{"args": [{"const": true}, {"input": "dependent.dc_under13"}], "test": "ne"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "ne"}]
877751740ae5afb1 {"args": {"$shared": "b79fdd45e73cdda7"}, "test": "any"}
6e80eb1a95b57749 [{"$shared": "877751740ae5afb1"}, {"args": [{"param": "dc.child_age"}, {"input": "dependent.age"}], "test": "le"}]
7158eb3d4682bff6 {"args": {"$shared": "6e80eb1a95b57749"}, "test": "all"}
4768d0730554dfac [{"$shared": "7158eb3d4682bff6"}, {"$shared": "516ab596982ec481"}, {"$shared": "eccaa1db5f6a2443"}]
78fcc5a7ae676cb2 {"args": {"$shared": "4768d0730554dfac"}, "test": "any"}
a694804dc4771044 [{"$shared": "aa7076552fb14768"}, {"$shared": "78fcc5a7ae676cb2"}]
20b3bcd40ee2b7fc {"args": {"$shared": "a694804dc4771044"}, "test": "all"}
c8cb73b986218afe {"guard": {"$shared": "20b3bcd40ee2b7fc"}, "then": {"const": 0}}
49ba61210109901e {"args": [{"const": true}, {"input": "dependent.dc_over12_care"}], "test": "eq"}
ff7152b9011d2a4a {"guard": {"args": [{"const": false}, {"ref": "f8863.paid"}], "test": "eq"}, "then": {"param": "edu.no"}}
c0f0c4c159ffea2d {"guard": {"$shared": "3f8a693dbfd55cbd"}, "then": {"param": "edu.no"}}
541da454340c6b75 {"guard": {"args": [{"const": false}, {"input": "dependent.edu"}], "test": "eq"}, "then": {"param": "edu.no"}}
6f3db53061fa74ce {"guard": {"args": [{"const": false}, {"input": "dependent.tin"}], "test": "eq"}, "then": {"param": "edu.no"}}
83a92c5b4cd6064c {"guard": {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, "then": {"input": "dependent.edu_1098t"}}
678479682f911276 [{"$shared": "6f3db53061fa74ce"}, {"$shared": "83a92c5b4cd6064c"}]
d0a43fb1b7c454b8 {"alternatives": {"$shared": "678479682f911276"}, "op": "choose"}
6f0e1f879ef64417 {"guard": {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "eq"}, "then": {"$shared": "d0a43fb1b7c454b8"}}
78879181dc366173 [{"$shared": "541da454340c6b75"}, {"$shared": "6f0e1f879ef64417"}]
227d941d24467b19 {"alternatives": {"$shared": "78879181dc366173"}, "op": "choose"}
c3339fdeb49ab4cc {"guard": {"$shared": "0e836bee5ee949c8"}, "then": {"$shared": "227d941d24467b19"}}
aa80624174dc5774 [{"$shared": "c0f0c4c159ffea2d"}, {"$shared": "c3339fdeb49ab4cc"}]
505f0d62391b09a2 {"alternatives": {"$shared": "aa80624174dc5774"}, "op": "choose"}
8ca908b86de4833b {"guard": {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}, "then": {"$shared": "505f0d62391b09a2"}}
f1a209978104c474 [{"$shared": "ff7152b9011d2a4a"}, {"$shared": "8ca908b86de4833b"}]
72503d59e1ee1a57 {"alternatives": {"$shared": "f1a209978104c474"}, "op": "choose"}
f6b29e7badd1aa9e [{"const": false}, {"$shared": "72503d59e1ee1a57"}]
899b721b35defc1c {"args": {"$shared": "f6b29e7badd1aa9e"}, "test": "eq"}
646177249adbb276 {"guard": {"$shared": "899b721b35defc1c"}, "then": {"param": "edu.no"}}
7c20e4ec7290e322 [{"const": true}, {"$shared": "72503d59e1ee1a57"}]
e22a9e36be873a00 {"args": {"$shared": "7c20e4ec7290e322"}, "test": "eq"}
4e1bcf613a6592d7 {"guard": {"args": [{"const": false}, {"line": "24"}], "test": "eq"}, "then": {"param": "edu.no"}}
f98cf9d779212336 {"guard": {"$shared": "9ab757132a95133d"}, "then": {"input": "dependent.edu_ein"}}
9bb64406bc44fd23 {"guard": {"$shared": "712d85b2e84d6696"}, "then": {"param": "edu.no"}}
46a474cbeec6cc85 [{"$shared": "f98cf9d779212336"}, {"$shared": "9bb64406bc44fd23"}]
cce73ed6f220d583 {"alternatives": {"$shared": "46a474cbeec6cc85"}, "op": "choose"}
e0cfc42d87a8efc5 {"guard": {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, "then": {"$shared": "cce73ed6f220d583"}}
363b4631d066f43b {"guard": {"args": [{"const": true}, {"line": "26"}], "test": "eq"}, "then": {"param": "edu.no"}}
2dd8e56c0f458f5b [{"$shared": "e0cfc42d87a8efc5"}, {"$shared": "363b4631d066f43b"}]
a086bdc8ed7fdd60 {"alternatives": {"$shared": "2dd8e56c0f458f5b"}, "op": "choose"}
ee8dd1cdcbfa5dcd {"guard": {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, "then": {"$shared": "a086bdc8ed7fdd60"}}
841394248ef0fdc9 {"guard": {"args": [{"const": true}, {"line": "25"}], "test": "eq"}, "then": {"param": "edu.no"}}
1c39724bd0ce858f [{"$shared": "ee8dd1cdcbfa5dcd"}, {"$shared": "841394248ef0fdc9"}]
bbf2c43547fb89a2 {"alternatives": {"$shared": "1c39724bd0ce858f"}, "op": "choose"}
2f9ff891d5c54084 {"guard": {"args": [{"const": true}, {"line": "24"}], "test": "eq"}, "then": {"$shared": "bbf2c43547fb89a2"}}
a2372991f98438f8 [{"$shared": "4e1bcf613a6592d7"}, {"$shared": "2f9ff891d5c54084"}]
fe765bbcecf6c2f7 {"alternatives": {"$shared": "a2372991f98438f8"}, "op": "choose"}
c6bcc0d89ff1720b {"guard": {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, "then": {"$shared": "fe765bbcecf6c2f7"}}
9dd74373b7e8d361 {"guard": {"args": [{"const": true}, {"line": "23"}], "test": "eq"}, "then": {"param": "edu.no"}}
9b110ab6108b865d [{"$shared": "c6bcc0d89ff1720b"}, {"$shared": "9dd74373b7e8d361"}]
b3c9320de87ab6db {"alternatives": {"$shared": "9b110ab6108b865d"}, "op": "choose"}
07155162e70a8682 {"guard": {"$shared": "e22a9e36be873a00"}, "then": {"$shared": "b3c9320de87ab6db"}}
a89aca3c036ffc27 [{"$shared": "646177249adbb276"}, {"$shared": "07155162e70a8682"}]
593e869d1fe4ad33 {"alternatives": {"$shared": "a89aca3c036ffc27"}, "op": "choose"}
3b3674044e632b92 [{"const": false}, {"$shared": "593e869d1fe4ad33"}]
0a77e89c3998d821 {"args": {"$shared": "3b3674044e632b92"}, "test": "eq"}
d1808d87c502bc72 {"guard": {"$shared": "0a77e89c3998d821"}, "then": {"const": 0}}
6ed94b865c34a7b2 [{"const": true}, {"$shared": "593e869d1fe4ad33"}]
21147f40fd2ff75a {"args": {"$shared": "6ed94b865c34a7b2"}, "test": "eq"}
e2187f51feaa0c68 {"of": [{"input": "dependent.edu_inst"}, {"input": "dependent.edu_mat"}], "op": "sum"}
d7f7169fe5412fb6 {"guard": {"$shared": "899b721b35defc1c"}, "then": {"const": 0}}
58614b8ab412763f [{"input": "dependent.edu_a_next_year"}, {"input": "dependent.edu_a_this_year"}, {"input": "dependent.edu_refunds"}]
60a124017e8fbd31 {"of": {"$shared": "58614b8ab412763f"}, "op": "sum"}
51bf74b16ff4adec {"guard": {"$shared": "e22a9e36be873a00"}, "then": {"$shared": "60a124017e8fbd31"}}
76404fbe7159b883 [{"$shared": "d7f7169fe5412fb6"}, {"$shared": "51bf74b16ff4adec"}]
2787d74fabba21e1 {"alternatives": {"$shared": "76404fbe7159b883"}, "op": "choose"}
3ef8ca0561c95442 {"from": {"$shared": "e2187f51feaa0c68"}, "op": "subtract_floor0", "take": {"$shared": "2787d74fabba21e1"}}
d4c9077b9b57f5a4 [{"$shared": "3ef8ca0561c95442"}, {"param": "aoc.expense_cap"}]
9d5c34fcba6bddb8 {"of": {"$shared": "d4c9077b9b57f5a4"}, "op": "smaller_of"}
75ff791dd1a5e24b {"args": [{"const": true}, {"input": "dependent.edu_tin_issued"}], "test": "eq"}
5310b12a261b938d [{"$shared": "17c073aa76ed8007"}, {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.edu_1098t"}], "test": "eq"}, {"$shared": "75ff791dd1a5e24b"}]
7de8c1119481c95f {"args": {"$shared": "5310b12a261b938d"}, "test": "all"}
ec9f8653ce205343 [{"$shared": "7de8c1119481c95f"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}]
3562882b0fd49dab {"args": {"$shared": "ec9f8653ce205343"}, "test": "all"}
be61e1100dccc68c {"args": [{"const": true}, {"input": "dependent.edu_tin_issued"}], "test": "ne"}
0ab9f40f9b078da5 [{"$shared": "eccaa1db5f6a2443"}, {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.edu_1098t"}], "test": "ne"}, {"$shared": "be61e1100dccc68c"}]
643c616e134e2878 {"args": {"$shared": "0ab9f40f9b078da5"}, "test": "any"}
d6c0406ea0c2082f [{"$shared": "643c616e134e2878"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}]
80564d9f7b2b8617 {"args": {"$shared": "d6c0406ea0c2082f"}, "test": "any"}
cd2c266b576ff107 {"from": {"$shared": "9d5c34fcba6bddb8"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}
3672e84b32d30cca {"amount": {"$shared": "cd2c266b576ff107"}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}
9c62a754eda4ada1 [{"const": 0}, {"$shared": "cd2c266b576ff107"}]
<!-- end -->
