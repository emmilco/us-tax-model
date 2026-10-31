# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7d0ff1a29d2512bac17273d2cc50c6421e6477a74270ba05b652f1366c503bc6 |
| printed lines compared | 14 |
| agree / disagree / missing | 7 / 7 / 0 |
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
{"args": [{"args": [{"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "lt"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}
```

Second transcription's note: Read as an invalid roster: not exactly one taxpayer, more than one spouse, or a spouse entry when the filer reports not married.

Ruling: model error; f1040 p. 1, "Your first name and middle initial" and "If joint return, spouse's first name and middle initial"; i1040gi p. 13, Married Filing Jointly: "You were married at the end of 2025, even if you didn't live with your spouse at the end of 2025" or "Your spouse died in 2025 and you didn't remarry in 2025". The line checks the person entries against the filing status. The new reply (its round-4 reply read claimed_no_tin) checks exactly one taxpayer entry, at most one spouse entry, and no spouse entry when household.married is no; it never reads f1040.status. So it accepts a joint return without a spouse entry and a return not filed jointly with one (where household.married is yes), refuses a joint return whose filer answered married no, and needs household.married from every filer. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,060 of 2,096 agree; 18 value, 11 project-unknown, 6 candidate-unknown, 1 project-refuses; on returns the full interview completes: 7 value, 3 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): the 7 values are classm fixtures filed jointly with a spouse entry whose household.married answer is no (classm.f8995.2, classm.ira.2, classm.se.2, classm.sli.4, classm.ssb.4, classm.tcw.1, classm.tcw.15; project no, candidate yes), an answer that contradicts the joint status the return claims and that the candidate reads in place of the status; the 3 candidate-unknown are partial records of joint returns withholding household.married (classm.f5695.3.deepseek, classm.f5695.13, classm.f8880.3), which the project decides from f1040.status. Off completed returns: 10 refused values of the same kind (classm.asset.1, classm.otjob.1, classm.s1a.1 and others); stage13.refuse.joint_without_spouse (project yes, candidate no), the roster mismatch the line exists for; 3 refused partial records withholding household.married; 11 project-unknown fixtures without person.under16 and audit.household.filer_under16 (the owner's entry check, amb.2025.filer_under_16). Project stands.

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

Second transcription's note: Read as at least two person entries having HSA forms.

Ruling: representation; i8889 p. 4: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you." The reply now tests at least two people with a Form 8889 (the Claude reply's test), where the project tests exactly two; household.roster_bad admits at most two person entries, so the tests coincide. Its round-4 reply summed Forms 8889 across persons. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,096 of 2,096 agree; no difference (observed equivalence on that sample). Project stands.

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
{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "le"}
```

Second transcription's note: Read as at least one person has an SSN valid for employment, as the CTC rule requires only one spouse on a joint return to have it.

Ruling: model error; i1040gi p. 17, Before you begin: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)." The new reply tests only that at least one person has an SSN valid for employment and drops the other spouse's SSN-or-ITIN test (its round-4 reply had that test and counted an applied-for ITIN; ruled ambiguity). executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,095 of 2,096 agree; 1 value; on returns the full interview completes: 1 value. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): the one difference is stage13.ctc_spouse_no_id, a joint return whose taxpayer has a work SSN and whose spouse has neither an SSN nor an ITIN (person.tin no, work_ssn no): project no, candidate yes. The source's second sentence decides it for the project. As ruled for the round-2 reply, which omitted the same test. Project stands.

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "eq"}
```

Ruling: representation; i1040gi p. 18, Step 3, question 4, asked of you. The reply counts taxpayer entries with work_ssn yes and tests the count equal to 1, where the project tests it above 0; household.roster_bad refuses any return without exactly one taxpayer entry, so the tests coincide. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,096 of 2,096 agree; no difference (observed equivalence on that sample). Project stands.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}
```

Second transcription's note: Read as not meeting unmarried or considered-unmarried status, the home-cost test, and at least one dependent HOH test.

Ruling: model error; i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; Test 1: "Your parent didn't have to live with you". The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only): it never reads f1040.status, so it fails every return that is not head of household, and it requires household.home_cost for Test 1. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 552 of 2,096 agree; 1,409 value, 68 candidate-refuses, 62 candidate-unknown, 3 project-refuses, 2 project-unknown; on returns the full interview completes: 561 value, 7 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): 561 value, project no and candidate yes: 559 returns that are not head of household (385 single, 150 joint, 24 qualifying surviving spouse; for example classm.s3.2.deepseek) and 2 head of household returns that qualify under Test 1 with home_cost no (stage8.hoh.parent.test1, generated 381); 7 candidate-unknown: 4 dependent.born_died, which the project asks only on a head of household return (classm.f8962.5 and .deepseek, generated 22, 361), and 3 partial records withholding home_cost or unmarried (classm.f8863.2.deepseek twice, classm.aqee.2.deepseek). Project stands.

### household.qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}
```

Ruling: model error; i1040gi p. 15, Qualifying Surviving Spouse: "You can check the 'Qualifying surviving spouse' box ... if all of the following apply". The reply's test is the one ruled in fix round 4 (qss_eligible eq false where round 4 had ne true, the same test on a Bool answer); the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only): it drops the f1040.status test, so it needs household.qss_eligible from every filer, where the project asks it only of a qualifying surviving spouse. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 590 of 2,096 agree; 1,506 candidate-unknown; on returns the full interview completes: 616 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): all 616 are household.qss_eligible asked of a filer whose status is not qss (341 single, 144 joint, 131 head of household; for example classm.f2441.1.deepseek); no value difference. Project stands.

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

Ruling: model error; i1040gi p. 23, Community Property States: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner"; p501 p. 6 (registered domestic partners aren't lawfully married for federal tax purposes); p525 p. 24. The reply's expression is identical to the one ruled in fix round 4; the project line is unchanged (BUG-0260 rewords household.home_cost and household.qss_eligible only). Like its round-4 reply, it has the project's two answers (community property state and registered domestic partner) but drops the not-joint condition, so it needs household.rdp from a joint filer in a community property state, whose return already reports both spouses' income and whom the source's partner rule does not reach, and refuses such a filer who answers yes. executable-triage-v2 (`reviews/2025/transcription/triage/household.deepseek.json`; 1,390 fixtures, 500 generated returns seed 20261026, 206 partial records; 2,096 comparisons): 2,087 of 2,096 agree; 9 candidate-unknown; on returns the full interview completes: 3 candidate-unknown. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly; scratch /tmp/adj-fixr5-household-refund/household.deepseek.full.json; the uncapped rerun reproduces the recorded counts exactly): the 3 are partial records of joint returns withholding household.community_property (classm.f5695.3.deepseek, classm.f5695.13, classm.f8880.3), where the project decides no from f1040.status. Off completed returns: 3 refused partial records of the same kind and 3 stage16.hsa fixtures without household.rdp. Project stands.

## Raw second transcription

```yaml
lines:
  - id: household.persons
    printed: "(helper)"
    label: "Number of persons on the return"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one}

  - id: household.roster_bad
    printed: "(helper)"
    label: "Person roster is invalid"
    type: Bool
    expr: {op: test, any: [{op: test, ne: [household.h_taxpayer_count, {const: 1, type: Count}]}, {op: test, gt: [household.h_spouse_count, {const: 1, type: Count}]}, {op: test, all: [{op: test, gt: [household.h_spouse_count, {const: 0, type: Count}]}, {op: test, eq: [household.married, {const: false}]}]}]}
    note: "Read as an invalid roster: not exactly one taxpayer, more than one spouse, or a spouse entry when the filer reports not married."

  - id: household.hsa_both
    printed: "(helper)"
    label: "Both taxpayer and spouse have HSA forms"
    type: Bool
    expr: {op: test, ge: [household.h_hsa_persons_count, {const: 2, type: Count}]}
    note: "Read as at least two person entries having HSA forms."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Count of HSA forms under equal allocation"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Count of HSA forms under an agreed allocation"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total HSA Step 1 family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total allocated HSA family contribution share"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}

  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "All persons have an SSN valid for the EIC"
    type: Bool
    expr: {op: test, eq: [household.h_eic_ssn_count, household.persons]}

  - id: household.all_tin
    printed: "(helper)"
    label: "All persons have a TIN or a timely TIN application"
    type: Bool
    expr: {op: test, eq: [household.h_tin_count, household.persons]}

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "At least one person has an SSN valid for employment for the CTC"
    type: Bool
    expr: {op: test, ge: [household.h_work_ssn_count, {const: 1, type: Count}]}
    note: "Read as at least one person has an SSN valid for employment, as the CTC rule requires only one spouse on a joint return to have it."

  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "Taxpayer has an SSN valid for employment"
    type: Bool
    expr: {op: test, eq: [household.h_taxpayer_work_count, {const: 1, type: Count}]}

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household tests fail"
    type: Bool
    expr: {op: test, not: {op: test, all: [{op: test, eq: [household.unmarried, {const: true}]}, {op: test, eq: [household.home_cost, {const: true}]}, {op: test, gt: [household.h_hoh_dep_count, {const: 0, type: Count}]}]}}
    note: "Read as not meeting unmarried or considered-unmarried status, the home-cost test, and at least one dependent HOH test."

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse tests fail"
    type: Bool
    expr: {op: test, eq: [household.qss_eligible, {const: false}]}

  - id: household.rdp_community_property
    printed: "(helper)"
    label: "Registered domestic partner in a community property state"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [household.rdp, {const: true}]}, {op: test, eq: [household.community_property, {const: true}]}]}

  - id: household.h_taxpayer_count
    printed: "(helper)"
    label: "Count of taxpayer entries"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, eq: [person.role, {const: "taxpayer"}]}}

  - id: household.h_spouse_count
    printed: "(helper)"
    label: "Count of spouse entries"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, eq: [person.role, {const: "spouse"}]}}

  - id: household.h_hsa_persons_count
    printed: "(helper)"
    label: "Count of persons with HSA forms"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, gt: [person.hsa_forms, {const: 0, type: Count}]}}

  - id: household.h_eic_ssn_count
    printed: "(helper)"
    label: "Count of persons with an SSN valid for the EIC"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, eq: [person.eic_ssn, {const: true}]}}

  - id: household.h_tin_count
    printed: "(helper)"
    label: "Count of persons with a TIN or timely TIN application"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, any: [{op: test, eq: [person.tin, {const: true}]}, {op: test, eq: [person.itin_applied, {const: true}]}]}}

  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Count of persons with an SSN valid for employment"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, eq: [person.work_ssn, {const: true}]}}

  - id: household.h_taxpayer_work_count
    printed: "(helper)"
    label: "Count of taxpayer entries with an SSN valid for employment"
    type: Count
    expr: {op: sum_over, collection: person, field: person.one, where: {op: test, all: [{op: test, eq: [person.role, {const: "taxpayer"}]}, {op: test, eq: [person.work_ssn, {const: true}]}]}}

  - id: household.h_hoh_dep_count
    printed: "(helper)"
    label: "Count of dependents meeting a head of household test"
    type: Count
    expr: {op: sum_over, collection: dependent, field: dependent.one, where: {op: test, any: [{op: test, eq: [dependent.hoh_test1, {const: true}]}, {op: test, eq: [dependent.hoh_test2, {const: true}]}]}}
```
