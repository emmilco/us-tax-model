# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-31 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 90aca9bdfd4d2700964bfc078a545034b8f20863224cfe41b31034a84ac845ef |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 45bf53c1a1842c7fd78dec17ee8b73636af9f598c8d3d3357a9c362a65af9b4e |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": null}], "op": "sum"}
```

Second transcription's note: Chosen reading: tax family size is the person entries plus the dependents listed.

Ruling: model error; f1040 p. 1, "Your first name and middle initial" and "If joint return, spouse's first name and middle initial". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The line counts the people on the return (you, and your spouse if filing jointly). The reply adds every dependent entry ("tax family size"), so every consumer of the count, including household.all_eic_ssn, all_tin and ctc_ssn, which compare a count of people with household.persons, gets a wrong count on any return listing a dependent. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 1,139 of 2,122 agree; 948 value, 35 candidate-unknown; on returns the full interview completes: 207 value. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): all 207 are value differences on returns listing dependents, the candidate higher by the number of dependent entries (96 by 3, 60 by 1, 51 by 2; 82 single, 52 head of household, 37 joint, 36 qualifying surviving spouse; for example classm.f8889.1.deepseek, classm.f4952.1.deepseek, classm.f8960.1.deepseek). Off completed returns: 741 value of the same kind and 35 candidate-unknown where the dependent roster is unconfirmed. As ruled in fix round 5 ("Adds dependent entries"). Project stands.

### household.roster_bad — The people entered do not match the filing status
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}], "test": "all"}}], "test": "lt"}
```

Second transcription's note: Chosen reading: bad roster means at least one claimed dependent fails both dependent definitions.

Ruling: model error; f1040 p. 1, "Your first name and middle initial" and "If joint return, spouse's first name and middle initial". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The line checks the person entries against the filing status. The reply never reads the person collection or f1040.status. It is true when a claimed dependent entry is neither dependent.qc_dependent nor dependent.qr_dependent, so it accepts any roster mismatch and inherits every dependent refusal. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 1,951 of 2,122 agree; 143 candidate-refuses, 25 candidate-unknown, 2 value, 1 project-refuses; on returns the full interview completes: none. No completed-return difference. Off completed returns: the 2 values are exactly the roster mismatches the line exists to catch, stage13.refuse.joint_without_spouse and stage13.refuse.single_with_spouse (project yes, candidate no). The 143 candidate-refuses are dependent refusals the project does not reach here (claimed_no_tin 48, other_claimant 30, divorced_rule 24, married 20, multiple_support 13, income_exception 5, qr_kidnapped 2, kidnapped 1). The 25 candidate-unknown are unconfirmed dependent rosters (23) and dependent.kidnapped unanswered (2). The project-refuses is audit.household.filer_under16, the owner's check (amb.2025.filer_under_16). Project stands.

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

Second transcription's note: Chosen reading: both spouse person entries have at least one Form 8889.

Ruling: representation; i8889 p. 4: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you." The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply counts person entries whose person.hsa_forms (the number of Forms 8889 entered for the person) is above zero and tests at least two. The project tests exactly two people with more than zero forms. household.roster_bad admits at most two person entries, so at least two and exactly two coincide. Unlike its T-091-round reply, it no longer adds household.married. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,122 of 2,122 agree; no difference (observed equivalence on that sample). Project stands.

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
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"ref": "dependent.eic_ssn"}], "test": "ne"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.eic_ssn"}], "test": "ne"}}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Chosen reading: taxpayer, spouse and each EIC qualifying child must have an EIC-valid SSN.

Ruling: model error; i1040gi p. 40, EIC Step 1, question 2: "Do you, and your spouse if filing a joint return, have a social security number ... that allows you to work and is valid for EIC purposes". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The line is the filers' test. The reply adds that every dependent.eic_child has dependent.eic_ssn. That test belongs to each child separately: a child without a valid SSN is not counted as a qualifying child, and it does not deny the credit to the filers. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 1,972 of 2,122 agree; 73 candidate-unknown, 57 candidate-refuses, 20 value; on returns the full interview completes: 2 value. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): both are single filers with an EIC-valid SSN listing an EIC child without one (generated 29 and 242): project yes, candidate no. Off completed returns: 18 value of the same kind (17 refused, 1 incomplete). The 57 candidate-refuses and 73 candidate-unknown come from reading dependent.eic_child (other_claimant, married and kidnapped refusals; dependent.us_half unanswered; unconfirmed rosters). As ruled in fix round 5 ("Adds every dependent entry's EIC SSN"). Project stands.

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "dependent.tin"}], "test": "ne"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.tin"}], "test": "ne"}}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Chosen reading: every person entry and every dependent must have a TIN issued by the return due date.

Ruling: model error; i1040gi p. 17, Before you begin: "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)"; p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply has the filers' test without the applied-for ITIN, and it adds that every dependent entry has dependent.tin, a test the source applies to each person separately (i1040gi p. 18, Step 3, question 1). executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,043 of 2,122 agree; 79 value; on returns the full interview completes: none. No completed-return difference. Off completed returns: 79 value, project yes and candidate no; 76 are refused returns (for example classm.dependent.7.deepseek) and 3 incomplete. As ruled in the T-091 round. Project stands.

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"ref": "dependent.work_ssn"}], "test": "ne"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second transcription's note: Chosen reading: one spouse's work-valid SSN suffices for the taxpayer side; each CTC child must have one.

Ruling: model error; i1040gi p. 17, Before you begin: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)". The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The line is the filers' identification test. The reply requires its own household.taxpayer_work_ssn (any person's work SSN) and that every dependent.ctc_child has a work SSN. dependent.ctc_child reads household.ctc_ssn, so the line is a cycle, unknown wherever a dependent entry exists. It also drops the other spouse's SSN-or-ITIN test. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 1,650 of 2,122 agree; 400 candidate-unknown, 72 candidate-refuses; on returns the full interview completes: 103 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): all 103 are "cycle at household.h_ctc_work_fail_count" (43 head of household, 30 single, 16 qualifying surviving spouse, 14 joint; for example classm.f4952.1.deepseek, classm.f8960.1.deepseek). Off completed returns: 297 of the same cycle and 72 candidate-refuses, dependent refusals reached through dependent.ctc_child (other_claimant, divorced_rule, married, kidnapped). As ruled in the T-091 round. Project stands.

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}
```

Ruling: model error; i1040gi p. 18, Step 3, question 4; the line is the question "Do you have an SSN valid for employment issued before the due date of your return?" asked of you, read by Schedule 1-A (forms/2025/s1a.yaml, s1a.line36a_senior). The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply counts any person's work SSN, so on a joint return your spouse's SSN answers for you. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,111 of 2,122 agree; 11 value; on returns the full interview completes: 3 value. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): the 3 are joint returns where only the spouse has a work SSN (generated 49, 150, 255): project no, candidate yes. Off completed returns: 8 of the same kind (5 incomplete, 3 refused). As ruled in the T-091 round. Project stands.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **AGREE**

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
{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Chosen reading: both the registered domestic partner fact and the community property state fact are true.

Ruling: model error; i1040gi p. 23, Community Property States: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner"; p501 p. 6 (registered domestic partners aren't lawfully married for federal tax purposes); p525 p. 24. The project line is unchanged by the T-091 correction (BUG-0267 adds household.test2_absence_persons, the gate household.hoh_absence and its refusal on household.hoh_eligible; no other household expression changed). The reply has the project's two answers but drops the not-joint condition, so it needs the answers from a joint filer and refuses a joint filer who answers yes to both, whose return already reports both spouses' income. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records; 2,122 comparisons): 2,113 of 2,122 agree; 9 candidate-unknown; on returns the full interview completes: 3 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): the 3 are partial records of joint returns withholding household.community_property (classm.s2.3.deepseek, classm.f8880.2, classm.f8995.2), where the project decides no from f1040.status. Off completed returns: 6 of the same kind (3 incomplete, 3 refused). As ruled in the T-091 round. Project stands.

## Raw second transcription

```yaml
lines:
  - id: household.h_person_count
    printed: "(helper)"
    label: "Number of person entries on the return"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one}
  - id: household.h_dependent_count
    printed: "(helper)"
    label: "Number of dependents listed on the return"
    type: Count
    expr: {op: sum_over, collection: dependent, field: dependent.one}
  - id: household.h_person_eic_fail_count
    printed: "(helper)"
    label: "Person entries without an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, ne: [person.eic_ssn, {const: true}]}
  - id: household.h_dep_eic_fail_count
    printed: "(helper)"
    label: "EIC qualifying children without an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - {op: test, eq: [dependent.eic_child, {const: true}]}
          - {op: test, ne: [dependent.eic_ssn, {const: true}]}
  - id: household.h_person_tin_fail_count
    printed: "(helper)"
    label: "Person entries without an SSN or ITIN issued by the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, ne: [person.tin, {const: true}]}
  - id: household.h_dep_tin_fail_count
    printed: "(helper)"
    label: "Dependents without an SSN, ITIN or ATIN issued by the due date"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, ne: [dependent.tin, {const: true}]}
  - id: household.h_person_work_count
    printed: "(helper)"
    label: "Person entries with an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}
  - id: household.h_ctc_work_fail_count
    printed: "(helper)"
    label: "CTC children without an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - {op: test, eq: [dependent.ctc_child, {const: true}]}
          - {op: test, ne: [dependent.work_ssn, {const: true}]}
  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Dependents satisfying the head of household parent test"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}
  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Dependents satisfying the head of household lived-with test"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}
  - id: household.h_hoh_eligible
    printed: "(helper)"
    label: "Head of household eligibility under Test 1 or Test 2"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.unmarried, {const: true}]}
        - op: test
          any:
            - {op: test, gt: [household.h_hoh_test1_count, {const: 0, type: Count}]}
            - op: test
              all:
                - {op: test, eq: [household.home_cost, {const: true}]}
                - {op: test, gt: [household.h_hoh_test2_count, {const: 0, type: Count}]}
  - id: household.h_roster_bad_count
    printed: "(helper)"
    label: "Claimed dependents who are neither qualifying children nor qualifying relatives"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - {op: test, eq: [dependent.claimed, {const: true}]}
          - op: test
            not:
              op: test
              any:
                - {op: test, eq: [dependent.qc_dependent, {const: true}]}
                - {op: test, eq: [dependent.qr_dependent, {const: true}]}
  - id: household.h_hsa_person_count
    printed: "(helper)"
    label: "Persons with at least one Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, gt: [person.hsa_forms, {const: 0, type: Count}]}
  - id: household.persons
    printed: "(helper)"
    label: "Number of persons in the tax family"
    type: Count
    expr: {op: sum, of: [household.h_person_count, household.h_dependent_count]}
    note: "Chosen reading: tax family size is the person entries plus the dependents listed."
  - id: household.roster_bad
    printed: "(helper)"
    label: "Any claimed dependent is not a qualifying child or qualifying relative"
    type: Bool
    expr: {op: test, gt: [household.h_roster_bad_count, {const: 0, type: Count}]}
    note: "Chosen reading: bad roster means at least one claimed dependent fails both dependent definitions."
  - id: household.hsa_both
    printed: "(helper)"
    label: "Both spouses have HSAs"
    type: Bool
    expr: {op: test, ge: [household.h_hsa_person_count, {const: 2, type: Count}]}
    note: "Chosen reading: both spouse person entries have at least one Form 8889."
  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of HSA allocations requiring equal division between spouses"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}
  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of HSA allocations using a different agreed allocation"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}
  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total family HSA contribution limit before spouse allocation"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}
  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total HSA contribution limit allocated to the persons on the return"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}
  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "Every person and EIC qualifying child has an SSN valid for the EIC"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.h_person_eic_fail_count, {const: 0, type: Count}]}
        - {op: test, eq: [household.h_dep_eic_fail_count, {const: 0, type: Count}]}
    note: "Chosen reading: taxpayer, spouse and each EIC qualifying child must have an EIC-valid SSN."
  - id: household.all_tin
    printed: "(helper)"
    label: "Every person and dependent has an SSN, ITIN or ATIN issued by the due date"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.h_person_tin_fail_count, {const: 0, type: Count}]}
        - {op: test, eq: [household.h_dep_tin_fail_count, {const: 0, type: Count}]}
    note: "Chosen reading: every person entry and every dependent must have a TIN issued by the return due date."
  - id: household.ctc_ssn
    printed: "(helper)"
    label: "Taxpayer or spouse has a work-valid SSN and every CTC child has a work-valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.taxpayer_work_ssn, {const: true}]}
        - {op: test, eq: [household.h_ctc_work_fail_count, {const: 0, type: Count}]}
    note: "Chosen reading: one spouse's work-valid SSN suffices for the taxpayer side; each CTC child must have one."
  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "At least one person on the return has an SSN valid for employment"
    type: Bool
    expr: {op: test, gt: [household.h_person_work_count, {const: 0, type: Count}]}
  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household status claimed but the tests are not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - {op: test, eq: [household.h_hoh_eligible, {const: false}]}
    note: "Chosen reading: Test 1 is carried by dependent.hoh_test1; Test 2 also requires household.home_cost."
  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse status claimed but the five tests are not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}
    note: "Chosen reading: failure is reported only when QSS status is actually claimed."
  - id: household.rdp_community_property
    printed: "(helper)"
    label: "Registered domestic partner in a community property state"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.rdp, {const: true}]}
        - {op: test, eq: [household.community_property, {const: true}]}
    note: "Chosen reading: both the registered domestic partner fact and the community property state fact are true."
```
