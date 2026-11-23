# Review record ed78fa6fd08b — transcription dependent

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
 "prompt_sha256": "ee20c7d13f1f31d2a47e0a98fef394ea104127c3a358998735036aff6bef8d76",
 "response_sha256": "ae78ece9bf4a31e92c5782e9391d88cc0504287b4fa1699f98c687ca15464234",
 "scope": "whole",
 "subjects": {
  "2(c)": "659e4b84f16739e939222794f60042816ad19e6b6e6685a05766cfa26f1bdda5",
  "2(d)": "9b0171c01f5ed0ddc1b455a58945bc7da26ff4a1b8f7fb6a45028db1bc1b963f",
  "27": "b7876860c106e824f97a02fb3e36f2fb913237d0a718fbec13ab192086eda42e",
  "28": "f2396bf870a626e2ffe01dae9539d9bd9757c1fb19ec93e69cfc3eea1fe6e209",
  "29": "85d9367a84c303a1d1b37f85d56e020c9ff9d33a0e703e4a70a93fe89c9f77e2",
  "30": "8df6f4b83424fa74abb5701b11531976cd84950e2adfd2ddd7d0e70daadec1dd",
  "31": "be48f65942e0d7d4def928d0bbc79533e6bb1636ad585bb9059a535d609857b5",
  "dependent.actc_amount": "75827a3c80fddf6f929aba2fd1f995d6ad72acfd6e03f0547e135b47f88bce96",
  "dependent.child_all_year": "a8a372e104187c679558a4b763ba9f6c79c85421eaf4529497bb75071f51cb54",
  "dependent.claimed": "c0bc2b3e50be2353e052ada12c4060559ec3433e52708f34bd7381cc7123c4d7",
  "dependent.ctc_amount": "9aa79f6af499104284e5f90476522a7fdc96ea219af6f8e17ff92e3c562abb63",
  "dependent.ctc_child": "4c27a6255c0d31ff716fd0abf6efee2eafb65ebf6cb930e6dbdde0f343df7338",
  "dependent.dc_count": "6e8b475ab185eebd8f897a7b2cceeb2d4e5cd73e196df35ea0733c70f0d819bd",
  "dependent.dc_lived_half": "a036957b722b993a839671d90e9862f346f80b9e77cc96aae9de42ded1e7ca54",
  "dependent.dc_qp": "38449a1a4f135d061bb01c785d09028f46ddbe3a23c85b0d075037d2ef0cfde9",
  "dependent.eic_child": "cbc8d4ca266384d8494eddf5ba5c666041f80e718781a5aaf2cd87b7b649404d",
  "dependent.eic_ssn_child": "354f858a488b4e4281890aafc258b74046c72529eeb13d3abe3f6d8e8994899e",
  "dependent.hoh_absence": "1c380595eb2b5d7e956398d95e4c43aa1d8d07a703d709c5f17979aff8a709e9",
  "dependent.hoh_test1": "1c432e26e5784a988c8ba3db008eff336ad59e4b50b2c1ad5ec1638d12e6f7e3",
  "dependent.hoh_test2": "c2146722874e3e52dfe03cfd4d01ffe2e94a886c8eb3770e6e185498bcb97b0d",
  "dependent.hoh_test2_lived": "96ca592acb766d9f38d4dbb8c9f1ae6d2741c2aac72a3748c752c682736f9d9b",
  "dependent.odc_amount": "55132e69773ce56ad4c892d753e2994f8f954d03a6aa8506f083fe1ecc1e1ccd",
  "dependent.odc_person": "44e2b6851ec9b668d3c3ee484e0f1272ac89849b003f29ab0f92278f833f81ab",
  "dependent.one": "858660bbf031f30a7be0943c8d565dfd22a05dfea0dff850664c1d7d444819a0",
  "dependent.ptc_magi_counted": "36df5490d8f688e7658883a287843703bab79f3f934b09b65ce08c22d8b425d8"
 }
}
```

<!-- part head -->
# Transcription agreement — dependent

Second transcription of `Dependents — qualifying child and qualifying relative tests, per person listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/dependent.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-23 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ee20c7d13f1f31d2a47e0a98fef394ea104127c3a358998735036aff6bef8d76 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 258f571aae5fe4efacdb36d4c6abff9fe253bf1e3126d44cc96d88cb8fa56e50 |
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
| subject sha256 | b1ce0b956fafcba55e2eb266906224f0b2baba2912f179e354b692d253dbddc1 |
| printed lines compared | 25 |
| agree / disagree / missing | 1 / 24 / 0 |
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
{"$shared": "f492ba63b9db5ab2"}
```

Second:

```json
{"$shared": "fd19247f4fee5692"}
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
{"$shared": "ffef0ab2d2add02c"}
```

Second transcription's note: Step 3, question 4 also requires you (or your spouse if filing jointly) to have an SSN valid for employment; read from household.ctc_ssn, taken to be that return-level condition.

Ruling: open

<!-- part section dependent.odc_person -->
dependent.odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **DISAGREE**

Project:

```json
{"$shared": "4011368a4d2e25ac"}
```

Second:

```json
{"$shared": "7cb1ce2222758717"}
```

Second transcription's note: Step 5, question 1 (you, and your spouse if filing jointly, have an SSN or ITIN by the due date) is read from household.all_tin, taken to be that return-level condition.

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
{"alternatives": [{"guard": {"$shared": "ffef0ab2d2add02c"}, "then": {"param": "ctc.per_child"}}, {"$shared": "1a2e562b9f40b554"}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.odc_amount -->
dependent.odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"$shared": "4011368a4d2e25ac"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"$shared": "4011368a4d2e25ac"}], "test": "eq"}, "then": {"param": "odc.per_dependent"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "7cb1ce2222758717"}, "then": {"param": "odc.per_dependent"}}, {"guard": {"args": [{"$shared": "ffef0ab2d2add02c"}, {"$shared": "d590ca39f5be6faa"}, {"$shared": "dfe58c4e8e47a8d5"}, {"$shared": "4e94f318a5bfe546"}, {"$shared": "712d85b2e84d6696"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
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
{"alternatives": [{"guard": {"$shared": "ffef0ab2d2add02c"}, "then": {"param": "actc.per_child"}}, {"$shared": "1a2e562b9f40b554"}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.hoh_test2_lived -->
dependent.hoh_test2_lived — A Test 2 person who lived with you more than half the year, or of the part of the year a r
Status: **DISAGREE**

Project:

```json
{"$shared": "74fd8f16b18bb4f2"}
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
{"alternatives": [{"guard": {"args": [{"args": [{"$shared": "496a1e5bc5a2855e"}, {"$shared": "9b04e8f56ed52305"}, {"$shared": "fb503e6d1d9918ed"}, {"args": {"$shared": "f6f3ee391e049e06"}, "test": "ne"}, {"args": {"$shared": "7949240bec5d163a"}, "test": "ne"}], "test": "any"}, {"args": [{"args": {"$shared": "ccde53ef36d17372"}, "test": "ne"}, {"$shared": "726b909b48f9c541"}, {"args": {"$shared": "6377ef03fa616477"}, "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"param": "household.no"}}, {"guard": {"$shared": "74fd8f16b18bb4f2"}, "then": {"input": "dependent.absence_no_return"}}], "op": "choose"}
```

Second:

```json
{"args": [{"$shared": "678fadf37507fe61"}, {"args": [{"const": true}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Pub. 501: temporary absences count only if it is reasonable to assume the person will return and you keep up the home. This flags such a person; the return-level head of household gate decides what to do with it.

Ruling: open

<!-- part section dependent.hoh_test2 -->
dependent.hoh_test2 — A Test 2 person who lived with you more than half the year, or of the part of the year a r
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "74fd8f16b18bb4f2"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"$shared": "678fadf37507fe61"}
```

Ruling: open

<!-- part section dependent.hoh_test1 -->
dependent.hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "cae21fd21ef95261"}, {"$shared": "65bcf55411127020"}, {"$shared": "304992367f5da773"}], "test": "all"}
```

Second:

```json
{"args": [{"$shared": "fd19247f4fee5692"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "65bcf55411127020"}], "test": "all"}
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
{"$shared": "ceafbfd6623775f4"}
```

Second:

```json
{"$shared": "fca3c3a458708262"}
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
{"cap": 100, "op": "percent_floor", "part": {"alternatives": [{"$shared": "36461792c70c4fb8"}, {"guard": {"$shared": "fca3c3a458708262"}, "then": {"const": 1}}], "op": "choose"}, "whole": {"param": "sc.hundred_cents"}}
```

Second transcription's note: 1 cent over 100 cents as a whole percentage gives 1; zero gives 0.

Ruling: open

<!-- part section dependent.ptc_magi_counted -->
dependent.ptc_magi_counted — This dependent's modified AGI counted in household income (zero unless required to file be
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"$shared": "efa039d59e86b80f"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"$shared": "efa039d59e86b80f"}], "test": "eq"}, "then": {"input": "dependent.ptc_magi"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "fd19247f4fee5692"}, {"args": [{"const": true}, {"input": "dependent.ptc_files"}], "test": "eq"}], "test": "all"}, "then": {"input": "dependent.ptc_magi"}}, {"guard": {"args": [{"$shared": "d590ca39f5be6faa"}, {"args": [{"const": true}, {"input": "dependent.ptc_files"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

<!-- part section dependent.child_all_year -->
dependent.child_all_year — Listed as your child, and lived with you for all of 2025 (the lived-all-year answer is rea
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "496a1e5bc5a2855e"}, {"$shared": "a10e36b275ccac18"}, {"$shared": "9b04e8f56ed52305"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "475db94656536733"}, {"$shared": "b97208e9b0a8586c"}, {"$shared": "fb503e6d1d9918ed"}], "test": "any"}, "then": {"param": "household.no"}}, {"guard": {"$shared": "cb88768b40471aff"}, "then": {"input": "dependent.lived_all_year"}}], "op": "choose"}
```

Second:

```json
{"args": [{"$shared": "cb88768b40471aff"}, {"$shared": "f668a52c8c67c388"}], "test": "all"}
```

Second transcription's note: Interface meaning inferred from the qualifying surviving spouse test 3 (a child who lived in your home for all of 2025). The child enum also covers foster children and descendants, which that test excludes; the return-level test is left to handle that.

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
{"alternatives": [{"$shared": "36461792c70c4fb8"}, {"guard": {"$shared": "fca3c3a458708262"}, "then": {"input": "dependent.dc_paid"}}], "op": "choose"}
```

Ruling: open

<!-- part section 2(c) -->
2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **DISAGREE**

Project:

```json
{"args": [{"$shared": "ceafbfd6623775f4"}, {"$shared": "5411e1ffa263fe04"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"$shared": "fca3c3a458708262"}, {"$shared": "5411e1ffa263fe04"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}], "test": "all"}
```

Ruling: open

<!-- part section 27 -->
27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "bb763fb5bb43315e"}, {"guard": {"$shared": "4ed192eea3d369dd"}, "then": {"$shared": "e9977107c62432dc"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"$shared": "d78ee4e4ba19d64b"}, "then": {"of": [{"from": {"$shared": "e2187f51feaa0c68"}, "op": "subtract_floor0", "take": {"$shared": "60a124017e8fbd31"}}, {"param": "aoc.expense_cap"}], "op": "smaller_of"}}, {"guard": {"$shared": "9b9de7014713a49d"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open

<!-- part section 28 -->
28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"$shared": "bb763fb5bb43315e"}, {"guard": {"$shared": "4ed192eea3d369dd"}, "then": {"$shared": "d1c097257d730ccd"}}], "op": "choose"}
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
{"alternatives": [{"$shared": "bb763fb5bb43315e"}, {"guard": {"$shared": "4ed192eea3d369dd"}, "then": {"$shared": "e6e4eeb660c6a99e"}}], "op": "choose"}
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
{"alternatives": [{"$shared": "bb763fb5bb43315e"}, {"guard": {"$shared": "4ed192eea3d369dd"}, "then": {"alternatives": [{"guard": {"args": {"$shared": "0f4c5346ced7745e"}, "test": "eq"}, "then": {"$shared": "e9977107c62432dc"}}, {"guard": {"args": {"$shared": "0f4c5346ced7745e"}, "test": "ne"}, "then": {"of": [{"$shared": "e6e4eeb660c6a99e"}, {"param": "aoc.full_band"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
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
{"alternatives": [{"guard": {"args": [{"$shared": "2070ed8ab3ddf5f8"}, {"$shared": "8469264f1c6c75ff"}], "test": "all"}, "then": {"from": {"input": "dependent.edu_inst"}, "op": "subtract_floor0", "take": {"$shared": "969c91f05b577996"}}}, {"guard": {"args": [{"args": {"$shared": "0299a5a9032e5318"}, "test": "ne"}, {"args": {"$shared": "03e58e98daf82025"}, "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"$shared": "6a3182f53cb6c109"}, {"$shared": "9b9de7014713a49d"}], "test": "all"}, "then": {"from": {"input": "dependent.edu_inst"}, "op": "subtract_floor0", "take": {"$shared": "60a124017e8fbd31"}}}, {"guard": {"args": [{"$shared": "d78ee4e4ba19d64b"}, {"$shared": "9333ffdf81639789"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
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
| 27 | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married |
<!-- part gate 28 -->
| 28 | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married |
<!-- part gate 29 -->
| 29 | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married |
<!-- part gate 30 -->
| 30 | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married |
<!-- part gate 31 -->
| 31 | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married, dependent.multiple_support | dependent.divorced_rule, dependent.h_edu_over_gate, dependent.married |
<!-- part raw -->

## Raw second transcription

```yaml
```yaml
lines:
  - id: dependent.one
    printed: "(helper)"
    label: "One (this person, counted once)"
    type: Count
    expr: {op: param, ref: dependent.one}

  - id: dependent.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: dependent.h_cent
    printed: "(helper)"
    label: "One cent (used to count this person once)"
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

  - id: dependent.h_age_test
    printed: "(helper)"
    label: "Under age 19 and younger than you (or your spouse if filing jointly); or under age 24, a full-time student and younger; or any age and permanently and totally disabled"
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

  - id: dependent.h_not_self_support
    printed: "(helper)"
    label: "Who didn't provide over half of their own support for 2025"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.own_money, {const: false}]}
        - {op: test, eq: [dependent.self_support_view, {const: "under_half"}]}
        - op: test
          all:
            - {op: test, eq: [dependent.self_support_view, {const: "unsure"}]}
            - {op: test, eq: [dependent.self_support, {const: false}]}

  - id: dependent.h_lived_half
    printed: "(helper)"
    label: "Who lived with you for more than half of 2025"
    type: Bool
    expr: {op: test, ge: [dependent.months, {const: 7, type: Count}]}
    note: "The months answer already applies the exceptions to time lived with you for a person who meets the other qualifying-child conditions. The kidnapped-child rule of Pub. 501 is not computed: time missing because of a kidnapping is not counted, as the months question says."

  - id: dependent.h_qc_tests
    printed: "(helper)"
    label: "Meets the conditions to be your qualifying child (Step 1)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_rel_qc, {const: true}]}
        - {op: test, eq: [dependent.h_age_test, {const: true}]}
        - {op: test, eq: [dependent.h_not_self_support, {const: true}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
        - {op: test, eq: [dependent.h_lived_half, {const: true}]}

  - id: dependent.h_tiebreak_ok
    printed: "(helper)"
    label: "Qualifying child of more than one person: you can treat the child as your qualifying child"
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
    note: "The tiebreaker rules turn on parenthood, time lived and AGI, which are not all asked. Chosen reading: the child is yours when no one else can claim it, every other claimant is not a taxpayer, the only other claimant is your spouse and you file jointly or your spouse does not claim the child, or you are the child's parent (a parent is preferred to a non-parent). The case of another parent, not your spouse, who also claims the child is not resolved by these inputs."

  - id: dependent.h_qc
    printed: "(helper)"
    label: "Your qualifying child after the rules for a qualifying child of more than one person"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_tests, {const: true}]}
        - {op: test, eq: [dependent.h_tiebreak_ok, {const: true}]}

  - id: dependent.h_citizen_us
    printed: "(helper)"
    label: "Was a U.S. citizen, U.S. national, or U.S. resident alien"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.citizen, {const: true}]}

  - id: dependent.h_citizen_any
    printed: "(helper)"
    label: "Was a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_citizen_us, {const: true}]}
        - {op: test, eq: [dependent.canada_mexico, {const: true}]}

  - id: dependent.h_tin
    printed: "(helper)"
    label: "Had an SSN, ITIN, or ATIN issued (or applied for) on or before the due date of your return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.tin, {const: true}]}

  - id: dependent.h_work_ssn
    printed: "(helper)"
    label: "Had an SSN valid for employment and issued before the due date of your 2025 return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
        - {op: test, eq: [dependent.work_ssn, {const: true}]}

  - id: dependent.h_filer_ok
    printed: "(helper)"
    label: "You are filing a joint return, or you could not be claimed as a dependent on someone else's 2025 return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [sa.dependent, {const: false}]}

  - id: dependent.h_qc_base
    printed: "(helper)"
    label: "Your qualifying child who meets the citizen or resident test (Step 2, question 1)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc, {const: true}]}
        - {op: test, eq: [dependent.h_citizen_any, {const: true}]}

  - id: dependent.h_claimed_qc
    printed: "(helper)"
    label: "You can claim this qualifying child as a dependent (Step 2)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_base, {const: true}]}
        - {op: test, eq: [dependent.h_filer_ok, {const: true}]}

  - id: dependent.h_rel_close
    printed: "(helper)"
    label: "Related to you (or, on a joint return, your spouse) in a way that doesn't require living with you all year"
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

  - id: dependent.h_rel_qr
    printed: "(helper)"
    label: "Member of household or relationship test (Step 4)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_rel_close, {const: true}]}
        - {op: test, eq: [dependent.relationship, {const: "household_member"}]}
        - op: test
          all:
            - {op: test, eq: [dependent.qr_all_year, {const: true}]}
            - {op: test, eq: [dependent.lawful, {const: true}]}
    note: "household_member is defined in the relationship question as a person who lived with you all year in a relationship that did not violate local law, so it is taken as meeting this test without the separate questions."

  - id: dependent.h_qr_not_qc
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

  - id: dependent.h_income
    printed: "(helper)"
    label: "Who had gross income of less than $5,200 in 2025"
    type: Bool
    expr: {op: test, lt: [dependent.gross_income, {param: qr.gross_income_limit}]}
    note: "The sheltered-workshop exception to the gross income test is not computed."

  - id: dependent.h_qr_core
    printed: "(helper)"
    label: "Qualifying relative tests other than gross income, with the citizen or resident test"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_rel_qr, {const: true}]}
        - {op: test, eq: [dependent.h_qr_not_qc, {const: true}]}
        - {op: test, eq: [dependent.h_supported, {const: true}]}
        - {op: test, eq: [dependent.h_citizen_any, {const: true}]}

  - id: dependent.h_claimed_qr
    printed: "(helper)"
    label: "You can claim this qualifying relative as a dependent (Step 4)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qr_core, {const: true}]}
        - {op: test, eq: [dependent.h_income, {const: true}]}
        - {op: test, eq: [dependent.h_filer_ok, {const: true}]}

  - id: dependent.claimed
    printed: "(helper)"
    label: "You can claim this person as a dependent"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_claimed_qc, {const: true}]}
        - {op: test, eq: [dependent.h_claimed_qr, {const: true}]}
    refuses: [dependent.divorced_rule, dependent.married, dependent.multiple_support]

  - id: dependent.ctc_child
    printed: "(helper)"
    label: "Qualifying child for the child tax credit (Step 3)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.h_claimed_qc, {const: true}]}
        - {op: test, eq: [dependent.h_tin, {const: true}]}
        - {op: test, eq: [dependent.h_citizen_us, {const: true}]}
        - {op: test, lt: [dependent.age, {param: ctc.age_limit}]}
        - {op: test, eq: [dependent.h_work_ssn, {const: true}]}
        - {op: test, eq: [household.ctc_ssn, {const: true}]}
    note: "Step 3, question 4 also requires you (or your spouse if filing jointly) to have an SSN valid for employment; read from household.ctc_ssn, taken to be that return-level condition."

  - id: dependent.odc_person
    printed: "(helper)"
    label: "Dependent for whom you can claim the credit for other dependents (Steps 3 and 5)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.h_tin, {const: true}]}
        - {op: test, eq: [dependent.h_citizen_us, {const: true}]}
        - {op: test, eq: [household.all_tin, {const: true}]}
        - {op: test, eq: [dependent.ctc_child, {const: false}]}
    note: "Step 5, question 1 (you, and your spouse if filing jointly, have an SSN or ITIN by the due date) is read from household.all_tin, taken to be that return-level condition."

  - id: dependent.h_ctc_per
    printed: "(helper)"
    label: "$2,200 per qualifying child"
    type: NonNegDollars
    expr: {op: param, ref: ctc.per_child}

  - id: dependent.ctc_amount
    printed: "(helper)"
    label: "Child tax credit amount for this child (Schedule 8812, line 5 share)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_ctc_per}
        - {guard: {op: test, eq: [dependent.ctc_child, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_odc_per
    printed: "(helper)"
    label: "$500 per other dependent"
    type: NonNegDollars
    expr: {op: param, ref: odc.per_dependent}

  - id: dependent.odc_amount
    printed: "(helper)"
    label: "Credit for other dependents amount for this person (Schedule 8812, line 7 share)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.odc_person, {const: true}]}, then: dependent.h_odc_per}
        - {guard: {op: test, eq: [dependent.odc_person, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_actc_per
    printed: "(helper)"
    label: "$1,700 per qualifying child"
    type: NonNegDollars
    expr: {op: param, ref: actc.per_child}

  - id: dependent.actc_amount
    printed: "(helper)"
    label: "Additional child tax credit limit for this child (Schedule 8812, line 16b share)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_actc_per}
        - {guard: {op: test, eq: [dependent.ctc_child, {const: false}]}, then: dependent.h_zero}

  - id: dependent.hoh_test1
    printed: "(helper)"
    label: "Test 1: you paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.relationship, {const: "parent"}]}
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.parent_home_paid, {const: true}]}

  - id: dependent.h_hoh_person
    printed: "(helper)"
    label: "Test 2 person: a dependent (not one only because the person lived with you all year), or your unmarried qualifying child who isn't your dependent"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_qc, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [dependent.h_claimed_qr, {const: true}]}
            - {op: test, eq: [dependent.h_rel_close, {const: true}]}
    note: "Married persons, multiple support and the rule for children of divorced or separated parents are refused, so items 3 and 4 of Test 2 and the multiple-support exclusion are not computed."

  - id: dependent.hoh_test2_lived
    printed: "(helper)"
    label: "Lived with you for more than half of the year (with the exceptions to time lived with you)"
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

  - id: dependent.hoh_test2
    printed: "(helper)"
    label: "Test 2: a qualifying person who lived in your home for more than half of the year"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_hoh_person, {const: true}]}
        - {op: test, eq: [dependent.hoh_test2_lived, {const: true}]}
    refuses: [dependent.divorced_rule, dependent.married, dependent.multiple_support]

  - id: dependent.hoh_absence
    printed: "(helper)"
    label: "Test 2 person whose time lived with you counts an absence from which return was not reasonable to assume or during which the home was not kept up"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.hoh_test2, {const: true}]}
        - {op: test, eq: [dependent.absence_no_return, {const: true}]}
    note: "Pub. 501: temporary absences count only if it is reasonable to assume the person will return and you keep up the home. This flags such a person; the return-level head of household gate decides what to do with it."

  - id: dependent.child_all_year
    printed: "(helper)"
    label: "Your child who lived in your home for all of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.relationship, {const: "child"}]}
        - {op: test, eq: [dependent.lived_all_year, {const: true}]}
    note: "Interface meaning inferred from the qualifying surviving spouse test 3 (a child who lived in your home for all of 2025). The child enum also covers foster children and descendants, which that test excludes; the return-level test is left to handle that."

  - id: dependent.eic_child
    printed: "(helper)"
    label: "Qualifying child for the EIC (Step 3)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_rel_qc, {const: true}]}
        - {op: test, eq: [dependent.h_age_test, {const: true}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
        - {op: test, eq: [dependent.us_half, {const: true}]}
        - {op: test, eq: [dependent.h_tiebreak_ok, {const: true}]}
    refuses: [dependent.divorced_rule, dependent.married]

  - id: dependent.eic_ssn_child
    printed: "(helper)"
    label: "Qualifying child for the EIC who has a valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.eic_child, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [dependent.citizen_ssn, {const: true}]}
            - {op: test, eq: [dependent.eic_ssn, {const: true}]}

  - id: dependent.dc_lived_half
    printed: "(helper)"
    label: "Lived with you for more than half of 2025 (a person born or who died in 2025: more than half the time alive)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ge: [dependent.months, {const: 7, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [dependent.born_died, {const: true}]}
            - {op: test, eq: [dependent.part_year_home, {const: true}]}

  - id: dependent.h_dc_under13
    printed: "(helper)"
    label: "Was under age 13 when the care was provided"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, lt: [dependent.age, {param: dc.child_age}]}
        - op: test
          all:
            - {op: test, eq: [dependent.age, {param: dc.child_age}]}
            - {op: test, eq: [dependent.dc_under13, {const: true}]}

  - id: dependent.h_dc_dependent
    printed: "(helper)"
    label: "Your dependent, or would have been except for gross income of $5,200 or more or your being claimable on someone else's return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_qc_base, {const: true}]}
        - {op: test, eq: [dependent.h_qr_core, {const: true}]}
    note: "The joint-return exception is not computed: a person on a joint return is married, which is refused."

  - id: dependent.dc_qp
    printed: "(helper)"
    label: "Qualifying person for Form 2441"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [dependent.h_claimed_qc, {const: true}]}
            - {op: test, eq: [dependent.h_dc_under13, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [dependent.dc_incapable, {const: true}]}
            - {op: test, eq: [dependent.dc_lived_half, {const: true}]}
            - {op: test, eq: [dependent.h_dc_dependent, {const: true}]}
    refuses: [dependent.divorced_rule, dependent.married, dependent.multiple_support]

  - id: dependent.dc_line2c
    printed: "2(c)"
    label: "Check here if the qualifying person was over age 12 and was disabled"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.dc_qp, {const: true}]}
        - {op: test, eq: [dependent.dc_incapable, {const: true}]}
        - op: test
          any:
            - {op: test, gt: [dependent.age, {param: dc.child_age}]}
            - op: test
              all:
                - {op: test, eq: [dependent.age, {param: dc.child_age}]}
                - {op: test, eq: [dependent.dc_over12_care, {const: true}]}
    shown_when: dependent.dc_qp

  - id: dependent.dc_line2d
    printed: "2(d)"
    label: "Qualified expenses you incurred and paid in 2025 for the person listed in column (a)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.dc_qp, {const: true}]}, then: dependent.dc_paid}
        - {guard: {op: test, eq: [dependent.dc_qp, {const: false}]}, then: dependent.h_zero}
    shown_when: dependent.dc_qp

  - id: dependent.h_dc_cent
    printed: "(helper)"
    label: "One cent if a qualifying person, else zero"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.dc_qp, {const: true}]}, then: dependent.h_cent}
        - {guard: {op: test, eq: [dependent.dc_qp, {const: false}]}, then: dependent.h_zero}

  - id: dependent.dc_count
    printed: "(helper)"
    label: "Number of qualifying persons for Form 2441 (this person: 1 or 0)"
    type: Count
    expr: {op: percent_floor, part: dependent.h_dc_cent, whole: {param: sc.hundred_cents}, cap: 100}
    note: "1 cent over 100 cents as a whole percentage gives 1; zero gives 0."

  - id: dependent.h_ptc_counted
    printed: "(helper)"
    label: "Dependent required to file a return because of income (Form 8962, line 2b)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.ptc_files, {const: true}]}

  - id: dependent.ptc_magi_counted
    printed: "(helper)"
    label: "This dependent's modified AGI included in Form 8962, line 2b"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_ptc_counted, {const: true}]}, then: dependent.ptc_magi}
        - {guard: {op: test, eq: [dependent.h_ptc_counted, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_edu_ok
    printed: "(helper)"
    label: "Education credit possible for this claimed dependent student (expenses paid, Form 1098-T, TIN issued by the due date)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.claimed, {const: true}]}
        - {op: test, eq: [dependent.edu, {const: true}]}
        - {op: test, eq: [dependent.edu_1098t, {const: true}]}
        - {op: test, eq: [dependent.edu_tin_issued, {const: true}]}

  - id: dependent.h_edu_over_gate
    printed: "(helper)"
    label: "Assistance and refunds for an academic period exceed that period's expenses"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_ok, {const: true}]}
        - {op: test, eq: [dependent.edu_over, {const: true}]}
    note: "The worksheet reduces each academic period separately; with totals over the year the reduction is right only when no period's adjustments exceed its expenses, so that case is refused."

  - id: dependent.h_edu_aoc_ok
    printed: "(helper)"
    label: "Student eligible for the American opportunity credit (lines 23 to 26, institution's EIN)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_ok, {const: true}]}
        - {op: test, eq: [dependent.edu_line23, {const: false}]}
        - {op: test, eq: [dependent.edu_line24, {const: true}]}
        - {op: test, eq: [dependent.edu_line25, {const: false}]}
        - {op: test, eq: [dependent.edu_line26, {const: false}]}
        - {op: test, eq: [dependent.edu_ein, {const: true}]}

  - id: dependent.h_edu_llc_on
    printed: "(helper)"
    label: "Line 31 completed for this student (lifetime learning credit)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_edu_ok, {const: true}]}
        - {op: test, eq: [dependent.h_edu_aoc_ok, {const: false}]}

  - id: dependent.h_edu_adj
    printed: "(helper)"
    label: "Total adjustments (tax-free assistance received in 2025 and in 2026, and refunds)"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_a_this_year, dependent.edu_a_next_year, dependent.edu_refunds]}
    refuses: [dependent.h_edu_over_gate]

  - id: dependent.h_edu_aoc_exp
    printed: "(helper)"
    label: "Qualified education expenses for the American opportunity credit (tuition, fees and course materials)"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_inst, dependent.edu_mat]}

  - id: dependent.h_edu_aoc_adjusted
    printed: "(helper)"
    label: "Adjusted qualified education expenses (AOC). If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.h_edu_aoc_exp, take: dependent.h_edu_adj}

  - id: dependent.h_aoc_cap
    printed: "(helper)"
    label: "$4,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.expense_cap}

  - id: dependent.h_edu_aoc_capped
    printed: "(helper)"
    label: "Adjusted qualified education expenses, not more than $4,000"
    type: NonNegDollars
    expr: {op: smaller_of, of: [dependent.h_edu_aoc_adjusted, dependent.h_aoc_cap]}

  - id: dependent.edu_line27
    printed: "27"
    label: "Adjusted qualified education expenses (see instructions). Don't enter more than $4,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_edu_aoc_ok, {const: true}]}, then: dependent.h_edu_aoc_capped}
        - {guard: {op: test, eq: [dependent.h_edu_aoc_ok, {const: false}]}, then: dependent.h_zero}
    shown_when: dependent.h_edu_aoc_ok

  - id: dependent.edu_line28
    printed: "28"
    label: "Subtract $2,000 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.edu_line27, take: {param: aoc.full_band}}
    shown_when: dependent.h_edu_aoc_ok

  - id: dependent.edu_line29
    printed: "29"
    label: "Multiply line 28 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: dependent.edu_line28, rate: {param: aoc.second_rate}}
    shown_when: dependent.h_edu_aoc_ok

  - id: dependent.h_band
    printed: "(helper)"
    label: "$2,000"
    type: NonNegDollars
    expr: {op: param, ref: aoc.full_band}

  - id: dependent.h_line29_plus
    printed: "(helper)"
    label: "Add $2,000 to the amount on line 29"
    type: NonNegDollars
    expr: {op: sum, of: [dependent.edu_line29, dependent.h_band]}

  - id: dependent.h_line28_zero
    printed: "(helper)"
    label: "Line 28 is zero"
    type: Bool
    expr: {op: test, eq: [dependent.edu_line28, {const: 0}]}

  - id: dependent.edu_line30
    printed: "30"
    label: "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29 and enter the result"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_line28_zero, {const: true}]}, then: dependent.edu_line27}
        - {guard: {op: test, eq: [dependent.h_line28_zero, {const: false}]}, then: dependent.h_line29_plus}
    shown_when: dependent.h_edu_aoc_ok

  - id: dependent.h_edu_llc_adjusted
    printed: "(helper)"
    label: "Adjusted qualified education expenses (lifetime learning credit: tuition and required fees). If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: dependent.edu_inst, take: dependent.h_edu_adj}

  - id: dependent.edu_line31
    printed: "31"
    label: "Adjusted qualified education expenses (see instructions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.h_edu_llc_on, {const: true}]}, then: dependent.h_edu_llc_adjusted}
        - {guard: {op: test, eq: [dependent.h_edu_llc_on, {const: false}]}, then: dependent.h_zero}
    shown_when: dependent.h_edu_llc_on
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
fa21055500dbb650 [{"const": false}, {"$shared": "e9899da862973fba"}]
58f5ab82873d1d55 {"args": {"$shared": "fa21055500dbb650"}, "test": "eq"}
7b3027880d0f77f1 [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}]
6ab7b8e749d2bb91 {"args": {"$shared": "7b3027880d0f77f1"}, "test": "any"}
0bd4f14c5489af85 {"guard": {"$shared": "6ab7b8e749d2bb91"}, "then": {"param": "household.no"}}
7530ac17e8154427 {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"input": "dependent.spouse_relative"}}
4b936c65667627e0 [{"$shared": "0bd4f14c5489af85"}, {"$shared": "7530ac17e8154427"}]
bba43f272c880e8b {"alternatives": {"$shared": "4b936c65667627e0"}, "op": "choose"}
f23cc85add55f5ec {"guard": {"$shared": "58f5ab82873d1d55"}, "then": {"$shared": "bba43f272c880e8b"}}
6ae638e15454bf35 [{"const": true}, {"$shared": "e9899da862973fba"}]
62d45528a902061e {"args": {"$shared": "6ae638e15454bf35"}, "test": "eq"}
f71e05c30cf4142b {"guard": {"$shared": "62d45528a902061e"}, "then": {"$shared": "e9899da862973fba"}}
635a38b8a6a86095 [{"$shared": "f23cc85add55f5ec"}, {"$shared": "f71e05c30cf4142b"}]
5cfae5cdf838a2d1 {"alternatives": {"$shared": "635a38b8a6a86095"}, "op": "choose"}
24414c2ff7362648 {"guard": {"$shared": "782ba030bc74113e"}, "then": {"$shared": "5cfae5cdf838a2d1"}}
496a1e5bc5a2855e {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}
49ede5044c113dde {"guard": {"$shared": "f5de24c486ce70c8"}, "then": {"$shared": "bba43f272c880e8b"}}
2ed3edcc8fc76ce6 {"guard": {"$shared": "dc0fef1e6b60aa95"}, "then": {"$shared": "5ef59dc55ce92244"}}
7026a45b964c31c2 [{"$shared": "49ede5044c113dde"}, {"$shared": "2ed3edcc8fc76ce6"}]
a523f2bb18644bdc {"alternatives": {"$shared": "7026a45b964c31c2"}, "op": "choose"}
841b491454239bf4 {"guard": {"$shared": "496a1e5bc5a2855e"}, "then": {"$shared": "a523f2bb18644bdc"}}
76d5c71c6f5fa8bd [{"$shared": "df298e38774d668f"}, {"$shared": "24414c2ff7362648"}, {"$shared": "841b491454239bf4"}]
92465a11dfa3da08 {"alternatives": {"$shared": "76d5c71c6f5fa8bd"}, "op": "choose"}
9ada4bf31bd0c124 [{"const": false}, {"$shared": "92465a11dfa3da08"}]
0f908ea39ea06262 {"args": {"$shared": "9ada4bf31bd0c124"}, "test": "eq"}
98f64f821899bf69 {"guard": {"$shared": "0f908ea39ea06262"}, "then": {"param": "household.no"}}
dc2e252336a7800b [{"const": true}, {"$shared": "92465a11dfa3da08"}]
8bb854f1ca9b9969 {"args": {"$shared": "dc2e252336a7800b"}, "test": "eq"}
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
c79b9f59a930af34 {"guard": {"$shared": "8bb854f1ca9b9969"}, "then": {"$shared": "21cda9b829a93fc8"}}
5e551d723b522337 [{"$shared": "98f64f821899bf69"}, {"$shared": "c79b9f59a930af34"}]
3ce51363c511387e {"alternatives": {"$shared": "5e551d723b522337"}, "op": "choose"}
98db2879ac990a01 [{"const": false}, {"$shared": "3ce51363c511387e"}]
fdfd77c9a3b76b71 {"args": {"$shared": "98db2879ac990a01"}, "test": "eq"}
a3c803fba7ae58f2 {"guard": {"$shared": "fdfd77c9a3b76b71"}, "then": {"param": "household.no"}}
103aff10063e7c92 [{"const": true}, {"$shared": "3ce51363c511387e"}]
dd522cd3aaa81f7f {"args": {"$shared": "103aff10063e7c92"}, "test": "eq"}
ccca83d3e8ec1e26 {"guard": {"$shared": "dd522cd3aaa81f7f"}, "then": {"$shared": "f5013721bd489d9d"}}
e18027a664f79876 [{"$shared": "a3c803fba7ae58f2"}, {"$shared": "ccca83d3e8ec1e26"}]
3593dd0d589dd27b {"alternatives": {"$shared": "e18027a664f79876"}, "op": "choose"}
9077f3ea0126c1c7 {"guard": {"$shared": "684faf9e6923f98a"}, "then": {"$shared": "3593dd0d589dd27b"}}
e980018b74e8c336 [{"const": true}, {"$shared": "cd75754270d615d0"}]
04706b205e474b59 {"args": {"$shared": "e980018b74e8c336"}, "test": "eq"}
7a895badee7db8c4 {"guard": {"$shared": "04706b205e474b59"}, "then": {"$shared": "cd75754270d615d0"}}
e2001652f342722d [{"$shared": "9077f3ea0126c1c7"}, {"$shared": "7a895badee7db8c4"}]
f492ba63b9db5ab2 {"alternatives": {"$shared": "e2001652f342722d"}, "op": "choose"}
990e6ef45b27484f [{"$shared": "6bfcd092e376d8ac"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}]
594cc74b63a2de96 {"args": {"$shared": "990e6ef45b27484f"}, "test": "all"}
9e69dd70a33593c6 [{"$shared": "594cc74b63a2de96"}, {"$shared": "3d996a5e0f7cd98e"}, {"args": [{"const": false}, {"input": "dependent.own_money"}], "test": "eq"}]
a12c4a1796e749c0 {"args": {"$shared": "9e69dd70a33593c6"}, "test": "any"}
0a2e10cedfae3bfb [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"$shared": "7bc7453b71deb151"}]
33fc981e094611e8 {"args": {"$shared": "0a2e10cedfae3bfb"}, "test": "all"}
638e10d34af6777d [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}]
549d9711fcb0a0d9 {"args": {"$shared": "638e10d34af6777d"}, "test": "all"}
2e05de679cee00c4 [{"$shared": "33fc981e094611e8"}, {"$shared": "549d9711fcb0a0d9"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}]
aae5cb78c743225c {"args": {"$shared": "2e05de679cee00c4"}, "test": "any"}
67c2755114df6641 [{"$shared": "a12c4a1796e749c0"}, {"$shared": "aae5cb78c743225c"}, {"$shared": "dfe671ee2eedd621"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"$shared": "da884a5a9bffad77"}]
4a7eda47fb09e869 {"args": {"$shared": "67c2755114df6641"}, "test": "all"}
21de8f70933b8703 {"args": [{"const": false}, {"input": "dependent.spouse_claims"}], "test": "eq"}
932daea67a3f4706 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"$shared": "21de8f70933b8703"}]
b34648d2d17420ab {"args": {"$shared": "932daea67a3f4706"}, "test": "any"}
19d9d483c884fe90 {"args": [{"const": true}, {"input": "dependent.other_only_spouse"}], "test": "eq"}
3c1297996c38f15c [{"$shared": "b34648d2d17420ab"}, {"$shared": "19d9d483c884fe90"}]
e6e30488ea6b250b {"args": {"$shared": "3c1297996c38f15c"}, "test": "all"}
b6381ef197b3b701 {"args": [{"const": false}, {"input": "dependent.other_only_spouse"}], "test": "eq"}
a86fbaaf1cc671fe [{"$shared": "b6381ef197b3b701"}, {"args": [{"const": true}, {"input": "dependent.filer_parent"}], "test": "eq"}]
83a584c9d08b9cc7 {"args": {"$shared": "a86fbaaf1cc671fe"}, "test": "all"}
02a6487023ff1c0e {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}
4d6abd3233e0922b {"args": [{"const": true}, {"input": "dependent.other_nontaxpayer"}], "test": "eq"}
674a048744f46ddf [{"$shared": "e6e30488ea6b250b"}, {"$shared": "83a584c9d08b9cc7"}, {"$shared": "02a6487023ff1c0e"}, {"$shared": "4d6abd3233e0922b"}]
c3cee0d9721af552 {"args": {"$shared": "674a048744f46ddf"}, "test": "any"}
89e0ac1e76fff904 [{"$shared": "4a7eda47fb09e869"}, {"$shared": "c3cee0d9721af552"}]
ae241daf27400f9a {"args": {"$shared": "89e0ac1e76fff904"}, "test": "all"}
93ec5473ae5e5158 [{"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "eq"}]
1fd77c3d63ad8b8e {"args": {"$shared": "93ec5473ae5e5158"}, "test": "any"}
ee2f97e51aef40ff [{"$shared": "1fd77c3d63ad8b8e"}, {"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}]
d3c7eccf3db4c0cf {"args": {"$shared": "ee2f97e51aef40ff"}, "test": "any"}
98cd22d2f26cf8d1 [{"$shared": "ae241daf27400f9a"}, {"$shared": "d3c7eccf3db4c0cf"}]
8f3e5c3fc94154be {"args": {"$shared": "98cd22d2f26cf8d1"}, "test": "all"}
e60882f7bb5e1a22 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}]
982ab331e31c3a45 {"args": {"$shared": "e60882f7bb5e1a22"}, "test": "any"}
51d0b171c39c7a06 [{"$shared": "8f3e5c3fc94154be"}, {"$shared": "982ab331e31c3a45"}]
bbe5fc5df82e58ec {"args": {"$shared": "51d0b171c39c7a06"}, "test": "all"}
f07b4f56dd3d7ee6 [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}]
78ee2dec84d6d953 {"args": {"$shared": "f07b4f56dd3d7ee6"}, "test": "any"}
86ebe37df995ae49 [{"$shared": "1381f8ffc1b24aec"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}]
d07889d0922fd64c {"args": {"$shared": "86ebe37df995ae49"}, "test": "any"}
31a1432bd7aa760e [{"$shared": "78ee2dec84d6d953"}, {"$shared": "d07889d0922fd64c"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}]
912a5a7a234e62fb {"args": {"$shared": "31a1432bd7aa760e"}, "test": "all"}
9dcdae15c6e67517 {"args": [{"const": "unsure"}, {"input": "dependent.self_support_view"}], "test": "ne"}
cc4b3f8ac854ec84 [{"$shared": "9dcdae15c6e67517"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}]
9b37979621983ac7 {"args": {"$shared": "cc4b3f8ac854ec84"}, "test": "any"}
1f5cbecb8499d1d3 {"args": [{"const": "under_half"}, {"input": "dependent.self_support_view"}], "test": "ne"}
858fafaa2c4a2e3e [{"$shared": "9b37979621983ac7"}, {"$shared": "1f5cbecb8499d1d3"}, {"args": [{"const": false}, {"input": "dependent.own_money"}], "test": "ne"}]
606c889abd628103 {"args": {"$shared": "858fafaa2c4a2e3e"}, "test": "all"}
6b958588ce0c364c {"args": [{"input": "dependent.months"}, {"const": 7, "type": "Count"}], "test": "lt"}
c1f11fe5f03793d8 [{"$shared": "912a5a7a234e62fb"}, {"$shared": "606c889abd628103"}, {"$shared": "259be3591f0d595e"}, {"$shared": "6b958588ce0c364c"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}]
4bf76f5e51de54b3 {"args": {"$shared": "c1f11fe5f03793d8"}, "test": "any"}
3ab93055c4a8bc36 [{"$shared": "02a6487023ff1c0e"}, {"$shared": "4d6abd3233e0922b"}]
1883b3543934be39 {"args": {"$shared": "3ab93055c4a8bc36"}, "test": "any"}
81c8f721afa5f99a [{"$shared": "4bf76f5e51de54b3"}, {"$shared": "1883b3543934be39"}]
b2403f4c9c7e981c {"args": {"$shared": "81c8f721afa5f99a"}, "test": "all"}
5d1792dbc0ff6ce8 [{"$shared": "7ee8927420db1540"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}]
5cdd94d35e804dbc {"args": {"$shared": "5d1792dbc0ff6ce8"}, "test": "all"}
83306ff2d22fccbf [{"$shared": "5cdd94d35e804dbc"}, {"$shared": "81e9b5c4c4ab4c50"}]
dc6a51f361363ce3 {"args": {"$shared": "83306ff2d22fccbf"}, "test": "any"}
e07497c2d2e787fb [{"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}]
00740b4f0410aeb6 {"args": {"$shared": "e07497c2d2e787fb"}, "test": "all"}
262d147998c405ca {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}
250d38940f4a5462 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"$shared": "262d147998c405ca"}]
458fab87f9dd7601 {"args": {"$shared": "250d38940f4a5462"}, "test": "all"}
0af63361e4edfb06 [{"$shared": "458fab87f9dd7601"}, {"$shared": "cb88768b40471aff"}, {"$shared": "a10e36b275ccac18"}, {"$shared": "cae21fd21ef95261"}, {"$shared": "475db94656536733"}, {"$shared": "b97208e9b0a8586c"}]
07ff44ec481e8052 {"args": {"$shared": "0af63361e4edfb06"}, "test": "any"}
984601c9dbc5eba5 [{"$shared": "00740b4f0410aeb6"}, {"$shared": "07ff44ec481e8052"}, {"$shared": "496a1e5bc5a2855e"}]
55ebead86d5265e0 {"args": {"$shared": "984601c9dbc5eba5"}, "test": "any"}
7b8797a85725e3e1 [{"$shared": "b2403f4c9c7e981c"}, {"$shared": "dc6a51f361363ce3"}, {"$shared": "55ebead86d5265e0"}, {"$shared": "d3c7eccf3db4c0cf"}]
2fa776fffcb120f2 {"args": {"$shared": "7b8797a85725e3e1"}, "test": "all"}
2a854f65795d5394 [{"$shared": "2fa776fffcb120f2"}, {"$shared": "982ab331e31c3a45"}, {"$shared": "14b7aaa29e3bef3d"}]
a935686f3afe9d76 {"args": {"$shared": "2a854f65795d5394"}, "test": "all"}
3bb29bf348c71fed [{"$shared": "bbe5fc5df82e58ec"}, {"$shared": "a935686f3afe9d76"}]
fd19247f4fee5692 {"args": {"$shared": "3bb29bf348c71fed"}, "test": "any"}
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
a8399a0f199ac2d1 [{"$shared": "bbe5fc5df82e58ec"}, {"$shared": "78ced2d4a94bd48a"}, {"$shared": "fd19247f4fee5692"}, {"$shared": "1fd77c3d63ad8b8e"}, {"$shared": "6f20306cdcff36df"}, {"$shared": "804674facba7ce5d"}, {"$shared": "3cec84f965d300a6"}]
ffef0ab2d2add02c {"args": {"$shared": "a8399a0f199ac2d1"}, "test": "all"}
2a0b76400b1bdb51 [{"const": false}, {"$shared": "f492ba63b9db5ab2"}]
3f97f06feb678aca {"args": {"$shared": "2a0b76400b1bdb51"}, "test": "eq"}
bf1b06a5905438ac {"guard": {"$shared": "3f97f06feb678aca"}, "then": {"param": "household.no"}}
7949240bec5d163a [{"const": true}, {"$shared": "f492ba63b9db5ab2"}]
304992367f5da773 {"args": {"$shared": "7949240bec5d163a"}, "test": "eq"}
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
8d64b10ebf605823 {"guard": {"$shared": "304992367f5da773"}, "then": {"$shared": "3d7126ffd3118950"}}
d6dd8b7eaded749f [{"$shared": "bf1b06a5905438ac"}, {"$shared": "8d64b10ebf605823"}]
4011368a4d2e25ac {"alternatives": {"$shared": "d6dd8b7eaded749f"}, "op": "choose"}
9aa80cb173938c68 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}]
622f481232897268 {"args": {"$shared": "9aa80cb173938c68"}, "test": "all"}
797e9b74b4e8e4ec {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "ne"}
79166e1cd7b8e694 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"$shared": "797e9b74b4e8e4ec"}]
61637c12d231a4af {"args": {"$shared": "79166e1cd7b8e694"}, "test": "any"}
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
9c72a298f12c5e32 [{"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}]
dfe58c4e8e47a8d5 {"args": {"$shared": "9c72a298f12c5e32"}, "test": "all"}
275fe334c8bcdd5f [{"$shared": "dfe58c4e8e47a8d5"}, {"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}]
4190821ec37110d1 {"args": {"$shared": "275fe334c8bcdd5f"}, "test": "all"}
8e88e6b668564f1f {"args": [{"const": "unsure"}, {"input": "dependent.supported_view"}], "test": "ne"}
fb2e9f8e4293cda6 [{"$shared": "8e88e6b668564f1f"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}]
5c8093da182190a2 {"args": {"$shared": "fb2e9f8e4293cda6"}, "test": "any"}
f3c71a8f2a5390b3 {"args": [{"const": "over_half"}, {"input": "dependent.supported_view"}], "test": "ne"}
fb8605d4d7745be4 [{"$shared": "5c8093da182190a2"}, {"$shared": "f3c71a8f2a5390b3"}]
df716d0500c208d3 {"args": {"$shared": "fb8605d4d7745be4"}, "test": "all"}
621f1cf2e59a5d98 {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}
74e4038d19cf5802 {"args": [{"const": true}, {"input": "dependent.other_nontaxpayer"}], "test": "ne"}
7998acacca13874d [{"$shared": "621f1cf2e59a5d98"}, {"$shared": "74e4038d19cf5802"}]
6a48aff82efb9960 {"args": {"$shared": "7998acacca13874d"}, "test": "all"}
95f034351c872b8e [{"$shared": "4a7eda47fb09e869"}, {"$shared": "6a48aff82efb9960"}]
6398491af040be10 {"args": {"$shared": "95f034351c872b8e"}, "test": "any"}
20f19252dc05bc67 [{"$shared": "0aa027d14441d2bb"}, {"$shared": "4190821ec37110d1"}, {"$shared": "df716d0500c208d3"}, {"$shared": "6398491af040be10"}]
24c948705defd9bc {"args": {"$shared": "20f19252dc05bc67"}, "test": "any"}
3a4aca6f498ded37 [{"$shared": "622f481232897268"}, {"$shared": "24c948705defd9bc"}, {"$shared": "f5726735e624cfd5"}]
e4c7e89934fd588b {"args": {"$shared": "3a4aca6f498ded37"}, "test": "any"}
ce1398ec8828bdaa {"args": [{"const": false}, {"input": "dependent.spouse_claims"}], "test": "ne"}
16f2ef0ded9edab2 [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"$shared": "ce1398ec8828bdaa"}]
2c483ea3c2873d39 {"args": {"$shared": "16f2ef0ded9edab2"}, "test": "all"}
50cb2527df09a6fd {"args": [{"const": true}, {"input": "dependent.other_only_spouse"}], "test": "ne"}
a463660a1ca1edc6 [{"$shared": "2c483ea3c2873d39"}, {"$shared": "50cb2527df09a6fd"}]
a6d237f1b5fde1c8 {"args": {"$shared": "a463660a1ca1edc6"}, "test": "any"}
096f10caa47b5b8c {"args": [{"const": false}, {"input": "dependent.other_only_spouse"}], "test": "ne"}
ec039f25641db7e5 [{"$shared": "096f10caa47b5b8c"}, {"args": [{"const": true}, {"input": "dependent.filer_parent"}], "test": "ne"}]
c0423f26999a19e2 {"args": {"$shared": "ec039f25641db7e5"}, "test": "any"}
01dc3c8ecbe942bf [{"$shared": "a6d237f1b5fde1c8"}, {"$shared": "c0423f26999a19e2"}, {"$shared": "621f1cf2e59a5d98"}, {"$shared": "74e4038d19cf5802"}]
6dd9875a885c8e76 {"args": {"$shared": "01dc3c8ecbe942bf"}, "test": "all"}
0fd12be63b157a49 [{"$shared": "6dd9875a885c8e76"}, {"$shared": "4bf76f5e51de54b3"}]
98e3812064f13e0a {"args": {"$shared": "0fd12be63b157a49"}, "test": "any"}
a91c8356c3278987 [{"$shared": "4190821ec37110d1"}, {"$shared": "98e3812064f13e0a"}]
b39d4d1182215093 {"args": {"$shared": "a91c8356c3278987"}, "test": "any"}
0e39ff2f9068cffb [{"$shared": "622f481232897268"}, {"$shared": "b39d4d1182215093"}]
bbe41163d151b442 {"args": {"$shared": "0e39ff2f9068cffb"}, "test": "any"}
c4fb84bb58054fa0 [{"$shared": "e4c7e89934fd588b"}, {"$shared": "bbe41163d151b442"}]
d590ca39f5be6faa {"args": {"$shared": "c4fb84bb58054fa0"}, "test": "all"}
42e234da23232c52 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}]
4e94f318a5bfe546 {"args": {"$shared": "42e234da23232c52"}, "test": "all"}
6ffafcc965368126 [{"args": [{"const": true}, {"input": "dependent.citizen_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}]
d970378acdded4c4 {"args": {"$shared": "6ffafcc965368126"}, "test": "all"}
bb4ff2cf1e5286e7 [{"$shared": "ac4b48c317adfa6c"}, {"const": 0, "type": "Count"}]
376b69af2e1fafab {"args": {"$shared": "bb4ff2cf1e5286e7"}, "test": "le"}
798a2b9fdc3c220e {"args": {"$shared": "3503b2668d859ed6"}, "test": "ne"}
f456402f77396702 [{"$shared": "376b69af2e1fafab"}, {"$shared": "798a2b9fdc3c220e"}]
39ef0fc4c27afcce {"args": {"$shared": "f456402f77396702"}, "test": "any"}
3c09719e882bd02b [{"$shared": "d590ca39f5be6faa"}, {"$shared": "dfe58c4e8e47a8d5"}, {"$shared": "4e94f318a5bfe546"}, {"$shared": "d970378acdded4c4"}, {"$shared": "bbe41163d151b442"}, {"$shared": "39ef0fc4c27afcce"}, {"$shared": "475a509e3d1380c7"}]
15bc44563c96e5d3 {"args": {"$shared": "3c09719e882bd02b"}, "test": "any"}
555f36fe5add1e3d [{"$shared": "fd19247f4fee5692"}, {"$shared": "15bc44563c96e5d3"}, {"$shared": "1fd77c3d63ad8b8e"}, {"$shared": "6f20306cdcff36df"}, {"$shared": "9ab757132a95133d"}]
7cb1ce2222758717 {"args": {"$shared": "555f36fe5add1e3d"}, "test": "all"}
c4cf55482c46be6c {"guard": {"$shared": "c2062ef24e1afd8f"}, "then": {"const": 0}}
1a2e562b9f40b554 {"guard": {"$shared": "15bc44563c96e5d3"}, "then": {"const": 0}}
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
3c241465a544363d [{"$shared": "3fa0c27493e1acc9"}, {"$shared": "304992367f5da773"}, {"$shared": "f4c5aea6dc665ec2"}, {"$shared": "bd88e482830d2da2"}, {"$shared": "5090e2054156fd72"}]
057b5d936fc1268d {"args": {"$shared": "3c241465a544363d"}, "test": "all"}
717392957dd314a0 [{"$shared": "fe55e6678145ddca"}, {"$shared": "057b5d936fc1268d"}]
74fd8f16b18bb4f2 {"args": {"$shared": "717392957dd314a0"}, "test": "any"}
87722dbfe6cea1e9 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}]
5a32eb26e872ff34 {"args": {"$shared": "87722dbfe6cea1e9"}, "test": "any"}
61276d911b7b575c [{"$shared": "5a32eb26e872ff34"}, {"$shared": "45b31d0efa71a78e"}]
fad782b1c0f89de1 {"args": {"$shared": "61276d911b7b575c"}, "test": "all"}
18eb08137572186e [{"$shared": "fad782b1c0f89de1"}, {"$shared": "da884a5a9bffad77"}]
2f7093f7d73aee4e {"args": {"$shared": "18eb08137572186e"}, "test": "any"}
cf4f221d9a1898e0 [{"$shared": "a935686f3afe9d76"}, {"$shared": "07ff44ec481e8052"}]
5c49724923737c83 {"args": {"$shared": "cf4f221d9a1898e0"}, "test": "all"}
a60afddeb650762b [{"$shared": "5c49724923737c83"}, {"$shared": "ae241daf27400f9a"}]
bb9b4ee3f21ef2ec {"args": {"$shared": "a60afddeb650762b"}, "test": "any"}
bd5631f7475eb721 [{"$shared": "bb9b4ee3f21ef2ec"}, {"$shared": "2f7093f7d73aee4e"}]
678fadf37507fe61 {"args": {"$shared": "bd5631f7475eb721"}, "test": "all"}
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
043678299820edb1 [{"$shared": "b80d786b1a8c7527"}, {"$shared": "304992367f5da773"}, {"args": [{"const": true}, {"ref": "f2441.care"}], "test": "eq"}]
ceafbfd6623775f4 {"args": {"$shared": "043678299820edb1"}, "test": "all"}
8d678eec54d07480 [{"args": [{"const": true}, {"input": "dependent.dc_under13"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}]
2ab913452348a2c5 {"args": {"$shared": "8d678eec54d07480"}, "test": "all"}
7d8a9efb1071bcd1 [{"$shared": "2ab913452348a2c5"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "lt"}]
f8784cea50608452 {"args": {"$shared": "7d8a9efb1071bcd1"}, "test": "any"}
02d77cac3627c437 [{"$shared": "bbe5fc5df82e58ec"}, {"$shared": "f8784cea50608452"}]
191593f2c01160bc {"args": {"$shared": "02d77cac3627c437"}, "test": "all"}
dfae6ccccc4cd2c9 [{"$shared": "8f3e5c3fc94154be"}, {"$shared": "2fa776fffcb120f2"}]
81439baca4d0b61e {"args": {"$shared": "dfae6ccccc4cd2c9"}, "test": "any"}
58e9949b7943d1fb [{"$shared": "81439baca4d0b61e"}, {"$shared": "46b66a31fd3a3891"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "eq"}]
bc59b231bcab83ff {"args": {"$shared": "58e9949b7943d1fb"}, "test": "all"}
e49e09aa5f6b8c0f [{"$shared": "191593f2c01160bc"}, {"$shared": "bc59b231bcab83ff"}]
fca3c3a458708262 {"args": {"$shared": "e49e09aa5f6b8c0f"}, "test": "any"}
994aa7102013a5ff [{"$shared": "24c948705defd9bc"}, {"$shared": "b39d4d1182215093"}]
8c63dd5bde3ec408 {"args": {"$shared": "994aa7102013a5ff"}, "test": "all"}
363446df813d9ff2 {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "ne"}
37f6678bff8e7bc6 [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "ne"}, {"$shared": "363446df813d9ff2"}]
cecce6ab0e8ea4c1 {"args": {"$shared": "37f6678bff8e7bc6"}, "test": "any"}
154dbc6f9edd32bc [{"$shared": "cecce6ab0e8ea4c1"}, {"$shared": "6b958588ce0c364c"}]
eae17f71d9814ab1 {"args": {"$shared": "154dbc6f9edd32bc"}, "test": "all"}
c855f7df261773a5 [{"$shared": "8c63dd5bde3ec408"}, {"$shared": "eae17f71d9814ab1"}, {"args": [{"const": true}, {"input": "dependent.dc_incapable"}], "test": "ne"}]
47bd88a36f8a2619 {"args": {"$shared": "c855f7df261773a5"}, "test": "any"}
b79fdd45e73cdda7 [{"args": [{"const": true}, {"input": "dependent.dc_under13"}], "test": "ne"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "ne"}]
877751740ae5afb1 {"args": {"$shared": "b79fdd45e73cdda7"}, "test": "any"}
6e80eb1a95b57749 [{"$shared": "877751740ae5afb1"}, {"args": [{"param": "dc.child_age"}, {"input": "dependent.age"}], "test": "le"}]
7158eb3d4682bff6 {"args": {"$shared": "6e80eb1a95b57749"}, "test": "all"}
3da483b26461f7de [{"$shared": "7158eb3d4682bff6"}, {"$shared": "bbe41163d151b442"}]
8295dbe0eb9f83de {"args": {"$shared": "3da483b26461f7de"}, "test": "any"}
f2ad63c8963b7d15 [{"$shared": "47bd88a36f8a2619"}, {"$shared": "8295dbe0eb9f83de"}]
d84877e7a11c7027 {"args": {"$shared": "f2ad63c8963b7d15"}, "test": "all"}
36461792c70c4fb8 {"guard": {"$shared": "d84877e7a11c7027"}, "then": {"const": 0}}
56db7e862d5e6240 {"guard": {"args": [{"const": true}, {"input": "dependent.own_money"}], "test": "eq"}, "then": {"input": "dependent.ptc_files"}}
1fc44ef19aad9190 [{"$shared": "5dd0f7b778264284"}, {"$shared": "56db7e862d5e6240"}]
efa039d59e86b80f {"alternatives": {"$shared": "1fc44ef19aad9190"}, "op": "choose"}
49ba61210109901e {"args": [{"const": true}, {"input": "dependent.dc_over12_care"}], "test": "eq"}
7228abc7a6a4b32e [{"$shared": "49ba61210109901e"}, {"args": [{"input": "dependent.age"}, {"param": "dc.child_age"}], "test": "eq"}]
fb5642142165b661 {"args": {"$shared": "7228abc7a6a4b32e"}, "test": "all"}
1bc0e69c10b54627 [{"$shared": "fb5642142165b661"}, {"args": [{"param": "dc.child_age"}, {"input": "dependent.age"}], "test": "lt"}]
5411e1ffa263fe04 {"args": {"$shared": "1bc0e69c10b54627"}, "test": "any"}
ff7152b9011d2a4a {"guard": {"args": [{"const": false}, {"ref": "f8863.paid"}], "test": "eq"}, "then": {"param": "edu.no"}}
088055d8e4449bbc {"guard": {"$shared": "3f97f06feb678aca"}, "then": {"param": "edu.no"}}
541da454340c6b75 {"guard": {"args": [{"const": false}, {"input": "dependent.edu"}], "test": "eq"}, "then": {"param": "edu.no"}}
6f3db53061fa74ce {"guard": {"args": [{"const": false}, {"input": "dependent.tin"}], "test": "eq"}, "then": {"param": "edu.no"}}
83a92c5b4cd6064c {"guard": {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, "then": {"input": "dependent.edu_1098t"}}
678479682f911276 [{"$shared": "6f3db53061fa74ce"}, {"$shared": "83a92c5b4cd6064c"}]
d0a43fb1b7c454b8 {"alternatives": {"$shared": "678479682f911276"}, "op": "choose"}
6f0e1f879ef64417 {"guard": {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "eq"}, "then": {"$shared": "d0a43fb1b7c454b8"}}
78879181dc366173 [{"$shared": "541da454340c6b75"}, {"$shared": "6f0e1f879ef64417"}]
227d941d24467b19 {"alternatives": {"$shared": "78879181dc366173"}, "op": "choose"}
2b44f100800d743c {"guard": {"$shared": "304992367f5da773"}, "then": {"$shared": "227d941d24467b19"}}
3b15177fb5fb3d17 [{"$shared": "088055d8e4449bbc"}, {"$shared": "2b44f100800d743c"}]
8450769efa1ccdf3 {"alternatives": {"$shared": "3b15177fb5fb3d17"}, "op": "choose"}
dd1ac14d3f864d52 {"guard": {"args": [{"const": true}, {"ref": "f8863.paid"}], "test": "eq"}, "then": {"$shared": "8450769efa1ccdf3"}}
a1c707c69438fcd5 [{"$shared": "ff7152b9011d2a4a"}, {"$shared": "dd1ac14d3f864d52"}]
b0961e8db5c71d11 {"alternatives": {"$shared": "a1c707c69438fcd5"}, "op": "choose"}
10400e59a3b77776 [{"const": false}, {"$shared": "b0961e8db5c71d11"}]
2c7622b420e9928c {"args": {"$shared": "10400e59a3b77776"}, "test": "eq"}
663ba5c3f1d0cec0 {"guard": {"$shared": "2c7622b420e9928c"}, "then": {"param": "edu.no"}}
03e58e98daf82025 [{"const": true}, {"$shared": "b0961e8db5c71d11"}]
8469264f1c6c75ff {"args": {"$shared": "03e58e98daf82025"}, "test": "eq"}
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
dff0b3b99e01c794 {"guard": {"$shared": "8469264f1c6c75ff"}, "then": {"$shared": "b3c9320de87ab6db"}}
b42bdd3d0746f83a [{"$shared": "663ba5c3f1d0cec0"}, {"$shared": "dff0b3b99e01c794"}]
2220337fde3c938d {"alternatives": {"$shared": "b42bdd3d0746f83a"}, "op": "choose"}
0299a5a9032e5318 [{"const": false}, {"$shared": "2220337fde3c938d"}]
2070ed8ab3ddf5f8 {"args": {"$shared": "0299a5a9032e5318"}, "test": "eq"}
bb763fb5bb43315e {"guard": {"$shared": "2070ed8ab3ddf5f8"}, "then": {"const": 0}}
cc133abbb6e4b869 [{"const": true}, {"$shared": "2220337fde3c938d"}]
4ed192eea3d369dd {"args": {"$shared": "cc133abbb6e4b869"}, "test": "eq"}
e2187f51feaa0c68 {"of": [{"input": "dependent.edu_inst"}, {"input": "dependent.edu_mat"}], "op": "sum"}
554916272e95c982 {"guard": {"$shared": "2c7622b420e9928c"}, "then": {"const": 0}}
58614b8ab412763f [{"input": "dependent.edu_a_next_year"}, {"input": "dependent.edu_a_this_year"}, {"input": "dependent.edu_refunds"}]
60a124017e8fbd31 {"of": {"$shared": "58614b8ab412763f"}, "op": "sum"}
cb0e7a1a83e8ffd0 {"guard": {"$shared": "8469264f1c6c75ff"}, "then": {"$shared": "60a124017e8fbd31"}}
41c87c0a8f6c4c41 [{"$shared": "554916272e95c982"}, {"$shared": "cb0e7a1a83e8ffd0"}]
969c91f05b577996 {"alternatives": {"$shared": "41c87c0a8f6c4c41"}, "op": "choose"}
894b2ce393a2a65e {"from": {"$shared": "e2187f51feaa0c68"}, "op": "subtract_floor0", "take": {"$shared": "969c91f05b577996"}}
d6973f91188015c7 [{"$shared": "894b2ce393a2a65e"}, {"param": "aoc.expense_cap"}]
e9977107c62432dc {"of": {"$shared": "d6973f91188015c7"}, "op": "smaller_of"}
75ff791dd1a5e24b {"args": [{"const": true}, {"input": "dependent.edu_tin_issued"}], "test": "eq"}
638448ee9d038a7b [{"$shared": "fd19247f4fee5692"}, {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.edu_1098t"}], "test": "eq"}, {"$shared": "75ff791dd1a5e24b"}]
6a3182f53cb6c109 {"args": {"$shared": "638448ee9d038a7b"}, "test": "all"}
802f9e52e784a13b [{"$shared": "6a3182f53cb6c109"}, {"args": [{"const": false}, {"line": "23"}], "test": "eq"}, {"args": [{"const": false}, {"line": "25"}], "test": "eq"}, {"args": [{"const": false}, {"line": "26"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.edu_ein"}], "test": "eq"}, {"args": [{"const": true}, {"line": "24"}], "test": "eq"}]
d78ee4e4ba19d64b {"args": {"$shared": "802f9e52e784a13b"}, "test": "all"}
be61e1100dccc68c {"args": [{"const": true}, {"input": "dependent.edu_tin_issued"}], "test": "ne"}
d303fa93d1006477 [{"$shared": "d590ca39f5be6faa"}, {"args": [{"const": true}, {"input": "dependent.edu"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.edu_1098t"}], "test": "ne"}, {"$shared": "be61e1100dccc68c"}]
9333ffdf81639789 {"args": {"$shared": "d303fa93d1006477"}, "test": "any"}
6da38407cdd98baa [{"$shared": "9333ffdf81639789"}, {"args": [{"const": false}, {"line": "23"}], "test": "ne"}, {"args": [{"const": false}, {"line": "25"}], "test": "ne"}, {"args": [{"const": false}, {"line": "26"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.edu_ein"}], "test": "ne"}, {"args": [{"const": true}, {"line": "24"}], "test": "ne"}]
9b9de7014713a49d {"args": {"$shared": "6da38407cdd98baa"}, "test": "any"}
d1c097257d730ccd {"from": {"$shared": "e9977107c62432dc"}, "op": "subtract_floor0", "take": {"param": "aoc.full_band"}}
e6e4eeb660c6a99e {"amount": {"$shared": "d1c097257d730ccd"}, "op": "multiply_rate", "rate": {"param": "aoc.second_rate"}}
0f4c5346ced7745e [{"const": 0}, {"$shared": "d1c097257d730ccd"}]
<!-- end -->
