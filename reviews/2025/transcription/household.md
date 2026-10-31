# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 20460f60f93e60360ace56e23ed67587f157939d543b7362380df6b7a2331a5a |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 2daedd54c7065412acfd38a4ff0b9956199a2cfbbd2fced35708cade10343bdb |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7d0ff1a29d2512bac17273d2cc50c6421e6477a74270ba05b652f1366c503bc6 |
| printed lines compared | 14 |
| agree / disagree / missing | 8 / 6 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | - | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
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

Second transcription's note: The pages do not state a roster check. It is inferred from i1040 and i8889, which treat a spouse as part of the return only when filing jointly, and a married filing separately filer generally reports only their own items. Chosen reading: exactly one taxpayer entry, exactly one spouse entry on mfj, and no spouse entry on any other status.

Ruling: ambiguity; amb.2025.filer_under_16 (owner's entry check); f1040 p. 1: "If joint return, spouse's first name and middle initial". The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). The candidate's roster test is the exact complement of household.roster_ok. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,084 of 2,096 agree; 11 project-unknown, 1 project-refuses; on returns the full interview completes: none. No completed-return difference: the 11 project-unknown are fixtures without person.under16 (classm.f8889.3 and .deepseek, stage16.hsa.partial.H01 and others; incomplete returns) and the one project-refuses is audit.household.filer_under16, the owner's under-16 check. As ruled since round 1. Project stands.

### household.hsa_both — You and your spouse each have a Form 8889
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "le"}
```

Second transcription's note: Read as both people on the return having a Form 8889. A person's having a Form 8889 stands for having an HSA, because the interface has no separate HSA-ownership field at this level.

Ruling: representation; i8889 p. 4: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you." The project tests exactly two people with a Form 8889; the candidate tests at least two people with at least one Form 8889 each. household.roster_bad admits at most two person entries, and a count of forms above zero and at least one are the same test. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,096 of 2,096 agree; no difference (observed equivalence on that sample). The reply is identical to fix round 4's. Project stands.

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

Second transcription's note: Open point: the other spouse's number. The child tax credit text says the number must have been issued by the due date and has no 'answer Yes if applying' wording, so an ITIN application alone does not count here. The child's own SSN is tested per dependent, not on this line.

Ruling: representation; i1040gi p. 17, Before you begin: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)"; amb.2025.ctc_spouse_itin_application (session reading under the owner's delegation, 2026-10-30), reading 1, chosen. The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). It reads person.tin or a work SSN for every person, as the project, and compares the work-SSN count as at least 1 instead of above 0, the same test. The difference is the refusal: the round-4 reply listed household.credit_disallowed on this line (ruled scope); this reply lists none (its note puts credit_disallowed on the credit lines, where the project applies it), so nothing differs. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,096 of 2,096 agree; no difference (observed equivalence on that sample). Project stands.

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

Second transcription's note: The pages do not name this result separately. Read as the taxpayer's own entry having an SSN valid for employment, whatever the spouse has.

Ruling: representation; i1040gi p. 18, Step 3, question 4. The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). A count of taxpayer entries with work_ssn above zero and a count of at least one are the same test. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,096 of 2,096 agree; no difference (observed equivalence on that sample). Project stands.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Open point: whether this result depends on the status claimed. Chosen reading: it is true only when head of household is the status claimed. Test 2 uses household.home_cost (your own home), while Test 1 concerns the parent's home, whose cost is assumed to be inside dependent.hoh_test1. The per-person qualifying tests, including the exclusions in Test 2 items 1a to 1c, are assumed to be inside dependent.hoh_test1 and dependent.hoh_test2, whose computations are not supplied.

Ruling: scope; i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; p. 23, Community Property States (amb.2025.hoh_community_property, the owner's decision of 2026-10-22). The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). The candidate writes the project's head of household test inline, with each Test 1 and Test 2 count compared as at least 1 instead of above 0, and so drops the refusal household.hoh_community_property that the project carries on household.hoh_eligible. It tests household.home_cost where the project does; BUG-0258's and BUG-0260's definitions change the question's wording, not the line. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,093 of 2,096 agree; 2 project-unknown, 1 project-refuses; on returns the full interview completes: none. No completed-return difference: the project-refuses is audit.household.hoh_community_property (the cited screen), and the 2 project-unknown are partial records withholding household.community_property (classm.f1040.5.deepseek, classm.f5329.3.deepseek). BUG-0257 (count lower bounds under a pending refusal gate) changes no witness here. Project stands.

### household.qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **AGREE**

### household.rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}], "test": "any"}
```

Second transcription's note: Open point: the pages say different rules apply to people in community property states but give no explicit trigger. Chosen reading: true for a registered domestic partner, or for someone married at the end of 2025, not filing jointly, who lived in a community property state. That includes a married person considered unmarried for head of household, as household.married does. A joint return is left out because both spouses' income is on it.

Ruling: model error; i1040gi p. 23, Community Property States: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner"; p525 p. 24, Registered domestic partners (RDPs) domiciled in community property states; p501 p. 6 (registered domestic partners aren't lawfully married for federal tax purposes). The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). The candidate refuses any registered domestic partner wherever they lived and whatever the filing status, and any married filer not filing jointly in a community property state (which repeats household.hoh_community_property and s3.mfs). It therefore needs household.rdp from joint filers and from filers who lived in no community property state. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 570 of 2,096 agree; 1,525 candidate-unknown, 1 value; on returns the full interview completes: 634 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.full.json; the uncapped rerun reproduces the recorded counts exactly): all 634 are household.rdp asked where the project does not ask it: 144 joint returns (141 with community_property no, 3 without the answer) and 490 non-joint returns with community_property no (340 single, 131 head of household, 19 qualifying surviving spouse; for example classm.f2441.1.deepseek). The one value is on audit.household.hoh_community_property, refused by the project's own screen. Project stands.

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.persons
    printed: "(helper)"
    label: "Number of people on the return (you, and your spouse if filing a joint return)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
    note: "The pages do not name this figure. Read as the count of entries in the person collection."

  - id: household.h_taxpayers
    printed: "(helper)"
    label: "Number of person entries for the taxpayer"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}

  - id: household.h_spouses
    printed: "(helper)"
    label: "Number of person entries for the spouse"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "spouse"}]}

  - id: household.roster_bad
    printed: "(helper)"
    label: "The people entered do not match the filing status: one taxpayer on every return, and a spouse entry only on a joint return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ne: [household.h_taxpayers, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, ne: [household.h_spouses, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, ne: [household.h_spouses, {const: 0, type: Count}]}
    note: "The pages do not state a roster check. It is inferred from i1040 and i8889, which treat a spouse as part of the return only when filing jointly, and a married filing separately filer generally reports only their own items. Chosen reading: exactly one taxpayer entry, exactly one spouse entry on mfj, and no spouse entry on any other status."

  - id: household.h_hsa_people
    printed: "(helper)"
    label: "Number of people on the return with a Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, gt: [person.hsa_forms, {const: 0, type: Count}]}

  - id: household.hsa_both
    printed: "(helper)"
    label: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you"
    type: Bool
    expr:
      op: test
      ge: [household.h_hsa_people, {const: 2, type: Count}]
    note: "Read as both people on the return having a Form 8889. A person's having a Form 8889 stands for having an HSA, because the interface has no separate HSA-ownership field at this level."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of Forms 8889 on the return that divide the family contribution limit between spouses (Form 8889, line 6)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_split

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of Forms 8889 on the return using a different allocation both spouses agree on (Form 8889, line 6)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_agreed

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total over both spouses of the refigured family contribution limit (Form 8889 instructions, line 6, Step 1)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_step1

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total over both spouses of the parts of the family contribution limit allocated to each (Form 8889 instructions, line 6)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_share

  - id: household.h_eic_ssn_count
    printed: "(helper)"
    label: "Number of people on the return with a social security number valid for the EIC"
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
    expr:
      op: test
      eq: [household.h_eic_ssn_count, household.persons]

  - id: household.h_tin_or_applied_count
    printed: "(helper)"
    label: "Number of people on the return with an SSN or ITIN issued on or before the due date, or who are applying for an ITIN by then"
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
    label: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer \"Yes\" if you are applying for an ITIN on or before the return due date (including extensions).)"
    type: Bool
    expr:
      op: test
      eq: [household.h_tin_or_applied_count, household.persons]
    note: "Open point: the line 19 caution says the number must be issued by the due date, while Step 5, question 1 says to answer Yes if applying for an ITIN by then. Chosen reading: follow the Step 5 question, so a timely application counts here."

  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Number of people on the return with an SSN valid for employment and issued before the due date of the return (including extensions)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: household.h_issued_number_count
    printed: "(helper)"
    label: "Number of people on the return with an SSN or ITIN issued on or before the due date of the return"
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
    label: "To claim the child tax credit, you must have a valid SSN. If you are filing a joint return, only one spouse is required to have a valid SSN; the other spouse must have either an SSN or ITIN, issued on or before the due date of the return."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_work_ssn_count, {const: 1, type: Count}]}
        - {op: test, eq: [household.h_issued_number_count, household.persons]}
    note: "Open point: the other spouse's number. The child tax credit text says the number must have been issued by the due date and has no 'answer Yes if applying' wording, so an ITIN application alone does not count here. The child's own SSN is tested per dependent, not on this line."

  - id: household.h_taxpayer_work_ssn_count
    printed: "(helper)"
    label: "Number of taxpayer entries with an SSN valid for employment, issued before the due date of the return (including extensions)"
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
    expr:
      op: test
      ge: [household.h_taxpayer_work_ssn_count, {const: 1, type: Count}]
    note: "The pages do not name this result separately. Read as the taxpayer's own entry having an SSN valid for employment, whatever the spouse has."

  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Number of dependents who meet head of household Test 1 (your parent whom you can claim as a dependent, whose main home for all of 2025 you paid over half the cost of keeping up)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}

  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Number of people who are a qualifying person under head of household Test 2 and lived with you for more than half of the year"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household is checked, but you are not unmarried (or considered unmarried), or neither Test 1 nor Test 2 applies"
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
    note: "Open point: whether this result depends on the status claimed. Chosen reading: it is true only when head of household is the status claimed. Test 2 uses household.home_cost (your own home), while Test 1 concerns the parent's home, whose cost is assumed to be inside dependent.hoh_test1. The per-person qualifying tests, including the exclusions in Test 2 items 1a to 1c, are assumed to be inside dependent.hoh_test1 and dependent.hoh_test2, whose computations are not supplied."

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse is checked, but not all of the five tests apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}
    note: "Like household.hoh_fails, true only when the status is claimed. The five tests are answered together in the household.qss_eligible input. household.credit_disallowed is not listed under refuses on any household line: it concerns the credit claims (Form 8862), and a return claiming none of those credits should not stop here, so it belongs on the credit lines."

  - id: household.rdp_community_property
    printed: "(helper)"
    label: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income; married people filing separately who lived in a community property state follow state law to determine community and separate income (Form 8958 and Pub. 555)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [household.rdp, {const: true}]}
        - op: test
          all:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.married, {const: true}]}
            - {op: test, eq: [household.community_property, {const: true}]}
    note: "Open point: the pages say different rules apply to people in community property states but give no explicit trigger. Chosen reading: true for a registered domestic partner, or for someone married at the end of 2025, not filing jointly, who lived in a community property state. That includes a married person considered unmarried for head of household, as household.married does. A joint return is left out because both spouses' income is on it."
```
```
