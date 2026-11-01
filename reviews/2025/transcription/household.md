# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-31 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 90aca9bdfd4d2700964bfc078a545034b8f20863224cfe41b31034a84ac845ef |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 0df870171290385204121da1f8c9d313996239db0a6896e046fe6e16be36748f |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 5ee788cba783257784151e57c5c3df3340b30fa22691f1858e75fd7517f54fe9 |
| printed lines compared | 14 |
| agree / disagree / missing | 6 / 8 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
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
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": null}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": null}], "test": "ne"}], "test": "all"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}
```

Second transcription's note: The pages do not define this check. It is read as a roster consistency test: exactly one taxpayer entry, two persons on a joint return (the Form 1040 header names the spouse only 'if joint return'), and one person otherwise.

Ruling: ambiguity; amb.2025.filer_under_16 (owner's entry check); f1040 p. 1: "If joint return, spouse's first name and middle initial". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply restates through helpers (household.h_mfj, household.h_taxpayers) the roster test ruled since round 1: exactly one taxpayer entry, two person entries on a joint return and one otherwise, the complement of household.roster_ok, without the owner's under-16 check. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,109 of 2,122 agree; 12 project-unknown, 1 project-refuses; on returns the full interview completes: none. The 12 project-unknown are fixtures without person.under16 (classm.f8889.3 and .deepseek, stage16.hsa.partial.H01, H02 and others, ss.person.separation; incomplete returns); the project-refuses is audit.household.filer_under16, the owner's check. As ruled in the T-091 round. Project stands.

### household.hsa_both — You and your spouse each have a Form 8889
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 2, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 1, "type": "Count"}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "le"}}], "test": "eq"}
```

Second transcription's note: i8889: 'If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you.' This is read as both person entries having a Form 8889.

Ruling: representation; i8889 p. 4: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you." The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The project counts people with more than zero Forms 8889 and tests exactly two; the reply counts people with at least one and tests exactly two. Above zero and at least one are the same test on a count. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,122 of 2,122 agree; no difference (observed equivalence on that sample). As ruled in the T-091 round. Project stands.

### household.hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **AGREE**

### household.hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **AGREE**

### household.hsa_step1_sum — Both spouses Step 1 limits added together
Status: **AGREE**

### household.hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **AGREE**

### household.all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.eic_ssn"}], "test": "eq"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "person.eic_ssn"}], "test": "eq"}}], "test": "eq"}
```

Ruling: representation; i1040gi p. 40, EIC Step 1, question 2 ("Do you, and your spouse if filing a joint return, have a social security number ... that allows you to work and is valid for EIC purposes"). The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The project compares the count of people answering yes with all people; the reply tests that no person answers no. On a Bool answered for every person these are the same test. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,122 of 2,122 agree; no difference (observed equivalence on that sample). As ruled in the T-091 round. Project stands.

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}], "test": "eq"}
```

Ruling: representation; i1040gi p. 17, Before you begin: "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN"; p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The project requires every person to have person.tin or person.itin_applied; the reply requires that no person answers no to both. That is the same test (De Morgan). executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,122 of 2,122 agree; no difference (observed equivalence on that sample). As ruled in the T-091 round. Project stands.

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "le"}], "test": "all"}
```

Second transcription's note: Open point: whether an ITIN that has only been applied for satisfies the other spouse's requirement. The CTC text says 'issued on or before the due date' and, unlike the ODC text, has no 'answer Yes if applying' clause. Chosen reading: only an issued SSN or ITIN (person.tin) counts.

Ruling: representation; i1040gi p. 17, Before you begin: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)"; amb.2025.ctc_spouse_itin_application, reading 1, chosen. The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply is new in form: it requires that no person answers no to person.tin (an SSN or ITIN issued on or before the due date) and that at least one person has a work SSN. The project accepts person.tin or person.work_ssn for each person. An SSN valid for employment issued before the due date (person.work_ssn) is an SSN issued by then, so on consistent answers work_ssn yes implies tin yes and the two tests agree. Its note excludes an applied-for ITIN, as the chosen reading does. Unlike the round-1 reply ruled a model error, this one does not count itin_applied. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,098 of 2,122 agree; 17 value, 7 candidate-unknown; on returns the full interview completes: 1 value. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.full.json; the uncapped rerun reproduces the recorded counts exactly): the one completed difference is generated 147, a single filer answering person.tin no and person.work_ssn yes, which contradict each other. Project yes, candidate no. Off completed returns: 16 value of the same contradiction on refused returns (classm.otjob.2, classm.sc.3, classm.ssb.2, classm.tcw.8, .10, .11; generated 45, 47, 98, 99, 106, 157, 425, 428, 470, 480). The 7 candidate-unknown are fixtures that omit person.tin for a person with a work SSN, all refused or incomplete (stage16.cleanup.refuse.rrta_medicare, stage16.cleanup.f5695_no_audit and five others). Project stands.

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

Ruling: representation; i1040gi p. 18, Step 3, question 4, the question asked of you, read by Schedule 1-A (forms/2025/s1a.yaml, s1a.line36a_senior). The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The count of taxpayer entries with work_ssn yes is above zero in the project and at least one in the reply, the same test on a count. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,122 of 2,122 agree; no difference (observed equivalence on that sample). As ruled in the T-091 round. Project stands.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Test 1 is a home kept up for a parent (dependent.parent_home_paid within dependent.hoh_test1), so it does not require household.home_cost. Test 2 requires paying over half the cost of keeping up your own home, so household.home_cost is required for it, even if dependent.hoh_test2 already includes that test.

Ruling: scope; i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; p501 p. 9, Temporary absences: "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence."; i1040gi p. 23 (amb.2025.hoh_community_property). The line's test is unchanged; the T-091 correction moved the absence refusal from dependent.hoh_test2 to the gate household.hoh_absence on household.hoh_eligible, which this line reads. The reply restores the f1040.status test it dropped in the T-091 round. It writes the project's test inline: status hoh, and not (unmarried and a Test 1 person), and not (unmarried, home_cost and a Test 2 person). Its Test 2 count reads dependent.hoh_test2, which now excludes a person who counted an absence head of household does not count. It lists neither of the project's refusals on household.hoh_eligible: the community property one and the new absence one. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,119 of 2,122 agree; 2 project-refuses, 1 project-unknown; on returns the full interview completes: none. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.full.json; the uncapped rerun reproduces the recorded counts exactly): there is none. Off completed returns: t091.absence.hoh_refused, refused by the project at household.hoh_absence, where the reply says head of household fails; audit.household.hoh_community_property, refused by the community property screen; and a partial record of classm.dependent.7.deepseek withholding household.community_property, which only that screen needs (incomplete). On the absence case the reply's 'fails' is not decided by the answers. The filer counted an absence p501 p. 9 does not count, and without it the child may still have lived with the filer more than half the year. The project refuses that recount with a cited gate. Both differences are cited project refusals. Project stands.

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

Second transcription's note: Open point: the pages say only that 'Different rules apply to people in community property states' for married persons filing separately, and that a registered domestic partner in Nevada, Washington or California must generally report half the combined community income. Chosen reading: true for any registered domestic partner, or for a married person (including one considered unmarried for head of household) who lived in a community property state and is not filing jointly.

Ruling: model error; i1040gi p. 23, Community Property States: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner"; p501 p. 6 (registered domestic partners aren't lawfully married for federal tax purposes); p525 p. 24. The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply is the one ruled in the T-091 round. It is true for any registered domestic partner wherever they lived and on any status, or for a married filer in a community property state not filing jointly. So it needs household.rdp from every filer and refuses a partner outside a community property state. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 595 of 2,122 agree; 1,526 candidate-unknown, 1 value; on returns the full interview completes: 220 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.full.json; the uncapped rerun reproduces the recorded counts exactly): all 220 are household.rdp asked where the project does not ask it (113 single, 47 joint, 41 head of household, 19 qualifying surviving spouse; community_property not answered yes; for example classm.f8889.1.deepseek, classm.f4952.1.deepseek). The one value is audit.household.hoh_community_property, refused by the project's own screen. Project stands.

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.h_mfj
    printed: "(helper)"
    label: "Filing status is married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: household.persons
    printed: "(helper)"
    label: "Number of persons on the return (you, and your spouse if filing jointly)"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one}
    note: "The pages do not define this interface. It is read as the count of entries in the person collection."

  - id: household.h_taxpayers
    printed: "(helper)"
    label: "Number of person entries marked as the taxpayer"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}

  - id: household.roster_bad
    printed: "(helper)"
    label: "The person entries do not match the filing status (a joint return lists you and your spouse; any other return lists only you)"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [household.h_mfj, {const: true}]}
            - {op: test, ne: [household.persons, {const: 2, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [household.h_mfj, {const: false}]}
            - {op: test, ne: [household.persons, {const: 1, type: Count}]}
        - {op: test, ne: [household.h_taxpayers, {const: 1, type: Count}]}
    note: "The pages do not define this check. It is read as a roster consistency test: exactly one taxpayer entry, two persons on a joint return (the Form 1040 header names the spouse only 'if joint return'), and one person otherwise."

  - id: household.h_hsa_persons
    printed: "(helper)"
    label: "Number of persons with at least one Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, ge: [person.hsa_forms, {const: 1, type: Count}]}

  - id: household.hsa_both
    printed: "(helper)"
    label: "Both you and your spouse have HSAs (a separate Form 8889 for each of you)"
    type: Bool
    expr: {op: test, eq: [household.h_hsa_persons, {const: 2, type: Count}]}
    note: "i8889: 'If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you.' This is read as both person entries having a Form 8889."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of persons whose line 6 uses the spouses' division of the family contribution limit"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of persons using an agreed (non-equal) allocation of the family contribution limit"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total of the spouses' Step 1 refigured family contribution limits (i8889, line 6)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total of the spouses' allocated shares of the family contribution limit (i8889, line 6)"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}

  - id: household.h_no_eic_ssn
    printed: "(helper)"
    label: "Number of persons on the return without an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.eic_ssn, {const: false}]}

  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "Do you, and your spouse if filing a joint return, have a social security number issued on or before the due date of your 2025 return (including extensions) that allows you to work and is valid for EIC purposes?"
    type: Bool
    expr: {op: test, eq: [household.h_no_eic_ssn, {const: 0, type: Count}]}

  - id: household.h_no_tin
    printed: "(helper)"
    label: "Number of persons on the return with neither an SSN or ITIN issued nor an ITIN applied for by the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.tin, {const: false}]}
          - {op: test, eq: [person.itin_applied, {const: false}]}

  - id: household.all_tin
    printed: "(helper)"
    label: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)"
    type: Bool
    expr: {op: test, eq: [household.h_no_tin, {const: 0, type: Count}]}

  - id: household.h_no_issued_tin
    printed: "(helper)"
    label: "Number of persons on the return without an SSN or ITIN issued on or before the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.tin, {const: false}]}

  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Number of persons on the return with an SSN valid for employment issued before the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "To claim the child tax credit, you must have a valid SSN (valid for employment and issued before the due date of your return, including extensions). If you are filing a joint return, only one spouse is required to have a valid SSN; the other spouse must have either an SSN or ITIN issued on or before the due date of the return."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_work_ssn_count, {const: 1, type: Count}]}
        - {op: test, eq: [household.h_no_issued_tin, {const: 0, type: Count}]}
    note: "Open point: whether an ITIN that has only been applied for satisfies the other spouse's requirement. The CTC text says 'issued on or before the due date' and, unlike the ODC text, has no 'answer Yes if applying' clause. Chosen reading: only an issued SSN or ITIN (person.tin) counts."

  - id: household.h_tp_work_ssn
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
    label: "You (the taxpayer) have an SSN valid for employment and issued before the due date of your 2025 return (including extensions)"
    type: Bool
    expr: {op: test, ge: [household.h_tp_work_ssn, {const: 1, type: Count}]}

  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Number of dependents meeting head of household Test 1 (parent whose main home you kept up)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}

  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Number of persons meeting head of household Test 2 (qualifying person who lived with you more than half the year)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household is checked, but you are not unmarried (or considered unmarried) with Test 1 or Test 2 applying"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - op: test
          not:
            op: test
            any:
              - op: test
                all:
                  - {op: test, eq: [household.unmarried, {const: true}]}
                  - {op: test, ge: [household.h_hoh_test1_count, {const: 1, type: Count}]}
              - op: test
                all:
                  - {op: test, eq: [household.unmarried, {const: true}]}
                  - {op: test, eq: [household.home_cost, {const: true}]}
                  - {op: test, ge: [household.h_hoh_test2_count, {const: 1, type: Count}]}
    note: "Test 1 is a home kept up for a parent (dependent.parent_home_paid within dependent.hoh_test1), so it does not require household.home_cost. Test 2 requires paying over half the cost of keeping up your own home, so household.home_cost is required for it, even if dependent.hoh_test2 already includes that test."

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse is checked, but not all five tests apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}

  - id: household.rdp_community_property
    printed: "(helper)"
    label: "Community property or registered domestic partner rules apply (Form 8958 and Pub. 555)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [household.rdp, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [household.community_property, {const: true}]}
            - {op: test, eq: [household.married, {const: true}]}
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
    note: "Open point: the pages say only that 'Different rules apply to people in community property states' for married persons filing separately, and that a registered domestic partner in Nevada, Washington or California must generally report half the combined community income. Chosen reading: true for any registered domestic partner, or for a married person (including one considered unmarried for head of household) who lived in a community property state and is not filing jointly."
```
```
