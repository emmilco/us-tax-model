# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d7bcff0582d13284000fde1202a0a6c7ad68da9fa35f67cd386b49cb1e9911f5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6b203e8a5df58509f54c7948a3bc96af5c58b0a1c7e432e0e4cbd823d7e79642 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 5466d64fb38b72b9dac93e0afe2ba271ce519579f173651c0c7af2c1e2eeae23 |
| printed lines compared | 17 |
| agree / disagree / missing | 9 / 8 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### household.persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **AGREE**

### household.roster_bad — The people entered do not match the filing status
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}
```

Second transcription's note: The IRS pages do not define this check. Chosen reading: the person collection holds each person on the return, so a joint return has one taxpayer and one spouse entry, and any other status has one taxpayer entry and no spouse entry.

Ruling: scope — The Boolean roster tests agree on complete age-screened records. Form 1040 p. 1 names the taxpayer and, on a joint return, spouse. The project also propagates household.roster_ok's under16 refusal (amb.2025.filer_under_16); the candidate bypasses it. All 12 observed differences are that extra scope prerequisite: 11 project-unknown on incomplete records and one project-refuses. This is not unconditional partial-input equivalence. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2204 agreements; differences by return state {"incomplete": {"project-unknown": 11}, "refused": {"project-refuses": 1}}. Sample witnesses: {"id": "classm.f8889.3.deepseek", "kind": "fixture"}, {"id": "classm.f8889.3", "kind": "fixture"}.

### household.hsa_both — You and your spouse each have a Form 8889
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 1, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "le"}}], "test": "le"}
```

Second transcription's note: Only persons on the return are entered, so this can be true only on a joint return. The closed interface has no input for the HSA of a spouse on a separate return.

Ruling: representation — i8889 p. 4 says to complete separate Forms 8889 if both spouses have HSAs. On a valid roster there are at most two persons, so exactly two and at least two HSA filers coincide (and > 0 vs >= 1 on integral Form 8889 counts coincide). All 2216 comparisons agree; no conclusion is asserted for invalid larger rosters. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.

### household.hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **AGREE**

### household.hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **AGREE**

### household.hsa_step1_sum — Both spouses Step 1 limits added together
Status: **AGREE**

### household.hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **AGREE**

### household.all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **AGREE**

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **AGREE**

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "le"}], "test": "all"}
```

Second transcription's note: Open: Step 5 lets an ITIN application count for the credit for other dependents, but the child tax credit text says the number must have been issued. Chosen reading: person.itin_applied does not count here.

Ruling: representation — i1040gi p. 17, Before you begin (and i1040s8812 p. 2) requires a work-valid SSN for you or your spouse, and an issued SSN/ITIN for the other spouse (amb.2025.ctc_spouse_itin_application). Both expressions require at least one work SSN and every filer to have work_ssn OR tin; the candidate uses >= 1 instead of > 0 on the integral work-SSN count. All 2216 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}
```

Ruling: representation — Both expressions restrict the sum to person.role=taxpayer and person.work_ssn=true (i1040gi p. 18). The Form 1040 identification requirement is taxpayer-specific at this interface; a nonnegative integral count > 0 equals >= 1. All 2216 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Test 1 concerns the cost of a parent's home, which dependent.parent_home_paid asks. Chosen reading: household.home_cost is required only with Test 2, the home in which you lived.

Ruling: scope — i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; i1040gi p. 23; p501 p. 9; amb.2025.hoh_community_property. Both expressions test f1040.status == "hoh" and whether Test 1 or Test 2 is met (using <= 0 vs < 1 on integral person counts); the project reads household.hoh_eligible, which carries the cited household.hoh_community_property and household.hoh_absence refusals, whereas the candidate inlines the Boolean test without those refusals. All 4 observed differences are on incomplete/refused records from those scope gates, with zero completed-return differences. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2212 agreements; differences by return state {"incomplete": {"project-unknown": 1}, "refused": {"project-refuses": 3}}. Sample witnesses: {"id": "stage21.household.community_still_married", "kind": "fixture"}, {"id": "audit.household.hoh_community_property", "kind": "fixture"}.

### household.qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **AGREE**

### household.widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second transcription's note: The guards follow the cases in which household.spouse_died_2025 is asked. A head of household or single filer who remarried cannot be told apart from one who did not; the filing status conflict line treats either answer of Yes as a conflict.

Ruling: model error — p501 p. 6 and i1040gi p. 13 allow married filing jointly when a spouse died in 2025 and the survivor did not remarry. This owner-selected refusal gate (BUG-0277) explicitly applies to "Filing as single or head of household although your spouse died in 2025" (status == "single" or status == "hoh", with spouse_died_2025 == true). The candidate adds an mfj branch (status == "mfj" and married == false and spouse_died_2025 == true), which wrongly turns a valid death-year joint return into a widowed_2025 failure on stage21.household.status_joint_death_year. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2215 agreements; differences by return state {"incomplete": {"value": 1}}. Sample witness: {"id": "stage21.household.status_joint_death_year", "kind": "fixture"}.

### household.cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **AGREE**

### household.rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Second:

```json
{"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}
```

Second transcription's note: Open: whether household.community_property must also be true. The IRS sentence states no further condition and all three states are community property states, so the chosen reading tests household.rdp alone.

Ruling: model error — i1040gi p. 23, Community Property States, and p501 p. 6 describe the registered domestic partner community-income regime. The published gate explicitly applies to a nonjoint return in a community property state (status != "mfj" and community_property == true and rdp == true); the candidate tests household.rdp alone, dropping both applicability guards and demanding the rdp answer on joint and non-community-property returns where the interview does not ask it. All 1,607 observed differences are candidate-unknown (including 226 completed returns), not tax-value disagreements. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 609 agreements; differences by return state {"completed": {"candidate-unknown": 226}, "incomplete": {"candidate-unknown": 796}, "refused": {"candidate-unknown": 585}}. Sample witnesses: {"id": "classm.f8889.1.deepseek", "kind": "fixture"}, {"id": "classm.f4952.1.deepseek", "kind": "fixture"}.

### household.filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second transcription's note: Open: Pub. 501 treats a spouse who died during the year as leaving you considered married, which could allow married filing separately, but household.spouse_died_2025 is not asked for that status. Chosen reading: married filing separately requires household.married to be true, as the Form 1040 instructions say. The head of household unmarried test is left to household.hoh_fails, and a head of household filer whose spouse died in 2025 is a conflict because that filer is considered married for the whole year.

Ruling: scope — i1040gi pp. 13–15 and p501 pp. 6–8. The published gate (BUG-0286) checks the marriage-status entry conflict (single with married == true, or mfj with married == false and spouse_died_2025 == false) and refuses scope.ready alongside the dedicated status gates (s3.mfs for married filing separately, household.widowed_2025 for single/HOH with spouse_died_2025, household.hoh_fails for HOH, and household.qss_fails for QSS). The candidate folds widowed_2025, mfs && !married, and qss && married into this single gate. On completed returns there are zero value differences and only 2 partial-record candidate-unknowns where household.married was withheld on a QSS return; the 128 value differences are all on already-refused returns (such as MFS returns refused by s3.mfs or death-year single/HOH returns refused by widowed_2025). Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2048 agreements; differences by return state {"completed": {"candidate-unknown": 2}, "incomplete": {"candidate-unknown": 23}, "refused": {"candidate-unknown": 15, "value": 128}}. Sample witnesses: {"base": "classm.dependent.3.deepseek", "kind": "partial", "withheld": "household.married"}, {"base": "classm.f5695.2.deepseek", "kind": "partial", "withheld": "household.married"}.

## Raw second transcription

```yaml
lines:
  - id: household.persons
    printed: "(helper)"
    label: "Number of persons on the return: you, and your spouse if filing a joint return"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one}
  - id: household.h_taxpayer_entries
    printed: "(helper)"
    label: "Number of person entries for you (the taxpayer)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}
  - id: household.h_spouse_entries
    printed: "(helper)"
    label: "Number of person entries for your spouse"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "spouse"}]}
  - id: household.roster_bad
    printed: "(helper)"
    label: "The person entries do not match the filing status: one entry for you, plus one for your spouse only if filing a joint return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ne: [household.h_taxpayer_entries, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, ne: [household.h_spouse_entries, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, ne: [household.h_spouse_entries, {const: 0, type: Count}]}
    note: "The IRS pages do not define this check. Chosen reading: the person collection holds each person on the return, so a joint return has one taxpayer and one spouse entry, and any other status has one taxpayer entry and no spouse entry."
  - id: household.h_hsa_persons
    printed: "(helper)"
    label: "Number of persons on the return with a Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, ge: [person.hsa_forms, {const: 1, type: Count}]}
  - id: household.hsa_both
    printed: "(helper)"
    label: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you"
    type: Bool
    expr: {op: test, ge: [household.h_hsa_persons, {const: 2, type: Count}]}
    note: "Only persons on the return are entered, so this can be true only on a joint return. The closed interface has no input for the HSA of a spouse on a separate return."
  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of Forms 8889 on which spouses with separate HSAs and family coverage divide the contribution limit (Form 8889, line 6)"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}
  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of Forms 8889 using a different allocation both spouses agree on (Form 8889, line 6)"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}
  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total over the persons on the return of the refigured contribution limit from Step 1 (Form 8889, line 6)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}
  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total over the persons on the return of the shares of the contribution limit allocated to each spouse (Form 8889, line 6)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}
  - id: household.h_eic_ssn_persons
    printed: "(helper)"
    label: "Number of persons on the return with a social security number valid for EIC purposes"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.eic_ssn, {const: true}]}
  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "Do you, and your spouse if filing a joint return, have a social security number issued on or before the due date of your 2025 return (including extensions) that allows you to work and is valid for EIC purposes?"
    type: Bool
    expr: {op: test, eq: [household.h_eic_ssn_persons, household.persons]}
  - id: household.h_tin_persons
    printed: "(helper)"
    label: "Number of persons on the return with an SSN or ITIN issued on or before the due date, or applying for an ITIN by then"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        any:
          - {op: test, eq: [person.tin, {const: true}]}
          - {op: test, eq: [person.itin_applied, {const: true}]}
  - id: household.all_tin
    printed: "(helper)"
    label: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer Yes if you are applying for an ITIN on or before the return due date (including extensions).)"
    type: Bool
    expr: {op: test, eq: [household.h_tin_persons, household.persons]}
  - id: household.h_work_ssn_persons
    printed: "(helper)"
    label: "Number of persons on the return with an SSN valid for employment and issued before the due date of the return (including extensions)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}
  - id: household.h_ctc_id_persons
    printed: "(helper)"
    label: "Number of persons on the return with an SSN or ITIN issued on or before the due date of the return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        any:
          - {op: test, eq: [person.tin, {const: true}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
  - id: household.ctc_ssn
    printed: "(helper)"
    label: "You must have a valid SSN to claim the child tax credit. If you are filing a joint return, only one spouse is required to have a valid SSN; the other spouse must have either an SSN or ITIN issued on or before the due date of the return (including extensions)."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_work_ssn_persons, {const: 1, type: Count}]}
        - {op: test, eq: [household.h_ctc_id_persons, household.persons]}
    note: "Open: Step 5 lets an ITIN application count for the credit for other dependents, but the child tax credit text says the number must have been issued. Chosen reading: person.itin_applied does not count here."
  - id: household.h_taxpayer_work_ssn_count
    printed: "(helper)"
    label: "Number of taxpayer entries with an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}
  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "You have an SSN valid for employment and issued before the due date of your return (including extensions)"
    type: Bool
    expr: {op: test, ge: [household.h_taxpayer_work_ssn_count, {const: 1, type: Count}]}
  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Number of persons meeting head of household Test 1"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}
  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Number of persons meeting the person conditions of head of household Test 2"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}
  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household is checked, but you are not unmarried (or considered unmarried) with either Test 1 or Test 2 applying"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - op: test
          not:
            op: test
            all:
              - {op: test, eq: [household.unmarried, {const: true}]}
              - op: test
                any:
                  - {op: test, ge: [household.h_hoh_test1_count, {const: 1, type: Count}]}
                  - op: test
                    all:
                      - {op: test, eq: [household.home_cost, {const: true}]}
                      - {op: test, ge: [household.h_hoh_test2_count, {const: 1, type: Count}]}
    note: "Test 1 concerns the cost of a parent's home, which dependent.parent_home_paid asks. Chosen reading: household.home_cost is required only with Test 2, the home in which you lived."
  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse is checked, but not all of the five qualifying surviving spouse tests apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}
  - id: household.widowed_2025
    printed: "(helper)"
    label: "Your spouse died in 2025 and you didn't remarry in 2025"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "single"}]}
            - {op: test, eq: [household.spouse_died_2025, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "hoh"}]}
            - {op: test, eq: [household.spouse_died_2025, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.married, {const: false}]}
            - {op: test, eq: [household.spouse_died_2025, {const: true}]}
    note: "The guards follow the cases in which household.spouse_died_2025 is asked. A head of household or single filer who remarried cannot be told apart from one who did not; the filing status conflict line treats either answer of Yes as a conflict."
  - id: household.cp_marriage_ended
    printed: "(helper)"
    label: "You were considered married for part of the year and lived in a community property state, with the marriage ended by divorce or legal separation before the end of 2025, and you are not filing jointly"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.community_property, {const: true}]}
        - {op: test, ne: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [household.married, {const: false}]}
        - {op: test, eq: [household.cp_married, {const: true}]}
  - id: household.rdp_community_property
    printed: "(helper)"
    label: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner."
    type: Bool
    expr: {op: test, eq: [household.rdp, {const: true}]}
    note: "Open: whether household.community_property must also be true. The IRS sentence states no further condition and all three states are community property states, so the chosen reading tests household.rdp alone."
  - id: household.filing_status_conflict
    printed: "(helper)"
    label: "The filing status checked does not agree with your marital status at the end of 2025"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "single"}]}
            - op: test
              any:
                - {op: test, eq: [household.married, {const: true}]}
                - {op: test, eq: [household.widowed_2025, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.married, {const: false}]}
            - {op: test, eq: [household.spouse_died_2025, {const: false}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfs"}]}
            - {op: test, eq: [household.married, {const: false}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "hoh"}]}
            - {op: test, eq: [household.widowed_2025, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "qss"}]}
            - {op: test, eq: [household.married, {const: true}]}
    note: "Open: Pub. 501 treats a spouse who died during the year as leaving you considered married, which could allow married filing separately, but household.spouse_died_2025 is not asked for that status. Chosen reading: married filing separately requires household.married to be true, as the Form 1040 instructions say. The head of household unmarried test is left to household.hoh_fails, and a head of household filer whose spouse died in 2025 is a conflict because that filer is considered married for the whole year."
```
